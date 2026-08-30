# A CNOT tree creates redundant records but also redundant faults

Owner: `marici.Kitaev`

## Question

What is the smallest exact dynamical model that creates many readable copies
of a classical pointer label, and what does it reveal about fault independence
and lost quantum information?

A layered CNOT tree copies one orthogonal source bit into `N` record qubits at
optimal unconstrained two-body depth

\[
\left\lceil\log_2(N+1)\right\rceil.
\]

For a coherent source input it creates a GHZ state rather than clones of the
unknown qubit. Every leaf carries a perfect record of the pointer-basis label,
while the conjugate phase survives only as a global correlation.

The same tree that spreads the record also spreads early faults. A single
`X` fault on an informed ancestor can flip its entire descendant subtree, and
a phase fault can remain invisible to every pointer-basis record. Readable
redundancy is therefore not fault-independent redundancy.

## Claim boundary

The optimal depth theorem uses arbitrary pair connectivity, layers of disjoint
two-qubit gates, clean record qubits, and ideal CNOT operations. Geometric
locality replaces the logarithmic bound by the stronger graph-distance and
volume constraints of the many-body light-cone packet.

The construction is a finite circuit model of record formation. It does not
derive CNOT, clean ancillas, stable pointer readout, or fault-tolerant cat-state
preparation from the microscopic `D(S3)` Hamiltonian.

## Fanout circuit

Let qubit zero carry the source pointer basis

\[
\{|0\rangle,|1\rangle\}.
\]

Prepare `N` record qubits in

\[
|0\rangle^{\otimes N}.
\]

Whenever a qubit already carries the source bit, use it as the control of a
CNOT into one clean record target. Repeating this in parallel layers produces
a binary fanout tree.

For a classical pointer value `b`, every used CNOT acts as

\[
|b\rangle|0\rangle
\longmapsto
|b\rangle|b\rangle.
\]

After the tree reaches all records,

\[
|b\rangle|0\rangle^{\otimes N}
\longmapsto
|b\rangle^{\otimes(N+1)}.
\]

Every record qubit is then individually sufficient to distinguish the two
pointer labels perfectly.

## Optimal depth theorem

Call a wire informed after its reduced computational-basis value can depend on
the source bit. Initially exactly one wire is informed.

In one layer of disjoint two-qubit gates, each informed wire can interact with
at most one uninformed wire. Therefore the number of informed wires can at
most double per layer. After depth `d`,

\[
N_{\rm informed}(d)\leq2^d.
\]

To inform the source plus `N` records, one must have

\[
2^d\geq N+1.
\]

Hence

\[
d\geq\left\lceil\log_2(N+1)\right\rceil.
\]

A balanced binary CNOT schedule attains this bound: every informed wire copies
to one fresh target in each layer until all targets are reached.

Thus the logarithmic depth is exact in the arbitrary-connectivity,
disjoint-gate model.

## Geometric locality correction

On a nearest-neighbor interaction graph, an informed bit can travel at most
one edge per circuit layer. Every record reached by depth `d` must lie in the
graph ball

\[
B_d(S).
\]

Therefore

\[
N+1\leq|B_d(S)|.
\]

On a fixed-dimensional lattice this volume grows polynomially rather than
exponentially in `d`. A balanced abstract binary tree cannot be embedded as a
constant-density nearest-neighbor circuit without paying routing, congestion,
or spatial-growth cost.

The abstract logarithmic theorem and the many-body light-cone theorem are
compatible. They apply to different Carrier geometries.

## Coherent source input

For an arbitrary source state

\[
|\psi\rangle
=
\alpha|0\rangle+\beta|1\rangle,
\]

linearity gives

\[
|\psi\rangle|0\rangle^{\otimes N}
\longmapsto
\alpha|0\rangle^{\otimes(N+1)}
+
\beta|1\rangle^{\otimes(N+1)}.
\]

This is a GHZ state. It is not

\[
|\psi\rangle^{\otimes(N+1)}.
\]

The circuit copies the commuting pointer label, not the unknown quantum
state. Hence there is no violation of no-cloning.

Each proper single-qubit reduction is diagonal in the pointer basis:

\[
|\alpha|^2|0\rangle\langle0|
+
|\beta|^2|1\rangle\langle1|.
\]

The relative phase between `alpha` and `beta` is stored only in a global
many-body correlation.

## Stabilizer anatomy

For equal amplitudes, the ideal record state is stabilized by

\[
Z_0Z_j
\]

for every record qubit `j`, together with the global operator

\[
X_0X_1\cdots X_N.
\]

The pairwise `Z` stabilizers certify agreement of all classical record bits.
They do not determine the eigenvalue of the global `X` operator.

Thus classical record agreement leaves one conjugate global phase coordinate.
More pointer-basis copies add more `Z` agreement checks but do not convert the
global phase into a local record.

## Exact Pauli propagation

For a CNOT with control `c` and target `t`, conjugation gives

\[
X_c\longmapsto X_cX_t,
\qquad
Z_c\longmapsto Z_c,
\]

\[
X_t\longmapsto X_t,
\qquad
Z_t\longmapsto Z_cZ_t.
\]

An `X` fault on an informed control before it fans out therefore propagates to
the newly written target. If that target later controls descendants, the same
fault continues down the subtree.

An early `X` fault at a tree vertex can consequently flip every final record
in its descendant set. At the root, one fault can flip the source and all
record copies together.

Conversely, a late leaf `X` fault changes only one record. Fault weight is
determined by causal location in the fanout tree, not merely by the number of
fault events.

## Invisible phase fault

A `Z` fault on any one qubit of the completed GHZ state changes the relative
sign between the two branches. It leaves every pointer-basis record
probability and every pairwise `Z` agreement check unchanged.

Therefore unanimous classical records do not certify the coherent phase of
the source. Detecting that fault requires a global `X`-type parity probe or a
different protected encoding.

This is the record-theoretic form of local syndrome blindness to a logical
operator.

## Majority does not repair the tree source

If at most one independently selected final leaf bit can flip, three or more
records and majority decoding correct that model.

The fanout tree does not naturally satisfy it. One early ancestor fault can
flip a large subtree, and a root fault can flip every leaf. Treating the final
records as independent repetitions therefore mis-types the physical fault
model.

A fault-tolerant record constructor needs at least one of the following:

- verified cat-state preparation with repeated parity checks;
- bounded-spread gadgets preventing one fault from reaching many leaves;
- several independently seeded fanout trees compared against a trusted source
  anchor;
- temporal repetition with a source-stability theorem;
- a code whose check geometry matches the actual subtree fault hypergraph.

Even these mechanisms cannot diagnose a common source relabeling without an
independent semantic reference.

## Coherent uncomputation

The ideal CNOT tree is unitary. Before any record is irreversibly measured or
leaked, applying the gates in reverse order returns

\[
\alpha|0\rangle^{\otimes(N+1)}
+
\beta|1\rangle^{\otimes(N+1)}
\]

to

\[
(\alpha|0\rangle+\beta|1\rangle)
\otimes|0\rangle^{\otimes N}.
\]

This restores the source coherence and erases every record.

If one orthogonal record has escaped into an uncontrolled environment, inverse
gates on the retained qubits cannot restore the reduced source coherence. The
which-branch information still exists outside the controlled Carrier.

Thus reversible premeasurement and stable objective recording are different
stages. Objectivity requires record persistence beyond the coherent
uncomputation boundary.

## Branch records and actuality

The GHZ state supplies correlated pointer effects. It does not by itself
select one record value as uniquely actual. Reading a fragment requires a
specified instrument, and claims about stable classical actuality require the
environmental record and irreversibility programme.

The circuit proves that orthogonal possible record values can be redundantly
encoded. It does not settle collapse, branching interpretation, or
observer-independent selection.

## Multi-sector generalization

For `r` orthogonal pointer labels, replace CNOT by controlled modular addition:

\[
|a\rangle|0\rangle
\longmapsto
|a\rangle|a\rangle.
\]

A fanout tree produces

\[
\sum_a\alpha_a|a\rangle^{\otimes(N+1)}.
\]

It copies the commutative label algebra and stores inter-label coherence only
in global correlations.

For the eight central `D(S3)` sectors, this gives an abstract finite record
constructor. It preserves unknown states inside each sector block because the
control depends only on the central label. It dephases coherent superpositions
between different labels once any record is discarded or irreversibly read.

The missing physical arrow remains substantial: derive the controlled sector
addition or equivalent pointer interaction from local Hamiltonians, anyon
transport, boundaries, or measurement gadgets, with declared propagation and
fault bounds.

## Minimal physical audit

A candidate topological record constructor should report:

1. the commuting source projectors being copied;
2. the microscopic two-body or local interaction implementing one copy step;
3. the geometric fanout graph and schedule;
4. the exact conditional pointer states;
5. the causal fault hypergraph of every gate location;
6. the checks used to verify record agreement;
7. the conjugate information not contained in those checks;
8. the location at which records become irreversibly unavailable for
   uncomputation;
9. the independent anchor for common source relabeling;
10. the resource scaling with record count and code size.

An abstract copy isometry alone answers only the first algebraic question.

## Hostile fixtures

### Unknown-state cloning claim

Apply the fanout tree to a superposition and call every reduced record qubit a
copy of the original pure state. Each reduction is diagonal and generally
mixed.

### Independent-leaf majority

Use a balanced tree, insert one `X` fault near the root, and treat the resulting
many flipped leaves as independent single-leaf faults.

### Perfect record agreement with wrong phase

Apply one `Z` fault to the GHZ state. Every computational-basis record agrees,
while the global coherent phase changes.

### Uncomputation after leakage

Copy one pointer label into an uncontrolled environment, reverse every
retained CNOT, and claim the source coherence is restored.

### Logarithmic depth on a local lattice

Use the arbitrary-connectivity doubling schedule while omitting routing and
light-cone constraints.

### Redundant encoding called selected record

Create a GHZ state and infer a unique actual value without a recording
instrument or interpretive postulate.

### Abstract sector copier called microscopic control

Write the eight-label controlled-addition unitary and treat it as generated by
the frozen `D(S3)` Hamiltonian without a local constructor.

## Falsifiers

- More than `2^d` wires depend on one source after depth `d` of disjoint
  two-body gates in the frozen circuit model.
- The balanced arbitrary-connectivity fanout tree fails to attain the stated
  depth.
- A proper single-qubit GHZ reduction retains the unknown source phase.
- A source-control `X` fault fails to propagate according to the CNOT
  conjugation rules.
- Pointer-basis agreement checks detect a pure global phase flip.
- Reversing only retained gates restores coherence after an orthogonal record
  has escaped.
- Readable tree leaves are promoted to independent fault domains.
- The no-cloning theorem is applied to prohibit copying orthogonal classical
  labels, or the classical copier is promoted to unknown-state cloning.

## Shared Carrier geometry and coefficient lens

Shared Carrier geometry supplies the branching tree, circuit depth, causal
descendant sets, fragment cuts, and distinction between retained and escaped
records.

The quantum coefficient lens supplies CNOT conjugation, GHZ coherence,
stabilizers, partial trace, and the no-cloning boundary. The same tree could
carry classical bits or other coefficient objects, but its fault propagation
and lost conjugate information depend on the lens.

## Disposition

The CNOT tree is the smallest constructive model joining dynamical record
formation to causal and fault structure. It achieves optimal logarithmic
fanout depth without geometric locality, creates perfectly readable copies of
one commuting pointer bit, and stores the conjugate quantum phase only in a
global correlation.

Its main hostile lesson is that record redundancy and fault independence move
in opposite directions under naive fanout. The tree amplifies both the desired
label and early faults. A physical objective-record theorem therefore needs a
verified fanout constructor, not merely many agreeing leaves.

No checker, build, or Git operation was run for this research-only packet.
