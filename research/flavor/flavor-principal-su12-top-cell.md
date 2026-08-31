# Principal \(SU(12)\) top cell: WP1055

## Question

Can a parent representation derive WP1054's spin-\(11\) pole cell rather than
postulate \(j=11\)?

## Principal-\(sl_2\) adjoint law

Under a principal \(sl_2\), the \(SU(n)\) adjoint decomposes as one
irreducible of each spin

\[
1,2,\ldots,n-1,
\]

with dimensions

\[
3,5,\ldots,2n-1.
\]

The dimensions sum to \(n^2-1\), the adjoint dimension.

For \(n=12\),

\[
\operatorname{Adj}(SU(12))
\longrightarrow
V_1\oplus V_2\oplus\cdots\oplus V_{11},
\]

with dimensions

\[
3,5,7,9,11,13,15,17,19,21,23.
\]

The unique top cell is therefore

\[
V_{11},
\qquad
\dim V_{11}=23.
\]

This is exactly WP1054's irreducible pole cell.

## Capacity match

Take the two nilpotent incidence directions \(E,F\) as the conditional
two-port arity:

\[
k=2.
\]

If the factor \(12\) in WP1036 is identified with the parent \(SU(12)\), then

\[
h=\frac{C\cdot12\pi^2}{1367k}
 =\frac{23\cdot12\pi^2}{1367\cdot2}
 =\frac{138\pi^2}{1367}.
\]

With the WP1054 common clock \(M^2=1\), the normalized response remains
\(1/2\).

## Lower-component hostile

The top-cell condition matters. In a bounded scan \(2\le n\le30\), only
\(SU(12)\) has top dimension \(23\):

- \(SU(11)\) has top spin \(10\), top dimension \(21\);
- \(SU(13)\) has top spin \(12\), top dimension \(25\).

\(SU(13)\) does contain a \(23\)-dimensional spin-\(11\) component, but it is
a lower component. Thus “the adjoint contains \(V_{11}\)” is insufficient;
the source must select the top principal cell.

## Boundary

This packet does not prove that WP1036's factor \(12\) is an \(SU(12)\)
parent, that the pole operator is the top principal component, or that the
nilpotent directions \(E,F\) are physical detector ports. It also does not
derive the common mass scale.

## Classification

Conditional parent/top-cell constructor. It gives WP1054's unexplained spin
\(11\) a minimal representation ancestry and a sharp lower-component hostile.

Checker: `research/flavor/checkers/wp1055_principal_su12_top_cell.py`

Result: `results/wp1055_principal_su12_top_cell.json`
