# A four-point count rules out the 27-vertex pair frame

Write m=k−1 and p=|P|, as in the [transfer plan](ramsey_pair_frame_k_plan.md). Let H be the graph of red edges between pair labels. No assumptions about its symmetry or omission pattern are needed.

For each four-set Q of ground points, let t_Q count retained pairs contained in Q and e_Q count the red edges between those pairs. Pick one endpoint of each of these e_Q edges and discard it. At least t_Q−e_Q pair labels remain, with no red edge. Together with the m−4 singleton labels outside Q they form a blue set. Its size is at most m, so e_Q ≥ t_Q−4. Every pair label lies in binom(m−2,2) four-sets. Every H-edge joins disjoint pairs, hence belongs to exactly one four-set. Thus

    e(H) ≥ binom(m−2,2) p − 4 binom(m,4).

Every red neighborhood is blue because the graph has no red triangle. Its size is at most m. Each pair label already has two red singleton neighbors, so its degree in H is at most m−2. Hence 2e(H) ≤ (m−2)p. Combining bounds gives the necessary condition for m≥4:

    (m−2)(m−4) p ≤ 8 binom(m,4).

At m=7 and p=19 the lower bound on e(H) is 190−140=50, whereas the upper bound is floor(95/2)=47. This proves that both two-omission patterns fail. In fact p≤18, so the carrier has order at most 26. This is not a nonexistence proof at 26. At m=6 and p=15 both bounds give 30, as attained in the six-point construction.

Next experiment: test p=18 at m=7, using the sharper local bounds e_Q≥max(0,t_Q−4) and deg_H≤5 for pruning. To target 27 vertices, change the carrier (for example, allow some nonsingleton labels to meet the ground set in a number other than two). Such a change requires a new capacity proof.
