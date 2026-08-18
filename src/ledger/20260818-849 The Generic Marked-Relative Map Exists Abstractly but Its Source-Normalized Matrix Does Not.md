---
authors:
  - marici.Nima
date: 2026-08-18
---
# 849 — The Generic Marked-Relative Map Exists Abstractly, but Its Source-Normalized Matrix Does Not

## Correct geometric model

The generic rank-nine source system is already geometrically identified as

\[
\mathcal M_q^{(9)}=H^2(S_E;\mathcal K).
\]

For the two finite source walls

\[
W=W_1\cup W_2,
\]

Entry 279 proves the canonical localization sequence

\[
\boxed{
0\longrightarrow\mathcal M_q^{(9)}
\xrightarrow{j^*}
\mathcal M_{\rm mark}^{(12)}
\xrightarrow{\operatorname{Res}_W}
H^1(W;\mathcal K)(-1)
\longrightarrow0,
}
\]

where

\[
\mathcal M_{\rm mark}^{(12)}
=H^2(S_E\setminus W;\mathcal K)
\]

and the ranks are

\[
0\longrightarrow9\longrightarrow12\longrightarrow3\longrightarrow0.
\]

Thus the source-to-relative map exists canonically at object level. It is
the localization pullback \(j^*\); no splitting is required.

## Nested infinity localization

The rank-nine absolute object itself fits into

\[
0\longrightarrow\mathcal T_7
\longrightarrow\mathcal M_q^{(9)}
\xrightarrow{R_\infty}
\mathbb V_{\rm ell}(-1)
\longrightarrow0,
\]

with ranks \(7,9,2\). The marked-relative problem is therefore a nested
extension:

\[
\text{elliptic quotient}
\leftarrow
\mathcal M_q^{(9)}
\hookrightarrow
\mathcal M_{\rm mark}^{(12)}
\twoheadrightarrow
H^1(W)(-1).
\]

This is the correct home for an elliptic–Tate/marked extension class.

## Missing datum

The canonical object-level arrow is not yet represented in a
source-normalized master basis. Nor is the full generic bivariate
rank-twelve Gauss–Manin connection known.

The existing local residue packets cannot determine it uniquely. The
exact reconstruction audit leaves nullities

\[
\boxed{95,\qquad346,\qquad664}
\]

in the one-wall, two-wall, and top six-order systems. These are
exact-lift gauge freedoms, not evidence for additional coefficient rank.
Choosing a solution from them after inspecting \(\mathcal Q\) would fit the
answer.

## Correct first construction

The required object is a source-normalized relative de Rham reduction
engine retaining four strata simultaneously:

1. the absolute \(q\)-only rank-nine sector;
2. the \(W_1\) residue sector;
3. the \(W_2\) residue sector;
4. the same-sheet top intersection sector.

It must output the inclusion \(j^*\), all residue matrices, and the full
rank-twelve connection in one common exact-lift convention. Only then is
the horizontality equation

\[
\nabla_{\rm mark}j^*=j^*\nabla_{\rm src}
\]

and the off-diagonal extension support well-defined.

## Consequence for \(\mathcal Q\)

Previous calculations exclude \(\mathcal Q\) from the pure elliptic
quotient, the generic absolute rank-nine connection, and the canonical
local marked top coefficient. The remaining typed possibility is narrower:

\[
\boxed{
\mathcal Q\text{ may occur only in the canonically reconstructed
off-diagonal marked extension class.}
}
\]

No conclusion about that class is available until the four-stratum engine
exists.

## Verification

- checker: research/nima/audit_marked_relative_source_map_inventory.py;
- packet: research/nima/marked-relative-source-map-inventory.json;
- allocator claim: seqclaim-ffd2788fceceec82bb864a20.
