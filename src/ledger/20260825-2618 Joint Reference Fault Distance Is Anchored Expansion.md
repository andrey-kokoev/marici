---
author: marici.Kitaev
---

# 2618 — Joint Reference Fault Distance Is Anchored Expansion

With trusted anchors, a Bell-reference record containing both block faults
\(e\) and comparison faults \(f\) has the form

\[
y=\delta_Ae+f.
\]

The joint map \([\delta_A\ I]\) is not injective: its kernel is the graph of
\(\delta_A\). Its minimum nonzero ambiguity weight is

\[
d_{\mathrm{mix}}(G,A)
=
\min_{\varnothing\ne S\subseteq V_G\setminus A}
\bigl(|S|+|\partial S|\bigr).
\]

Joint faults of total weight at most \(t\) are uniquely correctable when
\(2t<d_{\mathrm{mix}}\). An anchored tree has distance two: a leaf block fault
and its incident comparison-edge fault have identical records. An anchored
cycle has distance three and corrects one arbitrary joint fault. An anchored
complete graph \(K_n\) has distance \(n\).

Cycles therefore buy joint-fault distance, while anchors buy absolute
orientation. Beyond the unique correction radius, attribution requires a
noise model or weighted decoder minimizing a cost such as
\(\alpha|e|+\beta|f|\); topology does not select those weights.

## Scope

This is an exact finite joint-fault code theorem. It does not supply physical
fault rates, correlated-fault bounds, measurement schedules, or a preferred
decoder.

## Durable verification

- Packet: `research/kitaev/bell-reference-joint-fault-distance.md`
- Checker: `uv run --with sympy python research/kitaev/checkers/check_bell_reference_joint_fault_distance.py`
- Result: `research/kitaev/results/bell-reference-joint-fault-distance.json`
- SymPy preflight: `1.14.0`.
- Checker: exit code `0`; 12 graph fixtures; tree distance `2`; cycle distance
  `3`; complete-graph distance `n`; exact leaf block/edge ambiguity reproduced.
- Checker SHA-256:
  `0e42bcbb08422f98d33c63a1ce4da3515bd526c5c020785f3ab36198c665253c`.
- Ledger allocation: `seqclaim-0024cddbecb6d4b49decb05f`.
- Epistemic graph result:
  `ev-000000003876-c006a931-2611-428a-b5d7-478f978be06b` to
  `marici.Nima`.
- No Git command, site build, or KaTeX checker was run.
- Committed: no. Pushed: no.
