# A boundary-adapted atlas extends even transport one step earlier

For even `q`, the first pre-stable extension occurs at

\[
k=\frac q2+1,
\qquad a=q+2.
\]

A deterministic augmenting matcher may choose an old maximal minor that
consumes one of the two future semantic boundary rows.  Its subsequent scalar
ratio can then vanish or differ from the stable character.  This is a chart
effect.

Instead, reserve the future rows

\[
r_-=-a-g,
\qquad r_+=-a-g+q+1,
\]

and choose any full-rank old minor from the remaining observations.  In this
boundary-adapted chart, the Schur complement is exactly diagonal:

\[
\boxed{
S=\begin{pmatrix}
(-1)^{g+1}(a+g+q-1)a^{\overline g}&0\\
0&(-1)^gqg(g+3)a^{\overline{g-1}}
\end{pmatrix}.
}
\]

Thus the invariant even transport law already holds at `a=q+2`; the previously
used threshold `a=q+4` was sufficient for one preferred chart, not intrinsic.

This atlas crosses both known coordinate failures:

- at `(g,q,k)=(2,12,7)`, it gives `diag(-5670,1680)` despite the preferred
  minor being zero;
- at `(5,4,3)`, it gives `diag(423360,-483840)`, removing the apparent
  `99/40` ratio residual.

The checker verifies the construction on all 210 blocks with grades 2 through
15 and even depths 2 through 30.  This is exact finite evidence for an
unbounded reserved-row atlas theorem.  The remaining proof obligation is the
symbolic existence of an old full-rank minor after deleting the two reserved
rows; once that is established, the pivot formulas are already symbolic.
