# Quantum Group Memory Laws

**A nonlocal spin symmetry fixes different memory laws at the ends and in the bulk.**

How much of a local spin's late-time memory is fixed by symmetry alone?
For a fixed chain length, the conserved algebra has the same dimension at every
finite real $`q\ge1`$. Yet the part of a local transverse spin protected by that
algebra changes with position. Ordinary spin symmetry gives $`1/L`$ everywhere;
deformation gives an end contribution of order $`L^{-1/2}`$ and a bulk contribution
of order $`L^{-2}`$ in the proved regimes below.

| Read next | Purpose |
|---|---|
| [Tutorial bridge](research/TUTORIAL_BRIDGE.md) · [Physical mechanism](research/PHYSICAL_MECHANISM.md) | Learn from one external source, then follow the projection and sector explanation. |
| [Theorem](research/THEOREM.md) · [Proof map](research/PROOF_MAP.md) | Read the exact laws, constants, domains, and full proof dependencies. |
| [Model and claims](research/MODEL_AND_CLAIMS.md) · [Local realization](research/LOCAL_REALIZATION.md) | Check the physical trace, assumptions, and noise-averaged attainment. |
| [Contribution review](research/CONTRIBUTION_REVIEW.md) · [Attribution](literature/ATTRIBUTION.md) | Compare the evaluated spatial law with its inherited framework and predecessors. |
| [Verification](VERIFICATION.md) · [Scope and evidence](STATUS.md) | Reproduce the checks and inspect their evidential limits. |
| [LLM guide](llms.txt) · [Workspace](WORKSPACE.md) | Identify relevant questions and the authoritative reading route. |

## What symmetry protects

Use the ordinary infinite-temperature trace on $`L`$ physical spin-$`\tfrac12`$ sites.
For a local Pauli operator $`X_i`$, define

```math
M_{L,i}(q)=2^{-L}\|\Pi_q(X_i)\|_{\mathrm{HS}}^2,
\qquad C_i(t)=2^{-L}\mathrm{Tr}[X_i(t)X_i].
```

Here $`\Pi_q`$ projects onto the **whole quantum-group symmetry algebra**, including
products of its generators. The quantity $`M`$ measures the local operator's
squared overlap with that algebra.

A symmetry-preserving Hamiltonian obeys $`\overline C_i\ge M_{L,i}`$, where
$`\overline C_i`$ is the finite-chain infinite-time average. Its full time-averaged
memory can include the [Hamiltonian-specific excess](research/PLATEAU_DICTIONARY.md).
A specified local model with unrecorded, averaged bond kicks attains $`M`$ exactly
at fixed finite chain size and positive noise strength, even with a Hamiltonian
preserving the full algebra.

## The spatial memory laws

| Regime | Complete symmetry contribution |
|---|---|
| Ordinary symmetry, $`q=1`$ | $`M_{L,i}=1/L`$ at every site. |
| End spin, every fixed finite $`q>1`$ | $`M_{L,1}=\tanh(\log q)/\sqrt{2\pi L}+O_q(L^{-1})`$. |
| Bulk, $`i/L\to x\in(0,1)`$ and fixed $`q>q_0`$ | $`M_{L,i}=\mathcal K(q)\mathcal F(x)L^{-2}[1+o(1)]`$. |

The sufficient bulk proof threshold is $`q_0=2.0810189966\ldots`$. It is **not a
physical transition**. The amplitude and spatial profile are explicitly defined
in the [theorem](research/THEOREM.md). Both end and bulk contributions vanish as
the chain grows. The limits are not uniform as $`q\to1`$ or as the observation site
approaches a boundary.

Within the proved bulk domain, the ratio to the center contribution tends to
$`\mathcal F(x)/\mathcal F(1/2)`$, independently of $`q`$. Deformation changes the
leading bulk amplitude while preserving this normalized interior profile.

## Why position matters

Deformation changes the shape of the conserved operators while leaving the
algebra's dimension and physical sector weights unchanged. The sector explanation
in [physical mechanism](research/PHYSICAL_MECHANISM.md) connects the end and bulk
powers to the different local overlaps inside spin multiplets. The complete
large-chain equality rests on the uniform analytical proof.

The complete-commutant projection principle, representation theory,
orthogonal-polynomial formulas, and stationary-commutant mechanism are inherited.
The contribution under assessment is their evaluated **physical multiplicity
trace and uniform finite-deformation spatial asymptotics**. The
[contribution review](research/CONTRIBUTION_REVIEW.md) develops that distinction.

## One tutorial, then this result

The selected learning anchor is:

> S. Moudgalya and O. I. Motrunich, **Hilbert Space Fragmentation and Commutant Algebras**,
> *Physical Review X* **12**, 011050 (2022).
> [Author version, arXiv:2108.10324v2](https://arxiv.org/abs/2108.10324v2) ·
> [Published article](https://doi.org/10.1103/PhysRevX.12.011050)

Its pedagogical sections introduce conserved algebras and their contribution to
local memory. The [tutorial bridge](research/TUTORIAL_BRIDGE.md) selects the
sections, translates the notation, derives the physical-trace projection, and
checks the ordinary-symmetry result by hand. It then leads into the mechanism,
spatial theorem, proof, and local realization. The route assumes standard quantum
mechanics and linear algebra; the repository supplies the model-specific steps.

## Scope and evidence

The result uses an open physical spin-half chain, finite real $`q\ge1`$, and the
specified symmetric coproduct. The ordinary physical trace and multiplicities
are essential. The noisy attainment is averaged at fixed finite size; its
relaxation bound contains a dissipative gap whose system-size scaling is not
evaluated. The zero-noise and long-time limits must not be interchanged.

[Model and claims](research/MODEL_AND_CLAIMS.md) records the limit boundaries;
[attribution](literature/ATTRIBUTION.md) identifies inherited inputs and inspected
predecessors. Internal reproduction is not independent proof review or exhaustive
originality certification.

## Evidence and reproduction

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tools/verify.py --output build/verification
python tools/check_foundations.py --output build/verification/foundations.json
```

The checks use small physical Hilbert spaces and polynomial-size recurrence
arrays. They test identities and evaluations; fitting finite-size data does not
establish the asymptotic theorem. The original failed attempts, exact checkers,
and reference reports are retained in a [discrete archive](archive/README.md).
[Verification](VERIFICATION.md) explains unchanged scientific assertions,
reference comparisons, and exact-revision evidence.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

The [LLM guide](llms.txt) supplies relevant research questions, search phrases,
and direct links to authoritative files. [WORKSPACE.md](WORKSPACE.md) and
[the current work order](work_orders/CURRENT.md) govern continuation at the fixed
scientific scope; see [AGENTS.md](AGENTS.md) before edits.

Code is available under the owner's original [MIT license](LICENSE). Linked
third-party papers are not redistributed or relicensed by this repository.
