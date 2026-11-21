# Stronger seed-binding obstruction: no transported exit pole stays row-fixed

Before selecting an additional marking convention, test a necessary feature of the literal seed: both cage poles are stationary under its row involution. In output coordinates the entry pole is duad vertex7; the exit pole is the partition represented by triple[11,14,16]. Both are fixed by the original row action R (the triple setwise).

ramsey_transferred_pole_stationarity.py applies all five graph isomorphisms K:G->TG and tests the resulting typed poles under the SAME literal R. Exactly one transport leaves the entry pole row-fixed. NONE leaves the exit pole row-fixed. Therefore no center-transfer marking convention can preserve the seed's stationary-pole interpretation with R unchanged. This is stronger than noting that no K commutes with R globally.

The five transported exit partitions are:
[5,11,19], [6,11,14], [2,14,20], [4,7,20], [1,7,19].
Each contains one old ground-label vertex and two old duad vertices, now valid duads in the new presentation. A row-fixed triple of this form must have its unique old-label member fixed. Among those old-label choices only4 is fixed by R. Its candidate[4,7,20] maps to[4,7,19], so also fails. This gives a short structural explanation of the five-case exclusion.

Consequences:
- The reciprocal selected-duad convention from ramsey_mark_transport_anchor.md remains a coherent added rule, but is NOT an identification of center transfer with the original stationary-pole seed transition.
- The natural graph-update square TRG=RTG remains correct, but transporting marks separately with K and K_R=RKR makes the two images of the old exit pole different physical partitions.
- To keep the old pole identities stationary, one can transport the entire comparison frame: replace R by R'=KRK^{-1}, and the compared pair by (KG,KRG). Then stationarity follows by conjugation. But the second graph KRG is not automatically the independently center-transferred row graph T(RG); no fixed K commutes with R. This is a different specification of the operation, not a free identification.

Thus the remaining choice is structural, not merely a fivefold phase choice: either keep the original comparison and permit moving/retyped poles, or transport the comparison involution together with the marks. Neither should be inferred from the original strings without an operational rule.
