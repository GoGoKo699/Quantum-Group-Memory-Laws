#!/usr/bin/env python3
"""Supplementary finite checks of the explicit manuscript foundations.

Independent formulations check normalization, the elementary bulk profile,
local reflections and the free convolution. These checks do not prove uniform
asymptotics, generic Hamiltonian saturation or a deformed relaxation rate.
The original five scientific suites and their reference reports are untouched.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
import math
import os
from pathlib import Path
import platform
import sys

import numpy as np
import scipy
from scipy.linalg import eigh, expm

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.verify import ARCHIVE, output_location, revision, source_files

TOL = 1e-10


def archived_module(name, relative_path):
    spec = importlib.util.spec_from_file_location(name, ROOT / ARCHIVE / relative_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


memory = archived_module('foundation_memory', 'prior/prior/prior/prior/check_memory.py')
bulk = archived_module('foundation_bulk', 'prior/prior/bulk_tools.py')


def checked_group(cases, errors):
    assert all(math.isfinite(value) and value < TOL for value in errors.values()), errors
    return {'passed': True, 'cases': cases, 'max_errors': errors, 'tolerance': TOL}


def profile_elementary(x):
    return ((math.sqrt(2-x)/x**1.5 + math.sqrt(1+x)/(1-x)**1.5)/(2*math.pi)
            + 3*math.sqrt(2)/(4*math.pi*math.sqrt(x*(1-x)))
            * (math.asinh(math.sqrt(2*x/(1-x)))
               + math.asinh(math.sqrt(2*(1-x)/x))))


def profile_checks():
    records = []
    for x in (.02, .1, .25, .5, .7, .98):
        elementary = profile_elementary(x)
        integral = bulk.shape(x)
        records.append({'x': x, 'elementary': elementary, 'quadrature': integral,
                        'absolute_error': abs(elementary-integral)})
    result = checked_group(len(records), {'profile': max(r['absolute_error'] for r in records)})
    result['records'] = records
    return result


def sector_checks():
    errors = dict(probability=0., spin_moment=0., recurrence=0., undeformed_sector=0.,
                  observable_normalization=0., undeformed_projection=0., orthogonality=0.)
    cases = 0
    for length in range(2, 6):
        dimension = 2**length
        for q in (1., 1.3, 2.6):
            groups = {}
            for (_, h), basis in memory.qschur(length, q).items():
                groups.setdefault(h, []).append(basis)
            full_basis = np.column_stack([b for bases in groups.values() for b in bases])
            errors['orthogonality'] = max(errors['orthogonality'], float(np.linalg.norm(
                full_basis.conj().T @ full_basis - np.eye(dimension))))
            probabilities = {}
            for h, bases in groups.items():
                k = (length-h)//2
                multiplicity = math.comb(length, k) - (math.comb(length, k-1) if k else 0)
                assert len(bases) == multiplicity
                probabilities[h] = (h+1)*multiplicity/dimension
            errors['probability'] = max(errors['probability'], abs(sum(probabilities.values())-1))
            errors['spin_moment'] = max(errors['spin_moment'], abs(sum(
                p*h*(h+2) for h, p in probabilities.items())-3*length))
            for site in range(length):
                operator = memory.embed1(memory.X, site, length)
                value = 0.
                for h, bases in groups.items():
                    average = sum(b.conj().T @ operator @ b for b in bases)/len(bases)
                    eta = float(np.vdot(average, average).real/(h+1))
                    assert -TOL <= eta <= 1+TOL
                    value += probabilities[h]*eta
                    if q == 1:
                        errors['undeformed_sector'] = max(errors['undeformed_sector'],
                            abs(eta-h*(h+2)/(3*length**2)))
                errors['recurrence'] = max(errors['recurrence'],
                    abs(value-memory.complete_bound_fast(length, site+1, q)))
                for local, initial, factor in ((memory.X, 1., 1.), (memory.sp, .5, .5),
                                               (2*memory.sp, 2., 2.), (memory.X/2, .25, .25)):
                    observable = memory.embed1(local, site, length)
                    projected, _ = memory.project_schur(observable, length, q)
                    norm = float(np.vdot(observable, observable).real/dimension)
                    retained = float(np.vdot(projected, projected).real/dimension)
                    errors['observable_normalization'] = max(errors['observable_normalization'],
                        abs(norm-initial), abs(retained-factor*value), abs(retained/norm-value))
                if q == 1:
                    projected, _ = memory.project_schur(operator, length, q)
                    collective = sum(memory.embed1(memory.X, j, length)
                                     for j in range(length))/length
                    errors['undeformed_projection'] = max(errors['undeformed_projection'],
                        float(np.linalg.norm(projected-collective)))
                cases += 1
    return checked_group(cases, errors)


def pauli_reflection(q):
    identity = np.eye(2)
    x, y, z = memory.X, memory.Y, memory.Z
    eta = math.log(q)
    return ((np.eye(4)+np.kron(z, z))/2
            + (np.kron(x, x)+np.kron(y, y))/(2*math.cosh(eta))
            - math.tanh(eta)*(np.kron(z, identity)-np.kron(identity, z))/2)


def dissipator(a, operator):
    square = a @ a
    return a @ operator @ a - (square @ operator + operator @ square)/2


def local_checks():
    errors = dict(hecke=0., reflection=0., symmetry=0., dissipator=0.,
                  walk_closure=0., walk_evolution=0., stationary_projection=0., memory=0.)
    cases = 0
    for q in (1., 1.2, 2.6, 10.):
        u = pauli_reflection(q)
        e = q*np.eye(4)-memory.local_R(q)
        p = e/(q+1/q)
        errors['hecke'] = max(errors['hecke'], float(np.linalg.norm(u-(np.eye(4)-2*p))))
        errors['reflection'] = max(errors['reflection'], float(np.linalg.norm(u @ u-np.eye(4))))
        raising = memory.total_E(2, q)
        magnetization = np.kron(memory.Z, np.eye(2))+np.kron(np.eye(2), memory.Z)
        for generator in (raising, magnetization):
            errors['symmetry'] = max(errors['symmetry'], float(np.linalg.norm(u @ generator-generator @ u)))
        # Matrix units span every two-site operator, including non-Hermitian ones.
        for a in range(4):
            for b in range(4):
                operator = np.zeros((4, 4)); operator[a, b] = 1
                kick = u @ operator @ u-operator
                errors['dissipator'] = max(errors['dissipator'],
                    float(np.linalg.norm(kick-4*dissipator(p, operator))),
                    float(np.linalg.norm(kick-4*dissipator(e, operator)/(q+1/q)**2)))
                cases += 1
    for length, rates in ((3, (.4, 1.3)), (4, (.4, 1.3, 2.1))):
        dimension = 2**length
        generator = np.zeros((dimension**2, dimension**2), complex)
        walk = np.zeros((length, length))
        for j, rate in enumerate(rates):
            u = memory.embed2(pauli_reflection(1.), j, length)
            generator += rate*(np.kron(u.conj(), u)-np.eye(dimension**2))
            walk[j, j] -= rate; walk[j+1, j+1] -= rate
            walk[j, j+1] += rate; walk[j+1, j] += rate
        basis = np.column_stack([memory.embed1(memory.X, j, length).reshape(-1, order='F')
                                 for j in range(length)])
        errors['walk_closure'] = max(errors['walk_closure'], float(np.linalg.norm(generator @ basis-basis @ walk)))
        for time in (.37, 1.8):
            errors['walk_evolution'] = max(errors['walk_evolution'],
                float(np.linalg.norm(expm(time*generator) @ basis-basis @ expm(time*walk))))
            cases += 1
        eigenvalues, vectors = eigh(generator)
        stationary = vectors[:, abs(eigenvalues) < TOL]
        assert stationary.shape[1] == math.comb(length+3, 3)
        projected = stationary @ (stationary.conj().T @ basis)
        expected = np.repeat(basis.mean(axis=1, keepdims=True), length, axis=1)
        errors['stationary_projection'] = max(errors['stationary_projection'], float(np.linalg.norm(projected-expected)))
        errors['memory'] = max(errors['memory'], float(np.max(abs(np.sum(abs(projected)**2, axis=0)/dimension-1/length))))
    return checked_group(cases, errors)


def binomial_mass(n, k):
    return (Fraction(math.comb(n, (n+k)//2), 2**n)
            if abs(k) <= n and (n+k) % 2 == 0 else Fraction(0))


def adjacent(n, k):
    return binomial_mass(n, k)-binomial_mass(n, k+2)


def convolution_checks():
    cases = 0
    # Free regular polynomials: p_0=1 and p_1=2 cos(theta).
    for start, coefficients in ((0, {0: 1}), (1, {-1: 1, 1: 1})):
        state = [Fraction(int(r == start)) for r in range(18)]
        for n in range(15):
            for r in range(18):
                convolution = sum(c*adjacent(n, r+j) for j, c in coefficients.items())
                reflected = binomial_mass(n, r-start)-binomial_mass(n, r+start+2)
                assert state[r] == convolution == reflected
                cases += 1
            state = [(state[r-1] if r else Fraction(0))/2
                     + (state[r+1] if r+1 < len(state) else Fraction(0))/2 for r in range(18)]
    for n in range(15):
        for k in range(-n-6, n+7):
            assert adjacent(n, k) == -adjacent(n, -k-2)
            if k >= -n and (k-n) % 2 == 0:
                assert adjacent(n, k) == Fraction(2*(k+1), n+k+2)*binomial_mass(n, k)
            cases += 1
        # The excluded index has a nonzero left side and a zero denominator.
        assert adjacent(n, -n-2) == -Fraction(1, 2**n)
    return {'passed': True, 'cases': cases, 'max_errors': {'exact_fraction_error': 0},
            'arithmetic': 'Exact rational arithmetic; n=0,...,14, both magnetic parities.'}


def run(output):
    output = output_location(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    before = source_files(ROOT)
    groups = {'elementary_profile': profile_checks(), 'sector_decomposition': sector_checks(),
              'local_reflection_and_undeformed_walk': local_checks(), 'free_jost_convolution': convolution_checks()}
    assert source_files(ROOT) == before, 'Source changed during supplementary verification'
    report = {'scope': __doc__, 'commit': revision(), 'github_sha': os.environ.get('GITHUB_SHA'),
              'event': os.environ.get('GITHUB_EVENT_NAME'), 'run_id': os.environ.get('GITHUB_RUN_ID'),
              'python': sys.version, 'platform': platform.platform(), 'numpy': np.__version__,
              'scipy': scipy.__version__, 'source_sha256': before, 'source_unchanged': True,
              'groups_passed': len(groups), 'groups': groups}
    output.write_text(json.dumps(report, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'groups_passed': len(groups), 'output': str(output)}))
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT/'build/foundations.json')
    run(parser.parse_args().output)
