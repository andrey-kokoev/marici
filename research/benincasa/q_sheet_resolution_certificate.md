# Generic-Q sheet resolution and physical variation certificate

Date: 2026-08-15

## Result

For the canonical source-defined \(q_{\mathcal G_{12}}\)-residue germ,
\[
\boxed{\operatorname{Var}_{\mathcal Q}
(\Gamma_{\rm phys}^{\rm res})=0}
\]
at a generic nonsoft point of \(\mathcal Q=0\), away from the already
frozen discriminant union.

This is a statement about the \(q_{\mathcal G_{12}}\) relative residue
sector. It does not assert that every occurrence of the algebraic letter
\(\mathcal Q\) in the full integrated wavefunction is apparent.

## Frozen algebraic components

For every signed Cayley--Menger face support \(L\), the exact source
identity is
\[
\overline K|_L=R_L^2.
\]
Its pullback to
\[
\overline S:\quad W^2=\overline K
\]
splits as
\[
D_L^+=\{L=0,W=+R_L\},\qquad
D_L^-=\{L=0,W=-R_L\}.
\]

The three active pole supports coincident with face supports are, by their
literal equations,
\[
q_{\mathfrak g_1}=b-y-z=b-E+x,
\]
\[
q_{\mathfrak g_2}=a-x-z=a-E+y,
\]
\[
q_{\mathfrak g_3}=a+b+z.
\]
For each of these, the pulled-back pole divisor contains both
\(D_L^+\) and \(D_L^-\). The remaining active poles
\[
q_{\mathfrak g_{23}}=b-x,\qquad
q_{\mathfrak g_{31}}=a-y
\]
retain their ordinary full pullbacks.

The positive source sheet gives the segmentwise domain-boundary rule
\[
W=+\sqrt{\overline K}=|R_L|
\quad\Longrightarrow\quad
\Gamma_{\rm phys}\cap L
\subset D_L^{\operatorname{sign}R_L}.
\]
Thus the physical minor boundary is not one globally selected algebraic
component. It changes from \(D_L^+\) to \(D_L^-\) only through
\[
R_L=W=0,
\]
where \(D_L^+\), \(D_L^-\), and the ramification/domain boundary meet.
This labels the physical boundary without adding a divisor or choosing a
post hoc sheet.

## Sheet-switch lemma

At an intersection \(p\) of two forced-square supports,
\[
K(p)=R_i(p)^2=R_j(p)^2,
\]
hence
\[
(R_i-R_j)(R_i+R_j)=0.
\]
Away from \(K(p)=0\), exactly one relation \(R_i=R_j\) or \(R_i=-R_j\)
holds and is locally constant. It can switch only when
\[
R_i=R_j=0,
\]
which is precisely the branch-at-pair condition \(K(p)=0\).

Therefore every change of sheet-level incidence is contained in one of the
already frozen conditions:

1. surface or branch-cover singularity;
2. component degeneration/tangency;
3. line coincidence;
4. branch-at-pair incidence;
5. triple concurrence;
6. infinity-direction branch collision.

The exact checker check_generic_q_log_smoothness.rs rejected the
irreducible \(\mathcal Q\) from all 1,719 nonconstant conditions in this
exhaustive list. In particular it checked 60 coincidence, 250
branch-at-pair, and 1,360 triple-incidence polynomials.

## Simultaneous resolution

Choose a generic point
\[
\eta\in\{\mathcal Q=0\}
\]
outside the finite union of the frozen non-\(\mathcal Q\) discriminants,
soft support, and coefficient divisors. Let \(\Delta\) be a sufficiently
small disk transverse to \(\mathcal Q=0\) at \(\eta\).

Over \(\Delta\):

- the compactified residue surface remains smooth;
- each selected split component remains smooth;
- every pair and higher incidence section has constant combinatorial type;
- the four universal infinity-direction multiple sections remain étale;
- every forced-square ramification triple section remains ordinary.

Blow up the smooth relative incidence sections in decreasing multiplicity,
including the universal infinity sections and the ramification triple
sections. Subsequent pair tangencies are absent by the frozen
line-degeneration and branch-at-pair exclusions. The resulting pair
\[
(\widetilde{\mathcal S}_\Delta,
 \widetilde D_{\rm pole}\cup
 \widetilde D_{\rm minor}\cup
 \widetilde D_\infty)
\longrightarrow\Delta
\]
is a simultaneous relative SNC resolution. All centers are strata of the
existing marked residue geometry; no carrier component is added.

## Variation

The resolved proper pair is smooth over the full disk \(\Delta\), not only
over \(\Delta^\times\). Its relative Betti/de Rham local system therefore
extends across the origin. The monodromy of a small loop around the origin
is
\[
T_{\mathcal Q}=1,
\qquad N_{\mathcal Q}=0.
\]

Ledger 180 fixes the source physical residue germ. Its lift to the
simultaneous resolution is consequently single-valued around the disk, so
\[
\boxed{
\operatorname{Var}_{\mathcal Q}
(\Gamma_{\rm phys}^{\rm res})
=(T_{\mathcal Q}-1)\Gamma_{\rm phys}^{\rm res}=0.
}
\]

## Classification

- existing carrier: sufficient and unchanged;
- split pole components: frozen pullbacks \(D_L^\pm\);
- physical minor boundary: segmentwise positive-sheet chain on those
  components, switching only at frozen ramification strata;
- \(\mathcal Q\) in this sector: apparent alphabet data, not coefficient or
  relative-cycle support;
- new carrier datum: none.

## Evidence chain

- check_generic_q_log_smoothness.rs
  - SHA-256
    7286fd583eb4d4631a7147cd92c2330c5902b4448569194ef4e1c4c162f3d199
- generic_q_log_smoothness_certificate.md
  - SHA-256
    9e0bcabe2ef035490de15bc44b81ebeb261c2c0a0b0c13a7e9719c381851294e
- published_boundary_value_leray_uniqueness.md
  - SHA-256
    d1cfa9672ae7af8b4c8f873e1553d070a14b7f7b61e886ab59edd4cb36e63c50
- verify_q_sheet_resolution.rs
  - finite sheet-selection and resolution implication checker.
