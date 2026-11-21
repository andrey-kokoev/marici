# Extremal size alone does NOT force repair closure

Tested all191 local (3,7;22) catalogue records, without regularity restriction:
-349,202 disjoint pairs of individually invalid triangle-free switches:170 mutually repairing pairs,169 valid combined outputs, ONE counterexample.
-1,936,105 disjoint triples:31 closed collections, all31 valid.
Files: ramsey_closed_repair_conjecture.py --all-extremal --size2/3; corresponding JSON and run logs. Individual starting graphs were independently validated in the earlier Hall-center audit.

Counterexample is catalogue record149 (one-based), zero-based vertex labels. It has degree distribution {4:1,5:2,6:19}: vertex0 degree4, vertices1,2 degree5, all others degree6. Thus extremal order22 and triangle-freeness/alpha<=6 do not suffice for the low-order repair law.

Switch A: remove(1,6),(2,18); add(1,18),(2,6).
Switch B: remove(7,21),(12,15); add(7,15),(12,21).
The supports are disjoint, both preserve every vertex degree, and all four partial/final graphs are triangle-free.
Independent-seven counts: original0, A5, B3, AB2.
All FIVE A defects contain the edge(12,21) added by B.
All THREE B defects contain the edge(1,18) added by A.
So every proper-stage obligation is repaired, yet the combined output has new seven-sets:
{1,3,6,11,12,14,15}; {1,3,6,12,14,15,16}.
In the ORIGINAL graph each has exactly the two red edges(1,6) and(12,15), one removed by each switch. Neither contains any added edge. Therefore neither is an individual defect, but both become independent jointly.

Independent verification script ramsey_nonregular_closed_repair_counterexample.py enumerates ALL seven-subsets in each of the four outputs (rather than reusing recursive search). Its JSON stores the eight individual defect sets, explicit repair edges, both emergent defects, degrees and triangle counts. Refutation does not depend on catalogue completeness.

Simple degree-only regularization is impossible without abandoning triangle-freeness: the only two added edges that could fill the degree deficits are(0,1),(0,2). Both are absent, but adding them creates triangles(0,1,2),(0,1,6) already at the starting state. This observation does not explain the universal regular-case law, but rules out dismissing the example as a regular witness with two harmless omitted edges.

Interpretation: regularity (or some correlated additional restriction) is doing substantive work; extremal vertex count alone is not the explanation. Do not claim regularity is proven to be the sole sufficient cause. The regular-family finite tests remain valid; a structural proof of their low-order closure implication remains open. The conjectures concerning21-vertex deletion examples and overlapping supports have not yet been tested in this round.
