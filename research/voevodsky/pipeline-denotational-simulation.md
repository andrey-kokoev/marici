# Denotational simulation of overlapping straight-line pipelines

Status: written proof conditional on the compiler-specific contract closure in `pipeline-producer-contract-closure.md`. Neither document is proof-assistant certified. This supplies the missing semantic arrow without assuming that stages finish in execution order.

## Well-founded interpretation

Interpret a B/N path by its finite bit prefix and endpoint. NIL denotes empty suffix. At a producer endpoint substitute that producer's residual word:

* COPY.a and COPY.b both denote its input word.
* AB.r denotes A(s,k), where s is its saved support and k its budget length.
* AS.r denotes H(s,k): for b::v return b::A(v,k), and for [] return 0::A([],k). Equivalently H(s,k)=A(s,k+1). Its s is the principal support, k the saved budget.
* AR.r denotes A(s,0).
* UL.r denotes U(s,t) on principal left and saved right words.
* U_b.r denotes U(b::s,t), with saved left suffix s and principal right t.

A is zero-extending insertion; U is zero-padded OR with max input length. A producer at stage t depends only on earlier public producers: insertion's A_t may contain stage-t materialized data but no stage-t producer; union's right literal is closed; COPY's input has ceiling t-1. Therefore recursive producer expansion is well-founded by decreasing stage. Private COPY.b references first enter their same-stage COPY, whose recursive input then strictly decreases. There is no appeal to normalization to define this interpretation.

Each query output has a live denotation even before BOOL exists. QB denotes M(s,k), QS denotes M(s,k+1), QR denotes M(s,0); completed BOOL denotes itself. Its private path is interpreted with the same producer expansion. RET denotes its current public stream word. E carries no observation.

## Local semantic preservation

COPY materialization replaces its virtual input b::s by an explicit b followed by a residual COPY denoting s on both outputs; NIL gives empty suffix. Q phase equations preserve M exactly as in the isolated membership proof, now for any virtually expanded s. A query step does not alter its COPY's input or public output.

AB--K replaces A(s,k+1) by H(s,k); AB--N replaces A(s,0) by AR. AS--B replaces H(b::v,k) by b::A(v,k); AS--N replaces H([],k) by 0::A([],k). AR materializes A(s,0) by writing one and retaining the suffix or introducing NIL. These identities hold even when the unconsumed suffix ends at an earlier producer.

UL--B replaces U(b::s,t) by U_b; U_b--B emits (b OR c)::U(s,v). U_b--N emits b::s. UL--N forwards t because U([],t)=t. The direct boundary splice preserves denotation even though it differs topologically from a fresh-node interface substitution.

E consumes only a uniquely owned private membership or budget path. No observable public path or live query path uses those same data principals; virtual sharing exists only at COPY input, which E cannot consume. Thus erasure leaves RET and every OUT denotation unchanged.

## Contextual substitution and snapshots

Physical consumer paths are disjoint, but virtual interpretations can mention a producer through both COPY outputs. This is harmless: the local equations replace that producer by an equal word at every occurrence. Every downstream residual operation is a total function of its input words, so equality is preserved under arbitrary surrounding A/U/M expressions. The producer dependency relation is acyclic, making this substitution finite. Therefore a rewrite at any stage preserves the complete observation tuple (RET word, ordered membership answers), including answers belonging to earlier program positions. This handles the case where later insertion has already started while an earlier query is still pending.

Initially recursive expansion of the compiled graph is exactly the sequential fold of the instruction list: add applies A, union applies U with its literal, and member records M while passing an identical COPY word onward. Consequently all intermediate observation tuples equal that sequential fold. Contract closure, progress and finite-production termination imply every maximal reduction ends with complete RET and BOOL--OUT observations, giving correct final word and snapshots under every actual-step schedule.

## Uniqueness and limits

Under global coverage the terminal graph contains only the RET bit chain and the fixed collection of BOOL--OUT pairs. These values and their distinguished OUT identities determine its port/kind graph up to fresh names. Thus semantic preservation and terminal shape give unique terminal graphs for each compiled program without needing a separate general splicing-diamond theorem. Every reachable descendant terminates with that same graph; any two descendants can therefore be joined there. This yields confluence on the constructor-reachable pipeline domain, not on arbitrary malformed or externally assembled graphs.

Do not extend this conclusion to runtime branching, loops, mutable shared registers, imported graphs with invalid allocation counters, or full-cleanup barriers. Stage/provenance and serial diagnostics are proof/execution metadata, not part of the observable graph equivalence. The current gap in assurance is executable checking of this recursive interpretation and independent review of the two written proofs, rather than more local head-only tests.

Next implement the interpreter above and compare RET plus every live OUT before and after reductions against the sequential oracle, explicitly allowing unfinished queries and multiple COPY frontiers. Use adversarial scheduling and preserve any counterexample. That is the highest-value implementation bridge now that the written semantic argument is explicit.
