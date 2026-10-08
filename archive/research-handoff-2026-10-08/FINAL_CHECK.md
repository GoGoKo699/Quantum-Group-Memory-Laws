# Quantum-group memory: final operational check and departure point

**7 October 2026.** Retain one consolidated quantum research result. The next transition is a dedicated repository and workspace once its destination is explicitly created/authorized. No repository was checked, created or modified in this pass. Suggested working name remains **Quantum-Group-Memory-Laws**.

## What is unchanged

The mathematical specification is [prior/THEOREM.md](prior/THEOREM.md), preserved byte-for-byte. The complete ordinary-trace quantum-group projection gives $L^{-1/2}$ end-spin memory for fixed finite real $q>1$, and $\mathcal K(q)\mathcal F(x)L^{-2}$ at a fixed bulk fraction for fixed $q>q_0=2.0810189966\ldots$. The normalized bulk shape is independent of q within this proved domain. At q=1 the answer remains exactly 1/L everywhere.

The threshold is a sufficient proof condition. This pass does not extend the range or change an amplitude, use a quantum trace, infer a time exponent, or establish the full plateau of every deterministic Hamiltonian. The detailed uniform proof is the unchanged prior/prior/FOLLOWUP.md, not replaced by new numerical evidence.

## What was added

[LOCAL_REALIZATION.md](LOCAL_REALIZATION.md) shows that the already supplied local bond-noise model can be combined with any Hamiltonian preserving the full algebra. At fixed finite L, every positive noise strength converges to the same projection, with a norm bound in terms of the unestimated finite-size dissipative gap. This is an explicitly proved specialization of established open-system commutant theory, not a new central result. Two controls distinguish missing bonds and preservation of only U(1).

The same note explains why enhanced boundary overlap and suppressed bulk overlap are compatible with an unchanged dimension of the symmetry algebra. The elementary rank identity sums over the complete Pauli basis, not only one-body spins; it gives no physical transport-of-memory statement.

[SOURCE_CHECK.md](SOURCE_CHECK.md) adds the closer Gorbenko--Zhabin v2 construction comparison, rechecks the motivating model's incomplete-charge qualification, and explicitly credits Li--Sala--Pollmann for the coherent-plus-noisy stationary-commutant principle.

## Contribution decision

The candidate is a spatially resolved finite-size law for the complete memory enforced by a nonlocal spin symmetry. The added asymptotics, not a new Mazur bound, new definition of symmetry, local-noise principle or Haar calculation, carry the scientific claim. The physically simple contrast is enhanced unavoidable end-spin memory and suppressed unavoidable bulk memory relative to SU(2), with all fractions vanishing as L grows.

The main skeptical questions remain novelty and the breadth of this representation-specific result. Our statement concerns a well-defined symmetry baseline and a local noisy dynamics attaining it; it must not be promoted into a solution of the motivating paper's deterministic hydrodynamics. The current source reconstruction supports retaining this bounded contribution, not guaranteed editorial acceptance. No external independent review has occurred.

**Stop automatic scientific expansion.** Weak-deformation crossover, generic local-Hamiltonian plateau saturation, noise-gap scaling, finite temperature, other spins, encoded memory and a laboratory implementation remain optional different claims. Reopen for a specific proof objection, a directly covering source, or an explicitly selected new result. Another table or repeated regression suite is not required merely to continue.

## Verification in this pass

Four new groups passed twice and the two reports are byte-identical. They test stationary-subspace equality for local interactions plus preserving noise, finite-size contraction, piecewise preserving controls, algebra non-nesting and the full Pauli sum, and broken-hypothesis controls. The largest new Hilbert space is 16 (operator-space matrix dimension 256).

The immediate preceding five-group review checker ran unchanged and passed. Its report is byte-identical to the original reference. Its legacy finite-Hamiltonian controls use a Hilbert space of dimension 256; thus the largest physical Hilbert space executed anywhere in this turn is 256. The earlier six-, five- and four-group suites were not rerun in full. Some exact legacy routines are imported by targeted tests.

All 64 original files in the incoming review archive are preserved. Original theorem text, source checkers, reports and nested manifests are not refreshed. No new scientific assertion failed; no formula or assertion tolerance was edited to obtain a pass. A shell log-monitor command used an unsupported short option and was rerun with the standard option; it did not execute or alter scientific code. Exact evidence appears in VERIFICATION.json.

The original proof files include historical October 8 labels. Those labels are retained as provenance rather than silently edited to the current October 7 date.

## Reproduction and future import

From this directory:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python check_final.py --output reproduced.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python prior/check_review.py --output prior_review_reproduced.json
```

Read [PROJECT_HANDOFF.md](PROJECT_HANDOFF.md) before a future repository import. No old-project write authorization is transferred and no repository address is assumed available.
