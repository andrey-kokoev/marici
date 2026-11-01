# A coarse layer boundary matching the native join geometry

## A positive geometric correspondence, with explicit limits

Replace each directed **white + coloured** two-edge step by its endpoint chord.
Topologically this contracts each white edge; place the resulting vertex at its
white tail. Each layer then has 45 coarse vertices and 72 coarse edges. No edges
or routes are added to the original viewer or layer model.

At an interior coarse vertex there are two incoming and two outgoing edges.
The incoming arms have squared length 3 and mutual cosine 1/2: **60°**, rather
than the original white star's 120°. The two outgoing directions are exactly the
straight continuations of the two incoming directions.

This matches the native upper join's two incoming arms and two carrier axes.
Native arms have squared length 2 and the same cosine. A plane similarity of
scale **sqrt(2/3)** maps the coarse endpoint geometry to the native geometry,
preserving the directed join/carrier incidence pattern.

This is a coarse metric, **not** a rigid identification of the original white
segment. Internal white vertices and the two-edge path lengths are not preserved;
the two outgoing coarse paths originally share a white segment. The operation
is therefore a genuine change of representation, not a newly discovered fold
that evades the earlier single-edge angle obstruction.

## What the geometric test does—and does not—choose

Only native arrival vertices and incoming ports are used to fit each plane map.
The mapped outgoing coarse endpoints then match the generated native carriers.
Both port bijections work for every layer against every native upper join:
8 layers × 4 joins × 2 bijections = **64 equally valid unlabelled local alignments**.

These are alternative local placements, not 64 successful wirings or a
simultaneous embedding of the stacked layers. Geometry alone has not selected
the port labels, a/p/e context, or relative placement of charts.

## Bringing the history bit to an incoming boundary

The previous experiment found two histories, BR and RB, on the first central
white segment. Follow a second return diamond: either a red-blue or blue-red
pair of coarse steps reaches the same next central vertex, after four branch
choices. Retain the colour remembered at the earlier white segment.

The histories that visited that earlier anchor give:

| History at the incoming boundary | Incoming port | Retained anchor colour | Candidate b | Remaining completions by next red / blue |
|---|---|---|---|---|
| BRBR | red | red | + | 8 / 8 |
| BRRB | blue | red | + | 8 / 8 |
| RBBR | red | blue | - | 8 / 8 |
| RBRB | blue | blue | - | 8 / 8 |

Thus the same coarse vertex supplies both the native-compatible incoming
geometry and a **conditional two-port/two-memory-state family**. Membership is
defined by a past visit to a geometrically selected anchor, not by matching a
desired native route. The retained bit is the colour at that anchor; it is no
longer simply the penultimate bit after moving the boundary two steps onward.

## The channel is not closed

The full layer construction also contains:

- **Two bypass histories**, BBRR and RRBB, reaching this boundary without visiting
  the anchor. All incoming histories therefore number six, with three per port,
  rather than four with two per port.
- **Four escaping histories**, BRRR, RBRR, BRBB and RBBB, that visited the anchor
  but take two equal-colour steps and reach neighboring vertices instead.

All are retained in the audit. The four selected classes are a causal subfamily,
not an isolated four-strand population. Treating them as a closed Wiring would
require a justified entry/return rule or population assignment; silently dropping
bypasses and escapes would manufacture the desired result.

## History supplies information, not yet a routing law

Each selected four-step history has sixteen full-route completions: eight take
red next and eight take blue. The layer graph itself chooses neither. Supplying
a retained bit therefore does not establish that the graph obeys a particular
memory-dependent continuation rule.

For illustration, if current red/blue port colour is encoded as active sign +/−
and anchor red/blue as b=+/−, the calibrated native input rule would impose:
**next coarse colour = opposite of the retained anchor colour**. This follows
because equal active and b signs take the oblique branch, while unequal signs
continue straight. Reversing the relative encoding instead gives a repeat rule.
Both continuations exist in the layer graph. Neither is selected by the current
reflection construction. This is an explicit candidate rule, not a claimed
native prediction or an added layer route.

## The next chart change is still missing

Even with the coarse join aligned, **eight of sixteen native next departures
leave its plane**. Their squared normal distance in native coordinates is 4/3;
the other eight remain in the plane. A single planar coarse layer therefore
cannot reproduce the complete next neighbourhood. A labelled, directed change
of chart or another specified three-dimensional construction is still needed.

The work has narrowed the gap: the join angle and carrier directions now have a
natural coarse representation, and suitable historical information is present.
What remains is an actual transport/occupancy rule and its plane-changing
correspondence—not another relabelling of paths followed by a success count.
No full layer-to-native wiring correspondence is claimed.

## Reproduction

- node --test tests/sulfur-coarse-interface.test.mjs
- node scripts/check-sulfur-coarse-interface.mjs
- Layer-side model: research/realization-tower/sulfur-coarse-interface.mjs
- Separate comparison: scripts/lib/sulfur-coarse-interface-probe.mjs
- Receipt: results/sulfur-coarse-interface-v1/verification.json
