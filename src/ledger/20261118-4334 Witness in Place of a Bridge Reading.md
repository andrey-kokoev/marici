# 4334 — A witness in place of a bridge reading

**Date:** 2026-11-18. **Status:** finite check and conditional rule. **Sequence claim:** `seqclaim-729838560fa2923488843c43`.

Two appended rows each carry internal same-or-different readings. Cutting both bridge comparisons leaves four readings of the 22-address matrix when the original 20-address matrix is fixed. In this example one old positive link, (0,1), fixes both orientations: in each new row the two incident bits agree and cannot both be positive. Only the original reading avoids both forbidden patterns.

This replaces two bridge readings with a certificate under the validity assumption. It does not construct the internal readings from the old matrix. The open problem is to derive the partition of old addresses before observing the new row.

The research note also records the preceding construction tests. On the tested 20-address prefix, five single columns are legal but only one unordered pair reaches 22. Across all 231 two-address deletions of that graph, one changeable link accounts for all 41 ambiguous recoveries. The quotient and degree-splitting explanation uses a six-regularity assumption. These results concern construction and recovery; the bridge check concerns orientation after relative readings are known. The 20+3 count remains a conjecture.

[Research note, rule, and executable checks](../../research/chatgpt/ramsey/relative_readings_and_bridge_witnesses.md)
