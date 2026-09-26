# Pipeline minimal-rank progress

Critical path remains preservation of the causal phase interfaces, because it supplies progress and supports finite-production termination. Added `pipeline_phase_interfaces.py` covering both active principals and saved auxiliary tails. Budget heads are same-stage K/N; union right heads are same-stage literal B/N; saved support can be data from the same/earlier stage or an admitted producer port. Same-stage producer waits are confined to membership Q/E facing COPY; COPY itself must face strictly earlier-stage data/producer. The validator is deliberately a necessary interface predicate, not a full graph grammar.

## Conditional progress theorem

Assume a finite live graph satisfies these principal conditions and that every waiting endpoint is a live producer in the control signature. Rank each live control by (stage, role), with COPY role 0 and every other control role 1. A blocked control waiting at an earlier-stage producer has a strictly smaller-rank live control. A same-stage blocked control can wait only at COPY, also of smaller rank. Every control either waits this way or faces one of its admitted data principals. A minimal-rank live control therefore cannot wait and must form an enabled pair. Thus a graph satisfying the conditions cannot be stuck while any control remains. This proof is independent of input length and does not assume schedule fairness.

This proves an implication, not universal reachability of the hypotheses. It also does not rule out malformed passive residual components when all controls are gone: output/stream coverage is a separate clause.

Fresh test: 858 six-stage programs, 49,912 visited state occurrences under forward/reverse priorities, all phase and saved-tail conditions plus the minimal-control active witness pass. These tests do not prove rule preservation.

## Exact next bridge

To prove preservation, data successor ports must also carry stage/type constraints. Merely inspecting a consumer's current head does not constrain the successor exposed when that head is removed. Derive recursive stream inequalities: successor provenance cannot rise above its head's stage except at explicitly typed producer frontiers, whose producer stage is bounded by the consuming interface's stage. Particular care is needed for insertion-created same-stage NIL, membership private COPY.b, and UL--N forwarding a same-stage literal suffix to a later consumer. State per-stream ceilings, rather than assuming every edge decreases allocation stage. This is the next universal closure obligation; do not promote the progress implication into a completed pipeline theorem prematurely.
