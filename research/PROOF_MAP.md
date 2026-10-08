# Proof map

Read the [compact theorem](THEOREM.md) with the [model boundaries](MODEL_AND_CLAIMS.md). Detailed proof sources are preserved unchanged below; their historical allocation notes do not issue current work orders.

| Obligation | Authoritative source |
|---|---|
| Physical algebra, exact multiplicity trace, all-path finite recursion | [Initial calculation, Sections 2–4](../archive/research-handoff-2026-10-08/prior/prior/prior/prior/PILOT.md). |
| Closed edge sum, fixed-distance limit, auxiliary controls | [Asymptotics, Sections 2–6](../archive/research-handoff-2026-10-08/prior/prior/prior/FOLLOWUP.md). |
| Full fixed-deformation bulk theorem | [Bulk account](../archive/research-handoff-2026-10-08/prior/prior/FOLLOWUP.md), including Sections 4–5 on uniform domination and matching. |
| Both spectral endpoints, parity, and complete sector sum | [Bulk account, Sections 6–8](../archive/research-handoff-2026-10-08/prior/prior/FOLLOWUP.md). |
| Explicit Jost convolution, Gaussian constant, and parity normalization | [Kernel details](KERNEL_DETAILS.md), deriving the intermediate steps in the bulk account. |
| Sector explanation, observable readout, and elementary spatial profile | [Physical mechanism](PHYSICAL_MECHANISM.md), deductions from the exact projection and proved asymptotics. |
| Complement of the common symmetry in a fixed Hamiltonian's plateau | [Plateau dictionary](PLATEAU_DICTIONARY.md). |
| Local coherent-plus-noisy convergence and broken-hypothesis controls | [Local realization](LOCAL_REALIZATION.md). |

The kernel proof counts every second-coordinate change with two strictly subcritical tilts. The moderate-deviation estimate and large-spin norm bound are necessary to justify summing asymptotics. Numerical agreement with the limiting kernel is not substituted for this step. The imported proof remains author-side; no external independent proof report is present.

[Verification](../VERIFICATION.md) links the corresponding unmodified checkers. New concrete proof objections should be recorded separately, not resolved by silently editing the protected source.

## Support qualification for the archived binomial identity

The [bulk account, Section 4.2](../archive/research-handoff-2026-10-08/prior/prior/FOLLOWUP.md) uses adjacent differences of

$$
b_n(k)=2^{-n}\binom n{(n+k)/2},\qquad
\Delta b_n(k)=b_n(k)-b_n(k+2),
$$

with $n\ge0$ an integer and binomial coefficients zero outside their support. Its displayed rational identity should be read with the support condition

$$
\Delta b_n(k)=\frac{2(k+1)}{n+k+2}b_n(k),
\qquad k\equiv n\pmod2,\quad k\ge -n.
$$

Parity alone does not suffice: at $k=-n-2$ the denominator vanishes while the adjacent difference equals $-2^{-n}$. For indices below $-n$, use binomial symmetry in the nonsingular form

$$
\Delta b_n(k)=-\Delta b_n(-k-2).
$$

This explicitly qualifies the intermediate identity in the immutable source. The reflected index is at least $n$ for the omitted parity indices, so it is covered by the displayed support condition. The adjacent-difference estimates, kernel bound, and stated spatial-memory theorem are unchanged.
