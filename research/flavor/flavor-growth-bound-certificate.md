# Growth-bound certificate

Owner: `marici.Figueiredo`.

## Question

WP171 proved that a finite recurrence-growth window cannot uniformly certify
infinite closure without a finite-size bound. This packet tests the positive
boundary:

If the source bounds square finite-torus periods by `B`, what growth radius is
necessary and sufficient to separate them from `Z^2`?

## Frozen domain

- State domain: `Z^2` versus square finite tori `(Z/NZ)^2` with `2 <= N <= B`.
- Probe family: Cayley-ball growth in `+e1,-e1,+e2,-e2`.
- Audited bound: `B=8`.
- Instrument resource: maximum recurrence-growth radius.

## Exact claim

The radius-`R` ball in `Z^2` injects into `(Z/NZ)^2` exactly while `N > 2R`.
Therefore `(Z/NZ)^2` first differs from `Z^2` at radius `ceil(N/2)`.

If the source supplies a period bound `B`, then observing growth through
radius `ceil(B/2)` separates every finite square-torus rival with `N <= B`
from `Z^2`. The bound is sharp because `(Z/BZ)^2` still matches through
radius `ceil(B/2)-1`.

For `B=8`, the certificate radius is four. At radius four:

- `Z^2` growth is `41`;
- `(Z/8Z)^2` growth is `39`;
- the first difference is exactly two missing antipodal boundary points.

## Disposition

This is the recurrence-growth analogue of WP168. It becomes a conditional
selector only after the source supplies the finite period bound. It is not a
complete finite-source identifier, and it does not override WP171 without that
source bound.

Selector authority factors as:

`source period bound B -> recurrence instrument to radius ceil(B/2) -> finite-versus-infinite closure readout`.

The live physical gate is still the first arrow plus executable recurrence
depth.

## Exact checker

- Checker: `checkers/wp172_growth_bound_certificate.py`
- Result: `results/wp172_growth_bound_certificate.json`

The checker computes finite-torus Cayley balls by breadth-first search,
verifies every square torus with `2 <= N <= 8`, proves the sharp hostile case
`N=8`, and checks the same law through period bound fourteen.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `8/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `8/10`.
- Frozen optionality: search for source period/diameter bounds and for a
  recurrence-growth instrument with radius budget tied to that bound.

## Report to `marici.Nima`

- Admitted state domain: `Z^2` versus square finite tori with source period
  bound `B`.
- Faithful quotient coordinate: Cayley-ball growth sequence through
  `ceil(B/2)`.
- Source-authorized probe family: conditional recurrence-growth windows.
- Contextual partition: all finite tori with `N <= B` separate from `Z^2` by
  radius `ceil(B/2)`.
- Classification: conditional finite-versus-infinite selector under a source
  period bound.
- Smallest exact falsifier to under-radius certification: at `B=8`, `Z^2`
  versus `(Z/8Z)^2` still match through radius three.
- Remaining physical-instrument gate: derive `B` and execute recurrence growth
  to radius `ceil(B/2)`.
