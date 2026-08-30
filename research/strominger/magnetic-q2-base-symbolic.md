# The q=2 initialization block is triangular for every grade

Before the first even boundary extension, the `q=2` component contains the
four reflected columns

\[
(0,-),(0,+),(2,-),(2,+).
\]

Use the source-oriented observations

\[
1,\qquad2,\qquad-g-2,\qquad-g.
\]

The two depth-zero columns are singleton endpoints on rows `1` and `2`.
On the remaining rows, the depth-two plus support begins at `-g`, while the
minus support begins at `-g-2`.  The resulting matrix is triangular by
support.

Its determinant is

\[
\boxed{
D_{g,2}^{\mathrm{base}}
=-3(g-1)(g+1)(g+3)
\bigl(4^{\overline g}\bigr)^2
\bigl(2^{\overline g}\bigr)^2.
}
\]

Every factor is nonzero for `g>=2`.  Hence the `q=2` component cannot acquire
an initialization kernel at any grade.  The first extension `a=4=q+2` is
covered by the even boundary atlas, and all later extensions by the symbolic
stable even pivots.

This closes the smallest component family left open by the global coverage
audit.  The next uncovered base family is `q=3`; more generally, arbitrary
odd and even reflection distance still require a uniform initialization
theorem rather than separate fixed-`q` formulas.
