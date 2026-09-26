# Strict mixed straight-line programme theorem

Status: consolidated written proof for constructor-generated `StrictSetProgram` nets, not independent review, proof-assistant certification or formal Python verification. Fresh source inspection confirms GU's literal operand is named b (the original specification's t has been corrected).

## Statement and premises

Let w be a finite binary word and P a finite list of member(i), add(i), union(v), with nonnegative finite unary indices and finite literal words. Construct the net using `StrictSetProgram(w,P)`. Assume valid linear wiring, fresh allocation as maintained by the constructor/monotone allocator, and the stated replacement semantics; do not import arbitrary mutated graphs. Every maximal sequence of actual enabled rewrites terminates, releases instructions exactly in list order, preserves the original RET/ACK and ordered query OUT identities, and ends with:

* RET attached to the sequentially interpreted support word;
* each query OUT attached to its Boolean snapshot at that instruction;
* ACK attached to one DONE;
* no gates, operation controllers, budgets or detached garbage.

Data words preserve their specified finite length, including trailing zeroes. Addition zero-extends to max(n,i+1); union produces length max(n,m). This is a single-register, literal-operand theorem, not runtime multi-input composition or shared-register concurrency.

## Cut-interface lemma for update operations

During one active insertion or union, remove the unstarted suffix of gates and its operands/outputs. Replace its first s peer by a passive RET and its first p peer by a passive ACK; if there is no suffix these are already the real roots. Earlier BOOL--OUT components can be retained unchanged. There are no other edges from the active operation to this suffix. Later gate principals face predecessor c auxiliaries; the first pending gate faces the active controller's c auxiliary. Thus the suffix has no enabled pair until DONE reaches its first p.

Every active replacement uses boundary endpoints, not reachability through the suffix. Distinct external ports stay distinct even if both belong to the same gate. Replacing those two peers by leaves therefore commutes with every active rewrite, up to fresh names. In particular ULc--N splices its saved a peer to its result r peer and attaches DONE to c: cutting the r/c continuation peers commutes with this splice. The saved tail and result boundary are distinct by the two disjoint complete-input-chain invariant; there is no illicit same-port splice. No whole-graph forest assumption is used.

For the isolated projection, erase the passive acknowledgment leaf and its incident c edge, and erase the c port/annotation from the unique update controller. The resulting operation is precisely the old AB/AS/AR or UL/U0/U1 operation. Each nonterminal annotated rule is the corresponding old rule plus exactly one c-to-successor-c edge. Each terminal rule is the corresponding old rule plus fresh DONE. Erase that final DONE as well. This gives a step-for-step simulation, allowing renaming because allocating DONE changes the serial high-water mark. It transfers the existing isolated update semantics, termination and step counts.

Insertion has one controller, consumes the unary budget, and never creates cleanup work. Its last ARc step either retains a complete old suffix or installs NIL. Union has one controller, consumes alternating heads, and on either NIL terminal case returns the complete other suffix. No operand producer remains because inputs were complete at release. Therefore their final steps establish the full common postcondition, not merely a head value. Unique c threading establishes one DONE, and nonterminal controllers cannot emit it.

For membership, use the acknowledged single-copy NIL proof and the existing cut-interface simulation: DONE occurs only after the complete retained copy and query cleanup. The active query may have internal concurrency; this does not activate the gate suffix early.

## Gate and program induction

Initially there is one DONE at the first gate (or ACK if P is empty), a complete input word, completed operands, and no active operation. GM consumes DONE and creates exactly COPY/QB; GA creates ABc on its budget/support; GU creates ULc on support/literal. All result/acknowledgment boundaries are threaded to the next gate or final roots. Allocation and replacement preserve the linear interfaces. No release reads the diagnostic gate lists.

By the cut lemma and isolated postcondition, an active instruction terminates without enabling any later instruction before its cleanup is complete. At completion exactly the next gate is enabled, or final ACK is reached. Earlier Boolean components are isolated and never selected by these rules. Induction on the finite instruction list proves the statement, including absence of stranded operands: each dormant operand belongs to an instruction that eventually releases, and its postcondition accounts for every consumed or returned node.

## Exact cost and scheduler scope

For instruction t, let n_t be its input word length; let m_t be the union literal length. Define

* member(i): C_t = 2n_t+i+3;
* add(i): C_t = 2i+2;
* union(v): C_t = 2n_t+1 if n_t<=m_t, otherwise 2m_t+2.

Total rewrites = |P| + sum C_t. Each instruction pays one gate rewrite, including the first. Empty P costs zero. Isolated membership termination bounds all its scheduling choices; update projections have a single controller. Consequently no infinite actual-rewrite sequence exists, and a finite maximal sequence cannot stop with an enabled gate or unfinished instruction. No scheduler fairness premise is needed; a host that simply stops calling step is not a maximal reduction.

## Evidence and next obligation

The 777 mixed-program tests and 4,599 production replacement interface checks support, but do not replace, the argument. The universal cut/erasure bridge above is written rather than mechanically checked. Malformed-state transactional safety and externally restored allocation remain excluded.

This closes straight-line strict sequencing at the current written-proof assurance level. The next genuinely new obligation is a Boolean-triggered conditional: a join must wait for both query completion and its Boolean, release only the chosen branch, and account for the unchosen branch's operands without premature final DONE. Start with two literal insertion alternatives and an explicit unchosen-budget cleanup acknowledgment, not arbitrary nested branches or loops.
