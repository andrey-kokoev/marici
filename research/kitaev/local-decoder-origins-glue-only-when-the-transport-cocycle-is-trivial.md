# Local Decoder Origins Glue Only When the Transport Cocycle Is Trivial

Let (P) be a connected parameter graph indexing cutoffs, source charts, or
adiabatic sectors. At each vertex (p\in P), suppose the correction classes
form a torsor (T_p) over one fixed logical group (H).

Assume every oriented parameter edge (e:p\to q) carries an authorized
transport map

\[
\tau_e:T_p\to T_q.
\]

Choose local origins (r_p\in T_p). Relative to these choices, transport has
a displacement

\[
\tau_e(r_p)=r_q+h_e,
\qquad
h_e\in H.
\]

The edge labels (h_e) form a transport 1-cochain.

Changing local origins by

\[
r_p\longmapsto r_p+k_p
\]

changes the displacement by a coboundary:

\[
h_e\longmapsto h_e+k_p-k_q.
\]

Therefore the sum of displacements around any oriented parameter cycle is
frame independent.

## Gluing theorem

A globally transported decoder origin exists exactly when local origins can be
chosen so that every edge displacement vanishes:

\[
h_e+k_p-k_q=0.
\]

On a graph, this is possible if and only if every cycle holonomy vanishes. The
obstruction class is

\[
[h]\in H^1(P;H).
\]

Thus pointwise pointed torsors do not guarantee a globally pointed family.
The missing datum can be transport monodromy rather than a missing local
reference.

## Exact (C_2) triangle

Take a triangular parameter loop and (H=C_2\). Let the three oriented edge
displacements be

\[
(h_{01},h_{12},h_{20})=(1,0,0).
\]

Their cycle sum is one. No choices (k_0,k_1,k_2\) can make all transformed
edge displacements zero.

By contrast,

\[
(1,1,0)
\]

has cycle sum zero and is a coboundary. It admits two compatible choices of
local origins, differing by one global (C_2) translation.

On a parameter tree, every displacement cochain is removable because there
are no cycles. One root reference propagates uniquely, up to a global logical
translation.

## Reference versus transport

There are now two independent gates:

- local pointing: each torsor has a source-derived origin candidate;
- global transport: the candidate origins are preserved consistently around
  parameter loops.

A tensor unit or vacuum can solve the first gate. It solves the second only if
the authorized transport returns it to itself with trivial logical
displacement. If transport moves the unit, a normalization cell may cancel
the cocycle; that cell must itself be source-derived.

This is the precise algebra behind the distinction

\[
\text{canonical local frame}
\ne
\text{globally preserved frame}.
\]

## Completion gate

Even a trivial algebraic cocycle is insufficient if the edge transports or
frame changes have norms diverging with cutoff. Completion-stable gluing also
requires uniformly continuous transport and a fixed parameter cover. A
cutoffwise coboundary (k_{p,N}) with unbounded norm is the transport analogue
of an escaping decoder.

## Cross-sector use

For Fourier--Tate or sheet transport, the theorem asks whether the source unit
returns with a nontrivial invertible-current or phase displacement. It does
not derive that displacement. Grothendieck must supply the actual transport,
normalization, and parameter loop.

For toric decoding, an adiabatic or code-deformation family can have locally
valid decoder frames whose logical monodromy is nontrivial around a deformation
cycle. Such monodromy may be an intended logical gate rather than a defect;
the compiler must type which.

## Falsifiers

- Inferring global frame consistency from a preferred origin in each fiber.
- Removing a nonzero cycle displacement by independent local relabelling.
- Calling intended logical holonomy a decoder defect without checking the
  declared transport goal.
- Adding a normalization cell solely to cancel the measured cocycle.
- Ignoring divergent frame-change norms in completion.
- Inventing a Fourier--Tate parameter loop or displacement from the abstract
  theorem.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to classify the obstruction remaining after every local
torsor is pointed.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Local origins glue precisely when the authorized transport cocycle is
trivial; otherwise the family carries genuine logical monodromy.
