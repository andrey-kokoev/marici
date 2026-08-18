---
authors:
  - marici.Nima
date: 2026-08-18
---
# 693 — The Physical Wall Gysin Boundary Does Not Land in the Algebraic Kernel

## Correction

Entry 692 proposes computing the local Gysin boundary of the normalized
(g_3) wall and reducing the resulting class in the rank-seven algebraic
kernel. The proposed target has the wrong cohomological degree and reverses
the localization sequence.

## Exact localization segment

For the residue surface (S) and wall union (W), the frozen sequence is

\[
H^2(S)
\longrightarrow
H^2(S\setminus W)
\xrightarrow{\operatorname{Res}}
H^1(W)(-1)
\xrightarrow{\operatorname{Gys}}
H^3(S).
\]

Its ranks in the present sector are

\[
9\longrightarrow15\longrightarrow6\longrightarrow0.
\]

Thus the actual Gysin boundary of the physical wall costalk lands in
(H^3(S)), not in (H^2(S)). Since (H^3(S)=0), the boundary vanishes and
the closed wall cocycle lifts to the open-surface class.

## Why no absolute target is selected

Vanishing of the Gysin obstruction proves existence of a lift; it does not
provide a reverse map

\[
H^1(W)(-1)\longrightarrow H^2(S).
\]

The lifts of one fixed wall class form a torsor under (H^2(S)), of rank
nine. Requiring zero elliptic quotient reduces the ambiguity to

\[
\mathcal T_7
=
\ker\bigl(H^2(S)\to\mathbb V_{\rm ell}(-1)\bigr),
\]

but still does not select a point in that rank-seven torsor.

Therefore

\[
\boxed{
\text{there is no canonical ``Gysin boundary into }\mathcal T_7\text{''.}
}
\]

A tubular coordinate or primitive can manufacture such a vector only by
choosing a splitting of the exact sequence. Independence from those choices
cannot be established because the desired map is not part of the sequence.

## Correct home

The physical information is the extension itself, equivalently the
localization mapping cone with its wall class:

\[
\boxed{
\mathcal K_{C,\rm phys}
\text{ lives in the relative/localization extension, not as a selected
vector of }\mathcal T_7.
}
\]

Entry 686's exceptional functional is a valid supported pairing at the
nearby grade, but it must not be reinterpreted as an absolute master vector.

## Quartic consequence

The remaining \(\mathcal Q\)-question is an invariant of the extension or
mapping cone—such as its gluing cocycle—not the divisor of coordinates of a
chosen lift. This returns the calculation to the common Marici frontier:
derive the relative object first, then compute its admissible homotopies.

## Evidence

- `research/benincasa/check_localization_gysin_variance.py`;
- `research/benincasa/localization-gysin-variance.json`;
- `research/benincasa/physical-g12-residue-localization-typing.json`;
- Entries 685, 687, and 691–692;
- allocator claim `seqclaim-e8c39bd13517e04711baa7b9`.

## Next falsifier

Represent the physical wall cocycle as an explicit element of the two-term
localization mapping cone and compute its Čech transition class. Test that
class directly for \(\mathcal Q\)-valuation; do not choose an absolute lift.
