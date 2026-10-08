# Exploratory work not promoted to a finite-q bulk theorem

The initial scalar-loop finite-q site-profile survey completed its reported L<=160 cases. Vectorizing over the doubled-spin index and magnetic index greatly shortened the recurrence evaluation; the mathematical recursion is unchanged. `fast_grid_initial.py` retains the original development copy, including runtime-local demo paths. The active `../fast_grid.py` removes that demonstration and adds portable library documentation. No calculation or assertion in the formal test runner changed.

A further large-spin boundary-scattering route was investigated. Far from small total spin, the magnetic-index transition matrix tends to the tridiagonal J_q in the follow-up. Its off-diagonal entries and diagonal correspond formally to an Al-Salam–Chihara Jacobi matrix with base z=q^-2 and parameters q^-1,q^-3. This identification is not used in any proved finite-q bulk statement.

Solving its two zero-energy harmonic recurrences, normalized to unit asymptotic slope, suggests amplitudes

    A_+ = (1-q^-1) [(z;z)_infinity/(q^-1;z)_infinity]^4,
    A_- = (1+q^-1) [(z;z)_infinity/(-q^-1;z)_infinity]^4.

An unproved bulk-matching guess would multiply the auxiliary crystal scaling function by (A_+^2+A_-^2)/2. At q=2.6 this predicts a central coefficient about 9.5557097705. The finite data approach that scale but do not prove it. The unresolved step is uniform control of the full triangular finite-q recursion, including small-total-spin sectors, parity, and the propagation of the nonnegative-magnetic boundary. Neither the formal Jacobi identification nor the harmonic products establish that control. This guess is preserved only as a possible next route; it is not called a result in the final report.

The source search for the polynomial family returned relevant mathematical publications, but their full technical hypotheses were not audited. No orthogonal-polynomial theorem is imported into FOLLOWUP.md. The formal proofs there use only explicitly derived binomial, spectral-sine, Green-function, and Jensen estimates.
