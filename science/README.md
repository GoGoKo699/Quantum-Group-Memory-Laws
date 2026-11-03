# Symmetry projection, local memory, and physical loss

The full quantum-group symmetry algebra protects a coherent register whose dimension grows with the chain. Its physical embedding also controls what happens when individual spins are lost. These are distinct questions: the projection of a local observable determines a memory contribution, while communication capacity requires reference-entangled inputs and arbitrary coding across independent channel uses.

This repository owns the complete finite-deformation physical-erasure proof. Its sister [Quantum Permutation Noise Limits](https://github.com/GoGoKo699/Quantum-Permutation-Noise-Limits) owns the ordinary-permutation benchmark, including exact flagged-erasure capacities and the Schur/symmetric-loss reduction. Their common channel at deformation one connects the two accounts. Each repository states its own model and operational conclusion.

## Physical-erasure account

| Read in order | Question answered |
|---|---|
| [Model and stationary channel](model.md) | Which physical trace, symmetry algebra, erasure flags and capacity convention are used? |
| [Exact small-sector maps](small_sectors.md) | How does erasing one physical site act before any asymptotic argument? |
| [First erased mismatch](first_mismatch.md) | Why can the environment estimate a logical magnetic label with size-independent uncertainty along every Clebsch–Gordan path? |
| [All-sector capacity theorem](capacity.md) | How does that classical estimate bound the complete channel on arbitrary references and adaptive protocols? |
| [Interpretation and limits](interpretation.md) | What changes with deformation, and what remains outside the theorem? |

## Spatial-memory account

The original spatial-memory results remain authoritative in `research/`:

| Scientific purpose | Route |
|---|---|
| Physical multiplicity projection and spatial mechanism | [Model and claims](../research/MODEL_AND_CLAIMS.md), [commutant background](../research/COMMUTANT_BACKGROUND.md), [physical mechanism](../research/PHYSICAL_MECHANISM.md) |
| Exact finite-size expression and uniform asymptotic laws | [Theorem](../research/THEOREM.md), [proof map](../research/PROOF_MAP.md), [kernel details](../research/KERNEL_DETAILS.md) |
| Symmetry contribution versus a Hamiltonian's additional memory | [Plateau dictionary](../research/PLATEAU_DICTIONARY.md) |
| Specified local dynamics attaining the projection | [Local realization](../research/LOCAL_REALIZATION.md) |

The same full-algebra projection appears in both accounts. The erasure theorem is a separate operational result; it is not inferred from the edge or bulk autocorrelation powers.

For preparation use the single [Watrous bridge](../learning/WATROUS_BRIDGE.md) and [30-milestone map](../learning/MILESTONES.md). [Attribution](../literature/ATTRIBUTION.md), [physical-loss related work](../references/RELATED_WORK.md), and [verification](../VERIFICATION.md) identify inherited tools and the scope of reproducible checks.
