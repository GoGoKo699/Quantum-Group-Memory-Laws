# An all-sector ceiling after physical erasure

For the [physical channel](model.md)

```math
\mathcal N_{n,r,p}=\mathcal E_p^{\otimes n}\circ\Pi_r,
```

every fixed finite $`r\gt1`$ and $`0\lt p\lt1`$ admit a constant independent of chain length:

```math
\boxed{
1-h_2(p/2)\le Q_2(\mathcal N_{n,r,p})
\le C(r,p)\lt\infty\qquad(n\ge1).}
```

Here $`h_2`$ is binary entropy, all logarithms are base two, and capacities are qubits per complete $`n`$-site block. The upper constant $`C(r,p)=1+g_2(M+1)`$ is explicitly defined and proved finite in the [first-mismatch theorem](first_mismatch.md). Neither bound is asserted sharp.

The upper bound covers arbitrary encoders, external reference entanglement, and adaptive protocols using unlimited classical communication in both directions. Its operational ingredient is the established channel squashed-entanglement converse of Takeoka, Guha and Wilde. The new physical step is the uniform finite-deformation estimate and its application to the full projection's complementary channel.

## 1. The classical estimate needed by the channel proof

In a fixed spin sector let $`K=2j`$ and $`h=0,\ldots,K`$ label the magnetic basis. Each orthonormal multiplicity path gives an isometry $`W_{j,\alpha}`$ into the physical chain. The [first-mismatch proof](first_mismatch.md) establishes, for **every prior** on $`h`$ and **every path**,

```math
H(h\mid O,j,\alpha)\le C(r,p),
```

where $`O`$ consists of the physical erasure pattern and erased computational-basis values. This prior-uniform statement is essential: a maximally mixed input calculation alone would not bound a channel capacity.

The estimate is obtained by comparing physical spins with known path-edge signs. Each actual mismatch is independently revealed by erasure with probability $`p`$. Before the first revealed mismatch, the hidden count has a geometric tail. The exact finite-$`r`$ Clebsch–Gordan probabilities turn its location into a magnetic-label estimate with uniform exponentially decaying errors. The proof handles top weights, arbitrary path excursions and finite-word censoring.

## 2. Measure a valid environment of the complete projection

Use the sector coordinates of [the model](model.md). A Kraus family of the **full stationary channel** is

```math
L_{j,\alpha,\beta}
=\frac1{\sqrt{m_j}}
W_{j,\alpha}(I_{V_j}\otimes\langle\beta|)W_j^\dagger P_j.
```

The input multiplicity is $`\beta`$; the newly mixed output copy/path is $`\alpha`$. Summing $`L^\dagger L`$ gives the identity. These are ordinary physical multiplicity weights.

For an arbitrary pure reference-input state, define its sector vectors by

```math
(I_R\otimes W_j^\dagger P_j)|\Psi\rangle
=\sum_{h,\beta}|u_h^{j,\beta}\rangle_R
\otimes|h\rangle\otimes|\beta\rangle.
```

The reference vectors can be nonorthogonal and unnormalized. Measuring a Stinespring environment of $`\Pi_r`$ in its Kraus-label basis $`j,\alpha,\beta`$ leaves the corresponding pure vector

```math
\frac1{\sqrt{m_j}}\sum_h
|u_h^{j,\beta}\rangle_R\otimes W_{j,\alpha}|h\rangle.
```

Conditional on $`j,\beta`$, the logical prior is proportional to $`\|u_h^{j,\beta}\|^2`$. The output path $`\alpha`$ is uniform and independent of this logical weight. Thus the classical estimate applies to every branch, without restricting the original encoder or replacing its mixed multiplicity by a chosen pure path.

Now measure the erasure environment in the physical computational basis, including its pattern label. This is a rank-one environment measurement. Given the combined outcome $`y=(j,\alpha,\beta,O)`$, the reference–receiver branch is pure and has the form

```math
|\psi_y\rangle\ \propto\
\sum_h|u_h^{j,\beta}\rangle_R\otimes|v_{h,O}\rangle_B.
```

For distinct $`h`$, the surviving physical vectors are orthogonal. Their total initial up-spin numbers are $`(n-K)/2+h`$, and $`O`$ fixes the erased up-spin count; their surviving up-spin numbers therefore differ. Tracing the survivors leaves a mixture of the normalized reference vectors with the corresponding posterior label weights. Entropy of a mixture of pure states is at most the Shannon entropy of its weights, so

```math
S(R\mid y)\le H(h\mid y).
```

Averaging $`O`$ at each $`j,\alpha,\beta`$ and applying the uniform estimate gives

```math
\sum_y p_y S(R)_{\psi_y}\le C(r,p).
```

All operations here are mathematical squashing of the actual complementary environment. No physical path flag is supplied to sender or receiver, and no equivalence with ordinary local symmetric loss is assumed.

## 3. Squashed entanglement and arbitrary adaptive use

For a channel $`\mathcal N`$, its squashed entanglement is the supremum over pure reference-input states of the output squashed entanglement. Measuring the environment as above is one admissible squashing map. Since each conditional reference–receiver state is pure,

```math
\frac12 I(R;B\mid Y)=\sum_y p_y S(R)_{\psi_y}.
```

The previous bound holds for every pure reference-input state, hence directly for the complete channel:

```math
E_{\rm sq}(\mathcal N_{n,r,p})\le C(r,p).
```

Takeoka–Guha–Wilde, [arXiv:1310.0129v3](https://arxiv.org/html/1310.0129v3), Definition 1 and Theorems 7 and 9, supply the channel definition, the subadditivity needed to telescope adaptive uses, and

```math
Q_2(\mathcal N)\le E_{\rm sq}(\mathcal N).
```

They allow arbitrary intermediate LOCC and reference-correlated memories. Applying that established theorem to this direct bound proves the stated size-independent ceiling. No assertion of teleportation covariance or a maximally entangled optimal input is needed at finite deformation.

## 4. A positive rate at every block size

The largest spin sector has multiplicity one, so $`\Pi_r`$ is the identity on it. Encode a logical qubit in the all-down vacuum $`|v\rangle=|1\rangle^{\otimes n}`$ and its normalized one-up state

```math
|u\rangle=\sum_{i=1}^n\sqrt{w_i}\,|1\cdots 0_i\cdots1\rangle,
\qquad
w_i=\frac{(1-z)z^{n-i}}{1-z^n}.
```

For an erasure pattern $`E`$, let $`\eta_E=\sum_{i\notin E}w_i`$ be the surviving excitation weight. A receiver isometry identifies the vacuum and normalized surviving one-up state with a qubit; if $`\eta_E=0`$, it appends a vacuum output. The conditional logical channel is exactly amplitude damping with excitation survival $`\eta_E`$.

Sending half of a maximally entangled logical qubit gives a conditional normalized Choi state with eigenvalues $`(1+\eta_E)/2`$ and $`(1-\eta_E)/2`$. Its reference entropy is one bit. Bob announces the pattern and reverse hashing distills, pattern by pattern, at rate

```math
R_E=1-h_2\!\left(\frac{1-\eta_E}{2}\right)\ge0.
```

Erasure patterns are input independent and $`\mathbb E\eta_E=1-p`$. Concavity of binary entropy therefore yields

```math
\mathbb E R_E
\ge1-h_2\!\left(\frac p2\right)\gt0.
```

This is an achievable nonsharp rate for every $`n\ge1`$. Reverse hashing is inherited; the physical code and conditional channel identify how to apply it here. The proof does not postselect a rare event while omitting its probability.

## 5. Benchmark and remaining scope

At $`p=0`$ the largest sector transmits $`\log_2(n+1)`$ coherent qubits. At fixed positive erasure probability the theorem bounds that growing noiseless register by a constant. At $`r=1`$, [Quantum Permutation Noise Limits](https://github.com/GoGoKo699/Quantum-Permutation-Noise-Limits/blob/230ef8c5af1508f5ec2e13970c84ec2d8e0d2d36/science/erasure_capacities.md) proves the exact benchmark

```math
Q_2=\log_2(n+1)-\mathbb E\log_2(L+1),
\qquad L\sim\mathrm{Bin}(n,p),
```

which tends to $`-\log_2p`$. The finite-$`r`$ result proves persistence of a ceiling; it does not claim that this exact formula or sharp constant persists. The [small-sector maps](small_sectors.md) show why the original covariant symmetric-loss proof is not a physical loss-channel equivalence at $`r\gt1`$.

Local autocorrelation, global algebra dimension and finite-time mixing are separate questions. [Interpretation](interpretation.md) states their relation and the limits of this theorem.
