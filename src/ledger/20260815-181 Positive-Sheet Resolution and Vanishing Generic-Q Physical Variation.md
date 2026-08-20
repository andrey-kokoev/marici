---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# Positive-Sheet Resolution and Vanishing Generic-Q Physical Variation

## Record

Date: 2026-08-15

Status: generic nonsoft relative-cycle theorem for the
\(q_{\mathcal G_{12}}\)-residue sector.

This entry continues entries 161, 169, 175, 178, and 180. It changes no
source denominator, normalization, marked support, coefficient summand, or
carrier cell.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

\[
\boxed{
\text{the source-positive sheet extends through a simultaneous resolution
over generic }\mathcal Q=0,
\text{ and its physical residue variation is zero.}
}
\]

The finite falsifier was any sheet-level component degeneration or
incidence change over a generic transverse \(\mathcal Q\)-disk that escaped
the frozen raw discriminant census.

No component was allowed to be added after inspecting \(\mathcal Q\).

## Positive-sheet component labels

For every signed Cayley--Menger face support \(L\), entries 161 and 175
established the exact identity

\[
\overline K|_L=R_L^2.
\]

On the compactified residue surface

\[
\overline S:\qquad W^2=\overline K,
\]

the pullback splits canonically as

\[
D_L^+=\{L=0,W=+R_L\},
\qquad
D_L^-=\{L=0,W=-R_L\}.
\]

The three active source poles that coincide with face supports are fixed
without relying on inconsistent shorthand labels:

\[
q_{\mathfrak g_1}=b-y-z=b-E+x,
\]

\[
q_{\mathfrak g_2}=a-x-z=a-E+y,
\]

\[
q_{\mathfrak g_3}=a+b+z.
\]

For each, the algebraic pullback of the pole divisor contains both
\(D_L^+\) and \(D_L^-\). The remaining active lines

\[
q_{\mathfrak g_{23}}=b-x,
\qquad
q_{\mathfrak g_{31}}=a-y
\]

retain their ordinary full pullbacks.

Entry 180 fixes the positive source sheet. On a real source boundary
segment,

\[
W=+\sqrt{\overline K}=|R_L|.
\]

Therefore the physical minor boundary obeys the segmentwise rule

\[
\boxed{
\Gamma_{\rm phys}\cap L
\subset D_L^{\operatorname{sign}R_L}.
}
\]

It is not one global algebraic component. It moves from \(D_L^+\) to
\(D_L^-\) only at

\[
R_L=W=0,
\]

where the two pullback components and the ramification/domain boundary
meet. This is existing relative-chain geometry, not a new carrier stratum.

## Sheet-switch closure lemma

At an intersection \(p\) of two forced-square supports,

\[
K(p)=R_i(p)^2=R_j(p)^2.
\]

Hence

\[
(R_i-R_j)(R_i+R_j)=0.
\]

Away from \(K(p)=0\), exactly one of \(R_i=R_j\) and \(R_i=-R_j\) holds,
and that relation is locally constant. A sheet-level incidence can switch
only if

\[
R_i=R_j=0,
\]

equivalently if the frozen branch-at-pair condition

\[
K(p)=0
\]

holds.

Thus sheet selection introduces no hidden discriminant class. Every
possible sheet-level change is detected by the already frozen surface,
line-degeneration, coincidence, branch-at-pair, triple-incidence, or
infinity-direction conditions.

The exact multivariate checker rejected irreducible \(\mathcal Q\) from
all 1,719 nonconstant candidates, including:

- 60 line-coincidence conditions;
- 250 branch-at-pair conditions;
- 1,360 triple-incidence conditions.

This closes the exhaustiveness gap left open in entry 175.

## Simultaneous resolution

Choose a generic point

\[
\eta\in\{\mathcal Q=0\}
\]

outside soft support and every frozen non-\(\mathcal Q\) surface,
coefficient, component, and incidence divisor. Take a sufficiently small
disk \(\Delta\) transverse to \(\mathcal Q=0\) at \(\eta\).

Over \(\Delta\), the following have constant type:

- the smooth compactified residue surface;
- every split pole/face component \(D_L^\pm\);
- finite pair and higher incidence sections;
- the four universal infinity-direction multiple sections;
- the forced-square ramification triple sections.

Blow up the smooth relative incidence sections in decreasing multiplicity.
This includes the universal infinity sections and the ordinary
ramification triple sections. The frozen tangency and branch-at-pair
exclusions ensure that no new parameter-dependent center appears.

The result is a simultaneous relative SNC pair

\[
(\widetilde{\mathcal S}_\Delta,
 \widetilde D_{\rm pole}\cup
 \widetilde D_{\rm minor}\cup
 \widetilde D_\infty)
\longrightarrow\Delta.
\]

Every blowup center is an incidence stratum of the predeclared marked
residue geometry. No new carrier generator is used.

## Monodromy and variation

The resolved proper pair is smooth over the full disk. Its relative
Betti/de Rham local system extends across the origin. Therefore

\[
\boxed{
T_{\mathcal Q}=1,
\qquad
N_{\mathcal Q}=0.
}
\]

The canonical source physical residue germ from entry 180 lifts to this
simultaneous resolution. Consequently

\[
\boxed{
\operatorname{Var}_{\mathcal Q}
(\Gamma_{\rm phys}^{\rm res})
=
(T_{\mathcal Q}-1)\Gamma_{\rm phys}^{\rm res}
=
0.
}
\]

## Classification

At generic nonsoft kinematics in the
\(q_{\mathcal G_{12}}\)-relative residue sector:

- existing carrier: sufficient;
- coefficient support at \(\mathcal Q=0\): none;
- physical relative-cycle support at \(\mathcal Q=0\): none;
- \(\mathcal Q\): apparent alphabet data in this sector;
- new carrier datum: none.

This is the strongest update so far for H2:

\[
\text{shared carrier and calculus}
+
\text{sector-specific coefficient objects}.
\]

The algebraic quartic does not force a cosmology-specific carrier
incidence generator.

## Scope boundary

The theorem is generic along \(\mathcal Q=0\). It excludes intersections
with soft support and with the frozen discriminant or coefficient union.

It also does not claim that \(\mathcal Q\) is apparent in every sector of
the complete three-site wavefunction. It proves that the
\(q_{\mathcal G_{12}}\) marked relative residue sector does not supply its
monodromy.

## Exact evidence

- research/benincasa/check_generic_q_log_smoothness.rs
  - SHA-256
    7286fd583eb4d4631a7147cd92c2330c5902b4448569194ef4e1c4c162f3d199
- research/benincasa/generic_q_log_smoothness_certificate.md
  - SHA-256
    9e0bcabe2ef035490de15bc44b81ebeb261c2c0a0b0c13a7e9719c381851294e
- research/benincasa/published_boundary_value_leray_uniqueness.md
  - SHA-256
    d1cfa9672ae7af8b4c8f873e1553d070a14b7f7b61e886ab59edd4cb36e63c50
- research/benincasa/q_sheet_resolution_certificate.md
  - SHA-256
    b97ec536ad9b1cc9addc61457764fe92fdf90e26157543c96dc1772ad87d1f23
- research/benincasa/q_sheet_resolution_result.json
  - SHA-256
    78f9488e17e66cfbb82a45fb35f0d80307a013c9f44ab17c885fda489c1be966
- research/benincasa/verify_q_sheet_resolution.rs
  - SHA-256
    4562ad8cef255d6b1cbfbc9858477071d1185c4b26349d18a84510b7ea3ce255

The last verifier is a finite implication checker over all \(2^{12}=4096\)
split-face sign selections. Its compilation was not used as a premise:
the algebraic input is the independently executed 1,719-condition
certificate, and the sheet-switch lemma is displayed above.

## Next finite falsifier

The generic-\(\mathcal Q\) provenance question is now closed negatively for
this residue sector. The next attack must move to a different possible
source of the published algebraic letter without reopening the carrier:

1. test the other cyclic residue sectors
   \(q_{\mathcal G_{23}}\) and \(q_{\mathcal G_{31}}\);
2. test whether \(\mathcal Q\) is generated only after summing sectors or
   applying the physical integration chain;
3. recover the unpublished companion \(P\) or first-order factor
   \(\mathcal L_1\) if an author-level object becomes available.

## Outcome contract

~~~json
{
  "claim": "The source-positive split components admit a simultaneous resolution over a generic transverse Q disk, and the canonical q_G12 physical residue germ has zero Q variation.",
  "status": "survived",
  "physical_sheet_rule": "W=abs(R_L), hence D_L^{sign(R_L)} segmentwise",
  "simultaneous_resolution": true,
  "T_Q": "identity",
  "N_Q": "0",
  "Var_Q_Gamma_phys_res": "0",
  "classification": "Q_apparent_in_generic_nonsoft_q_G12_relative_residue_sector",
  "new_carrier_datum": "none",
  "next_experiment": "Apply the same frozen test cyclically to q_G23 and q_G31, then test sector-sum/physical-chain provenance."
}
~~~
