# Contribution and proof review

## Decision

Retain and consolidate one bounded result: the explicit complete-symmetry
transverse-memory law for the real-q spin-1/2 representation, with distinct
boundary and bulk exponents. It is coherent enough for a dedicated versioned
research record and author contribution assessment. No repository is created
or modified by this review. No manuscript submission, external contact, or
independent-review claim is made.

The optical/Bell projects and every other separated project remain untouched.
The old coplanar-POVM and electron-decoherence PDFs are not scientific inputs.
The current quantum-group line is not an extension of those projects.

## The prospective contribution, with predecessors already credited

Complete-commutant memory projections and quantum-group spin-chain multiplets
are established. Recent work reports anomalous transverse-spin relaxation and
unusual finite-size saturation, and explicitly improves a non-tight one-charge
bound using nonlinear conserved operators. The present result evaluates the
entire symmetry projection, rather than truncating that charge list, and obtains
an exact L^-1/2 edge asymptotic and a fixed-deformation L^-2 bulk asymptotic with
explicit amplitudes and normalized spatial profile. A local symmetry-preserving
random-kick model attains this baseline exactly. No equality with the full
plateau of an arbitrary deterministic Hamiltonian is inferred.

The proposed contribution is therefore a spatial finite-size memory law for a
specified physical representation and observable. It is not discovery of Mazur
bounds, nonlocal conserved charges, quantum-group symmetry, orthogonal-polynomial
methods, anomalous hydrodynamics, or general boundary/bulk differences.

## Claim hierarchy

1. **Finite-size definition and exact recursion.** The symmetry contribution is
   the ordinary physical Hilbert--Schmidt projection, with all multiplicities
   included. The q-Clebsch--Gordan recursion is exact at finite L.
2. **Boundary law.** For every fixed real finite q>1, the end-spin coefficient is
   tanh(log q)/sqrt(2 pi), multiplying L^-1/2. The q=1 answer is exactly 1/L.
3. **Bulk law.** At fixed i/L in (0,1), M=K(q) F(i/L)/L^2 [1+o(1)] under the
   explicit sufficient hypothesis b(q)<1. The threshold q0 is not a transition.
4. **Attainability.** The specified local, noise-averaged random-kick evolution
   has exactly this stationary projection. Its mixing time is not calculated.
5. **Hamiltonian interpretation.** The exact excess identity in
   [PLATEAU_DICTIONARY](PLATEAU_DICTIONARY.md) applies to every symmetry-preserving
   Hamiltonian. The exponentially small expected excess is proved only for its
   declared nonlocal random-eigenbasis reference ensemble, not for the local
   models in the motivating paper.

The last item is a clarification and a conventional random-matrix control. It
is not being substituted for the central spatial-law contribution or promoted
as a separate result merely to maintain momentum.

## Focused proof audit

| Obligation | Review finding and remaining boundary |
|---|---|
| Physical trace and symmetry decomposition | Retains 2^-L Tr and irrep dimension 2j+1. Quantum dimensions or another Temperley--Lieb representation would change the problem. |
| Exact recursion versus selected charges | The trace is over all multiplicity paths; the largest-size arrays are not a subset of thirteen generators or a many-body time simulation. |
| Complete quadrant paths | Horizontal steps are bounded by 1/2; all steps changing the second coordinate are counted by the diagonal majorant. The new check explicitly counts changes, not merely endpoint displacement. |
| Two subcritical tilts | Choose theta=-log b(q)/4, so e^(2 theta)b(q)=sqrt(b(q))<1. The proof already reserved two tilts; the legacy diagnostic tested a one-tilt bound. This review strengthens its diagnostic without changing the proof condition. |
| Gaussian kernel constant and typical spin window | The inherited Jost analytic inputs are used to obtain the moderate-deviation bound. The exact binomial-difference normalization is necessary, not only an unspecified heat-kernel analogy. |
| Summing and matching sectors | The dominating estimate controls small scaling coordinates; the observable norm controls atypically large spins. Truncating the number of second-coordinate changes is removed with the second tilt. |
| Spectral dictionary | Base z=q^-2 and parameters a=q^-1,b=q^-3 match Al-Salam--Chihara coefficients. Both spectral endpoints and parity sublattices remain; omitting either changes the amplitude. |
| Boundary and weak-deformation limits | Fixed distance, fixed fraction, and q approaching one are not interchanged. No uniform mesoscopic crossover theorem is claimed. |
| Complete Hamiltonian plateau | It is a different projection. The exact nonnegative excess is retained, including accidental spectral degeneracies. |

No blocking issue was identified in the audited steps. This is internal
scrutiny, not a fully independent proof report. Passing finite checks does not
prove the uniform large-L estimate. The original detailed proof remains in
[prior/FOLLOWUP.md](prior/FOLLOWUP.md), unchanged; the compact specification is
[THEOREM.md](THEOREM.md).

## Implication-level reconstruction from prior work

### Delacretaz--Gorbenko--Wang--Zan--Zhabin

*Hydrodynamic tails in chaotic spin chains with quantum group symmetry*,
arXiv:2606.20850v1, sections II, IV, VI and Appendix F:
https://arxiv.org/html/2606.20850v1

The source supplies the physical quantum-group-preserving local models,
nonlocal charges, and motivation from finite-size transverse-spin saturation.
Section IV reports approximately model-independent saturation in its numerical
comparison and contrasts it with conventional 1/L and nonconserved 2^-L scales.
Appendix F explicitly adds nonlinear charges, explains the symmetric coproduct,
and acknowledges a non-tight one-charge bound. No plot value was extracted or
converted between its sigma-plus convention and our Pauli-X convention.

Granting the source all of those results still does not evaluate the complete
symmetry projection's finite-q spatial asymptotic. The current law supplies that
baseline. Conversely it does not determine the source's hydrodynamic exponent,
prove a full plateau equality for its local Hamiltonians, or refute its evidence
for a common plateau. Random-matrix spectral statistics alone do not establish
the stronger Haar-eigenvector hypothesis of our optional benchmark.

### Moudgalya--Motrunich

*Hilbert Space Fragmentation and Commutant Algebras*, PRX 12, 011050 (2022),
arXiv:2108.10324:
https://arxiv.org/pdf/2108.10324

The full-commutant projection and the non-Abelian block decomposition are
inherited. Section V.D explicitly maps Temperley--Lieb sectors to the spin-1/2
quantum-group chain, with 2j+1 multiplet degeneracies there. The m-dimensional
local-spin realization discussed elsewhere has q-number degeneracy weights;
its full trace is not interchangeable with the physical 2^L trace here.
Appendix I's edge-memory observable is an edge energy operator in that other
realization, not the charged transverse X_i in this calculation.

Their framework can be applied to write our starting finite projection. It
does not, merely by naming the algebra, supply the evaluated q-Clebsch--Gordan
partial trace or its spatial asymptotic. We claim no new projection principle
or new classification of fragmentation.

### Hart

*Exact Mazur bounds in the pair-flip model and beyond*, arXiv:2308.00738v2:
https://arxiv.org/html/2308.00738v2

The conclusion and sections 4.3--4.4 provide exact nonlocal-pattern memory,
nonzero thermodynamic boundary memory, L^-1/2 bulk memory, and a spatial
interpolation in pair-/p-flip models. These are direct precedents for extracting
physical memory laws from constrained-path counting. The concluding discussion
separates the larger non-Abelian Temperley--Lieb commutant from its evaluated
Abelian pattern sector. Neither its physical representation nor local trace
weights match the current charged spin-1/2 problem. Its exponent cannot be
transferred solely because both calculations use walks.

### Li--Sala--Pollmann

*Hilbert space fragmentation in open quantum systems*, Physical Review Research
5, 043239 (2023), arXiv:2305.06918:
https://arxiv.org/pdf/2305.06918

Appendix B and the stationary-state discussion give the commutant/Mazur
connection for symmetry-preserving jumps. The local random-kick tightness control
uses that established framework. The new item is the explicit spatial value of
the projection in this representation, not the generic fact that such noise
retains the commutant.

### Spectral and ensemble tools

Koelink--Verding, *Spectral analysis and the Haar functional on the quantum SU(2)
group*, arXiv:math/9412225, Section 6, recurrence/orthogonality and generating
formulas: https://arxiv.org/pdf/math/9412225

Damanik--Simon, *Jost Functions and Jost Solutions for Jacobi Matrices, II. Decay
and Analyticity*, arXiv:math/0502487, Theorem 1.5 and Appendix A:
https://arxiv.org/pdf/math/0502487

These provide the orthogonal-polynomial and Jost analyticity input. Their
probability measures are spectral tools for the derived Jacobi operator, not
a replacement of the physical infinite-temperature trace by a Haar functional
on a quantum group. The complete finite-q recursion matching remains necessary.

Collins--Sniady, *Integration with respect to the Haar measure on unitary,
orthogonal and symplectic group*, arXiv:math-ph/0402073:
https://arxiv.org/abs/math-ph/0402073

Only the primary abstract/publication record was inspected for this final
attribution. No specific unread equation is imported: the second projector
moment and both excess formulas are derived directly in PLATEAU_DICTIONARY.
The general Haar method and random-matrix reasoning carry no new priority claim.

An adjacent transport comparison, Znidaric, *Inhomogeneous SU(2) symmetries in
homogeneous integrable U(1) circuits and transport*, Nature Communications 16,
4336 (2025), was inspected at its symmetry and boundary discussion:
https://www.nature.com/articles/s41467-025-59705-2
It addresses modulated symmetries and transport in a different circuit; no
complete finite-q transverse-symmetry projection law was imported from it.

## Strongest positive and skeptical assessments

The positive case is an exact, spatially resolved memory law that changes the
interpretation of a nonlocal symmetry: relative to SU(2), the unavoidable
finite-size end-spin memory is enhanced and the bulk contribution is suppressed.
The law covers the full symmetry algebra; it is realized by a declared local
random-kick dynamics. It is not a numerical ratio against a knowingly incomplete
one-charge comparator. The uniform bulk matching is a substantive analytical
obligation, not a finite-size fit.

The skeptical case is that the physical setting and commutant framework are
established, and a local deterministic model's full plateau remains unproved.
The bulk theorem uses a sufficient q range, not all q>1. A substantial fraction
of the work is a representation-specific spectral calculation. Its broad
importance must rest on the spatial conclusion and complete-symmetry baseline,
not on code size, exactness alone, or the standard random-eigenbasis addendum.

The inspected sources do not directly provide this complete finite-q spatial
law in the same physical representation. That is a bounded implication-level
comparison, not exhaustive priority clearance. No external independent review
has occurred. This supports consolidation and focused contribution assessment;
it does not establish a publication outcome.

## Stop boundary

Do not add a weak-deformation crossover, higher on-site spins, finite-temperature
trace, symmetry-breaking noise, a storage protocol, or a hydrodynamic exponent
merely to make the current result look larger. They are separate claims. A
concrete proof objection or a source that supplies the same physical implication
would reopen this assessment. A new repository, if authorized later, should
contain one central spatial-law result and its supporting proof, with this
plateau distinction kept explicit.

## Access and verification limits

Primary text was used for the passages above. Runtime attempts to download five
primary documents failed DNS; the web tool's readable primary text was used
instead. Three PDF screenshot requests failed with cache misses. No figure,
plot coordinate, or unviewed table entry is evidence in this review. Failed
retrievals and broad unrelated hits are not evidence of absence of prior work.
No third-party article is redistributed.

Five new check groups passed twice with identical reports. The immediate
six-group bulk checker was rerun unchanged and its report is byte-identical to
the canonical report. The earlier five- and four-group suites were not rerun
in full, although their exact routines are imported by some targeted checks.
The largest full spin Hilbert space is 256. An initial new-driver failure at
q=1 was fixed by using the proven exact value 1/L rather than passing q=1 to a
legacy function explicitly restricted to q>1. No scientific assertion,
tolerance, original file, or reference report was changed. The initial script
and failed log remain in development/. See VERIFICATION.json for exact hashes.
