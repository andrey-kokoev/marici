---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 689 — The Ramified Physical Conductor Leaves One Oriented Costalk Line

## Hard-to-vary claim

After retaining both normalization sheets of the \(g_3\) wall and both
ramified tangency roots, the total-energy physical residue does not cancel.
It defines one nonzero oriented conductor costalk. Its four leading
coefficients obey a forced outer-product sign law, so no character
projector or absolute master lift is needed to identify the line.

## Frozen local geometry

On the shared wall

\[
q_{g_3}=a+b+z=0,
\]

the Cayley--Menger restriction is

\[
K|_{q_{g_3}}=R_3(b)^2.
\]

The normalization has two sheets

\[
w=\sigma R_3(b),
\qquad
\sigma=\pm1.
\]

Set \(E=\epsilon^2\) and \(z=E-x-y\). The two conductor roots limit to
\(b=x\) and are indexed by \(\tau=\pm1\).

## Exact oriented residues

Use the source orientation \(+db\) and the literal physical numerator,
occurrence product, and remaining shared-wall product:

\[
\rho_{\sigma,\tau}
=
\left.
\frac{-E}
{\sigma\,\partial_bR_3,
(b-x)(-b-z-y)(b-y-z)(-b-x-2z)}
\right|_{b=b_\tau}.
\]

Direct Puiseux expansion gives

\[
\boxed{
\rho_{\sigma,\tau}
=
\sigma\tau C\,\epsilon^{-1}+O(1),
}
\]

where

\[
C=
\frac{\sqrt2}
{32x^2y^2\sqrt{-xy/(x+y)}}.
\]

Thus the four normalized coefficients form

\[
\begin{array}{c|cc}
&\tau=-&\tau=+\\
\hline
\sigma=-&+C&-C\\
\sigma=+&-C&+C
\end{array}.
\]

## Costalk interpretation

For each conductor node, the two normalization-sheet residues satisfy the
dualizing relation

\[
r_++r_-=0.
\]

They therefore define, rather than kill, the one-dimensional
anti-invariant conductor costalk. The two ramifying roots carry opposite
coefficients; after the Kummer normalization by \(\epsilon\), they are
the two presentations of the same nearby line under the deck exchange.

Consequently:

\[
\boxed{
\dim\mathcal K_{C,\mathrm{phys}}=1,
\qquad
\mathcal K_{C,\mathrm{phys}}\ne0.
}
\]

The line is anti-invariant under the surface normalization involution. This
is source-derived character data that any localization-triangle morphism
must preserve.

## Relation to Entry 687

Entry 687 proves that this finite costalk has zero direct infinity
restriction. The present nonvanishing is therefore not an elliptic
projection:

\[
\mathcal K_{C,\mathrm{phys}}
\longrightarrow
\psi_E\mathbb V_{\rm ell}(-1)
=0.
\]

Its only remaining global role is through the connecting morphism into the
algebraic/relative extension.

## Quartic audit

The local coefficient \(C\), root equation, and sign law contain no
\(\mathcal Q\) factor. Hence \(\mathcal Q\) is absent from the first
local conductor grade. This does not exclude it from transport or gluing of
the costalk line.

## Classification

- ramified conductor costalk: one nonzero Kummer coefficient line;
- normalization-sheet character: anti-invariant;
- direct elliptic image: zero;
- algebraic connecting class: not yet computed;
- new carrier datum: none;
- possible \(\mathcal Q\)-home: transport/gluing of the supported line
  only.

## Next falsifier

Compute the algebraic target character decomposition of the rank-seven
infinity-Gysin kernel and determine whether it contains exactly one
compatible anti-invariant line. If none exists, the connecting morphism is
forced to vanish. If exactly one exists, compute the source-derived scalar
by a local Gysin comparison; do not choose a splitting.

## Evidence

- `research/benincasa/compute_g3_oriented_conductor_costalk.py`;
- `research/benincasa/g3-oriented-conductor-costalk.json`;
- Entries 594--595 and 683--687;
- allocator claim `seqclaim-6de7ac0de23ad0dc65df0b7f`.

## Outcome contract

~~~json
{
  "claim": "The two normalization sheets cancel the ramified physical conductor residue completely.",
  "status": "falsified",
  "oriented_costalk_dimension": 1,
  "oriented_costalk_nonzero": true,
  "normalization_sheet_character": "anti-invariant",
  "direct_elliptic_image_rank": 0,
  "Q_in_first_local_grade": false,
  "new_carrier_datum": false,
  "next_experiment": "Match the costalk character against the rank-seven algebraic Gysin-kernel characters."
}
~~~
