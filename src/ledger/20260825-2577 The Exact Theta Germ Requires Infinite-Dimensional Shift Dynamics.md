---
author: marici.Kitaev
---

# 2577 — The Exact Theta Germ Requires Infinite-Dimensional Shift Dynamics

An exact finite-dimensional coefficient realization of the seam germ would
force the finite translate span of \(\Phi\) to be invariant under
differentiation. Cayley--Hamilton would then give a finite constant-coefficient
ODE for \(\Phi\), making it an exponential polynomial. This contradicts the
source-derived super-exponential theta tail. Therefore no finite constant
matrix generates the exact seam germ.

The correct source dynamics is the right-shift semigroup

\[
(S_tf)(u)=f(u+t),
\]

with endpoint observation. For \(g_q(u)=\Phi(u+q)\),

\[
\operatorname{ev}_0S_tg_q=\Phi(t+q).
\]

Point evaluation is unbounded on bare \(L^2\), but the integrated observation
map is the identity:

\[
\int_0^\infty|\operatorname{ev}_0S_tf|^2dt=\|f\|_2^2.
\]

Thus infinite-horizon observability is exact, while any finite horizon has an
ambient tail-hidden subspace. A finite discrete shift model has full-horizon
Gramian \(I_N\) and rank equal to the horizon under truncation.

## Scope

This is a source-typed finite-realization obstruction and exact
infinite-dimensional replacement. It does not authorize an infinite-horizon
physical detector or identify its identity norm with RH-bearing energy.

## Durable verification

- Packet: `research/kitaev/theta-seam-germ-requires-infinite-shift-dynamics.md`
- Checker: `uv run --with sympy python research/kitaev/checkers/check_theta_shift_realization.py`
- Result: `research/kitaev/results/theta-shift-realization.json`
- SymPy preflight: `1.14.0`.
- Exact checker: exit code `0`; Gaussian derivative-factor rank `6`,
  full-horizon shift Gramian identity, short-horizon rank `3`, hidden state
  `(0,0,0,1,0)`.
- Checker SHA-256:
  `2bd6c0845f296fb27c9d988e5f720430bb296b6ad3748ba1189bd6883e5784c3`.
- Ledger allocation: `seqclaim-808e90de0bebe69aef90d709`.
- Epistemic graph results: `ev-000000003697-3bd6b9e0-8f14-44e5-b2c8-08be13c8ecad`
  to `marici.Nima` and
  `ev-000000003698-c58690c5-9732-4cae-a070-ab2d8c98d369` to
  `marici.Grothendieck`.
- No Git command, site build, or KaTeX checker was run.
- Committed: no. Pushed: no.
