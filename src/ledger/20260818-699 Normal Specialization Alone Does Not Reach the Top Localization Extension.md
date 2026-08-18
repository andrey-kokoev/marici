---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 699 — Normal Specialization Alone Does Not Reach the Top Localization Extension

## Hard-to-vary claim

Let

\[
i:B_{X}\hookrightarrow B_{X,P},
\qquad
I=(\nu_1,\nu_2,\nu_3),
\qquad
\nu_i=P_i^2-X_i^2
\]

be the homogeneous embedding. The second normal grade of the generic lower
family does not canonically land in the homogeneous top-sector localization
extension by normal specialization alone.

## Frozen support vertices

The generic lower source family has denominator support

\[
S_{\rm low}
=\{q_{g_1},q_{g_2},q_{g_3},q_{g_{23}}\}.
\]

The corresponding complete homogeneous top family has

\[
S_{\rm top}
=S_{\rm low}\cup\{q_{\mathcal G_{12}}\}.
\]

Entry 698 shows that the first nonzero transverse terms lie in

\[
\operatorname{gr}^2_I\mathcal M_{\rm low}
\]

and are labelled by \(\nu_i\nu_j\). Taking an ordinary or Rees normal grade
acts on the base coefficients of the frozen twisted de Rham complex. It does
not adjoin a denominator. Hence every labelled second-normal component
remains at the support vertex \(S_{\rm low}\):

\[
\operatorname{supp}_{\rm den}
\left(\operatorname{gr}^2_I\mathcal M_{\rm low}\right)
=S_{\rm low}.
\]

But the top localization extension occupies the adjacent deletion-cube
vertex containing \(q_{\mathcal G_{12}}\). Therefore

\[
\boxed{
\operatorname{gr}^2_I\mathcal M_{\rm low}
\not\longrightarrow
\mathcal M_{\rm top}
\quad\text{canonically from normal specialization alone.}
}
\]

This is a typing obstruction, not a vanishing theorem for every possible
cross-sector map.

## Audit of the available source operations

The frozen paper defines the two families separately:

- `eq:subsec_1235` defines the four-denominator lower family and states that
  its generic \(X_i\ne P_i\) incarnation has rank 34 and algebraic letters;
- `eq:elliptic_subsec` then introduces sectors *containing*
  \(q_{\mathcal G_{12}}\), but the displayed basis and Picard--Fuchs analysis
  are homogeneous.

The possible connecting operations have the following status.

\[
\begin{array}{c|c|c|c}
\text{operation}&\text{domain contains labelled }N_2&\text{target}&\text{verdict}\\
\hline
d_{X,P}\text{ / Gauss--Manin}&\text{yes}&\mathcal M_{\rm low}^{\rm gen}&
\text{preserves pole support}\\
\text{IBP in }y_e&\text{yes}&\text{lower family/subsectors}&
\text{cannot create an absent }q_{\mathcal G_{12}}\text{ pole}\\
\text{residue at }q_{\mathcal G_{12}}&\text{no}&
\mathcal M_{4|\mathcal G_{12}}&
\text{requires that pole in the domain}\\
\text{deletion/localization}&\text{potentially}&
\mathcal M_{5}^{\rm gen}&
\text{generic five-pole map not supplied}\\
\text{incidence/Gysin}&\text{no typed instance}&
\text{physical wall cone}&
\text{no pre-specialization coherence cell supplied}
\end{array}
\]

Parameter differentiation can raise the power of a denominator already
present because it differentiates that denominator's coefficients. If the
exponent of \(q_{\mathcal G_{12}}\) is initially zero, however, no such term
is generated. Thus both the Gauss--Manin and IBP operations are
\(E\)-linear on the generic lower base but remain at the lower support
vertex.

Deletion--restriction is the only candidate with the correct support
variance. Yet the available homogeneous rank identity

\[
35=15+20
\]

does not specify its generic \((X,P)\)-family, its connection matrix, or a
filtered map on the labelled conormal module. Consequently there is no
matrix whose filtration degree or \(\mathcal Q\)-valuation can presently be
computed without inventing source data.

## Required mixed operation

Any admissible comparison must separately supply localization at
\(q_{\mathcal G_{12}}\) and then test compatibility with homogeneous
specialization. The smallest typed candidate is the Beck--Chevalley square

\[
\begin{CD}
i^*\operatorname{Loc}_{q_{\mathcal G_{12}}}\mathcal M_{\rm low}^{\rm gen}
@>>> i^*\mathcal M_{\rm top}^{\rm gen}\\
@VVV @VVV\\
\operatorname{Loc}_{i^*q_{\mathcal G_{12}}}
i^*\mathcal M_{\rm low}^{\rm gen}
@>>> \mathcal M_{\rm top}^{\rm hom}.
\end{CD}
\]

Only after constructing this square may one take \(\operatorname{gr}^2_I\)
and ask whether a labelled \(\nu_i\nu_j\) class enters the rank-twenty
residue/localization extension. The source currently fixes the two support
vertices and their ranks, but it does not print this mixed comparison map.

## Consequence for \(\mathcal Q\)

Entry 698 already proves that the leading lower normal coefficients are
coprime to \(\mathcal Q\). The present audit blocks the remaining shortcut:
those coefficients cannot be inserted into the top extension merely by
reinterpreting their normal grade as a localized class.

Thus \(\mathcal Q\) is still not derived from the generic lower radicals.
The surviving possibility is narrower:

\[
\boxed{
\mathcal Q\text{ could occur only in the mixed
normal--localization comparison or its extension data.}
}
\]

No new carrier wall is indicated.

## Classification

- existing carrier: the Cayley--Menger family and frozen marked planes;
- coefficient data: the labelled second-normal module
  \(I^2/I^3\otimes i^*\mathcal M_{\rm low}\);
- missing datum: a source-derived base-change/localization morphism adjoining
  \(q_{\mathcal G_{12}}\);
- new carrier datum: none.

## Evidence and scope

- arXiv:2408.16386v2, equation `eq:subsec_1235`;
- Entries 185, 338, 596, and 698;
- `research/benincasa/check_normal_specialization_localization_gate.py`;
- `research/benincasa/normal-specialization-localization-gate.json`;
- allocator claim `seqclaim-26d634c395a5a534c10997a9`.

The checker verifies denominator-support grading exactly. This entry does not
claim that no mixed morphism exists; it says that normal specialization alone
does not define one.

## Next falsifier

Construct the generic five-pole family by adjoining
\(q_{\mathcal G_{12}}\) before imposing \(P_i=X_i\). Derive the specialization
maps on its deletion--restriction triangle and test the Beck--Chevalley
commutator at second normal order. A nonzero commutator with
\(\mathcal Q\)-support would place \(\mathcal Q\) in extension data; a
commuting, \(\mathcal Q\)-regular square would eliminate this lower-to-top
route.
