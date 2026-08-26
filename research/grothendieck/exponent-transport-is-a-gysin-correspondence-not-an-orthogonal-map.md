# Exponent Transport Is a Gysin Correspondence, Not an Orthogonal Map

## Question

The five-channel degree comparisons preserve one global quadratic-form
family. Does the exponent-shift direction provide a second orthogonal map and
hence an ordinary metric-holonomy square?

No. Exponent transport has different variance at the wall. It is
noninvertible on every finite polar jet and must be represented as a relative
or Gysin correspondence.

## Mellin shift as source multiplication

For

\[
I_f(q)=\int_0^\infty y^qf(y)\,dy,
\]

one exponent step satisfies

\[
I_f(q+1)=I_{yf}(q).
\]

Thus positive exponent transport is multiplication by the wall coordinate
\(y\) before Mellin transformation.

Write the analytic wall germ as

\[
f(y)=a_0+a_1y+a_2y^2+\cdots.
\]

Then

\[
yf(y)=0+a_0y+a_1y^2+\cdots.
\]

The first wall coefficient is killed and every other coefficient moves up by
one grade.

## Polar interpretation

The meromorphic Mellin transform has residues

\[
\operatorname*{Res}_{q=-n-1}I_f(q)=a_n.
\]

After multiplication by \(y\), the residue sequence becomes

\[
(a_0,a_1,a_2,\ldots)
\longmapsto
(0,a_0,a_1,\ldots).
\]

This is the unilateral Rees shift. Its missing first coordinate is precisely
the boundary/Gysin grade.

## Finite-jet obstruction

On a jet through order \(N\), the shift matrix is

\[
S_N=
\begin{pmatrix}
0&0&\cdots&0\\
1&0&\cdots&0\\
0&1&\ddots&\vdots\\
\vdots&\ddots&\ddots&0
\end{pmatrix}.
\]

It satisfies

\[
S_N^{N+1}=0,
\qquad
\det S_N=0.
\]

If a nondegenerate quadratic form \(Q\) obeyed

\[
S_N^TQS_N=Q,
\]

then taking determinants would give

\[
0=\det Q,
\]

a contradiction. No finite Laurent-jet exponent shift can be orthogonal for
a nondegenerate form.

## Categorical correction

The two transport directions have different types:

- degree transport is an invertible comparison between coefficient fibers;
- exponent transport meets the wall divisor and has boundary/Gysin variance.

Consequently the desired coherence is not an ordinary commutative square of
isomorphisms. It must retain the exact triangle or correspondence connecting:

1. the regular Mellin strip;
2. the polar Rees tower;
3. the boundary residue grade.

The scalar Pearson identity is the pushforward shadow of this typed object.
Agreement after scalar integration cannot reconstruct the missing boundary
coordinate.

## Meaning for the five-channel form

The degree-global quadratic form remains valid. The new result says it cannot
be tested against exponent transport by placing both operations in the same
orthogonal group.

Instead, one needs a relative pairing for which multiplication by \(y\) and
the residue/Gysin map are adjoint pieces of a boundary-bearing complex. The
holonomy observable is then a chain homotopy or anomaly class, not a matrix
commutator.

This is not a request for a sixth scalar channel. At continuous exponent
depth, the missing object is the full function-valued base strip together
with its polar Rees filtration. Any fixed finite channel count is only an
integer-jet truncation.

## Sharp next theorem

Construct the smallest exact sequence in which multiplication by \(y\),
restriction to the wall, and the residue map coexist, then lift the
five-channel degree pairing to that sequence. The falsifier is a surviving
typed boundary class after comparing Pearson shift with residue restriction.

## Verification

The checker
`research/grothendieck/checkers/exponent_gysin_shift_obstruction.py` verifies
the residue shift, nilpotence and singularity through jet order twelve, and
the determinant obstruction to a nondegenerate invariant form.
