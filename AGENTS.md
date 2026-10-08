# Repository instructions

## Exact destination

This repository is `GoGoKo699/Quantum-Group-Memory-Laws`. Verify live main and the requested task before writes. Do not transfer permissions to another project. Do not use the older Bell or electron PDFs as inputs here.

## Scientific contract

Read `research/MODEL_AND_CLAIMS.md` and `research/THEOREM.md`. Preserve the ordinary physical trace and multiplicity weights, the q>1 edge law, q>q0 bulk domain, exact q=1 result, and orders of limits. Distinguish edge, bulk, weak-deformation, and fixed-distance limits. q0 is a sufficient proof threshold, not a phase transition. Keep the symmetry projection, Hamiltonian-specific excess, generally nonlocal random-eigenbasis reference, and local noise-averaged attainment distinct. The noisy realization is unrecorded/averaged, full-algebra preserving, and finite-size; its dissipative-gap scaling is unknown.

The single tutorial anchor is Moudgalya–Motrunich, arXiv:2108.10324v2. Keep `research/TUTORIAL_BRIDGE.md` and its notation dictionary consistent with the route from conserved algebra and physical projection to the sector mechanism, spatial theorem, proof, and local realization. Use `literature/ATTRIBUTION.md` for source comparisons.

Reader-facing pages explain results and hypotheses; maintenance evidence belongs in PR records. Reopen research for a named proof objection, a directly covering source, or an explicitly selected new claim.

The full proof is author-side and remains subject to independent scrutiny. Checkers are not proof of uniform asymptotics. Code success, correctness, originality, significance, and implementation status must remain distinct. Do not add target-journal claims to current public notices.

## Preservation

Keep every file under `archive/research-handoff-2026-10-08/` byte-identical. `provenance/IMPORT.json` identifies those protected bytes, the owner's license and the initial README. Never refresh a canonical report, import hash, scientific tolerance, or historical date to obtain a pass. Preserve failed attempts as evidence, not main-reader progress bars.

Active copies use only the declared transformations in `provenance/ACTIVE_EDITS.json`. For navigation or math-display edits, update the explicit edit specification and documentation-integrity hashes together, without modifying the immutable source. A scientific correction requires an explicit erratum/new claim and review; do not disguise it as presentation work.

## Workflow and checks

Before editing, inspect live main's source-matched verification receipt and separate merged-main workflow. Complete missing or incomplete hosted verification before further development; reuse existing evidence for unchanged source.

Use a feature branch and a reviewable PR. Run `python -m unittest discover -s tests -v` and the appropriate verification mode in `VERIFICATION.md`. For initial/full verification, run all five original suites (24 groups total) unchanged. Fixed numeric report-comparison tolerances are separate from the original scientific assertions; any discrepancy is recorded, not hidden.

Do not write test outputs into the archive. Use `build/` or a separate evidence location. Preserve `LICENSE` exactly. Review the diff and source-matched PR artifact, merge only the expected reviewed head, then verify merged main separately. CI must have read-only repository permissions; a one-time bootstrap, if used for import, must not remain in the merged tree.

Keep current work bounded. Submission, release, external communication, repository-setting changes and unrelated extensions require separate authorization.
