# Executable gate projection audit

Fresh `check_gate_projection.py` implements the cut projection in the written gate proof. It keeps components reachable from the gate's support/return peers and the first OUT while excluding the gate, supplies passive RET/ACK leaves, and drops dormant second-call resources. The projected object uses the actual AcknowledgedMembership rewrite implementation, not the gate implementation.

Across 86 two-call fixtures (all words n<=2, both indices through n+1), all 8,578 first-call edges commute with projection exactly, including names and serial state. Enabled first-call redex sets agree exactly. The raw named-state search visits 8,664 states, with 1,674 ready states; these are not alpha-class counts. Forest canonicalization is used only to verify the projected graph's domain, never to quotient the cyclic whole graph. All ready projections have DONE, unchanged retained word and correct first answer.

This validates the executable bridge behind the written passive-context argument. Tests remain bounded; universal assurance comes from the interface proof, subject to independent review. Gate release itself already has a literal five-boundary rewiring table and previous schedule tests; no new general cyclic-net theorem is claimed.

Critical-path reassessment: the useful next milestone is a finite chain of strict acknowledged queries, not more two-call samples. Generalize the gate construction so each DONE releases exactly one subsequent query, with ordered immutable outputs and a final ACK. Prove induction on the number of gates using the same cut lemma, and test three-or-more calls with an explicit no-overtaking condition. Keep the scope membership-only until acknowledgment conventions for insertion and union are specified.
