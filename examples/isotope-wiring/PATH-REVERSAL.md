# Explicit path-reversal audit

## Current interpretation: PE-based frame return

The current diagram convention supersedes the older separate-P/E path example:
PE is one distinguished vertex with incoming/outgoing legs. Triangles and neutron
squares denote directed paths, not filled shapes. The requirement is return to
the same PE vertex **and the same entire frame**, including reversed traversal.

`core/frame-return.mjs` implements that numerical contract separately from the
older NNPE/NNNN-labelled audit below. Run:

```sh
node --test tests/isotope-wiring-frame-return.test.mjs
node scripts/check-isotope-path-reversal.mjs --frame
node scripts/check-isotope-path-reversal.mjs --frame path/to/definition.json
```

Supply `frameTopology` with `vertices: [{id, role}]` (role `PE`, `N`, or
`junction`), `edges: [{id, from, to, support, reverse, transport}]`, and
`walks: [{id, base, edges, kind}]`. Kind defaults to `PE`, whose base must be a PE
vertex. Explicit `kind: 'N'` checks a neutron cycle based at an N vertex. `transport` is an explicit
3-by-3 SO(3) matrix; column frames obey `F_next = R_edge F`. The accumulated
product is in traversal order, `R_last ... R_first`. Return requires that product
to be the identity within the reported tolerance, not merely preservation of
one axis. Reverse arrows must retain incidence/support and carry inverse
transports. Optional allowed `turns` are edge-ID pairs; closing turns are checked
in both directions. Each PE vertex needs at least one supplied walk for coverage.
This checks those walks only, not all possible cycles or a uniquely determined
routing rule at branching vertices.

Missing transports return `unknown`; they are never silently treated as identity.
Reflections, nonorthogonal matrices, open walks, residual rotation, and forbidden
reverse turns fail. Numerical tolerance defaults to 1e-9. These are finite numeric
checks, not exact formal proofs or a derivation of SO(3) from the diagram.

**Still missing from Ca46:** directed path incidence, permitted routing at
junctions, and per-edge frame transport. Screen angles cannot determine a 3D
transport law. The current drawing therefore still reports `unknown`; tests use
explicitly synthetic rotation assignments, not inferred isotope dynamics.

## Ca46 drawing-bound local-cycle trial

```sh
node scripts/study-ca46-frame-return.mjs
node scripts/study-ca46-frame-return.mjs temp/ca46-frame-study.json
node --test tests/isotope-wiring-diagram-path-trial.test.mjs
```

`core/diagram-path-trial.mjs` reads the current renderer's cell polygons and
coherence contours, binding all 20 stored PE occurrences and six wrapper cycles.
It does not change the drawing or mark the fixture verified. This is partial:
vertices remain occurrence-local, ten vertical crossed-square diagonals are
unbound, and no global junction routing is asserted. The trial explicitly chooses
red-leg-in/blue-leg-out at PE and rendered contour order for N; its candidate
reverse arrows are declared assumptions, not extracted native inverse witnesses.

Two controls operate on the same bound topology:

- Planar turning transports use rotations about the screen normal at each corner.
  All 26 local walks return their frame, in the SO(2) subgroup of SO(3), by
  construction. This cannot select the preferred wrapper arrangement.
- Adding a quarter-turn to one PE edge and updating its reverse to the proper
  inverse preserves all incidence and counts, but that PE walk fails frame return.

Thus the current drawing alone does not select a transport law. The unassigned
packet reports `unknown`; the planar control verifies and the twisted control
refutes. The overall diagram remains `unknown` until junction routing, remaining
strokes, and the frame-transport law are supplied. The study command returns zero
when those expected control results are reproduced, not when Ca46 is verified.

## Endpoint-glued graph trial (all vertical diagonals included)

```sh
node scripts/study-ca46-connected-paths.mjs temp/ca46-connected-paths.json
node --test tests/isotope-wiring-connected-path-trial.test.mjs
```

`core/connected-path-trial.mjs` identifies equal explicit endpoint coordinates,
retains the 20 PE occurrence-to-vertex bindings, merges equal segment supports
while retaining their sources, and includes all ten vertical diagonals. It leaves
interior crossings unjoined and does not interpret enclosure as incidence.
These are declared candidate gluing rules, not silently inferred native topology.

On the current Ca46 drawing this produces 47 vertices, 76 undirected supports,
**7 components**, 27 branching vertices, and 20 unjoined interior crossing pairs.
Ten of the twenty projected crossings are now identified explicitly: each
two-PE square is a top-view projection of an abstract tetrahedron, with four
vertices and all six edges. Its horizontal and vertical diagonals are opposite
**neutron legs**, with four distinct endpoints; they do not meet at a central
vertex. Each tetrahedron vertex has internal degree three. The other ten
crossings retain the candidate non-joining convention, not a derived decision.
No depth order, metric tetrahedron, or frame transport is inferred from this.
Thus the drawing is not one connected path graph under endpoint-only gluing.
A spanning forest constructs all 36 fundamental cycles (`E − V + components`),
in addition to the retained primitive local walks. At branching vertices the
number of non-backtracking choices is reported; controls allow all composable
turns, but no deterministic physical routing has been chosen.

A noncommuting vertex-frame gauge assignment `R_uv = G_v G_u^T` returns frames
on every checked cycle by telescoping. Twisting a non-tree support, while updating
its reverse to the inverse, breaks frame return without changing incidence. This
is a global transport control, not a derived law: it cannot make the unresolved
gluing/routing choices or select a preferred drawing. Overall status stays
`unknown`. The command's zero exit status means the expected control outcomes
were reproduced, not that the diagram was physically verified.

## Ca44 comparison

```sh
node scripts/study-calcium-connected-paths.mjs Ca44 temp/ca44-connected-paths.json
node scripts/study-calcium-connected-paths.mjs Ca46 temp/ca46-connected-paths.json
```

The shared binder now accepts Ca44 and Ca46; the original Ca46-only entrypoints
retain their scope checks. Ca44 has ten projected tetrahedra and four coherence
contours spanning 1+2, 2+3, 1+2+3, and 3+4. Wrapper tip contacts are checked at
all three shell junctions. Every PE occurrence retains a traced forward/reverse
local route; the ten vertical neutron legs are present too.

Under the same candidate endpoint-gluing policy, Ca44 has 39 vertices, 68
supports, five components, and 34 fundamental cycles. Ten of its sixteen
projected crossing pairs are the known disjoint tetrahedral neutron legs; six
others remain unjoined by the candidate convention. There are 27 branching
vertices. Both isotope studies retain those unresolved routing choices.

The gauge-transport control verifies all declared walks; the inverse-consistent
twisted control refutes frame return. This reproduces the distinction between
incidence and transport on the less crowded Ca44 drawing without turning a
chosen flat transport into a physical conclusion.

## Ca46 deterministic reversible routing trial

```sh
node scripts/study-ca46-routing.mjs temp/ca46-routing.json
node --test tests/isotope-wiring-deterministic-routing.test.mjs
```

`core/deterministic-routing.mjs` supplies a declared rotation-system rule. At an
arrival vertex, locate the outgoing reverse of the incoming leg in cyclic port
order. Choose the next port counterclockwise for handedness +1, clockwise for
−1. Screen y is inverted to define that order. Reverse traversal flips
handedness. Coincident port rays are rejected, never broken by arbitrary IDs.
Interior crossings remain unjoined, including the opposite tetrahedral N legs.

This is a candidate based on projected port order, not a derived 3D cyclic order.
State includes the directed edge and handedness. At odd degree, a stateless,
reversal-compatible rule without reflection would require pairing an odd number
of incident legs, which is impossible; Ca46 has 24 odd-degree vertices. The
additional handedness state avoids that obstruction without immediate backtracks.
It is a discrete routing state, **not** a substitute for the SO(3) frame.

All 304 directed-edge/handedness states have one successor and one predecessor;
they form 46 cycles. Reversing each allowed turn yields an allowed reversed turn.
Each of the 20 retained PE departures, with either handedness, returns its full
routing state after eight edges (40 trials). Some revisit the PE vertex earlier:
first vertex returns occur at 3, 4, or 8 edges. A vertex revisit alone therefore
must not be mistaken for full routing-state return, let alone frame return.

Uniqueness is conditional on the initial departure and handedness. It is not
uniqueness from the bare PE vertex and does not establish this rule as canonical.
Finite-state periodicity follows from the permutation. The graph's seven
components are unchanged, and SO(3) frame return remains unverified until a
transport law is supplied. No drawing changes are made by the routing trial.

## Layered neutron-space / wrapper transport trial

```sh
node scripts/study-ca46-layered-transport.mjs temp/ca46-layered-transport.json
node --test tests/isotope-wiring-layered-neutron-transport.test.mjs
```

`core/layered-neutron-transport.mjs` keeps three distinct port-owning layers:
20 PE cycles, ten local neutron spaces, and six wrapper cycles. Each local space
retains its square boundary and opposite tetrahedral neutron legs (four ports,
six supports, no central crossing junction). The two PE occurrences remain
separate local paths sharing access to their cell's neutron space.

The following are **declared trial interfaces**, not inferred consequences of
visual enclosure:

1. Each PE main vertex attaches to its own neutron space's corresponding named
   corner port (20 attachments).
2. Coincident named boundary ports of different spaces in the same shell connect
   explicitly, without merging their identities (20 contacts in Ca46).
3. Each wrapper has two terminals: the upper endpoint shell's axial bottom port
   attaches to wrapper T, and wrapper B attaches to the lower endpoint shell's
   axial top port (12 attachments). Intermediate spanned shells remain recorded
   but receive no implicit attachment.

Span containment is retained as metadata and creates no transport edges.
Projected crossings create no attachment. Wrapper depth and frame transports
are not assigned. The ten local spaces do not add ten particles to the inventory:
the declared accounting stays 20 PE and 26 N, with six excess-N wrappers.

With these new interfaces the candidate graph has **one connected component**;
this is not a correction to the earlier seven-component graph under its different
rules. Removing wrapper-terminal interfaces yields ten components (four shell
complexes and six isolated wrappers); removing PE-to-space interfaces yields
21 components. These controls demonstrate which added interfaces do the connecting.

The retained example is a six-edge transfer from `s1-00-lower` through its space,
wrapper 1's T–R–B route, and shell 2's upper space to `s2-01-upper`. Its reverse
uses exactly the reversed interfaces. Local circulation at both ends plus the
outward and return transfer produces an 18-edge based excursion.

Neither uniqueness nor SO(3) frame return is claimed: a wrapper also offers the
other perimeter route, interfaces are proposed choices, and the transport law
is still absent. This layered representation is not asserted isomorphic to the
previous flattened graph. The drawing itself is unchanged.

### Complete terminal-transfer coverage for the layered trial

```sh
node scripts/study-ca46-layered-transfers.mjs temp/ca46-layered-transfers.json
node --test tests/isotope-wiring-layered-transfer-audit.test.mjs
```

`core/layered-transfer-audit.mjs` checks every source PE against each wrapper
having a terminal in its shell. Each transfer ends at the PE attached to the
opposite terminal; this is not enumeration of all possible PE destination pairs.
Local neutron-space access uses only within-shell space boundaries, tetrahedral
neutron legs, and declared space contacts. Both wrapper perimeter sides are
checked, with forward and exact reverse traces and closed PE excursions.

All 20 PEs reach their three incident terminal wrappers. There are 120 displayed
transfer witnesses (20 × 3 × 2 sides), covering 144 shortest transfer choices.
Twenty-four witnesses have two shortest local-space routes; eight PEs retain
local ambiguity even after the wrapper and perimeter side are specified.
Shortest means graph-step count, not physical distance. A stable lexical order
chooses only the displayed witness; **both alternatives remain counted**.
Longer local paths and tours using multiple wrappers are not enumerated.

The tests independently enumerate bounded local paths to verify counts. Removing
same-shell contacts produces blocked transfers rather than silently excluding
unreachable PEs, and missing inverses fail validation. All 120 representative
transfers reverse exactly and their based excursions close. SO(3) frame return
remains unknown: no transport matrix has been assigned by this audit.

### Neutron-space coherence: alternatives are allowed

```sh
node scripts/study-ca46-neutron-coherence.mjs temp/ca46-neutron-coherence.json
node --test tests/isotope-wiring-neutron-space-coherence.test.mjs
```

`core/neutron-space-coherence.mjs` no longer treats branching in neutron space
as a failure. It retains the alternatives and tests a **proposed path-independent
frame-transport criterion**: for paths p and q sharing endpoints, the loop
p followed by inverse(q) must have identity SO(3) holonomy. With inverse-consistent
edge transports, that is precisely equality of their endpoint frame transports.
It does not require identical paths or a unique outgoing arrow.

The Ca46 neutral subgraph (local spaces, wrappers, and their interfaces, excluding
PE circulation and PE-to-space attachments) has 64 vertices, 116 supports, one
component, and cycle rank 53. A spanning-tree construction supplies 53 independent
fundamental cycles. Additionally, eight distinct shortest local-path pairs and
six wrapper-side pairs are retained as explicit comparisons: 67 audit walks total.
The basis covers longer cycles algebraically under the declared all-composable-turns
assumption. Supplied turn restrictions are rejected rather than silently dropped;
they would require a state-space cycle audit.

All 67 actual comparisons are **unknown** because transport matrices are absent.
Synthetic noncommuting vertex-gauge transport passes all comparisons; an
inverse-consistent support twist fails a local comparison and basis cycles.
These are checker controls, not a derived transport law. Tests also independently
check basis independence and exact shortest-path counts. Enumeration caps fail
explicitly rather than silently omitting alternatives.

This is a strong flatness criterion on the declared graph connection. We have not
inferred filled faces, homotopy relations, or simple connectivity from the drawn
squares. If noncontractible loops are meant to carry physical holonomy, the
criterion must instead specify which path classes require agreement. The `N`
base role in this audit is only a checker annotation, not particle counting.
Neutral coherence alone does not establish return of the full PE circulation.

### Stacked shell-1 / shell-2-top-cell interface

```sh
node scripts/study-ca46-stacked-interface.mjs temp/ca46-stacked-interface.json
node --test tests/isotope-wiring-stacked-cell-interface.test.mjs
```

`core/stacked-cell-interface.mjs` isolates `s1-00` and `s2-01`, retaining both
PE occurrences and the neutron-space K4 of each cell. It tests a single reversible
channel from `space:s1-00:B` to `space:s2-01:T`. The direct version retains the
ports' layer identities and connects them with one support and two inverse arrows;
it does not merge ports or assert a metric distance. The mediated version subdivides
that same channel with a degree-two neutron-interface state. This state is a trial
representation associated with the existing 1+2 wrapper, **not** an extra counted
neutron or a claim that the wrapper's full structure has been reduced to a point.

Both versions have one channel: removing any channel segment disconnects the two
complexes. Internal neutron-space branching is preserved. The direct PE-to-PE
transfer uses three edges; the mediated transfer uses four. Each reverses exactly.
Subdivision adds one vertex and one support, leaving cycle rank unchanged: six
neutral cycles, ten cycles including PE circulation. Thus this path topology alone
does not distinguish the two physical interpretations. The bridge adds no new
cycle-based constraint on its transport; an SO(3) law remains unspecified.

**Isolation is explicit.** Other shell-2 cells and all wrapper-perimeter transport
are excluded and the omitted interfaces are recorded in the report. The original
full-isotope model still has bypass routes between these ports. No global
single-channel claim is made, no full-model attachments are silently rewired,
and no drawing, particle inventory, or 3D coordinate is changed. Extending this
interface to the full model requires deciding how its existing wrappers attach
without providing bypass channels.

### Full Ca46 bottleneck extension (declared attachment policy)

```sh
node scripts/study-ca46-full-stacked-interface.mjs temp/ca46-full-stacked-interface.json
node --test tests/isotope-wiring-stacked-full-interface.test.mjs
```

`core/stacked-full-interface.mjs` extends the isolated interface without deleting
any PE complex, neutron space, or wrapper boundary. This is an explicit alternative
to the earlier wrapper-terminal policy, not an automatic consequence of stacking:

- The 1+2 wrapper loses its upstream terminal and remains a coherence loop with
  one anchor on shell 2's side of the contact.
- The upstream terminals of the 1+2+3 and 1+2+3+4 wrappers move to that same downstream
  contact port. Shell 1 reaches them through the single reversible channel.
- Wrapper identities and coherence spans are retained. Spans no longer directly
  imply transport terminals at their endpoint shells; prior gateways are recorded.

The resulting full graph remains connected, with 20 PE occurrences, ten neutron
spaces, six wrapper cycles, and unchanged 20 PE / 26 N inventory. Only one support
leaves shell 1's complex. Removing any segment of the direct or mediated channel
disconnects shell 1 from the rest, so the bottleneck is checked globally rather
than asserted from a shortest path. A hostile extra upstream connection fails
this check. Internal neutral branching is unaffected.

The direct version has 124 vertices and 196 supports; the mediated version has
125 and 197. Both have cycle rank 73. Eleven wrapper-terminal attachments remain,
plus the new channel. The original model is not mutated. No SVG or metric 3D
geometry is changed. Frame audit of the twenty PE loops and the example excursion
remains unknown without transport matrices.

The earlier two-terminal transfer audit (and the coherence audit depending on it)
is intentionally rejected on the single-anchor wrapper representation rather than
reporting stale coverage. Its 120-transfer/67-walk results belong to the earlier
attachment model. An updated neutral audit is described below; downstream
delegation remains a proposed physical reading.

### Neutral coherence after the global bottleneck change

```sh
node scripts/study-ca46-bottleneck-coherence.mjs temp/ca46-bottleneck-coherence.json
node --test tests/isotope-wiring-bottleneck-neutron-coherence.test.mjs
```

The `actual-interface-ports` mode of `buildNeutronCoherence` reads the current
transport edges, not nominal span endpoints. It checks shortest access from each
PE's local neutron port to every actual same-shell interface port, including the
stacked contact. The single-anchor wrapper still has internal perimeter alternatives;
it is not silently restored as a two-terminal transfer route. The mediated
interface state is included in the neutral graph.

Both full-model variants have 36 local access endpoint pairs checked, eight
ambiguous local pairs, six internal wrapper comparisons, and 53 independent
basis cycles: 67 frame-audit walks. These results are recomputed on the new
attachment graph, despite matching the prior model's cycle counts. Direct
contact has 64 neutral vertices / 116 supports; mediated contact has 65 / 117.
All actual transport results remain unknown.

`core/bottleneck-neutron-coherence.mjs` adds a bridge-specific control: an
inverse-consistent nonidentity rotation on the bridge (noncommuting rotations
on the two mediated segments) preserves cycle coherence. In contrast, twisting
a cyclic support fails it. The channel supports are independently checked as
bridges and are not fundamental-cycle chords.

This distinction matters: a unique reversible channel does **not** determine
its frame rotation. Out-and-back transport cancels, and cycle flatness cannot
fix the relative frame convention across a bridge. The controls do not choose
a physical transport law or distinguish direct contact from a mediator. No
additional uniqueness constraint is imposed inside neutron space.

### Explicit channel-frame parameters and mediator equivalence

```sh
node scripts/study-ca46-channel-transport.mjs temp/ca46-channel-transport.json
node --test tests/isotope-wiring-channel-frame-transport.test.mjs
```

`core/channel-frame-transport.mjs` exposes the missing transport rather than
selecting it from a projected angle. Direct contact has an unspecified R in
SO(3); a mediated contact has entry A and exit B. With column frames its endpoint
transport is **B A**, and its reverse is **A^-1 B^-1**. Direct and mediated contact
agree on externally fixed endpoint frames exactly when R = B A.

A change of intermediate frame H sends A to H A and B to B H^-1, leaving the
endpoint product unchanged. Thus inserting an intermediate state alone supplies
no observable distinction in this transport representation. Individually
reversible direct and mediated channels may still have different endpoint actions;
roundtrip cancellation does not establish their equivalence.

`auditChannelTransport` validates SO(3) data and either explicit reverse-traversal
matrices or inverses declared by construction. `bindChannelTransport` assigns
only the selected channel segments in a cloned topology; it does not silently
fill transports for PE loops or neutral-space paths. Missing parameters remain
unknown. Noncommuting matched, intermediate-gauge, and wrong-order controls test
composition, not a physical rotation law.

The next geometric input is an alignment rule for the **full 3D endpoint frames**
at the contact (or a model-derived connection law). A point contact or an axis
alone does not specify that alignment, and no such data is supplied by this trial.

### What contact geometry fixes the frame?

```sh
node scripts/study-ca46-contact-alignment.mjs temp/ca46-contact-alignment.json
node --test tests/isotope-wiring-contact-frame-alignment.test.mjs
```

`core/contact-frame-alignment.mjs` distinguishes three levels of supplied data:

- Point contact alone selects no SO(3) rotation.
- Two directed transport axes leave SO(2) twist freedom about the target axis.
- An axis and nonparallel transverse reference at **each** endpoint determine
  right-handed frames, hence R = F_target F_source^T.

The frame uses z along the supplied axis, x along the reference projected
perpendicular to z, and y = z cross x. Zero axes, parallel/zero references, and
malformed data are rejected rather than replaced with a default roll direction.
Outward surface normals are not automatically transport axes: callers must
supply a consistent forward-traversal convention.

Conditional controls show that identity and a quarter turn both preserve the
same aligned axes, but correspond to different transverse alignments. These are
not Ca46 frame assignments. Actual contact-frame alignment remains unknown;
no full 3D port axes or transverse references have been derived from the drawing.
An oriented PE leg or neutron-space direction could provide the missing reference
only after its 3D meaning and correspondence across the contact are specified.

### Candidate tetrahedral lift with PE-leg frame markers

```sh
node scripts/study-ca46-tetrahedral-contact.mjs temp/ca46-tetrahedral-contact.json
node --test tests/isotope-wiring-tetrahedral-contact-trial.test.mjs
```

`core/tetrahedral-contact-trial.mjs` tries a concrete **local metric hypothesis**:
T=(0,-1,h), R=(1,0,-h), B=(0,1,h), L=(-1,0,-h). The second cell is translated so
its T meets the first cell's B. At |h|=1/sqrt(2), all six edges have length 2;
regularity was not supplied by the drawing. Each depth sign is independently
selectable without changing the square projection. The cells occupy opposite
y half-spaces and meet at their named vertices.

The forward frame axes are the source center-to-contact and target
contact-to-center directions. The transverse marker follows a selected PE leg
outward from its main vertex. Its named port is recovered from the existing
PE circulation, not chosen by a screen-angle routing rule. An incoming leg
used as a marker is also treated as an outward geometric ray, explicitly
separating the marker convention from circulation direction.

For equal positive depths and outgoing-to-outgoing markers (R-to-R), the
conditional rotation is about x by approximately -70.5288 degrees, with
cos(angle)=1/3. This is a consequence of the regular lift, radial-axis rule,
and correspondence—not a measured or derived physical contact rotation.
Changing the depth signs and target incoming/outgoing marker produces eight
different matrices in this fixed coordinate convention from identical square
projections. They are not claimed to be eight physically inequivalent states.

Each candidate is SO(3) and reverses correctly. The full model remains unmodified;
neutral and PE-loop transports are not filled in. This is not a global 3D packing
of Ca46, and the mediated case is rejected here because no mediator pose has
been supplied. Metric depth, port-axis choice, and marker correspondence remain
explicit physical assumptions to resolve.

### Extending tetrahedral depth choices across the cell assembly

```sh
node scripts/study-ca46-tetrahedral-depths.mjs temp/ca46-tetrahedral-depths.json
node --test tests/isotope-wiring-tetrahedral-depth-constraints.test.mjs
```

`core/tetrahedral-depth-constraints.mjs` checks all 2^10 binary depth-sign choices
for the ten regular-lift cells. It solves center-depth offsets from the twenty
declared same-shell port contacts and the direct shell-1/shell-2 contact. Wrapper
transport edges impose no geometric equalities; their 3D realization is absent.

A fixed-projection control fails: shell 1's B is (0,134), whereas shell 2's top-cell
T is (0,154). The **outer contours**, not these cell vertices, touch in the drawing.
The successful trial explicitly permits translations of the lifted cell clusters,
requiring shell 2 to move by (0,-20) in the projection. The displayed SVG is not
changed. Without that permission the solver rejects the requested direct contact.

Under the regular metric and declared shared-vertex constraints, **16 of 1024**
sign assignments survive. All cells with the same depth sign fail. The four-cell
assemblies of shells 2 and 3 each impose alternating relative signs, with twelve
fixed pairwise sign relations in total. Shell 1's sign relative to shell 2 remains
free; shell assembly therefore does not resolve the contact-frame choice.

The geometric contact graph has three components: shell 1 plus shell 2, shell 3,
and shell 4. Center-depth zero is fixed separately in each component as a reporting
gauge; two relative component depth offsets remain unconstrained. The sixteen
listed discrete assignments are not a count of complete or physically inequivalent
3D configurations. Every retained assignment is independently tested for all
21 vertex equalities and six equal edge lengths per tetrahedron.

This remains a regular-lift incidence trial, not a volume-nonintersection test or
a full 3D packing. It changes no particle inventory, wrapper topology, or transport
law. The mediated case is rejected here because the mediator's extent is unspecified.

### Cell-volume overlap and unintended-contact audit

```sh
node scripts/study-ca46-tetrahedral-packing.mjs temp/ca46-tetrahedral-packing.json
node --test tests/isotope-wiring-tetrahedral-packing-audit.test.mjs
```

`core/tetrahedral-packing-audit.mjs` applies the convex separating-axis test using
both tetrahedra's face normals and all cross-products of their edge directions.
It distinguishes disjoint volumes, boundary contact, and positive-volume overlap
with an explicit absolute distance tolerance. Degenerate tetrahedra are rejected.
It also independently checks the named vertex equalities, rather than accepting
a contact between the wrong ports as sufficient.

All sixteen regular-lift solutions pass at their reported component offsets.
Each has 45 cell pairs: **32 disjoint and 13 declared boundary-contact pairs**,
with no volume overlaps, unexpected contacts, or broken named-port equalities.
Eight contacting pairs share two named vertices and five share one. In particular,
the shell-1/shell-2 contact remains a single shared vertex, while adjacent cells
within a four-cell shell can share an edge. This does not create extra graph
attachments: only the already-declared port incidences are checked.

The result does not select among the sixteen depth choices. It inherits the
explicit shell-2 projection translation and the arbitrary component-depth gauges
of the incidence solver. Wrapper surfaces, global enclosure geometry, and physical
frame transport are still absent. This is a numerical cell-packing check under
those assumptions, not a full physical realization of Ca46.

### Earlier main-editor terminal-map presentation

The Ca46 editor drawing in `index.html` now replaces enclosure diamonds with six
labeled schematic wrapper loops and eleven bidirectional attachment lines. W1
(1+2) is a one-anchor loop; W3 and W6 have their former shell-1 terminals delegated
to shell 2's top port. W2, W4, and W5 retain their declared downstream terminal
pairs. A test compares every displayed wrapper-port/cell-port binding against
`buildStackedFullInterface`, including standalone SVG export, instead of merely
checking contour sizes. No wrapper attaches to a shell-1 cell.

Dots indicate actual neutron-space attachment ports. Lines crossing elsewhere
are unjoined; the footer explicitly distinguishes the transport schematic from
spatial enclosure geometry. All six wrapper identities and coherence spans remain
visible. This presentation applies to the main canvas, pinned references, and
SVG/canvas exports; the default pure-renderer historical projection remains
available to earlier research scripts. Spatial wrapper shapes and frame transport
are still unspecified, not inferred from the new layout.

### Rejected visual trial: shell layers and square witnesses

This visual trial used four horizontal shell layers rather than spatial enclosure
diamonds or the preceding eleven-line terminal map. Adjacent descent/lift links
use the declared B-to-T ports of shell 1 / shell-2-top, shell-2-bottom / shell-3-top,
and shell-3-bottom / shell 4. Each link has both arrow directions. W1, W2, and W4
are square witnesses placed beside those links, not additional paths around them.
The single shell-1 contact is visually separated across layer bands for readability,
not assigned a new metric gap.

W3 (123), W5 (234), and W6 (1234) are shown as witnesses of composed interlayer
transfer in a separate panel with no shortcut arrows. This is a proposed reading
of the longer spans, not an assertion that the earlier delegated-terminal graph
is isomorphic to the three-link chain. Existing transport/coherence audits of that
earlier graph remain historical controls; they do not verify this new interpretation.
The new diagram omits the detailed within-layer incidence network rather than
claiming that the side-by-side cell icons are disconnected.

All ten cells, twenty PE occurrences, and six excess-N witnesses are retained.
Inspection, occupancy labels, references, and exports use the layered drawing.
The pure renderer without `stackedContact: true` retains the historical projection
used by earlier research scripts. Tests check four layers, three reversible links,
all six witness identities, and absence of independent longer-span shortcut arrows.

### Visual rollback

At the operator's request the main Ca46 canvas, references, and exports were
restored to the enclosing-diamond view preceding both terminal-map and layer
redesigns. The shell-1/shell-2 vertex contact is retained. The redesigns are
available only as explicit pure-renderer experiments via `presentation`, not
selected by the UI. This rollback concerns presentation, not validation of the
enclosure contours as transport paths.

## Earlier topology-only audit (retained, not the current PE/frame model)

Run tests:

```sh
node --test tests/isotope-wiring-path-reversal.test.mjs
node scripts/check-isotope-path-reversal.mjs
node scripts/check-isotope-path-reversal.mjs path/to/definition.json
```

The default command audits the current Ca46 fixture. It returns `unknown` and
exit code 2: Ca46 has inventories and a drawing, but no declared NNPE/NNNN path
topology. Exit codes are 0 (verified), 1 (refuted), 2 (unknown).

## Contract

An absolute definition may supply a separate `pathTopology` object:

- `vertices`: `{id, role}` records; role is `N`, `P`, or `E`.
- `edges`: `{id, from, to, kind, support, reverse}` records. Endpoints refer to
  vertex IDs. `support` identifies the retained incidence being traversed, and
  `kind` identifies its role. `reverse` must name an **existing** reverse edge.
- `paths`: `{id, generator, edges}` records. Generator is `NNPE` or `NNNN`;
  `edges` is a nonempty ordered list of edge IDs.
- Optional `turns`: allowed consecutive edge-ID pairs. If supplied, both forward
  and reverse walks must obey them. If absent, all composable turns are allowed.

This is a proposed audit input contract, not a derivation of either generator.
The generator names classify supplied paths; the checker does not interpret the
letters as a native grammar or infer paths from inventory labels. Test chains
are explicitly synthetic examples, not extracted nuclear or Marici assemblies.

## What is checked

For each declared path, the reverse must traverse the same vertices in reverse
order, using existing arrows on the same supports and with the same edge roles.
The reverse declaration must be involutive. Consecutive steps must compose, and
any supplied turn restrictions must admit both traversals. Missing reverse
edges, wrong incidence, changed support, or forbidden reverse turns refute the
claim. Neither endpoint reachability by a different route nor a symmetric
outline substitutes for that reversed path.

The audit does not mutate or complete the graph. Missing topology or absent
coverage of either generator returns `unknown`, not vacuous success. A verified
report concerns only the supplied paths, not every possible path in the graph.
This is intentionally separate from the editor's inventory/legacy-model status.

## Native bridge still required

`research/realization-tower/seed-channel-binding.mjs` already reverses formal
edge words, but explicitly distinguishes free-path comparison from native
reverse execution. `sulfur-nnpe-composition.mjs` supplies a graded star/port
composition experiment, not this isotope renderer's path extraction.

To audit the actual drawing, supply the native NNPE and NNNN path constructors,
their directed incidence and reverse-operation rules, and a map from each
rendered primitive/wrapper to those records. Crossings and coincident SVG points
must not silently become graph vertices. The Ca46 wrapper-span metadata alone
cannot furnish this bridge. No conclusion about physical coherence or preferred
nuclear geometry follows from these software tests.
