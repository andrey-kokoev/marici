# Mixed recurrent programme theorem and verification boundary

## Supported language

`ScanningSetProgram(w,P)` compiles a finite list of member(i), add(i), union(v), ifadd(i,t,f) and scan(c,F). Inputs are finite completed binary words/literals and nonnegative unary indices/fuel. Compilation allocates one release gate per instruction, not one per scan iteration. Scan is a particular cursor-advancing fuel-bounded recurrence, not a general loop body.

Status: consolidated written theorem, supported by executable bounded audits. No independent review, formal proof certificate or verified Python semantics is claimed.

## Theorem

For constructor-generated valid linear nets with monotone fresh allocation, every maximal sequence of actual enabled rewrites terminates. Instructions release once in program order. The final retained word is the sequential interpretation of P, and the fixed ordered observation roots contain the corresponding typed values: Boolean for member/ifadd, FOUND or EXHAUSTED for scan. Final ACK is attached to one DONE, with no residual control, operand garbage, cursor, fuel or private token. RET, ACK and all observation root identities are preserved.

For scan(c,F), test only when fuel is positive, consuming one unit per query. True returns FOUND; false inserts at c, increments c and repeats. Zero fuel returns EXHAUSTED without an extra query. Thus the last permitted false test still updates support. For ifadd, the recorded Boolean is from before the selected insertion.

## Proof by common completion interfaces

Use the finite strict-program boundary invariant: a complete support word and DONE meet the next release gate; all later gates/operands are passive; prior observation pairs are isolated. Each gate uses its external slots once and creates its isolated operation with result/acknowledgment continuations at the next gate or final roots. Cutting those two continuation peers to passive leaves commutes with internal rewrites, even when the uncut context has cycles.

GM/GA/GU satisfy this invariant by `strict-mixed-program-theorem.md`; GC by `finite-conditional-program-theorem.md`; GS by `fuel-scanner-phase-theorem.md` and `scanner-strict-successor-composition.md`. GS maps its six external slots bijectively to FUEL's six ports. Runtime NEXT restores the scanner's own boundary invariant with strictly less fuel, while keeping the program continuation passive. Only its terminal SEAL may forward final completion; early FOUND/EXHAUSTED cannot release the next instruction.

Each operation returns a completed word, its optional typed observation, one DONE and no owned work. Induction on instruction count proves correctness and cleanup. Each scanner invocation has at most its supplied fuel queries and updates; all inner phases terminate. Therefore no infinite actual-rewrite sequence exists. A host that stops issuing rewrites early is not a maximal reduction.

The final graph has q+2 rooted components and n_final+4+2q agents, where q counts member/ifadd/scan instructions. Components are RET plus word/NIL, ACK plus DONE and each observation root plus a single typed leaf. This accounts for every node, not merely every allowed kind.

## Schedule independence

`reachable-concurrency-confluence.md` classifies the eight possible concurrent rule families and proves root-fixed local diamonds under reachable phase invariants. With termination this gives unique normal forms modulo fresh names. `schedule-observation-contract.md` separately proves immutable published observations and final ACK iff normal form in the reachable domain. Publication step numbers need not agree: a two-cell member query publishes at step4,5 or6 across schedules, with the same step8 terminal result.

## Costs

Total cost is |P| plus isolated operation costs evaluated on each instruction's entry state. Member costs2n+i+3; add2i+2; union2n+1 if n<=m, otherwise2m+2; ifadd2n+i+2k+l+10 for selected k and rejected l. For scan sum its visited-boundary costs: false cycle2n+5c+14, true terminal2n+5c+r+18 for residual fuel r, zero-fuel terminal c+4. Compilation allocations are excluded. These formulas are written consequences of the component rule counts; the integrated regression does not independently check every mixed-program cost sum.

## Public observations

`observe()` returns ordered (type,value) slots, distinguishing None from false and EXHAUSTED. Published values remain immutable. Readiness is not instruction completion: member may precede cleanup, ifadd precedes selected insertion/cleanup, scan outcome precedes terminal erasure. `complete` refers only to the whole program's ACK, and word is exposed only then. Observation is read-only for ordinary single-threaded use, not an atomic snapshot against concurrent mutation or an imported-state validator.

## Fresh executable closure

Run `python research/voevodsky/checkers/check_recurrent_program_closure.py`. It now launches18 fresh assertion-enabled subprocess checks, separates interfaces, observation timing, resource preparation and semantics/composition, and records stdout/stderr and local Python source hashes in `results/recurrent-program-closure.json`. All18 passed on the schedule-observation integration rerun. Signature evidence covers57 legal typed-pair templates and199 rejected combinations; it is not arbitrary-context semantic verification. Bounded schedules and fixtures do not establish the theorem universally; the written induction supplies that claim under the stated premises.

## Remaining highest-value gap

The next assurance task is mutation sensitivity of this closure: show that representative wiring/early-ACK/typed-observation defects are actually rejected by the corresponding checks, without modifying production files in place. Use isolated temporary copies and record each mutation's intended obligation and failing assertion. This is more informative now than adding another language feature, and does not substitute for independent review or formal verification. Imported allocation recovery, transactional malformed-state safety, runtime multi-input sharing and unrestricted loop bodies remain excluded.
