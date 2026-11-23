# A reciprocal pair forces a blue seven

Use the matched two-pole construction. Write M_s for the contact with left address s and right address f(s). Assume f is bijective and s is disjoint from f(s) for each s (necessary for red triangle avoidance).

Suppose f(ab)=cd and f(cd)=ab, with fifth label e. Partition the other eight addresses into X={ac,ad,bc,bd} and Y={ae,be,ce,de}. Each member of Y must map outside Y by disjointness. The addresses ab and cd are already taken. Hence f(Y)=X by bijectivity, and f(X)=Y. In particular the four members of X have right addresses all containing e. No two of their contacts are red-adjacent. The contact M_ab also has no red edge to these four because each of their left addresses meets ab.

Take these five contacts together with L_e and the right pole R. L_e sees none of the five contacts (no left address contains e). R sees no contact and is not linked to L_e. These seven vertices induce no red edge. M_cd can replace M_ab, and exchanging sides gives two more witnesses.

Thus directly, without a census, red-triangle and blue-seven avoidance rule out every 2-cycle of the pair permutation. This necessity result applies within this construction; it does not classify all (3,7)-avoiding graphs. Finite classification: results/ramsey_37_all_pair_placements.json.
