# Verification and evidence contract

## What is preserved

The 79-file source handoff is immutable under `archive/research-handoff-2026-10-08/`. `provenance/IMPORT.json` records its SHA-256 file list and the owner's unchanged license. All five original nested manifests are verified recursively. `provenance/ACTIVE_EDITS.json` specifies the navigation, math-display, import-status, and reader-facing exposition transformations for the three active scientific copies. No scientific formula, original checker, canonical report or scientific assertion tolerance is changed.

`provenance/DOCUMENTS.json` is separate documentation-integrity metadata. A reviewed documentation edit can update it; it must not refresh the protected import hashes.

## Commands

Use Python 3.13.5 and the exact versions in `requirements.txt` for the hosted reference environment. Other environments can be investigated, but must be recorded rather than called identical.

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tools/verify.py --output build/verification
python tools/check_foundations.py --output build/verification/foundations.json
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

Every subprocess retains its original assertions and tolerances and writes its output outside the archive. Scientific success requires the original exit status and expected group count. The infrastructure separately checks report structure, exact strings/Booleans/integers and finite floating-point values. Its report-comparison allowance is `abs(actual-reference) <= 2e-12 + 2e-10*abs(reference)`. This is separate from the scientific assertions.

Every nonidentical numeric field is listed in the receipt with both values and its absolute difference. Byte identity is reported separately. No original reference is overwritten. A failed comparison is investigated, not silently normalized or accepted by widening a tolerance.

The wrapper records the complete source-file hash map before execution, verifies it afterward, and refuses output directories within protected source locations. The ten infrastructure tests include negative controls for changed schemas/values, unsafe paths, and prohibited output locations.

## Complementary analytical checks

`tools/check_foundations.py` checks the supporting derivations in [physical mechanism](research/PHYSICAL_MECHANISM.md), [kernel details](research/KERNEL_DETAILS.md), and [attribution](literature/ATTRIBUTION.md). Its four groups compare independent expressions: the elementary spatial profile against the original integral; conditional sector overlaps and observable normalizations against dense physical projections; Pauli bond reflections, jump dissipators and the undeformed weighted-path evolution; and the free Jost convolution against exact rational killed-walk propagation.

These checks retain all 24 original groups and their canonical comparisons. They use small Hilbert spaces and fixed interior profile points, with exact arithmetic for the free kernel. They check identities and normalization, not uniform asymptotic limits. The separate `foundations.json` report records its checked commit, environment, source hashes, group results, fixed tolerances, and source-integrity result; no canonical report is regenerated.

## Hosted evidence

The workflow checks out the **actual PR head** for a pull-request event, not GitHub's synthetic merge commit. It records the checked-out commit, event SHA, source hashes, environment, original-suite logs, original-versus-reproduced report comparisons, and source-integrity outcome. `quantum-group-verification-<run_id>` contains these files and the infrastructure log. A separate `push` run checks the actual merged `main`.

Before merging, inspect the PR diff and download its artifact. Compare every source hash to the reviewed local tree; inspect all suite outputs and discrepancies. Merge only the reviewed expected head. Then inspect and download the separate merged-main artifact and verify the merged source tree again. Record exact run IDs, commit IDs and findings in the PR conversation so source files need not claim evidence about their own not-yet-executed commit.

The hosted artifact also contains `foundations.json`. Inspect its four group results and match its source hashes and commit to the same reviewed revision; keep its checks distinct from the 24 original groups and ten infrastructure tests.

A green badge or steps-only summary is not source-matched verification. Local execution, PR-head execution, and merged-main execution are separate receipts. No hosted success is asserted in advance by this document.

## Interpretation

The full physical Hilbert-space checks use dimensions up to 256. Larger chain lengths use polynomial-size recurrence arrays. These checks test identities, normalizations, and evaluations; the uniform asymptotic laws rest on the analytical arguments linked in the [proof map](research/PROOF_MAP.md).
