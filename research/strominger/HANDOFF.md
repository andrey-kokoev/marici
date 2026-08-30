# Strominger continuation handoff (2026-08-24)

You are marici.Strominger working in C:/Users/andrey/src/marici (Windows, Git Bash).
This file re-establishes you after a session abandonment. Do NOT resume the old
session (session_26ef830c): its context is poisoned by a tool-call repetition
loop (mcp_loader_attach_surface emitted regardless of intent). Harness and MCP
are healthy - Caroline's diagnosis: model-side repetition from a saturated
transcript, confirmed by fingerprint probe strominger-probe-9f3a1.

## Read first (in this order)
1. src/ledger/20260824-1982 Activation Certified Exactly One Invariant Observable and It Is Real.md
2. research/strominger/activation.md (the closed arc's packet)
3. src/ledger/20260824-1981 The Datum Side Is Classified...md (the classification this builds on)
4. AGENTS.md at ~/src/marici/AGENTS.md (sector protocol)

## Protocol essentials
- Checkers: uv run --with sympy python -u research/strominger/checkers/<file>.py from site root;
  long runs as background tasks with | tee <log>.
- Graph: mcp_loader_call_binding_tool, site_root C:/Users/andrey/src/marici,
  binding_id marici-epistemic-graph (stateless per call; connection ids expire).
- Inbox: epistemic_graph_query {"template":"epistemic:inbox","match":{recipient:
  "marici.Strominger",read_state:"unread",limit":20},"since_event":<INT>}; last
  checked empty through ev-2664. Re-check with since_event:2664.
- Ledger numbers: epistemic_graph_sequence_claim_next, sequence_name
  "marici-ledger-entry", actor "marici.Strominger", authority_basis OBJECT
  {kind:"operator_direct_instruction",summary:...}, unique idempotency_key.
  Last claimed: 1982.
- Comms: epistemic_graph_submit_review_admit with top-level actor +
  authority_basis; operations: entity.declare (kind narada.epistemic:communication;
  op-level fields local_ref, kind, title, sender, recipient, intent (one of
  request/handoff/result/notice/objection/reply/acknowledgment), status, sent_at,
  body - NOT inside "additional"), then relation.declare sent_by/addressed_to
  (source_ref + target_id). Strominger team_member:4561aedd7f948b5ddee5, Nima
  team_member:aa2834674c8559a5dee0, Figueiredo team_member:7f11641564913e4417ff.
  Last comm sent: ev-2668 (rank answer to Nima).
- Rules: ASCII-only in checkers/ledger/graph payloads; no commit/push without
  explicit operator instruction; touch only own files; no site build/KaTeX checks.

## Programme state (all verified, exit 0)
Five arcs closed. Variation audit (ledger 1971), deformation theory (1974),
gauge mechanism (1976, comm ev-2649), WP36 comparison (1977, comm ev-2651 to
Figueiredo - unanswered), datum classification (1981, comm ev-2662 to Nima -
unanswered, checker 101/101: exactly four grade-stable monomial-character
classes), activation (1982, comm ev-2668, checker activation_checks.py 27/27):
E_g(D=1) = ((g+3)!/6)(z^g+zb^g)/(1+u)^g, P-invariant at even g on the nose,
actualized at witness W2; rank theorem: invariant E readouts = span{1} at even
grades, {0} odd, no invariant M at any grade.

## Next arc: the magnetic kernel
Question: the sporadic grade-local accidents (zb^-2 class dies at g=3 with
M=0; magnetic-zero data) - shadows of what?
Hypothesis: M=0 iff the fold output pair (f, fb) is a gradient (M = d_zb f -
d_z fb = 0 is exactly the closedness condition), i.e. magnetic-zero data are
pure-gauge/exact data.
Plan (~a dozen moves):
1. Record operator stimulus (kind marici:operator_stimulus, title + flat
   additional object with pre-ratings excitement/confidence/info-gain) - NOT
   yet recorded for this arc.
2. Scratch: E,M for zb^-2 at g=1..4 (where does M vanish; E characters there).
3. Scratch: kernel of M on monomial grid z^-a zb^m, a in {0,2,4}, m in -4..4,
   g=2,3 - exact rational linear algebra (evaluate at rational points, null
   space over QQ, verify symbolically).
4. Scratch: gradient witnesses Phi for kernel elements (integrate f w.r.t. z,
   check d_zb Phi = fb).
5. Checker + packet + ledger entry + report. Consider comm to Figueiredo if
   the kernel characterization bears on his M-constancy question (ev-2651).
6. Check inbox since ev-2664 before sending any comm.

## Housekeeping
- ~23 orphaned epistemic-graph loader children were spawned by the poisoned
  session; operator was advised to enumerate via mcp_loader_process_ownership
  and restart the mcp-loader process. Confirm with operator whether done.
