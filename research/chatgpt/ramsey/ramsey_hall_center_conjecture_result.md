# Hall-center necessity conjecture: refuted

Conjecture: every 6-regular triangle-free 22-vertex graph of independence number at most six has a vertex v for which the fifteen vertices outside its closed neighborhood meet N(v) in all fifteen distinct pairs.

`ramsey_hall_center_conjecture.py` independently decoded and validated all 191 local r37_22.g6 records (triangle-freeness and no independent seven), then tested every vertex of every 6-regular record. Ten records are 6-regular. Records 182..189 have no Hall center; record 190 has centers 0,5; record 191 has center 0. Indices are one-based catalogue indices; vertices zero-based. Full reproducible evidence, graph6 witnesses and all root profiles are in `ramsey_hall_center_conjecture.json`. Input SHA256: 228d886ee01b3003d90c768af57804954f7adccbca901a3eeb3c69ccc020e8c5.

Refutation does not require catalogue exhaustiveness: each of the eight checked graphs is a counterexample on its own. The claim that these are ALL regular types does rely on catalogue coverage/nonredundancy, which this script does not establish.

The near miss is informative. In record 182, two roots have fifteen distinct external neighborhood signatures with size histogram {1:2,2:11,3:2}. Thus even quite small departures from the pair model remain valid witnesses. Other roots have larger departures; none is a Hall center.

Interpretation: the Hall construction is a sufficient, structured family, not a necessary consequence of regularity and the Ramsey constraints. A Hall center still reconstructs a perfect incidence matching: label the neighbors, identify outside vertices with pairs, use triangle-freeness to restrict edges to disjoint pairs, then degree and partition counting force one deletion per partition and one selected partition per duad.

Further explanatory question: what permits the replacement of uniform pair-neighborhoods by mixtures of singleton, pair and triple neighborhoods while preserving the witness constraints? This is a broader construction problem; do not repair the failed conjecture by assuming a Hall center. Nor does the counterexample refute the conditional BRNN common-frame constructor.
