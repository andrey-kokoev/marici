# 3592 — Positive Prime-Scale Recursion Transports a Hostile Seed Divisor

For any positive primitive transform `R(w)`, the positive scale recursion

\[
F(w)=R(w)+cwF(w),
\qquad 0<c<1,
\]

has the exact solution

\[
F(w)=\frac{R(w)}{1-cw}.
\]

Thus it preserves every primitive zero away from its positive geometric pole.
The smallest witness is `R(w)=1+2w`, `c=1/3`: all completed source
coefficients are positive, yet `w=-1/2` remains a zero, corresponding to
`Re z=-log 2` when `w=e^z`.

The conclusion survives any finite collection of independent positive scale
recursions: their geometric factors transport the primitive divisor rather
than orient it. Prime-scale recursion and positive Fock grammar explain source
provenance, not RH zero confinement. The missing law must constrain the
primitive remainder through non-triangular modular/archimedean sewing or an
equivalent cross-scale boundary condition.

The obstruction also survives mirrored positive recursion. The reciprocal
positive seed `(1+2w)(1+2/w)`, completed by the symmetric denominator
`(1-w/3)(1-1/(3w))`, has coefficientwise-positive reciprocal Laurent
expansion but retains the off-unit reciprocal pair `w=-1/2,-2`. Independent
completion of both sectors is still an invertible localization; genuine
sewing must relate the sectors rather than multiply their charts.

Checker result: `11/11` exact gates passed.

Artifact:
`research/grothendieck/positive-prime-scale-recursion-transports-a-hostile-seed-divisor.md`.
