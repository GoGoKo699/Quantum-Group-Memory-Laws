# Attribution and source comparison

The physical comparisons below use the primary passages in the stated versions. They distinguish the inherited framework from the evaluated physical spatial law. The [historical contribution review](../archive/research-handoff-2026-10-08/prior/REVIEW.md) and [historical source check](../archive/research-handoff-2026-10-08/SOURCE_CHECK.md) retain their original reading records. External articles are linked, not redistributed.

The single background anchor is Moudgalya–Motrunich, arXiv:2108.10324v2. Follow the [tutorial bridge](../research/TUTORIAL_BRIDGE.md) for its reading route and the translation into this repository. The comparisons below serve attribution and proof provenance rather than a list of prerequisite tutorials.

## Physical predecessors

| Source and inspected passages | Inherited result and distinction |
|---|---|
| Delacrétaz, Gorbenko, Wang, Zan, Zhabin, [Hydrodynamic tails in chaotic spin chains with quantum group symmetry, v1](https://arxiv.org/html/2606.20850v1), Sections II–IV and Appendix F; Eqs. (28)–(29), (43)–(48) | Real-$q$ spin-chain models, symmetric coproduct, finite-size saturation, and nonlinear-charge improvements. Appendix F already obtains position-dependent bounds using up to thirteen charges. The inspected calculation does not evaluate the complete algebra or derive its edge/bulk asymptotics. Our projection law supplies a symmetry baseline; it does not determine the source's dynamical exponent or full deterministic plateau. |
| Moudgalya–Motrunich, [Hilbert Space Fragmentation and Commutant Algebras, v2](https://arxiv.org/abs/2108.10324v2), Sections V.C–D, VII.A, VII.C.4 and Appendix I; Eqs. (61), (63)–(64), (69)–(73), (94) | Complete-commutant projection and quantum-group decomposition. The $m$-state Temperley–Lieb realization has multiplicity $[2\lambda+1]_q$, with $m=q+q^{-1}$; the spin-$\tfrac12$ realization has $2\lambda+1$ multiplet states. Both use ordinary physical traces, but in different representations. The exact edge-energy bound in Eq. (94) concerns $e_{1,2}$, not the charged transverse $X_i$. |
| Hart, [Exact Mazur bounds in the pair-flip model and beyond, v2](https://arxiv.org/html/2308.00738v2), Eq. (18), Sections 4.3–4.4 and conclusion; Eqs. (40), (54)–(55) | Exact conserved-pattern counting, nonzero thermodynamic boundary memory, $L^{-1/2}$ bulk memory, and interior spatial dependence are established precedents. The observable is $S_i^z$ in an $m^L$ physical space. The conclusion distinguishes its evaluated pattern sector from the larger entangled Temperley–Lieb commutant. A different exponent alone does not establish a new contribution; the physical representation, observable, and projected algebra must be matched. |
| Li–Sala–Pollmann, [Hilbert Space Fragmentation in Open Quantum Systems, v1](https://arxiv.org/abs/2305.06918v1), Section V opening and Eq. (26); Appendix B, Eqs. (B1)–(B6) | Hermitian Temperley–Lieb jumps preserve stationary coherences and yield the complete stationary commutant. This is the inherited noisy-attainment mechanism. Its spectral presentation states diagonalizability and peripheral-spectrum conditions; the [local realization](../research/LOCAL_REALIZATION.md) verifies finite-chain convergence directly by a Dirichlet estimate. The reflection/jump identity below makes the connection exact. |
| Gorbenko–Zhabin, [Chaos in Systems with Quantum Group Symmetry, v3](https://arxiv.org/html/2510.23247v3), Sections 2–4, conclusion and Appendix C; Eqs. (3)–(5), (13) | Hecke generators and symmetry-preserving interactions are structural predecessors. Version 3, dated 7 September 2026, adds system-size analysis of complex eigenvalues and spectral statistics to its unit-circle-$q$, non-Hermitian model. The inspected passages do not evaluate the real-$q$ transverse symmetry projection. The archived comparison with v2 remains unchanged. |

## Observable normalization

The following conversion is derived here from the repository's definition, independently of any plotted source value. Set

$$
\langle A,B\rangle=2^{-L}\operatorname{Tr}(A^\dagger B),\qquad
w(A)=\langle\Pi_q A,\Pi_q A\rangle,\qquad M=w(X_i).
$$

The projection preserves adjoints and magnetization-charge sectors. For $s_i^+=(X_i+iY_i)/2$, the projections of $s_i^+$ and $s_i^-$ therefore have equal norms and are orthogonal. Since $X_i=s_i^++s_i^-$, this gives

| Observable $A$ | Initial norm $\langle A,A\rangle$ | Projection weight $w(A)$ |
|---|---:|---:|
| $X_i$ | $1$ | $M$ |
| $s_i^+=(X_i+iY_i)/2$ | $1/2$ | $M/2$ |
| $\Sigma_i^+=X_i+iY_i$ | $2$ | $2M$ |

Thus the projection weight divided by the initial norm is the same in all three conventions. This is a statement about the symmetry projection, not arbitrary finite-time complex correlators.

The [finite-recursion derivation, Section 5](../archive/research-handoff-2026-10-08/prior/prior/prior/prior/PILOT.md) evaluates the projection of $X_i$ onto $\operatorname{span}\{E,F\}$ as

$$
M^{\{E,F\}}_{L,i}
=\frac1L\left[\frac{q+q^{-1}+2}{2(q+q^{-1})}\right]^{L-1}.
$$

This unit-normalized comparator has the same formula as the right side of Delacrétaz et al.'s Eq. (29). For Pauli $X_i$, it includes both charge sectors. The explicitly defined ladder convention in that source's Section III.1 must be matched to the initial norm before comparing absolute charged-correlator amplitudes. No plot ordinates or unstated plotting conventions enter this comparison. The complete-algebra result includes all products of the generators, not only this two-dimensional span.

## Reflection noise and Temperley–Lieb jumps

The connection to Li–Sala–Pollmann can be checked directly. For Hermitian $A$, define

$$
\mathcal D_A(O)=AOA-\tfrac12\{A^2,O\}.
$$

With the local operators of [LOCAL_REALIZATION.md](../research/LOCAL_REALIZATION.md),

$$
e_j=qI-R_j=(q+q^{-1})P_j,\qquad U_j=I-2P_j,
$$

expansion of the products gives

$$
U_jOU_j-O
=4\mathcal D_{P_j}(O)
=\frac{4}{(q+q^{-1})^2}\mathcal D_{e_j}(O).
$$

Consequently, positive-rate reflection noise is precisely Hermitian Temperley–Lieb jump noise after rate rescaling. Section V of Li–Sala–Pollmann uses jumps $L_j=e_{j,j+1}$ and Eq. (26) gives the stationary-commutant structure. The present physical representation and evaluated transverse projection specify the spatial plateau. This identity does not estimate the dissipative gap or imply saturation for deterministic Hamiltonians.

## Spectral and ensemble inputs

The detailed input routes are recorded in the [proof map](../research/PROOF_MAP.md) and preserved derivations.

| Source | Inherited input and boundary |
|---|---|
| Koelink–Verding, [Spectral analysis and the Haar functional on the quantum SU(2) group](https://arxiv.org/abs/math/9412225), Section 6 | Al-Salam–Chihara recurrence and spectral measure. The base is translated to $z=q^{-2}$; the quantum-group Haar functional is not substituted for the physical spin trace. |
| Damanik–Simon, [Jost Functions and Jost Solutions for Jacobi Matrices, II](https://arxiv.org/abs/math/0502487), Theorem 1.5 and Appendix A | Jacobi Jost decay/analyticity. The uniform moderate-window estimate and matching to the finite spin recursion are derived in the preserved proof. |
| Collins–Śniady, [Integration with respect to Haar measure](https://arxiv.org/abs/math-ph/0402073) | General Haar-integration attribution. The elementary moments are independently derived in [PLATEAU_DICTIONARY.md](../research/PLATEAU_DICTIONARY.md); no uninspected equation is needed from this source. |

The added implication is the evaluated physical multiplicity trace and its finite-$q$ spatial asymptotics, including the uniform bulk matching in the stated sufficient domain. The inspected passages do not directly supply that complete law in the same representation. This is a bounded source comparison, not exhaustive priority clearance or independent proof review.
