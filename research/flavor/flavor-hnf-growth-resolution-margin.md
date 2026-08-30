# HNF growth-resolution margin

Owner: `marici.Figueiredo`.

## Question

WP175 corrected the noiseless recurrence radius after expanding the finite
quotient domain from rectangular products to arbitrary HNF quotients. This
packet recomputes the detector-resolution margin on that corrected domain.

## Frozen domain

- State domain: `Z^2` versus all finite quotients `Z^2/L` with index at most
  `64`.
- Coordinate: Hermite normal form `(a,b,d)`.
- Probe family: Cayley-ball recurrence growth.
- Detector model: absolute count error `tau=1`.

## Exact claim

On the arbitrary-HNF quotient domain, the WP175 noiseless certificate radius
`R=5` has minimum deficit only `1`. The unique worst quotient is HNF
`(10,5,6)`, index `60`.

With `tau=1`, radius five is not robust. Strict interval separation requires
`d_min(R) > 2 tau`.

At radius six, the minimum deficit is `21`, so `tau=1` is robust. The first
error-robust radius is therefore six.

## Disposition

WP174's radius-five detector margin was valid for the rectangular domain, not
for arbitrary finite quotients. Once the legal state domain expands, the
instrument margin must be recomputed.

For `K=64`:

- rectangular, exact: radius four;
- rectangular, `tau=1`: radius five;
- arbitrary HNF, exact: radius five;
- arbitrary HNF, `tau=1`: radius six.

This is the cleanest current statement of domain-relative physical
faithfulness for recurrence growth.

## Exact checker

- Checker: `checkers/wp176_hnf_growth_resolution_margin.py`
- Result: `results/wp176_hnf_growth_resolution_margin.json`

The checker enumerates all `3403` HNF quotients of index at most `64`, computes
minimum growth deficits at radii five through seven, and verifies that
`tau=1` first becomes robust at radius six.

## Calibration

- Pre excitement: `10/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `10/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: detector margins are part of the quotient-domain
  definition; never port a margin across a domain expansion.

## Report to `marici.Nima`

- Admitted state domain: arbitrary HNF finite quotients of `Z^2` with index at
  most `64`.
- Faithful quotient coordinate: recurrence-growth counts with error intervals.
- Source-authorized probe family: conditional growth windows after source cap,
  quotient-domain law, radius, and count error are typed.
- Contextual partition: at `R=5,tau=1`, HNF `(10,5,6)` remains too close; at
  `R=6,tau=1`, all admitted finite quotients separate from `Z^2`.
- Classification: corrected conditional selector with detector margin.
- Smallest exact falsifier to noisy radius-five certification: HNF
  `(10,5,6)`, index `60`, deficit `1`.
- Remaining physical-instrument gate: derive legal quotient domain, order cap,
  recurrence radius, and count-resolution calibration from source dynamics.
