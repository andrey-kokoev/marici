# The Hidden Relative Response Is Exactly the Doubled Green Forcing Defect

## Reciprocal source system

In the common Fourier--Tate frame, write the reciprocal tail equations as

\[
u'=-zu-f,
\qquad
v'=+zv-f
\]

in the real specialization. Their Green difference satisfies

\[
(u^2-v^2)'
=-2z(u^2+v^2)-2f(u-v).
\]

Hence

\[
2z(u^2+v^2)
=-(u^2-v^2)'-2f(u-v).
\]

The last term was the surviving doubled forcing defect.

## Two local adjoint responses

The forward forcing column in each sector is \(-f\). Its local adjoint response
rows give

\[
r_+=-fu,
\qquad
r_-=-fv.
\]

Their common and relative outputs are

\[
r_\Sigma=r_++r_-=-f(u+v),
\qquad
r_\Delta=r_+-r_-=-f(u-v).
\]

Therefore the Green identity is exactly

\[
2z(u^2+v^2)
=-(u^2-v^2)'+2r_\Delta.
\]

For complex amplitudes, the corresponding real quadratic identity contains
\(2\operatorname{Re}(r_\Delta)\).

## Completed-zero specialization

At the scalar endpoint zero,

\[
u(0)+v(0)=0.
\]

Thus

\[
r_\Sigma(0)=0,
\]

while

\[
r_\Delta(0)=-2fu(0)
\]

can remain nonzero. The scalar readout and the Green obstruction are the two
orthogonal output coordinates of the same labelled response pair:

1. the common coordinate detects completed scalar amplitude;
2. the relative coordinate carries the conservation defect.

## Consequence

The extra response port was not invented to repair the proof. It was already
present as the typed term that refused to cancel. Aspect's tester revealed
that we had compressed the response pair before asking the relational
question.

This also sharpens the role of the source primitive. Introducing \(h'=f\)
does not create the response; it attempts to transport the already identified
relative response into a boundary current. Its known leftover common-path term
is the next outer-mate obstruction.

## Current architecture

```text
two reciprocal input incidences
    -> two transported tails
    -> two local adjoint responses
    -> common output: scalar section
    -> relative output: Green defect
    -> source-primitive outer mate: boundary transfer plus common-path residual
```

The next gate is now very narrow: determine whether the common-path residual
after primitive transfer has its own source-local response mate, or whether
Aspect's arity test requires retaining a genuinely ternary incidence among
input, reciprocal response pair, and moving seam.

