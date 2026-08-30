# The maximal declared experimental probe algebra is physical16-generated (WP67, move 8/12)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

The largest probe family with an instrument declared by the flavor source is
the algebra of reconstructible functions of six masses, CKM amplitudes, and
CP-odd data. `physical16` is the faithful generic coordinate used for this
algebra: six ordered singular values, all nine CKM moduli, and signed (J).

Its polynomial subalgebra is represented by spectral power traces, mixed Gram
words, and a CP-odd commutator invariant. Exact tests establish full
weak-basis descent and separation of the measured-ten hostile pair. The same
algebra intentionally identifies generation-exchange deck presentations with
equal `physical16`; the deck-odd row lies outside the physical algebra.

Contextual equivalence is therefore generic equality of `physical16`. This is
joint faithfulness on physical points, not selection: the algebra evaluates
states and has no proper-image operation. Any UV or generation-reference probe
would add a new experiment and needs separate instrument authority.

Verification:
`uv run --with sympy python research/flavor/checkers/wp67_experimental_probe_algebra.py`.
