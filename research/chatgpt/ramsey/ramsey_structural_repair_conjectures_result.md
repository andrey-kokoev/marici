# Structural explanations: two refutations

These are the SECOND conjecture round (local inheritance, complementary channels, cyclic phase locking), not the earlier round (mutual sufficiency, three-way cooperation, global connectivity).

1. Local one-vertex inheritance is FALSE. ramsey_local_obstruction_inheritance.py examines every emergent independent-seven occurrence across all disjoint triangle-free switch pairs from190,191. Source190: 7,570 occurrences, only70 with a support-local witness; 7,500 have no surviving individual obstruction obtainable by ANY replacements restricted to adding vertices from the switch supports. Source191: 6,895 occurrences, only45 with a support-local witness; 6,850 have none. Dropping support locality still does not save one-vertex inheritance: nearest surviving individual obstruction may require three replacements from190, and up to SEVEN from191.

An extreme type191 example:
A removes (1,7),(14,15), adds (1,14),(7,15).
B removes (3,18),(10,19), adds (3,10),(18,19).
Joint-only independent seven I={0,8,9,10,14,15,19}.
The surviving individual obstructions are exactly:
{1,4,5,7,16,17,18}, {1,3,6,12,13,18,20}, {1,3,12,13,17,18,20}.
Each is DISJOINT from I. Thus this is a global obstruction relation, not a local rerouting of I. Full first counterexamples, distance histograms and most-distant examples are in companion JSON/run log.

2. Pure complementary channels is FALSE. ramsey_repair_constraint_channels.py tests all five successful pairs at type191's UNIQUE Hall center0. All preserve that root and its neighbor set. Each pair has the same profile:
- A: alpha(H)=5, one independent-Hall-deficient set.
- B: alpha(H)=6, FIVE independent-Hall-deficient sets.
So A breaks only coverage, but B breaks BOTH coverage and external independence. There is no alternative original Hall center that would rescue the proposed pure separation. The coupled-channel characterization remains true; the proposed division of labor does not.

3. Cyclic phase locking subsequently VERIFIED: see `ramsey_cyclic_phase_explanation.md` and `ramsey_repair_cyclic_phase.py`/JSON. Independently recovered root automorphism group is C5; the participating switches are two orbits of five, uniquely paired equivariantly. Among disjoint relative phases, repairing B's unique root-containing seven alone selects the successful phase. This symmetry reduction still requires a representative combined-validity check.

Mutual-repair sufficiency itself still survives all 2,880 disjoint-pair tests. These failures refute proposed explanations, not that finite result. Avoid replacing falsified locality with arbitrary larger radius: the example requires complete replacement of the seven-set.
