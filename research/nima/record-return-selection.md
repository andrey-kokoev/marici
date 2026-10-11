# Conservation and witnessed return do not select the rotated record factor

## Fixed setup

Keep the successful two-edge adapter, Clifford sewing port C, carrier half-turn R, positive coefficient metric and prior exchange operation fixed. Compare the prior bank rotation L_left=R tensor I with L_right=I tensor R. Both preserve the ordered slot labels; they apply the same existing operation to different slots.

For either L, use the same formula:

    x_next = C L t
    t_next = C^T R x + (I-C^T C)Lt.

Right-factor rotation is a countercandidate for this test, not a newly adopted law or a claimed native WG derivation.

## Exact results

Both full twenty-dimensional maps have:

- exact orthogonality and inverse recovery;
- exact order six, with no smaller positive identity power;
- six-dimensional fixed space;
- rank-eight joint record observation (Ct,CLt);
- actual return of a previously unread record into the active carrier;
- the previously demonstrated ordinary/twisted tetrahedral response, +1/2 versus -1/2, with equal initial readout and budget.

The two maps nevertheless differ. On the legal general record-bank input t=1 tensor e1 with the same initial carrier, their next outputs are respectively +e1/2 and -e1/2.

This separating bank belongs to the prior feedback model's general retained-bank domain. It has not been shown to arise from the restricted Boolean tetrahedral adapter. Indeed both maps agree on the ordinary/twisted fixture, so that successful fixture cannot select between them.

## Disposition

The tested requirements do not uniquely select the prior left-factor law, even with the adapter and normalization held fixed. This is not a theorem that every WG selection principle fails, nor a proof that the two descriptions represent inequivalent physics. A permissible change of coordinates might relate them; its compatibility with the fixed source roles and readout would have to be proved.

The next precise selection question is which source operation singles out the acted-on record factor, or whether an admitted readout-preserving equivalence makes that choice inessential. Conservation, finite return and one witness-sensitive example alone do not answer it. No gravitational coefficient is derived by this audit.

## Follow-up

`record-return-equivalence.md` constructs that readout-preserving conjugacy explicitly. The left/right laws give identical observed trajectories when the bank adapter is transported with the signed factor interchange. The fixed-coordinate distinction above remains valid, but is not evidence of inequivalent physical laws by itself.

## Verification

`python research/nima/checkers/check_record_return_selection.py` passed. It uses exact rational 20x20 matrices, inverse products, powers, rank computations and concrete response controls. Results and source digests: `results/record-return-selection.json`.

No prior update implementation was changed. No ledger entry, commit or publication is claimed.
