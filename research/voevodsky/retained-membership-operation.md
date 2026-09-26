# Retained membership: specification, proof and sequential composition

## Delivered interface

`checkers/retained_membership.py` implements (w,i) -> (w,M(w,i)) with the same COPY, query and eraser rules as the restricted system, plus a passive unary RET boundary. `start(i)` plugs a COPY and one query into the *actual* chain currently attached to RET; it does not save or rebuild the input word. COPY.a feeds RET and COPY.b feeds the query. Previous BOOL--OUT results remain untouched. Inputs are bit words and nonnegative unary indices.

`start` is caller-side graph composition, NOT a reduction rule. It requires the preceding operation to have fully normalized. Internal autonomous sequencing and overlapping calls are not provided. Agents have fixed kinds and fixed arities; numeric allocation suffixes are names, not index payloads. The unary K chain represents the index.

## Strengthened invariant for the retained branch

In addition to the restricted theorem's data typing, port forest and original-source discipline, distinguish the COPY.a side: its only root is RET, and it is exactly RET--a finite copied bit prefix ending at COPY.a. COPY.b belongs to the ordinary query/eraser side. After COPY disappears, RET is attached to a complete finite B/N chain. The value of the retained path while copying is its copied prefix concatenated with the original suffix. Passive prior BOOL--OUT components are allowed. Replace the former two-output root clause by RET plus live-query/prior-result OUT roots and E roots.

At call entry the previous complete RET chain becomes the logical original suffix of the new call. This reassignment is a proof annotation; it changes no agent kind. A fresh query budget and OUT are attached to the other copier side. Their names are above the global serial high-water mark.

## Closure and preservation proof

The constructor of a call joins the original chain, passive RET boundary, and one disjoint query/budget/OUT tree through COPY, forming a tree. Cutting COPY exposes precisely these three sides. COPY--B removes one original bit, extends the RET prefix and query-side prefix by that same bit, and gives the original tail to fresh COPY. COPY--N closes both sides with fresh NIL. Therefore retained-prefix-plus-source remains w, and the RET side stays passive and independently rooted.

No non-COPY rule can act on the RET branch: it contains only RET and data, with no active consumer. In particular the copied head has its principal attached to RET or another bit auxiliary, never E/Q. All Q/E redexes lie on the other COPY side or a detached component. The restricted theorem's forest gluing, phase typing and root-transfer cases apply unchanged there. They cannot acquire a wire into the RET branch or source because replacements use only the redex's existing outside slots; the three COPY-cut components are separate. Query termination gives a BOOL--OUT and possibly an E root on its remaining tail. Prior BOOL--OUT components are unary closed pairs, so no rule touches them. This proves closure of the strengthened invariant and retained-value preservation in arbitrary finite contexts of this shape.

## Progress, termination and answers

With COPY present its source principal is active. Without COPY, any Q/E has admitted principal data and is active. No-active-pair states therefore contain the completed RET word and all Boolean output pairs, and no garbage: every other component needs Q/OUT or E root, and all OUTs now belong to closed Boolean pairs.

Use P=3O+C, counting original and all non-original B/N/K nodes in the current call. Each rewrite reduces P by one as before. At entry P=3(n+1)+(i+1)=3n+i+4. At completion the only data are the retained n+1 nodes, hence P=n+1. Exactly **2n+i+3 rewrites** occur. At intermediate stages RET's preserved virtual word has length n, so P never falls below its terminal residual n+1. The general natural potential already suffices for termination. Local diamonds use the same deterministic, fresh, exactly-once rule interfaces; adding passive RET and old results does not alter the argument. Thus normal form is unique modulo fresh names.

The query-side virtual support is interpreted by following COPY to its original suffix. Q_B/Q_S/Q_R meanings are M(s,k), M(s,k+1), M(s,0); existing semantic rule equations apply unchanged. The retained branch is not queried or erased, so noninterference is stronger here. Consequently the new output equals M(w,i), and RET returns w unchanged as a word, though its allocated nodes are fresh.

## Sequential composition

The postcondition supplies exactly the precondition for another `start(j)`: a complete RET word, no active consumers, preserved old result pairs and valid global allocation state. Induction over calls proves any finite sequential list of queries returns the same word and correct answers. Two calls take **4n+i+j+6** reductions, excluding caller-side interface plugging; k calls take sum_r(2n+i_r+3). This is a mathematical composition result for the explicit host-wired interface, not an implemented internal continuation calculus.

## Fresh evidence and assurance

`check_retained_membership.py` passes 2,426 two-call runs over all words n<=4, i,j through n+2 and two opposite priorities. It verifies the returned chain after each call, both answers including preservation of the earlier answer, exact step counts, and final agent count. Exhaustive individual-redex exploration of 31 small single-call fixtures gives 472 exact forest classes and 638 edges, each fixture with one correct terminal class.

This new implementation is a compact independent rendering of the table, not formal equivalence verification against the older scheduler. Written proof is for the specified rules and interface; tests support the implementation. Independent review/formal verification remains available assurance work. No `add`, union, concurrent reuse or physical superform encoding is supplied.

Next substantial milestone: specify and implement support-preserving local insertion `add(i)`, including the out-of-range extension convention. It must compose at RET and preserve the established query interface; do not confuse that new semantic choice with a theorem already proved here.
