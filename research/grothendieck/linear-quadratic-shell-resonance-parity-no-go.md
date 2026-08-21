# Rank-one linear and quadratic shell channels cannot cancel at odd pi

> **Scope correction.** This no-go is internal to the shell-center unitary
> surrogate. It proves that two radial prime phase totals cannot repair their
> own aliasing; it does not assert gamma or Xi singularities.

For the quarter-shifted unit-width shell, the normalized radial average of
the linear height phase is

```
phi_1(T)=e^(-iT/4)sinc(T/2),                          (1)
```

while the quadratic phase average is

```
phi_2(T)=e^(-iT/2)sinc(T).                            (2)
```

Relative to their centered unitary shell phases, the leading discrepancies
have the forms

```
L_k(T)=[sinc(T/2)-1]e^(-iTk-iT/4)/k,
Q_k(T)=[sinc(T)-1]e^(-2iTk-iT/2)/k.                  (3)
```

At an odd resonance `T=(2j+1)pi`, the quadratic outer phase is
`e^(-2iTk)=1`, so `sum_k Q_k(T)` has a nonzero harmonic divergence. The
linear outer phase is `e^(-iTk)=(-1)^k`, so `sum_k L_k(T)` is an alternating
harmonic series and remains bounded.

No fixed linear combination of these rank-one radial channels can cancel a
logarithmic divergence with a bounded term. The actual gamma resolvent is a
different functional calculus and is not part of this parity comparison.

Thus the scalar two-channel shell model fails already at every odd multiple
of `pi`. At even multiples both channels are resonant, but testing their
coefficients is unnecessary for this no-go.

## Required repair

Cancellation needs additional within-shell modes or an auxiliary mapping-cone
resolvent whose frequency content converts the linear channel into the even
harmonics seen by the quadratic channel. This must occur before radial
scalarization. Merely coupling the two scalar shell totals in a `2x2` matrix
cannot change their incompatible shell-frequency parity.

This is a stronger obstruction than independent scalar nonvanishing: even a
coupled rank-two scalar determinant lacks the divergent mode needed at odd
quadratic resonances. The surviving target is operator-valued in the radial
moment/mapping-cone fiber.
