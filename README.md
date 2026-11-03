# Quantum Group Memory Laws

**A nonlocal spin symmetry changes the spatial memory profile, while fixed physical erasure still imposes a size-independent quantum-capacity ceiling.**

This project studies the full real-deformation symmetry projection of an open spin-half chain. It evaluates its protected local transverse-spin memory and determines how much coherent information can survive subsequent independent physical erasure. Both questions use the same ordinary-trace projection; their observables and proofs are different.

**Sister project:** [Quantum Permutation Noise Limits](https://github.com/GoGoKo699/Quantum-Permutation-Noise-Limits) establishes the ordinary-permutation endpoint, with exact flagged-erasure capacities and a Schur/symmetric-loss reduction. This repository owns the complete finite-deformation physical-erasure proof. The changed embedding alters local loss maps, so the extension needs a new argument rather than a global change of algebra basis.

## Physical erasure after the complete stationary projection

Write $`r\gt1`$ for fixed finite real deformation, $`0\lt p\lt1`$ for physical erasure probability, and

```math
\mathcal N_{n,r,p}=\mathcal E_p^{\otimes n}\circ\Pi_r.
```

Here $`\Pi_r`$ projects onto the **whole** represented symmetry algebra, including products of its generators. Erasure acts afterward on the original physical sites, with positions flagged to the receiver. The capacity is measured in qubits per complete $`n`$-site block.

```math
\boxed{
1-h_2(p/2)\le Q_2(\mathcal N_{n,r,p})
\le C(r,p)\lt\infty\qquad(n\ge1).}
```

The upper constant is independent of size and covers arbitrary encodings, reference-entangled inputs and adaptive protocols with unlimited two-way classical communication. It is nonsharp. At zero erasure the largest coherent sector instead carries $`\log_2(n+1)`$ qubits.

The proof begins with [exact conditional one-erasure maps](science/small_sectors.md). A [first-erased-mismatch estimate](science/first_mismatch.md) then bounds the uncertainty of a magnetic label uniformly over every Clebsch–Gordan path and every prior. A [direct complementary-channel argument](science/capacity.md) turns this into a squashed-entanglement ceiling for the full stationary channel. The existing Schur/symmetric-loss resource and adaptive squashed-entanglement converse are credited separately.

At $`r=1`$, projection is ordinary permutation twirling. The sister's exact benchmark is $`Q_2=\log_2(n+1)-\mathbb E\log_2(L+1)`$, with $`L\sim\mathrm{Bin}(n,p)`$, tending to $`-\log_2p`$. No equality with that formula is claimed at finite deformation.

## The spatial memory laws

The original spatial account uses $`q=r`$ and chain length $`L=n`$. With the ordinary physical trace,

```math
M_{L,i}(q)=2^{-L}\|\Pi_q(X_i)\|_{\mathrm{HS}}^2,
\qquad C_i(t)=2^{-L}\mathrm{Tr}[X_i(t)X_i],\quad C_i(0)=1.
```

The quantity $`M`$ is the local Pauli operator's squared overlap with the full algebra. A symmetry-preserving Hamiltonian obeys the finite-chain time-average bound $`\overline C_i\ge M_{L,i}`$; its own invariant operators can give additional memory. The specified local, unrecorded bond-kick dynamics attains $`M`$ as its stationary value at fixed finite size.

| Regime | Complete symmetry contribution |
|---|---|
| Ordinary symmetry, $`q=1`$ | $`M_{L,i}=1/L`$ at every site. |
| End spin, fixed finite $`q\gt1`$ | $`M_{L,1}=\tanh(\log q)/\sqrt{2\pi L}+O_q(L^{-1})`$. |
| Bulk, $`i/L\to x\in(0,1)`$, fixed $`q\gt q_0`$ | $`M_{L,i}=\mathcal K(q)\mathcal F(x)L^{-2}[1+o(1)]`$. |

The sufficient bulk proof threshold is $`q_0=2.0810189966\ldots`$; it is not a physical transition. The [theorem](research/THEOREM.md) defines the amplitude and profile and states the orders of limits. Both contributions vanish with size. Their fixed-deformation limits are not uniform near ordinary symmetry or a boundary.

Deformation changes local overlaps while leaving ordinary irrep dimensions and physical multiplicities fixed. In the proved bulk domain the ratio to the center approaches $`\mathcal F(x)/\mathcal F(1/2)`$, independently of deformation. The [physical mechanism](research/PHYSICAL_MECHANISM.md) and its two figures explain this sector geometry; the full equality rests on the uniform analytical proof.

## Read by question

| Question | Authoritative route |
|---|---|
| What are the physical channel, flags and rate convention? | [Physical-erasure model](science/model.md) |
| Why does the finite-deformation capacity ceiling survive? | [First-mismatch proof](science/first_mismatch.md), then [all-sector capacity theorem](science/capacity.md) |
| Why is a global algebra isomorphism insufficient? | [Small-sector maps](science/small_sectors.md), [interpretation](science/interpretation.md) |
| Why do local end and bulk memories have different powers? | [Physical mechanism](research/PHYSICAL_MECHANISM.md), [spatial theorem](research/THEOREM.md), [proof map](research/PROOF_MAP.md) |
| When is the projection the actual stationary channel? | [Local realization](research/LOCAL_REALIZATION.md), [plateau dictionary](research/PLATEAU_DICTIONARY.md) |
| Which results are inherited? | [Spatial attribution](literature/ATTRIBUTION.md), [physical-loss related work](references/RELATED_WORK.md) |
| How are identities and finite cases reproduced? | [Verification](VERIFICATION.md), [physical-loss checks](verification/README.md) |

The [science index](science/README.md) joins both reading routes. The [LLM guide](llms.txt) maps additional questions to exact sources.

## Learn from one source

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**, using the [author's manuscript](https://cs.uwaterloo.ca/~watrous/TQI/). The [Watrous bridge](learning/WATROUS_BRIDGE.md) translates its channel, reference, entropy, symmetry and capacity language into this physical model, including a two-site loss example. The [30-milestone map](learning/MILESTONES.md) has 12 background and 18 narrative targets spanning the spatial and operational accounts.

The project supplies the quantum-group representation and estimator derivations absent from the textbook. Primary research sources such as Moudgalya–Motrunich, Li–Sala–Pollmann and Takeoka–Guha–Wilde remain scholarly proof dependencies.

## Reproduce and interpret

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tools/verify.py --output build/verification
python tools/check_foundations.py --output build/verification/foundations.json
python verification/check_small_sectors.py --output build/verification/small_sectors.json
python verification/check_estimator.py --output build/verification/estimator.json
python verification/check_cg_amplitudes.py --output build/verification/cg_amplitudes.json
```

The immutable spatial handoff, original assertions and canonical reports are retained. New finite checks compare exact physical maps, signed CG amplitudes, estimator tails and arbitrary-prior posteriors. They support the analytical statements and do not replace uniform proofs or the established adaptive converse.

The stationary projection is the supplied channel. Implementing it at finite time requires a separate mixing-time and reference-stable channel-error account. Local autocorrelation is not a capacity estimate. The finite-$`r`$ capacity bound is not a sharp formula, a uniform deformation crossover, or a singular infinite-deformation limit.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

Code is available under the owner's original [MIT license](LICENSE). Linked third-party papers are not redistributed or relicensed by this repository.
