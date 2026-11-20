# Hall types have exact exchange threshold four

After exhaustive two-edge rejection, ramsey_regular_three_exchange.py exhausts every exact three-edge degree-preserving exchange from records 190 and 191. It pairs the six removed-edge endpoint stubs in every way, including repeated vertices, rather than assuming disjoint removed edges. It rejects loops, repeated edges and overlap with old edges.

For each source, 45,760 removed triples were considered. Source190 has 110,795 legal exchanges, 50 triangle-free, zero valid Ramsey outputs. Source191 has 110,790 legal exchanges, 60 triangle-free, zero valid outputs. This lower bound does not rely on catalogue coverage.

ramsey_hall_center_four_exchange.py then constructs all 288 perfect incidence matchings with the original Hall center 0 and its fixed pair labels. For each source exactly ten constructions differ by four removed/four added edges. All ten go to the OTHER Hall-center type. This search is restricted to preserving the chosen Hall-center labeling; it is not an exhaustive four-edge search in general.

Explicit source190 -> type191 move, original zero-based catalogue labels:
remove (10,18),(11,16),(15,20),(17,19)
add    (10,15),(11,17),(16,20),(18,19).
The exchange is an alternating eight-cycle and preserves root0. Exact isomorphism certificates and all counts are stored in companion JSON files. Source191 similarly has ten reverse-type moves at its chosen root.

Therefore the smallest valid nontrivial degree-preserving exchange from either Hall type changes FOUR red edges to FOUR others. In particular, distinct Hall types are connected at that scale, despite being isolated under two- and three-edge moves. For a fixed Hall center this scale is also explained by the girth-eight incidence cage: a matching change needs an alternating cycle of at least eight flags, affecting at least four partition deletions.

Open: do unrestricted four-edge exchanges leave the Hall-center family entirely? The restricted construction cannot answer this: it deliberately preserves a Hall center. Do not claim that all ten regular types are connected, or that four edges suffice to reach a no-center counterexample.
