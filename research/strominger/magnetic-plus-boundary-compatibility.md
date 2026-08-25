# The aligned plus tail has zero reconstructed boundary jet

Separate the remaining low-grade plus system into:

- the triangular aligned tail `A`;
- the parity collision columns;
- boundary observations `(1,0)` for even `d`, or `(1,2,0)` for odd `d`.

In block form,

\[
M=\begin{pmatrix}A&B\\C&E\end{pmatrix}.
\]

Exact elimination gives the stronger identity

\[
\boxed{CA^{-1}B=0.}
\]

Therefore

\[
\boxed{S=E-CA^{-1}B=E.}
\]

The tail does not merely preserve the determinant of the local collision
coordinate.  It leaves that coordinate literally unchanged.

This is not the trivial statement `B=0` or `C=0`: both blocks are nonzero in
285 of the 345 audited cases.  It is, however, a support theorem after passing
to the aligned triangular basis.  Write `a` for the even pole-depth label of a
plus column.  Exact reconstruction has support

\[
 a\le d-2\quad(d\text{ even}),
 \qquad
 a\le d-3\quad(d\text{ odd}),
\]

whereas the tail columns having a nonzero reserved boundary jet satisfy

\[
 a\ge d+2\quad(d\text{ even}),
 \qquad
 a\ge d+3\quad(d\text{ odd}).
\]

Consequently the column support of `A^{-1}B` and the column support of `C` are
disjoint.  Their product vanishes term by term:

\[
\operatorname{supp}(A^{-1}B)\cap\operatorname{supp}(C)=\varnothing
\quad\Longrightarrow\quad CA^{-1}B=0.
\]

The gap has a direct path interpretation.  The aligned leading pivots solve a
collision column using only predecessor depths on the left of the collision.
A plus column at depth `a` has row interval starting at `d-a`; it can see the
reserved rows only after crossing to the right of the collision.  Triangular
transport never crosses that gap.

There is one exact simplification.  The `(0,-)` column is supported only on
the reserved rows `0,1`, because its source polynomial has only the terminal
coefficient `c_g`.  Its column in `B` is therefore identically zero.  The
nontrivial identity concerns only the neighboring plus columns:

\[
(d,+)
\]

for even `d`, or

\[
(d-1,+),(d+1,+)
\]

for odd `d`.  Thus the desired symbolic statement is internal to one
contiguous plus family; the reflected minus endpoint does not participate in
the reconstruction.

The exact checker verifies 345 low-grade blocks with

\[
2\le g\le16,
\qquad
2\le d\le24.
\]

It includes both distinguished zero fibers:

- the even presentation divisor `d=g+8`, unchanged before its row-`3` repair;
- the genuine odd exception `(g,d)=(2,5)`.

Together with the two-chart triangular theorem, these inequalities give the
symbolic boundary mechanism: predecessor-only reconstruction on the left and
boundary visibility on the right.  The checker separately tests the support
bounds and disjointness, rather than inferring them from a zero matrix product.
