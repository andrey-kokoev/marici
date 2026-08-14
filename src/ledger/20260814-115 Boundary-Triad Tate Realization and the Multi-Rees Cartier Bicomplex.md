# Boundary-Triad Tate Realization and the Multi-Rees Cartier Bicomplex

## Record

Date: 2026-08-14

Status: one proved integral carrier theorem, one proved coefficient theorem,
and one sharp loaded blocker. The actual boundary triad of the six-point
associahedron derives the complete Tate window and makes the carrier
\(\mathbb Z/3\) obstruction vanish. The filtered multi-Rees Cartier
Bockstein supplies the missing conormal-valued \(H_0\)-to-
\(\operatorname{Tor}_1\) direction. These two canonical differentials form
a bicomplex; a direct \(\lambda_{\rm ex}\) is only its transferred shadow.
The remaining gap is the spatial extraordinary-costalk comparison that
identifies this bicomplex with the actual loaded gallery/road complexes.

## The actual boundary triad

Let

\[
X=K_6,\qquad B=B_{\rm short},\qquad
L=F_{14}\sqcup F_{03}\sqcup F_{25}.
\]

Here \(X\) is an oriented three-ball, the three long facets are disjoint
closed squares, and

\[
\partial X=B\cup L,
\qquad
B\cap L=\partial L.
\]

Thus \(B\) is a sphere with three open disks removed. The genuine relative
\(Q=F_2/F_1\) carrier is

\[
C_*(X,B):
\qquad
0\longrightarrow
\mathbb Z_{\rm or}\langle[X]\rangle
\xrightarrow{N}
P_{\rm tag}\langle F_{14},F_{03},F_{25}\rangle
\longrightarrow0,
\]

with

\[
d[X]=F_{14}+F_{03}+F_{25}.
\]

This is an actual generic \(Q\)-leg. Neither term factors through the short
boundary complex \(F_1\).

The filtration connecting morphism is the saturated integral isomorphism

\[
\partial_F:
H_2(X,B)\xrightarrow{\sim}H_1(B,v_+).
\]

Complementary-boundary Poincare--Lefschetz duality gives

\[
\operatorname{AD}_{(X;B,L)}:
H_1(B,v_+)
\xrightarrow{\sim}
\widetilde H_0(L)
=\ker(\epsilon:P_{\rm road}\to\mathbb Z).
\]

Consequently the middle map is not classified and then inserted. It is the
geometric composite

\[
\boxed{
m:
P_{\rm tag}	woheadrightarrow H_2(X,B)
\xrightarrow{\partial_F}H_1(B,v_+)
\xrightarrow{\operatorname{AD}}
\widetilde H_0(L)
\hookrightarrow P_{\rm road}.
}
\]

With the established cyclic facet order and positive normal orientation,

\[
m(F_i)=[L_i]-[L_{i+1}],
\]

and hence

\[
\boxed{m=1-r.}
\]

The actual CW triad therefore produces the complete integral resolution

\[
\boxed{
0\longrightarrow\mathbb Z_{\rm or}
\xrightarrow N P_{\rm tag}
\xrightarrow{1-r}P_{\rm road}
\xrightarrow\epsilon\mathbb Z
\longrightarrow0.
}
\]

No rational projector, \(1/3\), chosen splitting, fitted road coefficient,
or new carrier cell occurs.

## The carrier obstruction is zero

Let \(e_F\) be the two-extension of the actual support filtration and let
\(\beta_\triangle\) be the based Tate class. The carrier realization formed
from the relative \(Q\)-complex, the connector \(\partial_F\), and the
complementary-boundary cap product sends

\[
\rho_{\rm PL}^{\rm car}(e_F)=\beta_\triangle.
\]

Therefore the obstruction left open in entry 114 now vanishes at the
integral carrier level:

\[
\boxed{
\omega_{\rm car}
=\rho_{\rm PL}^{\rm car}(e_F)-\beta_\triangle
=0
\in
\operatorname{Ext}^2_{\mathbb Z[D_3]}
(\mathbb Z,\mathbb Z_{\rm or})
\simeq\mathbb Z/3.
}
\]

The generic road norm remains

\[
q_\Sigma=N_{\rm road},
\qquad
\epsilon(q_\Sigma)=3.
\]

It is not killed and is not identified with the reflection-odd tag norm.

Equality of the two carrier extensions does not choose a unique equivariant
chain homotopy between them. Such coherent identifications form a torsor
under

\[
\operatorname{Ext}^1_{\mathbb Z[D_3]}
(\mathbb Z,\mathbb Z_{\rm or})
\simeq\mathbb Z/2.
\]

An explicit equivariant dual-cell diagonal/cap model must select this parity.

## The filtered Cartier Bockstein

Entry 114 was also too negative about the coefficient off-diagonal. It is
true that the derived Cartier fibre is split after forgetting its filtration,
but the filtered multi-Rees packet has a canonical Bockstein.

For one labelled normal, let

\[
A_i=\mathbb Z[t_i,x_i,(1+t_ix_i)^{-1}],
\qquad
P_i=[A_i h_i\xrightarrow{t_ix_i}A_i p_i].
\]

On the \(x_i\)-Cartier fibre \(C_i=A_i/(x_i)\),

\[
P_i\otimes_{A_i}C_i
=[C_i h_i\xrightarrow0C_i p_i].
\]

The first filtered connecting morphism is nevertheless nonzero:

\[
\beta_{x_i}([h_i])=t_i[p_i].
\]

After Verdier duality it has the required direction and first Rees symbol

\[
\boxed{
\beta_{x_i}^{\vee}:H_0\longrightarrow\operatorname{Tor}_1,
\qquad
\operatorname{gr}_{t_i}^1\beta_{x_i}^{\vee}
=[t_i]\epsilon_i.
}
\]

The conormal factor \([t_i]\) is part of the canonical symbol. Removing it
requires an oriented Gysin evaluation; simply writing \(\epsilon_i\) would
silently trivialize the Rees normal.

For the independent three-normal multi-Rees graph

\[
q_i-1=t_ix_i,
\qquad i\in\{1,3,5\},
\]

the central derived fibre is the exterior packet of ranks

\[
(1,3,3,1).
\]

On its Verdier dual the mixed operator is

\[
\boxed{
b^\vee
=\sum_{i\in\{1,3,5\}}[t_i]\epsilon_i\wedge(-),
\qquad
(b^\vee)^2=0.
}
\]

It is \(D_3\)-equivariant; reflection is carried by the determinant
orientation. No \(x_i\), \(u_i\), \(t_i\), or integer is inverted.

## The correct object is a bicomplex

Let

\[
C_{\rm PL}^{\rm Tate}
=
[\mathbb Z_{\rm or}\xrightarrow N P_{\rm tag}
\xrightarrow{1-r}P_{\rm road}\xrightarrow\epsilon\mathbb Z]
\]

be the boundary-triad complex, and let
\(\Lambda^\bullet N_{\rm Cart}^{\vee}\) denote the three-normal Cartier
exterior packet. The canonical coefficient/carrier object is

\[
\boxed{
\mathcal T_+^{\rm mR}
=\operatorname{Tot}
\left(
C_{\rm PL}^{\rm Tate}
\otimes
\Lambda^\bullet N_{\rm Cart}^{\vee}
\right),
\qquad
d_{\mathcal T}
=d_{\rm PL}+(-1)^{p}b^\vee.
}
\]

The oriented normalization/conductor differential supplies
\(N,1-r,\epsilon\) in every Cartier degree. The filtered Bockstein supplies
the vertical direction. Equivariance gives commutation before totalization,
and the Koszul sign gives

\[
d_{\mathcal T}^2=0.
\]

Thus a direct arrow

\[
\lambda_{\rm ex}:P_{H_0}\dashrightarrow P_{\operatorname{Tor}_1}
\]

is not primitive data. It is a transferred or collapsed shadow of this
bicomplex. Keeping the bicomplex avoids both a fitted \(1-r\) and a fitted
Cartier extension.

## The remaining loaded obstruction

The bicomplex above is canonical at the product of two established levels:
the actual integral PL carrier and the regular multi-Rees coefficient
packet. It is not yet an occurrence-resolved PC correspondence.

Indeed,

\[
V(t_1x_1,t_3x_3,t_5x_5)
\]

has eight irreducible coordinate components. The positive scalar branch
\(V(x_1,x_3,x_5)\) is only one of them. A relative-support or nearby-cycle
functor must select that branch while retaining the three \([t_i]\) normal
lines. It must then identify:

- the triple stratum with the actual loaded \(F_0\) packet;
- the three pair strata with the three whole Cartier galleries;
- the PL road components with the actual reciprocal/Borel--Moore
  \(\operatorname{Tor}_1\) costalks;
- the resulting map with the mixed block
  \(dH_\Sigma=q_\Sigma-\sum_i x_i\widetilde\xi_i\) and the Yoneda cone roof.

The first nontrivial column is now completely specified. For \(D03\), a
valid marked extraordinary-costalk map must derive

\[
\boxed{
-[n_{03}]
\longmapsto
[t_3](-\tau_{q_0}+\tau_{q_2}),
}
\]

where both adjacent-road terms arise from actual generizations and the
associated-grade costalk agrees with the established positive whole-gallery
normalization. Naming the two terms or inserting the column of \(1-r\) is
not a construction.

Consequently:

- \(\omega_{\rm car}=0\) is proved, but a loaded \(\omega^{!,\rm PC}\) is
  not yet typed;
- the filtered coefficient off-diagonal exists, but its spatial
  extraordinary pull--push does not;
- the residual \(\mathbb Z/2\) parity can be tested only after that loaded
  comparison exists;
- no negative-sheet assembly, physical-Cut theorem, full
  \(G_{03}^{\rm Cousin}\), or CHY identification follows yet.

## Evidence

New exact certificate:

- `research/voevodsky/check_multirees_cartier_pl_cap.rs`, SHA-256
  `3389c61357f1ac14503569dac448a15ac89efc294e8ec20e42d9ba118ba5db5e`.

The checker verifies the boundary-triad matrices and homology, the saturated
Poincare--Lefschetz middle map \(1-r\), the exact Tate window,
\(\omega_{\rm car}=0\), the \(\mathbb Z/2\) parity group, the one- and
three-normal Cartier Bocksteins, \((b^\vee)^2=0\), \(D_3\) covariance, the
totalization signs, and the eight-component support warning. It explicitly
does not construct the spatial PC comparison.

Reproduce with `rustfmt --check`,
`rustc --edition 2021 -D warnings -O`, execution of the certificate, JSON
parsing, and `git diff --check`.

## Outcome contract

```json
{
  "claim": "The actual boundary triad (K6; B_short, three long facets) canonically realizes the integral N/(1-r)/epsilon Tate window and makes the carrier Yoneda obstruction zero. Independently, the filtered multi-Rees Cartier Bockstein canonically supplies the conormal-valued H0-to-Tor1 direction. Their correct joint object is a bicomplex, not an inserted direct off-diagonal.",
  "status": "conditional",
  "assumptions": [
    "Carrier orientations and D3 labels are those fixed in entries 103 and 112.",
    "The multi-Rees parameters remain independent and their conormal lines are retained.",
    "The theorem is not promoted to the loaded PC category without an explicit relative-support extraordinary correspondence."
  ],
  "evidence_refs": [
    "research/voevodsky/check_multirees_cartier_pl_cap.rs",
    "ledger entries 100, 103-105, 112-114"
  ],
  "factorization_test": {
    "actual_Q_leg": "proved at carrier level",
    "PL_middle_map": "proved equal to 1-r",
    "omega_carrier": "zero in Z/3",
    "parity_torsor": "Z/2, unselected",
    "Cartier_Bockstein": "proved with first symbol [t_i] epsilon_i",
    "bicomplex_d_squared": "zero",
    "support_components": "eight; the positive x-side requires extraordinary selection",
    "D03_loaded_column": "unconstructed",
    "full_G03_Cousin": "unconstructed"
  },
  "counterevidence": [
    "Forgetting the filtration leaves split Cartier packets with zero direct differential.",
    "The carrier cap does not identify the actual gallery Tor1 lines with PL road cells.",
    "The multi-Rees graph alone does not select the positive support component or provide the Q/Yoneda pull-push."
  ],
  "next_experiment": "Construct the positive relative-support multi-DNC exit correspondence and prove the D03 column -[n03] -> [t3](-tau_q0+tau_q2), including reciprocal/BM variance, excess trace, physical normal, H_Sigma, and Yoneda compatibility."
}
```
