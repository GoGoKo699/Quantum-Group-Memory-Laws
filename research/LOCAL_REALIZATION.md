# Local interacting realization of the full symmetry-memory law

This note gives an operational corollary and interpretation of the quantum-group spin-memory result. Its asymptotic formulas and parameter domains are unchanged. The derivation is author-side, not independent review.

## 1. Unchanged setting

Use the finite open spin-1/2 chain and ordinary normalized Hilbert--Schmidt inner product

```math
\langle A,B\rangle_2=2^{-L}\operatorname{Tr}(A^\dagger B).
```

The full real-q symmetry algebra, its image in this physical representation, and its orthogonal projection are denoted by $`\mathcal A_q`$ and $`\Pi_q`$. In particular

```math
M_{L,i}(q)=\|\Pi_q X_i\|_2^2,\qquad \|X_i\|_2^2=1.
```

No quantum-dimension-weighted trace is used. The finite definition and spatial asymptotics remain exactly those in [the preserved theorem](THEOREM.md). The polynomial-size algebra image must not be described as exponentially fragmented.

The previously established local noise uses the inherited two-site Hecke matrices, in the ordered basis up-up, up-down, down-up, down-down,

```math
R(q)=\begin{pmatrix}q&0&0&0\\0&0&1&0\\0&1&q-q^{-1}&0\\0&0&0&q\end{pmatrix}.
```

They have eigenvalues $`q,-q^{-1}`$. With their chain embeddings $`R_j`$, set

```math
P_j=\frac{qI-R_j}{q+q^{-1}},\qquad U_j=I-2P_j,
\qquad \mathcal S(O)=\sum_{j=1}^{L-1}\gamma_j(U_jOU_j-O),\quad\gamma_j>0.
```

Each $`U_j`$ is a Hermitian two-site unitary. The dynamics is averaged over unrecorded Poisson-distributed kicks; an individual unitary trajectory is not asserted to converge to the projection.

The kernel is

```math
\ker\mathcal S=\{O:[O,R_j]=0\ \forall j\}=\mathcal A_q.
```

The second equality is the inherited q-Schur--Weyl commutant relation for this representation. At $`q=1`$ this is the ordinary Schur--Weyl limit. The zero-noise spin Hamiltonians and the random-eigenbasis benchmark remain distinct from this noise-averaged model.

## 2. Add coherent local interactions without changing the limiting projection

Let $`H=H^\dagger`$ commute with every element of $`\mathcal A_q`$. In particular, the previously studied quantum-group-preserving nearest- and next-nearest-neighbor Hamiltonians qualify. Locality of $`H`$ is not necessary for the algebraic proof; choosing that subclass makes the complete physical generator local.

For any fixed $`\varepsilon>0`$, define the Heisenberg generator

```math
\mathcal G_\varepsilon(O)=i[H,O]+\varepsilon\mathcal S(O).
```

For each finite $`L\ge2`$, define the strictly positive finite-size gap

```math
\delta_L=\min_{R\perp\mathcal A_q,\ R\ne0}
\frac{-\langle R,\mathcal S(R)\rangle_2}{\|R\|_2^2}>0.
```

Then

```math
\boxed{\|e^{t\mathcal G_\varepsilon}(I-\Pi_q)O\|_2
\le e^{-\varepsilon\delta_L t}\|(I-\Pi_q)O\|_2.}
```

In particular the infinite-temperature Pauli autocorrelation obeys

```math
\boxed{|C_{i,\varepsilon}(t)-M_{L,i}(q)|
\le[1-M_{L,i}(q)]e^{-\varepsilon\delta_Lt},}
```

and

```math
\boxed{\lim_{t\to\infty}C_{i,\varepsilon}(t)=M_{L,i}(q).}
```

This equality holds for each nonzero noise strength, without Haar eigenvectors, level-repulsion assumptions, integrability, or nonintegrability. It makes no bound on the scaling of $`\delta_L`$ with chain size or deformation. It is not a rapid-mixing result.

### Proof

The noise Dirichlet form is

```math
-\langle O,\mathcal S(O)\rangle_2
=\frac12\sum_j\gamma_j\|[U_j,O]\|_2^2.
```

It is nonnegative and vanishes exactly on the common commutant. Since the operator space is finite-dimensional, the positive gap on its orthogonal complement exists.

Write $`\mathcal K=i[H,\cdot]`$. It is skew-adjoint in this inner product. Since $`H`$ commutes with the full algebra,

```math
\mathcal K\Pi_q=\Pi_q\mathcal K=0,
\qquad\mathcal S\Pi_q=\Pi_q\mathcal S=0.
```

Thus $`\mathcal G_\varepsilon`$ leaves both the algebra and its orthogonal complement invariant and acts as zero on the algebra. For $`R(t)`$ in the complement,

```math
\frac d{dt}\|R(t)\|_2^2
=2\varepsilon\langle R(t),\mathcal S R(t)\rangle_2
\le-2\varepsilon\delta_L\|R(t)\|_2^2.
```

Gronwall's inequality proves the contraction. Writing $`X_i=\Pi_qX_i+R_i`$ and using orthogonality gives

```math
C_{i,\varepsilon}(t)=M_{L,i}+\langle R_i,e^{t\mathcal G_\varepsilon}R_i\rangle_2.
```

Cauchy--Schwarz and $`\|R_i\|_2^2=1-M_{L,i}`$ give the displayed correlation bound. This proof does not assume diagonalizability of the full generally nonnormal generator and excludes persistent nonzero-frequency modes in this stated class.

The same conclusion holds for products of propagators with different symmetry-preserving Hamiltonians and fixed $`\mathcal S`$. Each factor preserves $`\Pi_q`$ and contracts its complement by the corresponding duration, so the product contracts by total duration in either time ordering. This is sufficient for the piecewise-constant control tested here, without confusing the order of Schrödinger and Heisenberg propagators.

## 3. An explicit order-of-limits distinction

For fixed finite $`L`$,

```math
\lim_{\varepsilon\downarrow0}\lim_{t\to\infty}C_{i,\varepsilon}(t)=M_{L,i}.
```

On the other hand, continuity of finite-dimensional propagators gives the closed-system correlation at every fixed time as $`\varepsilon\downarrow0`$. Its time average is

```math
\lim_{T\to\infty}\frac1T\int_0^T
\left[\lim_{\varepsilon\downarrow0}C_{i,\varepsilon}(t)\right]dt
=\overline C_{i,0}=M_{L,i}+\Delta_{H,i},\quad\Delta_{H,i}\ge0.
```

The [preserved plateau dictionary](PLATEAU_DICTIONARY.md) identifies $`\Delta_{H,i}`$ exactly and includes finite local Hamiltonians with strict excess. Closed finite-system oscillations require a Cesàro average, not an unjustified pointwise limit. No simultaneous limit of $`L`$, $`t`$, and $`\varepsilon`$ is inferred.

The description is therefore: symmetry-preserving noise eliminates Hamiltonian-specific extra stationary information while retaining the symmetry contribution. It is not a claim that arbitrary laboratory noise improves storage or that the noiseless chaotic-chain plateau is solved.

## 4. Two hypothesis controls

**All bonds are a sufficient connectivity condition.** Removing the middle bond at $`L=4`$, setting $`H=0`$, and retaining the two separated bond channels increases the stationary-operator dimension from 35 to 100. At $`q=2.6`$, for the first spin, the plateau is $`0.5`$ rather than the connected-chain value $`0.2710324357256192`$. This does not prove that every missing bond prevents the conclusion when a Hamiltonian couples across that cut; the proof uses a sufficient condition.

**Preserving only total magnetization is insufficient.** Keep all bond channels, but choose

```math
H=\frac\omega2\sum_jZ_j.
```

This does not commute with the full raising/lowering algebra. Its protected transverse component rotates:

```math
\langle\Pi_qX_i,e^{t\mathcal G_\varepsilon}\Pi_qX_i\rangle_2
=M_{L,i}\cos(\omega t).
```

The remaining component decays, but the correlation need not approach a constant. The tests distinguish this from full strong-symmetry preservation; a generic weakly symmetry-covariant model is not substituted for the theorem's conditions.

## 5. Same number of conserved directions, different spatial overlap

For every finite real $`q\ge1`$,

```math
\dim\mathcal A_q=\sum_{h\equiv L\ (2)}(h+1)^2=\binom{L+3}{3}.
```

Let $`\mathcal P_L`$ be the $`4^L`$ Hermitian Pauli strings. They are an orthonormal basis in the normalized inner product. The trace of an orthogonal projection equals its rank, so

```math
\boxed{\sum_{P\in\mathcal P_L}\|\Pi_qP\|_2^2=\binom{L+3}{3}.}
```

This elementary identity is not a new sum rule to promote separately. It explains why the result must not be phrased as deformation creating more independent conserved-operator directions. The embedded algebras at $`q=1`$ and $`q>1`$ are different, have the same dimension, and are generally not nested. For example the undeformed total transverse spin fails to commute with the deformed local Hecke generator.

The increase of end-spin overlap and decrease of bulk-spin overlap therefore do not conflict with monotonicity under adding conserved subspaces: deformation is not such an inclusion. The sum runs over *all* Pauli strings, not only single-site spins. It does not establish that total one-body memory is invariant or that memory physically flows from the bulk to the ends.

## 6. Attribution and the unchanged main contribution

The stationary-commutant mechanism, including coherent Hamiltonians with strong-symmetry-preserving Lindblad terms, already belongs to the open-system commutant framework of Li, Sala and Pollmann, arXiv:2305.06918, Sec. II and Appendix B. The argument above is a direct specialization with an explicit norm estimate and scope controls. It carries no new general-principle priority claim.

The additional research contribution under assessment remains the evaluated spatial laws in the preserved theorem: $`L^{-1/2}`$ edge memory for fixed $`q>1`$ and $`L^{-2}`$ fixed-fraction bulk memory with its explicit amplitude/profile for $`q>q_0`$. Nothing here enlarges that bulk domain, solves the deterministic chain's full plateau, or establishes a relaxation exponent, a useful encoded quantum memory, or efficient physical realization.

See [SOURCE_CHECK.md](../archive/research-handoff-2026-10-08/SOURCE_CHECK.md) for primary-source reading boundaries and [contribution review](CONTRIBUTION_REVIEW.md) for the contribution assessment.
