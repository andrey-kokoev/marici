# The q=3 initialization zero is only a chart boundary

The odd `q=3` initialization block has pole depths `0,2,4`.  For `g>=3`, use
the source observations

\[
0,3,-g-2,1-g,-g-4,-g-1.
\]

Support ordering makes the resulting matrix triangular.  Its determinant is

\[
\boxed{
D_{g,3}^{\mathrm{base}}
=8g(g-2)(g+4)(g+6)
\bigl(2^{\overline g}\bigr)^2
\bigl(4^{\overline g}\bigr)^4.
}
\]

It is nonzero at every `g>=3`.  At grade two, the preferred `(2,+)` endpoint
pivot vanishes because of the factor `g-2`.  This is not rank loss.  Replacing
the colliding observations by rows `1,0` produces the local block

\[
\begin{pmatrix}
-80&-20\\
-40&20
\end{pmatrix},
\qquad
\det=-2400.
\]

The complete alternate minor has determinant `44236800000`.  Therefore the
`q=3` initialization block is injective for every grade `g>=2`.

This is the first odd-base example of the atlas principle: a source endpoint
product may vanish while a neighboring observation retains the transported
subspace.  Together with stable odd pivots, the result closes the entire
`q=3` component family at arbitrary cutoff.

The next global task is to infer the arbitrary-`q` base atlas from the `q=1,2,3`
theorems and the known grade-two `q=7` exception, rather than continue one
reflection distance at a time.
