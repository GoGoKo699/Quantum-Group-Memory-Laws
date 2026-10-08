# From the recursion kernel to the bulk coefficient

This note supplies explicit intermediate steps for Sections 4–7 of the
[bulk proof](../archive/research-handoff-2026-10-08/prior/prior/FOLLOWUP.md).
The physical trace, finite recursion, and fixed-$`q`$ domain are those of
[THEOREM.md](THEOREM.md). The kernel time below counts recursion steps.

## 1. Subcritical comparison and spectral endpoints

Let $`P_0`$ have off-diagonal entries $`1/2`$ on $`\mathbb N_0`$, with killing at $`-1`$.
Suppose $`H=P_0+W`$, where $`W=\mathrm{diag}(w_r)`$, $`w_r\ge0`$ decays
exponentially, and $`\beta=2\sum_{r\ge0}(r+1)w_r<1`$. With $`v_{-1}=0`$,

```math
\langle v,(I-P_0)v\rangle=\frac12\sum_{r\ge-1}|v_{r+1}-v_r|^2,
\qquad |v_r|^2\le(r+1)\sum_{s=-1}^{r-1}|v_{s+1}-v_s|^2.
```

Thus $`W\le\beta(I-P_0)`$ as quadratic forms, so
$`I-H\ge(1-\beta)(I-P_0)`$ and $`H\ge P_0\ge-I`$. There are no eigenvalues outside
$`[-1,1]`$. To exclude bounded regular solutions at the endpoints, use

```math
G_0(r,s)=2\min(r+1,s+1),\qquad
\|G_0W\|_{\infty,h_0}\le\beta<1,\qquad h_0(r)=r+1,
```

where $`\|v\|_{\infty,h_0}=\sup_r|v_r|/(r+1)`$. A bounded solution of $`Hv=v`$
satisfies $`v=G_0Wv`$: the difference is a free regular solution $`c(r+1)`$,
and boundedness forces $`c=0`$. Here $`G_0Wv`$ is bounded because
$`\sum_s(s+1)w_s<\infty`$. Contraction therefore gives $`v=0`$. Conjugating a
solution at $`-1`$ by $`(-1)^r`$ gives instead $`v=-G_0Wv`$, with the same conclusion.

For the physical comparison kernel,
$`w_r=e^{\vartheta}(q^{-1}+q^{-3})q^{-2r}/2`$ and $`\beta=e^{\vartheta}b(q)`$.
The choice $`\vartheta=-\log b(q)/4`$ makes both required tilts subcritical:
$`e^{2\vartheta}b(q)=\sqrt{b(q)}<1`$.

## 2. The Jost integral is an adjacent-difference convolution

The inherited Jacobi input is exponential Jost analyticity and the spectral
density for an exponentially decaying perturbation of $`P_0`$ with no bound states
or endpoint resonances. [Damanik–Simon](https://arxiv.org/pdf/math/0502487),
Theorem 1.5 and Theorem A.4, especially (A.39)–(A.45), provide this input after
rescaling their off-diagonal normalization from $`1`$ to $`1/2`$. The previous
section verifies the endpoint assumptions for $`H`$. The explicit measure in
Section 6 of the bulk proof verifies them for $`J_q`$.

Write $`\mathsf J`$ for either operator, $`p_r`$ for its regular orthonormal
polynomials, and $`u`$ for the real-coefficient Jost function with $`u(0)>0`$ and

```math
d\mu(\theta)=\frac2\pi\frac{\sin^2\theta}{|u(e^{i\theta})|^2}\,d\theta.
```

The two Jost waves give

```math
p_r(\cos\theta)=
\frac{e^{i(r+1)\theta}u(e^{-i\theta})-e^{-i(r+1)\theta}u(e^{i\theta})}
{2i\sin\theta}+\varepsilon_r(\theta),
\qquad |\varepsilon_r(\theta)|\le C(r+1)e^{-\eta r}.
```

This error bound follows from the exponentially small tail of the Jost
solutions in a fixed annulus. At $`\theta=0,\pi`$, the numerator difference
vanishes; analytic differentiation bounds its quotient uniformly, including
the factor $`r+1`$.

For an exponentially decaying vector $`g`$ (a fixed polynomial factor is allowed),
put $`G(\theta)=\sum_sg_sp_s(\cos\theta)`$. On a sufficiently small annulus,

```math
F(\theta)=\frac{G(\theta)}{u(e^{i\theta})}
=\sum_{j\in\mathbb Z}c_je^{ij\theta},\qquad |c_j|\le Ce^{-\eta|j|}.
```

The spectral integral, extended from $`[0,\pi]`$ to the full circle, now gives

```math
(\mathsf J^ng)_r=\sum_{j\in\mathbb Z}c_j\Delta b_n(r+j)+E_{n,r},
\qquad |E_{n,r}|\le C(r+1)e^{-\eta r}n^{-3/2},\quad n\ge1,
```

where $`b_n(k)=2^{-n}\binom n{(n+k)/2}`$ and $`\Delta b_n(k)=b_n(k)-b_n(k+2)`$,
with wrong-parity and out-of-support binomial values zero. Indeed the leading
integral is

```math
\frac1{i\pi}\int_{-\pi}^{\pi}(\cos\theta)^n\sin\theta\,
e^{i(r+1)\theta}F(\theta)\,d\theta
=\sum_jc_j\Delta b_n(r+j).
```

The error uses $`\int_0^\pi|\cos\theta|^n\sin^2\theta\,d\theta=O(n^{-3/2})`$.
As a normalization check, $`\mathsf J=P_0`$ and $`g=e_0`$ give $`u=G=F=1`$,
$`c_j=\delta_{j0}`$, and $`E_{n,r}=0`$: the formula is exactly the killed-walk
reflection identity $`(P_0^n)_{r,0}=\Delta b_n(r)`$.

## 3. Uniform Gaussian bound and both endpoint amplitudes

Use the [support-qualified binomial identity](PROOF_MAP.md#support-qualification-for-the-archived-binomial-identity)
and reflection $`\Delta b_n(k)=-\Delta b_n(-k-2)`$. Stirling bounds give the
adjacent-difference Gaussian estimate uniformly on each fixed window
$`|k|\le B\sqrt{n\log(n+2)}`$. For $`r\le A\sqrt{n\log(n+2)}`$, split the convolution
at $`|j|=\sqrt{n\log(n+2)}`$. The outer tail is exponentially small. On the inner
part, $`(r+j)^2\ge r^2-2r|j|`$ and $`r/n\to0`$ allow the cross term to be absorbed
by $`e^{-\eta|j|}`$. The polynomial factor obeys
$`|r+j|+1\le(r+1)(|j|+1)`$. Therefore, for every $`0<\delta<1`$,

```math
|(H^ng)_r|\le C_{A,\delta,g,H}(r+1)n^{-3/2}
e^{-(1-\delta)r^2/(2n)}.
```

The exponentially small Jost error is absorbed in the same window. This
Gaussian estimate is a derived consequence, not a theorem about physical
spin dynamics or a quoted result of Damanik–Simon.

For $`r/\sqrt n`$ in a compact positive interval, let
$`\mu_n(r)=2\sqrt{2/\pi}(r+1)n^{-3/2}e^{-(r+1)^2/(2n)}`$.
For each bounded $`j`$, the adjacent difference is $`\mu_n(r)[1+o(1)]`$ on its
allowed parity and zero on the other parity. Exponential summability then gives

```math
(\mathsf J^ng)_r=\frac{\mu_n(r)}2
\bigl[F(0)+(-1)^{n+r}F(\pi)\bigr]+o(n^{-1}).
```

For $`\mathsf J=J_q`$, $`g=f`$, the products in the bulk proof identify
$`(1-z)F(0)=A_+`$ and $`(1-z)F(\pi)=A_-`$. Both endpoint amplitudes are required.

## 4. Matching and the parity density in the physical sum

Write $`p=i-1`$, $`n=L-i`$, and $`h=r+u+1`$. On compact positive intervals for
$`r/\sqrt L,u/\sqrt L`$, restrict first to at most $`R`$ changes of $`u`$ and initial
$`r_0\le R`$. The accumulated coefficient error is $`O(Lz^{u-R})=o(1)`$, and bounded
shifts of the initial multiplicity share the same Stirling limit. The omitted
path contribution, multiplied by $`L^2`$, is bounded by
$`C(e^{-\vartheta R}+e^{-c_qR})`$ using the two subcritical tilts and the
exponential insertion tail. Taking $`L\to\infty`$ before $`R\to\infty`$ yields

```math
t_{L,i}(h,r)=\frac14\mu_p(u)\mu_n(r)
[A_++(-1)^{n+r}A_-]+o(L^{-2}).
```

For $`u=A\sqrt L`$, $`r=B\sqrt L`$, define

```math
Q_x(A,B)=\frac{(2/\pi)^{3/2}}{[x(1-x)]^3}
\frac{A^2B^2}{A+B}
e^{-A^2/x-B^2/(1-x)+(A+B)^2/2}.
```

Uniformly on those compact intervals,

```math
2t_{L,i}^2/D_L(h)=L^{-3}Q_x(A,B)[A_++(-1)^{n+r}A_-]^2+o(L^{-3}).
```

The physical constraint $`r+u+1\equiv L\pmod2`$ leaves two sublattices,
distinguished by $`r`$ parity. Each has scaled cell area $`4/L`$. The integrable
envelope and large-spin bound in Section 4.3 of the bulk proof justify summing,
including the portions outside the compact intervals. Since
$`\mathcal F(x)=\int_0^\infty\!\int_0^\infty Q_x(A,B)\,dA\,dB`$, the multiplier is

```math
\frac{(A_++A_-)^2+(A_+-A_-)^2}{4}
=\frac{A_+^2+A_-^2}{2}=\mathcal K(q).
```

This fixes the normalization of the complete bulk law while retaining the
ordinary physical multiplicities and both spectral endpoints.
