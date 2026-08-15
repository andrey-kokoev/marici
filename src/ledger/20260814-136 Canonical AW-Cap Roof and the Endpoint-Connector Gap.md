# Canonical AW-Cap Roof and the Endpoint-Connector Gap

## Record

Date: 2026-08-14

Status: proved at carrier level. The canonical integral \(D_3\)-equivariant
AW/cap roof exists and is independent of the front/back convention. It does
not select a direct full-cone lift; the endpoint-compatible butterfly
connector remains open.

Entry 135 proved that the minimal strict projection is obstructed modulo
three while the full augmented cone has an affine rank-nine lattice of
integral lifts. The question was whether relative Alexander--Whitney
geometry selects one of those nine parameters. The exact answer is no. It
canonically selects the derived roof common to every lift.

## Claim

Let

\[
U=\operatorname{Cone}\!\left(
C_*(v_+)\longrightarrow C_*(B_{\rm short})
\right),
\qquad
T=\operatorname{Cone}\!\left(
P_{\rm road}\xrightarrow{\epsilon}\mathbb Z
\right).
\]

Define

\[
C_{\rm tag}=
\left[
\mathbb Z_{\rm or}\langle\omega\rangle
\xrightarrow{N}
P_{\rm tag}
\right],
\qquad
N\omega=e_{14}+e_{03}+e_{25}.
\]

There is a canonical integral \(D_3\)-equivariant roof

\[
\boxed{
\mathcal R_{\rm AD}^{\rm car}:
\quad
U\xleftarrow[\sim]{\,g_{\rm cap}\,}
C_{\rm tag}
\xrightarrow{\,m\,}
T
}
\]

with

\[
g_2(\omega)=-S,\qquad
g_1(e_i)=c_i=\partial F_i,\qquad
m_1=M_{\rm AD}=R-R^2,\qquad
m_2=m_0=0,
\]

where \(S\) is the oriented sum of the six short facets. Both legs induce
the saturated complementary-boundary Alexander isomorphism on \(H_1\).
This roof is the canonical AW/cap output. It is not a canonical strict map
\(U\to T\).

## Exact AW/cap census

The labelled barycentric boundary of \(K_6\) has an oriented fundamental
cycle with 84 flag triangles. For each long facet \(F_i\):

- the positive-normalized front cap is a closed 8-edge cycle equal to the
  subdivision of the oriented boundary \(c_i\);
- the back cap is a second closed 8-edge dual loop;
- a 16-triangle collar \(H_i\) satisfies

  \[
  \partial H_i=z_i^{\rm back}-z_i^{\rm front}.
  \]

Rotation cycles the three packets. Reflection sends each packet to minus
the correspondingly reflected packet. Consequently

\[
g_{\rm back}-g_{\rm front}=dH+Hd
\]

strictly and \(D_3\)-equivariantly. Changing the AW convention changes only
the representative of one roof; it cannot toggle the unresolved
reflection parity.

The left leg is integrally saturated. The matrix
\([d_{B,2}\mid c_{14}\mid c_{03}]\) has an explicit \(8\times8\)
minor of determinant \(-1\), and the third cycle has only the norm
relation. Thus

\[
H_1(C_{\rm tag})=\operatorname{coker}N
\xrightarrow{\sim}H_1(U)
\]

integrally. On the right,
\(M_{\rm AD}N=0\), \(\epsilon M_{\rm AD}=0\), and the induced
\(A_2\)-matrix has determinant \(+1\).

## Non-selection theorem

For every solution \(F:U\to T\) of entry 135's frozen full-cone system, the
nine peripheral equations are exactly

\[
\boxed{F\,g_{\rm cap}=m.}
\]

The coefficient rank remains 71 in 80 variables, so the solution space
remains affine rank nine. Every full-cone lift factors the same canonical
roof and AW/cap fixes none of the remaining affine parameters.

The next object is therefore not a preferred matrix in the rank-nine
family. It is an endpoint-coherent pointing of the roof in the
arrow/two-extension category.

## Sharp blocker

To turn \(\mathcal R_{\rm AD}^{\rm car}\) into a pointed butterfly one
needs a \(D_3\)-equivariant contraction, or equivalent connector 2-cells,
for the acyclic complement of \(g_{\rm cap}\), compatible with the endpoint
maps in \(U\) and \(T\). Relative AW/cap supplies the cap-direction map but
not such an inverse or connector.

A strict endpoint-identity inverse would impose \(F_0(v_+)=1\), while the
exact full-cone equations force \(F_0(v_+)=3k\). The endpoint identity must
therefore be carried by butterfly/homotopy data rather than a strict
degree-zero component.

This entry does not prove that every additional geometric SDR algorithm is
impossible. It proves only that the canonical AW roof, including its
front/back homotopy, does not choose one. Until an endpoint-compatible
connector is constructed, no canonical direct representative or
reflection parity is defined.

## Formula objective

The immediate objective is

\[
\boxed{
\widehat{\mathcal R}_{\rm AD}^{\rm car}
\in
\operatorname{Lift}_{\operatorname{Arr}^2_{D_3}}
\left(
\mathcal R_{\rm AD}^{\rm car};
\mathbb E_F,\mathbb E_\triangle
\right).
}
\]

Equivalently, construct a pointed butterfly whose underlying roof is the
proved \(\mathcal R_{\rm AD}^{\rm car}\), with endpoint identities and both
connector coherences explicit. Only after this pointing exists should one
compute its mod-two reflection class and attempt the loaded extraordinary
lift toward \(d_{\rm sp,sc}\) and \(G_{03}^{\rm Cousin}\).

## Evidence

Exact certificate:

- research/voevodsky/check_k6_strict_ad_chain_map.rs
- SHA-256
  02b2a4691719501aee5d3535a209dbe131534c67048d05ada55d6ff062ed521c

Verification:

~~~text
rustfmt --edition 2021 --check
rustc --edition 2021 -D warnings -O
executable exit 0
JSON output parses
git diff --check
~~~

## Outcome contract

~~~json
{
  "claim": "The labelled relative barycentric AW/cap construction canonically gives a saturated integral D3-equivariant roof U<-C_tag->T with right leg M_AD=R-R^2. Front and back representatives are D3-equivariantly homotopic. Every integral full-cone lift factors this roof, so the roof does not select a point in the affine rank-nine lift lattice.",
  "status": "proved",
  "assumptions": [
    "The K6 incidence signs, ambient orientation, and D3 actions are those reconstructed from the labelled face poset.",
    "The physical road order is F14, F03, F25 and M_AD=R-R^2.",
    "The entry-135 full-cone equations and their frozen peripheral values are retained integrally.",
    "No rational splitting or endpoint-unit normalization is imposed."
  ],
  "evidence_refs": [
    "research/voevodsky/check_k6_strict_ad_chain_map.rs",
    "src/ledger/20260814-135 Strict Alexander Projection No-Go and the Integral Butterfly Objective.md",
    "src/ledger/20260814-115 Boundary-Triad Tate Realization and the Multi-Rees Cartier Bicomplex.md"
  ],
  "factorization_test": {
    "barycentric_fundamental_cycle": "84 oriented flag triangles",
    "front_caps": "three closed 8-edge cycles equal to subdivided oriented long-facet boundaries",
    "back_caps": "three closed 8-edge B-side dual loops",
    "front_back_homotopy": "three 16-triangle collars with boundary back-front",
    "D3_covariance": "rotation-covariant and reflection-odd for front, back, collars, and top chains",
    "left_leg": "g_cap is an integral saturated quasi-isomorphism; explicit determinant -1 minor",
    "right_leg": "m1=M_AD; mN=0; epsilon*m=0; induced A2 determinant +1",
    "canonical_roof": "proved",
    "full_cone_factorization": "all nine frozen peripheral equations are exactly F*g_cap=m",
    "full_cone_dimension": "affine rank 9 remains unchanged",
    "canonical_direct_point": "not selected",
    "reflection_parity": "undefined"
  },
  "counterevidence": [
    "All nine full-cone affine directions factor the same roof, so AW/cap cannot distinguish them.",
    "Front and back caps are explicitly D3-chain-homotopic, so convention reversal does not select or toggle a point.",
    "A strict endpoint-identity inverse would require 3k=1.",
    "No exhaustive no-go is claimed for additional geometric SDR or connector constructions."
  ],
  "sharp_blocker": "Construct endpoint-compatible D3 connector 2-cells, or an equivalent pointed butterfly, over the canonical AW roof.",
  "next_experiment": "Build the endpoint-compatible lift of the canonical roof in the arrow/two-extension category, compute its reflection class, and only then load that same pointed object with occurrence, multi-Rees, reciprocal/BM, and PC/Cousin data."
}
~~~
