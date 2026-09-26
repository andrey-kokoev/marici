# A coincident row proof does not validate a nonbijective permutation

Fresh `check_nonbijective_row_transport.py` has synthetic duplicate x<=1 rows A and B and a third y<=1 row C. The index map (0,1,1) duplicates B and drops C. For the selected A-only packet it nonetheless gives the same x<=1 implied normal/bound as an actual permutation, because B and C have zero multiplier. The transport gate rejects `NOT_A_BIJECTION` BEFORE accepting any coincident packet result; a genuine permutation (1,0,2) passes.

A permutation must rearrange every ordered row occurrence exactly once. One packet's equal math cannot justify deleting an unused source row. No owner-issued row set or analytic S,A,R,C,G mapping is established.

Next test PERMUTATION COMPOSITION: sequential genuine row permutations and corresponding multiplier transports equal a composed permutation mathematically, but retain both intermediate transport witnesses in derivation history rather than collapsing them to an observed direct transport.
