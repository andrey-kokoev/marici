# 1942 — The Canonical Five-to-Three Contraction Misses the Homogeneous (mathcal Q) Locus

## Question

Does Entry 1941's physically activated five-site divisor (D_4) possess a
source-defined contraction to the homogeneous three-site family on which
(mathcal Q) is defined?

## Carrier contraction

The active five-site regions are

\[
\{1,2\},\qquad\{3,4\},\qquad\{5\}.
\]

Enumerate all pairs of cycle edges whose contraction turns (C_5) into a
three-vertex graph and requires each active region to become one target
vertex.  Exactly one pair is admissible:

\[
\boxed{e_{12},e_{34}.}
\]

The quotient blocks are

\[
A=\{1,2\},\qquad B=\{3,4\},\qquad C=\{5\},
\]

and the retained edges (e_{23},e_{45},e_{51}) form a triangle.  Thus the
active occurrence labels themselves canonically select a five-to-three
carrier contraction.

## Induced frozen kinematics

On Entry 1234's regular-cone slice,

\[
X'=(2t,2t,t).
\]

Using (P_i^2=2) and

\[
P_i\cdot P_{i+1}=\frac{3+\sqrt5}{4},
\]

the contracted resultant norms are

\[
\left((P_A')^2,(P_B')^2,(P_C')^2\right)
=
\left(\frac{11+\sqrt5}{2},\frac{11+\sqrt5}{2},2\right).
\]

The homogeneous massless conditions (X_i'^2=(P_i')^2) would require

\[
t^2=\frac{11+\sqrt5}{8}
\quad\text{and}\quad
t^2=2.
\]

Their difference is

\[
2-\frac{11+\sqrt5}{8}
=\frac{5-\sqrt5}{8}\neq0.
\]

Therefore

\[
\boxed{
\text{the canonical contraction of the frozen five-site slice does not
intersect the homogeneous three-site }\mathcal Q\text{ locus}.}
\]

## Interpretation

The carrier comparison exists and is canonical, but the coefficient-sector
specialization required to compare (D_4) with (mathcal Q) does not exist
on the frozen one-parameter family.  Substituting contracted energies into
the homogeneous formula for (mathcal Q) would therefore be mistyped.

Entry 1941 remains a genuine higher-site successor-polynomial result.  It is
not presently evidence that (D_4) is a parent deformation of (mathcal Q).

## Next falsifier

Return to the generic five-site source before imposing the regular-cone
slice.  Perform the same labelled contraction there and derive the contracted
three-site Landau discriminant as a function of independent (X'_i,P'_i).
Only if that generic divisor meets the homogeneous locus may its restriction
be compared with (mathcal Q).

## Evidence

- `research/benincasa/marici-gm/src/bin/five_to_three_active_wall_contraction.rs`
- `research/benincasa/results/five-to-three-active-wall-contraction.json`
- allocator claim: `seqclaim-988693169ac82de05e9efd36`

