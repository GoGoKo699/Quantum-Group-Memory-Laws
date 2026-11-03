# Reproducing the physical-erasure identities

These checks support the analytical [physical-loss account](../science/README.md). The [main verification contract](../VERIFICATION.md) separately preserves all original spatial-memory assertions and canonical reports. Install the repository's pinned `requirements.txt`, then run from its root:

```sh
python verification/check_small_sectors.py --output build/verification/small_sectors.json
OPENBLAS_NUM_THREADS=1 python verification/check_estimator.py --output build/verification/estimator.json
OPENBLAS_NUM_THREADS=1 python verification/check_cg_amplitudes.py --output build/verification/cg_amplitudes.json
```

Outputs go under `build/`; no scientific source or protected reference report is regenerated. Python and dependency versions are recorded by the main verification receipt.

## Exact physical-sector maps and achievable rates

`check_small_sectors.py` tests the two-qubit triplet and three-qubit multiplicity-averaged spin-one-half embeddings at deformation 1, 1.2, 2 and 3. It checks orthonormality, the physical raising/lowering coproduct, trace preservation, Choi positivity, and equality with physical one-site partial trace on every logical matrix unit. It records conditional Choi spectra and reverse coherent information, keeping these resource values distinct from a full-block capacity.

The same script checks the charged two-site rate against the ordinary-permutation benchmark, with strict improvement at finite deformation greater than one. For chain sizes 1 through 6 it independently constructs the physical vacuum/one-excitation Choi purification for every erased pattern, verifies its environment spectrum against the amplitude-damping formula, and checks the pattern-averaged reverse-hashing lower bound at four erasure probabilities. These finite comparisons do not establish optimality.

## Estimator, full erasure flags and arbitrary priors

`check_estimator.py` exhaustively enumerates every nonnegative spin path through size 7, every logical weight, every nonzero physical computational word and every erasure flag. The tested deformations are 6/5, 2 and 3, with erasure probabilities 1/5, 1/2 and 4/5. CG branch and word probabilities use rational arithmetic; flag sums, logarithms and entropies use floating point. There is no sampling or survivor-pattern cutoff.

It checks branch/word normalization, magnetization, the net mismatch identity, both finite-deformation hazard inequalities, the hidden-mismatch geometric tail, censoring, separate early/late estimator tails, the combined tail, and mean/rounded errors. Full word-and-flag enumeration is compared with the independently implemented dynamic first-event law in `first_event.py`.

Five representative priors per path—uniform, both endpoint point masses, an interior-heavy prior and a reproducible Dirichlet prior—are checked against the complete erased-bit observation. The script verifies posterior entropy against integer-error entropy, the geometric mean-entropy bound, and the stated finite constant. Representative priors test implementation and interpretation; the analytical theorem covers every prior.

The full run contains 3,293,388 word/flag cases, 14,364 estimator-tail comparisons and 3,465 posterior-prior checks. The report records actual counts, numerical discrepancies and a summable remainder for the constant's infinite series. Counts describe this declared finite scope, rather than a uniform-proof certificate.

## Independent physical amplitudes

`check_cg_amplitudes.py` reconstructs signed CG amplitudes independently and compares them with the physical raising coproduct. For every tested deformation and size through 7, all path columns together must be a complete orthonormal physical basis and intertwine the exact irrep ladders. This tests the physical signs and orientation independently of the probability-only estimator calculation.

The channel-capacity conclusion additionally uses the analytical prior-uniform estimate, direct complementary measurement and inherited adaptive squashed-entanglement theorem. None is certified by a finite checker, Choi spectrum alone or a local autocorrelation measurement.
