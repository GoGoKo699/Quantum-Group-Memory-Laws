# Actual GitHub mathematics

The read-only collector visits commit-pinned public GitHub pages at widths 1440 and 760. It compares every recognized source expression with actual hosted MathML, preserves structural child positions, checks display geometry, and saves HTML and screenshots for separate visual review.

Install `playwright@1.56.1` and `mathjax-full@3.2.1` outside the source tree, install Chromium, then run:

    node verification/hosted/capture_hosted_math.cjs --root . --repository GoGoKo699/Quantum-Group-Memory-Laws --revision FULL_COMMIT_SHA --output build/hosted-review --page README.md

Repeat `--page` for the intended active science, research, learning and reference pages. The workflow records its complete page inventory. Immutable historical archives are preserved source material; they are excluded from the active reader-page capture. Use a new empty output directory for every attempt.

The report binds source hashes, actual hosted expressions, both viewports and capture artifacts. Automated comparison does not establish the scientific proof or replace reading the screenshots. Browser access is anonymous; this workflow requests only `contents: read` and uses no credentials in the checked-out source.
