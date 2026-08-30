# Li Möbius rigidity packet

## Grothendieck source

This packet formalizes `research/grothendieck/li-mobius-coordinate-rigidity.md`.

After the pole-at-zero condition gives `d = 0` and normalization at infinity
gives `c = a`, the coordinate has the form

`(a*s+b)/(a*s)`.

The cross-multiplied reflection-to-inversion law is represented by
`ReflectionInverts a b`. Evaluation at `s = 0` gives

`(a+b)*b = 0`.

The nonconstant condition is exactly `b != 0`, so `b = -a`. Away from the
endpoint, `liMobius_coordinate_rigidity` identifies the coordinate with
`1 - 1/s`.

## Assumptions and coefficient type

- Coefficients lie in an arbitrary field `K`.
- `a != 0` is required for a genuine denominator and for rational-function
  evaluation away from the endpoint.
- `s != 0` is required only for the evaluated coordinate equality.
- `b != 0` is the nonconstancy premise.

The coefficient theorem itself does not need `a != 0`; it isolates exactly
what follows from reflection plus nonconstancy after the endpoint and infinity
normalizations have already been applied.

## Hostile omitted-premise model

With `b = 0`, the coordinate is identically one wherever defined and still
satisfies the cross-multiplied reflection law. Therefore reflection, endpoint
placement, and infinity normalization do not imply the Li coordinate unless
nonconstancy is retained.

## Scope boundary

This is coordinate rigidity only. It does not prove positivity of the Li
cone, positivity of an explicit formula, zero confinement, or RH.

## Verification boundary

Static placeholder checks are permitted. Lean elaboration is withheld under
Nima's active no-build instruction.
