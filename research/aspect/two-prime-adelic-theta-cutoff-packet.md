# Two-prime adelic theta cutoff packet

## Construction

The first packet retains primes `2` and `3`, valuation depth two, and both
positive and reciprocal sectors. Each of the four local chains has three
states, giving twelve internal states. Six boundary coordinates are appended:
primitive, prime-square, seam, endpoint, connected-tail, and archimedean.
The total matrix is `18x18`.

Every local block is source-derived from its nilpotent valuation shift. Its
incoming boundary incidence is `e_0`, and its outgoing boundary readout is the
augmentation over the three valuation states. No dense coupling is fitted.

## Result

The computation is immediate in exact symbolic arithmetic. All four local
interiors have determinant one and are acyclic. Prime deletion is therefore
structurally clean.

But the source data generate only one boundary direction. Every chain enters
and leaves through the primitive coordinate. The `6x6` boundary Schur
correction has rank one, and the other five boundary coordinates remain the
identity reference.

This gives a rank-five completion deficit.

Conjugating the boundary by the exact six-point Fourier control spreads the
primitive signal across six displayed coordinates but leaves its rank equal
to one. Optical mixing cannot manufacture the missing arithmetic currents.
The earlier six-port tomography was therefore correctly dimensioned as a
lower-bound detector, but its six labels were not yet six source-generated
directions.

## Implication

The completed adelic operator is not computationally obstructed. The first
exact packet is tiny. It is source-obstructed: five independent incidence maps
are absent.

The required next additions are not more primes. They are source constructors
for prime-square, seam, endpoint, connected-tail, and archimedean incidence,
each independent of the primitive column. Until those appear, increasing the
prime cutoff merely enlarges the same rank-one boundary image.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_two_prime_adelic_theta_cutoff_packet.py
```
