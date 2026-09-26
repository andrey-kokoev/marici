# Forest gluing and root partitions for arbitrary contexts

## Generic graph lemma

Let G be a finite port multigraph forest. Let R be the connected two-agent subgraph of an active principal pair. Remove R and its incident wires, recording each auxiliary boundary slot and its outside peer. Distinct boundary slots have peers in distinct components of G-R: otherwise the path in that outside component, together with the path through R, would yield a cycle in G (including the parallel-edge case). Therefore each outside component meets at most one slot.

Replace R by a finite fresh forest H with each boundary slot attached exactly once to a port of H, all new ports paired internally or at these attachments. Gluing H to those outside components cannot create a cycle. Indeed contract each outside tree to a vertex; every such vertex has degree at most one toward H. Adding pendant vertices to a forest preserves acyclicity. Components unrelated to R are unchanged. Full port incidence follows from the exactly-once interface conditions. This proves forest preservation for arbitrary outside tree sizes, not a finite sample of contexts.

The conclusion is only topological: it does not alone preserve phase types, original ownership, output count, or root coverage.

## Root-partition criterion

For each component h of H, collect the boundary slots attached to h. The resulting glued component is rooted iff h contains a surviving/new root or at least one outside component at those slots contains a root. A replacement component with no boundary and no root is forbidden. An empty H (E--N) simply removes the isolated old component when R has no boundary. Root coverage elsewhere is unchanged.

This criterion explains why the old coarse COPY--N premise failed: H has two separate NIL components, neither locally rooted. Each of its two slots must independently bring an outside root. The per-COPY-side anchor clause supplies exactly this. A single root in the entire original connected component would not suffice.

## Application to the fifteen templates

* COPY--B0/B1: H is a connected tree with two new bits and a new COPY. Its three boundary slots receive the two rooted consumer sides and the original source tail. Root coverage is immediate; cutting the new COPY again separates those two rooted sides from the source.
* COPY--N: H has two unary NIL components; each attaches to its independently rooted consumer side.
* Q_B--K, Q_B--N, Q_S--B0/B1: H is one query agent with all its external slots attached; the OUT boundary supplies a root. The replacement changes port roles but retains the outside-component connectivity partition.
* Q_S--N, Q_R--B0/B1: H has BOOL and E components. The BOOL component attaches to OUT; E is itself a root of the remaining budget/support side.
* Q_R--N: H is BOOL attached to OUT.
* E--B0/B1/K: H is E, already a root, attached to the old data successor.
* E--N: H is empty and the old pair was an isolated component.

Together with the typed boundary tables, this closes the generic forest/root-coverage context argument in written form. The outstanding integrated check is preservation of the more specific COPY-cut partition and original/source exclusion across non-COPY rewrites, not just ordinary component roots. Next make the root partitions executable from production replacement AST and review those stronger clauses as a separate obligation. No complete arbitrary-n normalization theorem is claimed here.
