# Strict completion barrier: contract and premature-signal counterexamples

Critical path for adding barriers is defining what the signal certifies, before inventing a token. This is a new semantic extension; the existing dataflow theorem does not require or implement it.

## Three distinct predicates

1. Head-ready: RET's peer is a B/N principal. This enables streaming but says nothing about the remaining tail.
2. Value-ready: the complete retained B/N chain exists and the stage's result OUT is BOOL. This does not certify garbage erasure.
3. Strict stage completion: every computation agent owned by that operation, including detached erasers, has disappeared; retained word and specified outputs are complete. Unrelated earlier/later work is outside the scope unless explicitly included in the barrier.

A sequential strict barrier must not release the next operation before predicate 3 holds for the protected operation. Safety is required for every schedule. Eventual release can only be required under continued execution/fairness of enabled protocol work; no local token can force an external scheduler to act. Logical operation identity and linear ownership must be explicit, not an implicit scan of diagnostic stage metadata.

## Executable witnesses

Fresh `check_premature_completion.py` explores a legal one-query net on [1,0], member(0), and stores exact wires and named redex traces in `results/premature-completion.json`. Eleven classes suffice:

* After one rewrite, RET has a bit head but the tail still ends at COPY.
* After three rewrites, the Boolean answer is present while COPY still exists.
* After five rewrites, both the full RET word and Boolean exist, but a detached E remains.

These refute head-only, Boolean-only, and even full-word-plus-Boolean readiness as strict-cleanup barriers. The last case is especially decisive: disconnected garbage cannot notify a boundary after it has been erased unless a communication path was installed beforehand.

## Necessary protocol change

Existing E--N removes both unary agents and produces nothing. Once a garbage component is detached, no endpoint remains through which it can signal completion to the result boundary. A sound local protocol must preserve a return/acknowledgment wire through garbage generation and erasure, or explicitly weaken completion to exclude garbage. Polling all graph nodes for stage absence is a host oracle, not an interaction rule.

A candidate extension is a return-bearing eraser with an acknowledgment auxiliary, forwarding that wire along B/K and emitting a done token on NIL. Query finalization must route the done dependency either through that eraser or directly when no tail exists. COPY also needs a retained-stream completion acknowledgment; Boolean or erase completion alone does not establish COPY exhaustion in all cases. A join must consume both linear acknowledgments before opening the continuation. Detailed port tables, no-early-release proof, and liveness are not yet supplied.

Next design the acknowledgment-carrying eraser and query-finalization interface first, including the no-garbage branch. Prove exactly one acknowledgment and only after cleanup, before integrating COPY completion and the join. This is the highest-value missing causal path, not another search for larger premature examples.
