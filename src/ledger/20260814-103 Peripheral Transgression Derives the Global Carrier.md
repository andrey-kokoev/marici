# Peripheral Transgression Derives the Global Carrier

## Record

Date: 2026-08-14

Status: proved at the integral cellular-carrier level. This entry refines the
provenance of entry 99's plus carrier. It does not construct the loaded
filtered comparison, a Pochhammer--Cousin morphism, or the full half-object.

## Claim

Let \(X=K_6\), let \(B=B_{\rm short}\) be the union of the six
short-diagonal facets, and let \(v_+\) be the all-odd central triangulation.
The actual labelled face poset supplies the bounded \(D_3\)-stable filtration

\[
F_0=C_*(v_+)\subset F_1=C_*(B)\subset F_2=C_*(X).
\]

Its only nontrivial reduced groups on the first exact-couple page are

\[
H_0(v_+)\simeq\mathbb Z,
\qquad
H_1(B,v_+)\simeq\mathbb Z^2,
\qquad
H_2(X,B)\simeq\mathbb Z^2.
\]

The first connecting transgression

\[
\boxed{
\delta_1:H_2(X,B)\longrightarrow H_1(B,v_+)
}
\]

is an integral saturated isomorphism. The three long-road facets
\((F_{14},F_{03},F_{25})\) map to their actual oriented peripheral boundary
cycles. Their sum is the boundary of the six short facets, and any two,
together with the short-facet boundaries, form a saturated basis of the
peripheral cycle lattice.

The three unique flips out of \(v_+\) canonically mark those same roads:

\[
(e_1,e_3,e_5)\longleftrightarrow(F_{14},F_{03},F_{25}).
\]

Consequently entry 99's map

\[
f_+\longmapsto K_{\rm rel},
\qquad
(e_1,e_3,e_5)\longmapsto(F_{14},F_{03},F_{25}),
\qquad
(q_0,q_1,q_2,a)\longmapsto0
\]

is the unique normalized \(D_3\)-equivariant augmented chain lift of
\(\delta_1^{-1}\), equivalently of the dual-block variance of the first
transgression. It is derived from the scalar face poset, not fitted to the
desired road matrix.

The uniqueness statement is integral. Before imposing transgression
normalization, every equivariant road map has the form

\[
M(a,b)=aI+b(J-I),
\qquad c=a+2b,
\]

where \(c\) is the top coefficient. Ordered orientation fixes \(c=1\). On
the peripheral augmentation quotient \(A_2\), the map acts by
\(1-3b\). Requiring the saturated inverse of \(\delta_1\) forces \(b=0\),
so \(M=I\). Symmetry and the top equation alone would also allow the
distinct integral map \(M(-1,1)\); the exact-couple geometry is what removes
that ambiguity.

## Evidence

The exact certificate is

- `research/voevodsky/check_central_vertex_rees_transgression.rs`

with SHA-256

```text
8075c4100f2a72a336b3d60166cd59ccb0863e3facb43121649a9e20b177dfc5
```

It enumerates the labelled hexagon associahedron with face census
\((1,9,21,14)\), constructs the signed cellular boundary and \(D_3\) actions,
computes the actual triple, certifies saturation by Smith factors, derives
the central-flip/road matching, classifies the full equivariant ambiguity,
and verifies the entry-99 chain map and its ordinary integral null-homotopy.

Reproduce with:

```powershell
$src = "research/voevodsky/check_central_vertex_rees_transgression.rs"
$exe = Join-Path $env:TEMP "check_central_vertex_rees_transgression.exe"
rustfmt --edition 2021 --check $src
rustc --edition=2021 -D warnings -O $src -o $exe
& $exe | ConvertFrom-Json | Out-Null
```

The primary audit reran the certificate and checked that its output status is
`proved`.

## Boundary

The literal barycentric coface block of \(v_+\) remains inside the star of
\(v_+\) and contains no long-road facet. It is therefore **not** entry 99's
map. The road map appears only after the peripheral contraction through
\(B_{\rm short}\).

Variance also matters. The homological connecting arrow is

\[
\delta_1:\text{relative roads}\longrightarrow\text{peripheral cycles};
\]

entry 99 is its normalized inverse/dual lift. Calling entry 99 itself
\(\delta_1\) reverses the canonical direction.

After forgetting the filtration and the peripheral marking, the carrier map
is explicitly null-homotopic. Therefore this theorem does not produce a
nonzero morphism in the ordinary unfiltered derived category. It proves no
occurrence pullback, normal/Rees weight, can--var map, Cech residue,
Pochhammer loading, physical-normal evaluation, or Tate comparison.

## Consequence

The next construction can be stated more economically as a correspondence.
Let \(\mathcal P_+^{F,\rm PC}\) denote the still-to-be-constructed loaded
peripheral object and let \(\mathcal R_{\rm road}^{F,\rm PC}\) denote the
loaded relative three-road object. Seek the cospan

\[
\boxed{
\mathcal S_+^{\rm cond}
\xrightarrow{\alpha_+^{\rm per}}
\mathcal P_+^{F,\rm PC}
\xleftarrow{\delta_1^{F,\rm PC}}
\mathcal R_{\rm road}^{F,\rm PC}.
}
\]

It must satisfy

\[
\operatorname{gr}(\delta_1^{F,\rm PC})=\delta_1,
\qquad
\operatorname{gr}\!\left(
(\delta_1^{F,\rm PC})^{-1}\alpha_+^{\rm per}
\right)=A_+^{\rm car},
\]

where the inverse is asserted only on the saturated associated-grade sector,
not as a strict global inverse. Its three peripheral restrictions must be the
entry-100 local excess traces; its supported road grade must be entry 101's
weighted star; and its carrier forgetting must recover entry 102's Tate
two-extension.

This factors the old single missing arrow into two geometrically typed tests:
conductor-to-peripheral comparison and coefficient-loaded peripheral
transgression. The immediate falsifier is failure of either map to preserve
one of the three established local residues without inverting a normal
parameter or dividing by three.

## Outcome contract

```json
{
  "claim": "For the actual cellular triple v+ subset B_short subset K6, entry 99's plus carrier is the unique normalized integral D3-equivariant augmented lift of the inverse/dual first connecting transgression; it is derived from the face poset and saturated peripheral marking, not fitted.",
  "status": "proved",
  "assumptions": [
    "The homological transgression is oriented from H2(K6,B_short) to H1(B_short,v+); entry 99 has the inverse/dual variance.",
    "Ordered diagonal normals fix dK_rel=F14+F03+F25 and the positive top normalization.",
    "The theorem is confined to integral cellular carriers."
  ],
  "evidence_refs": [
    "research/voevodsky/check_central_vertex_rees_transgression.rs",
    "ledger entries 99, 101, and 102"
  ],
  "factorization_test": {
    "actual_face_poset": "passed",
    "saturated_connecting_isomorphism": "passed",
    "D3_covariance": "passed",
    "equivariant_ambiguity_classification": "passed",
    "entry99_selection": "passed",
    "loaded_filtered_lift": "unconstructed"
  },
  "counterevidence": [
    "The literal dual-block inclusion contains no road facet.",
    "D3 covariance plus the top equation alone admits a second integral map.",
    "The selected carrier becomes null-homotopic after forgetting its filtration and peripheral marking."
  ],
  "next_experiment": "Construct the loaded conductor-to-peripheral and peripheral-transgression cospan, and test that its associated-grade inverse gives entry 99 while its three restrictions give the entry-100 local traces."
}
```
