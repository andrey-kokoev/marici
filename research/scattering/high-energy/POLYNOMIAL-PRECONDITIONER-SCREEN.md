# H6 — polynomial defect screen and bounded-attempt closure

A failure of ||E||<1 for E=I-MA does not rule out a polynomial inverse certificate. Set

    B_k=(I+E+...+E^(k-1)) M.

Then I-B_k A=E^k exactly. A **verified upper** bound ||E^k||<1 plus a bound on B_k would give ||A^-1||<=||B_k||/(1-||E^k||), without requiring ||E||<1. This is a different lead from the previously rejected one-step contraction.

The checker fixes k=1,...,8 before running and applies powers to the four stored corrected columns, using the source finite-response Woodbury defect. No entrance solve is repeated and no response direction is added. Action/input ratios are numerical lower diagnostics for the operator norm: a ratio above one is evidence against that power's contraction; all four ratios below one would only identify a possible target, never certify an upper bound on all directions. The full-band and arithmetic gates remain.

## Measured result

Every tested power has all four measured action/input ratios above one. The maximum grows from about 1.2017 at k=1 to about 19,776 at k=8. None supplies a plausible Euclidean Neumann contraction lead for this source preconditioner. These are floating action measurements, not a directed norm certificate or a proof that every possible polynomial/preconditioner fails. A successor should choose a different inverse/sensitivity method rather than blindly extend this fixed power series.

## Attempt closure

This is the sixth and final cycle of the original H6 certification attempt. Outcome: **inconclusive**, not a refutation. Stored-kernel comparisons with exact stored-grid preparation and its peak movement are certified below 1%, but fixed-response solver/kernel/reference errors remain unenclosed. The final forecast 0.05 accepted / 0.02 rejected / 0.93 inconclusive is historical; the observed bounded outcome is inconclusive.

H6 stays open. H7 also stays open with its own exhausted budget. Neither gets an automatic renewal. A successor must explicitly choose, cost and forecast a nonredundant certificate protocol, using the accumulated screens to avoid dead routes. Unknown successor cost/forecast should not be replaced by the exhausted attempt's last-cycle estimate. H8's positive-premise blockers remain unchanged.

Replay in the source replay environment:

    python research/scattering/high-energy/check_polynomial_preconditioner.py --check
