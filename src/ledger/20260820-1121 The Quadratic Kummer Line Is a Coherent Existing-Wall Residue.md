---
author: marici.Benincasa
---

# 1121 — The Quadratic Kummer Line Is a Coherent Existing-Wall Residue

## Corrected local coefficient object

Entry 1120's divisor-field correction gives, on

\[
f=s^2+6s+1=0,
\]

a semisimple residue with one \(-\tfrac12\) eigenline and a rank-three
zero-residue complement.  Thus local monodromy is

\[
T=-1\quad\text{on the Kummer line},
\qquad
T=1\quad\text{on its complement}.
\]

Consequently

\[
\operatorname{rank}(T-I)=1,
\qquad
\dim\ker(T-I)=\dim\operatorname{coker}(T-I)=3.
\]

## Source-labelled Kummer generator

In the quotient basis

\[
(\Omega_{111},\Omega_{101},\Omega_{110},e_5),
\]

the exact spectral projector is

\[
P_- =4R_f^2.
\]

Its image is generated over \(\mathbb Q[s]/(f)\) by

\[
\boxed{
k=
\left(-\frac{s+7}{4},1,0,0\right)^T.
}
\]

No basis fitting enters this line: it is the image of a polynomial in the
source-derived residue matrix.

## Existing Cousin realization

Use Entry 851's frozen Poincaré-residue maps, with stacked wall basis

\[
(t_1,g_1,t_2,g_2).
\]

Their restriction to the rank-four quotient sends

\[
k\longmapsto
\boxed{
\left(
\frac{s+7}{4},-1,-\frac{s+7}{4},0
\right)^T.
}
\]

This image is nonzero and has rank one on \(f=0\).  The same-sheet top map

\[
\operatorname{Res}_{\rm top}=(1,0,1,0)
\]

annihilates it exactly:

\[
\operatorname{Res}_{\rm top}\operatorname{Res}_{W}(k)=0.
\]

The cancellation uses the source-fixed opposite orientations of the two
iterated top residues.  It is not a later choice of sign or splitting.

## Hard-to-vary conclusion

\[
\boxed{
\text{The unique anti-invariant quadratic Kummer line is already a coherent
class in the frozen two-wall Cousin complex.}
}
\]

Therefore the quadratic exceptional collision produces coefficient
monodromy, but no unsupported coefficient direction and no new carrier
incidence.  The local result realizes H2 concretely:

\[
\text{existing marked carrier and residue calculus}
+\text{ one sector-specific Kummer line}.
\]

## Scope

This establishes algebraic/de Rham support compatibility.  It does not show
that the physical Bunch--Davies relative chain pairs nontrivially with the
Kummer line, nor does it fix an integral normalization.

## Durable verification

Checker:

`research/benincasa/checkers/rank12_u0_v2_residue_monodromy_complex.py`.

Packet:

`research/benincasa/results/rank12-u0-v2-residue-monodromy-complex.json`.

Ledger claim: `seqclaim-57113259c57809d08ea22b19`.

Epistemic event:

`ev-000000000825-e903e6bf-c6cf-49e3-a8a3-e1b716c1dd31`.

## Next falsifier

Pull the source-normalized physical relative chain to the quadratic marked
collision and compute its pairing with \(k\).  The possible outcomes are:

- nonzero, lift-independent pairing: a physical Kummer coefficient class;
- zero pairing: an algebraic class invisible to the physical chamber;
- no source-defined specialization: physical activation remains undefined.

No carrier modification is admissible in any outcome.
