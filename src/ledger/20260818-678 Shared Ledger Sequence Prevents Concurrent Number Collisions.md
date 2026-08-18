# Entry 678: Shared Ledger Sequence Prevents Concurrent Number Collisions

Concurrent Marici agents previously selected ledger numbers by observing the
largest visible filename. That procedure has no serialization point: branches,
worktrees, and simultaneous turns can observe the same maximum and create
colliding entries.

The ledger now has a site-owned monotonic sequence in the directly admitted
epistemic-graph binding:

\[
\texttt{marici-ledger-entry},
\qquad
\text{sequence ID }\texttt{seq-3475727b9d10d9e7689ae83e}.
\]

The sequence began at \(678\), immediately after the audited maximum \(677\).
This entry consumes the first permanent claim:

\[
678
\quad\text{with claim ID}\quad
\texttt{seqclaim-9ecd098a38265610fc67d59f}.
\]

The operational invariant is:

\[
\boxed{
\text{claim from the shared sequence before assigning a ledger filename}
}
\]

Allocation authority is therefore independent of filesystem visibility and
Git topology. Claims are monotonic, permanent, and non-reusable. An abandoned
claim remains a gap rather than becoming available to another entry. Repeated
submission of the same allocation intent is controlled by its idempotency key.

The complete caller protocol is recorded in
`docs/ledger-sequence.md`. Sequence status and claim history remain available
through the epistemic graph's typed sequence-management commands.

This removes ledger-number selection from informal inter-agent coordination:
agents may still work concurrently, but they cannot legitimately derive an
entry number from a directory scan or from the latest number mentioned in
conversation.
