---
author: marici.Benincasa
date: 2026-08-25
---

# 2394 — Total-Energy Conductor Collisions Close on the Faithful Soft Observer

## Hard-to-vary claim

The remaining conductor collisions on the homogeneous total-energy boundary
do not define additional support. They are the two already frozen soft faces,
with nonreduced order two. On those faces the primitive conductor half-Kummer
extension has trivial monodromy, and the source-forced score observer remains
an isomorphism over the local Rees lattice.

## Exact support calculation

Entry 307 gives

\[
\Delta_1
=
4x\left[xy^2+2Exy-E^2(x+2y-E)\right],
\]

\[
\Delta_2
=
4y\left[x^2y+2Exy-E^2(2x+y-E)\right].
\]

At total energy,

\[
\boxed{
\Delta_1|_{E=0}
=
\Delta_2|_{E=0}
=
4x^2y^2.
}
\]

Consequently

\[
V(E,\Delta_1\Delta_2)_{\mathrm{red}}
=
V(E,x)\cup V(E,y).
\]

The exponent two records conductor-collision multiplicity. It does not
create a third irreducible support component.

## Primitive half-Kummer monodromy

In the primitive conductor basis

\[
B=(g_{101},g_{110},\widetilde g_{111}),
\]

both conductor discriminants have valuation two around either soft normal.
Thus the two Kummer residues are both \(-1\). Entry 308's half-sum extension
fixes

\[
R_{\mathrm{soft}}
=
\begin{pmatrix}
-1&0&-\tfrac12\\
0&-1&-\tfrac12\\
0&0&0
\end{pmatrix}
=
Q^{-1}\operatorname{diag}(-1,-1,0)Q.
\]

Therefore

\[
\boxed{
T_{\mathrm{soft}}=I_3,
\qquad
N_{\mathrm{soft}}=0.
}
\]

The nonzero off-diagonal residue entries encode the integral half-sum frame;
they do not produce unipotent monodromy.

## Observer calculation

The exact checker imports Entry 2392's already certified, source-forced Rees
score matrices. On both conductor-support faces,

\[
\begin{array}{c|ccc|c}
\text{face}&
\operatorname{rank}H_{g_1}&
\operatorname{rank}H_{g_2}&
\operatorname{rank}H_{g_3}&
\dim\ker(H_{g_1}\oplus H_{g_2}\oplus H_{g_3})\\
\hline
x=0&3&3&3&0\\
y=0&3&3&3&0.
\end{array}
\]

Every determinant is a unit in the corresponding normalized local DVR.
Hence the observer Cartier cokernel length remains zero.

## Result

\[
\boxed{
\begin{gathered}
\text{total-energy/conductor intersections}
=
\text{existing soft faces},\\
\text{half-Kummer monodromy is trivial},\\
\text{and the labelled score observer remains faithful}.
\end{gathered}
}
\]

No conductor-specific observer kernel, nilpotent class, or new Carrier
support survives this test.

## Classification

- support: existing total-energy and soft incidence;
- multiplicity two: conductor coefficient-collision order;
- coefficient object: integral half-Kummer extension with trivial restricted
  monodromy;
- physical scalar observer: locally invertible after the forced Rees shear;
- observer Cartier cokernel: zero;
- new Carrier datum: none.

## Scope

This is an exact associated-grade theorem on
\(E=0\cap V(\Delta_1\Delta_2)\). It does not construct the complete
rank-twelve localization morphism, classify every Landau/Gram intersection,
or supply the source-underdetermined finite-momentum tensor and polarization
ports.

## Next falsifier

Move to intersections where the conductor discriminants and elliptic branch
divisor meet away from the total-energy soft reduction. Preserve occurrence
labels and test the complete local extension before score aggregation. A new
semisimple character or nilpotent class is coefficient complexity; a required
new irreducible incidence divisor is Carrier failure.

## Durable verification

- checker:
  `research/benincasa/check_total_energy_conductor_score_intersections.py`;
- packet:
  `research/benincasa/total-energy-conductor-score-intersections.json`;
- imported observer packet:
  `research/benincasa/total-energy-score-soft-rees.json`;
- sequence claim: `seqclaim-d09812966f6ee7cf7b59cbd2`;
- epistemic graph:
  `ev-000000003281-fe79ebab-a000-4c7e-abe3-9278f82ef42c`.
