# A concrete finite trace now exports checked RepresentedStep proofs

The new certificate path retains BOTH the concrete execution and the abstract proof:

1. Run an actual closed port net through seven rewrites, saving every full before/after agent table, reciprocal wire table, allocator and selected active pair.
2. Serialize and restore those snapshots with a restricted tagged codec; reject malformed fields, duplicate entries and bad wiring.
3. Replay each selected concrete rewrite and compare the entire resulting snapshot exactly, not just its endpoint package.
4. Reify the actual states, identify the contextual abstract step and its pure-compression witness, and generate an Agda RepresentedStep inhabitant for each pair of terms.
5. Freshly check the generated Agda module with --ignore-interfaces.

All seven steps pass. The packet stores the exact finite package payload, rule-witness table and seed-evidence table; the generated module embeds the packet's SHA256 in its provenance comment, and the result manifest binds both bytes. The hash is transport/provenance binding, NOT a proof inside Agda of the codec.

Two negative controls are distinct: a corrupted reciprocal-wire snapshot is rejected by Python admission; an abstract certificate replacing seed0 by seed1 is rejected by Agda with UnequalTerms (0 != 1). The failing test module is retained as text under results, not as a live failing Agda source.

Artifacts: results/concrete-port-certificates.json, agda/ResolutionNetPortCertificates.agda, results/port-certificates.json and the check/rejection logs. Reproduce: python research/voevodsky/resolution-net-v1/check_port_certificates.py. Explicit UTF-8 output is required on this Windows host; the initial default-encoding failure was corrected before the successful fresh run.

Trust boundary: this first exporter supports ONE explicit package, representing its admitted rule and seed witnesses by injectively assigned natural-number codes. It rejects foreign packages. The codec, reifier, table assignment and exporter remain trusted Python; Agda checks the generated abstract statements, not the meaning of the original JSON wires. No universal concrete port-refinement theorem has been established.

Next remove the one-package restriction with a finite indexed package/rule signature whose constructors preserve actual source and target indices. Use a heterogeneous-resource or transport fixture to test that mismatched packages are rejected by Agda itself, not only by the Python exporter. A universal formal graph representation remains a separate stronger obligation.
