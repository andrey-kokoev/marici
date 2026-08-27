---
id: 20260827-3318
date: 2026-08-27
status: exact-typing-obstruction
---

# 3318 — Matching Primitive Residues Do Not Yet Select the Global e6 Torsor

## Question

Entry 3315 shows that the reconstructed \(e_6\) lift is the canonical
double-pole scale times a primitive logarithmic vector on the base:

\[
\frac{f}{C_2}
=d\log\frac{v}{v-2},
\qquad
\operatorname{Res}_{(v=0,v=2)}\frac{f}{C_2}
=(1,-1).
\]

Entry 304 independently derives the primitive oriented Leray boundary

\[
\partial[p_-,p_+]=[p_+]-[p_-],
\]

with vector \((-1,1)\) in the ordered fiber-endpoint basis
\((p_-,p_+)\).

This entry tests whether the existing comparison calculus identifies these
two vectors.

## Base soft lattice

On the total-energy slice

\[
X_1=1,
\qquad
X_2=\frac{v-2}{2},
\qquad
X_3=-\frac v2.
\]

Hence the two candidate poles are the labelled soft divisors

\[
s_3=\{v=0\}=\{X_3=0\},
\qquad
s_2=\{v=2\}=\{X_2=0\}.
\]

Their primitive divisor difference is source-defined:

\[
\operatorname{div}\frac{X_3}{X_2}
=s_3-s_2,
\]

which gives \((1,-1)\) in the ordered basis \((s_3,s_2)\).

## Fiber endpoint lattice

Entry 304's vector belongs to a different object. Its basis is

\[
p_- = \{r=-1\},
\qquad
p_+ = \{r=1\},
\]

on the exceptional integration-fiber interval. Its orientation is fixed by
the physical Leray chain \(p_-\to p_+\).

Thus the equality of the two primitive vectors after relabelling is not yet
a comparison theorem.

## Existing maps

The current admitted maps do not bridge the two lattices:

1. The conductor/enhanced comparison
   \[
   J:
   \langle g_{101},g_{110},\widetilde g_{111}\rangle
   \longrightarrow
   \langle\delta,\epsilon,\epsilon\delta\rangle
   \]
   maps occurrence characters, not fiber endpoints to base-soft divisors.

2. Infinity Gysin kills \(e_6\), so it cannot normalize this residue.

3. The diagonal Hom connection is zero, which classifies the torsor
   cohomology but does not select a class inside it.

4. Total-energy conductor specialization maps the top graph cycle into its
   finite vanishing object, not into the ordered pair \((s_3,s_2)\).

Therefore no current source-derived arrow has type

\[
\mathbb Z\langle p_-,p_+\rangle
\longrightarrow
\mathbb Z\langle s_3,s_2\rangle.
\]

## Verdict

The candidate passes a strong compatibility test:

- its base residue vector is primitive;
- it has the same difference pattern as the independently derived Leray
  boundary;
- its scale is the canonical \(C_2=-1/8\).

But compatibility is not selection. Identifying the two vectors without a
source-derived specialization map would transport authority across variance.

The candidate \(e_6\) torsor therefore remains globally nontrivial but
physically and source-theoretically unselected.

## Classification

| Datum | Classification |
|---|---|
| \((1,-1)\) on \((s_3,s_2)\) | base-soft divisor class |
| \((-1,1)\) on \((p_-,p_+)\) | fiber Leray boundary |
| equality after relabelling | compatibility evidence |
| typed comparison | absent |
| new carrier datum | none |

## Next falsifier

Construct the weighted specialization of the source Leray interval over the
whole total-energy exceptional divisor. Its boundary must be retained both
vertically in the integration fiber and horizontally at \(X_3=0,X_2=0\).

The candidate is selected only if the resulting boundary-of-boundary
comparison sends

\[
[p_+]-[p_-]
\longmapsto
[s_3]-[s_2]
\]

with coefficient \(C_2\), independently of weighted lift and chart.

## Durable artifacts

- checker: `research/benincasa/checkers/audit_e6_torsor_selection_typing.py`;
- packet: `research/benincasa/results/e6_torsor_selection_typing.json`;
- allocator claim: `seqclaim-c31c11ad949df01c1aba07de`.
