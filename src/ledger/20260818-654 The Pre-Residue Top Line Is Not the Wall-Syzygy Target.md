---
authors:
  - marici.Nima
date: 2026-08-18
---
# 654 — The Pre-Residue Top Line Is Not the Wall-Syzygy Target

## Typing correction

Entries 652 and 653 produce adjacent but different objects. They cannot be
joined by a direct \(3\to1\) matrix without first constructing the
Poincare-residue chain map.

## Entry 653 object

The occupied proper top line belongs to the three-variable pre-residue
complex

\[
(c,a,b);
\qquad
(q_{g_1},q_{g_2},q_{G_{12}}).
\]

Its deletion ranks are

\[
21-20=1.
\]

Thus \([\Omega_{111}]\) spans a one-dimensional quotient before taking the
\(q_{G_{12}}\) residue.

## Entry 652 object

The three minimal logarithmic derivations live after imposing

\[
q_{G_{12}}=0
\]

on the two-variable residue surface. Their frozen divisor contains five
walls

\[
(q_{g_1},q_{g_2},q_{g_3},q_{g_{23}},q_{g_{31}}).
\]

The shared-three-wall localization target is not rank one. Its exact ranks
are

\[
0\longrightarrow\mathbb Q^9
\longrightarrow\mathbb Q^{15}
\longrightarrow\mathbb Q^6
\longrightarrow0.
\]

Hence the first typed residue map is

\[
\operatorname{Der}^{(7)}(-\log D)
\longrightarrow H^1(W_{123})(-1),
\]

with a rank-six ambient target.

## Missing comparison

To ask whether the three syzygies reach the physical source line, one must
construct the chain

\[
M_{111}^{\rm pre}
\xrightarrow{\operatorname{Res}_{G_{12}}}
H^2(S_E\setminus W)
\xrightarrow{\partial_W}
H^1(W_{123})(-1)
\]

on retained presentations. Only then does Entry 648's source cocycle define
a distinguished line inside the rank-six wall quotient.

Therefore the proposed shortcut

\[
\mathbb Q^3_{\rm syz}
\longrightarrow
\mathbb Q^1_{\rm top}
\]

is untyped. The legal matrix initially has shape

\[
\boxed{\mathbb Q^3_{\rm syz}\longrightarrow\mathbb Q^6_{\rm wall}.}
\]

Its comparison with the physical line requires the separately derived
residue-localization vector.

## Consequence

Entry 653 remains a valid physical-occupancy theorem. Entry 652 remains a
valid primitive-choice census. The correction only prohibits identifying
their codomains before constructing the residue functor.

## Updated frontier

Retain pivot certificates for both complexes and implement the
\(q_{G_{12}}\) Poincare residue column map. Then:

1. map \([\Omega_{111}]\) to the rank-six wall quotient and verify that it
   reproduces Entry 648's cocycle;
2. compute the three degree-seven syzygy images in that same quotient;
3. compare their span with the source-cocycle line;
4. quotient relative-exact primitive differences.

## Evidence

- `research/benincasa/pre_residue_to_wall_syzygy_type_gate.py`;
- Entries 648 and 650--653.

## Outcome contract

~~~json
{
  "claim": "The three minimal residue-surface syzygies map directly to Entry 653's one-dimensional pre-residue proper top quotient.",
  "status": "mistyped",
  "pre_residue_top_rank": 1,
  "residue_surface_wall_quotient_rank": 6,
  "minimal_syzygy_rank": 3,
  "legal_first_matrix_shape": [6, 3],
  "missing_operation": "retained-presentation Poincare residue followed by wall localization",
  "next_experiment": "Construct that residue-localization column map and compare both source and syzygy images in the common rank-six target."
}
~~~
