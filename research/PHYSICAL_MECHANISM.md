# Why the spatial memory laws differ

The [spatial theorem](THEOREM.md) concerns the ordinary infinite-temperature
projection of a local Pauli operator onto the complete symmetry algebra. Its
different end and interior powers come from the local operator's overlap within
spin sectors. The sector dimensions and their physical trace weights are
unchanged by finite real deformation. This account separates that exact
decomposition from the large-size estimates that evaluate it.

There is a direct physical readout in the [local averaged model](LOCAL_REALIZATION.md).
Prepare $`\rho_i(p)=2^{-L}(I+pX_i)`$ with $`|p|\le1`$: spin $`i`$ is polarized and
the other spins are maximally mixed. For its Schrödinger generator $`\mathcal G_*`$,
duality and preservation of the maximally mixed state give

```math
\operatorname{Tr}\!\left[X_i e^{t\mathcal G_*}\rho_i(p)\right]
=pC_i(t)\longrightarrow pM_{L,i}(q).
```

Thus $`M`$ is the retained same-site polarization fraction in that model. The
identity holds for every allowed $`p`$, without a small-polarization approximation.
Long time is taken at fixed finite $`L`$ and positive noise strength. For an
isolated symmetry-preserving Hamiltonian, the same preparation measures $`pC_i(t)`$,
whose time average can include the [Hamiltonian-specific excess](PLATEAU_DICTIONARY.md).

## 1. An exact conditional-sector formula

For the decomposition

```math
\mathcal H_L=\bigoplus_h\mathcal V_{h/2}\otimes\mathbb C^{m_{L,h}},
\qquad D_L(h)=2^{-L}m_{L,h},
```

define the sector probability and the multiplicity-averaged local operator by

```math
p_{L,h}=(h+1)D_L(h),\qquad
\overline X_{L,i;h}=
\frac{\operatorname{Tr}_{m_{L,h}}(P_hX_iP_h)}{m_{L,h}}.
```

The sum is over parity-compatible sectors with nonzero multiplicity. Although
their embeddings depend on $`q`$, their ranks do not: $`\sum_h p_{L,h}=1`$, and
$`p_{L,h}`$ is independent of $`q`$. The projection formula gives exactly

```math
M_{L,i}(q)=\sum_h p_{L,h}\,\eta_{L,i;h}(q),\qquad
\eta_{L,i;h}=\frac{\|\overline X_{L,i;h}\|_{\rm HS}^2}{h+1}.
\tag{1}
```

Here $`\eta`$ is the normalized squared overlap conditioned on a sector,
with $`0\le\eta\le1`$. It is an operator-space quantity, not a probability of
measuring a spin in a particular direction. In the magnetic ladder basis,
write $`\alpha_{L,i}(h,r)=T_{L,i}(h,r)/m_{L,h}=t_{L,i}(h,r)/D_L(h)`$ for
the multiplicity-averaged raising matrix element, $`0\le r<h`$. Then

```math
\eta_{L,i;h}=\frac{2}{h+1}\sum_{r=0}^{h-1}
|\alpha_{L,i}(h,r)|^2.
\tag{2}
```

The factor two includes raising and lowering. The [finite recursion](../archive/research-handoff-2026-10-08/prior/prior/prior/prior/PILOT.md)
computes this multiplicity average before squaring it; an average of squared
matrix elements would be a different quantity.

The binomial multiplicity formula implies that $`h`$ is typically of order
$`\sqrt L`$. More precisely, the probability measures assigning mass $`p_{L,h}`$
to $`h/\sqrt L`$ converge to the density

```math
\rho(y)=\sqrt{\frac2\pi}\,y^2e^{-y^2/2},\qquad y>0.
\tag{3}
```

The spacing of allowed $`h`$ is two. Thus
$`p_{L,h}\sim2\rho(y)/\sqrt L`$ when $`h/\sqrt L\to y>0`$.
This same distribution underlies all the deformation regimes below.

## 2. Ordinary spin symmetry: a uniform local overlap

At $`q=1`$, permutation symmetry makes every local spin have the same projection,
$`\Pi_1(X_i)=L^{-1}\sum_jX_j`$. In the spin-$`h/2`$ sector this is
$`2S^x/L`$, giving

```math
\eta_{L,i;h}(1)=\frac{h(h+2)}{3L^2},\qquad
\sum_h p_{L,h}h(h+2)=3L.
```

Equation (1) therefore gives $`M_{L,i}(1)=1/L`$ exactly. The second identity is
also the ordinary trace identity $`4\langle\boldsymbol S^2\rangle=3L`$.

## 3. A deformed end spin: a short magnetic-ladder profile

Fix finite $`q>1`$ and put $`z=q^{-2}`$. On sectors with
$`h/\sqrt L\to y>0`$, the exact right-end insertion formula gives, for fixed $`r`$,

```math
\alpha_{L,L}(h,r)\longrightarrow\frac{1-z}{2}f_r,\qquad
f_r=q^{-r}\sqrt{1-z^{r+1}},\qquad
\sum_{r\ge0}f_r^2=\frac1{1-z^2}.
```

Only a bounded range of ladder entries remains appreciable at fixed $`q`$;
the profile has an exponential tail. Its squared norm stays of order one,
whereas the irrep dimension $`h+1`$ grows as $`\sqrt L`$. Consequently,

```math
\eta_{L,L;h}(q)\sim
\frac{1-z}{2(1+z)(h+1)}.
```

The [edge proof](../archive/research-handoff-2026-10-08/prior/prior/prior/FOLLOWUP.md)
controls the other sectors and the errors. In particular,
$`\sum_hD_L(h)=2^{-L}\binom L{\lfloor L/2\rfloor}`$ yields

```math
M_{L,L}(q)=\frac{\tanh(\log q)}{\sqrt{2\pi L}}+O_q(L^{-1}).
```

Reflection followed by a global spin flip gives the same left-end value.
This is a magnetic-ladder statement inside each irrep; it is not a claim
about a localized dynamical mode or a nonzero limiting end plateau.

## 4. An interior spin: small overlaps across a growing ladder

Fix $`q>q_0`$, with the sufficient hypothesis $`b(q)<1`$ from the theorem, and
take $`i/L\to x\in(0,1)`$. Put $`\ell=i-1`$, $`n=L-i`$, and $`u=h-r-1`$.
The proved matching on positive compact ranges of $`u/\sqrt L,r/\sqrt L`$ is

```math
t_{L,i}(h,r)=\frac14\mu_\ell(u)\mu_n(r)
\big[A_+(q)+(-1)^{n+r}A_-(q)\big]+o(L^{-2}),
```

```math
\mu_N(v)=2\sqrt{\frac2\pi}(v+1)N^{-3/2}
e^{-(v+1)^2/(2N)}.
```

Here $`\mu`$ is the smooth interpolation of the nonzero binomial
multiplicities; it is not set to zero on the other parity sublattice.
Both factors $`\mu`$ are of order $`L^{-1}`$ and $`D_L(h)`$ is of order
$`L^{-1}`$, so each averaged entry $`\alpha=t/D`$ is of order $`L^{-1}`$.
There are of order $`\sqrt L`$ such entries. Their squared norm is therefore
of order $`L^{-3/2}`$, and division by $`h+1`$ in (2) gives order $`L^{-2}`$.

These powers explain the mechanism; the equality and coefficient require
the [uniform bulk proof](../archive/research-handoff-2026-10-08/prior/prior/FOLLOWUP.md).
Its envelope controls small ladder coordinates and atypical spin sectors,
so the count above does not discard contributions that might change the
power. The two magnetic parities average the squared bracket to
$`A_+^2+A_-^2`$, giving
$`\mathcal K(q)=(A_+^2+A_-^2)/2`$ and the spatial profile $`\mathcal F(x)`$.
These are recursion estimates, not an assumed diffusion law in physical time.

Thus $`q`$ changes the sector-conditioned local overlaps while leaving both
$`p_{L,h}`$ and $`\dim\mathcal A_q=\binom{L+3}{3}`$ unchanged. Equation (1)
does not give a sum rule over sites or imply movement of memory between sites.

## 5. An elementary form of the bulk profile

The integral in the theorem can be evaluated without further asymptotics:

```math
\begin{aligned}
\mathcal F(x)={}&\frac1{2\pi}
\left[\frac{\sqrt{2-x}}{x^{3/2}}+
\frac{\sqrt{1+x}}{(1-x)^{3/2}}\right]\\
&+\frac{3\sqrt2}{4\pi\sqrt{x(1-x)}}
\left[\operatorname{arsinh}\sqrt{\frac{2x}{1-x}}+
\operatorname{arsinh}\sqrt{\frac{2(1-x)}x}\right],\quad0<x<1.
\end{aligned}
\tag{4}
```

For a direct derivation put $`a=x(1-x)`$, $`c=1-2x`$, and
$`t=\sqrt{2/a}(u-x)`$ in that integral. Its prefactor becomes
$`3\sqrt2/(\pi a^{5/2})`$, and the remaining numerator is
$`[a+c\sqrt{a/2}\,t-at^2/2]^2`$. An antiderivative after division by
$`(1+t^2)^{5/2}`$ is

```math
G(t)=\frac{a^2}{4}\operatorname{arsinh}t+
\frac{3a^2t/4+ac\sqrt{a/2}\,t^2+ac^2t^3/6}{(1+t^2)^{3/2}}.
```

Differentiation verifies this identity using $`c^2=1-4a`$.
Evaluating at $`t=-\sqrt{2x/(1-x)}`$ and $`t=\sqrt{2(1-x)/x}`$ gives (4).
In particular,

```math
\mathcal F(1/2)=\frac{2\sqrt3+3\sqrt2\operatorname{arsinh}\sqrt2}{\pi}
=2.650593017679487\ldots,
\qquad
\frac{\mathcal F(1/4)}{\mathcal F(1/2)}=1.437091009736557\ldots.
```

Positivity, reflection symmetry, and
$`\mathcal F(x)\sim(\pi\sqrt2)^{-1}x^{-3/2}`$ as $`x\downarrow0`$
are explicit. This endpoint behavior does not supply a uniform finite-chain
boundary-to-bulk interpolation. The normalized interior shape is the ratio
$`\mathcal F(x)/\mathcal F(1/2)`$; $`\mathcal F`$ is not a probability density.

## 6. A concrete local dynamics and its undeformed limit

Write $`\eta=\log q`$. The two-site reflection in the local realization is

```math
U_j=\frac{I+Z_jZ_{j+1}}2+
\frac{\operatorname{sech}\eta}{2}(X_jX_{j+1}+Y_jY_{j+1})-
\frac{\tanh\eta}{2}(Z_j-Z_{j+1}).
```

It fixes the aligned-spin states and has middle block

```math
\begin{pmatrix}-\tanh\eta&\operatorname{sech}\eta\\
\operatorname{sech}\eta&\tanh\eta\end{pmatrix},
```

whose square is the identity. This equals $`I-2(qI-R_j)/(q+q^{-1})`$, so it preserves the full
quantum-group algebra. Independent Poisson kicks on every bond, with positive
rates $`\gamma_j`$, give
$`\mathcal S(O)=\sum_j\gamma_j(U_jOU_j-O)`$ after averaging over their unrecorded
times. Taking $`H=0`$ is already a complete local realization. A coherent local
choice is $`H=\sum_j J_jU_j`$ with real $`J_j`$; every term commutes with the full
symmetry algebra, so the [contraction proof](LOCAL_REALIZATION.md#2-add-coherent-local-interactions-without-changing-the-limiting-projection)
gives the same limiting projection.

At $`q=1`$, $`U_j`$ is SWAP. For $`H=0`$, the one-spin operators form a closed subspace:

```math
\mathcal S(X_i)=\gamma_{i-1}(X_{i-1}-X_i)
+\gamma_i(X_{i+1}-X_i),
```

with absent end terms omitted. Their coefficients obey a continuous-time random
walk on a connected path with symmetric positive edge rates. Its stationary
probability vector is uniform, giving
$`e^{t\mathcal S}X_i\to L^{-1}\sum_kX_k`$ and $`M_{L,i}(1)=1/L`$ by Pauli
orthogonality. This closed single-site evolution applies to $`q=1`$, $`H=0`$;
the general deformed model uses the stationary-algebra proof. Its relaxation
scaling is not obtained from this undeformed check.

The [source comparison](../literature/ATTRIBUTION.md) derives the conversion
between Pauli and ladder-operator normalizations and the exact equivalence
between reflection noise and Hermitian Temperley–Lieb jumps. The local mechanism
is inherited; the evaluated spatial profile specifies what polarization it retains.
