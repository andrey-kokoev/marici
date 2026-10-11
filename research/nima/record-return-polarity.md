# The inherited agreement-fixing comparison selects positive exchange polarity

## Audit before selecting

Fix the previous record adapter, C, R, L and metric. Compare readable-port exchanges

    E_s(x,t) = (s Ct, s C^T x + (I-C^T C)t),   s=+1 or -1.

Both versions of U_s=E_s diag(R,L) pass exact orthogonality, inverse recovery, order-six return and fixed-space dimension-six tests. Both distinguish the ordinary and twisted tetrahedral fixtures, with opposite signed outputs. Conservation and recurrence alone therefore do not select the polarity.

Unlike the earlier left/right-factor alternatives, they are not intertwined by any transformation preserving the declared observation O(x,t)=(x,Ct). After one step the bank readout is s R x, independently of t. If S preserves O and S U_+=U_- S, applying the bank readout gives Rx=-Rx for every x. The scalar unit is a counterexample. This argument does not assume S linear; it applies to the stated calibrated full-vector observation, not every possible coarser readout.

## Recover the actual source condition

The prior source `comparison-update-dynamics-and-energy-normalization.md`, section “Exact memory lift of the projection”, supplies

    q_next = q + r(z-a),    z_next = a,
    a = r^T q / (r^T r).

The stored z has the SAME coordinate units as a. When z=a, the discrepancy is zero and this comparison leaves the state unchanged. This is already a property of the reused source operation, not a new fitted criterion.

In the multi-component port adapter, write an agreed bank as

    t = C^T x + k,   Ck=0.

Then Ct=x and the positive exchange satisfies

    E_+(x,t) = (x,t).

The negative candidate instead gives (-x,-C^T x+k), changing every such state with nonzero x. It fails the inherited agreement-fixing condition.

The checker tests this on all four carrier basis vectors and sixteen projected kernel generators, alongside the algebraic identity above. The condition applies to the exchange stage AFTER its inputs are presented; it does not assert that the complete cycle's separately supplied rotations leave every agreed input fixed.

## Disposition

Positive polarity is selected **among these two candidates** when faithfully extending the prior same-coordinate comparison law. The negative candidate is a useful countermodel to conservation-only selection, but not an equally faithful implementation of that source convention.

This is concrete progress on source-relative selection. It is not a proof that WG uniquely selects every feature of the full dynamics: the adapter, metric, rotation schedule, richer multi-port mixing and physical interpretation remain separate choices. Nor does it derive the old gravitational coefficients. If a different observation or signed-coordinate convention is proposed, its full adapter and agreement meaning must be transported explicitly rather than changing only a sign in the update.

## Verification

`python research/nima/checkers/check_record_return_polarity.py` passed with exact Fraction matrices, inverse products, powers, fixed-space ranks, tetrahedral-response controls and agreement-fixing tests. Results: `results/record-return-polarity.json`, including source digests and the inherited source locator.

No prior update implementation was modified. No ledger entry, commit or publication is claimed.
