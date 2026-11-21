# Repair closure extends beyond Hall types; only orders two and three are nontrivial

Run ramsey_closed_repair_conjecture.py --all-regular --size k for k=2,3,4,5. This tests all ten independently validated regular catalogue types, including the eight with no Hall center. Only individually invalid, triangle-free two-edge switches are candidates; supports must be vertex-disjoint. All nonempty proper partial-stage obstructions must be hit by edges added by the remaining switches.

Counts:
k=2:10,619 collections,12 closed,12 valid.
k=3:46,720 collections,18 closed,18 valid.
k=4:49,169 collections,0 closed.
k=5:8,177 collections,1 closed,1 valid.
Total114,685 collections;31 closed;all31 valid. Seven of the closed pairs and eight closed triples start outside the Hall family. Coverage is exhaustive for these ten catalogue representatives and this move definition; identifying them with ALL regular (3,7;22) isomorphism classes relies on catalogue completeness.

## A general bounded-birth lemma

Let a valid initial graph undergo k vertex-disjoint edge switches, and suppose a set I of r vertices is independent in the final graph. Let S contain exactly the switches that remove at least one ORIGINAL red edge with both endpoints in I. Every original red edge in I is removed by S, since I is finally independent. No edge added by any switch lies inside I. Therefore I is already independent after applying S alone.

Each member of S uses at least TWO vertices of I, and the supports of different switches are disjoint. Hence |S|<=floor(r/2). Since the initial graph has no such independent set, S is nonempty.

For r=7 every final obstruction is born in a subcollection of at most THREE switches. Consequently, for k>=4, closure of all proper partial repair obligations AUTOMATICALLY rules out a final independent seven: its birth subset S is proper, and the remaining added edges do not hit it, contradicting closure. Triangle-freeness is also automatic for the combined disjoint switches when each individual output is triangle-free: a triangle cannot contain two added edges from disjoint supports.

Thus the genuinely nontrivial conjectural content was at k=2 and k=3. Higher-arity proper-subset closure sufficiency is a general theorem, independent of Hall centers, regularity, and22 vertices. Equivalently, for any k>=4 it suffices to inspect obstructions of subcollections of sizes1,2,3 and whether the remaining added edges repair them; larger proper subsets add no independent requirement.

This does NOT bound the order of irreducible successful cooperation by three. Five switches can still be needed to repair the entire network of low-birth-order obstructions, as the verified five-way orbit demonstrates. Distinguish maximum BIRTH ORDER of a forbidden configuration from minimum SIZE OF A SUCCESSFUL REPAIR COALITION.

The extensive k4/k5 checks are consistent verification, not new empirical support needed for this lemma. A short structural proof of the nontrivial k2/k3 implication across regular extremal witnesses remains open; the finite catalogue test supports it beyond Hall geometry.

Evidence: ramsey_closed_repair_all_regular_size2/3/4/5.json. The --all-regular option was added without overwriting the earlier Hall-only result files.
