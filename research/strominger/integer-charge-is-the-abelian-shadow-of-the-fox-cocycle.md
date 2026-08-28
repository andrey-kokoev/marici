# Integer charge is the abelian shadow of the Fox cocycle

## Falsifier

The additive-charge theorem is exact for the elementary response family and for pure powers. It is not source-complete on the full free-group grammar.

Consider three words in \(F(x,y)\):

\[
x,
\qquad
x[x,y],
\qquad
[x,y]x.
\]

All three have the same abelian charge,

\[
(1,0).
\]

Their Fox derivatives are nevertheless distinct. The scalar charge therefore aliases three source histories that the Fox calculus separates.

## Exact relation

The charge is recovered by augmenting the Fox row:

\[
\epsilon(\partial_x w)=\operatorname{exp}_x(w),
\qquad
\epsilon(\partial_y w)=\operatorname{exp}_y(w).
\]

Thus the diagram is

\[
F(x,y)
\xrightarrow{\;\mathcal D\;}
\mathbb Z[F(x,y)]^2
\xrightarrow{\;\epsilon\;}
\mathbb Z^2,
\]

where \(\mathcal D\) is the Fox crossed derivative and the second arrow is augmentation.

The scalar charge is not false. It is a quotient of the source-complete differential datum.

## Composition law

The correct law is crossed rather than merely additive:

\[
\mathcal D(uv)=\mathcal D(u)+u\mathcal D(v).
\]

The prefix action retains where each contribution entered the word. Augmentation erases that action and leaves ordinary addition.

This explains why the scalar theorem worked perfectly on powers: on that restricted one-axis grammar, the omitted placement data is forced. Once commutator decorations are admitted, it is no longer forced.

## Consequence for atomicity

The response-side content charge remains the correct local invariant for \(E(a)\). The word-side invariant cannot generally be replaced by exponent sums.

The source-complete square criterion must therefore retain:

1. the response content ideal;
2. the Fox cocycle or an explicitly justified quotient of it;
3. the endpoint anti-invariant class.

A compiler may collapse the Fox cocycle to integer charge only after proving that its admitted grammar makes the augmentation fiber irrelevant.

## Deutschean reading

The integer charge predicts when repetition or cancellation occurs, but it does not explain why differently placed source operations can share that charge. The Fox cocycle supplies the missing explanatory structure: it records both contribution and placement under composition.

So the stronger statement is:

> Atomicity is a unit condition on a source cocycle. Additive charge is its abelian readout.

## Evidence

The exact checker computes reduced free-group words and integral group-ring Fox derivatives. It verifies:

- identical charge for all three hostile words;
- pairwise distinct Fox rows;
- augmentation recovery of charge;
- the Fox fundamental identity;
- aliasing by scalar response;
- separation by the crossed cocycle.

All six gates pass.
