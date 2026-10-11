# Full-state agreement, not retention alone, fixes the unread complement

## Test

The preceding uniqueness theorem assumed that the exchange leaves unread bank components untouched. Test whether lossless retention implies that condition.

For t=C^T a+k, with Ck=0, compare

    E_s(x,t)=(a,C^T x+s k),    s=+1 or -1.

The negative option reverses unread data without destroying it. Both complete updates E_s diag(R,L) preserve the positive budget, have exact inverses and order six, reproduce the empty-bank projection, and fix pure-readable agreement states (x,C^T x). Both also give the same first-step witness-sensitive tetrahedral response.

They are nevertheless observably different after two cycles:

    x_after_two = s C t_initial.

For the existing ordinary/twisted banks, the original law gives +1/2 at the second step; the unread-negating candidate gives -1/2. These identities hold over the full numerical state space, as checked by exact matrix multiplication. A transformation preserving O(x,t)=(x,Ct) cannot intertwine the laws, because applying the two-step carrier identity would force Ct=-Ct for every bank.

## Important distinction: two meanings of agreement

The alternative fixes agreement only when the unread complement is absent. It does NOT satisfy the full inherited zero-discrepancy rule:

    Ct=x  implies  E(x,t)=(x,t).

Indeed, for x=0 and any nonzero k in ker C, the readable discrepancy is already zero, but the alternative changes k to -k. The checker explicitly verifies this counterexample and its reversibility.

Consequently the unread-fixing condition in the uniqueness theorem is not an independent extra assumption if agreement means agreement of the WHOLE exchange state. Set x=0 and t=k in the full-agreement rule to obtain E(0,k)=(0,k).

This matches the existing source memory-lift formula: its update vanishes at zero comparison discrepancy. It should not be weakened silently to a rule about the active projection alone. It applies to the exchange stage; the separately declared prior bank rotation may still move hidden records into the readable port before that exchange.

## Sharpened selection statement

Given the port C and its metric, the previous uniqueness argument needs:

- a linear isometry;
- full-state agreement-fixing whenever Ct=x;
- the specified empty-bank projection response.

Those imply the unread-fixing condition and uniquely determine the prior exchange. Mere reversible retention would not suffice. The countercandidate is not adopted and is not presented as another faithful implementation of the full source agreement law.

This clarifies the mechanism: hidden records affect future comparisons through the declared bank mixing, not through an additional unexplained operation at an exchange whose discrepancy is zero. The mixing law, adapter and physical interpretation still require their own selection arguments. No gravitational coefficient follows from these tests.

## Verification

`python research/nima/checkers/check_unread_record_selection.py` passed with exact rational matrices, inverse, period, rank, two-step readout and nonzero unread-record controls. Results: `results/unread-record-selection.json`.

No prior update implementation was changed. No ledger entry, commit or publication is claimed.
