# Cut-interface simulation for the strict two-call gate

Status: written proof for the specific GatedMembership constructor and rules, not arbitrary cyclic graphs or machine-certified Python semantics. Fresh source inspected: `checkers/gated_membership.py`.

## Cut invariant before gate release

Let g be the unique GATE. Partition its ports into first-call interface {s,p} and dormant resources {r,b,o,c}. The first call attaches its retained-support endpoint to g.s and its cleanup-return endpoint to g.p. Its own OUT remains separate. Dormant resources are: g.r--RET, g.b--the second finite K/N budget, g.o--second OUT, g.c--ACK. These four resources have no consumers and cannot reduce. They are pairwise disjoint and have no path to the first call except through g.

Define projection pi by deleting g and all dormant resources, attaching a fresh passive RET leaf to the former s peer, and a fresh passive ACK leaf to the former p peer. Keep the first OUT and all first-call agents. The result is precisely an acknowledged single-call graph, initially the original constructor. The projection is a proof device, not an executed rewrite.

The combined graph may have a cycle through g, but cutting the two interfaces separates it. No forest claim about the combined graph is required.

## Step simulation until DONE

Every enabled pair other than GATE--DONE lies entirely in the first-call region: dormant resources contain only K/N and passive roots. Replacing a first-call pair neither removes g nor reads its other ports. If a removed auxiliary has g.s or g.p as outside peer, `replace` reconnects that same port to the fresh endpoint. Under pi this is exactly the corresponding reconnection to RET or ACK. All other incidences are identical. Fresh names can be matched by local allocation slots; the extra dormant budget changes initial serial values but not rule choices.

Therefore each non-gate step projects to exactly one legal acknowledged single-call step, and conversely every projected redex exists in the combined graph. The cut invariant is preserved inductively, including when one first-call pair has both support and return paths connected into the gate context. Those are distinct outside port endpoints; the executable replacement does not conflate them merely because their agent is the same g.

Before acknowledgment, g.p meets a query c auxiliary or EA.r auxiliary, so it cannot form the GATE--DONE principal pair. When it meets DONE.p, the projection has reached acknowledged completion. The single-call NIL argument in `query-acknowledgment-subsumes-single-copy-completion.md` then implies complete support, correct first Boolean, no COPY/query/eraser. Thus gate eligibility implies strict first-call cleanup, not just an early value.

## Release and second call

GATE--DONE removes those agents and creates COPY/QB with the five surviving boundary peers: support becomes COPY.p, RET becomes COPY.a, budget becomes QB.p, second OUT becomes QB.r, ACK becomes QB.c, with COPY.b--QB.a internal. Each peer is distinct, and each external/new port occurs once. The resulting active component is an acknowledged single-call constructor on the retained word and the second budget, alongside the immutable first BOOL--OUT component. Freshness follows from the same monotone allocator premise. There is exactly one gate and it is consumed, so release occurs at most once.

## Termination, safety and liveness

Before release, only first-call steps occur and the projection terminates after 2n+i+3 rewrites. Its terminal DONE enables the gate, so a maximal reduction cannot stop there. One gate step starts the second call, which terminates after 2n+j+3 rewrites. The total is 4n+i+j+7. Every maximal actual-rewrite sequence therefore completes both calls; no fairness is needed because there is no infinite sequence of competing enabled work. A host scheduler that stops issuing steps can of course prevent release.

The retained word and both answers follow from the two single-call correctness arguments and the cut simulation. This gives a written strict two-call barrier theorem despite the transient cycle. It does not establish arbitrary barrier composition, dynamic branching, or safe mutation of malformed graphs. Next test pi explicitly against executable first-call edges to audit the proof/implementation correspondence, with observable boundary identities preserved rather than using forest canonicalization on the cyclic whole graph.
