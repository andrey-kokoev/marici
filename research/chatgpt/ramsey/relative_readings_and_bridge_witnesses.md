# When an old link determines a new row

**2026-11-18. Result:** Given the relative readings within a new row, an old positive link can determine the orientation of the whole row. It does not supply the relative readings. [Ledger entry 4334](../../../src/ledger/20261118-4334%20Witness%20in%20Place%20of%20a%20Bridge%20Reading.md).

## Representation

Use an undirected binary relation with no loops. For two pairs that share an address, record 0 if their bits agree and 1 if they differ. An ordered chain through all 190 pairs on 20 addresses needs 189 comparisons. Read alternate upper-triangle rows backward to keep a shared address at each step. One known pair value then fixes the other 189 by successive XOR. Without it, simultaneous reversal gives the other possible reading. The balanced address order is not required. This is a change of representation, not a reduction in the number of bits.

More generally, for consistent comparisons, each connected component needs one orientation bit. Adding one address to n old addresses gives n new pairs incident to it. Use n−1 comparisons to connect them and one bridge comparison to the old component. The bridge fixes their orientation relative to the old readings.

## Certificate in the 22-address example

Start with an anchored 20-address record. Append addresses 20 and 21 (labels start at 0). Keep the original 189 comparisons and add 19 and 20 comparisons internal to the two new rows. Each row also has a bridge to the old pair (0,1). With both bridges there are 230 comparisons; each of the 231 possible anchors recovers the same matrix. Without either bridge, four relative-record completions remain when the old matrix is fixed. These are readings, not four valid witnesses.

The old pair (0,1) is positive. In each new row the internal comparisons imply that the links to 0 and 1 agree. If both were positive, they would complete a positive triangle. Thus both must be negative. The same old pair fixes both orientations. Among the four completions only the original avoids both a positive triangle and a negative seven-set.

## General rule and limit

A connected record of internal comparisons partitions a row into two classes of addresses with equal readings. If a class contains both ends of an old positive link, that class cannot be positive in a triangle-free extension. If exactly one class contains such a link, the triangle condition determines the orientation. If both do, neither orientation works. If neither does, this condition cannot decide. Other forbidden patterns must still be checked.

**Next construction question:** derive the partition from the old relation before measuring the new row. The current decoder orients a given partition. It does not predict the partition or prove a Ramsey threshold. Nor does the example imply that a search for a certificate costs less than a direct bridge reading.

## Findings before the bridge test

These are different tasks. A small representation need not give a rule for constructing the next address.

| Task | Result | Scope and evidence |
|---|---|---|
| Count information | A symmetric binary matrix with 20 named addresses and a fixed diagonal has 190 free bits. If only the isomorphism class matters, the worst-case fixed-length index is 129 bits. | These are capacities over all graphs, not the size of this one file. They do not determine the number of comparisons a search needs. |
| Order addresses | Ten pivots tie for the minimum initial sign-count difference (6 positive, 13 negative). Reordering both axes preserves every link. | [Balance test](ramsey_min_diff_order.py). Balance is not a requirement of the decoder. |
| Choose address 21 | The tested 20-address prefix has five legal columns. None is within one bit of an old row (minimum distance: five). No single eigenvector cutoff found one; pairs of eigenvectors could separate all five after the answers were known. Two rounds of degree-difference grouping retained four; direct greedy coverage could also fail at a tie. | [Column tests](ramsey_next_column_three_tests.py), [one-vector test](ramsey_spectral_next_address.py), [two-round test](ramsey_difference_quotients.py). Separation after the fact is not prediction. |
| Choose two addresses | Of 15 unordered pairs of legal columns, including repeats, only one extends this prefix to 22. Either insertion order works. Address 6 rules out a positive link between the two new addresses in all 15 cases. | [Pair test and certificates](ramsey_20_pair_blockers.py). The pair is forced here; the first column is not. |
| Recover missing data | Among the 231 two-address deletions of one 22-address graph, 190 admit one completion and 41 admit two, up to exchange of the new addresses. All 41 hide link 0–6, whose sign can change without a forbidden set. | [Hidden-link check](ramsey_hidden_link_audit.py). In the ambiguous cases, construction does not require recovery of the original bit. |
| Explain a quotient | Neither member of the successful pair is an XOR of old columns, but their difference is. For a six-regular completion its difference is the vector of old degree parities. Degree deficits and triangle exclusion construct the pair in this example. | [XOR test](ramsey_xor_address_test.py), [degree split](ramsey_degree_split.py). Six-regularity is an extra assumption, not a Ramsey condition. |
| Test a proposed interface | Two distinct valid states can give the same four readings for a named witness but disagree on a named next move. Two mixed queries can share one index when they use the same B group. | [Substitution counterexample](ramsey_interface_substitution.py). [Index audit](ramsey_interface_index_probe.py). Efficient lookup and sufficient information for continuation are distinct claims. |

**Conjecture, not finding:** [20 comparisons plus three interface positions](ramsey_37_comparison_interface_conjecture.md). The later interpretation `(7+3)+(7+3) → 2 → 1` counts reports in a computation. Neither interpretation identifies those positions with 23 distinct addresses. The [earlier consolidated note](ramsey_relational_construction_consolidated.md) covers the separate Ramsey witness and obstruction work.

## Checks

- [Two-step growth checker](ramsey_relative_growth_two_steps.py): keep or cut each bridge; test every anchor.
- [Validity checker](ramsey_bridge_cut_validity.py): test all four orientations against both forbidden patterns.
