# Finite-q bulk symmetry memory — analytical checkpoint

Read `FOLLOWUP.md` for the full result, proof, physical scope, and precise inherited ingredients. The proved bulk domain is fixed `q > 2.0810189966245356`, with the observation site at a fixed interior fraction of an open spin-1/2 chain. This is a sufficient technical condition, not a phase transition. The exact boundary law from the prior note remains valid for every fixed q>1.

The new result is an author-side asymptotic proof for the **complete symmetry projection**, not a proof that every closed Hamiltonian saturates that bound. No dynamical exponent, encoded-memory guarantee, apparatus, manuscript, or new repository is claimed.

## Contents

- `FOLLOWUP.md`: theorem, proof including the full-recursion domination and matching steps, spectral evaluation, limitations, and source-reading record.
- `bulk_tools.py`, `check_bulk.py`: evaluation routines and six finite mathematical/numerical check groups. Numerical diagnostics do not prove asymptotic limits.
- `report_initial.json`, `report.json`, `report_repeat.json`: three equal completed reports, plus their actual execution logs.
- `VERIFICATION.json`: exact old-file preservation and old-report difference record.
- `prior/`: the complete unchanged immediate input archive, including its own unchanged earlier pilot. Historical gaps remain in those historical notes; the current proof resolves the finite-q bulk gap only within its declared range.

## Reproduction

The recorded environment is Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. Install the pinned numerical dependencies, then run from this directory:

```sh
python -m pip install -r requirements.txt
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python check_bulk.py --output reproduced.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python prior/check_asymptotics.py --output reproduced_prior_asymptotics.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python prior/prior/check_memory.py --output reproduced_prior_memory.json
```

Write fresh reports, not over archived canonical reports. Exact byte reproduction is environment dependent; fixed scientific assertions and the difference record distinguish numerical variation from changes to the reference. Full Hilbert-space checks remain small: dimension 16 in the new checks, and dimension 256 in the rerun legacy suite. Larger chain results use scalar recursion arrays.

This archive excludes interpreter caches and third-party source PDFs. `MANIFEST.json` hashes every packaged file other than itself. Its purpose is integrity, not scientific or novelty certification.
