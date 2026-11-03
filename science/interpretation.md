# What the capacity ceiling says about symmetry memory

The full symmetry projection preserves a coherent matrix algebra whose largest irrep has dimension $`n+1`$. Deformation changes the physical realization of those logical matrices. The [spatial-memory laws](../research/THEOREM.md) quantify how local transverse operators overlap with that algebra; the [capacity theorem](capacity.md) instead describes quantum communication through the projected chain followed by independently flagged physical erasure.

For every fixed finite $`r\gt1`$ and $`0\lt p\lt1`$, the two-way capacity stays between a positive lower bound and a finite upper bound independent of $`n`$. Consequently it is of order one per complete block, and its rate per physical carrier vanishes as $`n`$ grows. The exact finite-deformation capacity and sharp ceiling are not determined.

## A physical embedding changes loss without removing its ceiling

At $`r=1`$, permutation twirling allows the inherited Schur/symmetric-loss comparison and exact erasure capacities. At $`r\gt1`$, one-site conditional channels already have different Choi spectra; three-site multiplicity averaging still leaves distinct end and middle loss maps. Thus the finite-deformation result needs its own proof.

That proof follows information which reaches the **lost** sites. Within each CG path, the first erased physical spin that differs from the path's edge sign locates a logical magnetic label to bounded uncertainty. Hidden mismatches before that observation have a geometric tail because each mismatch is erased independently. Exact finite-$`r`$ coefficients convert the resulting exposure estimate into an entropy bound. Measuring the full complementary multiplicity labels then makes that statement valid for arbitrary coherent inputs to the whole projection. Squashed entanglement supplies the established adaptive communication converse.

The environment measurement is a proof device. A user need not implement it, and it does not imply that the receiver knows the input magnetic label. A converse can use information available in a mathematical extension of the channel's environment.

## Distinct limits and resources

| Setting | Supported statement |
|---|---|
| Fixed finite $`r\gt1`$, fixed $`0\lt p\lt1`$ | A size-independent two-way-capacity ceiling for the supplied stationary projection followed by local erasure. |
| $`r=1`$ | The ordinary-permutation benchmark has exact finite-block capacities. |
| $`p=0`$ | The largest coherent sector transmits $`\log_2(n+1)`$ qubits per block. |
| $`p=1`$ | The channel erases every physical carrier and has zero capacity. |
| Parameters varying with $`n`$ | The fixed-parameter result supplies no uniform crossover formula. |
| A finite-time implementation of $`\Pi_r`$ | It needs a separate reference-stable channel-error and mixing-time analysis. |

The upper constant in the first-mismatch proof is deliberately nonsharp and becomes singular in limits such as $`r\downarrow1`$ or $`p\downarrow0`$. This is a limitation of that estimate, rather than a claim of a physical capacity discontinuity. No singular $`r\to\infty`$ generator limit is substituted for finite deformation.

## Relationship and ownership

[Quantum Group Memory Laws](../README.md) owns the physical quantum-group projection, spatial-memory account, exact deformed small-sector maps and full finite-$`r`$ ceiling proof. [Quantum Permutation Noise Limits](https://github.com/GoGoKo699/Quantum-Permutation-Noise-Limits) owns the ordinary-permutation reduction, exact flagged-erasure benchmark and its broader replacement-noise conclusions. The two projects share the operational boundary at $`r=1`$, with different proof mechanisms on either side. Reciprocal explanations retain their definitions and main consequences without duplicating the entire deformed proof.

The commutant projection, representation theory, symmetric-loss resources, reverse hashing and squashed-entanglement converse are inherited and credited in [related work](../references/RELATED_WORK.md). The new operational contribution is the finite-deformation, all-path environment estimate and its reference-stable extension to the complete stationary channel.
