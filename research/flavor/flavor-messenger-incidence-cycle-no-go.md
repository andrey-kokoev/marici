# Messenger-incidence cycle no-go

## Bounded question

Does the complete WP489 two-sector messenger incidence contain any closed
coupling product whose phase or sign survives all legal field rephasings?

## Exact incidence theorem

Use the six entrance, connector, and exit vertices together with the four
singlet-generated messenger masses. Form the signed interaction-by-field
incidence matrix: barred fermions enter with coefficient minus one, unbarred
fermions and ordinary scalars with plus one, and the conjugate up doublet with
minus one.

The ten interaction rows have exact rank ten. Their left kernel is zero.
Consequently no nonempty product of the ten coupling phases is invariant under
all continuous field rephasings. Reducing the same incidence modulo two also
has zero left kernel, so no nonempty product of coupling signs is invariant.

The structural reason is visible without elimination: terminal fields such as
the two entrance doublets and right-handed quarks provide leaves that force the
coefficient of their incident row to vanish, and the constraint propagates
inward through both messenger chains.

## Consequence for the selector search

WP633's sign collapse is not an accident of the chosen singlet reference. The
current interaction hypergraph has no closed interference cycle at all. Every
candidate phase or sign can be transported into field coordinates before the
map to `physical16`. The source therefore contains no rephasing-invariant
internal probe capable of selecting the proposed relative class.

An additional interaction helps only if its incidence closes a cycle and is
independently legal under the complete gauge group. Since the up and down
messengers differ by one unit of hypercharge, a direct cross-sector bilinear is
forbidden without an additional charged carrier or an electroweak insertion.
Such a carrier changes the source field census, thresholds, anomalies, decay
channels, and instrument grammar. Algebraic addition of a dependent row is not
yet executable physics.

## Disposition

The current common-singlet messenger source has zero internal phase/sign-cycle
capacity. It rigidifies route presentations and matches Yukawa magnitudes, but
it supplies neither a relative-sign selector nor an internal interference
instrument. The smallest exact falsifier is the full row rank of the ten-by-
sixteen signed incidence matrix.

The next progressive branch must declare a gauge-legal cycle-closing carrier
independently of the desired phase, then recompute source closure and test
whether its invariant product descends to `physical16` and a calibrated
threshold observable.

## Reproduction

Run:

    python research/flavor/checkers/wp634_messenger_incidence_cycle_no_go.py

The generated result is
`research/flavor/results/wp634_messenger_incidence_cycle_no_go.json`.

