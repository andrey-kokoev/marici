---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 711 — The Disappearing Triple Mixes Diagonal and Square-Free Second Normals

## Frozen object

Entry 706 finds that the proper grade on

\[
q_{\mathfrak g_2}q_{\mathfrak g_3}q_{\mathfrak g_{23}}
\]

has generic rank one and vanishes on \(P_i=X_i\). Entry 709 leaves this
triple as the only adjacent source cell capable of mediating between the
nonisomorphic signed pair residues.

Write

\[
\nu_i=P_i^2-X_i^2.
\]

Expanding the exact source value of \(K\) at the triple intersection gives
zero in normal orders zero and one. Its first nonzero grade is

\[
\boxed{
T_2=
X_3^2\nu_2^2
+(X_1^2-X_2^2-X_3^2)\nu_2\nu_3
+X_2^2\nu_3^2.}
\]

The next term is

\[
T_3=\nu_1\nu_2\nu_3.
\]

## Mixed normal mechanism

The quadratic grade \(T_2\) contains both diagonal directions
\(\nu_2^2,\nu_3^2\), which govern the direct residue-branch smoothings of
corrected Entry 705, and the square-free direction \(\nu_2\nu_3\), which
governs the pair radicals of Entry 698. Therefore the disappearing triple is
a source-derived mixed second-normal object; it is not confined to either
normal subspace separately.

As a binary quadratic form in \((\nu_2,\nu_3)\), its discriminant is

\[
\boxed{
(X_1^2-X_2^2-X_3^2)^2-4X_2^2X_3^2
=\ell_1\ell_2\ell_3\ell_4.}
\]

No new carrier divisor appears.

## Consequence

The restricted discriminant route of Entry 705 and the square-free pair route
of Entries 698 and 707 are not wholly disjoint after derived incidence is
restored. Their first source-defined meeting place is this disappearing
triple's second-normal cone.

This does not yet prove that the triple boundary lifts Entry 707's weighted
signed relation. It proves that the adjacent source cell has exactly the
required mixed normal type and begins at the required second order.

## Evidence

- `research/benincasa/check_disappearing_triple_second_normal.py`;
- `research/benincasa/generic_lower_collision_result.json`;
- Entries 698, corrected 705, 706, 707, and 709;
- allocator claim `seqclaim-39bc3695f0958a8222aee074`.

## Next falsifier

Compute the oriented triple-to-pair residue boundary before homogeneous
specialization, then take its second Rees symbol. Test whether its
\(\nu_2\nu_3\) component yields Entry 707's weighted signed relation after
the strict plus-occurrence identity from Entry 709 is imposed. If it does
not, the mixed triple cone is geometrically adjacent but does not supply the
needed chain homotopy.
