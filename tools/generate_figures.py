#!/usr/bin/env python3
"""Regenerate the spatial-memory figures from preserved numerical routines.

python tools/generate_figures.py --output build/figures
python tools/generate_figures.py --check --output build/figure-check

The sole maintained point dataset is figures/spatial_memory.json. Regeneration
writes a candidate dataset, two SVGs and a calculation receipt outside source.
Check mode compares a fresh calculation to the maintained dataset with the
repository's fixed report tolerances, then renders the maintained values to
check the SVGs without amplifying harmless cross-runtime numerical roundoff.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from pathlib import Path
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FuncFormatter
import numpy as np
import scipy

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import check_foundations as foundations
from tools.verify import (ARCHIVE, REPORT_ATOL, REPORT_RTOL, compare_reports,
                          output_location, revision, source_files)

HANDOFF = ROOT / ARCHIVE
sys.path[:0] = [str(HANDOFF / 'prior/prior/prior'),
               str(HANDOFF / 'prior/prior/prior/prior')]
grid = foundations.archived_module('figure_grid', 'prior/prior/prior/fast_grid.py')
edge = foundations.archived_module('figure_edge', 'prior/prior/prior/check_asymptotics.py')
bulk = foundations.bulk
memory = foundations.memory

DATA_NAME = 'spatial_memory.json'
SVG_NAMES = ('end_center_memory.svg', 'normalized_interior_profile.svg')
SOURCE_PATHS = (
    'tools/generate_figures.py', 'tools/check_foundations.py', 'tools/verify.py',
    'requirements.txt', 'requirements-figures.txt',
    ARCHIVE + '/prior/prior/prior/fast_grid.py',
    ARCHIVE + '/prior/prior/bulk_tools.py',
    ARCHIVE + '/prior/prior/prior/check_asymptotics.py',
    ARCHIVE + '/prior/prior/prior/prior/check_memory.py',
    ARCHIVE + '/prior/prior/prior/report.json',
)
SETTINGS = {
    'figure_a': {'q': 2.6, 'lengths': [10, 20, 40, 80, 160, 320, 640],
                 'sites': ['1', 'L/2'], 'curve_points': 241},
    'figure_b': {'L': 160, 'q_values': [2.6, 3.5],
                 'base_sites': [16, 32, 40, 48, 64, 80],
                 'reflection': 'i -> L + 1 - i', 'x_coordinate': 'i/L',
                 'curve_domain': [0.09, 0.91], 'curve_points': 257},
    'arithmetic': 'IEEE-754 binary64 floating-point evaluations; no certified intervals',
    'recurrence': 'complete finite-size recurrence; no sector cutoff',
    'amplitudes': 'analytical formulas; no fitted exponent or amplitude',
    'profile_quadrature': {'epsabs': 2e-12, 'epsrel': 2e-12,
                           'source': 'bulk_tools.shape'},
    'q_product_tail_criterion': 'abs(t)/(1-z) <= 1e-17 in bulk_tools.logpoch',
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def input_hashes():
    return {name: digest(ROOT / name) for name in SOURCE_PATHS}


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True, allow_nan=False) + '\n')


def calculate():
    """Compute each displayed point and independent checks without fitting."""
    values = {}
    identity_checks = []
    report_differences = []

    def finite(length, site, q):
        key = (length, site, q)
        if key not in values:
            value = float(grid.fast(length, site, q))
            assert math.isfinite(value) and 0 < value <= 1, key
            values[key] = value
        return values[key]

    def identity(name, actual, independent, inputs):
        error = abs(actual-independent)
        assert math.isfinite(error) and error < foundations.TOL, (name, inputs, error)
        identity_checks.append({'check': name, 'inputs': inputs, 'value': actual,
                                'independent_value': independent,
                                'absolute_difference': error,
                                'tolerance': foundations.TOL})

    archive_report = json.loads((HANDOFF / 'prior/prior/prior/report.json').read_text())
    saved = {r['L']: r for r in archive_report['finite_q_diagnostics']['values']}
    q = SETTINGS['figure_a']['q']
    coefficient_edge = edge.edge_coefficient(q)
    coefficient_bulk = bulk.multiplier(q)*bulk.shape(.5)
    assert bulk.criterion(q) < 1
    figure_a = []
    for length in SETTINGS['figure_a']['lengths']:
        end = finite(length, 1, q)
        center = finite(length, length//2, q)
        row = {'L': length, 'q': q, 'edge_site': 1, 'center_site': length//2,
               'edge': end, 'center': center, 'undeformed': 1/length,
               'edge_asymptote': coefficient_edge/math.sqrt(length),
               'center_asymptote': coefficient_bulk/length**2}
        if length in saved:
            row['archived_reference'] = (
                ARCHIVE + '/prior/prior/prior/report.json#finite_q_diagnostics.values'
                + '[L=' + str(length) + ',q=2.6]')
            for field, old_field in (('edge', 'M_edge'), ('center', 'M_bulk')):
                report_differences += compare_reports(
                    saved[length][old_field], row[field], f'archive.L{length}.{field}')
        figure_a.append(row)
        identity('edge recurrence versus closed sum', end, edge.edge_exact(length,q),
                 {'L': length, 'q': q, 'i': 1})
    curve_a = []
    for length in np.geomspace(10., 640., SETTINGS['figure_a']['curve_points']):
        length = float(length)
        curve_a.append({'L': length, 'undeformed': 1/length,
                        'edge_asymptote': coefficient_edge/math.sqrt(length),
                        'center_asymptote': coefficient_bulk/length**2})

    length = SETTINGS['figure_b']['L']
    sites = sorted(set(SETTINGS['figure_b']['base_sites']) |
                   {length+1-i for i in SETTINGS['figure_b']['base_sites']})
    figure_b = []
    for q in SETTINGS['figure_b']['q_values']:
        assert bulk.criterion(q) < 1
        center = finite(length, length//2, q)
        for site in sites:
            value = finite(length, site, q)
            figure_b.append({'L': length, 'q': q, 'i': site, 'reflected_i': length+1-site,
                             'x': site/length, 'memory': value,
                             'center_memory': center, 'ratio': value/center})
        for site in SETTINGS['figure_b']['base_sites']:
            identity('finite-chain reflection', finite(length, site, q),
                     finite(length, length+1-site, q),
                     {'L': length, 'q': q, 'i': site, 'reflected_i': length+1-site})
    lo, hi = SETTINGS['figure_b']['curve_domain']
    curve_x = [float(x) for x in np.linspace(lo, hi, SETTINGS['figure_b']['curve_points'])]
    # Check all plotted curve abscissae and every finite-size sample abscissa.
    profile_values = {}
    for x in sorted(set(curve_x + [site/length for site in sites] + [.5])):
        quadrature = bulk.shape(x)
        identity('profile quadrature versus elementary expression', quadrature,
                 foundations.profile_elementary(x), {'x': x})
        profile_values[x] = quadrature
    curve_b = [{'x': x, 'profile': profile_values[x],
                'normalized_profile': profile_values[x]/profile_values[.5]} for x in curve_x]

    for q in SETTINGS['figure_b']['q_values']:
        for site in (1, 5, 10):
            identity('vectorized versus original recurrence', finite(10, site, q),
                     memory.complete_bound_fast(10, site, q), {'L': 10, 'q': q, 'i': site})
        for site in (1, 2, 4):
            projected, _ = memory.project_schur(memory.embed1(memory.X, site-1, 4), 4, q)
            dense = float(np.vdot(projected, projected).real/2**4)
            identity('recurrence versus dense physical projection', finite(4, site, q),
                     dense, {'L': 4, 'q': q, 'i': site})

    data = {
        'schema': 1,
        'settings': SETTINGS,
        'calculation_source_sha256': input_hashes(),
        'methods': {
            'finite_points': ARCHIVE + '/prior/prior/prior/fast_grid.py:fast(L,i,q)',
            'edge_asymptote': ARCHIVE + '/prior/prior/prior/check_asymptotics.py:edge_coefficient(q)/sqrt(L)',
            'center_asymptote': ARCHIVE + '/prior/prior/bulk_tools.py:multiplier(q)*shape(1/2)/L**2',
            'limiting_profile': ARCHIVE + '/prior/prior/bulk_tools.py:shape(x)/shape(1/2)',
            'undeformed': 'exact 1/L',
        },
        'coefficients': {'q': 2.6, 'edge': coefficient_edge, 'center': coefficient_bulk,
                         'edge_to_center_ratio': coefficient_edge/coefficient_bulk,
                         'F_center': profile_values[.5],
                         'K': bulk.multiplier(2.6)},
        'figure_a': {'finite_points': figure_a, 'analytical_curves': curve_a},
        'figure_b': {'finite_points': figure_b, 'analytical_curve': curve_b},
    }
    checks = {'passed': True, 'identity_checks': identity_checks,
              'max_absolute_identity_difference': max(r['absolute_difference'] for r in identity_checks),
              'archived_report_numeric_differences': report_differences,
              'report_comparison_tolerances': {'atol': REPORT_ATOL, 'rtol': REPORT_RTOL},
              'asymptotic_agreement_used_as_pass_condition': False}
    return data, checks


def render(data, output):
    """Render only the supplied dataset; fixed SVG IDs and no clock metadata."""
    plt.rcParams.update({
        'font.family': 'DejaVu Sans', 'font.size': 11,
        'axes.titlesize': 16, 'axes.labelsize': 12,
        'axes.spines.top': False, 'axes.spines.right': False,
        'axes.edgecolor': '#536273', 'axes.labelcolor': '#24364b',
        'xtick.color': '#536273', 'ytick.color': '#536273',
        'text.color': '#24364b', 'svg.fonttype': 'path',
        'svg.hashsalt': 'quantum-group-memory-laws-spatial-figures-v1',
    })
    colors = {'edge': '#1766a5', 'center': '#cf641e', 'reference': '#677482'}

    def save(fig, filename, title, description):
        fig.savefig(output / filename, format='svg', facecolor='white', metadata={
            'Date': None, 'Creator': 'tools/generate_figures.py',
            'Title': title, 'Description': description,
        })
        plt.close(fig)

    rows = data['figure_a']['finite_points']
    curves = data['figure_a']['analytical_curves']
    lengths = [r['L'] for r in curves]
    fig, ax = plt.subplots(figsize=(8.2, 5.8))
    fig.subplots_adjust(left=.125, right=.97, bottom=.14, top=.87)
    ax.set_xscale('log'); ax.set_yscale('log')
    ax.plot(lengths, [r['undeformed'] for r in curves], color=colors['reference'],
            lw=1.6, linestyle=':', label=r'Undeformed: $1/L$ (exact)')
    ax.plot(lengths, [r['edge_asymptote'] for r in curves], color=colors['edge'],
            lw=1.8, linestyle='--', label=r'End asymptote: $\tanh(\log q)/\sqrt{2\pi L}$')
    ax.plot(lengths, [r['center_asymptote'] for r in curves], color=colors['center'],
            lw=1.8, linestyle='--', label=r'Center asymptote: $\mathcal{K}(q)\mathcal{F}(1/2)L^{-2}$')
    ax.plot([r['L'] for r in rows], [r['edge'] for r in rows], linestyle='none',
            marker='o', ms=6.5, color=colors['edge'], label=r'End: $M_{L,1}$ (recurrence)')
    ax.plot([r['L'] for r in rows], [r['center'] for r in rows], linestyle='none',
            marker='s', ms=6, color=colors['center'], label=r'Center: $M_{L,L/2}$ (recurrence)')
    ax.set_xlim(8.5, 760); ax.set_ylim(1.5e-5, .2)
    ax.xaxis.set_major_locator(FixedLocator(data['settings']['figure_a']['lengths']))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda value, _: f'{value:g}'))
    ax.xaxis.set_minor_locator(FixedLocator([]))
    ax.set_xlabel(r'Chain length $L$ (even)')
    ax.set_ylabel(r'Retained local fraction $M_{L,i}$')
    ax.set_title(r'End and center memory  |  $q=2.6$', loc='left', pad=18)
    ax.grid(axis='y', which='major', color='#e3e8ed', lw=.7)
    handles, labels = ax.get_legend_handles_labels()
    order = [3, 4, 0, 1, 2]
    ax.legend([handles[i] for i in order], [labels[i] for i in order],
              loc='lower left', frameon=True, facecolor='white', edgecolor='#dce3e9',
              framealpha=.96, fontsize=9.1)
    save(fig, SVG_NAMES[0], 'End and center memory at q=2.6',
         'Markers: floating-point evaluations of the complete finite-size recurrence. '
         'Curves: exact undeformed value and analytical leading asymptotes; no fitted parameters. '
         'Point data and provenance: spatial_memory.json.')

    rows = data['figure_b']['finite_points']
    curve = data['figure_b']['analytical_curve']
    fig, ax = plt.subplots(figsize=(8.2, 5.5))
    fig.subplots_adjust(left=.125, right=.97, bottom=.19, top=.86)
    ax.plot([r['x'] for r in curve], [r['normalized_profile'] for r in curve],
            color='#394855', lw=2, label=r'Analytical limit: $\mathcal{F}(x)/\mathcal{F}(1/2)$')
    for q, color, marker in ((2.6, colors['edge'], 'o'), (3.5, colors['center'], 'D')):
        selection = [r for r in rows if r['q'] == q]
        ax.plot([r['x'] for r in selection], [r['ratio'] for r in selection],
                linestyle='none', marker=marker, ms=6, markerfacecolor='white',
                markeredgewidth=1.6, color=color, label=rf'Recurrence: $q={q}$, $L=160$')
    ax.set_xlim(.075, .925)
    ax.set_ylim(.8, max(r['normalized_profile'] for r in curve)*1.07)
    ax.set_xlabel(r'Site coordinate $x=i/L$')
    ax.set_ylabel(r'$M_{L,i}(q)/M_{L,L/2}(q)$')
    ax.set_title('Normalized interior memory', loc='left', pad=18)
    ax.grid(axis='y', color='#e3e8ed', lw=.7)
    ax.legend(loc='upper center', frameon=True, facecolor='white', edgecolor='#dce3e9',
              framealpha=.96, fontsize=9.5)
    fig.text(.125, .045, r'Finite-chain reflection: $i\mapsto161-i$; every marker uses $x=i/160$.',
             fontsize=10, color='#536273')
    save(fig, SVG_NAMES[1], 'Normalized interior profile at L=160',
         'The limiting normalized profile is deformation-independent in the proved bulk domain. '
         'Markers are floating-point recurrence values at q=2.6 and q=3.5; '
         'finite-size corrections depend on q. Reflection uses i -> 161-i, with x=i/160. '
         'Point data and provenance: spatial_memory.json.')


def run(output, check=False):
    output = output_location(output)
    output.mkdir(parents=True, exist_ok=True)
    source_before = source_files(ROOT)
    before = input_hashes()
    data, validations = calculate()
    write_json(output / DATA_NAME, data)
    render_data = data
    differences = []
    if check:
        maintained = json.loads((ROOT / 'figures' / DATA_NAME).read_text())
        differences = compare_reports(maintained, data, 'figure_data')
        render_data = maintained
    render(render_data, output)
    svg_checks = {}
    for name in SVG_NAMES:
        svg_checks[name] = {'sha256': digest(output/name)}
        if check:
            same = (output/name).read_bytes() == (ROOT/'figures'/name).read_bytes()
            svg_checks[name]['matches_render_of_maintained_data'] = same
            assert same, f'{name}: maintained SVG differs from the rendering of maintained data'
    assert input_hashes() == before, 'Calculation inputs changed during figure generation'
    assert source_files(ROOT) == source_before, 'Source changed during figure generation'
    receipt = {
        'checked_commit': revision(), 'mode': 'check' if check else 'regenerate',
        'environment': {'python': platform.python_version(), 'numpy': np.__version__,
                         'scipy': scipy.__version__, 'matplotlib': matplotlib.__version__},
        'source_sha256': source_before, 'calculation_source_sha256': before,
        'source_integrity': True, 'calculation_source_integrity': True, 'settings': SETTINGS,
        'candidate_data_sha256': digest(output/DATA_NAME),
        'displayed_data_sha256': digest(ROOT/'figures'/DATA_NAME) if check else digest(output/DATA_NAME),
        'displayed_point_provenance': {'data_file': DATA_NAME, 'methods': render_data['methods'],
                                      'figure_a': render_data['figure_a'], 'figure_b': render_data['figure_b']},
        'validation': validations,
        'maintained_data_numeric_differences': differences,
        'svg_checks': svg_checks,
        'passed': True,
    }
    write_json(output/'receipt.json', receipt)
    return {'passed': True, 'mode': receipt['mode'], 'output': str(output),
            'identity_checks': len(validations['identity_checks']),
            'max_identity_difference': validations['max_absolute_identity_difference'],
            'maintained_data_numeric_differences': len(differences)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('build/figures'))
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    print(json.dumps(run(args.output, args.check), sort_keys=True))
