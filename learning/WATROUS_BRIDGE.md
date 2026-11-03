# From quantum channels to symmetry memory and physical loss

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**. The [author's freely available manuscript](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf) supplies the chapter and section numbering below. This bridge explains the additional steps supplied by this project; the textbook does not prove the real-deformation memory laws or the physical-erasure ceiling.

The project asks two related questions. How strongly does a local spin overlap the full conserved algebra? How much coherent information remains when the corresponding stationary channel is followed by independent physical erasure? Both begin with the same algebra projection, but they require different observables and proofs. The [30-milestone map](MILESTONES.md) connects the routes without identifying their conclusions.

## Read the relevant part of the book alongside the project

| Watrous 2018 | Foundation supplied | Project application |
|---|---|---|
| §§2.1.1–2.1.3: registers, states, and purifications | Tensor factors, partial trace, and an untouched reference | [Physical-erasure model](../science/model.md) |
| §§2.2.1–2.2.3: channels and representations | Complete positivity, Kraus maps, Choi operators, and composition | [Exact conditional one-erasure maps](../science/small_sectors.md) |
| §4.2.2: fixed points of channels | A stationary operator space and the channel acting on it | [Full-algebra projection](../research/MODEL_AND_CLAIMS.md) and [local realization](../research/LOCAL_REALIZATION.md) |
| §§5.1–5.2: entropy and quantum relative entropy | Entropy of a mixture, conditional information, and information inequalities | [First-mismatch entropy estimate](../science/first_mismatch.md) and [capacity proof](../science/capacity.md) |
| §§6.1.1–6.1.2: separability and LOCC | Operations available between channel calls and the role of an entanglement resource | [Two-way communication convention](../science/model.md) |
| §6.2.2: distillable entanglement and cost | The operational difference between retained correlations and usable entanglement | [Capacity ceiling](../science/capacity.md) |
| §§7.1.1–7.1.2: permutation-invariant vectors and operators | The ordinary symmetric-space and invariant-algebra endpoint | [Undeformed comparison](../science/interpretation.md) |
| §§8.2.1–8.2.2: quantum capacities | Rates, repeated channel uses, and asymptotic transmission | [Per-block capacity statement](../science/capacity.md) |

Start with §§2.1–2.2 and the two-site example below. Then read only the relevant book section when a project proof needs its language. The whole book is not a prerequisite.

## One physical space, two uses of its projection

The carrier consists of $`n`$ physical qubits. Write $`r>1`$ for a fixed finite real deformation and $`p`$ for the independent erasure probability, with $`0<p<1`$. Earlier spatial-memory pages use $`L`$ for chain length and $`q`$ for deformation; in this bridge $`L=n`$ and $`q=r`$.

For each spin $`j`$, let $`V_j`$ be its $`2j+1`$ dimensional representation and $`M_j`$ its multiplicity space. A deformed Clebsch–Gordan basis gives

```math
\mathcal H_n=\bigoplus_j V_j\otimes M_j,
\qquad
\mathcal A_r=\bigoplus_j\mathrm{End}(V_j)\otimes I_{M_j}.
```

The full algebra contains products of the symmetry generators. Keeping only their linear span would retain fewer directions. Deformation changes how the sectors sit in the physical tensor product, even though their ordinary dimensions and multiplicities stay the same.

With $`m_j=\dim M_j`$ and sector projector $`P_j`$, the ordinary-trace orthogonal projection is

```math
\Pi_r(X)=\bigoplus_j
\mathrm{Tr}_{M_j}(P_jXP_j)\otimes\frac{I_{M_j}}{m_j}.
```

This formula describes a CPTP channel: measure the sector, discard its multiplicity register, and replace that register by the maximally mixed state. Reembedding the blocks uses the physical deformed basis. Each operation is completely positive, so the identity remains valid with an arbitrary reference attached. Its self-adjointness in the Hilbert–Schmidt inner product also makes it the operator projection used in the memory calculation.

| Object | Meaning |
|---|---|
| $`R`$ | An untouched reference; it can be entangled with the transmitted state |
| $`B`$ | Surviving physical qubits and the receiver's erasure flags |
| $`E`$ | The complementary output, including lost qubits; it is not supplied to the receiver |
| $`\Pi_r`$ | Projection onto the full physically embedded symmetry algebra |
| $`M_{L,i}(r)`$ | Squared Hilbert–Schmidt overlap of one local Pauli operator with that algebra |
| $`Q_2`$ | Asymptotic coherent communication rate with unlimited two-way classical communication, per complete block |

The physical trace is used throughout. Quantum dimensions or a deformation-dependent inner product cannot replace it.

### A short normalization check at ordinary symmetry

At $`r=1`$, $`\Pi_1`$ is the ordinary permutation twirl. Every local transverse Pauli has the same projection,

```math
\Pi_1(X_i)=\frac1L\sum_{k=1}^L X_k.
```

Different single-site Pauli operators are orthogonal under $`2^{-L}\mathrm{Tr}`$. Squaring the norm therefore gives $`M_{L,i}(1)=1/L`$. This is an autocorrelation statement. It does not determine the quantum capacity after local noise.

The [spatial theorem](../research/THEOREM.md) separately evaluates the finite-deformation projection. Its edge law holds for every fixed finite $`r>1`$; its stated bulk equality requires $`r>r_0`$ and a fixed interior position fraction. Here $`r_0=q_0=2.0810189966\ldots`$ is a sufficient proof threshold, not a physical transition. Those conditions do not restrict the physical-erasure ceiling, which uses a different argument for every fixed finite $`r>1`$.

## A two-site loss calculation

Let $`|\uparrow\rangle,|\downarrow\rangle`$ be the physical spin basis. In the spin-one sector set

```math
|t_+\rangle=|\uparrow\uparrow\rangle,
\quad
|t_0\rangle=\frac{|\uparrow\downarrow\rangle+r|\downarrow\uparrow\rangle}
{\sqrt{1+r^2}},
\quad
|t_-\rangle=|\downarrow\downarrow\rangle.
```

For input $`|t_0\rangle`$, erasing the first site leaves

```math
\frac{r^2|\uparrow\rangle\langle\uparrow|
+|\downarrow\rangle\langle\downarrow|}{1+r^2}
```

on the second site. Erasing the second instead leaves the weights reversed. They coincide at $`r=1`$. At $`r>1`$, the erasure location matters despite the unchanged spin-one dimension.

A channel calculation must also act on off-diagonal operators, such as $`|t_+\rangle\langle t_0|`$, and on reference-entangled inputs. The [small-sector account](../science/small_sectors.md) supplies complete Kraus maps, including the multiplicity-averaged three-site sector. Comparing only the displayed diagonal state would not establish channel equivalence or a capacity formula.

The two-site example also has an operational consequence. Reverse hashing on the triplet resource, with every erasure branch weighted by its probability, gives an achievable block rate strictly larger than the exact ordinary-permutation two-site rate when $`r>1`$. This comparison changes an achievable finite-block rate; it does not identify the deformed capacity exactly. The calculation is given with the [small-sector maps](../science/small_sectors.md).

This example explains why a global unitary identifying the abstract algebras at $`r=1`$ and $`r>1`$ cannot identify their physical local-loss channels. Physical erasure is defined on the original sites.

## From a path observation to a communication ceiling

The [first-mismatch proof](../science/first_mismatch.md) supplies the deformation-specific step that is absent from Watrous. A multiplicity label specifies a Clebsch–Gordan path. Measuring the physical spins computationally gives an exact backwards classical process along that path. The magnetic label is encoded in the excess of one type of path mismatch over the other.

Independent erasure reveals each mismatch with probability $`p`$. Before the first revealed mismatch, the number of hidden mismatches has a geometric tail. For fixed $`r>1`$, the exact Clebsch–Gordan coefficients connect the location of that first observation to the magnetic label. A cumulative path exposure gives an estimator with uniformly controlled error, including the event that no mismatch is observed. The conclusion is a constant bound on the magnetic label's conditional entropy, independent of chain length, sector, path, and prior distribution.

The [capacity proof](../science/capacity.md) then restores the quantum problem. Measure the complementary multiplicity label and lost computational spins as a squashing operation. For every reference-entangled input, each resulting reference–survivor branch is pure. Distinct magnetic labels have distinct surviving total magnetizations, so the conditional reference entropy is at most the classical posterior entropy. The research-level squashed-entanglement channel bound converts this into a two-way capacity ceiling valid under adaptive LOCC between calls.

Watrous supplies channels, entropy, and the operational capacity language. The exact path estimator and its uniform estimates are supplied here; squashed entanglement's adaptive channel bound is a credited research input in the capacity account. Neither is inferred from a local autocorrelation or from the textbook's capacity chapter alone.

## Read the two conclusions with their own limits

The [memory route](../research/PHYSICAL_MECHANISM.md) explains spatial overlaps, the [plateau dictionary](../research/PLATEAU_DICTIONARY.md) separates symmetry memory from Hamiltonian-specific excess, and the [local realization](../research/LOCAL_REALIZATION.md) identifies the supplied stationary projection. Its finite-time convergence depends on a finite-size dissipative gap; no uniform mixing-time law follows.

The [loss route](../science/README.md) starts with exact physical conditional maps and ends with an $`r,p`$ dependent, size-independent ceiling. It does not claim a sharp finite-deformation capacity or a limit uniform in deformation. The exact ordinary-permutation/symmetric-loss benchmark remains separately credited in the [interpretation](../science/interpretation.md). The related [Quantum Permutation Noise Limits](https://github.com/GoGoKo699/Quantum-Permutation-Noise-Limits) account establishes that benchmark for arbitrary encodings; its singlet-padding and permutation-covariance proof is not a physical-loss equivalence at finite deformation.

The loss theorem also has a positive lower bound. A logical qubit using the all-down state and the normalized one-up state yields, after accounting for every erasure pattern and applying reverse hashing,

```math
1-h_2(p/2)\le Q_2(\mathcal E_p^{\otimes n}\circ\Pi_r)\le C(r,p),
```

where $`h_2`$ is binary entropy. The left side is positive at every fixed $`0<p<1`$. The [capacity account](../science/capacity.md) derives the physical code and the bound. Thus coherent communication stays of order one per block; the ceiling does not assert that all entanglement is lost.

The primary research sources in the attribution accounts remain necessary for checking inherited inputs. They are scholarly references, not additional educational anchors.
