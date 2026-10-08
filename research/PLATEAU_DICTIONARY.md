# Symmetry memory and Hamiltonian-dependent excess

The full time-averaged correlation separates into the symmetry projection and a
nonnegative Hamiltonian-dependent excess. A Haar-random eigenbasis within each
multiplicity space gives a generally nonlocal reference ensemble in which the
mean excess can be evaluated exactly.

## 1. An exact separation, including accidental degeneracies

Let the spin-chain Hilbert-space dimension be $`D=2^L`$, and use the ordinary,
unnormalized Hilbert--Schmidt norm. Let $`\Pi_q`$ be the orthogonal projection
onto the full symmetry algebra $`\mathcal A_q`$. For a Hermitian observable O
and any H commuting with this algebra, define

```math
\mathcal D_H(O)=\sum_\epsilon P_\epsilon O P_\epsilon,
\qquad M(O)=D^{-1}\|\Pi_q(O)\|_{\rm HS}^2.
```

The projectors are onto distinct energies, not individual vectors within a
possibly degenerate eigenspace. Finite-dimensional time averaging gives
$`\bar C(O)=D^{-1}\|\mathcal D_H(O)\|_{\rm HS}^2`$.
Because $`\mathcal A_q\subseteq\{H\}'`$, the projections are nested:
$`\mathcal D_H\Pi_q=\Pi_q\mathcal D_H=\Pi_q`$.
Consequently

```math
\boxed{
\bar C(O)=M(O)+D^{-1}\|\mathcal D_H[O-\Pi_q(O)]\|_{\rm HS}^2.
}\qquad(1)
```

This is the Pythagorean identity for nested operator-space projections and
includes all degeneracies. The residual term depends on the Hamiltonian. It
vanishes exactly when the residual observable has no matrix elements within
any energy eigenspace. In particular H=0 gives $`\bar C(X_i)=1`$.

## 2. Explicit multiplicity form

Use the symmetry decomposition

```math
\mathcal H_L=\bigoplus_j(\mathcal V_j\otimes\mathbb C^{m_j}),
\qquad d_j=2j+1,
\qquad H=\bigoplus_j(I_{d_j}\otimes h_j).
```

For the following simplified formula assume that each h_j has simple spectrum
and that eigenvalues in different j blocks do not coincide. Equation (1) covers
arbitrary degeneracies. If $`|u_{j\alpha}\rangle`$ is an eigenbasis of h_j, put

```math
O_j=P_jOP_j,\quad S_j=\mathrm{Tr}_{m_j}\,O_j,\quad
B_{j\alpha}=(I\otimes\langle u_{j\alpha}|)O_j
             (I\otimes|u_{j\alpha}\rangle).
```

Then

```math
\bar C=D^{-1}\sum_{j,\alpha}\|B_{j\alpha}\|_{\rm HS}^2,
\quad
M=D^{-1}\sum_j\frac{\|S_j\|_{\rm HS}^2}{m_j},
```

and $`\sum_\alpha B_{j\alpha}=S_j`$ yields

```math
\boxed{
\bar C-M=D^{-1}\sum_{j,\alpha}
\left\|B_{j\alpha}-\frac{S_j}{m_j}\right\|_{\rm HS}^2.
}\qquad(2)
```

The extra plateau is the variation of the diagonal multiplicity blocks around
their average. Additional accidental degeneracies contribute coherent matrix
elements, which (1) includes.

### Examples in a local Hamiltonian

For the quantum-group-preserving XXZ Hamiltonian and its three-site deformation,
the [Hamiltonian checker](../archive/research-handoff-2026-10-08/prior/check_review.py)
gives the following values at L=8, q=2.6, site 4:

| deformation coefficient | complete symmetry M | full time average | excess in (1) |
|---:|---:|---:|---:|
| 0 | 0.0640102152378 | 0.0841751509613 | 0.0201649357235 |
| 1 | 0.0640102152378 | 0.0860813187749 | 0.0220711035371 |

Both examples have a strictly positive Hamiltonian-dependent excess.

## 3. Exact random-eigenbasis control

Choose each h_j to have any prescribed simple spectrum, with no cross-block
coincidences, and choose its eigenvectors Haar-uniformly in U(m_j). The spectra
may be fixed: eigenvalue randomness is unnecessary for this plateau calculation.
The resulting H commutes with the symmetry but is generally nonlocal.

Define
```math
C_j=O_j-\frac{S_j}{m_j}\otimes I_{m_j},\qquad
R_j=\|C_j\|_{\rm HS}^2
=\|O_j\|_{\rm HS}^2-\frac{\|S_j\|_{\rm HS}^2}{m_j}.
```

The standard Haar-vector moment is
```math
\mathbb E|\langle u|A|u\rangle|^2
=\frac{\mathrm{Tr}(AA^\dagger)+|\mathrm{Tr}\,A|^2}{m(m+1)}.
```
It follows from unitary invariance and
$`\mathbb E(|u\rangle\langle u|)^{\otimes2}=(I+\mathsf S)/[m(m+1)]`$.
Apply it to every irrep matrix element of C_j and sum over the m_j columns.
Correlations between different columns are irrelevant because this expression
is linear in their individual squared overlaps. Therefore

```math
\boxed{
\mathbb E(\bar C-M)=D^{-1}\sum_j\frac{R_j}{m_j+1}.
}\qquad(3)
```

For $`\|O\|_\infty\le1`$, compression gives
$`R_j\le\|O_j\|_{\rm HS}^2\le d_jm_j`$. Thus

```math
\boxed{
0\le\mathbb E(\bar C-M)
\le\frac{1}{2^L}\sum_jd_j
=\frac{\lfloor(L+2)^2/4\rfloor}{2^L}.
}\qquad(4)
```

The bound includes low-multiplicity sectors. At m_j=1, R_j is exactly zero.

For a real O and a real q-Schur basis, a real-symmetric reference H can instead
have Haar-orthogonal multiplicity eigenvectors. The sphere fourth moment gives

```math
\mathbb E_{\mathbb R}(\bar C-M)
=\frac1D\sum_j\frac{
\|C_j\|_{\rm HS}^2+
\sum_{a,b}\mathrm{Tr}[(C_j^{ab})^2]}{m_j+2}
\le\frac{2\lfloor(L+2)^2/4\rfloor}{2^L}.\qquad(5)
```
Here $`C_j^{ab}`$ are real m_j by m_j blocks. The numerator equals
$`2\sum_{ab}\|\mathrm{Sym}\,C_j^{ab}\|_{\rm HS}^2`$, so it is nonnegative.
Equation (5) gives the real ensemble's exact mean and its upper bound.

### Relative excess in the reference ensemble

At fixed q in the proved bulk domain and fixed x in (0,1), M is asymptotically a
positive multiple of L^-2. Equations (4)-(5), positivity, and Markov's inequality
then give $`\bar C/M\to1`$ in probability for the stated random-eigenbasis
ensemble. For each fixed relative tolerance the failure probability is bounded
by a constant times L^4 2^-L. The boundary law similarly gives a vanishing
relative excess in this ensemble.

At q=2.6, the exact finite-size symmetry values and the real-ensemble *upper
bound* on its mean excess are:

| L | M at the central site | real-ensemble mean-excess bound |
|---:|---:|---:|
| 20 | 0.0142698350805 | 0.000230789184570 |
| 40 | 0.00428106000724 | 8.02174326964e-10 |
| 80 | 0.00121046009971 | 2.78098121940e-21 |

The table combines exact finite-size symmetry values with the analytic bound
in (5). The Haar-eigenbasis assumption defines this generally nonlocal
reference ensemble; for a specified local Hamiltonian, (1) remains the exact
expression for its excess.

## 4. Verification method

The Haar moment check uses a deterministic exact fourth-moment design. For a
complex Haar vector in dimension m, mix the m
coordinate basis vectors (total weight 1/(m+1)) with all vectors whose entries
are independent fourth roots of unity divided by sqrt(m) (total weight m/(m+1)).
Their fourth moments agree exactly with the Haar expression. For a real Haar
vector, mix coordinate vectors with weight 2/(m+2) and normalized independent
sign vectors with weight m/(m+2). Their fourth moments equal the real-sphere
fourth moments. Small dimensions are explicitly enumerated.

Independently, small full spin Hamiltonians are assembled from random
multiplicity eigenbases and distinct spectra; direct spectral time averages
agree with (2). The deterministic local Hamiltonians check (1),
including accidental degeneracies. These finite checks complement the
algebraic derivations above.

## Attribution

The nested-projection and commutant framework comes from Moudgalya--Motrunich,
PRX 12, 011050 (2022), arXiv:2108.10324. Unitary and orthogonal Haar integration
is treated by Collins--Sniady, arXiv:math-ph/0402073. The elementary moments
used here are derived above and specialized to the physical spin representation.
See the [attribution map](../literature/ATTRIBUTION.md) for the source comparison.
