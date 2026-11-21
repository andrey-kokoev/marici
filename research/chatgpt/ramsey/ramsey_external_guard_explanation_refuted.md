# Triangle guards need not be outside the combined operation

A stronger version of the proposed explanation was tested: allow individual switches to create red triangles, demand mutual repair of their BLUE defects plus a new joint blue defect, and ask whether some triangle guard must lie outside BOTH disjoint supports.

ramsey_external_triangle_guard.py first checked all ten regular types without finding a counterexample. The broader minimum-degree5 search found one at catalogue147 (degree5 at four vertices, degree6 at eighteen). Search stopped at first failure after156 eligible graphs,123,592,311 disjoint pairs considered and1,297,116 pairs without an external-to-both guard. It is not an exhaustive188-type guard census. An earlier unbounded run timed out without final evidence; the revised program checkpoints and filters by external-guard absence before the expensive repair tests.

Counterexample moves:
A removes(5,21),(6,19), adds(5,19),(6,21).
B removes(10,11),(12,15), adds(10,15),(11,12).
Their supports are disjoint.
A creates one blue seven, repaired by B's added edge(10,15).
B creates one blue seven, repaired by A's added edge(6,21).
Together they create TWO new blue sevens.
But A also creates red triangle(6,12,21): its guard12 lies INSIDE B's support.
B creates red triangle(5,10,15): its guard5 lies INSIDE A's support.
There are NO guards outside the union of supports. Exact triangle/seven counts original,A,B,AB are respectively0,1,1,2 for BOTH kinds of defects.

ramsey_cross_supported_triangle_guards.py independently checks every triangle and seven-subset in the four graphs; its JSON lists all defects and repair edges.

This refutes an external-reservoir explanation, NOT the original admissible-switch closure law: both proposed switches are already inadmissible because they create triangles. The missing protection need not be supplied by an untouched third vertex outside the entire operation. The two supports themselves can supply each other's triangle guards.

Why the other switch cannot repair such a triangle: each switch changes only edges within its own support. A guard in B's support is connected by cross-support edges to the endpoints of A's new edge; B cannot remove either cross-support edge. Thus the triangle survives the combined update. More generally, for vertex-disjoint two-edge switches, every newly created triangle uses one added edge and a guard outside that switch's own support; no other switch can remove its two guard edges.

Remaining structural question: do extremal size and minimum degree force at least one guard somewhere outside the support of its OWN switch whenever blue repair closes but joint blue validity fails? The finite admissible-switch results support this weaker statement, but an independent counting/structural proof remains open. Do not treat the stronger 'outside all supports' conjecture as established.
