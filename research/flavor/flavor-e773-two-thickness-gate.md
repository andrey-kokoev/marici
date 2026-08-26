# E773 two-thickness no-refit gate (WP409)

## Executed experiment

Fermilab E773 implemented two active scintillator regenerators. The proposal
specified 40 cm and 61 cm carbon-dominated lengths in two beams, switched between
beam lines. The completed experiment extracted neutral-kaon interference phases,
the $K_L-K_S$ mass difference, and the $K_S$ lifetime. This is direct evidence
that multiple regenerator settings and finite-width decay spectroscopy are
experimentally executable.

Primary records are the [E773 proposal](https://lss.fnal.gov/archive/test-proposal/0000/fermilab-proposal-0773.pdf),
the [completed-result summary](https://arxiv.org/abs/hep-ex/9407001), and the
[published result](https://doi.org/10.1103/PhysRevLett.74.4376).

## Exact insufficiency

For an intercept, affine thickness response, and quadratic correction, the two
rows at 40 cm and 61 cm have rank two. The exact checker produces a nonzero
one-dimensional kernel. Thus the two physical records cannot distinguish a
quadratic completion from a changed intercept and slope.

E773 also lacked a simultaneous vacuum beam for the incident kaon spectrum. Its
analysis floated two parameters to compensate for the unknown input flux. The
second regenerator record therefore depends on a second fitted normalization; it
is not a displacement predicted from the first regenerator without refitting.

A source-off record combined with both thicknesses would make the quadratic
design rank three, but it still would leave no separately withheld material
setting. This is the smallest exact obstruction.

## Disposition

E773 strengthens WP406's executability claim and supplies a real two-context
finite-width instrument. It cannot replace WP408's sealed four-setting protocol.
Completion requires source-off input calibration, enough open material settings
to type the admitted correction grammar, and a separately sealed event sample.

Run `uv run --with sympy python
research/flavor/checkers/wp409_e773_two_thickness_gate.py` to regenerate the
JSON result.
