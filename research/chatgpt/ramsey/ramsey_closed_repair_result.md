# Closed repair conjecture survives full disjoint-switch test; five-way cooperation discovered

Scope: vertex-disjoint, individually triangle-free two-edge switches from Hall types190,191. Every single switch is invalid. Since each uses four vertices, at most five switches can have pairwise disjoint supports on22 vertices. The tests therefore exhaust all collection sizes2..5, not just a sampled arity. Size2 was checked in ramsey_mutual_repair_conjecture.py; sizes3..5 in ramsey_closed_repair_conjecture.py.

A collection is closed when every independent seven in EVERY nonempty proper partial application is hit by an edge added by the remaining switches. This is stronger than collectively repairing singleton defects. The full output is independently tested afterward.

Counts (source190,source191):
size2 collections (1430,1450), closed (0,5), valid closed (0,5).
size3 collections (6780,7005), closed (0,10), valid closed (0,10).
size4 collections (7950,8245), closed (0,0).
size5 collections (1584,1585), closed (0,1), valid closed (0,1).
Total36,029 collections,16 closed, all16 valid; no counterexample. This is exhaustive confirmation on these two starting graph types, not a general theorem for arbitrary witnesses.

Intermediate-stage constraints matter: source190 has five triples that repair all singleton defects but fail at pair defects. Source191 has two five-switch collections that repair all singleton defects, but only one survives the pair-stage requirements and closes fully. Thus singleton repair cannot substitute for proper-subset closure.

The unique closed quintuple is IRREDUCIBLE: every one of its30 nonempty proper subsets is invalid. Each single creates6 independent sevens; pairs and triples create6 or12; each four-switch subset creates6; all five together create zero. All intermediate graphs are triangle-free. Its final graph is isomorphic to source191, but differs on labeled edges. It is not a transition to a new unlabelled type.

Concrete source191 switches:
remove (2,13),(7,21); add (2,21),(7,13).
remove (3,16),(11,20); add (3,20),(11,16).
remove (4,14),(9,17); add (4,17),(9,14).
remove (5,12),(10,19); add (5,19),(10,12).
remove (6,15),(8,18); add (6,18),(8,15).
The five supports partition twenty vertices and leave0,1 untouched. The five-switch set is invariant under the independently recovered C5 and forms a single five-element orbit. Thus full cyclic symmetry closes a cooperative operation that no proper subset can perform validly.

Evidence: ramsey_closed_repair_size3/4/5.json. Size5 additionally retains all30 partial-subset counts, switches and full output adjacency. The valid quintuple's target191 was verified by exact graph isomorphism using the existing helper. New conjectural task: derive the five-way closure from the explicit cyclic-coordinate pattern, explaining the obstruction counts and why every proper subset fails, without enumerating all seven-subsets. Distinguish a valid labeled reorganization returning to the same graph type from reaching a different type.
