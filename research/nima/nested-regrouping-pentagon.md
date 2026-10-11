# Regrouping coherence requires a weighted representative

## Question

Instead of adding another witness slot, compare different groupings of the same four ordered marked inputs. Do the two reassociation routes from (((ab)c)d) to (a(b(cd))) agree on the representative and retained comparison coordinates? Active obligation: regrouping coherence and readout descent.

## Representation and construction

A component carries a constituent count w and a barycenter c. For disjoint sets of the declared equal-weight primitive occurrences, merge by

\[
(w_L,c_L),(w_R,c_R)\longmapsto
\left(w_L+w_R,\frac{w_Lc_L+w_Rc_R}{w_L+w_R}\right).
\]

The count is not physical mass. Shared or repeated inputs require their own occurrence/overlap accounting; this test uses four distinct marked leaf occurrences exactly once each.

For a merge of p left leaves and q right leaves, the comparison normal has entries q on the left group and -p on the right. Its squared norm is pq(p+q). The three postorder merge normals of any binary tree are mutually orthogonal. The same reversible projection lift as the prior construction retains one mismatch coefficient at each merge, reaches the uniform four-leaf barycenter and reconstructs the input from that center and its records.

Different trees have different record metrics. The canonical nested tree has diagonal (2,6,12), while the balanced tree has (2,2,4). Consequently a valid comparison transports the metric along with the record coordinates rather than assuming identical coordinate norms.

## Exact pentagon

The five bracketings are

    A = (((ab)c)d)
    B = ((a(bc))d)
    C = (a((bc)d))
    D = (a(b(cd)))
    E = ((ab)(cd)).

The exact record maps satisfy

\[
T_{CD}T_{BC}T_{AB}=T_{ED}T_{AE}=T_{AD}.
\]

All 25 frame maps are invertible and preserve the transported quadratic form; all 125 indexed triple compositions agree. Exact linear-basis checks verify the corresponding readout identities for arbitrary real input coordinates. These are identities of the specified linear realization, not a theorem identifying all native histories.

## What breaks if weights are omitted

For input (1,2,4,8), the weighted representative is 15/4 in every bracketing. Taking an unweighted midpoint of the two child representatives instead gives:

| Bracketing | Unweighted result |
|---|---:|
| A | 43/8 |
| B | 5 |
| C | 13/4 |
| D | 5/2 |
| E | 15/4 |

Thus a bare center is insufficient for regrouping as though all bracketings represented the same constituent mean. The earlier history-weighted midpoint readout is not thereby invalid: it deliberately weights construction routes differently. It simply cannot also be asserted to be invariant under this reassociation without changing its weighting rule.

## Disposition and verification

The working representative must carry its aggregation weight alongside its linked witness record if downstream regrouping is intended to preserve the constituent barycenter. The paths remain distinct records, but both sides of the pentagon give the same record-coordinate transformation. No spatial volume, atomic mass or new native physical interaction is inferred.

`python research/nima/checkers/check_nested_regrouping_pentagon.py` passed via `structured_command_execution:e_32876_1791228406099265000_52`. Results: `results/nested-regrouping-pentagon.json`. No commit or publication is claimed.
