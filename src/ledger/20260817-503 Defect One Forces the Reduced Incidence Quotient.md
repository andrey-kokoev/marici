# Entry 503 — Defect One Forces the Reduced Incidence Quotient

Entry 502 finds a natural cyclic incidence module

\[
A_+\eta,
\qquad
A_+=\mathbb Q[x]/(x^2),
\quad x=a^2.
\]

It has rational dimension two.  Entry 473's invariant flatness defect,
however, is one-dimensional at every cutoff.  These cannot be identified as
bare vector spaces.

There is only one possible one-dimensional \(A_+\)-module.  If \(x\) acts
on a one-dimensional rational space by a scalar \(\lambda\), the relation
\(x^2=0\) requires

\[
\lambda^2=0,
\]

and hence \(\lambda=0\).  Therefore

\[
\boxed{
\text{any one-dimensional plus defect has type }A_+/(x).
}
\]

## Consequence

The full incidence principal-parts module \(A_+\eta\) is too large to be the
observed defect.  If incidence descent explains Entry 473, the total
differential must kill the second Cartier layer \(x\eta\) while retaining
the reduced generator \(\eta\):

\[
A_+\eta\longrightarrow A_+\eta/(x\eta)
\cong A_+/(x).
\]

This sharpens the next computation from a generator count to a specific
chain-level condition.  Merely adjoining the cyclic length-two module would
overcorrect the finite defect.

The result also distinguishes the local conormal coefficient object from
its global filtered image: the local object may retain Cartier length two,
while the orbit comparison sees only its reduced incidence head.

## Next gate

Compute multiplication by \(a^2\) on the stable plus-defect line directly
from the cutoff matrices, using the transition from cutoff \(D\) to
\(D+2\).  The incidence hypothesis predicts that the induced map is zero.
Then identify the ordinary exact column whose boundary kills \(x\eta\).

The module-theoretic constraint is checked by
`research/voevodsky/check_soft_axis_plus_defect_module_constraint.py`.
