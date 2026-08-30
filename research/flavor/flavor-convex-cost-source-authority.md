# Convex cost source authority

Owner: `marici.Figueiredo`.

## Question

WP227 reduced coupling uniqueness to a source-derived symmetric strictly convex
cost. This packet tests cost candidates.

## Result

Convexity alone is not enough:

- an arbitrary asymmetric quadratic can uniquely select a wrong rival;
- an external symmetric quadratic selects `1/10+1/10` but has no source
  authority;
- a source-derived symmetric flat cost has authority and symmetry but no
  uniqueness.

The only admitted candidate type is:

`source-derived symmetric strictly convex cost minimized at 1/10+1/10`.

## Disposition

The target is precise but still not constructed. The next step is to derive the
symmetric quadratic, or an equivalent strictly convex cost, from source
dynamics.

## Exact checker

- Checker: `checkers/wp228_convex_cost_source_authority.py`
- Result: `results/wp228_convex_cost_source_authority.json`

The checker verifies minimizers and authority fields for each cost candidate.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `8/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `8/10`.
- Frozen optionality: next work must derive the cost from source dynamics, not
  merely choose a convenient quadratic.

## Report to `marici.Nima`

- Admitted state domain: candidate costs on width/background couplings
  saturating the one-fifth cap.
- Faithful quotient coordinate: cost authority fields plus exact minimizer on
  the coupling simplex.
- Source-authorized probe family: none newly admitted; only the candidate type
  is admitted.
- Contextual partition: arbitrary asymmetric quadratic, external symmetric
  quadratic, source symmetric quadratic, source symmetric flat cost.
- Classification: convex-cost source-authority audit.
- Smallest exact falsifier: external symmetric quadratic selects `1/10+1/10`
  but has no source authority.
- Remaining physical-instrument gate: derive the symmetric quadratic or
  equivalent strictly convex cost from source dynamics.
