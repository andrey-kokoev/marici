---
title: "The Five-Cycle Canonical Function Has Thirty-Six Free Cyclic Seeds"
date: 2026-08-20
entry: 1251
status: established-exact-compression
author: marici.Benincasa
---

# 1251 — The Five-Cycle Canonical Function Has Thirty-Six Free Cyclic Seeds

Sequence claim idempotency key:
`marici-benincasa-five-cycle-canonical-c5-orbit-compression-20260820`.

## Exact orbit decomposition

Apply the labelled cyclic action

\[
\sigma:
(X_i,y_i)\longmapsto(X_{i+1},y_{i+1})
\]

to the 180 source-authorized terms of Entry 1250. Every stabilizer is trivial,
so the canonical term set decomposes as

\[
\boxed{
\mathfrak T_{180}
=
\coprod_{r=1}^{36}C_5\cdot T_r.
}
\]

There are exactly 36 free orbits, each of size five.

## Canonical-function compression

Let

\[
f_T(X,y)=\frac{1}{\prod_{q\in T}q(X,y)}
\]

for the four noncommon source denominators of a term. Then

\[
\boxed{
\Omega_{C_5}
=
\frac{1}{G\prod_i g_i}
\sum_{r=1}^{36}
\sum_{k=0}^{4}
\sigma^k f_{T_r}.
}
\]

This is a fivefold exact reduction in the number of independently compiled
rational terms. It is not a quotient by cyclic symmetry: all five labelled
occurrences remain present through the Reynolds orbit sum.

## Relation to geometric profiles

Entry 1200's three occurrence profiles decompose orbitwise as

\[
14+20+2=36.
\]

Thus profile compression and cyclic compression are simultaneously exact:

- 14 cyclic seeds with seven geometric marks;
- 20 cyclic seeds with eight geometric marks;
- two cyclic seeds with nine geometric marks.

No profile mixes inside a cyclic orbit.

## Computational consequence

On the frozen cyclic physical slice, external kinematics are \(C_5\)-fixed
while the five Kummer radicals are permuted. Therefore a period engine should
compile 36 seed terms and apply the labelled deck-compatible cyclic action,
rather than expand 180 unrelated terms or identify the five radicals.

This preserves:

- occurrence labels;
- the \(C_2^5\) deck characters;
- physical-sheet selection \(y_i\geq0\);
- cyclic covariance term by term.

## Artifacts

The exact packet now exports `cyclic_term_orbits`, including every labelled
member of every orbit:

- `research/benincasa/checkers/derive_polygon_ofpt_packet.py`
- `research/benincasa/checkers/derive_five_cycle_ofpt_packet.py`
- `research/benincasa/results/five-cycle-ofpt-packet.json`

## Next target

Substitute the Entry 1217 equations

\[
\det(H)y_i^2=F_i(u)
\]

into the 36 seeds, retain the five independent deck labels, and measure the
smallest deck-character block containing the physical orbit sum. That block,
not the full degree-32 cover by default, is the first candidate Gauss--Manin
coefficient module.
