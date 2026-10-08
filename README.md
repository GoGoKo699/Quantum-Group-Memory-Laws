# Quantum-Group-Memory-Laws

## Boundary and bulk memory from a nonlocal spin symmetry

How much of a local spin's late-time memory is fixed by symmetry alone?

This repository records a spatial law for the **complete transverse symmetry contribution** in an open spin-$\tfrac12$ chain with real quantum-group deformation. Relative to ordinary $SU(2)$, the deformed symmetry enhances the unavoidable end-spin memory while suppressing the bulk contribution. These are overlaps with a conserved operator algebra, not an encoded-memory lifetime or a hydrodynamic decay exponent.

With the ordinary infinite-temperature trace,

$$
M_{L,i}(q)=2^{-L}\|\Pi_q(X_i)\|_{\mathrm{HS}}^2,
\qquad C_i(t)=2^{-L}\operatorname{Tr}[X_i(t)X_i].
$$

Here $\Pi_q$ projects onto the **whole quantum-group symmetry algebra**, including products of its generators. A symmetry-preserving Hamiltonian obeys $\overline C_i\ge M_{L,i}$; its full plateau need not equal this contribution.

| Regime | Complete symmetry contribution |
|---|---|
| Ordinary symmetry, $q=1$ | $M_{L,i}=1/L$ at every site. |
| End spin, every fixed finite $q>1$ | $M_{L,1}=\tanh(\log q)/\sqrt{2\pi L}+O_q(L^{-1})$. |
| Bulk, $i/L\to x\in(0,1)$ and fixed $q>q_0$ | $M_{L,i}=\mathcal K(q)\mathcal F(x)L^{-2}[1+o(1)]$. |

The sufficient bulk proof threshold is $q_0=2.0810189966\ldots$. It is **not a physical transition**. The positive amplitude and normalized spatial profile are explicitly defined in the [theorem](research/THEOREM.md). The limits are not uniform as $q\to1$ or as the observation site approaches a boundary.

A specified local, noise-averaged bond-kick model attains this contribution exactly, even with a Hamiltonian preserving the full algebra. The finite-size relaxation bound contains a dissipative gap whose system-size scaling is not evaluated. The zero-noise and long-time limits must not be interchanged.

## Reading map

| Start here | What it contains |
|---|---|
| [Model and claims](research/MODEL_AND_CLAIMS.md) | Observable, trace, assumptions, and the distinction between established claims and nonclaims. |
| [Theorem](research/THEOREM.md) and [proof map](research/PROOF_MAP.md) | Finite recursion, edge/bulk laws, explicit amplitudes, and the complete proofs. |
| [Local realization](research/LOCAL_REALIZATION.md) | Symmetry-preserving interactions plus unrecorded local noise. |
| [Hamiltonian plateau dictionary](research/PLATEAU_DICTIONARY.md) | Exact excess beyond symmetry and the explicitly nonlocal random-eigenbasis benchmark. |
| [Contribution review](research/CONTRIBUTION_REVIEW.md) and [attribution](literature/ATTRIBUTION.md) | Inherited methods, the additional implication, and source-access limits. |
| [Verification](VERIFICATION.md) | How to rerun the unchanged scientific checks and inspect exact-revision evidence. |

The complete-commutant projection principle, representation theory, orthogonal-polynomial formulas, and stationary-commutant mechanism are inherited. The contribution under assessment is their evaluated **physical multiplicity trace and uniform finite-deformation spatial asymptotics**. Internal reproduction is not independent proof review or exhaustive originality certification.

## Reproduce

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tools/verify.py --output build/verification
```

The checks use small physical Hilbert spaces and polynomial-size recurrence arrays. They do not establish an asymptotic theorem by fitting finite-size data. The original failed attempts, exact checkers, and reference reports are retained in a [discrete archive](archive/README.md).

## Workspace

[WORKSPACE.md](WORKSPACE.md) and [the current work order](work_orders/CURRENT.md) define takeover at the fixed scientific scope. See [AGENTS.md](AGENTS.md) before edits. Other research projects are outside this repository's authorization.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## License

The owner's original [MIT license](LICENSE) is preserved. Linked third-party papers are not redistributed or relicensed by this repository.
