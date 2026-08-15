# Minimal Alexander Projection No-Go and the Integral Full-Cone Lift

## Record

Date: 2026-08-14

Status: proved dichotomy. The strict minimal projection is falsified, while
unframed integral full-cone lifts exist; their canonical AW/cap pointing
remains open.

Entry 134 correctly retyped the scalar off-diagonal as a path between two
fixed two-extensions. Entry 135 now separates three statements that must not
be conflated: the Alexander map has no strict representative on the minimal
edge-only quotient, it does have integral representatives on the full
augmented cone, and an additional endpoint-unit framing is obstructed by
index three. The remaining problem is canonical geometric pointing, not
bare existence.

## Claim

Let

\[
P_\partial=C_*(B_{\rm short})/C_*(v_+)
\]

for the actual labelled \(K_6\) associahedron, and let

\[
K=\ker\!\left(
\epsilon:P_{\rm road}=\mathbb Z\langle q_0,q_1,q_2\rangle
\longrightarrow\mathbb Z
\right).
\]

The relative cellular complex has ranks

\[
\operatorname{rank}(P_2,P_1,P_0)=(6,21,13),
\]

differential ranks

\[
\operatorname{rank}d_2=6,\qquad
\operatorname{rank}d_1=13,
\]

and therefore \(H_1(P_\partial)\simeq\mathbb Z^2\).

Complementary-boundary Alexander duality and the first support
transgression still give the saturated integral isomorphism

\[
H_1(P_\partial)\xrightarrow{\sim}K.
\]

However, there is no integral strict \(D_3\)-equivariant chain map

\[
\boxed{
a_{\rm AD}^{\rm str}:P_\partial\longrightarrow K[1]
}
\]

which induces that fixed isomorphism. This is a strictification obstruction,
not a failure of homological Alexander duality.

In the physical road order \((F_{14},F_{03},F_{25})\), write

\[
R=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix},
\qquad
M_{\rm AD}=R-R^2
=\begin{pmatrix}0&-1&1\\1&0&-1\\-1&1&0\end{pmatrix}.
\]

The matrix used in the first version of the checker is not a competing
physical convention. If \(J\) reverses the three coordinates and
\(\bar q=-Jq\), then

\[
M_1=-J M_{\rm AD}=M_{\rm AD}J.
\]

The checker derives this unimodular basis dictionary and reproduces the
same obstruction in both bases. It also verifies the entry-115 relation
\((1-R)R=M_{\rm AD}\).

## Evidence

A strict map is a \(3\times21\) matrix \(F\). The exact checker imposes only:

- the chain equation \(F d_2=0\);
- the condition \((1,1,1)F=0\), so the image lies in \(K\);
- strict rotation and reflection covariance;
- the independently established peripheral values

  \[
  F(c_{14},c_{03},c_{25})
  =
  \begin{pmatrix}
  1&-1&0\\
  -1&0&1\\
  0&1&-1
  \end{pmatrix}.
  \]

These give 174 integral equations in 63 variables.

Over \(\mathbb Q\), the coefficient and augmented matrices both have rank
59, so the solution space is an affine four-plane. Modulo \(3\), their
ranks are instead

\[
\operatorname{rank}_{\mathbb F_3}A=58,\qquad
\operatorname{rank}_{\mathbb F_3}[A|b]=59.
\]

The checker includes a fixed 32-row linear combination whose left side is
zero and whose right side is one in \(\mathbb F_3\). Hence the integral
solution set is empty, while rational solutions necessarily use thirds.

The full augmented problem behaves differently. Put

\[
U=\operatorname{Cone}(C(v_+)\to C(B_{\rm short})),
\qquad
T=\operatorname{Cone}(P_{\rm road}\xrightarrow\epsilon\mathbb Z).
\]

The frozen full-cone chain-map system has 209 equations in 80 variables.
Its coefficient and augmented matrices both have rank 71. Hence its
solution space has affine rank nine, and the checker supplies an explicit
integral solution with \(\ell=-1\),

\[
F_0(v_+)=0,\qquad F_0(v_-)=-1.
\]

More generally its endpoint values obey

\[
F_0(v_+)=3k,\qquad
F_0(v_-)-F_0(v_+)=2+3\ell.
\]

Thus unframed full-cone lifts exist integrally. Only the extra normalization
\(F_0(v_+)=1\) gives the simpler obstruction \(3k=1\). That equation is an
endpoint-unit framing ablation, not a no-go for full-cone maps.

Exact certificate:

- research/voevodsky/check_k6_strict_ad_chain_map.rs
- SHA-256
  ae82b2b84591b18c510e9b0ad4bab7a74d52ece043c979715f31769c7a11f723

Verification:

~~~text
rustfmt --edition 2021 --check
rustc --edition 2021 -D warnings -O
executable exit 0
JSON output parses with status=falsified
git diff --check
~~~

## Boundary

The result does not falsify:

- the integral homology isomorphism
  \(H_1(B_{\rm short},v_+)\simeq\ker\epsilon\);
- entry 134's formal lift-space theorem;
- an integral full-cone chain map: such maps are now explicitly proved to
  exist;
- a derived Alexander morphism represented by a roof;
- an integral butterfly between the two augmented two-extensions;
- a strict map on a canonically enlarged barycentric or dual-cell
  resolution.

It does falsify replacing the derived comparison by a direct projection
from the minimal cellular quotient to its \(A_2\) homology module. Neither a
front/back Alexander--Whitney convention nor an ordinary chain homotopy can
remove the mod-three inconsistency. Inverting \(3\) would erase the exact
integral extension that the construction is meant to retain.

It also falsifies the stronger endpoint-unit framing
\(F_0(v_+)=1\). It does not select one of the rank-nine unframed lifts,
identify an AW/cap representative, or determine the reflection parity.

The no-go also narrows entry 115: its \(1-r\) statement is an exact
homology/derived-carrier result, not an already constructed strict cellular
Alexander projection.

## Consequence

The next task is no longer to prove that some integral augmented lift
exists. It is to derive a distinguished point

\[
\boxed{
a_{\rm AD}^{\rm AW}
\in
\operatorname{Lift}^{\mathbb Z}_{D_3}
(U,T;M_{\rm AD})
}
\]

from the relative barycentric AW diagonal and PL cap, and to compare that
point with the frozen Tate two-extension. Equivalently, package the same
data as a pointed butterfly between

\[
0\to C(v_+)\to C(B_{\rm short})\to P_\partial\to0
\]

together with the second support extension, and

\[
0\to\mathbb Z_{\rm or}\xrightarrow N P_{\rm tag}
\xrightarrow{1-r}P_{\rm road}\xrightarrow\epsilon\mathbb Z\to0.
\]

The pointing and both connector coherences must be forced by the relative
barycentric AW/cap geometry. Choosing an arbitrary member of the rank-nine
affine lattice, or imposing the desired \(1-r\) shadow, would fit the answer.

The carrier objective is now

\[
\boxed{
\mathcal B_{\rm AD}^{\rm car}
\in
\operatorname{Butterfly}_{D_3}
(\mathbb E_F,\mathbb E_\triangle),
\qquad
\ell_{\rm car}
\in
\operatorname{Path}
(\rho_{\mathcal B}(e_F),\beta_\triangle).
}
\]

The butterfly must retain endpoint identities and both cone-connector
coherences. Only after that structure is explicit is its mod-two reflection
parity defined.

The loaded objective is the same butterfly with occurrence lines,
independent multi-Rees conormals, reciprocal/Borel--Moore variance, and
PC/Cousin maps. It must be constructed before evaluating
\(K_{\rm alt}\), \(q_\Sigma\), or the entry-131 residue.

## Outcome contract

~~~json
{
  "claim": "For the actual labelled K6 system, the minimal edge-only D3-equivariant projection to ker(epsilon)[1] is obstructed modulo 3, while the full augmented cone admits an integral affine rank-nine family of lifts with the same frozen peripheral data.",
  "status": "falsified",
  "assumptions": [
    "The K6 incidence signs and D3 actions are those reconstructed from the labelled face poset and fixed ambient orientation.",
    "The road order is F14, F03, F25 and the required H1 map is the independently established saturated inverse transgression.",
    "D3 covariance is strict over Z and 3 is not inverted.",
    "The endpoint-unit condition F0(v+)=1 is an ablation, not part of the unframed full-cone system."
  ],
  "evidence_refs": [
    "research/voevodsky/check_k6_strict_ad_chain_map.rs",
    "src/ledger/20260814-134 Framed Lift-Space Theorem and the Relative AW Reference-Lift Gap.md",
    "src/ledger/20260814-115 Boundary-Triad Tate Realization and the Multi-Rees Cartier Bicomplex.md"
  ],
  "factorization_test": {
    "cellular_ranks": "6/21/13 with H1=Z^2",
    "strict_system": "174 equations in 63 variables",
    "rational_result": "consistent, rank 59, affine dimension 4",
    "mod3_result": "coefficient rank 58, augmented rank 59",
    "explicit_falsifier": "32 equations sum to 0=1 over F3",
    "strict_integral_map": "empty",
    "physical_basis": "M_AD=R-R^2; the old M1 is its signed reversed-basis form -J M_AD=M_AD J",
    "full_cone_system": "209 equations in 80 variables; coefficient and augmented ranks 71",
    "full_cone_integral_lifts": "nonempty affine lattice of rank 9; explicit ell=-1 lift has F0(v+)=0 and F0(v-)=-1",
    "endpoint_formula": "F0(v+)=3k and F0(v-)-F0(v+)=2+3ell",
    "endpoint_unit_framing": "falsified by 3k=1",
    "canonical_AW_point": "unconstructed",
    "reflection_parity": "undefined until a geometric point is selected"
  },
  "counterevidence": [
    "The rational system is nonempty, so the failure is 3-primary rather than a rank obstruction.",
    "The full-cone system is integrally nonempty, so the minimal no-go cannot be promoted to a blanket chain-level no-go.",
    "The full augmented Tate sequence is integral and must not be replaced by a 1/3 splitting.",
    "Existence of nine affine parameters does not provide a canonical AW/cap pointing."
  ],
  "next_experiment": "Construct the relative barycentric AW/cap map directly on the full cone, prove that it selects a distinguished integral point in the rank-nine lift space with both connector coherences, and compute its mod-two reflection parity without imposing endpoint unit normalization or dividing by 3."
}
~~~
