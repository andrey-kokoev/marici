# Identical-beam orientation no-go: WP679

## Source preparation

The smallest available collider preparation is an unpolarized identical-beam
proton-proton source. Its physical groupoid includes exchange of the two beam
labels,

\[
b\longleftrightarrow-b.
\]

No native event field in the WP674 cascade selects one label as positive.

## Descent obstruction

The WP678 reference-assisted CP port would have the form

\[
S=D b\sqrt{uv}\sin\phi.
\]

It is odd under beam exchange. Therefore the untagged identical-beam
expectation vanishes exactly:

\[
\frac{S(b)+S(-b)}{2}=0.
\]

Squaring the port makes it descend, but also makes it even under
\(\phi\leftrightarrow-\phi\). It cannot distinguish the conjugate source
points.

## Smallest relational repair

A source-derived beam-odd event tag (t) changes sign together with (b).
Then (tS) is beam-exchange invariant while remaining odd in (phi). This
would be a legitimate relational orientation, not an absolute beam label.

The present cascade grammar contains no admitted associated-production channel
that supplies such a tag. A candidate must be derived from a concrete hard
process and accompanied by calibrated tag dilution and sign-assignment error.

## Disposition

The existing proton-proton preparation does not orient the WP678 reference.
Phase recovery remains unavailable. A tagged production analysis would define
a new source/readout context and must be tested for rank after its dilution is
included.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp679_identical_beam_orientation_no_go.py

Generated result: results/wp679_identical_beam_orientation_no_go.json.
