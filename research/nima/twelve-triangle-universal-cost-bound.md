# No universal arrow cost follows from packet count and record dimension alone

## Claim

There is no unavoidable arrow count determined solely by a packet-vector decomposition into `n` records of internal dimension `r`. The decomposition fixes the ambient dimension `N=nr`; it does not fix a linear map, an allowed circuit class, or what counts as a primitive operation. Consequently

\[
C(n,r)=nr^2+rn^2+(nr)^2
\]

is an exact count for the specified dense local / dense componentwise transport / dense full-vector feedback realization, not a universal lower bound.

## Proof by counterexamples

Fix any `n,r >= 1`, and `N=nr`.

1. **Zero map.** If the target operation is unconstrained, the zero map has empty support and needs zero nonzero-coefficient arrows. Thus no positive lower bound depending only on `n,r` can apply to all packet-vector maps.
2. **Identity map.** With the `N` visible coordinates as ports, the identity uses exactly `N` straight wires. Its cost is `N`, rather than `C(n,r)`. If a convention excludes wires or charges them differently, that convention is additional model data.
3. **Dependence on the target.** Maps on the same `N`-dimensional carrier can have different support and factorizations. Therefore dimensions alone cannot determine their minimum implementation size. Even requiring a nonzero map does not recover the proposed three dense-stage count: a rank-one projector can be factored through a one-dimensional auxiliary port.

The first example already proves the universal-lower-bound claim impossible as stated. This is a scope result, not an assertion that arbitrary circuit-complexity lower bounds are easy once a target and model are specified.

## Target-specific result already established for the tetrahedral projector

For the particular nonzero rank-one collective projector `N=u u^dagger/80` on the 36 visible ports, the audited comparison gives:

- `72` arrows as the exact minimum for a two-pass factorization through a disjoint auxiliary interface of arbitrary dimension;
- `73` arrows as the exact minimum for a three-stage, no-bypass factorization with disjoint stages and arbitrary intermediate dimensions;
- `1836` arrows for the original dense `L`, `G`, `N` three-stage realization.

The 72/73 bounds are attained by one-dimensional collective-mode interfaces. They preserve the complete input/output projector, not merely its action on the collective eigenline. The 1836 realization is pruning-minimal only when its weights and graph are held fixed; it is not implementation-size-minimal in either factored class.

Checker: `research/nima/checkers/check_twelve_triangle_net_minimality.py`.
Latest run: passed; confirmed the fixed-weight pruning result and the attained 72/73 bounds.

## What would make a universal bound a well-posed theorem?

Specify at least:

1. the target map or the required family of maps and whether equality is required on the full input space;
2. the allowed coefficient field and primitive gates (including whether a nonzero matrix entry costs one arrow);
3. permitted auxiliary dimensions, stages, bypasses, feedback, fan-out, and cancellations;
4. whether intermediate maps must be preserved separately or only their composite;
5. whether geometric, symmetry, positivity, or equivariance constraints are mandatory and how they are tested.

Only after fixing these data can one ask for an implementation-specific lower bound. The dimensions `(n,r)` alone prove no such positive cost.
