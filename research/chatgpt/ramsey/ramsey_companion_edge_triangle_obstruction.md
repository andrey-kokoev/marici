# The triangle may block the degree-balancing companion edge, not the repair edge

First logical clarification: within the disjoint-switch setting, saying every blue-closed but blue-invalid collection has a triangle guard somewhere outside its OWN switch's support is equivalent to the already tested admissible-switch closure implication. It is not an independent explanation. A structural proof must derive that guard from the original graph constraints.

A sharper possible explanation was tested: must one of the added edges that actually repairs an individual blue defect itself create a red triangle? This is FALSE, even for a regular witness.

ramsey_repair_edge_guard_probe.py finds a counterexample in regular catalogue182:
A removes(2,11),(8,21), adds(2,8),(11,21).
B removes(4,19),(10,17), adds(4,17),(10,19).
A creates three independent sevens, all repaired by B's edge(10,19).
B creates one independent seven, repaired by A's edge(11,21).
The two repair edges are triangle-free in their respective switched graphs.
The other added edges create triangles: A's companion(2,8) has guard16, B's companion(4,17) has guard9. Both guards lie outside the combined supports. The joint output has four new independent sevens and the two triangles, so neither operation was admissible.

Degree preservation explains why the bad companion cannot simply be omitted: after deleting a matching on four vertices, every endpoint has one degree deficit. Once one added repair edge uses two endpoints, the edge between the remaining two endpoints is forced. For these particular deleted edges, the safe repair edge thus forces an unsafe companion. Choosing other deleted edges would be a DIFFERENT operation and requires a new defect analysis.

The script searches triangle-producing as well as triangle-free degree-preserving switches, using coverage masks to test blue repair. It stopped at the first counterexample in its first graph, after476540 disjoint pairs and2143 blue-mutual pairs. No full all-graph census is claimed. An independent brute enumeration of all triangles and seven-subsets verifies counts original,A,B,AB: blue0,3,1,4; red triangles0,1,1,2. The JSON preserves each individual blue defect, its safe repair edge, and the red triangles.

Interpretation: admissibility is a property of the entire degree-conserving update, not of its useful repair edges in isolation. Red/blue interaction can be mediated by the edge required to balance degrees. This provides a concrete mechanism but not a general proof that every would-be low-order counterexample in22-vertex delta>=5 witnesses has such an obstruction.

Open proof target: show that under the size/degree constraints, a blue-closed but invalid candidate cannot complete ALL its required edge repairs into degree-preserving triangle-free switches. This formulation retains the companion-edge mechanism instead of assuming the repair edges themselves must be blocked.
