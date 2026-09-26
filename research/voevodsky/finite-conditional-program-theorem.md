# Finite conditional programme: theorem and observation contract

Status: written proof for `ConditionalSetProgram`, freshly inspected; not a proof-assistant certificate or independent implementation verification. This extends `strict-mixed-program-theorem.md` with ifadd(i,t,f), not arbitrary branch bodies or loops.

## GC boundary audit

GC(p,s,r,b,c,o,t,f)--DONE consumes its principal pair. Its seven external slots s,r,b,c,o,t,f map respectively to COPY.p, WAIT.r, QB.p, WAIT.c, WAIT.o, WAIT.t, WAIT.f. The remaining fresh ports occur in precisely four internal wires: COPY.a--WAIT.s, COPY.b--QB.a, QB.r--WAIT.b, QB.c--WAIT.p. Thus seven outside plus eight internal endpoints cover all fifteen fresh ports (COPY3+QB4+WAIT8), exactly once. This is a symbolic audit of the fixed wiring template, independent of operand lengths. It does not prove allocator freshness or malformed-context safety.

The fresh topology is exactly the isolated conditional constructor with query Boolean redirected to WAIT.b, retained support to WAIT.s and query completion to WAIT.p. In particular, there is no OUT simultaneously sharing the query Boolean wire. WAIT.o preserves the external OUT identity and PICK later creates its snapshot leaf. Compile-time GM replacement preserves each peer independently; adjacent replacements reconnect to the current neighboring gate, not a stale stored peer. After compilation, every instruction has its own completed operands and distinct result/acknowledgment continuation ports.

## Induction invariant and semantics

At each instruction boundary there is one completed retained word and one DONE, all prior snapshots are isolated immutable pairs, and the suffix contains only dormant gates, operands and unfilled OUT roots. All suffix principals except the first face predecessor c auxiliaries. A release instantiates exactly its operation; its result/acknowledgment boundaries face the next gate or final RET/ACK.

The GM/GA/GU cases follow the strict mixed theorem. In the GC case, cut the next gate's s,p into passive RET/ACK leaves. External-port rewiring commutes with the cut; the whole cyclic graph need not be a forest. The isolated conditional theorem gives query completion before selection, exactly one selected insertion, erasure of the rejected unary budget and consumption of both local completion tokens before final DONE. It also returns one correct immutable Boolean snapshot. Therefore the same boundary invariant is restored for the suffix, including consecutive GC instructions.

Induction establishes sequential interpretation of any finite list over member/add/union-literal/ifadd. For ifadd, evaluate membership in the word at entry, then insert at t if true or f otherwise; record the pre-insertion Boolean. Termination of each isolated region plus the finite instruction count implies termination of every maximal actual-rewrite sequence. There is no remaining garbage: each instruction accounts for its operands, and the final rooted components are RET plus word/NIL, ACK plus DONE and one OUT/Boolean pair per member or ifadd. Their total agent count is n_final+4+2q, with q the number of observations. Root identities are unchanged.

Exact cost is one release per instruction plus each isolated cost. For ifadd it is 2n+i+2k+l+10, where k is the selected index and l the rejected index. Costs for other instructions are as in the strict mixed theorem. All counts exclude compile-time allocation.

## Public observations are not completion barriers

The ordered `outputs` list is fixed at compilation. Before an instruction publishes its Boolean, its OUT faces a gate or WAIT auxiliary, not a Boolean; callers must not treat that as false. Once a TRUE/FALSE leaf reaches OUT it remains unchanged for the rest of the program.

Ordinary member can publish its Boolean before COPY/EA cleanup ends. Conditional ifadd publishes its Boolean only at PICK, after the initial query's full completion, but in the same rewrite that creates the selected insertion and rejected-budget EA. Therefore its visible Boolean certifies the query snapshot, NOT completion of its insertion or rejected cleanup. Even when t=f or one budget is empty, publication is not final acknowledgment.

A following instruction may begin only after that conditional's JOINR emits DONE and its next gate consumes it. Final ACK is the program-completion signal, not an individual result-ready signal. RET is a final-result interface: during execution it may face a dormant gate or an unfinished producer; observing a complete-looking prefix does not replace ACK. Internal gates' DONE tokens are private, consumed control resources, not duplicable public events.

## Assurance and next step

The existing bounded tests support this theorem but do not quantify over all graphs or schedules. Imported allocation state, failure-safe mutation, arbitrary branch bodies, loops and shared-register concurrency remain outside scope.

The next useful executable obligation is an observation API that distinguishes pending from false and separates snapshot readiness from final ACK, with prefix-time tests (including a visible conditional result while rejected cleanup is deliberately delayed). This avoids a real client-level semantic error that final-state tests alone cannot catch. It is more useful than another round of final-state scheduling samples.
