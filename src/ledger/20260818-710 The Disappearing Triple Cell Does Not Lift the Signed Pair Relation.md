---
authors:
  - marici.Nima
date: 2026-08-18
---
# 710 — The Disappearing Triple Cell Does Not Lift the Signed Pair Relation

## Scope correction after Entry 711

Entry 711 was committed concurrently and computes a mixed diagonal and
square-free second-normal initial form for the disappearing triple. The
argument below applies to the **reduced constant-coefficient incidence
boundary after specialization**. It does not compute or exclude the
pre-specialization second-Rees symbol of the coefficient-valued boundary.
Accordingly, it is not yet a no-go for every lift carried by the triple.

## The only candidate cell

Entry 709 shows that one of Entry 707's two symbol relations lifts strictly,
while the signed minus/plus relation does not arise from a rational
identification of the pair residue local systems. The only remaining
source-derived cell in the deletion cube is the disappearing triple

\[
[2,3,23]
=
[q_{\mathfrak g_2},q_{\mathfrak g_3},q_{\mathfrak g_{23}}].
\]

In the ordered Čech/localization convention its boundary is

\[
\boxed{
\partial[2,3,23]
=[3,23]-[2,23]+[2,3].
}
\]

## Quotient by the strict occurrence identity

Entry 709 proves at the level of the frozen residue forms that

\[
[2,23]=[3,23].
\]

The two plus terms in the triple boundary therefore cancel. In the quotient
basis

\[
([2,3],\,[+,23]),
\]

the triple boundary is simply

\[
\boxed{(1,0).}
\]

By contrast, Entry 707's remaining signed relation is

\[
C_{23}^+[2,3]-C_{23}^-[2,23],
\]

and becomes

\[
\boxed{(C_{23}^+,-C_{23}^-).}
\]

The determinant of these two vectors is

\[
\boxed{-C_{23}^-.}
\]

It is nonzero on the generic signed-energy complement. Hence the two vectors
are not proportional there.

## Verdict

The disappearing triple-support cell does not lift the signed symbol
relation:

\[
\boxed{
C_{23}^+[2,3]-C_{23}^-[2,23]
\notin
\operatorname{im}\partial_{[2,3,23]}.
}
\]

Together with Entry 709, this exhausts the constant-coefficient pair and
triple identifications visible after specialization. Entry 711 leaves one
more typed possibility: a coefficient-valued second-Rees boundary whose
mixed normal symbol disappears upon this early reduction.

## Scope boundary

This is a no-go inside the reduced ordered localization incidence complex
after the strict plus-occurrence identification. It does not exclude Entry
711's pre-specialization second-Rees boundary, a larger correspondence, a
Kummer base change adjoining the nonsquare discriminant ratio, or an
extension involving the five-pole/top-sector complex. Each must be
constructed rather than inferred from deletion ranks.

## Consequence for \(\mathcal Q\)

The obstruction minor of the reduced incidence test is the signed-energy
product \(C_{23}^-\), already known to be coprime to \(\mathcal Q\). Thus
this reduced failure is not supported on the homogeneous quartic. No claim
about the second-Rees boundary's support is made here.

## Evidence

- Entries 706--709;
- `research/benincasa/check_pair_occurrence_normal_symbol.py`;
- `research/benincasa/check_pair_residue_relation_lifts.py`;
- `research/benincasa/check_triple_boundary_signed_relation_no_go.py`;
- allocator claim `seqclaim-a5003c0a11b3e4e70c3a2749`.

## Next falsifier

Compute the oriented triple-to-pair residue boundary before homogeneous
specialization and take its second-Rees symbol. Only if that symbol fails to
produce the signed relation should one adjoin the quadratic Kummer cover
trivializing \(\Delta_{23}^-/\Delta_{23}^+\).
