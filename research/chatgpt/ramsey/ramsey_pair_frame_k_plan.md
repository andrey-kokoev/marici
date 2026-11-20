# Transfer plan: pair incidence for R(3,k)

**Objective:** retain the singleton/pair incidence rule, and find out which pair labels and pair-to-pair red edges can be specified uniformly from k. A valid output gives a lower bound, not an upper bound. Use known Ramsey numbers to measure results, not as inputs to the eventual generator.

## 1. Fix the contract before choosing edges

Put m=k−1. Take one root, the m singletons of X, and a family P of distinct pairs from X. Join the root to all singletons, and each pair to its endpoints. Put a graph H on P; permit a red H-edge only between disjoint pairs. No other edges are red. The order is 1+m+|P|.

There is an exact test, independent of k. Require H to be triangle-free. For Y contained in X, let H[Y] here denote the graph on retained pairs contained in Y. Require

- alpha(H[X]) ≤ m−1;
- alpha(H[Y]) ≤ |Y| for every proper subset Y of X (empty graph has independence number zero).

**Proof.** Only H can contain a triangle. A blue set containing the root can use only pair labels in addition. For a blue set without the root, fix its singletons to be X minus Y. Its maximum size is m−|Y|+alpha(H[Y]). These two cases give the tests in both directions. The singletons themselves attain m. Equivalently, a blue family of pairs must have at least as many distinct endpoints as pairs, and cannot have m pairs. A violating family gives an explicit certificate.

## 2. First experiment: k=8, with a finite stop condition

At k=7 the [six-point construction](ramsey_37_pair_rotation_rule.py) passes with all 15 pairs. At k=8, retaining all pairs would give 1+7+21=29 vertices, impossible since R(3,8)=28. Thus *choosing which labels to retain* is necessary; changing only the distinguished-pair rule cannot work.

Test whether this carrier can reach 27 at all before seeking a formula. It needs exactly 19 retained pairs on seven points. Up to relabeling, the two omitted pairs are either adjacent (12,13) or disjoint (12,34). Test both, without imposing rotational symmetry. Do not require one omitted edge per triple of disjoint pairs: that was a sufficient six-point device, not the general triangle condition.

1. Create a Boolean variable for each permitted edge of H. For each triple of mutually disjoint pair labels forbid the three edges from all being red.
2. Solve, then test the two independence inequalities. For a violation return the blue family F and add a clause requiring at least one permitted edge inside F to be red. Repeat to feasibility or certified infeasibility. This terminates: a new clause excludes the current assignment.
3. Deliver either a matrix independently verified against red triangles and blue eight-sets, or checkable infeasibility proofs for both omission patterns. A timeout is neither result. First regression: verify the k=7 fixture by the same subset tests.

## 3. Turn discovery into a transfer test

If a 27-vertex matrix exists, identify a rule for P and H using only m and incidence. Freeze its definitions **before** testing k=9. Generate the graph without solver decisions or witness data; report order, forbidden-set checks, and a concrete obstruction if invalid. Distinguish a valid lower bound from attaining a known extremal order. If both k=8 templates are impossible, record that the root/singleton/distinct-pair carrier cannot attain 27; test 18 retained pairs for a smaller witness or change the carrier explicitly. Do not interpret a carrier exclusion as a Ramsey upper bound.

**Completion criterion:** an explicit parameter rule, a proof of the two capacity inequalities and triangle condition for its stated range, and a stated order 1+m+|P(m)|. Reproducing solver outputs alone is not such a rule.
