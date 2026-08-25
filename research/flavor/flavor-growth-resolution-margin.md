# Growth-resolution margin

Owner: `marici.Figueiredo`.

## Question

WP173 gives an exact recurrence-growth certificate under a source finite-order
cap. That certificate assumes exact growth counts. This packet adds the next
physical instrument gate:

How much recurrence radius is needed when the growth count has bounded absolute
error?

## Frozen domain

- State domain: `Z^2` versus rectangular finite tori
  `(Z/n1Z) x (Z/n2Z)` with `n1 n2 <= K`.
- Source cap: `K=64`.
- Probe family: Cayley-ball growth in the labelled generators.
- Detector model: absolute count error at most `tau=1`.

## Exact claim

Let

`d_min(R) = min_finite [ growth_Z2(R) - growth_finite(R) ]`

over the finite rivals admitted by the order cap. With absolute error at most
`tau` on both the infinite and finite readouts, strict interval separation
requires

`d_min(R) > 2 tau`.

For `K=64`, WP173's noiseless certificate radius is `R=4`. At that radius the
minimum deficit is only `2`, realized by `(Z/7Z)x(Z/9Z)`, `(Z/8Z)^2`, and
`(Z/9Z)x(Z/7Z)`. With `tau=1`, the intervals touch, so the selector is not
robust.

At radius `R=5`, the minimum deficit rises to `10`, so `tau=1` is robust.

## Disposition

The recurrence-growth selector now has three independent gates:

`source order cap K -> executable radius R -> calibrated count resolution tau`.

WP173 supplies the noiseless radius. WP174 supplies the resolution margin. A
physical claim needs both; exact integer growth is a hidden instrument
assumption if not stated.

## Exact checker

- Checker: `checkers/wp174_growth_resolution_margin.py`
- Result: `results/wp174_growth_resolution_margin.json`

The checker enumerates all rectangular rivals with `n1 n2 <= 64`, computes
minimum finite deficits at radii four through six, verifies that `tau=1` breaks
radius four, and verifies that radius five is the first robust radius.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: every proposed recurrence-growth selector must publish
  its detector error model and margin, not only its formal radius.

## Report to `marici.Nima`

- Admitted state domain: `Z^2` versus finite rectangular tori with order cap
  `K=64`.
- Faithful quotient coordinate: recurrence-growth counts with declared error
  intervals.
- Source-authorized probe family: conditional growth windows, if the source
  cap and instrument resolution are derived.
- Contextual partition: at `R=4,tau=1`, the decisive intervals are not
  disjoint; at `R=5,tau=1`, all finite rivals separate from `Z^2`.
- Classification: conditional selector only with source cap, executable
  radius, and calibrated resolution.
- Smallest exact falsifier to noisy radius-four certification: `(Z/8Z)^2`
  and the rectangular rivals `(7,9),(9,7)` have deficit only `2`.
- Remaining physical-instrument gate: derive the count error `tau` and operate
  at a radius satisfying `d_min(R)>2 tau`.
