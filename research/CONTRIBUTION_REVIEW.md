# The result in context

## The physical question

How much of a local transverse spin survives projection onto the **entire conserved symmetry algebra**, and how does that amount depend on its position in an open chain?

For ordinary $`SU(2)`$, the contribution is exactly $`1/L`$ at every site. Real quantum-group deformation changes this spatial law: at every fixed finite $`q>1`$, the end contribution scales as $`L^{-1/2}`$; at fixed $`q>q_0`$ and fixed interior position fraction, the bulk contribution scales as $`L^{-2}`$ with an explicit amplitude and spatial profile. These are asymptotic enhancement and suppression relative to $`1/L`$. Both contributions still vanish as $`L`$ grows. The [theorem](THEOREM.md) gives the coefficients and precise domains; $`q_0`$ is a sufficient proof threshold.

For every finite real $`q\ge1`$, the represented algebra has dimension $`\binom{L+3}{3}`$. Deformation changes its embedding in physical operator space and its overlap with local spins. The algebras are generally not nested. The [Pauli-basis identity](LOCAL_REALIZATION.md#5-same-number-of-conserved-directions-different-spatial-overlap) expresses this fixed dimension as a sum of projection weights over all Pauli strings.

The [physical mechanism](PHYSICAL_MECHANISM.md) makes this statement quantitative: the infinite-temperature probabilities of total-spin sectors are unchanged, while their conditional overlap with a local spin changes. At a deformed end the overlap occupies a short magnetic-ladder profile; in the bulk many ladder entries contribute with much smaller amplitudes. In the stated local averaged dynamics, $`M_{L,i}`$ is exactly the retained fraction of an initially polarized spin, with all other spins maximally mixed.

The bulk law also fixes a common interior shape. At each fixed $`q>q_0`$, with $`i_L/L\to x\in(0,1)`$,

```math
\frac{M_{L,i_L}(q)}{M_{L,\lfloor L/2\rfloor}(q)}
\longrightarrow\frac{\mathcal F(x)}{\mathcal F(1/2)}.
```

Thus deformation changes the leading bulk amplitude, while this ratio to the center is independent of $`q`$ throughout the proved domain. The [bulk proof, Section 2](../archive/research-handoff-2026-10-08/prior/prior/FOLLOWUP.md) specifies the profile at fixed interior position fractions.

## What supports the central claim

| Role | Result and its use |
|---|---|
| Exact quantity | The ordinary physical infinite-temperature inner product defines the projection of $`X_i`$ onto the full symmetry algebra. The finite recursion includes all physical multiplicity paths, fixing the quantity whose asymptotic behavior is sought. |
| Central spatial law | The end coefficient and restricted-domain bulk amplitude/profile are evaluated explicitly. The bulk proof controls all contributing sectors uniformly, rather than inferring an exponent from finite-size data. |
| Hamiltonian interpretation | The [exact excess identity](PLATEAU_DICTIONARY.md) separates this symmetry contribution from additional time-averaged memory specific to a Hamiltonian, including accidental degeneracies. |
| Local attainment | The [coherent-plus-noisy model](LOCAL_REALIZATION.md) converges to this projection at fixed finite size and positive noise strength. It realizes the baseline as an actual noise-averaged plateau. |
| Reference ensemble | A generally nonlocal random eigenbasis has a controlled mean excess. This is a diagnostic benchmark for the distinction above. |

The central result is the evaluated spatial law. The excess identity clarifies its meaning; the local realization shows how it can be attained. The random-eigenbasis calculation supplies a separate, generally nonlocal reference ensemble.

The technical chain is recorded in the [proof map](PROOF_MAP.md): physical multiplicity trace, exact finite recursion, uniform domination and sector matching, then spectral evaluation. The ordinary trace and physical representation are essential throughout. Spectral measures used in the calculation do not replace those physical trace weights.

## Physical interpretation

Deforming the symmetry makes its unavoidable local memory asymptotically larger at an end and smaller in the interior, even though the algebra dimension is unchanged. The calculation covers the entire algebra, so the spatial contrast accounts for all conserved symmetry operators and their products. The local noise-averaged realization turns that projection into a measurable retained polarization at fixed finite size.

## Relation to prior work

The complete-commutant projection principle, quantum-group representation theory, orthogonal-polynomial and Jost tools, and the stationary-commutant mechanism for symmetry-preserving noise are inherited from the literature. The contribution here is the **evaluated physical multiplicity trace and uniform finite-deformation spatial asymptotics**.

The [attribution map](../literature/ATTRIBUTION.md) compares the physical predecessors in their stated versions and gives exact observable and dissipator conversions. In particular it distinguishes the spin-$`\tfrac12`$ physical trace from different Temperley–Lieb representations. The comparison identifies the representation, observable, and projected algebra associated with each result.

## Orders of limits that carry the interpretation

| Statement | Order and domain |
|---|---|
| End-spin law | Fix finite $`q>1`$, then take $`L\to\infty`$. The exact $`q=1`$ result is stated separately. |
| Bulk law | Fix $`q>q_0`$ and take $`L\to\infty`$ with $`i_L/L\to x\in(0,1)`$. |
| Boundary-distance matching | First take $`L\to\infty`$ at fixed distance from the end, then take that distance large. |
| Noisy attainment | Fix finite $`L`$ and positive noise strength, then take long time. Removing noise first returns isolated dynamics, whose infinite-time average can include Hamiltonian-specific excess. |

The [model and results](MODEL_AND_CLAIMS.md) give the full assumptions. The local convergence estimate uses a finite-size dissipative gap; the [local realization](LOCAL_REALIZATION.md) states the resulting bound.
