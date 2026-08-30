---
author: marici.Benincasa
---

# 1910 — The Literal Eight-Site Chamber Has Zero Ordinary Supported Pullback

## Correction

The original draft incorrectly promoted empty ordinary support to vanishing
of Leray/nearby activation. Entry 1083 is a counterexample to that inference:
an empty literal intersection can acquire a nonzero source-defined
double-Leray specialization. This entry is therefore restricted to ordinary
supported pullback. Leray/nearby activation remains open.

Correction admission: `ev-000000002296-f649303c-d25d-4aa6-904c-373638c82e64`.

## Question

Entry 1909 found 36 source-admitted rank-four C8 strata with genuine
horizontal coefficient discriminants, including

\[
2k-3=0
\qquad\text{and}\qquad
7+6k-8l=0,
\]

but no strictly positive-\(X_i\) critical sheet. Does the literal
Bunch--Davies chamber have a nonzero ordinary supported pullback to one of
those coefficient divisors?

## Frozen comparison

For a labelled orbit \(O\), let \(S_O\) denote its rank-four source wall and
\(D_O\) any irreducible component of its coefficient discriminant.  The
minimal ordinary typed comparison is

\[
\Phi_O^{\rm ord}:\mathcal C_{\Gamma_{\rm BD}}
\longrightarrow
R\Gamma_{S_O\cap D_O}(\operatorname{gr}_{D_O}\mathcal V_O).
\]

The source is the literal Bunch--Davies chain
\(\Gamma_{\rm BD}=\{X_i>0\}\), with its source boundary value.  The target is
supported on the source wall. No continuation class, support summand, or
carrier facet is added after seeing \(D_O\).

Ordinary restriction, ordinary boundary Gysin/residue, and ordinary
localization/Cut support pullback are support-local. Consequently they cannot
create a physical section after the support has empty pullback to
\(\Gamma_{\rm BD}\).

## Exact support audit

The checker independently reconstructs every serialized Gordan witness.  For
all 36 orbits it obtains

\[
g_O\in
\operatorname{rowspan}(R_{X,O})\cap\mathbb Q_{\ge0}^{8},
\qquad g_O\ne0.
\]

If \(R_{X,O}X=0\) and \(X_i>0\), then

\[
0=g_O\cdot X>0,
\]

which is impossible.  Therefore

\[
\boxed{\Gamma_{\rm BD}\cap S_O=\varnothing}
\]

for every candidate before either the linear factor or its companion
coefficient discriminant is imposed.

The complete family count is

\[
21:\ 2k-3,
\qquad
15:\ 7+6k-8l.
\]

Each linear factor occurs with determinant valuation one.  Its generic
coefficient grade is therefore rank one and Cartier length one, with labelled
conormal line fixed by the source-normalized adjugate identity

\[
\lambda J=\det(J)e_1.
\]

The 36 nonconstant companion discriminants are retained without assuming
irreducibility or assigning an unsupported total nearby-cycle rank.  Every
component lies over the same physically empty \(S_O\).

## Typed map and cone

For every orbit,

\[
\boxed{\Phi_O^{\rm ord}=0}
\]

because its supported source object is zero.  This happens before any
weighted, normal, or analytic lift, so the result is strictly
lift-independent.  All eight occurrence charts and their residue-wedge signs
are retained.  Orientation changes multiply the zero map by \(\pm1\).

The ordinary physical image has rank zero.

The comparison cone retains the coefficient grade but no physical class:

\[
\boxed{
\text{nonzero coefficient support}
+
\text{zero physical image}.
}
\]

## Narrow theorem

\[
\boxed{
\text{Every divisor component of the 36 C8 coefficient discriminants has
zero ordinary supported pullback from the literal Bunch--Davies chamber.}
}
\]

No new Carrier structure is required or justified.  The result strengthens
the surviving architecture

\[
\text{shared Carrier and calculus}
+
\text{sector-specific coefficient objects}
+
\text{independent physical-chain selection}.
\]

The published negative-imaginary prescription may instead determine a
continued Leray germ. Whether that germ has nonzero Picard--Lefschetz pairing
at the C8 discriminants is not inferred from ordinary support and is the next
gate. Coefficient monodromy is not classified here.

## Durable verification

- `research/benincasa/eight-site-supported-activation-conventions.md`
- `research/benincasa/marici-gm/src/bin/eight_site_supported_activation_gate.rs`
- `research/benincasa/results/eight-site-supported-activation-gate.json`
- source inventory theorem: Entry 1909
- ledger sequence claim: `seqclaim-a3249cf0e89b85a42b3fe33d`
- epistemic graph event: `ev-000000002292-a99a061e-22cf-4fee-9b65-f9e25d0d5edd`
