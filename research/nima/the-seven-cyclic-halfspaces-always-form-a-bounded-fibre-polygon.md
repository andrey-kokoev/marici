# The seven cyclic halfspaces always form a bounded fibre polygon

The sampled cyclic-halfspace observation now has one **universal** theorem: compactness. This is not a claim that the fourteen noncyclic minor inequalities are redundant.

For moment-curve external data `Z_j=(1,j,...,j^5)`, `j=1..7`, the one-dimensional left kernel is

    k=(1,-6,15,-20,15,-6,1).

Fix ANY real rank-two source `C` whose seven **ordered cyclic** minors `Delta12,Delta23,...,Delta67,Delta17` are strictly positive. Its fixed-target fibre representatives have the form `C(a,b)=C+[a,b]^T k`. Each of these seven minors is affine in `(a,b)`.

Assign positive weights to the seven cyclic edges in that order:

    (1/6, 1/90, 1/300, 1/300, 1/90, 1/6, 1).

The exact symbolic identity is

    sum_i weight_i * Delta_i(C(a,b))
       = sum_i weight_i * Delta_i(C) = K > 0.

The coefficients of both `a` and `b` cancel identically. Indeed, writing `q_i=C_i/k_i`, every weighted normal is (up to a common quarter-turn) a successive difference `q_(i+1)-q_i`, with the last edge contributing the opposite full difference `q_7-q_1`. Their sum telescopes.

The seven normals also span the two-dimensional fibre dual when the seven cyclic source minors are strictly positive. If they were collinear, the successive differences of the `q_i` would be collinear. All six consecutive determinants `det(q_i,q_(i+1))` must be strictly NEGATIVE because consecutive `k_i k_(i+1)<0` while `Delta_(i,i+1)>0`. Collinearity would make `det(q_1,q_7)` their sum, hence negative. But `k_1 k_7>0` and `Delta17>0` require `det(q_1,q_7)>0`, contradiction.

Inside the seven-halfspace region every cyclic minor is nonnegative, so the positive weighted sum `K` bounds EACH minor above by `K/weight_i`. Two independent affine normals therefore bound both fibre coordinates. The region is closed and contains `(0,0)` strictly; it is a nonempty compact polygon with interior. This holds without assuming the other fourteen minors of `C` are positive. The earlier cyclic-positive but nonadmitted target is consistent: its cyclic polygon is compact, yet its FULL positive fibre is empty.

This establishes a durable precondition for the next exact Farkas/active-set gate: if the target has a strictly positive source, any noncyclic minor can be checked on finitely many vertices of a GUARANTEED bounded cyclic polygon. It does not establish that those checks always pass, prove six-cell coverage, or identify the source forms with physical histories.

Run `uv run --with sympy python research/nima/checkers/check_seven_point_cyclic_polygon_boundedness.py`. The checker verifies the symbolic identity for independent source variables, checks positivity of every weight, and rejects seven single-weight deletion mutations. Artifact: `research/nima/results/seven-point-cyclic-polygon-boundedness.json`.
