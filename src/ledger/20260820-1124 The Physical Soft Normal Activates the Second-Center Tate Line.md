---
author: marici.Benincasa
---

# 1124 — The Physical Soft Normal Activates the Second-Center Tate Line

## Source-defined physical limit

Entries 1099--1104 constructed the second exceptional center

\[
(u,v)=(2,0)
\]

and its unique anti-invariant nodal Tate line, but did not pair that line with
a physical specialization.

In source energies the center is

\[
(X_1,X_2,X_3)=(1,0,1).
\]

The canonical \(X_2\)-soft operation holds the other external energies fixed:

\[
X_1=X_3=1,
\qquad
X_2=\eta\longrightarrow0^+.
\]

This is an ordinary physical normal specialization, not a chosen regulator
hierarchy.

## Pullback to the joint Rees chart

Using

\[
u=\frac{X_1+X_2+X_3}{X_1},
\qquad
v=\frac{X_1+X_2-X_3}{X_1},
\]

and the local coordinates

\[
p=u-2,
\qquad
q=v,
\qquad
s=\frac qp,
\]

the physical soft normal gives exactly

\[
\boxed{p=\eta,\qquad q=\eta,\qquad s=1.}
\]

Entry 1100's normalized node has smoothing parameter, up to its fixed
nonzero scalar unit,

\[
t=p\,s\,(B-1).
\]

Therefore

\[
\boxed{t=\eta(B-1).}
\]

On the generic conductor locus \(B-1\ne0\), the physical normal valuation is
one.  Its Gysin coefficient into Entry 1103's Tate line is consequently

\[
\boxed{1.}
\]

The resulting pairing is nonzero up to the already frozen global orientation
sign, and it carries the source square-root deck character \(-1\).

## Tangential-lift typing

For completeness, allow a first-order moving-base lift

\[
X_1=1+\alpha\eta,
\qquad
X_2=\eta,
\qquad
X_3=1+\gamma\eta.
\]

Then

\[
p=(1-\alpha+\gamma)\eta+O(\eta^2),
\qquad
q=(1+\alpha-\gamma)\eta+O(\eta^2).
\]

The locus

\[
1+\alpha-\gamma=0
\]

enters the separately labelled \(q=0\) corner.  It is not an ambiguity of the
fixed-base soft specialization.  This distinction prevents promoting the
result to an unjustified all-path statement.

## Hard-to-vary conclusion

\[
\boxed{
\text{The source-normalized physical }X_2\text{-soft nearby cycle activates
the second-center anti-invariant Tate line with multiplicity one.}
}
\]

This supplies the physical comparison absent from Entry 1104.  The complete
local architecture is now

\[
\text{existing soft/marked carrier}
+\text{ exact three-face Gysin simplex}
+\text{ physically selected Tate coefficient line}.
\]

No new carrier datum appears.

## Scope

The theorem holds on the generic conductor locus \(B-1\ne0\).  The deeper
soft--\(q\)--marked corner remains governed by Entry 1104's full three-face
simplex and should not be collapsed into this one-normal statement.

## Durable verification

Checker:

`research/benincasa/checkers/rank12_u2_v0_physical_soft_tate_pairing.py`.

Packet:

`research/benincasa/results/rank12-u2-v0-physical-soft-tate-pairing.json`.

Ledger claim: `seqclaim-f45493647dfbc69fd80bad30`.

Epistemic event:

`ev-000000000831-3c00bcdc-b407-416f-8111-e797336bc870`.

## Next falsifier

Transport the physical soft Tate generator through the cyclic occurrence
atlas and test whether the three site-soft activations form the regular
\(C_3\) occurrence module with the source residue orientations.  A cyclic
transition defect would be coefficient descent failure on the existing
carrier; it would not by itself authorize a new incidence divisor.
