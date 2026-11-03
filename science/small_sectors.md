# Exact conditional physical one-erasure maps

The first comparison can be done exactly before any limit in size or deformation. A conditional map below is conditioned on a particular erased position: its scalar pattern probability $`p(1-p)^{n-1}`$ is divided out. The output retains all surviving physical qubits.

For a fixed spin sector, its multiplicity-averaged embedding is

```math
\mathcal J_j(X)=\frac1{m_j}\sum_\alpha W_{j,\alpha}XW_{j,\alpha}^\dagger.
```

Erasing site $`i`$ gives the exact Kraus identity

```math
\mathcal L_{j,i}(X)=\sum_{\alpha,b}K_{\alpha,b}XK_{\alpha,b}^\dagger,
\qquad
K_{\alpha,b}=\frac1{\sqrt{m_j}}
(\langle b|_i\otimes I)W_{j,\alpha},\quad b=0,1.
```

This is an equality of completely positive maps, including arbitrary reference extensions. Fixing a pure multiplicity path instead of averaging it would be a different stationary-sector channel.

## Two qubits: the deformed triplet

Put $`D=1+r^2`$. In logical basis order $`+,0,-`$, the spin-one embedding has columns

```math
|00\rangle,\qquad
\frac{|01\rangle+r|10\rangle}{\sqrt D},\qquad
|11\rangle.
```

The spin-zero vector is $`(r|01\rangle-|10\rangle)/\sqrt D`$. Projection removes the coherence between these two sectors and preserves the full triplet matrix.

Erasing the right site has Kraus matrices

```math
K_0=\begin{pmatrix}1&0&0\\0&r/\sqrt D&0\end{pmatrix},\qquad
K_1=\begin{pmatrix}0&1/\sqrt D&0\\0&0&1\end{pmatrix}.
```

Erasing the left exchanges $`r`$ and $`1`$ in the two middle coefficients. The middle basis state reduces to $`\mathrm{diag}(1,r^2)/D`$ on the left and $`\mathrm{diag}(r^2,1)/D`$ on the right. Physical position already matters.

The normalized Choi state has nonzero spectrum

```math
\left\{\frac{1+2r^2}{3D},\frac{r^2+2}{3D}\right\}.
```

At $`r=1`$ this is the flat spectrum $`\{1/2,1/2\}`$ of symmetric one-particle loss. It is nonflat for every $`r\gt1`$. Thus unitary input and output basis changes cannot turn this conditional channel into its ordinary symmetric-loss counterpart: they preserve normalized Choi spectra.

For a maximally entangled triplet input, reverse hashing gives the conditional resource lower bound

```math
\log_2 3-h_2\!\left(\frac{1+2r^2}{3D}\right).
```

It exceeds $`\log_2 3-1`$ at $`r\gt1`$. This is an achievable entanglement rate for that conditional resource, not a capacity formula for the complete independently erased block.

### A full two-site rate changes with deformation

The conditional resource does give a charged achievable rate for the complete two-site channel when all erasure flags are included. Send half of a maximally entangled logical triplet. No loss has probability $`(1-p)^2`$ and supplies $`\log_2 3`$ ebits. Either one-loss pattern has probability $`p(1-p)`$ and supplies the reverse-hashing rate just derived. Two losses supply zero. Announcing the flags and distilling the pattern classes separately therefore achieves

```math
R_2(r,p)=(1-p^2)\log_2 3-2p(1-p)h_2(\lambda_r),
\qquad \lambda_r=\frac{1+2r^2}{3(1+r^2)}.
```

At $`r=1`$, binary entropy is one and this equals the inherited exact ordinary-permutation capacity

```math
f_2(p)=(1-p^2)\log_2 3-2p(1-p).
```

For every $`r\gt1`$ and $`0\lt p\lt1`$, $`\lambda_r\ne1/2`$ and therefore

```math
Q_2(\mathcal N_{2,r,p})\ge R_2(r,p)\gt f_2(p).
```

This strict finite-block improvement proves that the undeformed capacity formula does not persist unchanged. It is compatible with the size-independent finite-deformation ceiling. Equality with $`R_2`$ is not claimed.

## Three qubits: the two copies of spin one-half

Put $`S=1+r^2+r^4`$. The following columns give two orthonormal copies of the same logical spin-one-half representation:

```math
\begin{aligned}
A_+&=(r|010\rangle-|100\rangle)/\sqrt D,&
A_-&=(r|011\rangle-|101\rangle)/\sqrt D,\\
B_+&=(rD|001\rangle-|010\rangle-r|100\rangle)/\sqrt{DS},&
B_-&=(r^2|011\rangle+r^3|101\rangle-D|110\rangle)/\sqrt{DS}.
\end{aligned}
```

For each copy the physical coproduct obeys $`E V_+=0`$, $`F V_+=V_-`$, $`E V_-=V_+`$, and $`F V_-=0`$. The actual stationary-sector embedding is

```math
\mathcal J(X)=\tfrac12(AXA^\dagger+BXB^\dagger).
```

Erasing the first site, and ordering the survivor basis as $`00,01,10,11`$, gives

```math
\begin{aligned}
K_{A0}&=\frac1{\sqrt{2D}}
\begin{pmatrix}0&0\\0&0\\r&0\\0&r\end{pmatrix},&
K_{A1}&=\frac1{\sqrt{2D}}
\begin{pmatrix}-1&0\\0&-1\\0&0\\0&0\end{pmatrix},\\
K_{B0}&=\frac1{\sqrt{2DS}}
\begin{pmatrix}0&0\\rD&0\\-1&0\\0&r^2\end{pmatrix},&
K_{B1}&=\frac1{\sqrt{2DS}}
\begin{pmatrix}-r&0\\0&r^3\\0&-D\\0&0\end{pmatrix}.
\end{aligned}
```

Other sites follow by taking the indicated physical partial matrix element of $`A,B`$, without assuming permutation covariance. Their Choi spectra are:

| Erased site | Nonzero normalized Choi eigenvalues |
|---|---|
| Either end | $`1/4,\ 1/4,\ (r^2+2)/(4S),\ r^2(1+2r^2)/(4S)`$ |
| Middle | $`[1+(r^2-1)/\sqrt S]/4`$ twice and $`[1-(r^2-1)/\sqrt S]/4`$ twice |

At $`r=1`$ both spectra are $`1/4`$ four times. At every $`r\gt1`$ they differ. Multiplicity averaging therefore does not restore ordinary permutation covariance of physical loss.

## Consequence for the proof route

The ordinary Schur/symmetric-loss results remain the exact $`r=1`$ benchmark. Their flat Choi resources and covariant simulation cannot be imported by identifying abstract matrix blocks. The finite-deformation ceiling instead uses the [first-erased-mismatch estimate](first_mismatch.md) and a [direct complementary-channel entropy bound](capacity.md).

[Verification](../verification/README.md) checks these Kraus maps, charge and ladder conventions, reference-stable matrix-unit identities, and the estimator probabilities independently. Finite checks support the formulas; they do not replace the all-path analytical argument.
