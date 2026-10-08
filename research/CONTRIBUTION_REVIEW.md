# Contribution and physical interpretation

## The physical question

How much of a local transverse spin survives projection onto the **entire conserved symmetry algebra**, and how does that amount depend on its position in an open chain?

For ordinary $SU(2)$, the contribution is exactly $1/L$ at every site. Real quantum-group deformation changes this spatial law: at every fixed finite $q>1$, the end contribution scales as $L^{-1/2}$; at fixed $q>q_0$ and fixed interior position fraction, the bulk contribution scales as $L^{-2}$ with an explicit amplitude and spatial profile. These are asymptotic enhancement and suppression relative to $1/L$. Both contributions still vanish as $L$ grows. The [theorem](THEOREM.md) gives the coefficients and precise domains; $q_0$ is a sufficient proof threshold.

The number of conserved operator directions does not increase. For every finite real $q\ge1$, the represented algebra has dimension $\binom{L+3}{3}$. Deformation changes its embedding in physical operator space and its overlap with local spins. The algebras are generally not nested. The [Pauli-basis identity](LOCAL_REALIZATION.md#5-same-number-of-conserved-directions-different-spatial-overlap) explains this distinction: its sum runs over all Pauli strings, so it implies neither conservation of total single-site memory nor motion of memory from the bulk to the ends.

The [physical mechanism](PHYSICAL_MECHANISM.md) makes this statement quantitative: the infinite-temperature probabilities of total-spin sectors are unchanged, while their conditional overlap with a local spin changes. At a deformed end the overlap occupies a short magnetic-ladder profile; in the bulk many ladder entries contribute with much smaller amplitudes. In the stated local averaged dynamics, $M_{L,i}$ is exactly the retained fraction of an initially polarized spin, with all other spins maximally mixed.

The bulk law also fixes a common interior shape. At each fixed $q>q_0$, with $i_L/L\to x\in(0,1)$,

$$
\frac{M_{L,i_L}(q)}{M_{L,\lfloor L/2\rfloor}(q)}
\longrightarrow\frac{\mathcal F(x)}{\mathcal F(1/2)}.
$$

Thus deformation changes the leading bulk amplitude, while this ratio to the center is independent of $q$ throughout the proved domain. This is the normalized profile already stated in the [bulk account, Section 2](../archive/research-handoff-2026-10-08/prior/prior/FOLLOWUP.md), with fixed interior position fractions; it does not extend the result to sites approaching a boundary.

## What supports the central claim

| Role | Result and its use |
|---|---|
| Exact quantity | The ordinary physical infinite-temperature inner product defines the projection of $X_i$ onto the full symmetry algebra. The finite recursion includes all physical multiplicity paths, fixing the quantity whose asymptotic behavior is sought. |
| Central spatial law | The end coefficient and restricted-domain bulk amplitude/profile are evaluated explicitly. The bulk proof controls all contributing sectors uniformly, rather than inferring an exponent from finite-size data. |
| Hamiltonian interpretation | The [exact excess identity](PLATEAU_DICTIONARY.md) separates this symmetry contribution from additional time-averaged memory specific to a Hamiltonian, including accidental degeneracies. |
| Local attainment | The [coherent-plus-noisy model](LOCAL_REALIZATION.md) converges to this projection at fixed finite size and positive noise strength. It realizes the baseline as an actual noise-averaged plateau. |
| Reference ensemble | A generally nonlocal random eigenbasis has a controlled mean excess. This is a diagnostic benchmark for the distinction above. |

The central result is the evaluated spatial law. The excess identity clarifies its meaning; the local realization shows how it can be attained. The reference ensemble is not an assumption about the eigenvectors of a local spin Hamiltonian.

The technical chain is recorded in the [proof map](PROOF_MAP.md): physical multiplicity trace, exact finite recursion, uniform domination and sector matching, then spectral evaluation. The ordinary trace and physical representation are essential throughout. Spectral measures used in the calculation do not replace those physical trace weights.

## Why the result matters, and the skeptical case

The positive case is a quantitative answer for a complete conserved algebra. It shows that deforming a symmetry can make its unavoidable local memory asymptotically larger at an end and smaller in the interior, even though the algebra dimension is unchanged. Because the calculation covers the entire algebra, the contrast does not depend on selecting an incomplete list of charges. The local noise-averaged realization gives the spatial law a concrete dynamical setting.

The skeptical case is that the model and framework are established, while the additional analysis is specific to this representation and observable. The result's significance rests on the spatial conclusion. Exactness and successful reproduction do not by themselves establish broad physical importance. The bulk equality has a sufficient deformation restriction, and symmetry alone does not determine a generic isolated local Hamiltonian's complete time-averaged memory. The noisy realization supplies a specified model with exact attainment; its unestimated dissipative gap leaves the chain-size dependence of relaxation time unresolved.

This supports retaining one focused contribution with the spatial law as its organizing claim. Stronger dynamics or a storage protocol would be separate scientific questions, rather than premises needed to state this result.

## Relation to prior work

Grant the literature the complete-commutant projection principle, quantum-group representation theory, orthogonal-polynomial and Jost tools, and the stationary-commutant mechanism for symmetry-preserving noise. The additional implication assessed here is the **evaluated physical multiplicity trace and uniform finite-deformation spatial asymptotics**.

The [attribution map](../literature/ATTRIBUTION.md) compares the physical predecessors in their stated versions and gives exact observable and dissipator conversions. In particular it distinguishes the spin-$\tfrac12$ physical trace from different Temperley–Lieb representations, and includes the newer structural-reference version. The inspected passages do not supply the same complete spatial law. The [archived contribution review](../archive/research-handoff-2026-10-08/prior/REVIEW.md) and [historical source check](../archive/research-handoff-2026-10-08/SOURCE_CHECK.md) preserve the earlier reading record. This bounded comparison does not establish exhaustive priority; internal proof scrutiny and executable checks remain distinct from independent review.

## Orders of limits that carry the interpretation

| Statement | Order and domain |
|---|---|
| End-spin law | Fix finite $q>1$, then take $L\to\infty$. The exact $q=1$ result is stated separately. |
| Bulk law | Fix $q>q_0$ and take $L\to\infty$ with $i_L/L\to x\in(0,1)$. |
| Boundary-distance matching | First take $L\to\infty$ at fixed distance from the end, then take that distance large. |
| Noisy attainment | Fix finite $L$ and positive noise strength, then take long time. Removing noise first returns isolated dynamics, whose infinite-time average can include Hamiltonian-specific excess. |

The [model and claim boundaries](MODEL_AND_CLAIMS.md) give the full scope. The spatial law does not establish a hydrodynamic decay exponent or an encoded-memory lifetime. The [current work order](../work_orders/CURRENT.md) defines when a concrete objection or a selected new claim should reopen research.
