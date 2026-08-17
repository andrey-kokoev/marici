---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# First Conductor--Energy Tangency Requires One Marked Coefficient Weight

## Question

Entry 380 closed the rational support of the cusp exceptional divisor. The
first unresolved center in Entry 370 is the conductor--energy tangency

\[
(r,s)=\left(1,\frac12\right).
\]

In the \(x=1\) chart of the generic marked engine this is

\[
(u,v)=(E_T,\ell_3)=(1,2).
\]

Freeze the claim

\[
\boxed{\text{the canonical marked projection cannot extend across this
center using the existing tangency blowup and a conductor coefficient
lattice.}}
\]

No new support factor or carrier center may be introduced.

## Frozen charts and frame

Use both point-blowup charts

\[
u=1+t,\quad v=2+tr,
\]

\[
v=2+t,\quad u=1+tr.
\]

The unique frozen tangent direction is \(r=0\): the signed-energy line
\(v=2\) and the relevant conductor branch have the same tangent there.
The source sign and Kummer shear remain

\[
\widehat\Omega_{111}=\Omega_{111}+\frac{e_6}{8u}.
\]

## Raw failure

For each chart, 20 exact exceptional directions and 55 exact normal samples
are reduced over \(\mathbf F_{2305843009213693951}\). Before an additional
local lattice is applied, the canonical seven-coordinate projection has

\[
\min\operatorname{ord}_t A_t=-2,
\qquad
\min\operatorname{ord}_t A_r=-1.
\]

The nonlogarithmic-entry masks coincide:

\[
\boxed{M_{\rm radial}=M_{\rm tangent}=120.}
\]

In the row-major ordering of three marked rows against

\[
(\widehat\Omega_{111},\Omega_{101},\Omega_{110},e_6,e_7,e_8,e_9),
\]

mask 120 consists exactly of

\[
\widehat\Omega_{111}\longrightarrow(e_6,e_7,e_8,e_9).
\]

Thus the raw frame genuinely fails, but its failure is confined to one
source-defined marked row and the algebraic kernel.

## Minimal conductor lattice

The valuation inequalities force one and only one positive marked weight:

\[
\boxed{
(w_{111},w_{101},w_{110};w_6,w_7,w_8,w_9)
=(1,0,0;0,0,0,0).
}
\]

No weight is assigned after inspecting individual coordinates. Applying this
single saturation gives

\[
\boxed{
\min\operatorname{ord}_t A_t'=-1,
\qquad
\min\operatorname{ord}_t A_r'=0.
}
\]

All 84 transformed rational coordinates reconstruct. Fifty-four are nonzero;
the radial and tangent degree bounds are respectively \((1,1)\) and
\((1,2)\).

## Support factorization

Every transformed denominator divides a power of the predeclared tangent
direction. The complete root set is

\[
\boxed{\{0\}.}
\]

No residual irreducible denominator remains.

## Verdict

The tested claim is falsified at this center:

\[
\boxed{\text{the first conductor--energy tangency is logarithmic after a
single marked conductor weight, with no new support factor.}}
\]

The raw failure is not discarded. It identifies a genuine sector-specific
coefficient lattice. The lattice lives over the support-resolution center
already forced by the conductor and signed-energy divisors; it does not add a
carrier stratum.

## Classification

| Datum | Classification |
|---|---|
| center \((1,\frac12)\) | existing conductor--energy tangency |
| raw mask 120 | marked-to-algebraic frame degeneration |
| weight \(w_{111}=1\) | conductor/Rees coefficient lattice |
| denominator root \(r=0\) | frozen common tangent direction |
| residual support factor | none |
| new carrier datum | none found |

## Epistemic boundary and next falsifier

This is an exact generic-fiber de Rham test of one of the four tangencies and
the canonical seven-coordinate projection. It does not prove that the same
weight works at the other three tangencies, the four elliptic base points,
the five exact-lift-gauge coordinates, or the physical relative chain.

The next test transports this predeclared one-step conductor weight to the
remaining three tangencies. Failure of the same transported lattice is a
coefficient-architecture failure; a denominator outside their frozen tangent
directions is the carrier-level falsifier.

## Evidence

- `research/benincasa/marici-gm/src/bin/marked_tangency_support.rs`;
- `research/benincasa/marked-tangency-support-certificate.json`;
- `research/benincasa/triple-soft-exceptional-resolution-certificate.json`;
- Entries 370--371, 374, 378, and 380.
