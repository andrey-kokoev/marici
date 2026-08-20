---
author: marici.Strominger
---
# 1096 — The Sub-Subleading Soft Factor Needs No Conservation Law: the P→J Escalation Terminates, the Ward Bridge Verifies at the D_z⁴ Grade, and the Memory Corner Is Open

## Question

Entries 1056 and 1079 established a pattern: the soft–Ward–memory
bridge closes leg-summed under four-momentum conservation
\(\mathcal P\) at the leading rung and under total angular momentum
conservation \(\mathcal J\) at the subleading rung. This entry opens
rung three: the sub-subleading soft graviton factor \(S^{(2)}\) of
Cachazo–Strominger [CS (9), (20)], universal at tree level with no
known symmetry input, and asks whether the pattern escalates again
(boosts? an extended-BMS charge?) or terminates.

## The verdict

The escalation **terminates**. \(S^{(2)}\) is gauge invariant
**per leg** from the antisymmetry of \(J_a^{\mu\nu}\) alone — the
grounded CS text says so verbatim — and the checker proves the
mechanism: each per-leg gauge variation vanishes identically with all
\(\Sigma\)-constraints removed (anti-test T5.1: nothing changes), while
the rung-2-grade contraction \(\Lambda_\mu q_\nu J^{\mu\nu}\) is
nonzero without \(\Sigma J=0\) (T1.5). No conservation law is the
closure input at rung three.

The Ward corner is grounded and verifies: Campiglia–Laddha
(arXiv:1605.09094) pair \(S^{(2)}\) with charges \(Q_{rX},\tilde
Q_{rX}\) of \(O(r)\) large diffeomorphisms \(\xi\sim rX^A\partial_A\)
(divergence-free \(X^A\), beyond generalized BMS). Under the declared
fold prescription (weight sequence \((-1,0,1,2)\), uniqueness
witnessed), the regular part of \(D_z^4 S^{(2)-}\) vanishes in all
four operator channels and the \(\delta^2\) channel is pinned; the
electric/magnetic doubling is exact at operator level. The cross-rung
ladder is exact: one fold recursion reproduces rung 2's declared fold,
and the derivative/time-integral grades run
\(D_z^2,\int^0\) (rung 1) \(\to D_z^3,\int^1\) (rung 2)
\(\to D_z^4,\int^2\) (rung 3).

The memory corner is **open by grounding, not by a failed check**:
Nichols' center-of-mass memory lives at the rung-2 grade (the
electric-parity partner of spin memory), and no rung-3 observable is
named in the grounded literature. The structural core of a candidate
is verified — a rung-3 memory would be a **double retarded-time
integral, first-moment, \(D_z^4\)-grade** observable (CL16 (17)
structure) — but naming it is left as a typed open item.

## Named residuals (typed, none absorbed)

- **Half-strength \(\delta\) drift (T3.5c).** The computed
  \(\delta^2\) coefficient in the CL16 smearing identity is uniformly
  HALF the printed one (\(-3\pi/E_k\) computed vs \(-6\pi/E_k\)
  printed) — the same \(\delta^2\)-normalization drift family as the
  rung-2 KLPS scaffold residual. Regular parts vanish identically.
- CS (9) vs CL16 (14) normalizations differ by a ratio \(-\omega\)
  (T2.3c), typed as convention drift.
- The magnetic half \(\tilde Q_{rX}\) lacks a first-principles
  derivation in CL16 (their own caveat); FPR (arXiv:2111.15607)
  collinear corrections are a beyond-tree residual; loop
  non-universality of tree-level \(S^{(2)}\)
  (Bern–Davies–Di Vecchia–Nohle) is citation-level only.
- The fold weight sequence is a declared prescription, selected by the
  vanishing-regular-part requirement; it relies on the inherited
  rung-1 distributional prescription
  \(\partial_{\bar z}(z-w)^{-1}=\pi\delta^2\).

## Scope

The verdict covers the exactly checkable core: soft-corner gauge
mechanism, Ward-corner smearing, and the cross-rung operator ladders.
It does not assert a rung-3 memory observable, and the leg-summed
question at rung 3 is answered at the operator level (kinematic
closure), not by a fully summed symbolic amplitude run.

## Verification artifacts

- exact checker (sympy):
  `research/strominger/checkers/subsubleading_triangle_exact_checks.py`
  (run: `uv run --with sympy python research/strominger/checkers/subsubleading_triangle_exact_checks.py`;
  31/31 pass, exit 0);
- independent cross-validation (Rust + Symbolica 2.2.0, new bin):
  `research/strominger/marici-triangle/src/bin/subsubleading.rs`
  (31/31 pass, programmatic diff against sympy: zero mismatches,
  `research/strominger/checkers/diff_subsubleading_results.py`);
- results JSONs:
  `research/strominger/results/subsubleading_triangle_exact_checks.json`,
  `research/strominger/results/subsubleading_triangle_symbolica_checks.json`;
- packets:
  `research/strominger/subsubleading-triangle-conventions.md`,
  `research/strominger/subsubleading-triangle-source-boundary.md`;
- grounded source texts (new this entry):
  `research/strominger/sources/{cl1605.09094,cl1502.02318,nichols1807.08767,fpr2111.15607}.txt`;
- rung-2 suites re-run after all rung-3 work: no regression (53/53
  both engines);
- ledger-number allocator claim: `seqclaim-68fffb4df7f91a874900663e`
  (sequence `marici-ledger-entry`, value 1096).

Epistemic graph event: see the rung-3 admission event (test + claim +
report communication to marici.Nima, admitted 2026-08-20); the claim
`marici:refines` the 1079 subleading claim.
