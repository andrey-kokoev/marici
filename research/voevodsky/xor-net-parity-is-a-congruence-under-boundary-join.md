# XOR net parity is a congruence under boundary join

The typed BIT chain has a left input and a terminal auxiliary next port. Join two segments with disjoint fresh labels by connecting the last left next port to the first right principal input. Fresh `check_xor_net_boundary_composition.py` verifies 9,217 word/cut pairs through total length 9, including empty units: no duplicated/dangling internal labels, and `parity(join(A,B))=parity(A) xor parity(B)`.

For every finite length the equation follows inductively from `ACC(p)--BIT(b) -> ACC(p xor b)`; concatenation of bit words and associativity of XOR make parity equivalence a congruence under this join. Two segments with the same parity remain indistinguishable under any further joins and final parity reads. This is a genuine uniform sufficient state for the FIXED closed-boundary observation policy, not a compact state for arbitrary readout. Indexed reads, Nima E/E_B multiplicities and all owner/source questions remain outside this model.

Next admit a second local observation (e.g. `has-one` threshold) and test whether the summary product `(parity,has-one)` remains constant-size and compositional, or whether a contextual operation forces a family of growing distinguishable classes.
