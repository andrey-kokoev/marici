# External wiring breaks the local symmetry; repair fails one level later

For the locally indistinguishable orbit10/orbit12 switches, the core is {0,1,2,12,13,16}. The apparent local symmetry fixes0,1,2,16 and swaps12,13. All external-to-core neighborhood counts and complete signature multiplicities respect this swap.

But a small external edge already prevents extension to a graph symmetry. External vertices are uniquely identified by their core signatures:
vertex5 has {0,12}; vertex10 has {1,13}; their proposed images must be vertex4 with {0,13}, and vertex8 with {1,12}.
Edge(5,10) is RED, whereas(4,8) is BLUE. Thus the local swap cannot preserve the external wiring. No independent-seven enumeration is needed to verify this symmetry-breaking certificate. ramsey_external_wiring_separator.py finds14 signature-class edge-count discrepancies; the stated one uses singleton classes and is especially small.

However distinguishing diagrams is not yet a proof of viability. An additional direct repair test shows BOTH local twins can have their own initial defects covered by disjoint candidate helpers. For dead orbit10, candidates50 and77 cover all five initial defects. So the explanation is NOT immediate lack of repair coverage.

The failure occurs when the helpers' obligations are included. ramsey_dead_template_refutation.py extracts a backward-trimmed27-assignment unit-refutation DAG from the necessary low-order rules. Starting with orbit10's representative (candidate38), its defect {2,4,6,10,11,12,21} requires one of candidates19,28,52,77. The first three are excluded by the propagated support/repair constraints, forcing77.
Candidate77 removes(6,17),(8,21), adds(6,21),(8,17). It creates independent seven {0,8,10,11,14,16,21}. Every possible compatible repairer of that seven is already excluded. The chain closes in contradiction. The proof JSON records the intermediate reasons, including support overlaps and exact birth/repairer clauses, so this is not merely a statement that a completion search failed.

For viable orbit12, the earlier explicit three-way recipe supplies a successful continuation. Its apparent locally symmetric counterpart dies in the repair cascade. The outside-edge certificate explains why local indistinguishability was misleading; the implication certificate explains the actual failure of completion. We have not shown that changing the single separating edge alone would interchange their viability—such a change could violate other constraints.

Artifacts: ramsey_external_wiring_separator.py/JSON; ramsey_local_symmetry_repair_obstruction.py/JSON (initial-defect covers); ramsey_dead_template_refutation.py/JSON (trimmed failure proof). The remaining abstract task is to derive these repair-cascade templates from external incidence structure without first compiling all relevant independent-seven clauses.
