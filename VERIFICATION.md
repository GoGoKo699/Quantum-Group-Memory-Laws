# Verification and evidence contract

## What is preserved

The 79-file source handoff is immutable under `archive/research-handoff-2026-10-08/`. `provenance/IMPORT.json` records its SHA-256 file list and the owner's unchanged license. All five original nested manifests are verified recursively. `provenance/ACTIVE_EDITS.json` specifies the navigation, GitHub math-delimiter and import-status transformations for the three active scientific copies. No scientific formula, original checker, canonical report or scientific assertion tolerance is changed.

`provenance/DOCUMENTS.json` is separate documentation-integrity metadata. A reviewed documentation edit can update it; it must not refresh the protected import hashes. The archived date labels are preserved even where their chronology is inconsistent.

## Commands

Use Python 3.13.5 and the exact versions in `requirements.txt` for the hosted reference environment. Other environments can be investigated, but must be recorded rather than called identical.

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tools/verify.py --output build/verification
```

For an infrastructure-only documentation check:

```sh
python tools/verify.py --infrastructure-only --output build/infrastructure
```

That mode executes **no scientific suite**. It cannot stand in for the full initialization or scientific-change checks.

## Unchanged scientific suites

All paths below are relative to the protected handoff root.

| Suite | Original entry | Groups |
|---|---|---:|
| Finite physical projection and recursion | `prior/prior/prior/prior/check_memory.py` | 4 |
| Boundary, fixed-distance and auxiliary asymptotics | `prior/prior/prior/check_asymptotics.py` | 5 |
| Fixed-deformation bulk proof controls | `prior/prior/check_bulk.py` | 6 |
| Plateau dictionary and contribution-review controls | `prior/check_review.py` | 5 |
| Coherent-plus-noisy local realization | `check_final.py` | 4 |
| **Total** | | **24** |

Every subprocess retains its original assertions and tolerances and writes its output outside the archive. Scientific success requires the original exit status and expected group count. The infrastructure separately checks report structure, exact strings/Booleans/integers and finite floating-point values. Its newly declared report-comparison allowance is `abs(actual-reference) <= 2e-12 + 2e-10*abs(reference)`. This is not a replacement for an original assertion.

Every nonidentical numeric field is listed in the receipt with both values and its absolute difference. Byte identity is reported separately. No original reference is overwritten. A failed comparison is investigated, not silently normalized or accepted by widening a tolerance. Historical floating-point differences already recorded in the archive remain visible.

The wrapper records the complete source-file hash map before execution, verifies it afterward, and refuses output directories within protected source locations. The ten infrastructure tests include negative controls for changed schemas/values, unsafe paths, and prohibited output locations.

## Hosted evidence

The workflow checks out the **actual PR head** for a pull-request event, not GitHub's synthetic merge commit. It records the checked-out commit, event SHA, source hashes, environment, original-suite logs, original-versus-reproduced report comparisons, and source-integrity outcome. `quantum-group-verification-<run_id>` contains these files and the infrastructure log. A separate `push` run checks the actual merged `main`.

Before merging, inspect the PR diff and download its artifact. Compare every source hash to the reviewed local tree; inspect all suite outputs and discrepancies. Merge only the reviewed expected head. Then inspect and download the separate merged-main artifact and verify the merged source tree again. Record exact run IDs, commit IDs and findings in the PR conversation so source files need not claim evidence about their own not-yet-executed commit.

A green badge or steps-only summary is not source-matched verification. Local execution, PR-head execution, and merged-main execution are separate receipts. No hosted success is asserted in advance by this document.

## Interpretation

The full physical Hilbert-space checks are small (up to dimension 256 in the original suites). Larger chain lengths use polynomial-size recurrence arrays. These tests do not independently prove a uniform asymptotic theorem, establish exhaustive originality, prove a hydrodynamic exponent, or certify a device.
