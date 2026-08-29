# Coupled filler torsors produce relative bits and a triangle coherence syndrome

Owner: marici.Kitaev

## Question

What new information appears when two and then three \(C_2\) filler torsors are
coupled, and how does the first higher coherence law emerge from their relative
comparisons?

## Claim boundary

Let each system carry an unframed \(C_2\)-torsor coordinate

\[
x_i\in\mathbb F_2,
\]

where the simultaneous change of reference

\[
x_i\longmapsto x_i+g
\]

for one common \(g\in\mathbb F_2\) is gauge. No individual \(x_i\) is
canonically meaningful without a source reference.

Define the pairwise relative coordinate

\[
d_{ij}=x_i+x_j.
\]

This is invariant under the common shift and is therefore observable without
choosing an absolute filler frame.

### Two systems

For two torsors, the complete gauge-invariant information is the single bit

\[
d_{12}=x_1+x_2.
\]

The map

\[
(x_1,x_2)\longmapsto d_{12}
\]

has kernel

\[
\{(0,0),(1,1)\}.
\]

Thus two-system comparison is faithful modulo the common-mode torsor action but
cannot reconstruct either absolute filler coordinate.

This exactly matches the earlier redundancy result: equality comparison can
detect one relative flip, while a common-mode flip remains invisible.

### Three systems

For three torsors, the three pairwise comparisons satisfy

\[
d_{12}+d_{23}+d_{31}=0.
\]

Only two of the three bits are independent. Conversely, any triple satisfying
this equation arises from some \((x_1,x_2,x_3)\), unique up to common shift.

Therefore the sequence

\[
\mathbb F_2
\xrightarrow{\Delta}
\mathbb F_2^3
\xrightarrow{\delta}
\mathbb F_2^3
\xrightarrow{\kappa}
\mathbb F_2
\]

has the relevant exact portion

\[
\ker\kappa=\operatorname{im}\delta,
\]

where

\[
\delta(x_1,x_2,x_3)=(d_{12},d_{23},d_{31})
\]

and

\[
\kappa(d)=d_{12}+d_{23}+d_{31}.
\]

The scalar

\[
s=\kappa(d)
\]

is the triangle coherence syndrome.

If \(s=0\), the pairwise data admit an underlying set of filler frames, unique
up to common mode. If \(s=1\), no choice of local frames can realize all three
pairwise reports. The inconsistency is relational curvature, not an absolute
bit error at a vertex.

### Detection is not correction

A nonzero triangle syndrome detects an odd number of corrupted pairwise reports
on that triangle. It does not identify which edge is wrong. All three
single-edge corruptions produce the same syndrome.

Thus the three-system closure law provides consistency detection but not a
preferred decoder. Additional trusted ports, asymmetric reliability weights,
or overlapping triangles are required to localize and correct the fault.

This is the higher-torsor analogue of toric syndrome: a boundary law detects a
defect class without choosing its repair representative.

### Cochain interpretation

The vertex frames form a 0-cochain \(x\). The pairwise differences form the
coboundary

\[
d=\delta x.
\]

The triangle syndrome is the next coboundary

\[
s=\delta d=\delta^2x=0
\]

for every consistent source assignment.

Hence the first higher coherence law is not imposed separately. It follows
from the common parent incidence operator and its nilpotence. A corrupted edge
record is exposed because it no longer lies in the image of the lower
incidence map.

On a general connected comparison graph, edge data reconstruct vertex torsors
up to common mode exactly when their sum vanishes around every independent
cycle. A spanning tree reconstructs relative frames but has no redundant cycle
syndrome. Each non-tree edge adds a consistency check.

### Nonabelian successor

Let the filler torsor use a possibly nonabelian group \(G\). Relative
coordinates become

\[
d_{ij}=x_i^{-1}x_j.
\]

The triangle law is ordered:

\[
d_{12}d_{23}d_{31}=e.
\]

Changing a local convention conjugates the based holonomy rather than adding a
scalar. Therefore the \(C_2\) parity syndrome is only the abelian coefficient
shadow of an ordered higher holonomy.

Any scalarization such as trace or determinant can miss a nontrivial
operator-valued triangle residual. The full coefficient lens is required when
\(G\) is nonabelian.

### Relation to Pfaffian volume

The triangle syndrome is not a Pfaffian. It is a curvature or cocycle test.
Pfaffian volume becomes available only after the relative data carry a
skew-bilinear structure on an even-dimensional linearized space.

Thus two distinct invariants must not be merged:

- coboundary closure tests whether relative comparisons come from underlying
  frames;
- Pfaffian nondegeneracy tests whether an alternating relational pairing has
  full volume.

A system can pass triangle closure while its skew pairing is degenerate, or
have a nondegenerate local pairing while its reported comparisons violate the
cycle law.

### Next rung

Suppose every triangle of a tetrahedral comparison network has zero syndrome.
For abelian vertex-difference data on the full simplex, global reconstruction
then follows up to common mode. No new independent scalar obstruction remains.

For operator-valued or weak fillers, however, face fillers can compose in
different orders. A tetrahedral 3-cell must compare those composites. Its
residual is invisible to the abelian triangle equations.

This gives the clean transition:

- two systems expose relative state;
- three systems expose curvature consistency;
- four systems can expose coherence among face fillers.

## Disposition

The coupled-torsor theorem supplies the smallest exact model requested by the
higher-filler programme.

Its machine-independent audit packet is:

- vertex torsor group;
- common-mode action;
- pairwise relative maps;
- cycle incidence matrix;
- kernel and image dimensions;
- triangle or ordered holonomy syndrome;
- decoder authority;
- coefficient lens;
- next-cell coherence status.

The strongest immediate prediction is that adding a third system does not add
a third independent relative coordinate. It adds one redundant report whose
new information is a consistency syndrome.

The first falsifiers are:

- a common-mode shift changing some \(d_{ij}\);
- zero triangle syndrome without any underlying vertex assignment on a simply
  connected complete comparison complex;
- a claimed single-edge correction selected from one triangle syndrome without
  extra authority;
- a nonabelian triangle residual certified only by an abelian scalar shadow.
