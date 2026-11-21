# Minimum degree and admissibility, not regularity alone

ramsey_repair_minimum_degree_audit.py separates all191 catalogue types by minimum degree:178 have delta5, ten have delta6 (regular), three have delta4 (records65,149,150).

The178 nonregular delta5 types have332,313 candidate disjoint pairs with155 closed/155 valid;1,852,369 triples with13 closed/13 valid. Thus regularity is NOT needed for the observed closure result. All failures occur at delta4, but only one of the three delta4 types fails. The sharpened conjecture is sufficiency of delta>=5 at order22, not equivalence or necessity for each graph.

A surgical test explains what the missing degree can do in the actual counterexample149. Its ONLY triangle-free red-edge addition is(0,2). Adding it preserves the Ramsey constraints (red-edge addition cannot create independent sevens) and raises the degree distribution to two degree5 vertices and twenty degree6 vertices, minimum5. The result is isomorphic to catalogue record9.

The old counterexample switches still preserve degrees, but A is no longer triangle-free: its added edge(2,6) completes triangle(0,2,6), since(0,6) was already present. The four augmented states have triangles: original none, A exactly(0,2,6), B none, AB exactly(0,2,6).

Crucially, the two emergent independent sevens do NOT contain vertex0, so adding(0,2) does not remove those blue obstructions. It instead makes their enabling switch inadmissible by introducing a red-triangle obstruction. This is a direct mechanism, not merely a degree histogram correlation: additional incidence can protect the closure law by forbidding dangerous operations rather than by directly repairing their final defects.

Other minimum4 records are also edge-unsaturated:65 permits addition(0,1);150 permits(0,1),(0,3),(1,2),(2,3). Thus minimum degree and edge saturation are not yet cleanly separated as explanations by the lone failure. Do not claim a general delta5 theorem from the surgical test. The broader task is to prove that any mutually repaired but invalid disjoint pair/triple would force a vertex of degree at most4, or find an alternative structural obstruction explaining the catalogue pattern.

Independent exact isomorphism, all minimum-degree counts, safe addition, and post-addition triangle certificates are in the companion audit JSON. No vertices or edges of the original witnesses were silently modified; the augmented graph is a separately constructed comparison.
