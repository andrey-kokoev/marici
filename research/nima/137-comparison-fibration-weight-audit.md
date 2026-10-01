# 137 comparison slots under fibration and family promotion

## Domain and reference

Use two labelled four-state carriers. Each has all twelve directed nonidentity
edges; exclude the distinguished edge (0,1) from the counted leg selection,
leaving eleven selected legs. Keep all four state labels. The comparison domain is

    D = (E'_A x E'_B) disjoint-union (S_A x S_B),
    |D| = 121+16 = 137.

The exclusion defines this comparison view. The direct reference is retained
separately in the assembly; it does not require deleting a carrier record. See
[reference semantics](reference-semantics-carrier-versus-counted-domain.md) for
the distinction between retained carrier, local marks and counted subrelation.

An ordered pair here denotes a comparison slot. It is not by itself a composable
path. Aligning endpoints and requiring target(e)=source(f) leaves30 arrow pairs
for this reference choice, instead of121. That would change the domain rule.

## Grouping and fresh identities

Group arrow slots by the pair of source labels, keeping the arrow/state tag.
Treat state-pair slots as individual state records. Each side has outgoing
fiber sizes (2,3,3,3). Thus arrow group sizes are their pairwise products.
Target-indexing instead uses (3,2,3,3), giving the same size distribution.

| Number of groups | Members per group | Total members |
|---:|---:|---:|
| 1 | 4 | 4 |
| 6 | 6 | 36 |
| 9 | 9 | 81 |
| 16 | 1 | 16 |
| 32 | — | 137 |

Assigning a fresh label to every group preserves all137 slots through retained
membership. A label identifies a family; it does not give each family an equal
share of the original measure.

## Measure transported through grouping

Under the proposed uniform slot measure each slot weighs1/137. A group F must
then carry mass |F|/137. Within that group the conditional slot weight is1/|F|.
Their product is1/137, so regrouping and promotion preserve the readout exactly.
For any slot response f, the same identity is

    mean_D(f) = sum_F (|F|/137) * mean_F(f).

A different policy assigns each of the32 fresh labels equal mass1/32. That
gives individual state slots weight1/32, and arrow slots weights1/128,1/192,
or1/288 according to their group size. Arrow and state blocks now each have
mass1/2, compared with121/137 and16/137 under uniform slots. Both policies are
normalized, but they are different measures and generally yield different
physical readouts if used as weights.

Thus content-preserving family promotion requires transporting the measure as
well as membership if the weighted response is to remain unchanged. Uniformity
at one level need not remain uniformity across promoted family labels.

## Slot count versus independent response

The existing comparison assembly treats slots as products of two input legs.
For scalar legs at the all-unit baseline,

    delta(x_i*y_j) = delta x_i + delta y_j.

The11-by11 arrow block has response rank21 from22 leg parameters. The4-by4
state block has rank7 from8 parameters. The disjoint response map has rank28.
This calculation assumes independent scalar leg perturbations at that baseline;
it is not a rank theorem for arbitrary carrier dynamics or matrix-valued maps.
It demonstrates that137 distinct records need not be137 independent response
channels. One changed arrow leg affects11 slots; a state leg affects4.

## Does reference symmetry select the measure?

Fix directed reference (0,1) independently on each four-state carrier. Its
local stabilizer permutes only the other two points: S2 on each side. The
remaining eleven arrows have six orbits (one of size1 and five of size2),
and the four states have three orbits (sizes1,1,2). The comparison domain has
36 arrow-pair orbits and nine state-pair orbits under S2 x S2.

An invariant normalized nonnegative measure is determined by45 orbit masses
summing to one:44 free parameters. Additional carrier identifications may
reduce the symmetry group; they require a new census rather than an assumed
uniform measure. The following three measures are all invariant under this
reference stabilizer and preserve readouts under correctly weighted grouping:

| Trial measure | Arrow block mass | Reverse-reference arrow-leg response | Reference-source state-leg response |
|---|---|---|---|
| Uniform slots | 121/137 | 11/137 | 4/137 |
| Equal orbit masses | 4/5 | 2/15 | 1/15 |
| Equal block masses, uniform within each | 1/2 | 1/22 | 1/8 |

Responses are derivatives of the scalar assembled mean at unit input legs.
They measure sensitivity to one primitive perturbation; they are not feedback
loop gains or electromagnetic couplings. The state and arrow perturbations
need a physical common normalization before their sensitivities can be compared
as physical responses.

Even assuming uniformity within each block leaves its relative mass beta free:

    R_beta = beta * mean_arrow(response) + (1-beta) * mean_state(response).

The leg sensitivities are beta/11 and (1-beta)/4. Uniform slots require
beta=121/137, giving equal per-slot weights beta/121=(1-beta)/16=1/137.
Thus equal per-slot weight is a precise additional rule, not a consequence
of the reference stabilizer or fibration invariance. A response or resource law
must select the relative block weight and any within-block orbit differences.

Verification:

    python research/nima/checkers/check_137_reference_symmetry.py

The checker enumerates all45 orbits, constructs three distinct normalized
invariant measures, checks grouped readout invariance, and calculates the stated
primitive sensitivities with exact fractions.

## Consequence for electromagnetic normalization

The count137 survives these membership-preserving presentations. Equal slot
weight remains1/137 if its measure is transported. The fibration architecture
does not select that initial measure or identify its average with electromagnetic
coupling. The next calculation needs a carrier-selected response observable
and a rule fixing primitive weights. Its invariance under presentation changes
can then be tested using the grouped-measure identity above.

## Verification

    python research/nima/checkers/check_137_fibration_weights.py

Exact fractions check source/target group census, promoted membership recovery,
measure transport, equal-group alternative, composable-pair count, and Gaussian
elimination rank of the137-by30 scalar linear-response matrix. No measured
coupling value is used.
