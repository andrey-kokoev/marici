# Degree floor five is not sufficient without extremal order

The question was whether degree>=5 itself explains low-order repair closure. ramsey_degree5_vertex_deletion_probe.py deletes one vertex from regular22-vertex witnesses. Each resulting21-vertex graph remains triangle-free with no independent seven, and has six degree5 and fifteen degree6 vertices. The same disjoint individually-invalid switch test is applied.

A counterexample was found after72 deletion cases and67,776 disjoint pairs (search stops at first failure, not an exhaustive count). Parent is catalogue185; delete vertex5. For clear replay, use ORIGINAL parent labels below, omitting5:
A removes(1,20),(9,12); adds(1,9),(12,20).
B removes(6,18),(15,17); adds(6,17),(15,18).
Supports are disjoint, every degree is preserved, and all four21-vertex states are triangle-free. Independent-seven counts: original0, A1, B2, AB1. Every individual defect is repaired by the other switch, but one independent seven appears only jointly. All four states were independently verified by enumerating seven-subsets. JSON stores compressed21-vertex labels, their parent correspondence, switches, all seven-sets and adjacency.

Restore the deleted vertex5 with its original six neighbors, keeping the same switches. The parent22-vertex graph is regular and valid, but A now creates triangle(5,12,20); B creates triangle(5,15,18); both together create both triangles. Independent-seven counts remain0,1,2,1. Thus the restored vertex does NOT remove the emergent blue obstruction: it forbids both enabling operations by acting as a common-neighbor triangle guard. This was independently checked on all four parent-labeled graphs.

Combined with the earlier22-vertex minimum4 counterexample, we now know:
- extremal order22 alone does not force closure;
- minimum degree5 alone does not force closure;
- the combination (order22, minimum degree>=5, the stated disjoint admissible switches) still passes all188 applicable catalogue types, but lacks a structural proof.

The promising mechanism is external triangle protection: vertices outside the switch supports can prevent an otherwise closed-but-invalid blue-repair pattern from being an admissible triangle-free operation. Both surgical interventions found so far act this way. A proof would need to show that the joint degree/order constraints force such guards for any would-be counterexample. This remains a conjectural explanation, not established by two examples.

Helper update: sevens() and switches() now infer graph order from adjacency length instead of hardcoding22, preserving earlier22-vertex behavior while supporting the21-vertex probe.
