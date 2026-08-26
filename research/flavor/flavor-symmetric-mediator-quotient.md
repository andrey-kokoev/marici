# Symmetric-mediator quotient (WP345)

## Physical quotient

For the equal-weight WP344 mediator, exchanging its two branches sends
(d\mapsto-d) without changing any marginal domain observable. The faithful
source coordinate is therefore

\[
(\bar p,s),
\qquad
s=d^2,
\]

not the literal signed pair ((\bar p,d)).

The first two moments give the exact inverse

\[
\bar p=u_1,
\qquad
s=u_2-u_1^2.
\]

Their response Jacobian with respect to ((\bar p,s)) has determinant one. In
the signed presentation coordinate its determinant is (2d), which vanishes
at the branch-collision point (d=0); this is a chart effect removed by the
quotient coordinate (s).

## Third-order control

The third moment supplies no new parameter inside the frozen symmetric
two-branch grammar. It must obey

\[
u_3=3u_1u_2-2u_1^3.
\]

A nonzero residual falsifies the grammar. Thus second order identifies the
quotient, while third order tests whether the admitted source family was too
narrow.

## Reference rule

Resolving the sign of (d) requires a mediator branch label. Such a port
creates a new relational experiment over the branch stabilizer; it does not
recover an absolute sign from the unlabelled preparation.

Run `uv run --with sympy python
research/flavor/checkers/wp345_symmetric_mediator_quotient.py` to regenerate the
exact quotient audit.
