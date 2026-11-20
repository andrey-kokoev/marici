# Conjecture 1: mutual repair survives exhaustive testing

Conjecture: for two vertex-disjoint triangle-free two-edge switches from a Hall-type witness, if each destroys every independent seven created by the other, their joint application is valid.

ramsey_mutual_repair_conjecture.py enumerates all 80 triangle-free individual switches at each of the two Hall catalogue types (190,191). Every individual switch has independent sevens, as independently rechecked by listing them. Then it tests every disjoint pair, using explicit added-edge hits to certify mutual repair, and separately lists all independent sevens after the combined operation.

Results:
- source190: 1,430 disjoint pairs; zero mutually repairing pairs; zero valid joint outputs.
- source191: 1,450 disjoint pairs; exactly five mutually repairing pairs; exactly these five give valid joint outputs.
- zero counterexamples to the conjecture in 2,880 tested pairs.

There are genuinely emergent independent sevens in 800 source190 pairs and 810 source191 pairs: these sets are independent only in the combined output, not in either individual output. However all those pairs already fail mutual repair. So emergent obstructions are real, but do not defeat a successful mutual-repair certificate in this finite experiment. Do not assert emergent obstructions never occur.

For a vertex-disjoint pair, the combined graph is automatically triangle-free if both individual outputs are triangle-free: a triangle could not contain an added edge from both disjoint supports. Thus the only possible failure is an independent seven. Destruction of every individually created independent seven is necessary for combined validity (the other operation must add an edge inside it). The empirical content is sufficiency: no genuinely emergent seven survives when this necessary condition holds.

Full witnesses and independent-set masks are saved in ramsey_mutual_repair_conjecture.json. This is finite exhaustive confirmation on the two Hall graph representatives, not a structural proof or a claim for arbitrary Ramsey graphs. Counts match the five unrestricted type191-to-type182 four-edge escapes found independently.

Outstanding conjectures from the current synthesis round:
2. Existence of three vertex-disjoint two-edge switches on some regular witness with valid simultaneous output but invalid output for EVERY nonempty proper subset. This would establish genuinely three-way cooperation. Untested.
3. Connectivity of all ten regular types under valid degree-preserving exchanges of at most four edges. Only outgoing four-edge moves from190,191 and all two-edge moves are currently enumerated. Untested globally.

Recommended next: either derive a short reason mutual repair rules out joint-only obstructions for Hall starts, or test conjecture2 to determine whether cooperation extends beyond pairs.
