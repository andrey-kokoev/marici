# Local substitution prototype

`local_net.py` implements explicit reciprocal port wiring, one external result boundary, and a principal-principal active pair between a flatten agent F and a data constructor. The evaluator never invokes reference flattening or domain callbacks.

Signatures: F/1, atomic seed/0, layered seed/1, unary step/1, binary step/2 (arity counts auxiliary ports). Thus ONE semantic operator currently has FIVE fixed-arity agent signatures and THREE local rewrite schemas. A claim of one agent would be false.

Rules:

* F meets layered Seed: remove both and splice the result boundary to the retained inner history's principal port.
* F meets unary Step(w): reconstruct Step(w) one layer lower; attach a fresh F to its premise.
* F meets binary Step(w): reconstruct Step(w) one layer lower; attach one fresh F to each ordered premise.

Only the active pair and its incident wires are rewritten. Rule witnesses are retained without execution. No duplication of premise subnets occurs. Input compilation unfolds repeated immutable Python references into distinct occurrences, explicitly giving tree rather than shared-graph semantics. Seed payloads are embedded as actual subnets, not recursively flattened by a callback.

Wire reciprocity, complete port occupancy, tree connectivity and single ownership are asserted after each step. These whole-net checks are instrumentation, not part of the constant-size local rewrite claim; they do not establish a performance improvement. Readback is normal-form only and reconstructs the witnessed derivation.

Fresh `python research/voevodsky/resolution-net-v1/check_local_net.py` passes six exhaustive schedules (19 explored transitions) for a branching fixture,640 seeded randomized runs (1760 transitions), and three misuse controls. Every normal form equals reference flattening, including a triple-layer input whose result remains nested. Different witnesses and premise order survive the comparison; the distinct-layering/noninjective-flattening regression is also exercised.

Remaining: prove a decreasing measure and local commutation/simulation for the admitted tree class, strengthen malformed-net rejection beyond trusted compilation, and compare a translated legacy fixture without claiming equivalence from these finite tests. No general confluence proof, arbitrary dependent-type implementation, or graph-sharing semantics is supplied yet.
