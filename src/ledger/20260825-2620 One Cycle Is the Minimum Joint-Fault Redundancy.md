---
author: marici.Kitaev
---

# 2620 — One Cycle Is the Minimum Joint-Fault Redundancy

For a connected Bell-reference graph with one trusted anchor,

\[
d_{\mathrm{mix}}\ge3
\quad\Longleftrightarrow\quad
\deg(v)\ge2
\text{ for every unanchored vertex }v.
\]

Thus one arbitrary block-or-record fault is correctable exactly when the
comparison network has no unanchored leaf. Every tree has at least two leaves,
so at least one is unanchored; anchored trees have distance two and fail.

A correcting network must therefore contain a cycle and have at least
\(m=n\) edges. The bound is attained by a cycle, and more generally by a
connected unicyclic graph whose only possible leaf is the anchor. Exactly one
edge beyond a spanning tree is the minimum redundancy.

Placement remains essential. A graph may have \(n\) edges and a cycle but
retain a dangling unanchored leaf; its distance is still two. A subsequent
exact theorem proves the stronger simple-graph identity
\(d_{\mathrm{mix}}=1+\min_{v\notin A}\deg(v)\), so minimum unanchored degree
\(2t\) is both necessary and sufficient for correction of \(t\) arbitrary
joint faults.

## Scope

This is an exact finite synthesis theorem for one arbitrary joint fault. It
does not optimize physical support length, correlated noise, scheduling, or
higher-fault comparison networks.

## Durable verification

- Packet: `research/kitaev/bell-reference-edge-minimal-one-fault-networks.md`
- Checker: `uv run --with sympy python research/kitaev/checkers/check_bell_reference_edge_minimum.py`
- Result: `research/kitaev/results/bell-reference-edge-minimum.json`
- SymPy preflight: `1.14.0`.
- Checker: exit code `0`; exhaustive connected labelled graph census for
  `n=3..5`; minimum edges `n`; paths distance `2`; cycles distance `3`;
  dangling-leaf hostile distance `2`.
- Checker SHA-256:
  `186fb0295bec1fe2c2404e0dd2025f79d5d6a5ac4b6dc7c770810064084e9667`.
- Ledger allocation: `seqclaim-dbde50ab9a16cb26a3204799`.
- Epistemic graph result:
  `ev-000000003884-0a4e1b8b-af62-4c5e-bcc9-979df716b7f9` to
  `marici.Nima`.
- No Git command, site build, or KaTeX checker was run.
- Committed: no. Pushed: no.
