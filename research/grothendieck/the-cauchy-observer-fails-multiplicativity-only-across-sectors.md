# The Cauchy observer fails multiplicativity only across sectors

## The character law

For the centered Cauchy law of scale `1/2`, write

\[
\phi(u)=\mathbb E e^{iuT}=e^{-|u|/2}.
\]

For two Mellin frequencies `u` and `v`, define the multiplicativity defect

\[
\delta(u,v)
=
\phi(u+v)-\phi(u)\phi(v).
\]

The triangle inequality gives

\[
\delta(u,v)
=
e^{-|u+v|/2}-e^{-(|u|+|v|)/2}
\ge0.
\]

Equality holds exactly when `u` and `v` have the same sign or one is zero.
For nonzero opposite signs, the inequality is strict.

## One-sided character, two-sided defect

On either valuation cone separately, absolute value is additive:

\[
|u+v|=|u|+|v|.
\]

Therefore the Cauchy observer is multiplicative on every word whose Mellin
frequencies remain in one cone. This explains the exact descent in Entry
3925 from the one-sided raw Euler power algebra to powers of `diag(p^-1)`.

Reciprocal Fourier--Tate sewing introduces the opposite cone. A word
containing frequencies of both signs can partially cancel before the absolute
value is taken. Then the observer of the composite is larger than the product
of the separately observed pieces.

The smallest witness is `v=-u`:

\[
\delta(u,-u)=1-e^{-|u|}>0
\qquad (u\ne0).
\]

Thus observer multiplicativity fails already in one forward--backward
two-step loop.

## Operator form

Let a labelled path carry successive frequency increments

\[
u_1,\ldots,u_n.
\]

Observing only after composition gives the scalar weight

\[
e^{-|u_1+\cdots+u_n|/2},
\]

whereas observing each segment first gives

\[
e^{-(|u_1|+\cdots+|u_n|)/2}.
\]

Their difference is nonnegative and is strictly positive exactly when the
path contains cancellation between the two oriented cones. Hence the defect
is supported on mixed-sector words.

For matrix-valued transports this scalar kernel weights the labelled path
expansion. Positivity of the scalar defect does not automatically make the
full matrix residual positive: coefficients and adjoint pairing must still be
derived from the source. The claim here is the exact frequency kernel, not a
completed operator inequality.

## Consequence for the completion square

The observer--completion cell separates into two parts:

```text
one-sided Euler words: strict multiplicativity, no anomaly
mixed reciprocal words: positive Cauchy multiplicativity defect
```

Therefore the BSY anomaly cannot originate inside either isolated Euler
chart. It must be carried by the mixed Fourier--Tate sewing sector, including
its endpoint and archimedean boundary terms.

This is the first source-native candidate for the missing anomaly current:
sum the mixed-word defects with their complete labelled theta--Tate
coefficients before taking a scalar trace. The hostile test is immediate. If
a proposed completion omits mixed words, its observer square commutes
trivially and has no RH force. If it includes them but loses their labels,
scalar cancellation may manufacture either sign.

## Deutsch--Popperian target

Construct the completed mixed-word packet and prove that its source-derived
coefficient pairing turns the nonnegative kernel `delta` into exactly the BSY
divisor entropy. Then determine whether theta modular sewing forces that
packet to vanish.

The first equality would explain where the anomaly lives. The second would
be the RH-bearing conservation theorem. They must remain separate.

## Scope

This packet proves the exact one-sided multiplicativity and mixed-sector
defect of the Cauchy observer. It does not derive the completed mixed-word
coefficients, identify their trace with BSY, prove their vanishing, or prove
RH.
