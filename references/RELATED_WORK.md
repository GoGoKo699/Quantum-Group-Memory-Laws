# Physical-loss results and their predecessors

The [spatial attribution account](../literature/ATTRIBUTION.md) documents the complete-algebra projection, evaluated local-memory laws, stationary dynamics and spectral inputs. This page compares the additional physical-erasure theorem at the level of channels and operational claims. The single educational anchor remains [Watrous 2018](../learning/WATROUS_BRIDGE.md).

## Ordinary Schur and symmetric-loss tools

[Quantum Permutation Noise Limits](https://github.com/GoGoKo699/Quantum-Permutation-Noise-Limits/tree/230ef8c5af1508f5ec2e13970c84ec2d8e0d2d36) establishes the physical ordinary-permutation benchmark. Its all-spin reduction is a reference-stable channel identity using symmetric spin blocks, singlet padding and permutation covariance of identical local noise. Its flagged-erasure capacities are exact. The symmetric partial-trace resource, separable comparison and irreducible-sector simulation are inherited from Stefano Pirandola, [arXiv:2610.06832v3](https://arxiv.org/html/2610.06832v3), Appendices B and G.

Those ingredients are credited as prior results. At finite $`r\gt1`$, the physically embedded local-loss channel lacks the needed ordinary permutation covariance. The [two- and three-site Choi spectra](../science/small_sectors.md) directly demonstrate this obstruction. An equality of abstract algebra blocks does not extend the symmetric-loss simulation to that physical channel.

## Deformed symmetric states and physical inner products

Raveh and Nepomechie, [*q-analog qudit Dicke states*, arXiv:2308.08392v2](https://arxiv.org/html/2308.08392v2), Sections 3.1–3.2 and 4 with Appendix B, establish recursive constructions, weighted inversion formulas and contiguous Schmidt decompositions. These are representation-theoretic predecessors. Their deformation and basis convention must be translated to the symmetric coproduct used here. They do not establish the full stationary-projection channel's local-erasure capacity.

Ballesteros, Gutiérrez-Sagredo, de Ramón and Relancio, [*Deformations of the symmetric subspace of qubit chains*, arXiv:2503.23554v3](https://arxiv.org/html/2503.23554v3), Sections II–IV, develops ordinary and deformed symmetry. Sections V–VII construct deformed transpositions and a deformed Hilbert-space inner product. In particular, the changed adjoint and inner product in Eqs. (110)–(117) do not identify ordinary-physical-trace CPTP local-erasure channels. That work is a relevant algebraic comparison, rather than a physical loss-equivalence theorem for this model.

## Stationary coherent symmetry

Moudgalya and Motrunich, [arXiv:2108.10324v2](https://arxiv.org/abs/2108.10324v2), Sections II.A, II.B.3, V.C–D and VII.A–B, supplies the bond/commutant framework, representation structure and physical-trace projection principle. Li, Sala and Pollmann, [arXiv:2305.06918v1](https://arxiv.org/abs/2305.06918v1), Section V and Appendix B, supplies the inherited strong-symmetry stationary-coherence mechanism. The [local realization](../research/LOCAL_REALIZATION.md) specializes and checks it in the physical representation used here.

A stationary conserved algebra does not determine the quantum capacity after losing physical sites. Nor does a fixed-size stationary projection give a finite-time mixing law. The new erasure account retains those distinctions.

## Entanglement conversion and the adaptive converse

Takeoka, Guha and Wilde, [*The squashed entanglement of a quantum channel*, arXiv:1310.0129v3](https://arxiv.org/html/1310.0129v3), Definition 1 and Theorems 7 and 9, defines channel squashed entanglement and proves its upper bound on two-way quantum communication with arbitrary interleaved LOCC. The [capacity proof](../science/capacity.md) applies that established theorem after constructing a suitable measurement of the actual channel's complementary environment.

The one-excitation achievable bound uses the established one-way hashing inequality, with classical communication directed from receiver to reference holder. A primary source is Devetak and Winter, [*Distillation of secret key and entanglement from quantum states*, arXiv:quant-ph/0306078](https://arxiv.org/abs/quant-ph/0306078). The finite-deformation physical code and its pattern-conditioned amplitude-damping reduction identify the resource to which that inequality is applied.

## Contribution and limits

The additional result proved here is the first-erased-mismatch estimate, uniform over physical chain length, irrep, multiplicity path and logical prior, and its direct reference-stable translation to the full projection's complementary channel. It proves that a finite size-independent two-way-capacity ceiling survives every fixed finite real deformation greater than one. A simple physical code also gives a positive size-independent achievable rate.

The theorem does not supply exact finite-deformation capacities, a sharp ceiling, parameter crossovers uniform in size, or a mixing-time account. The nearest-source comparison above identifies material inherited inputs and model differences; it is not an exhaustive priority claim.
