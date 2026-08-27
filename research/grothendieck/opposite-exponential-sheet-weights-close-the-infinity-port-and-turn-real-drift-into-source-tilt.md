# Opposite Exponential Sheet Weights Close the Infinity Port and Turn Real Drift into Source Tilt

## Spectral weights forced by the two orientations

Write

\[
z=a+it.
\]

For the reciprocal tails define

\[
H_+(q)=e^{aq}G_+(q),
\qquad
H_-(q)=e^{-aq}G_-(q).
\]

The source-normalized domain is

\[
H_+,H_-\in H^1(0,\infty).
\]

Equivalently, the original tails lie in opposite exponentially weighted
Sobolev spaces. These weights are not fitted: they are the moduli of the two
reciprocal Mellin characters.

## Fixed-domain conjugation

The sheet equations conjugate exactly as

\[
(\partial_q+z)G_+
=e^{-aq}(\partial_q+it)H_+,
\]

and

\[
(-\partial_q+z)G_-
=e^{aq}(-\partial_q+it)H_-.
\]

Thus the real spectral drift is removed from the differential operators. Both
live on fixed `H^1` domains and retain only the unitary seam parameter `t`.

The homogeneous forgers transform to

\[
e^{aq}e^{-zq}=e^{-itq},
\qquad
e^{-aq}e^{zq}=e^{itq}.
\]

Neither belongs to `L^2(0,infinity)`. Hence the weighted domain excludes the
zero-forging torsor on both sheets and is closed after conjugation to ordinary
`H^1`.

At `a=0` the two weights become one, so the domains sew to the ordinary
unitary seam domain without a discontinuous choice.

## Real drift becomes opposite source tilt

The source equations become

\[
(\partial_q+it)H_+=-e^{aq}f,
\qquad
(-\partial_q+it)H_-=e^{-aq}f.
\]

Their source solutions are

\[
H_+(q)=\int_q^\infty e^{av}f(v)e^{it(v-q)}\,dv,
\]

and

\[
H_-(q)=\int_q^\infty e^{-av}f(v)e^{-it(v-q)}\,dv.
\]

Since the weights equal one at `q=0`, the scalar readout remains

\[
X(z)=H_+(0)+H_-(0).
\]

The real coordinate has therefore moved from operator drift into a relative
tilt of the common source. This is the canonical meaning of the two open
half-planes in the completed boundary system.

## RH target in the fixed frame

For real `f`, define

\[
F_a(t)=\int_0^\infty e^{aq}f(q)e^{itq}\,dq.
\]

Then

\[
X(a+it)=F_a(t)+\overline{F_{-a}(t)}.
\]

An off-seam zero requires two independent conditions:

\[
|F_a(t)|=|F_{-a}(t)|
\]

and opposite phase. Therefore the strict modulus inequality

\[
a>0
\quad\Longrightarrow\quad
|F_a(t)|>|F_{-a}(t)|
\]

would exclude zeros in the right half-plane, with reflection excluding the
left. This is the vertical-modulus or de Branges monotonicity target recovered
from source-domain closure rather than introduced as an external scalar
criterion.

## Scope boundary

The weighted-domain theorem repairs completion and rejects the homogeneous
forger. It does not prove the strict modulus inequality. Generic positive
sources can violate it at selected frequencies. Theta's modular and labelled
structure must supply the missing orientation.

The result does explain why that scalar inequality is the correct observable:
it compares the two source tilts induced by the only completion that preserves
the Volterra infinity normalization on both sheets.

## Result

Opposite exponential sheet weights give a closed, source-faithful completion
that sews at the critical line. They transform the real spectral displacement
into opposite tilts of one theta source. RH is thereby reduced to strict
dominance of the outward-tilted Fourier amplitude over the inward-tilted one.

