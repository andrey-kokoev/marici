# Coherence-probe redundancy is edge connectivity, not probe count

Owner: `marici.Kitaev`

## Question

How much redundancy makes the pairwise qutrit coherence probes tolerant to a
faulty probe edge?

Pairwise coherent tests measure differences of hidden vertex phases. Their
fault structure is therefore a graph synchronization code. Cycle sums are the
syndrome, and edge connectivity is the exact distance parameter.

For a probe multigraph with edge connectivity `lambda`:

- every set of at most `f` known edge erasures is tolerated exactly when
  `lambda` is greater than `f`;
- every nonzero error on at most `t` edges is detected when `lambda` is greater
  than `t`;
- every error on at most `t` edges is uniquely correctable when `lambda` is
  greater than `2t`.

For three qutrit phase vertices, a triangle detects one arbitrary bad edge but
cannot correct it. Five independently routed pairwise probe instances are the
minimum multigraph resource for correcting one arbitrary edge fault.

## Claim boundary

The theorem concerns exact additive phase-difference readouts with sparse edge
faults. It does not include basis-ray preparation faults, output tomography
faults, leakage, finite sampling, phase wrapping ambiguity, or a fault that
simultaneously corrupts several nominally repeated edges.

Parallel graph edges count as independent coordinates only after their source,
transport, phase reference, and readout fault domains have been proved
independent enough for the declared sparse-edge model.

## Phase synchronization model

Let the trusted logical basis vertices be

\[
V=\{1,\ldots,n\}.
\]

After the basis-ray tests, a promised residual unitary has the form

\[
E
=
\operatorname{diag}
(e^{i\theta_1},\ldots,e^{i\theta_n}).
\]

Global phase shifts all vertex labels equally and is quotiented.

Orient a multigraph

\[
\Gamma=(V,\mathcal E)
\]

of pairwise coherent probes. Let `B` be its oriented incidence matrix. In an
exact lifted phase convention, the edge readout is

\[
y=B^*\theta+e,
\]

where `e` is the edge-fault vector. The same equations may be read modulo
`2pi` when a branch convention has been frozen.

An edge from `j` to `k` ideally reports

\[
y_{jk}=\theta_k-\theta_j.
\]

The graph is not merely an index for repeated experiments. It is the boundary
operator relating semantic vertex phases to measured relative phases.

## Cycle syndrome

Let `z` be an oriented cycle vector. Then

\[
Bz=0.
\]

Consequently,

\[
z^*y
=
z^*e.
\]

Every ideal phase gradient has zero circulation around every cycle. The cycle
space therefore supplies the parity-check or syndrome map for edge faults.

Write the cycle-syndrome map as `S_cyc`. Its kernel is the cut or gradient
space:

\[
\ker S_{\mathrm{cyc}}
=
\operatorname{im}B^*.
\]

An edge-error pattern in that kernel is indistinguishable from changing the
vertex phases. This is the exact common-mode boundary of internal coherence
checks.

## Edge connectivity

Let

\[
\lambda(\Gamma)
\]

be the minimum number of edges whose deletion disconnects the multigraph.
Equivalently, it is the minimum size of a nontrivial edge cut.

If a vertex label difference `delta theta` is not globally constant, then its
gradient

\[
B^*\delta\theta
\]

has support on at least one nontrivial cut. Therefore

\[
\left|
\operatorname{supp}(B^*\delta\theta)
\right|
\geq
\lambda(\Gamma).
\]

Conversely, shifting all phases on one side of a minimum cut produces a
nonconstant vertex assignment whose gradient is supported exactly on that
cut.

Thus `lambda` is the exact minimum support of an internally invisible
nonconstant phase-gradient pattern.

## Known-erasure theorem

Suppose a set `F` of failed probe edges is known and removed. The remaining
edge data determine all vertex phases modulo global phase exactly when

\[
\Gamma\setminus F
\]

is connected.

Every erasure set of size at most `f` is tolerated if and only if

\[
\lambda(\Gamma)>f.
\]

This is connectivity after deletion, not majority voting.

## Sparse-error detection theorem

Let `e` be a nonzero error supported on at most `t` edges. If its cycle syndrome
vanished, then it would be a nonconstant phase gradient or a zero global
gradient. A nonzero gradient has support at least `lambda`.

Therefore every such error is detected when

\[
\lambda(\Gamma)>t.
\]

The bound is exact. A minimum-cut phase shift produces an invisible error of
weight `lambda`.

Detection reports inconsistency. It does not identify which edge is wrong or
which vertex phases are correct.

## Sparse-error correction theorem

Suppose one observed edge vector has two candidate decompositions

\[
y=B^*\theta+e
\]

and

\[
y=B^*\theta'+e',
\]

with

\[
|\operatorname{supp}e|
\leq t,
\qquad
|\operatorname{supp}e'|
\leq t.
\]

Then

\[
B^*(\theta-\theta')
=
e'-e
\]

has support at most `2t`. If

\[
\lambda(\Gamma)>2t,
\]

the phase difference must be globally constant and the two logical solutions
agree modulo global phase.

Conversely, if a minimum cut has size at most `2t`, partition its edges into
two sets of size at most `t`. A phase shift on one side of the cut can then be
traded between the two sparse error vectors, producing two inequivalent
logical phase assignments for the same data.

Hence unique correction of every `t`-edge error is possible exactly when

\[
\lambda(\Gamma)>2t.
\]

## Qutrit tree

The ideal pairwise qutrit tester used the two edges

\[
(1,2),
\qquad
(2,3).
\]

This graph is a tree with

\[
\lambda=1.
\]

It is jointly faithful when fault free, but it has no cycle syndrome. One bad
edge is indistinguishable from a valid change of vertex phases.

Thus minimal ideal faithfulness and single-fault detection require different
probe graphs.

## Qutrit triangle

Add the third edge

\[
(1,3).
\]

The triangle has

\[
\lambda=2.
\]

Its oriented cycle residual is

\[
s
=
y_{12}+y_{23}-y_{13}.
\]

One arbitrary edge fault gives a nonzero syndrome and is detected. But one
syndrome equation cannot determine which of the three edges is faulty when
its value is unrestricted. The triangle does not correct one arbitrary edge
fault because

\[
2\not>2.
\]

It does tolerate one known edge erasure because deleting any one edge leaves a
connected tree.

## Minimum one-error-correcting qutrit multigraph

Correction of one arbitrary edge error requires

\[
\lambda\geq3.
\]

A three-vertex multigraph with edge connectivity three has minimum degree at
least three. The degree sum is therefore at least nine, so the edge count is at
least

\[
\left\lceil\frac92\right\rceil=5.
\]

This bound is attained by probe multiplicities

\[
m_{12}=2,
\qquad
m_{23}=2,
\qquad
m_{13}=1.
\]

The vertex degrees are `3,4,3`, and every nontrivial cut contains at least
three edges. Hence

\[
\lambda=3>2.
\]

Five independently faulted pairwise coherence-probe instances are therefore
necessary and sufficient in this multigraph model to correct one arbitrary
edge error and reconstruct the three logical phases modulo global phase.

This count excludes the three basis-ray probes and every tomography setting.

## Common-mode vertex fault

Let a preparation-frame fault change the vertex phases by `eta`. Every incident
edge readout changes coherently as

\[
e=B^*\eta.
\]

Its cycle syndrome is identically zero. The internal decoder interprets the
data as the valid phase assignment

\[
\theta+\eta.
\]

Adding more edges does not distinguish this common vertex-frame displacement
from a true logical phase. An independently prepared vertex anchor or
source-fixed absolute comparison is required.

This is not a contradiction with the sparse-edge correction theorem. A single
vertex fault generally corrupts every incident edge and lies outside the
one-independent-edge-fault model.

## Gate fault versus tester fault

The vertex phases `theta` describe the realized logical gate. The edge vector
`e` describes tester corruption. A valid decoder reconstructs `theta` in the
presence of sparse `e`; it must not erase a genuine logical gate fault by
relabeling it as tester noise.

Only a source-derived command frame determines which reconstructed `theta` is
correct. Internal graph consistency establishes existence of a phase
assignment, not agreement with the commanded gate.

## Causal independence requirement

Parallel graph edges improve the code distance only when their fault events
are separately supported. Examples that invalidate nominal multiplicity
include:

- all repeated probes prepared by one drifting phase source;
- one fanout controller setting every pairwise phase;
- one tomography calibration shared across every edge;
- one route segment physically reused by nominally different probes;
- one postprocessing sign convention copied to all cycle equations.

The effective fault hypergraph, not the printed multigraph, determines the
real code distance. A source fault touching `r` probe edges must be counted as
an `r`-edge event unless an inner verification gadget reduces its spread.

## Beyond exact phases

With finite sampling and continuous noise, exact support minimization becomes
a robust estimation problem. A useful decoder may minimize a weighted residual
or an edge-sparse norm subject to phase consistency.

The exact connectivity theorem remains the zero-noise identifiability
boundary. Stability additionally requires quantitative conditioning of the
incidence and cycle matrices under the declared weights. Algebraic edge
connectivity alone does not bound sample complexity or estimation variance.

## Closure fault hierarchy

The qutrit corridor tester now separates:

1. fault-free phase identifiability: connected probe graph;
2. known erasure tolerance: edge connectivity greater than erasure count;
3. arbitrary edge-fault detection: edge connectivity greater than error count;
4. arbitrary edge-fault correction: edge connectivity greater than twice the
   error count;
5. common vertex-frame rejection: independent anchor;
6. correlated preparation/readout faults: verified causal fault domains;
7. continuous statistical stability: weighted conditioning and sample bounds.

No lower level implies a higher one.

## Hostile fixtures

### Faithful tree with one bad edge

Use the two-edge qutrit tree. Any measured pair of phase differences is
consistent with some vertex phases, so one edge error is invisible.

### Triangle correction overclaim

Use the triangle cycle syndrome to detect inconsistency, then claim it identifies
the faulty edge. Three distinct one-edge explanations remain possible.

### Five nominal edges from one phase source

Implement the `2,2,1` multigraph using one shared unverified phase generator.
A single source fault moves several edges together and violates the sparse-edge
model.

### Cycle-consistent wrong gate

Apply a true logical diagonal phase fault. Every edge is internally consistent
with the wrong vertex assignment. Only the command anchor identifies the gate
as wrong.

### Edge archive without quadrature orientation

Record pairwise fringe magnitudes but not oriented phases. The incidence model
is unavailable and cycle sums are undefined.

## Falsifiers

- Probe count is substituted for edge connectivity.
- A tree is claimed to detect an arbitrary edge error.
- The triangle is claimed to correct one unrestricted edge error.
- Five qutrit edges are called one-error-correcting without independent fault
  domains.
- A gradient or common vertex fault is claimed to have nonzero cycle syndrome.
- Internal phase consistency is claimed to certify agreement with an external
  command frame.
- The sparse exact theorem is promoted to a finite-sample stability bound.
- Basis-ray, leakage, or tomography faults are silently included in the edge
  model.
- Parallel physical routes sharing one controller are counted as independent
  edges.

## Disposition

Fault tolerance of the qutrit coherence packet is now an exact graph-code
problem. A connected tree gives ideal faithfulness. A triangle adds one-edge
detection and erasure tolerance. A five-edge multigraph with connectivity
three is the smallest pairwise-probe design correcting one arbitrary edge
fault.

The remaining kernel is common-mode vertex calibration. It is invisible to
all cycle checks and requires an independently prepared semantic anchor. Thus
redundancy repairs sparse coordinate faults; it still does not manufacture the
reference that tells the graph which logical phase assignment is commanded.

No checker, build, or Git operation was run for this research-only packet.
