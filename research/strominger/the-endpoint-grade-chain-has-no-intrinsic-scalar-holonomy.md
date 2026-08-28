# The Endpoint Grade Chain Has No Intrinsic Scalar Holonomy

## Question

The Cartan quadric determines the endpoint spaces and their multiplication.
Does the sequence of numerical factors in the spin-weighted grade-changing
maps define additional invariant structure?

## Multiplicity-one rigidity

For every nonnegative integer \(l\), the Clebsch decomposition is

\[
H_1\otimes H_l
\cong
H_{l+1}\oplus H_l\oplus H_{l-1},
\]

with the final summand absent at \(l=0\). Therefore

\[
\dim\operatorname{Hom}_{SO(3)}
\left(H_1\otimes H_l,H_{l+1}\right)=1.
\]

Every equivariant adjacent grade-changing constructor is consequently a
scalar multiple of Cartan multiplication:

\[
J_l=\lambda_l C_l.
\]

The representation theory fixes the direction of the map, but not its scalar
until a normalization is supplied.

## Scalar gauge theorem

Regard the grades as the vertices of the one-sided chain

```text
H_s -> H_(s+1) -> H_(s+2) -> ...
```

Suppose every \(\lambda_l\) is nonzero. Choose a nonzero scale \(t_s\) and
define recursively

\[
t_{l+1}=\lambda_l t_l.
\]

After the vertex change of presentation \(v_l\mapsto t_lv_l\), every edge
coefficient is one. Hence a nonzero scalar sequence on this chain has no
intrinsic holonomy and supplies no additional isomorphism invariant.

The spin-weighted factors

\[
\lambda_l^2=\frac{2(2l+1)}{l+1}
\]

are therefore a source-fixed metric normalization, not a new algebraic
attachment class.

## What remains invariant

Two kinds of data survive the scalar gauge:

1. A zero edge. No invertible vertex rescaling can turn a zero constructor
   into a nonzero one. It is a genuine grade barrier.
2. Holonomy around a cycle, or a relative ratio between distinct paths with
   the same endpoints. Vertex rescaling cancels from the path ratio.

The present Cartan endpoint tower has neither: all adjacent factors are
nonzero and symmetric multiplication makes every path comparison trivial.
Thus it contains no scalar attachment modulus beyond its normalized
presentation.

## Categorical interpretation

The grade index is the acyclic quiver \(A_\infty\). A rank-one local system on
an acyclic chain is trivializable. Scalar anomaly data require a nontrivial
loop in the presentation graph or a noninvertible edge.

This separates three layers that had been close together:

- the quadric algebra fixes the objects and Cartan products;
- equivariance proves each adjacent constructor is unique up to scale;
- the source metric and spin-raising convention select a representative of
  the otherwise gauge-trivial scale sequence.

## Hostile extension

Add one return edge joining a later grade to an earlier grade. If the product
of edge factors around the resulting cycle is not one, no vertex rescaling
can trivialize all factors. The cycle product is genuine scalar holonomy.

Therefore the no-modulus result must not be exported from the grade chain to
an arbitrary coherence network. Its source is acyclicity, not scalar
commutativity alone.

## Consequence for the deeper geometric object

For the endpoint subsystem, the required object is the pair consisting of
the Cartan algebra and its graded tail module. No further scalar correspondence
is needed to describe the abstract tower. A physical comparison of amplitudes
between grades still requires the independently authorized Hermitian or graph
norm that fixes the vertex scales.

This does not classify affine torsion attachment. Such attachment is an
extension problem outside the multiplicity-one Cartan chain and may carry
genuine extension data.

## Evidence replay

The checker verifies multiplicity one, nonvanishing of every spin-weighted
factor through degree fifty, recursive scalar trivialization, the invariance
of zero edges, and the first cycle-holonomy hostile fixture.

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/endpoint_grade_chain_scalar_holonomy_checks.py
```

Machine-readable results are written to
`research/strominger/results/endpoint_grade_chain_scalar_holonomy_checks.json`.

