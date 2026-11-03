# A uniform estimate from the first erased mismatch

This proof controls every finite $`r`$-Clebsch–Gordan path and every magnetic label, with no promise on the final spin or the physical multiplicity. It estimates a classical label from observations available in the erasure environment. The [capacity proof](capacity.md) applies that estimate to arbitrary coherent, reference-entangled inputs.

Fix $`r\gt1`$, $`z=r^{-2}\in(0,1)`$, and erasure probability $`0\lt p\lt1`$. All constants below depend only on these two fixed parameters.

## 1. Backwards Clebsch–Gordan probabilities

A multiplicity path has doubled spins

```math
K_0=0,\ K_1,\ldots,K_n=K,\qquad
K_t\ge0,\qquad \epsilon_t=K_t-K_{t-1}\in\{+1,-1\}.
```

The final irrep has logical weights $`h=0,\ldots,K`$, with doubled magnetization $`2h-K`$. Its physical up-spin count is $`(n-K)/2+h`$. Fixing a path and a final weight gives one pure physical state. Its computational-basis probabilities can be generated backwards, from $`t=n`$ to $`1`$.

At a step put $`k=K_t`$, $`J=K_{t-1}`$, and let $`h`$ denote the current logical weight. The emitted physical spin $`s_t`$ is $`+1`$ for up and $`-1`$ for down. Squaring the normalized Clebsch–Gordan coefficients gives:

| Path edge | Emitted spin | Probability | Predecessor weight |
|---|---|---|---|
| $`k=J+1`$ | $`+1`$ | $`(1-z^h)/(1-z^k)`$ | $`h-1`$ |
| $`k=J+1`$ | $`-1`$ | $`z^h(1-z^{k-h})/(1-z^k)`$ | $`h`$ |
| $`k=J-1`$ | $`+1`$ | $`z^{h+1}(1-z^{k+1-h})/(1-z^{k+2})`$ | $`h`$ |
| $`k=J-1`$ | $`-1`$ | $`(1-z^{h+1})/(1-z^{k+2})`$ | $`h+1`$ |

Invalid predecessor weights have zero probability. The two entries on each edge sum to one. The first upward edge has $`k\ge1`$, so no zero denominator occurs. The signed coefficients themselves are the physical ones in the [finite recursion](../archive/research-handoff-2026-10-08/prior/prior/prior/prior/check_memory.py); a downward coefficient's sign disappears only in this computational-basis probability calculation. For a fixed physical word, its intermediate weights are unique, so this backwards description omits no interference between alternative trajectories.

Define a **mismatch** by $`s_t\ne\epsilon_t`$. On either edge a mismatch leaves the predecessor weight equal to $`h`$, whereas a matching spin changes it by $`-\epsilon_t`$.

Let $`\delta=K-h_n`$ be the initial distance from the top of the final irrep. After any number of backwards emissions,

```math
h_t-K_t=-\delta+S_t,
```

where $`S_t`$ starts at zero, increases by one at an upward-edge mismatch, decreases by one at a downward-edge mismatch, and otherwise stays fixed. At the root, $`h_0=K_0=0`$, so the final net value of $`S`$ equals $`\delta`$. The total number $`N`$ of physical mismatches therefore satisfies $`N\ge\delta`$.

## 2. The first erased mismatch

The erasure environment knows the erased positions and their physical computational-basis values. Fix the path, scan these positions from right to left, and let $`\tau`$ be the first erased mismatch. Put $`\tau=\infty`$ if there is none. Let $`G`$ count the nonerased mismatches before $`\tau`$; if there is no event, count all mismatches.

Each physical mismatch is independently erased with probability $`p`$. Hence, for every integer $`g\ge0`$,

```math
\Pr(G\ge g)\le(1-p)^g,
\qquad
\Pr(\tau=\infty\mid\delta)
=\mathbb E[(1-p)^N]\le(1-p)^\delta.
```

The first inequality is valid even when the finite word contains fewer than $`g`$ mismatches. It uses the iid erasure marks on the actual mismatch sequence, without conditioning on a future favorable event.

Before the first observed mismatch, at most $`g`$ hidden mismatches imply $`|S_t|\le g`$. The mismatch probability $`q_t`$ from the preceding table always obeys

```math
q_t\le C_z z^{h_t},\qquad C_z=\frac1{1-z}.
```

If also $`\delta\gt g`$, then $`K_t-h_t=\delta-S_t\ge1`$ and

```math
q_t\ge c_z z^{h_t},\qquad c_z=z(1-z).
```

For an upward edge the factor multiplying $`z^h`$ is $`(1-z^{k-h})/(1-z^k)`$; its lower bound $`1-z`$ requires $`k-h\ge1`$. For a downward edge the additional factor $`z`$ gives the common lower constant. The only excluded upward boundary is $`h=k`$, where the mismatch probability vanishes. The proof uses the lower bound only when $`\delta\gt g`$, so that boundary is handled explicitly.

Define the deterministic exposure increment $`a_t=z^{K_t}`$ at physical site $`t`$. Let $`A_t=\sum_{s=t}^n z^{K_s}`$ be the exposure through that site in the right-to-left scan, and let $`A_{\tau^-}=\sum_{s=\tau+1}^n z^{K_s}`$ denote exposure strictly before the event. Before $`\tau`$, while the hidden count stays at most $`g`$,

```math
p c_z z^{-\delta+g}a_t\le p q_t
\le p C_z z^{-\delta-g}a_t,
```

with the lower inequality requiring $`\delta\gt g`$.

For the lower-hazard survival bound, stop the process also at its $`(g+1)`$st hidden mismatch. Conditional on any current surviving state, the probability of no observed mismatch at that step is at most $`1-pc_z z^{-\delta+g}a_t`$. Killing at the additional stop can only reduce survival. Iteration and $`1-x\le e^{-x}`$ bound survival through any deterministic exposure prefix by the exponential of minus its lower cumulative hazard. If a prefix has no reachable state satisfying the weight and hidden-count constraints, its killed survival probability is zero. This argument never conditions a transition probability on a future event such as $`G\le g`$.

## 3. A path-uniform estimator

For finite $`\tau`$, use

```math
\widehat\delta=\mathrm{clip}_{[0,K]}(\log_z A_\tau).
```

Set $`\widehat\delta=0`$ when there is no observed mismatch. The estimator uses the known path and the environment's erased-bit observations only.

For an integer error threshold $`t\ge3`$, let $`g=\lfloor t/3\rfloor`$. The following bounds hold for every length, path, final spin and initial weight.

**Overestimation.** The event $`\widehat\delta-\delta\ge t`$ implies

```math
A_\tau z^{-\delta}\le z^t.
```

On $`G\le g`$, summing the upper observed hazard over the deterministic prefix with exposure at most $`z^{\delta+t}`$ gives

```math
\Pr(\widehat\delta-\delta\ge t)
\le(1-p)^g+p C_z z^{t-g}.
```

This union bound needs no lower hazard and includes weights arbitrarily close to the top boundary.

**Underestimation at a finite event.** This event requires $`\delta\ge t\gt g`$ and implies $`A_\tau z^{-\delta}\ge z^{-t}`$. Before that event on $`G\le g`$, nonnegative current weight gives $`K_\tau\ge\delta-g`$. The current exposure jump is therefore at most $`z^{\delta-g}`$, and

```math
A_{\tau^-}z^{-\delta}
\ge z^{-t}-z^{-g}
\ge(1-z)z^{-t}.
```

The deterministic prefix first crossing exposure $`(1-z)z^{\delta-t}`$ occurs strictly before the observed event. The killed survival bound above applies to it. Adding the hidden-count tail and the no-event case gives

```math
\Pr(\delta-\widehat\delta\ge t)
\le(1-p)^g+
\exp[-p z(1-z)^2z^{g-t}]+(1-p)^t.
```

The last term follows from $`\Pr(\tau=\infty\mid\delta)\le(1-p)^\delta`$ and $`\delta\ge t`$. Thus finite-path censoring is part of the bound.

Combining the two tails,

```math
\Pr(|\widehat\delta-\delta|\ge t)\le B_t,
```

where

```math
\begin{aligned}
B_t={}&2(1-p)^{\lfloor t/3\rfloor}
+\frac{p}{1-z}z^{t-\lfloor t/3\rfloor}\\
&+\exp[-p z(1-z)^2z^{\lfloor t/3\rfloor-t}]
+(1-p)^t.
\end{aligned}
```

Three terms decay exponentially, and the remaining term decays faster than exponentially. In particular

```math
M=3+\sum_{t=3}^\infty\min\{1,B_t\}\lt\infty,
\qquad
\mathbb E|\widehat\delta-\delta|\le M.
```

Every bound is uniform in $`\delta`$, rather than only in a selected prior.

## 4. Bounded posterior entropy

Let the logical label have any prior and let $`O`$ be the full erasure pattern and erased physical bits. Round $`\widehat\delta(O)`$ to an integer $`\widetilde\delta(O)`$ in $`[0,K]`$. Then the integer error $`D_\mathrm{err}=\delta-\widetilde\delta(O)`$ has mean absolute value at most $`m=M+1`$ under every prior.

Let

```math
g_2(m)=(m+1)\log_2(m+1)-m\log_2m.
```

Specifying an integer's sign costs at most one bit. A nonnegative integer of mean at most $`m`$ has entropy at most the geometric-distribution value $`g_2(m)`$. Therefore

```math
\boxed{
H(h\mid O)=H(\delta\mid O)
=H(D_\mathrm{err}\mid O)
\le1+g_2(M+1)=:C(r,p)\lt\infty.}
```

This holds for every CG path and every prior. Supplying additional observations cannot weaken it.

An elementary closed bound may replace the series. Set $`a=1-p`$, $`A=pz(1-z)^2`$ and $`b=-2\ln z`$. Grouping $`t=3k,3k+1,3k+2`$ gives

```math
M\le\overline M=
3+\frac{6a}{p}
+\frac{p z^2(1+z+z^2)}{(1-z)(1-z^2)}
+\frac{3e^{-A}}{Ab}+\frac{a^3}{p}.
```

For the faster-than-exponential term, use

```math
\sum_{k\ge1}e^{-A e^{bk}}
\le\int_0^\infty e^{-A e^{bx}}\,dx
\le\frac{e^{-A}}{Ab}.
```

Thus $`1+g_2(\overline M+1)`$ is also an explicit finite ceiling. The constants are nonsharp and may diverge in deformation or noise limits. The argument assumes fixed finite $`r\gt1`$ and fixed $`p\gt0`$ throughout; it never takes a singular generator limit.

The next step is the [reference-stable capacity theorem](capacity.md). [Verification](../verification/README.md) independently compares these probabilities with signed physical CG amplitudes and exhaustively enumerated physical words and erasure flags on finite systems.
