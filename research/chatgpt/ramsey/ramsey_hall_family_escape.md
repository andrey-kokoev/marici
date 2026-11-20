# Four-edge escape from the Hall family: cooperative switches

Exhaustive unrestricted four-edge exchange search: ramsey_regular_four_exchange.py, with full certificates in its JSON. Every four-edge removal set is examined (720,720 per source). All degree-restoring pairings of endpoint stubs are considered, including shared endpoints. Triangle pruning happens only AFTER all four old edges are removed, and during monotone edge addition; thus it cannot eliminate a final triangle-free result.

Source190: 4,455 triangle-free exchanges; 20 valid, all to type191.
Source191: 4,425 triangle-free exchanges; 15 valid, ten to type190 and FIVE to type182, which has NO Hall center.

Therefore four-edge exchange is sufficient and, by earlier two/three-edge exhaustive exclusions, necessary to escape the Hall family directly from type191. Type190 cannot leave the family in a single four-edge move, but can via 190->191->182. This does not establish the minimum size of a direct 190-to-non-Hall exchange, nor connect all ten regular types.

A certified source191 -> type182 exchange in original zero-based catalogue labels:
remove (1,7),(5,20),(10,17),(14,15)
add    (1,14),(5,17),(7,15),(10,20).
Root0 and its six neighbors {1,2,3,4,5,6} remain fixed. Its fifteen external signatures change from fifteen pairs to two singletons, eleven pairs, two triples, all distinct. The output has NO alternative Hall center.

Crucial structure: this change is TWO disjoint alternating four-cycles, not one alternating eight-cycle. It factors into two degree-preserving switches:
A: remove (1,7),(14,15); add (1,14),(7,15).
B: remove (5,20),(10,17); add (5,17),(10,20).
Their supports are disjoint, so they commute as edge updates. Yet their validity is coupled globally:
- A alone is triangle-free but has exactly ONE independent seven: {1,4,5,7,16,17,18}.
- B alone is triangle-free but has SIX independent sevens; one is {0,7,8,10,15,16,17}.
- A+B is triangle-free and has ZERO independent sevens.
Both individual switches give root signature sizes {1:1,2:13,3:1}; together give {1:2,2:11,3:2}. Counts were checked by enumerating all seven-subsets of the three output graphs, independently of the recursive existence test.

Interpretation: leaving the pair model does not require moving the root or changing its neighbor set. Two individually inadmissible local redistributions compensate each other's global independent-set obstructions. Thus disjoint support does NOT imply independent admissibility. Contrast with independent alternating-cycle flips of a Hall perfect matching, where every intermediate matching remains valid. This distinction is a promising conceptual bridge back to irreducibility: an operation can be decomposable as an edge permutation but irreducible within the space of valid witnesses.
