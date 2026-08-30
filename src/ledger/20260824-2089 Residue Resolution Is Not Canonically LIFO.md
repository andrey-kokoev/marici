# 2089 — Residue Resolution Is Not Canonically LIFO

A diamond of two legal operation paths joined by one coherence cell has a
canonical dependency DAG but six valid linear extensions. Any chosen extension
can unwind in LIFO order, yet the choice of extension is arbitrary.

Thus stack unwinding is a special execution strategy. The invariant residue is
a partial order with typed dependencies and higher cells joining branches.

Verification: dependency-free exact checker, 6/6 gates.

Epistemic event: ev-000000002867-3bd42223-ea67-4ef5-a3aa-f1523afc9c74.

Sequence claim: seqclaim-e7b359f6e33a09a704776c81.
