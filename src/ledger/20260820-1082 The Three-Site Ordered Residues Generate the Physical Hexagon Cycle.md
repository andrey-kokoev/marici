# 1082 — The Three-Site Ordered Residues Generate the Physical Hexagon Cycle

## Question

Entry 1081 derived a canonical physical normal link

\[
\operatorname{Lk}_{\rm phys}=C_6
\]

from the six denominator terms in equation (51) of arXiv:2408.16386v2.
Topology alone did not determine whether the source coefficients cancel or
generate its one-dimensional \(H_1\).

The finite test is to derive the Poincaré-residue orientation of every source
pair in the fixed loop-coordinate orientation

\[
dy_{12}\wedge dy_{23}\wedge dy_{31}.
\]

## Source-linear normals

For a deletion pole \(q_{\mathcal G_{ij}}\), its normal is the corresponding
coordinate direction \(dy_{ij}\), up to a positive normalization that does not
affect orientation. For the connected two-site pole
\(q_{\mathfrak g_{jk}}\), equation (9) gives the sum of the two edge directions
departing from that subgraph. The remaining coordinate is the edge internal to
\(\mathfrak g_{jk}\).

Thus each source term has a canonically ordered local frame

\[
(dq_{\mathcal G_{ij}},dq_{\mathfrak g_{jk}},dy_{jk}).
\]

Taking its determinant relative to
\((dy_{12},dy_{23},dy_{31})\) gives, in the order printed in equation (51),

\[
\boxed{(-,+,-,+,-,+).}
\]

## Transport to the oriented link

Use the oriented hexagon

\[
q_{\mathcal G_{12}}
\to q_{\mathfrak g_{23}}
\to q_{\mathcal G_{31}}
\to q_{\mathfrak g_{12}}
\to q_{\mathcal G_{23}}
\to q_{\mathfrak g_{31}}
\to q_{\mathcal G_{12}}.
\]

Three source pairs are printed in the opposite order to this orientation.
Poincaré residues are antisymmetric under exchanging the two normals, so those
three coefficients change sign. In the oriented edge basis the coefficient
vector is therefore

\[
\boxed{(-1,-1,-1,-1,-1,-1).}
\]

At every vertex the incoming and outgoing coefficients agree. Hence

\[
\partial_1 c_{\rm src}=0.
\]

Since \(C_6\) has no two-cells and \(c_{\rm src}\neq0\),

\[
[c_{\rm src}]\neq0\in H_1(C_6;\mathbb Q).
\]

## Narrow result

\[
\boxed{
\text{The source three-site integrand canonically generates the fundamental
physical residue-link cycle.}
}
\]

This is stronger than Entry 1081's carrier statement: the coefficients and
ordered-residue orientations select the nonzero class without fitting.

It remains an integrand-level statement. It does not yet prove that the
Bunch--Davies relative integration chain pairs nontrivially with this class, or
that the resulting integrated observable contains an additional period.

## Implication for H2

The class requires no new carrier cell. It is assembled from

\[
\text{existing connected-subgraph incidence}
\quad+\quad
\text{Poincaré-residue orientation}
\quad+\quad
\text{sector-specific coefficient weights}.
\]

This is direct support for the shared-carrier/shared-calculus part of H2.

## Next falsifier

Construct the restriction of the source Cayley--Menger relative chain to the
six physical pairwise residue strata and evaluate its pairing with
\(c_{\rm src}\). Preserve the six labels, contour orientations, and any deck
character.

The acceptable outcomes are:

- nonzero lift-independent pairing: physical activation;
- zero pairing: integrand cycle physically invisible;
- no source-defined relative-chain restriction: activation remains undefined.

## Durable checker

- `research/benincasa/check_three_site_physical_residue_link.rs`
- `research/benincasa/three-site-physical-residue-link.json`

