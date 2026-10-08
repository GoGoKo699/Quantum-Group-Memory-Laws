# Quantum-group symmetry memory: consolidated review

This package reviews the existing boundary/bulk theorem and supplies an exact
account of the difference between complete symmetry memory and the time average
of a particular Hamiltonian. No protected repository is used or modified.

Read in this order:

1. [THEOREM.md](THEOREM.md): compact physical model, law, hypothesis and proof map.
2. [REVIEW.md](REVIEW.md): contribution, predecessor reconstruction and limits.
3. [PLATEAU_DICTIONARY.md](PLATEAU_DICTIONARY.md): exact excess and explicitly
   nonlocal random-eigenbasis benchmark.
4. [prior/FOLLOWUP.md](prior/FOLLOWUP.md): unchanged detailed bulk proof, with the
   preceding edge and finite-size records nested under prior/.

The main theorem's formulas are unchanged. The new plateau identities are
standard projection and Haar-moment consequences specialized to this setting.
They do not establish saturation or a relaxation exponent for local chaotic
Hamiltonians. The random-kick tightness example remains a different, explicitly
noise-averaged dynamics.

## Reproduce

The inherited numerical dependencies are in [prior/requirements.txt](prior/requirements.txt).
Run from this directory with one BLAS thread:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python check_review.py --output reproduced_review.json
(cd prior && OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python check_bulk.py --output ../reproduced_bulk.json)
```

Five new groups passed twice. The second command's six legacy groups passed and
reproduced their original report exactly in this runtime. The separate older
five- and four-group suites were not rerun in full. Finite numerical checks do
not prove an asymptotic theorem. See [VERIFICATION.json](VERIFICATION.json).

The nested files retain their original dates, corrections and reports. New
files are a consolidated internal review, not an independent referee report,
exhaustive priority certificate, manuscript submission, or repository release.
