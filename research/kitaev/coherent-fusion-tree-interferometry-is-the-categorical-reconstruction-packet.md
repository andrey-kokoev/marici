# Coherent fusion-tree interferometry is the categorical reconstruction packet

Owner: `marici.Kitaev`

## Bounded question

Which finite operational contexts upgrade fusion rules and modular scalar data
to reconstruction of coherent associators and channel-wise braiding, and what
equivalence remains after that reconstruction?

For the multiplicity-free `D(S3)` fusion ring, the answer is a family of
phase-sensitive fusion-tree and braid interferometers, together with explicit
unit, duality, pentagon, and hexagon contexts. Fusion probabilities and closed
link invariants alone are insufficient.

## Fusion rules define spaces, not their identifications

Let simple sectors be (a,b,c,\ldots) and let

\[
N_{ab}^c\in\{0,1\}
\]

be the `D(S3)` fusion multiplicities. A nonzero coefficient says that the
trivalent space

\[
V_{ab}^c=\operatorname{Hom}(a\otimes b,c)
\]

is one-dimensional. It does not choose a normalized vector in that line or a
phase convention for its preparation port.

For fixed (a,b,c,d), define the left and right intermediate-label sets

\[
E_{abc}^d
=
\{e:N_{ab}^eN_{ec}^d=1\},
\]

\[
F_{abc}^d
=
\{f:N_{bc}^fN_{af}^d=1\}.
\]

Associativity of the fusion ring guarantees equal cardinalities. The two
fusion-tree spaces are

\[
\bigoplus_{e\in E_{abc}^d}
V_{ab}^e\otimes V_{ec}^d
\]

and

\[
\bigoplus_{f\in F_{abc}^d}
V_{bc}^f\otimes V_{af}^d.
\]

An associator is a unitary map between them. In selected trivalent frames its
matrix is

\[
F_d^{abc}=(F_d^{abc}[e,f]).
\]

Multiplicity-free fusion makes the matrix indices discrete. It does not make
the matrix diagonal, real, or determined by the allowed-channel sets.

## Why fusion probabilities are insufficient

Prepare the left tree with intermediate label (e), reassociate, and measure the
right intermediate label (f). The transition probability is

\[
p(f|e)=|F_d^{abc}[e,f]|^2.
\]

These probabilities reconstruct only entry moduli. They do not reconstruct:

- phases between entries in one row or column;
- interference between different intermediate channels;
- the action on a coherent superposition of fusion trees;
- the pentagon phase accumulated by alternate reassociation routes.

Two unitary matrices can have the same entrywise moduli without being equal in
the chosen port frames. Even when a difference is a categorical basis gauge,
the operational packet must state that gauge rather than treating the matrices
as numerically identical.

## Complex associator interferometer

For every admissible quadruple ((a,b,c;d)), every (e\in E_{abc}^d), and every
(f\in F_{abc}^d), prepare a coherent control qubit selecting two routes:

1. a calibrated reference route from the source unit to the (f)-tree output;
2. the (e)-tree preparation followed by the physical reassociation route.

Interference in two complementary control bases gives the real and imaginary
parts of

\[
F_d^{abc}[e,f]
\]

relative to the declared trivalent-port frames.

Equivalently, use a Hadamard-test interface for the reassociation isometry with
preparation (|e\rangle) and effect (\langle f|). The apparatus must retain the
path-control coherence. A classical randomized choice of routes recovers only
probabilities and cannot supply the phase.

Complete complex matrix elements for all (e,f) reconstruct the associator map
on that channel space. Unitarity supplies an internal consistency test, not a
replacement for phase-sensitive measurements.

## Channel-wise braid interferometer

For every ordered pair ((a,b)) and every channel (c) with (N_{ab}^c=1), the
braiding restricts to a scalar map

\[
R_c^{ab}:V_{ab}^c\longrightarrow V_{ba}^c.
\]

Its complex phase is observable only relative to another coherent path. Use a
control system to superpose:

- fusion through (c) with no exchange;
- one oriented exchange of (a) and (b), followed by the same calibrated fusion
  effect.

Complementary control readouts reconstruct the complex value of (R_c^{ab}) in
the selected vertex frames.

The reverse ordered exchange (R_c^{ba}) requires its own oriented context. A
double braid measures only the product

\[
R_c^{ba}R_c^{ab}.
\]

That monodromy product is related to twists by the balancing law. It does not
by itself reconstruct the two oriented braid maps.

## The square-root hostile ambiguity

For identical incoming sectors, monodromy can determine

\[
(R_c^{aa})^2
\]

while leaving two square-root candidates for (R_c^{aa}). Pentagon and hexagon
constraints may reject one candidate, but the double-braid scalar alone does
not.

A single-exchange interferometer is the direct finite falsifier. This is the
braid analogue of retaining an oriented loop rather than only its unoriented
closed trace.

## Trivalent gauge

Choose a normalized basis vector in every nonzero (V_{ab}^c). In the
multiplicity-free case, another choice is

\[
v_{ab}^c
\longmapsto
u_{ab}^c v_{ab}^c,
\qquad
u_{ab}^c\in U(1).
\]

These phases transform the numerical (F) and (R) symbols while leaving every
closed, consistently assembled physical process unchanged. Schematically,

\[
(F_d^{abc})'_{ef}
=
\frac{u_{bc}^f u_{af}^d}
{u_{ab}^e u_{ec}^d}
F_d^{abc}[e,f],
\]

and

\[
(R_c^{ab})'
=
\frac{u_{ba}^c}{u_{ab}^c}R_c^{ab}.
\]

Therefore complete categorical reconstruction is naturally unique up to this
vertex-basis gauge. If the physical apparatus declares calibrated open
trivalent ports, those port phases become implementation coordinates and the
equivalence becomes finer.

Closed scalar diagrams cannot fix an open-port gauge because every internal
vertex phase cancels against its adjoint occurrence.

## Tensor unit and duality packet

Identify the tensor unit (A) operationally through preparation and fusion tests

\[
A\otimes a\simeq a,
\qquad
a\otimes A\simeq a.
\]

For every (a), identify the dual (\bar a) and calibrated evaluation and
coevaluation ports

\[
a\otimes\bar a\longrightarrow A,
\qquad
A\longrightarrow\bar a\otimes a.
\]

Snake identities test that the cup and cap are mutually coherent. Pivotal or
ribbon trace contexts then reconstruct quantum dimensions and twists in the
same source frame.

The tensor unit fixes unit constraints and gives a canonical positive
normalization for vacuum amplitudes. It does not fix every internal trivalent
phase (u_{ab}^c). A source unit is a reference object, not a complete higher
fusion-frame calibration.

## Pentagon as an operational path equality

For every admissible five-object fusion packet, compose the reconstructed
associators along the two routes around the pentagon. The resulting maps
between the same initial and final fusion-tree spaces must agree.

This is stronger than checking scalar probabilities after each route. The
comparison must retain coherent channel amplitudes or be tomographically
complete on the final channel space.

Pentagon failure means the fitted local reassociation matrices do not compose
into a monoidal category, even if every individual matrix is unitary.

## Hexagon as an operational braid--associator equality

For every admissible triple and total charge, compare the two coherent routes
that move one object around a fused pair using associators and elementary
braids. Equality of the channel maps is the hexagon law.

The hexagon tests the relative phases that closed monodromy and separate
transition probabilities can miss. It also fixes which braid orientation is
being represented.

Pentagon and hexagon are constructor composition laws. They do not follow from
having numerically plausible (F) and (R) tables.

## Finite sufficient reconstruction packet

For a finite multiplicity-free unitary fusion theory, the following data are
sufficient to reconstruct a braided fusion category in selected open-port
frames:

1. simple-sector labels, duals, and fusion coefficients;
2. a normalized trivalent preparation/effect pair for every nonzero fusion
   channel;
3. all complex associator matrix elements for every admissible quadruple;
4. every oriented channel-wise braid amplitude;
5. unit, cup, cap, pivotal trace, and twist contexts;
6. tomographically complete pentagon and hexagon route comparisons.

If open vertex frames are not physically fixed, the reconstructed object is
unique only up to the unitary trivalent gauge. In higher multiplicity, each
(U(1)) phase is replaced by a unitary basis change in (V_{ab}^c).

This packet is sufficient in data type. It is not claimed count-minimal after
using symmetries, dualities, or generating objects to compress the number of
experiments.

## Minimality by missing-context witnesses

Each context type has an independent hostile omission.

### Remove fusion outcomes

The dimensions and even existence of channel spaces become unknown.

### Remove complex route interference

Only (|F_{ef}|^2) remains; associator phases are invisible.

### Remove single oriented braids

Monodromy products and twists remain, but individual (R_c^{ab}) maps are not
reconstructed.

### Remove unit and cup/cap contexts

Vacuum normalization, duality, and pivotal trace are not tied to the same
source frame.

### Remove pentagon

Individually unitary reassociation matrices need not compose coherently.

### Remove hexagon

Fusion and braid tables need not define one braided monoidal structure.

### Remove ancillary channel tomography

Transpose or conjugate process candidates can survive probability-only tests.

Thus the packet is minimal by constructor type, though not necessarily by the
number of individual settings.

## `D(S3)` application

The current `D(S3)` fusion ring supplies item one except for a fully
operationally calibrated duality-port packet. Exact modular data supply closed
trace combinations of items four and five and independently recover the
fusion coefficients.

The present programme has not yet supplied one unified executable family of:

- coherent fusion-tree preparations;
- complex associator interferometers;
- single-exchange channel interferometers;
- open trivalent phase frames;
- tomographically complete pentagon and hexagon instruments.

Therefore it has not operationally reconstructed the full braided fusion
category from experiments, even though the frozen quantum-double source
algebra mathematically determines such a category.

This distinction protects source authority: one may calculate (F,R) data from
the Hopf algebra without claiming that the current apparatus has tomographically
reconstructed or executed those maps.

## Categorical reconstruction versus topological phase

Even a complete braided fusion category packet does not automatically
reconstruct:

- gapped boundaries and module categories;
- defect fusion and crossed braiding;
- microscopic locality and energy scales;
- an invertible stacked phase or chiral response;
- a finite-depth or quasi-adiabatic equivalence;
- executable ribbon constructors and their fault tolerance.

These require additional boundary, defect, gravitational, local-net, and
compiler contexts. Categorical equivalence is one reconstruction level, not a
synonym for complete physical phase identity.

## DPC: coherent route comparison reconstructs composition law

The conjecture is:

> Topological scalar invariants become a categorical explanation only after
> the experiment family compares coherent fusion and braid routes, preserves
> their open channel frames, and verifies pentagon and hexagon as operational
> path equalities. Closed link values are shadows of that constructor system;
> they are not its realization.

The explanation identifies why phase-sensitive contexts are required: an
associator is the law relating two compositions, and a braid is an oriented
map between channel spaces. Neither object is determined by the probability
of one terminal label alone.

## Critics

### `D(S3)` fusion is multiplicity-free, so there are no basis choices

Each trivalent space is one-dimensional but still has a phase. Moreover,
several intermediate labels can contribute to one four-object fusion space,
making the (F)-move a nontrivial matrix.

### Unitarity reconstructs missing phases from moduli

Not generally. Orthogonality constrains phases but need not fix them uniquely,
and categorical vertex gauges remain even when a numerical completion is
unique.

### Modular data already contain braiding

They contain closed-link traces and twists. They do not expose every
channel-wise oriented braid map or its coherent action on open fusion spaces.

### Gauge-dependent (F,R) symbols are not observable

Their individual numbers depend on open-port frames. Complete physical route
amplitudes are gauge invariant. Reconstruction should therefore report the
category up to vertex gauge unless those open ports are externally calibrated.

### Pentagon and hexagon can be checked algebraically from source formulas

Yes, as a source-derived mathematical theorem. Operational reconstruction
requires the corresponding maps to be exposed or compiled by the apparatus.

## Exact falsifiers

- A fusion-probability packet uniquely determining complex associator matrices
  without an additional phase or gauge theorem.
- Double-braid monodromy alone uniquely determining both oriented elementary
  braid maps.
- A tensor-unit normalization eliminating every nontrivial trivalent vertex
  gauge.
- Individually unitary (F) matrices claimed to define a monoidal category
  without pentagon.
- Fusion and braid tables claimed compatible without hexagon.
- Closed modular scalars promoted to open-channel instrument tomography.
- A complete braided-category packet promoted directly to boundary, defect,
  gapped-phase, or executable-ribbon equivalence.
- A phase-sensitive interferometer whose reference path is not source
  calibrated or coherently retained.

## Machine-readable reconstruction packet

```json
{
  "code": "coherent_fusion_tree_categorical_reconstruction",
  "fusion_multiplicity": "zero_or_one_for_D_S3",
  "fusion_rules_reconstruct_channel_support": true,
  "fusion_probabilities_reconstruct_F_phases": false,
  "complex_associator_interferometry_required": true,
  "single_oriented_braid_interferometry_required": true,
  "monodromy_reconstructs_individual_R": false,
  "tensor_unit_fixes_all_vertex_gauge": false,
  "pentagon_route_tomography_required": true,
  "hexagon_route_tomography_required": true,
  "categorical_equivalence_gauge": "unitary_trivalent_basis_change",
  "boundary_and_defect_reconstruction_included": false,
  "stable_phase_equivalence_included": false,
  "executable_ribbon_compiler_included": false
}
```

## Claim boundary

This packet derives the finite tester types needed for categorical
reconstruction and their gauge. It does not enumerate a setting-minimal
`D(S3)` experiment list, compute new (F,R) symbols, construct the required
interferometers, or claim uniqueness of a general topological phase from a
braided fusion category.

Its structural conclusion is that coherent route comparison, not more closed
scalar invariants, is the missing bridge from fusion/modular data to the
composition law of the anyon theory.
