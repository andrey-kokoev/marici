# Internal straight-line dataflow sequencing

## Delivered execution model

`checkers/sequenced_set.py` compiles a finite straight-line program of add(i), member(i), and union(literal_word) into one port graph. All unary indices, union inputs, consumers and output roots are wired BEFORE execution. The Python instruction list is not retained for runtime dispatch. Execution uses only existing principal-pair rules; there is no `start`, `insert`, `union_from`, global completion poll, or host-side rewiring between instructions. Diagnostic stage numbers influence test scheduling priority only, never enabledness or rule topology.

Compilation threads a linear support output through successive input boundaries:

* add: support enters AB.a; outgoing producer is AB.r.
* member: support enters COPY.p; outgoing retained producer is COPY.a; COPY.b feeds its query and a fresh OUT.
* union: support enters UL.p; its a receives a separately constructed literal operand; outgoing producer is UL.r.

The final producer is attached to RET. A producer auxiliary may initially meet a consumer principal or auxiliary. Such a connection is NOT an active pair. As a preceding rule materializes a B/N principal, the waiting consumer can fire. Thus data availability, encoded by wiring, is the internal sequencing mechanism. No new agent types are needed.

## Semantics and explicit limitations

This implements **dataflow sequencing, not a full-normalization barrier**. A later instruction can process an available prefix while an earlier instruction still copies or erases another branch. A membership output belongs to the support value at its position in the program: its private copy is not subsequently mutated by later insertion. The retained stream feeds the next stage. Union inputs here are literal independent words, not dynamically referenced previous result registers.

The prior single-operation proofs require completed input chains and at most one active operation; they cannot be cited unchanged as a proof of arbitrary pipeline execution. The new graphs may contain multiple COPY agents, producer-to-consumer waits, and boundary splicing from union. The old unified invariant deliberately rejects some of these graphs. What is delivered is an executable internal sequencing prototype with bounded tests, not a new blanket confluence theorem.

A proposed proof route is an acyclic stage dependency invariant: each support stream has one downstream owner; a blocked producer/consumer path runs only toward earlier stages; each stage denotes its sequential operation on a virtual completed input; materializing prefixes preserves that denotation. A producer-aware rank and a generalized interface commuting argument must handle UL--N splicing. These are open obligations. Dynamic conditionals, loops, explicit continuation tokens, full cleanup barriers and unrestricted concurrent shared registers are not implemented.

## Fresh tests

`check_sequenced_set.py` runs 858 six-operation programs:

    member(j); add(i); member(j); union([0,1,0]); add(j); member(i)

across all bit words of length <=3, indices through n+2 and forward/reverse stage priorities. All match an independent sequential word oracle and preserve prior query snapshot meanings. In 429 runs the observed rewrite trace returns to an earlier stage after reducing a later one, demonstrating real interleaving rather than concealed stage-by-stage host execution. Exact all-individual-redex exploration of four small programs covers 142 forest classes and 290 edges; each has one expected terminal class.

Next establish the pipeline-specific acyclic dependency invariant and semantic preservation, then prove normalization and confluence including union splicing. If the intended interface requires a strict completion barrier instead, implement a separate explicit completion protocol rather than relabelling prefix-demand execution as one.
