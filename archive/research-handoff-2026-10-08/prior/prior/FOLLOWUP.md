# Fixed-deformation bulk symmetry memory
## A controlled bulk limit, its prefactor, and its relation to boundary memory

**8 October 2026 — author-side analytical continuation.**

The missing finite-q bulk asymptotic is obtained in the explicit sufficient range

\[
 b(q):=\frac{q^{-1}+q^{-3}}{(1-q^{-2})^2}<1.
\]

This is equivalent to \(q>q_0=2.0810189966\ldots\). It includes the working value \(q=2.6\). The boundary of this estimate is **not a physical transition**, and no failure of the bulk law for \(1<q\le q_0\) is asserted. The earlier lower bound for \(q>\sqrt3\) and the exact boundary results for every fixed \(q>1\) remain intact.

The exponent, coefficient, and spatial function below are derived, not fitted. Standard representation theory, Al-Salam–Chihara spectral formulas, and Jacobi scattering theory are inherited mathematical inputs. The new step is uniform control of the complete triangular spin recursion and its matching to those spectral formulas. The account is an author-side proof, not independent review or exhaustive priority clearance.

No repository or protected project was accessed or modified. No manuscript was prepared and no external contact was initiated. The two older PDFs in the conversation were not scientific inputs. The immediate predecessor is preserved unchanged in `prior/`.

## 1. Fixed quantity and operational scope

Keep the open L-site spin-1/2 chain, symmetric real-q coproduct, and infinite-temperature Pauli convention of the preceding notes. The full quantum-group algebra is

\[
\mathcal A_q=\bigoplus_h\operatorname{End}(\mathcal V_{h/2})\otimes I_{m_{L,h}},
\qquad
m_{L,h}=\binom L{(L-h)/2}-\binom L{(L-h)/2-1}.
\]

Wrong-parity and out-of-range multiplicities vanish. Set \(D_L(h)=2^{-L}m_{L,h}\). For the orthogonal projection \(\Pi_q\) onto this algebra,

\[
 M_{L,i}(q)=2^{-L}\|\Pi_q(X_i)\|_{\rm HS}^2.
\]

For any Hamiltonian commuting with the symmetry,

\[
 \overline C_i\ge M_{L,i}(q),\qquad
 C_i(t)=2^{-L}\operatorname{Tr}[X_i(t)X_i],\quad C_i(0)=1.
\]

The bar denotes the finite-system infinite-time average. The projection principle and its use with complete commutant algebras are established [MM]. This quantity need not exhaust a selected Hamiltonian's plateau. The local random-kick model in the first pilot does attain it, but is not substituted for the deterministic Hamiltonians in [D26]. No dynamical exponent, relaxation time, or encoded-qubit fidelity follows from a static memory value.

## 2. Main result

Let q be fixed with \(b(q)<1\), and let \(i_L/L\to x\in(0,1)\). Put \(z=q^{-2}\), and use

\[
 (a;z)_\infty=\prod_{k=0}^{\infty}(1-az^k).
\]

Define two positive amplitudes

\[
 A_+(q)=(1-q^{-1})\left[\frac{(z;z)_\infty}{(q^{-1};z)_\infty}\right]^4,
\qquad
 A_-(q)=(1+q^{-1})\left[\frac{(z;z)_\infty}{(-q^{-1};z)_\infty}\right]^4,
\]

and

\[
 \mathcal K(q)=\frac{A_+(q)^2+A_-(q)^2}{2}.
\]

Then the complete symmetry projection has the limit

\[
 \boxed{M_{L,i_L}(q)=\frac{\mathcal K(q)\mathcal F(x)}{L^2}[1+o(1)].}\tag{1}
\]

The positive symmetric function is

\[
 \boxed{
 \mathcal F(x)=\frac{3\sqrt2}{4\pi[x(1-x)]^3}
 \int_0^1\frac{u^2(1-u)^2\,du}
 {[\frac12+(u-x)^2/(x(1-x))]^{5/2}}.
 }\tag{2}
\]

In particular, the leading normalized bulk profile \(M_{L,i}/M_{L,\lfloor L/2\rfloor}\) tends to \(\mathcal F(x)/\mathcal F(1/2)\), independently of q **within the proved range**. q changes the positive amplitude, not this exponent or normalized bulk profile.

The sufficient threshold follows by writing \(s=q+q^{-1}\): \(b(q)<1\) is \(s^2-s-4>0\). Thus

\[
 q_0=\frac{s_0+\sqrt{s_0^2-4}}2,\qquad s_0=\frac{1+\sqrt{17}}2.
\]

This threshold comes from a deliberately enlarged positive comparison kernel, not from a singularity of the quantum-group representation. Constants below can deteriorate as \(q\downarrow q_0\). The theorem is not uniform near q=1, near a spatial boundary, or under q changing with L.

At q=2.6,

\[
 A_+=2.68164492284445\ldots,\quad A_-=0.137925444864756\ldots,
\quad\mathcal K=3.60512146027929\ldots,
\]

so

\[
 \boxed{L^2M_{L,\lfloor L/2\rfloor}(2.6)\longrightarrow9.55570977050275\ldots.}\tag{3}
\]

The product and integral definitions, rather than these floating-point decimals, specify the constant.

## 3. Exact quadrant form of the spin recursion

This is a change of indices in the preceding exact Clebsch–Gordan recurrence. It changes no physical model.

Write \(r=M+j\), \(h=2j\), and now put \(u=h-r-1\). Both r and u are nonnegative. If \(t_{n,i}(h,r)=2^{-n}T_{n,i}(h,r)\), then

\[
 M_{L,i}=2\sum_{h\equiv L\ (2)}\sum_{r=0}^{h-1}\frac{t_{L,i}(h,r)^2}{D_L(h)}.
\]

One extension step is a positive kernel \(\mathsf K_q\) on the quadrant. Its row at (r,u) connects to

\[
 (r-1,u),\quad(r,u-1),\quad(r,u+1),\quad(r+1,u)
\]

with coefficients

\[
\begin{aligned}
a_{r,u}&=\frac{\sqrt{(1-z^r)(1-z^{r+1})}}{2(1-z^{r+u+1})},\\
b_{r,u}&=\frac{z^{r+1/2}\sqrt{(1-z^u)(1-z^{u+1})}}{2(1-z^{r+u+1})},\\
c_{r,u}&=\frac{z^{r+3/2}\sqrt{(1-z^{u+2})(1-z^{u+1})}}{2(1-z^{r+u+3})},\\
d_{r,u}&=\frac{\sqrt{(1-z^{r+1})(1-z^{r+2})}}{2(1-z^{r+u+3})}.
\end{aligned}\tag{4}
\]

Terms leaving the quadrant have zero coefficient. Total h changes by one at every step, preserving the correct spin parity. Initial support h<=i automatically enforces h<=n throughout forward propagation.

Two elementary bounds will be decisive:

\[
 a_{r,u},d_{r,u}\le\frac12,\qquad
 b_{r,u}+c_{r,u}\le v_r:=\tfrac12(q^{-1}+q^{-3})z^r.\tag{5}
\]

For example, the denominator of a is at least \(1-z^{r+1}\), and its numerator is at most that number. For b, its square root is at most \(1-z^{u+1}\), which is no larger than the denominator. The other two cases are identical comparisons. No large-h approximation is involved in (5).

With p=i-1, the insertion obeys the global absolute bound

\[
 |t_{i,i}(h,r)|\le C_q q^{-r}[D_p(h-1)+D_p(h+1)].\tag{6}
\]

This follows directly from its two exact terms and \(1-z^h\ge1-z\). Signs at small spin cause no problem for the upper estimates. In the domain of (1) the stronger positivity condition of the preceding lower-bound proof also happens to hold, but is not needed to control the absolute remainder here.

## 4. Uniform upper estimate: the previously missing control

### 4.1 Count changes of u, rather than assuming u stays fixed

Let \(P_0\) be the nearest-neighbor kernel \((P_0)_{r,r\pm1}=1/2\) on nonnegative integers, killed at -1. Its Green kernel is

\[
 G_0(r,s)=\sum_{n\ge0}(P_0^n)_{r,s}=2\min(r+1,s+1).
\]

For a positive tilt \(\vartheta\), define a one-dimensional majorant

\[
 H_\vartheta=P_0+e^\vartheta\operatorname{diag}(v_r).
\]

Every step changing u is counted once by its diagonal term. By (5), for any nonnegative function g,

\[
 \sum_{r_0,u_0}(\mathsf K_q^n)_{(r,u),(r_0,u_0)}
 e^{\vartheta|u_0-u|}g(r_0)
 \le (H_\vartheta^ng)_r.\tag{7}
\]

The absolute displacement is no greater than the number of u-changing steps. This is a sum over every physical recursion path; it neither assumes a short path nor discards an unfavorable spin sector.

With the weight \(h_0(r)=r+1\),

\[
 \|G_0e^\vartheta V\|_{\infty,h_0}
 \le2e^\vartheta\sum_{s\ge0}(s+1)v_s
 =e^\vartheta b(q).
\]

When \(b(q)<1\), choose \(\vartheta>0\) with \(e^{2\vartheta} b(q)<1\). Both tilts \(\vartheta\) and \(2\vartheta\) are then available; the second reserves room for the path-tail estimate in Section 5. This is the only parameter restriction in the uniform domination step.

The Neumann series for \((I-G_0e^\vartheta V)^{-1}\) provides a positive 1-harmonic function comparable to r+1. The same Green bound excludes eigenvalues above 1 and bounded regular solutions at the spectral endpoints. Positivity of V also excludes eigenvalues below -1. For the negative endpoint one may conjugate by \((-1)^r\); a hypothetical bounded regular solution would obey the corresponding signed Green equation, also excluded by the norm bound. Thus H has spectrum [-1,1], no endpoint resonance, and exponentially decaying perturbation coefficients.

### 4.2 Spectral-kernel estimate used in the proof

The precise auxiliary estimate is the following. If

\[
 H=P_0+\operatorname{diag}(w_r),\quad w_r\ge0,\quad w_r=O(e^{-\kappa r}),
 \quad2\sum_{r\ge0}(r+1)w_r<1,
\]

and \(g_r\) decays exponentially times a fixed polynomial, then, for any fixed A and any \(\delta>0\),

\[
 |(H^ng)_r|\le C_{A,\delta,g,H}(r+1)n^{-3/2}
 \exp[-(1-\delta)r^2/(2n)],
 \quad0\le r\le A\sqrt{n\log(n+2)}.\tag{8}
\]

A proof is included here to specify more than an appeal to a heat-kernel analogy. Exponential Jacobi scattering gives an analytic Jost function, with no unit-circle zeros once endpoint resonances are excluded, and spectral density

\[
 \frac{2}{\pi}\frac{\sin^2\theta}{|u(e^{i\theta})|^2}\,d\theta.
\]

These spectral facts are standard [DS], with the off-diagonal normalization rescaled from 1 to 1/2. The regular polynomials are a linear combination of the two Jost waves. They have the form

\[
 p_r(\cos\theta)=
 \frac{e^{i(r+1)\theta}u(e^{-i\theta})-
       e^{-i(r+1)\theta}u(e^{i\theta})}{2i\sin\theta}
 +\varepsilon_r(\theta),
\]

where a choice of the overall phase or sign makes no difference below and
\(|\varepsilon_r(\theta)|\le C(r+1)e^{-\kappa' r}\) uniformly on the circle. Exponential decay follows from the Jost Volterra series; at theta=0,pi the apparently singular difference is divided only after taking its vanishing numerator. Analyticity bounds that difference by \(C(r+1)e^{-\kappa' r}|\sin\theta|\) before division.

The transform \(G(\theta)=\sum_sg_sp_s(\cos\theta)\) is analytic in a fixed strip. Substituting the displayed polynomial into its spectral integral expresses the leading part of \((H^ng)_r\) as an exponentially summable convolution of adjacent differences of the free Fourier coefficients

\[
 b_n(k)=2^{-n}\binom n{(n+k)/2}.
\]

The exact identity on the allowed parity lattice is

\[
 b_n(k)-b_n(k+2)=\frac{2(k+1)}{n+k+2}b_n(k).
\]

Stirling bounds therefore give adjacent differences bounded by
\(C(|k|+1)n^{-3/2}e^{-(1-\delta/2)k^2/(2n)}\) in the required moderate-deviation window. Convolution with exponentially decaying coefficients preserves this estimate with delta in place of delta/2: bounded shifts use the same Gaussian bound, and shifts of order n or larger have exponentially small coefficients. Equivalently, for r/n small, the cross term is absorbed by \(e^{-\kappa'|k-r|}\). The error polynomial contributes at most \(C(r+1)e^{-\kappa'r}n^{-3/2}\), from its spectral \(\sin^2\theta\) factor. That is absorbed into (8) in this window. This proves the estimate, including parity, and establishes the needed Gaussian constant rather than only an unspecified exponential envelope.

No decay law of the physical spin dynamics is inferred from this **recursion** kernel.

### 4.3 Apply it to every relevant spin sector

Let p=i-1 and n=L-i, both proportional to L. For total spin \(h\le A\sqrt{L\log L}\), the binomial estimate and (6) give, uniformly over the initial r0,u0,

\[
 |t_{i,i}(r_0+u_0+1,r_0)|
 \le C_q (u+1)p^{-3/2}e^{-u^2/[2(p+1)]}
 e^{\vartheta|u_0-u|}(r_0+1)q^{-r_0}.
\]

To check this comparison, \(u/(p+1)\to0\) uniformly in the stated window. Moving u0 below u changes the Gaussian exponent by at most \(u|u_0-u|/(p+1)\); the tilt absorbs this and the polynomial prefactor. Moving u0 above u only improves the Gaussian after a harmless unit shift. Thus no unproved independence between r and u is being assumed.

Equations (7)-(8) yield

\[
 |t_{L,i}(r+u+1,r)|\le
 C_q\frac{(u+1)(r+1)}{p^{3/2}n^{3/2}}
 \exp\left[-\frac{u^2}{2(p+1)}-\frac{(1-\delta)r^2}{2n}\right].\tag{9}
\]

On the allowed parity lattice in the same window,

\[
 D_L(h)\ge c(h+1)L^{-3/2}
 \exp[-(h+1)^2/(2L)-o(1)].
\]

Since \(h=r+u+1\) and \(p+n=L-1\), Cauchy–Schwarz controls the denominator's growing exponential by the two decreasing exponentials in (9). Choose delta below 1/4. Consequently each memory summand is bounded by

\[
 C L^{-9/2}\frac{(u+1)^2(r+1)^2}{u+r+2}
 e^{-c(u^2+r^2)/L}.\tag{10}
\]

Summation over r,u gives O(L^-2). Moreover, after multiplication by L^2 this is an integrable Riemann-sum envelope. Regions where r/sqrt(L) or u/sqrt(L) approach zero have vanishing contributions, not an uncontrolled boundary remainder.

The excluded large-spin sectors are handled separately and without (9). The average matrix element in each multiplet has modulus at most one; hence its total memory contribution is bounded by \(2hD_L(h)\). Binomial tails imply that all \(h>A\sqrt{L\log L}\) contribute o(L^-2) if A is chosen sufficiently large. This is where the full operator norm, rather than a diffusion estimate, controls the most atypical spin sectors.

These arguments establish both a matching bulk order and the domination needed for the exact coefficient.

## 5. Match the complete recursion to the large-spin kernel

Now keep r and u in fixed positive multiples of sqrt(L). In the same coordinate system, sending u to infinity in (4) gives horizontal coefficients

\[
 (J_q)_{r,r+1}=\tfrac12\sqrt{(1-z^{r+1})(1-z^{r+2})}
\]

and, after summing the two possible u-changing steps, the diagonal

\[
 (J_q)_{r,r}=\tfrac12(q^{-1}+q^{-3})z^r.
\]

The initial profile is \(f_r=q^{-r}\sqrt{1-z^{r+1}}\). Let

\[
 \mu_p(u)=2\sqrt{2/\pi}(u+1)p^{-3/2}e^{-(u+1)^2/(2p)}
\]

denote the smooth interpolation of the nonzero binomial multiplicities. It is not assigned zero on the other parity sublattice.

The matching statement, in additive rather than relative-error form, is

\[
 t_{L,i}(r+u+1,r)=
 \frac{1-z}{2}\mu_p(u)(J_q^nf)_r+o(L^{-2})\tag{11}
\]

uniformly on compact positive intervals for r/sqrt(L),u/sqrt(L), with the actual total-spin parity retained.

Here is why the pointwise approximation is uniform in the full number n of extension steps. Restrict the path sum temporarily to at most R u-changing steps and to initial r0<=R. Its u-coordinate differs by at most R from the final u, so every finite-h denominator and every additional u-factor differs from its infinite-u value by O(z^(u-R)). The total relative error is O(n z^(u-R))=o(1). Stirling's formula makes each bounded shift of the initial multiplicity equal to \(\mu_p(u)[1+o(1)]\). The insertion then becomes \((1-z)\mu_p(u)f_{r_0}/2\).

The restriction can be removed **after** taking L to infinity. Paths with more than R u-changing steps are bounded by \(e^{-\vartheta R}H_{2\vartheta}^n g\): one tilt absorbs the shifted initial multiplicity as in Section 4.3, and the other counts the excess u-changing steps. The reserved tilt remains subcritical. Equations (8)-(9) make their scaled contribution uniformly O(e^-theta R). Initial r0>R is handled by splitting its exponential factor into two halves and applying (8) to the remaining exponentially decaying vector. These tails are uniformly small as R grows.

Thus the unobserved u-changing paths have not been silently dropped, and the q->infinity limit is never taken. Correct parity at insertion follows from the fact that every full step changes h by one. It imposes no extra exclusion of the initial r0 once u0 is summed.

## 6. Spectral evaluation of J_q and the two endpoint amplitudes

Use the standard Al-Salam–Chihara family with **base z=q^-2 in (0,1)** and parameters

\[
 a=q^{-1},\qquad b=q^{-3},\qquad ab=z^2.
\]

This base is different from the spin-chain parameter q. The inherited recurrence is

\[
 2xQ_r=Q_{r+1}+(a+b)z^rQ_r+(1-z^r)(1-abz^{r-1})Q_{r-1}.
\]

Normalized by \(\sqrt{(z;z)_r(z^2;z)_r}\), it has exactly the coefficients of J_q. Because |a|,|b|<1, its measure has no discrete masses. The normalized measure on theta in (0,pi) is

\[
 d\mu(\theta)=\frac{(z,z^2;z)_\infty}{2\pi}
 \left|\frac{(e^{2i\theta};z)_\infty}
 {(ae^{i\theta},be^{i\theta};z)_\infty}\right|^2d\theta.
\]

The recurrence and measure are standard [KV]; the measure normalization was also checked against [DLMF]. Their role is spectral evaluation of an explicitly derived auxiliary matrix, not an imported spin-memory law.

The standard generating function, also verified directly from the recurrence, gives the transform of f:

\[
 \widehat f(\theta)=\sqrt{1-z}\,
 \frac{(z,z^2;z)_\infty}{(ae^{i\theta},ae^{-i\theta};z)_\infty}.
\]

For a direct verification, the generating function \(G(t)=\sum_rQ_r(x)t^r/(z;z)_r\) satisfies
\((1-at)(1-bt)G(zt)=(1-2xt+t^2)G(t)\), and \(G(0)=1\). Iterating gives the product formula. Thus its application at t=a is not an unverified summation identity.

The Jost function in the density convention of Section 4 is

\[
 u(e^{i\theta})=
 \frac{(ae^{i\theta},be^{i\theta};z)_\infty}
 {\sqrt{(z,z^2;z)_\infty}(ze^{2i\theta};z)_\infty}.
\]

At the two spectral endpoints,

\[
 (1-z)\frac{\widehat f(0)}{u(1)}=A_+,
 \qquad(1-z)\frac{\widehat f(\pi)}{u(-1)}=A_-.
\]

Expanding the spectral integral at theta=0,pi, or equivalently using the analytic Fourier-coefficient argument of Section 4, gives for r in a fixed positive multiple of sqrt(n)

\[
 \boxed{
 (1-z)(J_q^nf)_r=
 \frac{\mu_n(r)}2\left[A_++(-1)^{n+r}A_-\right]+o(n^{-1}).
 }\tag{12}
\]

Both endpoints are necessary. Keeping only theta=0 would give the wrong coefficient at large q; it would fail to recover the free walk's parity restriction. Finite phase shifts in the Jost waves change r by O(1), so they do not affect this diffusive-scale limit.

## 7. Sum the parity sectors and obtain the complete bulk coefficient

Equations (11)-(12) give the leading t as

\[
 \frac14\mu_p(u)\mu_n(r)
 [A_++(-1)^{n+r}A_-].
\]

For fixed total-spin parity, there are two r-parity sublattices, each with (r,u) lattice area four. Their squared amplitudes add:

\[
 (A_++A_-)^2+(A_+-A_-)^2=2(A_+^2+A_-^2).
\]

The uniform envelope (10) and the high-spin bound justify dominated passage to the two Riemann sums. Relative to the auxiliary crystal formula already derived, the multiplier is exactly \((A_+^2+A_-^2)/2\), not \(A_+^2\) and not \((A_++A_-)^2\).

An independent continuum expression for the spatial function is

\[
 \mathcal F(x)=\frac{(2/\pi)^{3/2}}{[x(1-x)]^3}
 \int_0^\infty\!\int_0^\infty
 \frac{A^2B^2}{A+B}
 e^{-A^2/x-B^2/(1-x)+(A+B)^2/2}\,dA\,dB.
\]

Set A=su and B=s(1-u), including the Jacobian s. Integrating \(s^4e^{-Ds^2}\) yields (2). This derives (1). No interchange of q and L limits is used.

## 8. Boundary-to-interior consistency, with the order of limits stated

The prior fixed-distance coefficient is

\[
 B_d(q)=\frac{(1-z)^2}{\sqrt{2\pi}}\|J_q^df\|^2.
\]

Its exact spectral integral above gives, for every fixed q>1,

\[
 \boxed{B_d(q)\sim\frac{\mathcal K(q)}{\pi\sqrt2}\,d^{-3/2}.}\tag{13}
\]

Indeed the spectral density times \(|\widehat f|^2\) has a quadratic zero at each endpoint, and \(\int_0^\infty e^{-d\theta^2}\theta^2d\theta=\sqrt\pi/(4d^{3/2})\). The two endpoint constants give (13).

This is the **iterated** limit: first L->infinity at fixed distance d, then d->infinity. It is not a uniform finite-L formula for all d. The independently proved bulk law has \(\mathcal F(x)\sim(\pi\sqrt2)^{-1}x^{-3/2}\) as x decreases to zero, agreeing with that overlap of scales; agreement itself was not used as a proof of either limiting law.

At q=1 the exact answer remains 1/L everywhere. Neither the bulk proof domain nor the fixed-q boundary expansion is uniform in this endpoint. No crossover size or physical transition is inferred from the auxiliary threshold q0.

## 9. Numerical checks, not a fitted theorem

For q=2.6 at the center, fresh evaluations of the complete recurrence give:

| L | Complete M | L^2 M | Derived limit |
|---:|---:|---:|---:|
| 160 | 0.000327223236878 | 8.3769148641 | 9.5557097705 |
| 320 | 0.0000858452260820 | 8.7905511508 | 9.5557097705 |
| 640 | 0.0000221061695045 | 9.0546870291 | 9.5557097705 |
| 1280 | 0.00000562933737190 | 9.2231063501 | 9.5557097705 |

At x=1/4 the coefficient is 13.7324246028..., so the normalized quarter-chain/center profile tends to 1.4370910097... (the exact ratio is F(1/4)/F(1/2)). These decimal evaluations are not certified numerical intervals. No fit determines a coefficient or exponent.

Direct small-Hilbert-space projections check the unchanged physical recurrence. Independently evaluated orthogonal-polynomial integrals check its auxiliary spectral dictionary. Harmonic recurrences normalized to unit asymptotic slope check both infinite-product amplitudes. The weighted-path tests check the actual quadrant kernel against the tilted positive majorant; they do not substitute a finite sample for its analytical proof.

## 10. What this changes, and what remains outside the result

Together with the established edge law,

\[
 M_{L,1}\sim\frac{\tanh(\ln q)}{\sqrt{2\pi L}},\qquad
 M_{L,\lfloor xL\rfloor}\sim\frac{\mathcal K(q)\mathcal F(x)}{L^2},
\]

the complete symmetry has parametrically different boundary and bulk memory in the proved domain. Compared with q=1, it enhances the unavoidable end-spin fraction but suppresses the unavoidable bulk fraction at sufficiently large L. Both fractions vanish; there is no nonzero thermodynamic plateau claimed.

This completes an explanation of the **symmetry-enforced baseline**, not of the full late-time value for every Hamiltonian in [D26]. The finite-H counterexamples in the first pilot remain valid. The random-kick model attains the baseline exactly, but is explicitly a different dynamical model. The result determines no superdiffusive exponent and does not imply that a single local operator stores an arbitrary quantum state.

## 11. Contribution and prior-art audit at the new claim

[D26] already reports anomalous transverse-spin dynamics and finite-size saturation, states that the one-generator Mazur bound is not tight, and improves it using nonlinear charges. It does not equate that one-charge estimate with the complete symmetry projection. This work does not claim to discover the role of nonlinear charges or to refute their simulations. It supplies the complete algebraic baseline, now with a bulk law at fixed finite deformation.

[MM] supplies the full-algebra memory framework and quantum-group multiplet structure. [H] supplies exact boundary/bulk memory calculations in pair-/p-flip representations and already motivates caution about finite-size exponents. Neither a matching abstract algebra nor a constrained-walk technique transfers its trace weights or local observable to the current spin-1/2 representation.

[KV] and [DS] supply the mathematical spectral machinery. They do not contain a spin-chain autocorrelation conclusion merely by containing the required Jacobi formulas. The added implication is the uniform control in Sections 4–5: in particular, all u-changing paths, atypically small spin sectors, parity, and large-spin tails are accounted for. The earlier unproved scattering guess is therefore replaced by a proved **restricted-domain** statement, not by numerical agreement with that guess.

The focused source check does not establish exhaustive priority. Some broad searches returned unrelated results and are not negative evidence. No source's plot data are extracted, and no independently reviewed status is claimed. A direct source containing the same complete finite-q memory law would change the novelty assessment.

**Decision:** continue toward a compact contribution review of the combined edge/bulk symmetry baseline. Do not automatically add weak-deformation crossover, other on-site representations, a full hydrodynamic theory, or large Hamiltonian simulations. The most consequential remaining comparison is whether and under what assumptions a selected generic dynamics exhausts this baseline; it must not be asserted merely because the static theorem is now complete in its declared parameter range. No repository is initiated in this pass.

## 12. Verification record

`check_bulk.py` has six groups. The first complete run passed. Exact finite identities use fixed tolerances; asymptotic tables are labeled diagnostics and are not used to promote fits to proofs. The largest new physical Hilbert-space projection has dimension 16. The 1,280-spin values use the unchanged polynomial-size recursion. Auxiliary matrices and scalar vectors are not physical spin-state simulations.

All three completed new runs passed six groups and produced byte-identical reports. The unchanged five-group asymptotics suite also passed and reproduced its canonical report exactly. The unchanged four-group original memory suite passed; twenty floating-point fields differ from its original report, with maximum absolute difference 8.881784197001252e-16. The original report was not replaced. All 29 incoming archive members and both nested integrity manifests are verified unchanged. `VERIFICATION.json` records the complete comparisons. The final proof drafting also corrected a copied spatial-ratio decimal and made the two reserved tilts explicit; these edits change neither the stated rate formula nor any test or tolerance. No original checker, canonical report, formula, or scientific tolerance is modified. Run with

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python check_bulk.py --output reproduced.json
```

## References and source boundaries

- **[D26]** L. V. Delacretaz, V. Gorbenko, J. Wang, B. Zan, A. Zhabin, *Hydrodynamic tails in chaotic spin chains with quantum group symmetry*, arXiv:2606.20850v1. Sections II, IV and Appendix F were reopened: https://arxiv.org/html/2606.20850v1 . No plotted plateau or transport exponent was remeasured.
- **[MM]** S. Moudgalya, O. I. Motrunich, *Hilbert Space Fragmentation and Commutant Algebras*, PRX 12, 011050 (2022), arXiv:2108.10324. Projection and representation framework inherited from the explicitly preserved reading record; the primary abstract was reopened this pass. https://arxiv.org/abs/2108.10324 . This is not a new full rereading of all examples.
- **[H]** O. Hart, *Exact Mazur bounds in the pair-flip model and beyond*, arXiv:2308.00738. The primary abstract was reopened; the predecessor's targeted full-text comparison remains in prior/SOURCES.md. https://arxiv.org/abs/2308.00738 . No formula is transferred across representations without checking trace weights.
- **[KV]** H. T. Koelink, J. Verding, *Spectral analysis and the Haar functional on the quantum SU(2) group*, arXiv:math/9412225. Sections 6, Eq.(6.2), Eq.(6.10) and following recurrence/orthogonality paragraphs were read in the primary PDF: https://arxiv.org/pdf/math/9412225 . Their group parameter is not our physical q; the dictionary uses base z=q^-2.
- **[DS]** D. Damanik, B. Simon, *Jost Functions and Jost Solutions for Jacobi Matrices, II. Decay and Analyticity*, arXiv:math/0502487, IMRN (2006), Article 19396. Theorem 1.5, Eqs.(1.12)–(1.13), (2.10), and Appendix A, especially Theorem A.4 and the Jost asymptotics, were checked in the primary text. https://arxiv.org/pdf/math/0502487 . The spectral facts are inherited; the moderate-window bound (8) and application to the spin recursion are derived above rather than attributed verbatim to that paper.
- **[DLMF]** NIST Digital Library of Mathematical Functions, §18.28(iii), Eqs.(18.28.7)–(18.28.8): https://dlmf.nist.gov/18.28 . Used only as an official normalization cross-check for the independently identified Al-Salam–Chihara measure. With our |a|,|b|<1, no discrete mass terms occur.

Third-party PDFs are not redistributed. The old attached Bell and electron papers are not used or imported.
