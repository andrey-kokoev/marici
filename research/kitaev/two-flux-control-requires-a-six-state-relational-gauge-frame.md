# Two-flux control requires a six-state relational gauge frame

## Bounded question

Can the transposition- and three-cycle-resolved flux ports required for full
finite (D(S_3)) endpoint generation be made gauge invariant, and what is the
smallest shared reference carrier that supports both?

## Source obstruction

For a plaquette holonomy (h) based at a vertex, a gauge transformation

\[
h\longmapsto xhx^{-1}
\]

conjugates the element-flux projector:

\[
B^g\longmapsto B^{xgx^{-1}}.
\]

An individual noncentral (B^g) therefore depends on a gauge frame. The
conjugacy-class sum is gauge invariant, but it erases the element resolution
needed by the 36-dimensional endpoint generator theorem.

The two-port result cannot be promoted to a gauge-invariant physical control
surface without identifying where its based frame is carried.

## Relational reference construction

Introduce a reference register with orthonormal basis

\[
\{|r\rangle:r\in S_3\}.
\]

Let a gauge transformation act jointly by

\[
h\longmapsto xhx^{-1},
\qquad
|r\rangle\longmapsto|xr\rangle.
\]

For a frozen relative group element (q), define

\[
P_q
=
\sum_{r\in S_3}
B^{rqr^{-1}}\otimes|r\rangle\langle r|.
\]

Under the joint gauge action, the summand indexed by (r) is carried to the
summand indexed by (xr). Hence

\[
[P_q,U_x\otimes L_x]=0
\]

for every (xin S_3).

The projector (P_q) measures or phases the holonomy element relative to the
reference orientation. Element resolution survives, but it is now relational
rather than an absolute gauge label.

## Quotient-frame construction

A full six-state frame is not always necessary. Let the reference orientations
form a transitive (S_3)-set

\[
X=S_3/K
\]

for a subgroup (Kleq S_3). A representative (r) of the coset (rK) is
ambiguous under

\[
r\longmapsto rk.
\]

The relative element

\[
r^{-1}hr=q
\]

is well defined on the coset exactly when every (kin K) fixes (q) under
conjugation. Thus the condition is

\[
K\subseteq C_{S_3}(q),
\]

where (C_{S_3}(q)) is the centralizer of (q).

The coarsest transitive reference supporting the (q)-resolved port is
therefore

\[
S_3/C_{S_3}(q).
\]

Its number of orientations is the conjugacy-class size.

## Individual minima

For a transposition (t),

\[
|C_{S_3}(t)|=2.
\]

Therefore the minimal transitive reference has

\[
[S_3:C_{S_3}(t)]=3
\]

states.

For a three-cycle (c),

\[
|C_{S_3}(c)|=3.
\]

Therefore the minimal transitive reference has

\[
[S_3:C_{S_3}(c)]=2
\]

states.

These are orientation registers for one conjugacy class. They do not identify
an arbitrary absolute element of (S_3).

## Shared-reference minimum

One transitive reference (S_3/K) supports both element-resolved ports only if

\[
K
\subseteq
C_{S_3}(t)\cap C_{S_3}(c).
\]

For a transposition and a three-cycle in (S_3),

\[
C_{S_3}(t)\cap C_{S_3}(c)=\{e\}.
\]

Hence

\[
K=\{e\}.
\]

The shared transitive reference must be the regular (S_3)-torsor and has six
states.

Thus:

- one transposition port requires at least three reference orientations;
- one three-cycle port requires at least two;
- both ports on one shared transitive gauge frame require exactly six.

The six-state upper bound is realized by the explicit regular-reference
projectors (P_t) and (P_c).

## Why separate three- and two-state references do not automatically suffice

A three-state transposition frame and a two-state cycle frame have six joint
labels, but their product is not automatically one coherent (S_3)-torsor.
The two quotient frames may carry incompatible gauge histories.

To use them as one endpoint-control frame, the apparatus must provide a
correlation cell identifying their common lift to (S_3). Algebraically, it
must trivialize the residual intersection ambiguity and respect the diagonal
gauge action.

Without that cell, switching between the two ports can introduce an untyped
relative-frame displacement even though each port is separately gauge
invariant.

## Forgetting the reference

If the reference is retained, downstream constructors can condition on the
relational element label while preserving joint gauge invariance.

If the reference is traced out or dephased without retaining its orientation,
the exposed data operation becomes conjugacy averaged. Element-resolved
coherence is lost, and the effective port collapses toward class membership.

Thus the reference is not catalytic in the strong sense unless it is returned
to its exact initial state without carrying information about the endpoint.
Clean uncomputation must be proved for the joint gauge frame, not merely for a
holonomy-computation ancilla.

## Pure reference states and gauge invariance

The uniform reference state

\[
|+\rangle
=
\frac{1}{\sqrt6}
\sum_{r\in S_3}|r\rangle
\]

is invariant under left multiplication. Applying a relational port to this
state can entangle reference orientation with holonomy orientation. The joint
state remains gauge invariant, while the reduced data state need not retain an
absolute element label.

Preparing a sharp state (|e\rangle) selects a gauge frame. That may be a valid
boundary condition or apparatus resource, but it is not a gauge-invariant
vacuum preparation. The source theory must say which interpretation is
intended.

## Relation to the existing nine-gate compiler

The existing holonomy-ancilla circuit computes the based element (h), phases
one ancilla label, and uncomputes. It is exact relative to a frozen base frame.

The relational construction refines its authority boundary:

- with a sharp external frame, it implements the earlier based compiler;
- with a transforming quantum reference, it implements a gauge-invariant joint
  port (P_q);
- after forgetting that reference, it does not retain full element-resolved
  control on the data alone.

The nine-gate count therefore prices holonomy computation but not preparation,
transport, stabilization, or uncomputation of the gauge reference.

## Consequence for endpoint controllability

The two algebraic flux ports are not two untyped scalar knobs. They consume a
shared relational orientation resource.

Under a retained six-state frame and the previously compiled gauge actions, the
same associative and projective Lie-generation theorems apply fibrewise in the
chosen relational frame. If the frame is unavailable or forgotten, only
conjugacy-class controls remain and full endpoint generation fails.

This identifies a physical resource strictly between abstract algebra and
timed pulse synthesis: element-resolved control requires a relational gauge
frame.

The implication is a typing requirement, not a claim that the frame is easy to
build or protect.

## Fault boundary

A reference-frame fault can conjugate both element-flux ports coherently. Such a
fault may preserve all internal algebraic relations while changing which
physical holonomy is called (t) or (c).

Duplicating readout after the shared frame does not detect this common-mode
displacement. Detection requires an independently transported frame reference
or a gauge-invariant relational check crossing the frame-preparation cut.

The frame register is therefore a named common-mode fault domain in any
fault-tolerant endpoint compiler.

## General finite-group theorem

For a finite group (G) and desired relative elements (q_1,\ldots,q_m), a
transitive reference (G/K) supports every element-resolved relational port
when

\[
K\subseteq\bigcap_{j=1}^{m}C_G(q_j).

\]

The smallest transitive reference has size

\[
[G:K_{\max}],
\]

where (K_{\max}) is a largest subgroup contained in the centralizer
intersection.

If the intersection is trivial, the regular (G)-torsor is necessary. This
turns flux-port selection into a reference-capacity theorem for every finite
quantum double.

## DPC: element flux is relational information

The conjecture is:

> Every physical claim of noncentral element-flux control in a gauge model must
> identify the reference carrier relative to which the element is resolved. The
> minimum reference is determined by the intersection of the relevant
> centralizers. Forgetting the reference reduces the accessible operation to a
> gauge-averaged quotient and cannot inherit the full endpoint-control theorem.

This explains why conjugacy classes are native observables while individual
elements require a frame.

## Critics

### Gauge transformations are redundancy, so no reference should be physical

The joint construction remains gauge invariant. The reference carries a
relational orientation, not an observable absolute gauge coordinate. Boundary
conditions and charged reference systems can make such relations operational.

### A base vertex already supplies the frame

A basepoint fixes where holonomy is based, not how its group element transforms.
Gauge conjugation at that vertex remains. An element label requires an internal
frame at the basepoint.

### The full six-state register is obviously sufficient but not minimal

For either port alone it is not minimal. For a shared transitive reference
supporting a transposition and a three-cycle, trivial centralizer intersection
forces all six orientations.

### Two separate quotient references have the same total dimension

Dimension alone does not give a common lift or correlated gauge action. Their
relative frame must be typed and stabilized.

### The relational projector proves physical executability

No. It proves gauge-invariant algebraic typing and the reference minimum.
Hamiltonian locality, pulse synthesis, preparation, noise, and fault tolerance
remain apparatus theorems.

## Exact falsifiers

- A noncentral element-flux port claimed gauge invariant on data alone.
- A transitive transposition reference with fewer than three orientations.
- A transitive three-cycle reference with fewer than two orientations.
- One shared transitive reference for both ports with fewer than six
  orientations.
- A proposed quotient stabilizer not contained in the relevant centralizer.
- A forgotten reference claimed to preserve absolute element resolution.
- Separate quotient frames combined without a common-lift correlation cell.
- A sharp frame state presented as a gauge-invariant vacuum state.

## Machine-readable reference packet

```json
{
  "code": "relational_gauge_frame_minimum",
  "group": "S3",
  "ports": ["transposition", "three_cycle"],
  "transposition_centralizer_order": 2,
  "three_cycle_centralizer_order": 3,
  "centralizer_intersection_order": 1,
  "individual_reference_sizes": [3, 2],
  "shared_transitive_reference_size": 6,
  "joint_projectors_gauge_invariant": true,
  "data_only_element_resolution": false,
  "physical_frame_preparation": "unproved",
  "fault_tolerant_frame_transport": "unproved"
}
```

## Deutschian explanation

An individual flux element is not an absolute property of a non-Abelian gauge
field. It is a relation between the holonomy and a frame at its basepoint.
Conjugacy class survives when the frame is forgotten; element identity does
not.

The two endpoint ports need enough reference capacity to orient both a
transposition and a three-cycle consistently. Their centralizers share no
nontrivial symmetry, so the reference must retain the full six-state (S_3)
torsor.

## Claim boundary

This packet proves gauge invariance of the relational projectors and the
minimal transitive reference sizes from centralizer intersections. It does not
derive a physical reference preparation, a local frame Hamiltonian, timed pulse
words, or fault-tolerant transport.

## Process calibration

Pre-objective ratings were excitement 10/10, confidence 8.5/10, and expected
information gain 10/10. The target was the missing gauge-authority layer beneath
the two element-flux controls.

Post-objective ratings are excitement 10/10, confidence 9.5/10, and realized
information gain 10/10. The algebraic ports now have an exact relational source
type and a six-state shared-frame minimum; physical frame construction remains
the next apparatus problem.
