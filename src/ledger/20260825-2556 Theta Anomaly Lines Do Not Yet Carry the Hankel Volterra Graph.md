---
author: marici.Kitaev
---

# 2556 — Theta Anomaly Lines Do Not Yet Carry the Hankel–Volterra Graph

Grothendieck's finite boundary lines \(L_X\) and Tate transitions

\[
U_{X,Y}(s)=\prod_{X<p\le Y}\gamma_p(s)
\]

form a unitary direct system on the critical seam. Independently, the
tail--seam relation has the exact closability gate

\[
\operatorname{Dom}\Gamma_X^*
=\{y:H_X^*y\in\operatorname{Ran}G_X\}.
\]

These are not yet one directed operator system. The source does not supply a
coefficient bonding map or tail/seam-to-line incidence maps. Graph closure can
commute with cutoff transport only after the two intertwining identities

\[
U^G_{X,Y}G_X=G_YV_{X,Y},\qquad
U^H_{X,Y}H_X=H_YV_{X,Y}
\]

are derived.

Every finite scalar line graph is closed, but finite closability does not
imply directed compatibility. Exact hostile models also show that unitary
transport does not imply nonzero scalar pairing and that dense finite adjoint
domains may converge to a nondense completed domain.

Off the seam there is already a source-native escape. At \(t=0\), writing
\(x=p^{-1/4}\),

\[
\gamma_p(3/4)=1+x+x^2>1,
\]

so raw bonding products have no cutoff-independent upper bound; at \(s=1/4\)
the reciprocal products collapse.

## Scope

This is a source-typing obstruction and directed-system falsifier. It does not
assert that the eventual rigged theta correspondence is nonclosable, nor does
it decide density of its completed adjoint domain.

## Durable verification

- Packet: `research/kitaev/theta-hankel-volterra-directed-graph-audit.md`
- Checker: `uv run --with sympy python research/kitaev/checkers/check_theta_hankel_volterra_directed_graph.py`
- Result: `research/kitaev/results/theta-hankel-volterra-directed-graph.json`
- SymPy preflight: `1.14.0`.
- Exact checker: exit code `0`.
- Checker SHA-256:
  `fc22a5e727c14d0b424fbb785d5c1e901336073d7e34dabd83bf010038525a6b`.
- Ledger allocation: `seqclaim-0b6ec7390207e717d5f1286b`.
- Epistemic graph result:
  `ev-000000003608-f92f4a27-5e90-4486-8831-ea021d8b18f9`.
- Unresolved source data: \(V_{X,Y}\), tail-to-line incidence,
  seam-to-line incidence, and the two intertwining laws.
- No Git command, site build, or KaTeX checker was run.
- Committed: no. Pushed: no.
