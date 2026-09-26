# Boolean-dependent insertion with cleanup-safe completion

Status: fixed-signature rule specification and written safety argument; implementation pending. Scope is one retained membership query followed by add(t) if true, otherwise add(f), with both unary alternatives prewired. This is data-dependent control, not arbitrary branch syntax or loops.

## Interface and constructor

Begin with an acknowledged query on complete word w at index i. Replace its OUT root with a Boolean input to WAIT; replace its ACK root with WAIT.p; replace RET by WAIT.s. Preserve the external RET, ACK and a fresh OUT root as WAIT.r, WAIT.c and WAIT.o. Attach completed unary budgets t and f to WAIT.t and WAIT.f. Thus WAIT(p,b,s,r,t,f,o,c) has principal p waiting for query DONE and auxiliary b waiting for the query Boolean. All roots are distinct linear endpoints.

The query Boolean must not be connected to OUT and WAIT simultaneously. The query now supplies only WAIT.b. The selected branch rule below creates a fresh Boolean snapshot for OUT, preserving the observation without illegal wire sharing. Query completion already implies that its Boolean exists, but the runtime still checks only principal pairs.

## Rule tables (letters denote fresh agents)

In these tables an old auxiliary port denotes its outside peer, exactly as `replace` does. Each external endpoint and every fresh port appears once.

1. WAIT--DONE: create PICK(p,s,r,t,f,o,c), connect
   b--PICK.p, s--PICK.s, r--PICK.r, t--PICK.t,
   f--PICK.f, o--PICK.o, c--PICK.c.
   Consume both old agents. This is a local completion latch; no support traversal occurs.

2. PICK--TRUE/FALSE: let selected = t/f and rejected = f/t, respectively.
   Create A=ABc(p,a,r,c), E=EA(p,r), J=JOIN(p,a,c),
   and V=TRUE/FALSE(p) matching the consumed Boolean. Connect
   selected--A.p, s--A.a, r--A.r, A.c--J.p,
   rejected--E.p, E.r--J.a, c--J.c, o--V.p.
   Consume PICK and the original Boolean. Only one insertion controller is allocated.

3. JOIN--DONE: create J2=JOINR(p,c), connect a--J2.p,
   c--J2.c. Consume JOIN and the selected insertion's DONE.

4. JOINR--DONE: create D=DONE(p), connect c--D.p.
   Consume JOINR and the rejected-budget cleanup's DONE.

There are five typed new rules (one WAIT, two PICK, one JOIN, one JOINR), plus existing ABc/ASc/ARc and EA rules. JOIN deliberately waits for insertion first; cleanup can finish in either order. A cleanup DONE at JOIN.a is principal-to-auxiliary, hence passive until JOIN's rewrite promotes it to JOINR.p. No multi-principal matching or global emptiness check is needed.

## Ownership and cut argument

Before WAIT fires, all budgets are complete and unconsumed. WAIT.b and WAIT.s are passive boundaries of the acknowledged query. Cut these and WAIT.p into the query's OUT/RET/ACK leaves: query rewrites simulate the isolated operation. In particular, no support update starts on an early Boolean. WAIT can meet DONE only after COPY/query/EA exhaustion and complete retained support.

After WAIT--DONE the Boolean principal meets PICK.p; there is exactly one enabled choice rule, determined by that Boolean. After selection, insertion and rejected-budget EA have disjoint active regions. Their only shared context is JOIN, at distinct ports p and a. Cut both acknowledgment interfaces into passive leaves: the regions reduce independently. Neither can rewrite the other's input or consume its DONE. The ordinary insertion postcondition certifies complete updated support; EA certifies destruction of exactly the rejected unary chain including its NIL.

JOIN consumes insertion DONE but cannot issue final DONE. JOINR consumes cleanup DONE and emits the sole final DONE. Therefore final ACK implies both selected insertion completion and rejected-budget exhaustion; it also implies original query completion, no outstanding branch controller, and the correct preserved Boolean snapshot. Returned support, snapshot and final DONE are the only live result components. This argument assumes constructor-generated linear inputs and fresh replacement, not arbitrary cyclic contexts.

## Semantics, liveness and exact cost

Let b = (i<|w| and w[i]=1), k = t if b else f, and l the other budget length. Final support is add(k,w); OUT is b. Query takes 2|w|+i+3 steps; WAIT and PICK take two; selected insertion takes 2k+2; rejected cleanup takes l+1; JOIN and JOINR take two. Total = 2|w|+i+2k+l+10 actual rewrites. Both budgets may be empty or have equal lengths; their agents must still be distinct.

Each active region terminates by its existing measure. JOIN may wait while cleanup proceeds, or cleanup DONE may wait passively for insertion. Neither ordering deadlocks, so every maximal actual-rewrite sequence reaches final ACK. No fairness is needed to rule out infinite rewrite sequences. The host can of course stop issuing steps.

## Implementation obligations

Implement as a separate bounded conditional prototype reusing the existing acknowledging query and strict insertion rules. Validate rule-slot linearity, root identity, Boolean value and branch selection, exact count, absence of final ACK during either remaining workload, and final absence of rejected budget/branch controls. Force both cleanup-first and insertion-first schedules and include out-of-range queries, empty support, zero and equal branch indices. Then test embedding the final acknowledgment into a subsequent strict gate; do not assume this constructor proves arbitrary nested branch composition.
