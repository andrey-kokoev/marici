# Order-bound growth certificate

Owner: `marici.Figueiredo`.

## Question

WP172 used a source period bound. This packet weakens the required source datum:

If the source only bounds the total order of finite two-port closures by `K`,
can finite recurrence growth still certify infinite closure?

## Frozen Domain

- State domain: `Z^2` versus rectangular finite tori
  `(Z/n1Z) x (Z/n2Z)` with `n1,n2 >= 2` and `n1 n2 <= K`.
- Probe family: Cayley-ball growth in the labelled generators.
- Audited order cap: `K=64`.

## Exact Claim

A radius-`R` growth window is fooled whenever both finite periods satisfy
`n1,n2 > 2R`, because the radius-`R` diamond still embeds without wrapping.
Therefore an order cap `K` defeats all hostile finite tori exactly when no
such pair can fit under the cap:

`(2R+1)^2 > K`.

The least certificate radius is the least integer `R` satisfying that
inequality.

For `K=64`, the least certificate radius is `R=4`. Radius three still fails:
`(Z/7Z)^2` has order `49 <= 64` and matches `Z^2` through radius three. At
radius four it separates.

## Disposition

This is a weaker and more plausible source gate than WP172's period cap. A
source finite-order cap plus a recurrence-growth instrument to the derived
radius gives a conditional finite-versus-infinite selector. Without the cap,
WP171 still governs.

It remains weaker than source identification. Many finite tori can share
growth prefixes and even closure order. The selector only decides whether the
closure is in the infinite class relative to the bounded finite domain.

## Exact Checker

- Checker: `checkers/wp173_order_bound_growth_certificate.py`
- Result: `results/wp173_order_bound_growth_certificate.json`

The checker enumerates all rectangular rivals with `n1 n2 <= 64`, verifies
separation at radius four, verifies the sharp hostile radius-three pair
`(Z/7Z)^2`, and checks the order-cap law through `K=100`.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: prefer source order/volume bounds over period bounds if
  flavor dynamics naturally supplies finite state-space size.

## Report to `marici.Nima`

- Admitted state domain: `Z^2` versus finite rectangular two-port tori with
  total order at most `K`.
- Faithful quotient coordinate: Cayley-ball growth through the certificate
  radius.
- Source-authorized probe family: conditional recurrence-growth windows.
- Contextual partition: with `K=64`, all finite rivals separate from `Z^2` by
  radius four.
- Classification: conditional finite-versus-infinite selector under a source
  order cap.
- Smallest exact falsifier to radius-three certification: `Z^2` versus
  `(Z/7Z)^2`, order `49`, matching through radius three.
- Remaining physical-instrument gate: derive the finite-order cap and execute
  recurrence growth to the radius determined by `(2R+1)^2 > K`.
