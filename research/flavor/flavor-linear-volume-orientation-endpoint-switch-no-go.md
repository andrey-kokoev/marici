# Linear positive volume does not stabilize an oriented three-family interior: WP963

## Question

Does the source-derived Gram volume repair WP962 when added with an arbitrary
positive normalization to the squared ternary orientation?

## Closed-triangle source type

The source packet has `3+3+1` structure: three projective rays, three pairwise
overlaps, and one ternary Bargmann orientation.  It is not a chain-shaped
`3+2+1` packet.  Define

\[
D=\det G,
\qquad q=\operatorname{Im}\mathcal B,
\qquad F_\lambda=q^2+\lambda D,
\qquad \lambda>0.
\]

Maximizing `F_lambda` is equivalent to minimizing a source action containing
both the CP-even orientation reward and a positive volume reward.  Both terms
are weak-basis invariant and conjugation even.

## Exact upper envelope

At fixed overlap sum, arithmetic-geometric mean shows that the upper envelope
is attained on equal squared overlaps `x=y=z=u`.  Optimizing the real
Bargmann component then gives

\[
D(u)=(1-u)(1-2u),
\qquad
q^2(u)=u^3(1-u),
\qquad 0\leq u\leq\frac12.
\]

Therefore

\[
F_\lambda(u)=u^3(1-u)+\lambda(1-3u+2u^2)
\]

and its derivative factors exactly as

\[
F_\lambda'(u)=(4u-3)(\lambda-u^2).
\]

The interior stationary point `u=sqrt(lambda)`, when present, is a minimum.
Every global maximum is consequently an endpoint:

- if `lambda < 1/16`, the orientation endpoint wins:
  `u=1/2`, `q^2=1/16`, `D=0`, span rank two;
- if `lambda > 1/16`, the volume endpoint wins:
  `u=0`, `q^2=0`, `D=1`, an orthonormal CP-blind frame;
- at `lambda=1/16`, the two endpoints are degenerate and no interior maximum
  appears.

## Disposition

A linear positive-volume completion does not balance volume against
orientation.  It creates a first-order endpoint switch between collapsed CP
orientation and full-volume CP blindness.  This holds for every positive
relative normalization, so fixing `lambda` cannot rescue the constructor.

The next source term must enforce the faithful interior rather than merely
reward volume linearly—for example through an independently derived barrier,
constraint, or additional completion field.  Its normalization and occurrence
must be source-derived, and exact conjugation symmetry must retain both
handednesses.  Instrument transport remains open.  No composition is assigned
physical time or causality.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp963_linear_volume_orientation_endpoint_switch_no_go.py

Generated result:
`research/flavor/results/wp963_linear_volume_orientation_endpoint_switch_no_go.json`.
