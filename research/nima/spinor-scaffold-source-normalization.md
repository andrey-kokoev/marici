# Spinor–Scaffold Source Normalization

For a single scalar pair, the source dictionary is

\[
q=p_a+p_b,\qquad \epsilon=p_b-p_a.
\]

On the angle branch \(\langle ab\rangle=0\), write

\[
\lambda_b=t\lambda_a.
\]

Then

\[
q=\lambda_a(\widetilde\lambda_a+t\widetilde\lambda_b),
\qquad
\epsilon=\lambda_a(t\widetilde\lambda_b-widetilde\lambda_a).
\]

Both are rank-one bispinors and share their left spinor.  On the square branch
the transposed statement holds: they share their right spinor.  Thus the two
normalization branches are precisely the two circular-polarization coefficient
lines, up to the conventional naming of helicity sign.

Two operations must be kept distinct:

* four-dimensional parity transposes the bispinors and exchanges the angle and
  square branches;
* exchanging the two scalar labels fixes \(q\), negates \(\epsilon\), and stays
  on the same spin branch.

Therefore physical spin parity and scaffold exchange are independent already
in the source momentum geometry.  This supplies the source-level explanation
for the twelve-state correspondence and for the product character derived from
the two normalization quotients.

It also sharpens the remaining problem.  For each of the two alternating
three-pair scaffold strata, helicity evaluation is locally canonical as a
coefficient line.  The unresolved datum is its comparison across the common
six-scalar conductor—not the definition of helicity on either branch.

Certificate:
`research/nima/checkers/check_spinor_scaffold_source_normalization.py`
