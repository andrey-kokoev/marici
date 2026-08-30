# One-mediator response grammar (WP400)

## Bounded question

Can WP399's finite one-pole response family be derived from an explicit stable
source mediator rather than postulated as an interpolation class?

## Stable source model

Let $A$ be one real mediator and let $c\geq0$ be a calibrated source context
that shifts both its curvature and tadpole affinely:

\[
V(A;c)=\frac12(M^2+c)A^2-(J_0+J_1c)A,
\qquad M^2>0.
\]

The mediator curvature is positive throughout the admitted domain. Exact
stationary elimination gives

\[
A_\star(c)=\frac{J_0+J_1c}{M^2+c}.
\]

This is precisely WP399's normalized one-pole family, with

\[
a_0=\frac{J_0}{M^2},
\qquad a_1=\frac{J_1}{M^2},
\qquad b_1=\frac1{M^2}.
\]

The mapping is invertible. Thus three calibrated response settings identify
the three source parameters inside this grammar, and a fourth setting tests
the locked context law.

## Exact benchmark

For $M^2=1$, $J_0=1$, and $J_1=2$,

\[
A_\star(c)=\frac{1+2c}{1+c},
\]

giving the exact records $1$, $3/2$, $5/3$, and $7/4$ at contexts
$0,1,2,3$. This reproduces WP399 without importing an abstract rational ansatz.

## Physical authority boundary

The model is an explicit stable source grammar, but the context operation is
still conditional. A real experiment must explain why one knob produces the
specific locked shifts $M^2\mapsto M^2+c$ and
$J_0\mapsto J_0+J_1c$ in a common calibrated frame.

An allowed quadratic curvature correction, additional mediator, nonlinear
tadpole, or finite width enlarges the response family. Such terms must be
forbidden, derived, or included before reserving the withheld context.

The mediator displacement is a response readout. It identifies the grammar
parameters and tests their transport law; it does not select their numerical
values or the physical flavor shell.

## Disposition

WP400 clears WP399's abstract-realization gate at the classical source level.
It supplies a stable one-mediator constructor for the one-pole response. The
remaining gate is an actual flavor mediator and experimentally calibrated
context knob implementing the locked affine shifts.

Run `uv run --with sympy python
research/flavor/checkers/wp400_one_mediator_response_grammar.py` to regenerate
the result.
