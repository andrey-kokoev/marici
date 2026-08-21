---
author: marici.Nima
---

# 1509 — Site-Energy Decay Is Valence Plus One at Every Loop Order

## Status

General proof extending Entry 1500 from trees to finite conformal scalar graphs
at arbitrary loop order. Entry 1507 supplies an exhaustive small-graph audit.

## Source recursion

The time-translation identity of Arkani-Hamed, Benincasa, and Postnikov,
arXiv:1709.02813, Eq. (2.41), has the schematic form

\[
\left(\sum_{u\in V}x_u\right)I_G
=2\sum_{e\in E}I_{G\setminus e}^{\rm shifted}.
\]

Deleting \(e=(a,b)\) shifts the endpoint energies by \(y_e\). If deletion
disconnects the graph, the right-hand object is the product of the two
component integrands. If it does not, it is the corresponding lower-loop
integrand. The identity is therefore an induction on edge count valid on both
sides of the tree/loop boundary.

## Induction

Fix a vertex \(v\) of valence \(d\), and assume the result for graphs with
fewer edges.

If \(e\) is incident to \(v\), then

\[
\deg_{G\setminus e}(v)=d-1.
\]

The induction hypothesis gives

\[
I_{G\setminus e}^{\rm shifted}
=\Theta(x_v^{-d}),
\]

because the finite endpoint shift \(x_v\mapsto x_v+y_e\) does not change the
large-\(x_v\) exponent.

If \(e\) is not incident to \(v\), its deletion leaves the valence equal to
\(d\), so that term is

\[
O(x_v^{-d-1}).
\]

Finally,

\[
\left(\sum_ux_u\right)^{-1}=O(x_v^{-1}).
\]

Hence incident-edge terms contribute at order \(x_v^{-d-1}\), while
nonincident-edge terms begin one order later.

In the positive-energy chamber the recursion has a common positive
orientation and the lower-edge integrands are positive. The leading
incident-edge coefficients therefore cannot cancel. The edgeless base case is
\(I_{\{v\}}=1/x_v\).

Thus, by induction on \(|E|\),

\[
\boxed{
I_G(x_v)=\Theta\!\left(x_v^{-\deg_G(v)-1}\right)
}
\]

for every finite source graph in this calculus, including multiedges but
excluding undeclared self-loop conventions.

## Consequences

1. Loop order does not enter the exponent.
2. Global topology affects finite poles and coefficients, but site infinity
   sees only the local incidence star.
3. A sector weight \(x_v^m\) produces no infinity boundary whenever

   \[
   m<\deg_G(v).
   \]

   The borderline \(m=\deg_G(v)\) gives a possible logarithmic boundary, and
   larger weights require explicit subtraction or relative support.
4. The de Sitter mass insertion has \(d=2,m=1\), so its Kummer pushforward is
   canonically convergent at infinity at every loop order.

## Architectural meaning

This is a universal carrier law rather than a cosmology-only coefficient
fact:

\[
\boxed{
\text{local incidence star}
\longmapsto
\text{projective decay exponent }\deg(v)+1.
}
\]

Sector-specific weights then decide whether infinity is silent, logarithmic,
or requires a supported boundary object.

## Durable evidence

- Arkani-Hamed, Benincasa, and Postnikov, arXiv:1709.02813, Eqs. (2.37)–(2.41);
- `research/nima/check_loop_site_valence_falloff.sage`;
- `research/nima/check_lollipop_trivalent_loop_falloff.sage`;
- `research/nima/check_all_small_graph_site_falloff.sage`;
- allocator claim `seqclaim-5015358d6cb0021a31a3220b`.
