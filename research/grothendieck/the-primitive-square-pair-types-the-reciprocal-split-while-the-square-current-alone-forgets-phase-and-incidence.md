# The primitive-square pair types the reciprocal split while the square current alone forgets phase and incidence

## Reciprocal quadratic with a phase bit

Let

\[
Q_{\sigma,c}(r)=r^2+\sigma cr+1,
\qquad c>0,
\qquad \sigma\in\{-1,+1\}.
\]

Write

\[
Q_{\sigma,c}(r)
=(r+\sigma\alpha)(r+\sigma\alpha^{-1}),
\qquad
\alpha+\alpha^{-1}=c.
\]

After removing the leading monomial and putting `u=r^{-1}`, the connected
logarithmic coefficients are

\[
a_k
=\frac{(-1)^{k+1}\sigma^k}{k}
(\alpha^k+\alpha^{-k}).
\]

In particular,

\[
a_1=\sigma c,
\qquad
a_2=1-\frac{c^2}{2}.
\]

The square grade determines the discriminant

\[
c^2-4=-2(a_2+1),
\]

but is blind to `sigma`. The primitive grade carries that missing phase bit.
For `sigma=+1`, the off-unit roots cross through `r=-1`; for `sigma=-1`, they
cross through `r=+1`.

## Numerator versus denominator incidence

If the same quadratic occurs with incidence `eta` in a determinant section,

\[
Q_{\sigma,c}(r)^\eta,
\qquad \eta\in\{-1,+1\},
\]

then its observed connected grades are

\[
b_1=\eta\sigma c,
\qquad
b_2=\eta(1-\tfrac12c^2).
\]

Changing numerator to denominator reverses both grades without moving the
quadratic roots. A scalar square current therefore cannot decide whether a
local divisor is a zero of the section or a pole of its carrier.

Away from the exceptional value `c=sqrt(2)`, the typed pair `(b_1,b_2)` and
the declared factor incidence recover all three data:

```text
magnitude c
phase sigma
zero-versus-pole incidence eta
```

At the exceptional value the square grade vanishes and a third connected
grade or an independently retained incidence tag is required.

## Correction and consequence

The preceding minimal-family theorem remains correct within its fixed
positive-numerator orientation. Its global interpretation must be narrowed:
the square current is the radial order parameter only after phase and
incidence have been typed.

This explains the necessity of the coupled primitive and square boundary
packet. The global theta bridge cannot map a scalarized `k=2` current directly
to zero confinement. It must preserve:

1. the primitive phase channel;
2. the square discriminant channel;
3. determinant incidence distinguishing section zeros from carrier poles;
4. reciprocal-chart coherence.

Local Euler/Tate factors make this distinction unavoidable: their reciprocal
off-unit singularities belong to an invertible transition or denominator
presentation, not to the completed section's zero divisor.

## Durable verification

- Checker: `checkers/check_primitive_square_split_typing.py`
- The checker verifies phase blindness of grade two, phase recovery by grade
  one, incidence reversal, and the common discriminant for exact rational
  witnesses.
