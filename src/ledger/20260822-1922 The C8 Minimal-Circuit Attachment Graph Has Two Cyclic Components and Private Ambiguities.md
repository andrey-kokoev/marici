# 1922 — The C8 Minimal-Circuit Attachment Graph Has Two Cyclic Components and Private Ambiguities

## Frozen object

Expand the 36 free cyclic rank-four source orbits to their 288 labelled occurrences. For each occurrence retain every primitive support-minimal dependence among its seven partial-energy normals. Identify two circuit nodes only when their labelled primitive relations agree up to global sign.

This constructs the bipartite support-attachment graph

\[
\mathcal G_{\rm att}
=
\{\text{labelled occurrences}\}
\longleftrightarrow
\{\text{labelled minimal-circuit supports}\}.
\]

No residue orientation or physical-current coefficient is inserted.

## Exact census

The graph has

\[
288\ \text{occurrence vertices},
\qquad
182\ \text{circuit vertices},
\qquad
1520\ \text{attachments}.
\]

It decomposes into exactly two connected components, each containing

\[
144\ \text{occurrences}
\quad\text{and}\quad
91\ \text{circuit supports}.
\]

A one-site cyclic rotation exchanges the two components; a two-site rotation preserves each component. Thus the support attachment retains an occurrence-polarity doublet even though the complete source is cyclic.

## Private ambiguous circuits

Among the 182 labelled circuit supports, 32 occur in exactly one source occurrence. All 32 have mixed regulator sign on the positive regulator cone.

Therefore

\[
\boxed{
\text{ordinary equality-of-boundary pairwise sewing cannot cancel every C8 chamber ambiguity.}
}
\]

Any complete cancellation must use a higher source-derived coherence map connecting nonidentical circuit supports, or a physical-current identity stronger than pairwise support identification. Neither is constructed here.

## Narrow consequence

The naive pairwise sewn comparison is falsified. This does not prove that the full Bunch--Davies observable is ambiguous: the canonical-form source may contain higher residue/Čech coherence. It does prove that such coherence cannot be replaced by scalar summation or by matching identical circuit equations.

Classification:

- carrier: existing labelled C8 incidence carrier;
- coefficient: Entry 1918's rank-one complex fold lines;
- derived support object: two-component minimal-circuit attachment graph;
- missing datum: higher sewing/current coherence;
- new carrier primitive: unsupported.

Allocator claim: `seqclaim-01abe97e932dc2a4bca91bab`.

Artifacts:

- `research/benincasa/checkers/eight_site_rank4_circuit_attachment_graph.py`;
- `research/benincasa/results/eight-site-rank4-circuit-attachment-graph.json`.
