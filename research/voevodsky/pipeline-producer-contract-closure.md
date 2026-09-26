# Producer contracts and pipeline closure

Status: written structural argument for compiler-generated straight-line pipelines. Not a proof-assistant certificate. This document replaces the head-only predicates as the proposed proof specification; existing validators check projections of it, not its entire global coverage clause.

## 1. Stream contracts

A stream is a physical directed path starting at a receiving port's peer. It visits only data principals, leaving data through a, until reaching NIL.p or a declared producer output. Paths are finite and disjoint in their data nodes. Multiple paths may end at the two distinct outputs of one COPY, but must not share either output port. This is physical linearity, not virtual expansion of COPY's input twice.

Define S_t (public support at ceiling t) as a B0/B1 prefix, with each data node labelled <=t, ending in NIL with label <=t or a public producer output of stage <=t. Stage -1 permits only original literal data, no producer. Public outputs are COPY.a and insertion/union control r. Define P_t (private copied support) as B data of stage t ending in stage-t NIL or COPY.b of the unique stage-t COPY. K_t is a complete K/N budget with all nodes stage t. L_t is a complete B/N literal with all nodes stage t. Let A_t be a B prefix with labels <=t ending in NIL <=t or a public producer of stage STRICTLY LESS than t. Thus A_t allows insertion-created stage-t NIL but no self-stage producer wait. Producer control cardinalities follow the compiler: each stage has one operation kind, at most one COPY and one Q for membership, or at most one insertion/union control for those operations; E agents may remain from membership.

These stricter public/private contracts prevent a later stage from taking the private query stream. They are stronger than scalar stage comparisons alone.

## 2. Input/output judgment table

| Stage-t live control | Inputs | Output contract |
|---|---|---|
| COPY | p: S_(t-1) | a: S_t; b: P_t |
| QB | p: K_t; a: P_t | r to its fixed OUT |
| QS | p: P_t; a: K_t | r to its fixed OUT |
| QR | p: P_t | r to its fixed OUT |
| E | p: K_t or P_t | none |
| AB | p: K_t; a: A_t | r: S_t |
| AS | p: A_t; a: K_t | r: S_t |
| AR | p: A_t | r: S_t |
| UL | p: S_(t-1); a: L_t | r: S_t |
| U0/U1 | p: L_t; a: S_(t-1) | r: S_t |

Initially AB's saved input is S_(t-1), which embeds into A_t. QB/QR private streams never escape their stage. E budget-vs-support origin is a proof annotation propagated when spawned; it is not selected by an external oracle. K and L streams contain no producer waits.

## 3. Global coverage and construction

Every live data node belongs to exactly one input stream from the table, or the final RET stream; every producer output is consumed exactly once, either immediately by such a stream root or after its data prefix. Every control is of its stage's declared operation kind (plus membership Q/E), every OUT meets its own Q.r or BOOL.p, and all BOOL nodes belong to these OUT pairs. Every producer's input paths are independently represented by the table, not recursively included as nodes of its output path. There are no other agents or unattached components. The graph is a port-linear forest with fixed arities and finite immutable stage labels.

The compiler establishes this judgment by induction on instructions. Each instruction takes the preceding public S_(t-1), creates its own finite budget or literal, and exports S_t. Membership additionally makes one private COPY.b-to-Q path and OUT; union makes no private query path. The final S_(last stage) is attached to RET. Freshly allocated nodes and linear boundary wiring give disjoint streams and no cycles. An empty program has RET attached directly to the initial word.

## 4. Substitution lemma

If a public stage-t frontier is replaced by a stream satisfying S_t, any public context admitting that frontier remains valid: its ceiling is >=t and the prefix ownership is unchanged. A stage-t private COPY.b frontier may only be replaced by P_t, not by arbitrary S_t. Distinct data paths cannot merge during substitution because every boundary slot is used once and the source forest puts distinct removed-pair boundaries in distinct outside components.

The only direct splice, UL--N, joins its r context to its a stream. They are distinct outside components of the removed pair; otherwise the old graph had a cycle. Thus the splice creates no cycle, preserves linear coverage, and exposes L_t, which embeds into S_t. This explicitly extends the earlier no-splice context argument for this rule.

## 5. All rule families preserve the contracts

**COPY:** its input B head and suffix have ceiling t-1. COPY--B emits two stage-t B nodes; the public tail ends at new COPY.a, the private tail at new COPY.b. The successor COPY consumes the unchanged S_(t-1) suffix. COPY--N supplies stage-t NIL at both outputs. Both substitutions meet their distinct contracts.

**Query and eraser:** QB--K exchanges a P_t input and K_t suffix into QS's declared ports. QB--N creates QR on the P_t input. QS--B exchanges the P_t suffix and saved K_t into QB. QS--N gives its K_t tail to fresh E; QR--B gives its P_t suffix to fresh E; both keep BOOL at the original OUT. QR--N leaves only BOOL--OUT. E advances along its K_t/P_t path, or vanishes with NIL. All suffixes retain their types, and any private frontier remains COPY.b of that same stage. Consuming a head cannot affect another stream by disjoint physical ownership.

**Insertion:** AB--K moves A_t/K_t inputs to AS; AB--N moves A_t to AR. AS--B emits a stage-t bit into S_t and leaves fresh AB.r at its end; its saved input is the old A_t suffix. AS--N does the same but supplies a stage-t NIL as AB's A_t input. AR--B/N emits B1 and returns the remaining A_t suffix or new NIL. A_t embeds into S_t, so the forwarded suffix is valid for every downstream public client. No same-stage dependency is introduced into the control's input.

**Union:** UL--B saves S_(t-1)'s successor in U_b.a and moves the L_t right stream to U_b.p. U_b--B emits a stage-t OR bit ahead of new UL.r, passing the same two stream suffix contracts to UL. U_b--N emits its remembered stage-t bit followed by the saved S_(t-1) suffix, valid in S_t. UL--N directly returns L_t as covered by the splice lemma.

All replacement control counts respect the stage cardinality restriction. All consumed data leave their old path; all new data belong to exactly one replacement path. Splitting a query into BOOL and E creates no unowned remainder; deleting E--N deletes its entire path. Output boundary preservation and the splice lemma therefore preserve global coverage as well as the local table. Fresh name allocation is still a separate executable high-water premise. This is a simultaneous closure argument for the written compiler-specific contracts, not a claim that the old single-COPY validator accepts pipelines.

## 6. Progress and final shape

A blocked principal at stage t either waits on a public producer with strictly earlier stage, or a private query/E waits at its own COPY.b. Every other declared principal faces admitted B/K/N. Ordering controls by (stage, COPY-before-others) makes every blocking dependency strictly descend. A minimal live control is therefore active. If no control remains, global coverage leaves only a complete RET B/N word and one BOOL--OUT pair per member instruction: budgets/literals cannot survive as orphan components because their consuming control would be absent.

Together with the finite-production induction, this provides a written normalization argument: insertion is budget-bounded, union is bounded by its finite right literal, and COPY consumes only finitely produced earlier-stage data; Q/E consumes its finite private copy and budget. This does not yet establish that the final word and all snapshots equal the sequential program denotation. That semantic simulation is now the highest-value remaining proof. General local diamonds with splicing are another independent route to normal-form uniqueness; semantic correctness plus the stated canonical terminal shape may suffice for observable uniqueness, but must be argued rather than assumed.
