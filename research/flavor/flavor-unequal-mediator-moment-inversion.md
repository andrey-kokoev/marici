# Unequal-mediator moment inversion (WP346)

## Generic two-branch source

Let a shared mediator choose probabilities (a) and (b) with weights (w)
and (1-w). The first three normalized domain coincidences are the first three
moments of this two-point measure.

Their response determinant is

\[
w(1-w)(a-b)^4.
\]

It is nonzero for distinct occupied branches. Define

\[
S=\frac{u_3-u_1u_2}{u_2-u_1^2},
\qquad
P=Su_1-u_2.
\]

Then (S=a+b), (P=ab), and the unordered branch probabilities are the roots
of

\[
z^2-Sz+P=0.
\]

After choosing a root ordering, (w=(u_1-b)/(a-b)). Exchanging roots sends
((w,a,b)) to ((1-w,b,a)), the same unlabelled mediator point.

## Collision and grammar gates

The determinant vanishes when a branch has zero weight or when (a=b). These
are genuine quotient strata where the unused or collided branch cannot be
identified.

Fourth order supplies the recurrence test

\[
u_4=Su_3-Pu_2.
\]

A nonzero residual rejects the two-point mixing grammar. Thus three moments
identify its generic quotient and fourth order tests whether the family was too
narrow.

Run `uv run --with sympy python
research/flavor/checkers/wp346_unequal_mediator_moment_inversion.py` to
regenerate the exact inversion audit.
