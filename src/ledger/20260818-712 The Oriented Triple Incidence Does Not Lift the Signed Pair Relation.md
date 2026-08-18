---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 712 — The Oriented Triple Incidence Does Not Lift the Signed Pair Relation

## Frozen incidence calculation

Use the disappearing triple

\[
(q_{\mathfrak g_2},q_{\mathfrak g_3},q_{\mathfrak g_{23}})
\]

and pair order

\[
([23],[2,23],[3,23]).
\]

Taking each ordered double residue and then the remaining residue gives

\[
\boxed{
(r_{23},r_{2,23},r_{3,23})
=\left(\frac12,-\frac12,\frac12\right).}
\]

All three remaining linear forms vanish at the same triple point
\(c=-X_2\). Hence the primitive oriented incidence vector is

\[
\boxed{(1,-1,1).}
\]

## Failure of the proposed lift

Entry 709 proves the strict residue identity

\[
[2,23]=[3,23].
\]

Their two contributions to the triple incidence therefore cancel, leaving
the minus pair \([23]\). Applying Entry 707's branch-discriminant symbol gives

\[
\sigma_2(\operatorname{Disc})(1,-1,1)
=C_{23}^-\nu_2\nu_3,
\]

which is generically nonzero. Consequently

\[
\boxed{
\text{the disappearing triple incidence is not a lift of the weighted
signed-pair kernel relation}.}
\]

This is a source-derived orientation test, not a rank argument.

## What survives

Entry 711 gives the triple's first nonzero normal coefficient

\[
T_2=X_3^2\nu_2^2
+(X_1^2-X_2^2-X_3^2)\nu_2\nu_3
+X_2^2\nu_3^2.
\]

Thus the second-Rees triple costalk naturally lives on

\[
\boxed{\eta^2=T_2.}
\]

The mixed triple remains a valid Kummer coefficient object over the existing
normal carrier, but it does not provide the sought polynomial chain homotopy
between the signed pair residues.

## Classification

- five pair occurrences: existing marked-incidence carrier;
- strict repeated-plus relation: incidence identity;
- mixed triple cover \(\eta^2=T_2\): sector-specific Kummer coefficient data;
- weighted signed-pair relation: symbol-level only, with no lift from the
  adjacent triple cell.

No new carrier stratum is indicated.

## Evidence

- `research/benincasa/check_triple_to_pair_second_rees_boundary.py`;
- Entries 707, 709, and 711;
- allocator claim `seqclaim-11647084d139a42910b81661`.

## Next falsifier

Retire the direct triple-homotopy route. The remaining typed possibility is a
nontrivial extension between the pair Kummer systems and the mixed triple
costalk. Construct its Gauss--Manin connecting morphism on the quadratic
normal cover and test whether its extension coefficient has \(\mathcal Q\)
support. If no source-derived connecting morphism exists, this entire lower
normal branch remains disconnected from the homogeneous \(\mathcal Q\)
sector.
