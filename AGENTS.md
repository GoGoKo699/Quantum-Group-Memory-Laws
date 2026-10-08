# Repository instructions

## Exact destination

This repository is `GoGoKo699/Quantum-Group-Memory-Laws`. Verify live main and the requested task before writes. Do not transfer permissions to another project. Do not use the older Bell or electron PDFs as inputs here.

## Scientific contract

Read `research/MODEL_AND_CLAIMS.md`, `research/THEOREM.md`, and `work_orders/CURRENT.md`. Keep the physical trace and multiplicity weights; distinguish edge, bulk, weak-deformation, and fixed-distance limits. q0 is a sufficient proof threshold, not a phase transition. An exact symmetry projection is not the entire plateau of every Hamiltonian. The noisy realization is unrecorded/averaged, full-algebra preserving, and finite-size; its dissipative-gap scaling is unknown.

The full proof is author-side and remains subject to independent scrutiny. Checkers are not proof of uniform asymptotics. Code success, correctness, originality, significance, and implementation status must remain distinct. Do not add target-journal claims to current public notices.

## Preservation

Keep every file under `archive/research-handoff-2026-10-08/` byte-identical. `provenance/IMPORT.json` identifies those protected bytes, the owner's license and the initial README. Never refresh a canonical report, import hash, scientific tolerance, or historical date to obtain a pass. Preserve failed attempts as evidence, not main-reader progress bars.

Active copies use only the declared transformations in `provenance/ACTIVE_EDITS.json`. For navigation or math-display edits, update the explicit edit specification and documentation-integrity hashes together, without modifying the immutable source. A scientific correction requires an explicit erratum/new claim and review; do not disguise it as presentation work.

## Workflow and checks

Use a feature branch and a reviewable PR. Run `python -m unittest discover -s tests -v` and the appropriate verification mode in `VERIFICATION.md`. For initial/full verification, run all five original suites (24 groups total) unchanged. Fixed numeric report-comparison tolerances are separate from the original scientific assertions; any discrepancy is recorded, not hidden.

Do not write test outputs into the archive. Use `build/` or a separate evidence location. Preserve `LICENSE` exactly. Review the diff and source-matched PR artifact, merge only the expected reviewed head, then verify merged main separately. CI must have read-only repository permissions; a one-time bootstrap, if used for import, must not remain in the merged tree.

Keep current work bounded. Submission, release, external communication, repository-setting changes and unrelated extensions require separate authorization.
