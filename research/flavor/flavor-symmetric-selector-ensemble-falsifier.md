# Symmetric-selector ensemble falsifier (WP313)

## Canonical fitted domain

The checker consumes all 1,210 records in the canonical WP20 viable ensemble.
For each record it rebuilds the stored Yukawa textures, diagonalizes
(Y_uY_u^\dagger) and (Y_dY_d^\dagger), and compares their ordered positive
singular spectra. These are weak-basis invariants rather than texture-chart
coordinates.

WP312 predicts (M_u=M_d), hence identical ordered spectra. Its coarser
reciprocal prediction also requires

\[
\frac{m_{u,\max}/m_{u,\min}}{m_{d,\max}/m_{d,\min}}=1.
\]

## Complete-ensemble result

At the declared numerical equality tolerance, zero of the 1,210 fitted sheets
has equal up/down spectra and zero has equal hierarchy ratios. The generated
result records the closest hostile sheet for each condition, including its
ordered singular values and invariant log-distance. The closest spectrum gap
is approximately (4.0808), more than eight orders of magnitude above the
declared tolerance, so the conclusion is insensitive to floating-point noise.

Thus WP312 passes source descent, stability, zero response rank for its ratio,
and coefficient-family selection, but fails the numerical prediction on the
complete fitted ensemble. This is a useful negative selector rather than a
rigidifier masquerading as one.

## Successor gate

A viable successor needs independently derived exchange breaking that produces
unequal spectra. It must retain a predeclared proper `physical16` prediction;
fitting the breaking parameters to the readout would revert to WP301's
target-coded coefficient problem.

Run `uv run --with numpy --with scipy --with sympy python
research/flavor/checkers/wp313_symmetric_selector_ensemble_falsifier.py` to
regenerate the complete-ensemble audit.
