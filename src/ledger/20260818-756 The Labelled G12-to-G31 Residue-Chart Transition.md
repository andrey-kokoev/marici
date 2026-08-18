---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 756 — The Labelled G12-to-G31 Residue-Chart Transition

## Frozen charts

Write

\[
(c,a,b)=(y_{12},y_{23},y_{31}),\qquad
\Omega=dc\wedge da\wedge db,
\]

and use the Poincaré-residue convention

\[
\Omega=dq_{\mathcal G}\wedge
\operatorname{Res}_{q_{\mathcal G}=0}\Omega .
\]

On the source chart

\[
q_{\mathcal G_{12}}=E+c=0
\]

the retained coordinates and orientation are

\[
(a,b),\qquad
\operatorname{Res}_{\mathcal G_{12}}\Omega=da\wedge db.
\]

On the target chart

\[
q_{\mathcal G_{31}}=E+b=0
\]

they are

\[
(c,a),\qquad
\operatorname{Res}_{\mathcal G_{31}}\Omega=dc\wedge da.
\]

## Labelled occurrence reflection

The site transposition \(\sigma_{23}\) acts by

\[
(X_1,X_2,X_3)\longmapsto(X_1,X_3,X_2),
\]

\[
(c,a,b)\longmapsto(b,a,c).
\]

Hence the retained fiber coordinates transform as

\[
(a,b)\longmapsto(c',a')=(b,a).
\]

The five marked source poles and their target images are

\[
\boxed{
(g_1,g_2,g_3,g_{23},g_{31})
\longmapsto
(g_1,g_3,g_2,g_{23},g_{12}).
}
\]

On the \(\mathcal G_{31}\)-residue chart the target marked forms are

\[
\begin{aligned}
q_{g_1}&=c-X_2-X_3,\\
q_{g_3}&=a-X_1-X_2,\\
q_{g_2}&=c+a+X_2,\\
q_{g_{23}}&=c-X_1,\\
q_{g_{12}}&=a-X_3.
\end{aligned}
\]

After the reflected parameter substitution and
\((c',a')=(b,a)\), these are respectively the source
\(g_1,g_2,g_3,g_{23},g_{31}\) forms.

## Poincaré-residue orientation

The chart transition is not orientation-free:

\[
\sigma_{23}^*(dc'\wedge da')
=
db\wedge da
=
-da\wedge db.
\]

Therefore the labelled residue-chart transport is

\[
\boxed{
T_{12\to31}
=
-\,\sigma_{23}^*
}
\]

when written from the source oriented residue basis to the target oriented
residue basis.

The minus sign is forced by the frozen ambient volume form and residue
convention. It is not a normalization choice.

## Retained-pivot transport

The product-pole presentations were constructed independently over
\(\mathbb F_{32003}\) at the reflected points

\[
(2,3,4)\longmapsto(2,4,3),
\]

with

\[
\gamma=5,\qquad
d_{\rm ambient}=10,\qquad
d_{\rm cutoff}=5.
\]

A source label

\[
(k;\ell_1,\ldots,\ell_5;a^ib^j)
\]

maps to

\[
-(k;\ell_1,\ldots,\ell_5;c^ja^i),
\]

where the pole levels are retained positionally in the ordered labelled map
above.

The exact audit gives

\[
\dim Q_{12}=\dim Q_{31}=21,
\]

\[
\operatorname{rank}T_{12\to31}
=
\operatorname{rank}T_{31\to12}
=21.
\]

All \(6317\) retained source pivot relations reduce to zero in the target
presentation:

\[
\boxed{
T_{12\to31}(\operatorname{im}d_{12})
\subseteq
\operatorname{im}d_{31}.
}
\]

The two signed transports satisfy

\[
\boxed{
T_{31\to12}T_{12\to31}=1
}
\]

on every retained quotient basis vector.

The physical numerator also transports with the labelled partner change:

\[
q_{g_{23}}+q_{g_{31}}
\longmapsto
q_{g_{23}}+q_{g_{12}}.
\]

## Narrow result

The \(G_{12}\) and \(G_{31}\) residue presentations are related by a
canonical labelled, orientation-sensitive isomorphism. Occurrence reflection
does not act inside one fixed residue chart; it exchanges charts and carries
an unavoidable residue sign.

Thus any cyclic or deck-equivariant global extension calculation must use
these inter-chart maps before comparing connection blocks. A parameter swap
inside the fixed \(G_{12}\) reducer is not the required comparison.

This constructs one edge of the residue-chart descent datum. It does not yet
prove the three-chart cocycle condition or Gauss--Manin horizontality.

## Evidence

- `research/benincasa/g12_g31_residue_chart_transition.py`;
- `research/benincasa/g12-g31-residue-chart-transition.json`;
- Entry 753;
- allocator claim `seqclaim-bf2d39144486b7378ae7e691`;
- epistemic event `ev-000000000370-d494e518-4aba-4155-8ba6-2435ac22fd99`.

## Next falsifier

Construct the other two labelled residue-chart transitions with the same
ambient residue convention, then test the signed three-chart composition.
After that, test connection intertwining under the corresponding permutation
of kinematic derivatives. A nontrivial cocycle or failed intertwiner would
localize the missing descent datum rather than permit a fitted gauge.
