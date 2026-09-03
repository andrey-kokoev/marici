# Universal ordered-triple horn

## Question

Can the geometric horn be constructed universally without an already materialized global carrier?

## Claim boundary

Yes at relative top weight. Let `C` carry a rank-three normal bundle with ordered splitting

`N^vee=L1 plus L2 plus L3`.

Blow up the zero section of `Tot(N)`. The exceptional `P(N)` has three coordinate hyperplanes forming a labeled triangle. Fiberwise and globally in the dual complex,

`Gamma=[E,D1,D2]+[E,D2,D3]+[E,D3,D1]`

has boundary `sigma123`.

Local ratios `u=l1/l3` and `v=l2/l3` define a global relative logarithmic form because transition units come from `C` and vanish under the relative differential. Hence

`d Phi(Gamma)=(Xi_rel,-sigma123)`.

The construction commutes with base change of ordered split normal bundles. Forgetting the order retains it with coefficients in the orientation sign local system.

Local integral tame tuples also descend at the valuation level, but their K2 symbols differ on overlaps by base-unit symbols; full integral descent requires a Cech–Gersten cocycle.

## Disposition

The top-weight `HomotopyLift` is universal. Any future carrier map into the ordered-transverse-triple category pulls it back. The next leaf constructs or obstructs the full integral descent cocycle.

## Verification

- `research/voevodsky/check_cosmology_universal_ordered_triple_horn.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
