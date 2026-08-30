# The complete interval observer is faithful but scalar nullity fixes only an endpoint projection

## Common comparison fiber

Let `A` be a real source that is nonzero on an interval, and use the Fourier
parameter `zeta`. Define the doubled complete interval section

\[
\mathcal O(\zeta)(\ell)
=
\left(B_\ell(\zeta),B_\ell(-\zeta)\right),
\qquad
B_\ell(\zeta)=\int_0^\ell A(v)e^{i\zeta v}\,dv.
\]

All reciprocal and adjoint images now live in one common fiber of locally
absolutely continuous functions of `ell`.

## Faithfulness theorem

Suppose

\[
\mathcal O(\zeta)=\mathcal O(\eta).
\]

Differentiating almost everywhere gives

\[
A(\ell)e^{i\zeta\ell}
=
A(\ell)e^{i\eta\ell}.
\]

On any interval where `A` is nonzero,

\[
e^{i(\zeta-\eta)\ell}=1
\]

for every `ell` in that interval. Hence `zeta=eta`. The complete interval
observer is therefore faithful in the spectral parameter.

In particular,

\[
\mathcal O(-\zeta)=\mathcal O(-\overline\zeta)
\]

forces `zeta=conjugate(zeta)`, which is the seam in the Fourier convention.

## What scalar nullity supplies

The completed scalar readout is only the aggregate of the terminal endpoint

\[
X(\zeta)
=
\sigma\mathcal O(\zeta)(\infty),
\qquad
\sigma(x,y)=x+y.
\]

Every doubled interval path begins at the same zero vector. At a Real-even
scalar zero, reciprocal and adjoint terminal states satisfy only

\[
\sigma\mathcal O(-\zeta)(\infty)
=
\sigma\mathcal O(-\overline\zeta)(\infty)
=0.
\]

Thus both terminal states lie in `ker sigma`. Scalar nullity does not say that
the terminal vectors agree, much less that their intermediate paths agree.

## Exact projection hostile

In the terminal doubled fiber, the distinct vectors `(1,-1)` and `(2,-2)`
both lie in `ker sigma`. Join the common initial zero vector to them by two
different piecewise-linear paths. The paths share their initial state and
their terminal scalar readout, while both their terminal vectors and their
interiors differ.

This is the smallest exact witness to the information loss. Source equations
may restrict the admissible paths further, but scalar nullity alone cannot do
so.

## Categorical meaning

The complete interval observer supplies the common comparison object and its
parameter faithfulness. Those were the first and third gates isolated by the
simple-kernel audit. The unresolved second gate is now exact:

> Why should a source-authorized scalar-null projection have a unique lift to
> a terminal doubled state and then to the full interval path?

This is a path-lifting or boundary-value uniqueness theorem. It cannot follow
from endpoint equality alone because the source equation is forced and admits
distinct reciprocal and adjoint paths.

## Surviving mechanisms

A viable source law must provide at least one of:

- equality of the interval derivatives through a conserved Real current;
- a unique minimal-action or horizontal lift selected before scalarization;
- dense arithmetic values that are star-compatible for an independently
  derived reason;
- a boundary differential equation whose two-endpoint solution is unique;
- a localization theorem making the difference path inadmissible.

## Disposition

The common-fiber and faithfulness problems are solved by the complete interval
observer. The singular RH-bearing problem is uniqueness of the zero-state lift
through two stages: scalar projection to terminal state, then terminal state
to full path. Any next proposal should expose both stages explicitly.
