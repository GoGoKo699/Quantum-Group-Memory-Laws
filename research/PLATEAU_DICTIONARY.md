# Symmetry memory and Hamiltonian-dependent excess

## Status and purpose

This note resolves an interpretation question without asserting a new law for
local chaotic Hamiltonians. The existing complete-symmetry projection is retained.
The identities below say precisely what a particular Hamiltonian adds. A Haar
random eigenbasis within each multiplicity space is then a **declared nonlocal
reference ensemble**, not an assumption silently imposed on a spin-chain Hamiltonian.

The projection and random-vector moment methods are standard. Their specialized
application here is a diagnostic for interpreting the boundary/bulk memory law,
not a separate first-discovery claim or a second paper.

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

This is the Pythagorean identity for nested operator-space projections. It
includes all degeneracies and does not require integrability, nonintegrability,
randomness, locality, or a dynamical approximation. The residual term is not
known from symmetry alone. It is zero if and only if the residual observable
has no matrix elements within any energy eigenspace. In particular H=0 gives
$`\bar C(X_i)=1`$, not M. Finite spectral projectors alone do not establish
that their additional overlap is large or small.

## 2. Explicit multiplicity form

Use the symmetry decomposition

```math
\mathcal H_L=\bigoplus_j(\mathcal V_j\otimes\mathbb C^{m_j}),
\qquad d_j=2j+1,
\qquad H=\bigoplus_j(I_{d_j}\otimes h_j).
```

For the following simplified formula assume that each h_j has simple spectrum
and that eigenvalues in different j blocks do not coincide. These assumptions
are not needed for (1). If $`|u_{j\alpha}\rangle`$ is an eigenbasis of h_j, put

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
their average. Additional accidental degeneracies contribute further coherent
matrix elements; they are already handled by (1). Neither absence of accidental
degeneracies nor nonintegrability forces the variance in (2) to vanish.

### Direct checks in the already selected local Hamiltonian

The unchanged source Hamiltonian checker uses the QG-preserving XXZ Hamiltonian
and its specified three-site deformation. At L=8, q=2.6, site 4:

| deformation coefficient | complete symmetry M | full time average | excess in (1) |
|---:|---:|---:|---:|
| 0 | 0.0640102152378 | 0.0841751509613 | 0.0201649357235 |
| 1 | 0.0640102152378 | 0.0860813187749 | 0.0220711035371 |

The values reproduce the previously established small-system distinction. They
are not new thermodynamic evidence. The fresh contribution is the explicit
identity measuring the residual, not another assertion that the residual can exist.

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

This bound treats low-multiplicity sectors explicitly; no claim that every m_j
is exponentially large is needed. At m_j=1, R_j is exactly zero.

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
The real and complex ensembles are distinct. The upper bound is deliberately
conservative; it need not be below one at the smallest L.

### What this does imply

At fixed q in the proved bulk domain and fixed x in (0,1), M is asymptotically a
positive multiple of L^-2. Equations (4)-(5), positivity, and Markov's inequality
then give $`\bar C/M\to1`$ in probability for the stated random-eigenbasis
ensemble. For each fixed relative tolerance the failure probability is bounded
by a constant times L^4 2^-L. The boundary law similarly permits a vanishing
relative excess there. This is a consequence of a specified ensemble, not a
claim of almost-sure convergence for a spatially local sequence of Hamiltonians.

At q=2.6, the exact finite-size symmetry values and the real-ensemble *upper
bound* on its mean excess are:

| L | M at the central site | real-ensemble mean-excess bound |
|---:|---:|---:|
| 20 | 0.0142698350805 | 0.000230789184570 |
| 40 | 0.00428106000724 | 8.02174326964e-10 |
| 80 | 0.00121046009971 | 2.78098121940e-21 |

No random 40- or 80-spin Hamiltonian is simulated. The bounds are analytic.
The exact ensemble mean itself was calculated only for small blocks, using (3)
and (5), and is retained in the report rather than confused with its upper bound.

### What this does not imply

A local Hamiltonian's eigenvectors need not be uniformly distributed within
multiplicity sectors. Real-versus-complex level statistics do not establish that
hypothesis. An energy-dependent eigenstate expectation can retain a systematic
excess. We have not proved an ETH statement, its rate of convergence, or the
plateau law of the source's local Hamiltonian/Floquet models. This benchmark is
therefore not used to erase the inequality in their physical comparison.

## 4. Verification method

The Haar moment check uses a deterministic exact fourth-moment design, not a
Monte Carlo error bar. For a complex Haar vector in dimension m, mix the m
coordinate basis vectors (total weight 1/(m+1)) with all vectors whose entries
are independent fourth roots of unity divided by sqrt(m) (total weight m/(m+1)).
Their fourth moments agree exactly with the Haar expression. For a real Haar
vector, mix coordinate vectors with weight 2/(m+2) and normalized independent
sign vectors with weight m/(m+2). Their fourth moments equal the real-sphere
fourth moments. Small dimensions are explicitly enumerated.

Independently, small full spin Hamiltonians are assembled from random
multiplicity eigenbases and distinct spectra; direct spectral time averages
agree with (2). The original deterministic source Hamiltonians check (1),
including accidental degeneracies. None of these finite checks replaces the
algebraic proofs of (1)-(5).

## Attribution

The nested-projection/commutant viewpoint is inherited from Moudgalya--Motrunich,
PRX 12, 011050 (2022), arXiv:2108.10324. Unitary and orthogonal Haar integration
is established, e.g. Collins--Sniady, arXiv:math-ph/0402073; the elementary moment
used here is derived explicitly above. The ensemble and bounds in this note
specialize those tools to the declared physical representation. No exhaustive
novelty claim is made for this subsidiary calculation.
