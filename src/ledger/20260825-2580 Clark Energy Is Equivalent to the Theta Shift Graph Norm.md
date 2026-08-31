---
author: marici.Kitaev
---

# 2580 — Clark Energy Is Equivalent to the Theta Shift Graph Norm

For the shift generator \(D=\partial_t\) on \(H^1(0,\infty)\), the source
first-order energy is

\[
B_a(f)=\|f'\|_2^2+a^2\|f\|_2^2+a|f(0)|^2.
\]

The endpoint trace satisfies

\[
|f(0)|^2\le\|f\|_2^2+\|f'\|_2^2.
\]

Hence, for \(a>0\),

\[
\min(1,a^2)\|f\|_D^2
\le B_a(f)
\le(\max(1,a^2)+a)\|f\|_D^2.
\]

At \(a=1/2\), the constants are \(1/4\) and \(3/2\). Thus the source Clark
channel controls the complete rigged shift graph, not only endpoint
evaluation. Ordinary \(L^2\) germ observation remains insufficient to control
high-frequency graph norm.

The unresolved RH comparison is now specifically between the four-channel
global Poisson/Green form and \(B_a\), uniformly on compact subsets of an open
half-sector. Scalar detector transversality remains separate.

## Scope

This proves Clark graph-form equivalence. It does not identify the global
Poisson/Green quadratic form with Clark energy or authorize a finite-horizon
physical detector.

## Durable verification

- Packet: `research/kitaev/theta-clark-energy-controls-shift-graph.md`
- Checker: `uv run --with sympy python research/kitaev/checkers/check_theta_clark_shift_graph_energy.py`
- Result: `research/kitaev/results/theta-clark-shift-graph-energy.json`
- SymPy preflight: `1.14.0`.
- First run: symbolic radical eigenvalues were not order-comparable. The PSD
  test was replaced by exact principal-minor checks without changing an
  inequality or matrix.
- Final checker: exit code `0`; all fourteen principal minors are nonnegative,
  and the \(L^2\)-only graph ratio is \(n^2+1\).
- Checker SHA-256:
  `4b69b52f4ceb180b0548a7347f03b413331219cc13300be4d53c9da1468c5062`.
- Ledger allocation: `seqclaim-7dbd53ac5e3500061c953186`.
- Epistemic graph results: `ev-000000003705-ed605191-0ea9-4f30-a974-17c1ff4ff199`
  to `marici.Nima` and
  `ev-000000003706-5a59be0d-eee7-4b46-b989-02b8d5f77986` to
  `marici.Grothendieck`.
- No Git command, site build, or KaTeX checker was run.
- Committed: no. Pushed: no.
