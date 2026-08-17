---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# The Positive Chain Does Not Transgress the Exact Three-Cut Packet

## Question

Entry 364 found the source-defined Cousin packet

\[
\Omega_{\rm src}\longrightarrow c_1\longrightarrow0,
\]

with (c_1) closed but exact. The remaining possibility was that pairing
with the physical relative chain turns this coefficient boundary into a
nonzero Cut-supported relative class. The hard-to-vary claim tested here is

\[
\boxed{
\partial\Gamma_{\rm phys}\text{ has nonzero incidence with }D_{\rm Cut},
\text{ transgressing }c_1.}
\]

The literal positive Bunch--Davies chain, source Cut equations, positive
Cayley--Menger sheet, and boundary-value prescription are frozen.

## Symbolic positive-cone certificate

Write

\[
a=y_{23},\qquad b=y_{31},\qquad c=y_{12},
\qquad E=x+y+z.
\]

The three marked-Cut forms are

\[
q_{\mathcal G_{12}}=E+c,
\qquad
q_{\mathcal G_{23}}=E+a,
\qquad
q_{\mathcal G_{31}}=E+b.
\]

On the source chain,

\[
x,y,z>0,qquad a,b,c\ge0.
\]

Each Cut form has coefficient one on all three positive site energies,
coefficient one on its corresponding nonnegative edge, and no negative
coefficient. Hence its exact lower bound on the full positive orthant is

\[
\inf q_{\mathcal G_{ij}}=E>0.
\]

Restricting the orthant to the frozen Cayley--Menger and signed-minor domain
cannot create a zero. The same inequality holds on every finite boundary
face (a=0), (b=0), or (c=0), and on the closure of the physical domain.

Therefore

\[
\boxed{
\overline\Gamma_{\rm phys}\cap D_{\rm Cut}=\varnothing.
}
\]

## Relative pairing

The three chain-boundary incidence numbers are

\[
(0,0,0).
\]

Retaining the six lower-denominator occurrences gives

\[
\left\langle\partial\Gamma_{\rm phys},c_1\right\rangle
=(0,0,0,0,0,0).
\]

Thus the exact Cousin packet does not transgress into a literal
Cut-supported relative/Borel--Moore class on the starting positive sheet.
The tested claim is falsified.

## Analytic-continuation qualification

This is not a vanishing theorem for the analytically continued Cut residues.
Entry 180 proved that the Bunch--Davies boundary value uniquely determines a
local Leray residue germ after continuation to
(q_{\mathcal G_{ij}}=0). Such a germ lives on a continued residue surface
with its induced positive sheet and orientation. It is not a boundary
component of the original real positive chain.

The type distinction is

\[
\boxed{
\text{zero literal chain/Cut incidence}
\not\Rightarrow
\text{zero analytically continued Leray residue}.}
\]

## Narrow result

On the physical starting chamber, the complete global packet remains

\[
\boxed{
\text{degree-zero meromorphic period}
\longrightarrow
\text{exact Cut-support grade},
}
\]

with no extra relative boundary class. The nonzero sector residue systems
belong to analytic continuation/nearby-cycle data, not to a hidden boundary
of (Gamma_{\rm phys}).

## Classification

| Datum | Classification |
|---|---|
| positive orthant and CM domain | frozen physical chain |
| lower bound (q_{\mathcal G_{ij}}\ge E) | source positivity |
| literal Cut incidence | zero |
| six-occurrence boundary pairing | zero |
| continued Leray germ | source-defined analytic continuation datum |
| new carrier datum | none |

## Evidence

- `research/benincasa/marici-gm/src/bin/three_cut_relative_chain_pairing.rs`;
- `research/benincasa/three-cut-relative-chain-pairing-certificate.json`;
- Entries 180, 188, 229, and 364.

## Next falsifier

Move from the starting real chamber to the source-defined boundary-value
continuation. Construct the three cyclic local Leray morphisms from the
single meromorphic source packet and test their compatibility on a common
continuation domain without introducing pairwise Cut poles.

The target statement is not Čech descent. It is a naturality square between:

1. analytic continuation of the degree-zero physical period; and
2. the three sectorwise residue/nearby-cycle functors applied to the exact
   Cousin support grade.

Failure of cyclic naturality would expose genuinely sector-dependent
continuation data. Success would identify analytic continuation—not carrier
gluing or literal chain boundary—as the global operation assembling the
three rank-twelve residue systems.
