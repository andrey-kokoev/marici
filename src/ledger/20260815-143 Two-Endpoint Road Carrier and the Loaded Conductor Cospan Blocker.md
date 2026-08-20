# Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker

## Record

Date: 2026-08-15

Status: one exact integral spatial theorem and one sharp loaded blocker.

Entry 142 constructed the coefficient mapping fibre of the normalization-sheet
difference and the orientation-twisted road augmentation, but left both maps
to a common filtered endpoint object spatially untyped. The present entry
closes one side of that gap:

\[
\boxed{
V=\{v_+,v_-\}\subset B_{\rm short}\subset K_6
}
\]

is the actual integral road-side endpoint carrier. It realizes the complete
unsplit \(N/(1-r)/\epsilon\) window after one physical road-orientation
twist. The result is saturated, torsion-free, and \(D_3\)-equivariant.

The two **closed conductor points** are also matched to \(v_\pm\) by their
exact odd/even labels, and the marked plus/minus half-galleries concatenate
to the three road corridors.  This is stronger than a character match, but
it is still only a carrier map on the closed conductor fibre.  It does not
construct a ringed map from the full normalization--Cech branches or the
reciprocal/multi-Rees/PC extraordinary endpoint cospan.  That promotion
remains the single blocker.

## The actual two-endpoint pair

Let \(K_6\) be the labelled three-dimensional associahedron, let
\(B_{\rm short}\) be the union of its six short-diagonal facets, and let

\[
v_+=\{x_1,x_3,x_5\},
\qquad
v_-=\{x_0,x_2,x_4\}.
\]

Both vertices lie in \(B_{\rm short}\), and physical reflection exchanges
them. The relative cellular complex of the pair
\((B_{\rm short},V)\), with \(V=\{v_+,v_-\}\), has ranks

\[
\bigl(
\operatorname{rk} C_2,
\operatorname{rk} C_1,
\operatorname{rk} C_0
\bigr)
=(6,21,12)
\]

and differential ranks

\[
(6,12).
\]

Hence its only homology is in degree one and has rank three. The checker
proves the stronger integral statement. Six short-facet boundaries, three
road corridors joining \(v_+\) to \(v_-\), and twelve forest edges form a
unimodular basis of the twenty-one edge chains. Therefore

\[
\boxed{
H_1(B_{\rm short},V;\mathbb Z)\simeq\mathbb Z^3
}
\]

is saturated and torsion-free; no field calculation or rational projector is
used.

Choose the three corridor classes in physical road order

\[
(F_{14},F_{03},F_{25}).
\]

Every corridor has boundary

\[
\partial\gamma_i=v_--v_+.
\]

Consequently the relative endpoint map is exactly

\[
\epsilon=(1,1,1):
H_1(B_{\rm short},V)\longrightarrow
\widetilde H_0(V).
\]

## The closed-conductor label map and marked half-corridors

Entry 93's two branch ideals are

\[
J_+=(x_1,x_3,x_5),
\qquad
J_-=(x_0,x_2,x_4).
\]

Their closed conductor points therefore have exactly the labels of
\(v_+\) and \(v_-\).  In ordered bases \((+,-)\) and
\((v_+,v_-)\), the closed-fibre carrier map is the identity.  It commutes
with rotation and with reflection exchanging the two components, so the
sheet difference maps to \(v_--v_+\) before any character-only
identification is made.

For \(D=03\), entry 99's positive marked half-gallery and its polarity
conjugate are

\[
\gamma^+_{03}:
v_+
\longrightarrow
\{D03,x_1,x_3\}
\longrightarrow
\{D03,x_0,x_3\},
\]

\[
\gamma^-_{03}:
v_-
\longrightarrow
\{D03,x_0,x_4\}
\longrightarrow
\{D03,x_0,x_3\}.
\]

They meet at the same labelled road vertex.  Their difference

\[
\boxed{
\gamma_{03}=\gamma^+_{03}-\gamma^-_{03}
}
\]

is the primitive four-edge \(D03\) corridor and satisfies

\[
\partial\gamma_{03}=v_--v_+.
\]

Rotation gives the \(F_{14}\) and \(F_{25}\) corridors.  Thus the
normalization labels and the road endpoints agree at closed-conductor carrier
grade for a geometric reason, not only because both quotient lines carry the
same \(D_3\) character.

Let
\[
\Gamma_\Sigma^+=\sum_i\gamma_i^+,
\qquad
\Gamma_\Sigma^-=\sum_i\gamma_i^-,
\qquad
N_{\rm road}=\sum_i\gamma_i.
\]
The labelled special-leg chains satisfy the strict integral identity
\[
\boxed{\Gamma_\Sigma^+-\Gamma_\Sigma^-=N_{\rm road}}
\]
and
\[
\partial\Gamma_\Sigma^+=-3v_+,
\qquad
\partial\Gamma_\Sigma^-=-3v_-,
\qquad
\partial N_{\rm road}=3(v_--v_+).
\]
This is the exact carrier shadow of the sheetwise endpoint defect.  The
notation deliberately distinguishes \(\Gamma_\Sigma^\pm\subset F_B\)
from entry 113's nonzero generic \(q_\Sigma\in Q=F_K/F_B\).  The identity
is stronger than a character comparison, but it does not supply the loaded
boundary-crossing connector between those two support types.

Every edge in these half-galleries lies in \(B_{\rm short}\).  Their
literal image in \(Q=F_K/F_B\) is therefore zero.  The nonzero
\(q_\Sigma\) leg remains in the full seven-generator quotient and must be
related to the half-corridors by the missing loaded
Beck--Chevalley/boundary-crossing map.

## The physical \(D_3\) action and the one required twist

In the corridor basis, rotation acts by

\[
R=
\begin{pmatrix}
0&0&1\\
1&0&0\\
0&1&0
\end{pmatrix},
\]

while the raw cellular reflection is the road permutation

\[
S_{\rm raw}=
\begin{pmatrix}
0&1&0\\
1&0&0\\
0&0&1
\end{pmatrix}.
\]

The raw endpoint difference is reflection-odd. Therefore the complete pair
triangle must be tensor-twisted once by the physical road-orientation
character. After this single twist,

\[
S_{\rm road}=-S_{\rm raw},
\qquad
\widetilde H_0(V)=\mathbb Z_{\rm or},
\]

and

\[
\epsilon R=\epsilon,
\qquad
\epsilon S_{\rm road}=-\epsilon.
\]

This is the same endpoint character used by entry 142. The twist is global
to the pair triangle; it is not an edgewise sign fit.

## Recovery of the unsplit Tate window

The oriented boundaries of the three genuine long facets give the middle
map. In the geometrically normalized long-facet basis it is

\[
I-R^2=
\begin{pmatrix}
1&-1&0\\
0&1&-1\\
-1&0&1
\end{pmatrix}.
\]

It has rank two, primitive entries, norm kernel, and augmentation-zero image:

\[
(I-R^2)N=0,
\qquad
\epsilon(I-R^2)=0,
\qquad
N=(1,1,1)^T.
\]

Entry 142 uses the signed cyclic tag basis obtained by the unimodular change
\(-R\). In that basis the same geometric map is

\[
(I-R^2)(-R)=I-R.
\]

Thus the two formulas are a basis dictionary, not competing constructions.
The actual pair and its long-facet boundaries realize the integral exact
window

\[
0\longrightarrow\mathbb Z
\xrightarrow{N}P_{\rm tag}^{\rm or}
\xrightarrow{1-r}P_{\rm road}^{\rm or}
\xrightarrow{\epsilon}\mathbb Z_{\rm or}
\longrightarrow0.
\]

No splitting, averaging, or division by three occurs.

## The original-twist loaded support restriction

Entry 105 constructed the absolute unlocalized original-twist/Borel--Moore
support complex of the oriented boundary blowup, with generators
\((S,H)\) for \(H\subset S\). Applying that established generator rule to the
actual inclusions

\[
V\subset B_{\rm short}\subset K_6
\]

gives strict \(D_3\)-stable subcomplex ranks

\[
\boxed{
16\subset208\subset215.
}
\]

The quotient by the short-boundary support retains seven generators: the
top cell and the three physical long facets with their normal states. Hence
the nonzero \(Q\)-leg is not lost by passing from the carrier theorem to the
established original-twist support model.

This statement is deliberately scoped. It does not identify that
original-twist complex with a reciprocal-regular, multi-Rees, or complete PC
extraordinary costalk.

## The canonical original-twist endpoint/\(Q\) object

The strict support triple itself supplies a useful simplification. At the
already established original-twist/Borel--Moore level, the common
endpoint/\(Q\) object is not another unknown costalk:

\[
\boxed{
\mathcal E_{\partial,Q}^{\rm abs}:=F_K/F_V .
}
\]

It carries the canonical short exact filtration

\[
\boxed{
0\longrightarrow F_B/F_V
\longrightarrow F_K/F_V
\longrightarrow F_K/F_B=Q
\longrightarrow0 .
}
\]

Its carrier grade is \(C_*(K_6,V)\), with chain ranks
\((1,9,21,12)\) and differential ranks \((1,8,12)\). The unimodular
road basis above and a unit maximal minor of the genuine long-facet
connector prove

\[
\boxed{
H_1(K_6,V;\mathbb Z)\simeq\mathbb Z_{\rm or},
\qquad
H_i(K_6,V;\mathbb Z)=0\quad(i\ne1),
}
\]

after the same single road-orientation twist. The line is primitive and
torsion-free.

The loaded degree ranks are equally explicit:

\[
\begin{array}{c|c}
\text{object}&(\operatorname{rk}C_0,\operatorname{rk}C_1,
\operatorname{rk}C_2,\operatorname{rk}C_3)\\ \hline
F_K/F_V&(12,57,87,43)\\
F_B/F_V&(12,57,84,39)\\
Q=F_K/F_B&(0,0,3,4).
\end{array}
\]

Thus the original-twist endpoint object, its road-relative subobject, and
its nonzero generic \(Q\) quotient are canonical before any contraction.
What remains unknown is narrower: promote this fixed quotient and filtration
to reciprocal/multi-Rees/PC variance, and construct the full
normalization--Cech sheet arrow into that promotion.

## Verdier-dual shortcut audit

There is one further simplification, but not the tempting identification of
the common endpoint object with its dual.  All three terms in the displayed
filtration are bounded complexes of finite free modules.  Hence the
semilinear finite dual

\[
\boxed{
\mathcal E_{\partial,Q}^{\vee,\mathrm{fin}}
:=\mathbb D_\iota(\mathcal E_{\partial,Q}^{\rm abs}),
\qquad \iota(q_D)=q_D^{-1},
}
\]

exists canonically and has the reversed exact filtration

\[
0\longrightarrow\mathbb D_\iota(Q)
\longrightarrow\mathcal E_{\partial,Q}^{\vee,\mathrm{fin}}
\longrightarrow\mathbb D_\iota(F_B/F_V)
\longrightarrow0.
\]

The one-normal unit and orientation convention are already forced by the
entry-100 pairing
\(K(u)\otimes K(u^\vee)\to R[1]\), with
\(u^\vee=-q^{-1}u\).  Thus no second finite reciprocal coefficient complex
should be manufactured.

This finite dual is nevertheless not, by itself,
\(\mathcal E_{\partial,Q}^{!,\mathrm{PC}}\):

1. the canonical road inclusion
   \(F_B/F_V\to F_K/F_V\) dualizes in the opposite direction.  Turning it
   into a road-to-dual endpoint arrow requires the relative AW/cap pairing
   and its endpoint-compatible pointed butterfly, precisely the connector
   left open in entry 136;
2. the honest supported PC/Cousin object contains the extended Cech packets
   \(K_1(u)\to[R\to R[u^{-1}]]\).  They are not recovered by finite duality
   alone, and their lower localization terms must still glue globally;
3. entry 105 identifies the conductor source with
   \(\mathbb D(F_V)[-2]\) only at the locally completed, fixed-nonzero-
   \(\beta\) purity placement.  Entries 129--131 prove its edge
   restrictions, not a universal full normalization--Cech branch map.

The economical object is therefore the **paired packet** consisting of
\(\mathcal E_{\partial,Q}^{\rm abs}\), its canonical semilinear finite dual,
and the subquotient filtration.  The remaining construction is one
mixed-variance PC/Cousin enhancement with the endpoint connector and sheet
purity map.  Verdier duality removes an unnecessary object-construction
step; it does not manufacture either cospan leg.

## Forward refinement: the global target-side Cech realization

The Borel--Moore target-side Cousin extension is no longer an unknown
object.  For every entry-105 generator \((S,H)\), put

\[
\lambda(S,H)
=
\prod_{a\in S\setminus H}u_a^{-1}.
\]

The canonical extended Cech realization of the endpoint quotient is

\[
\boxed{
\mathcal E_{\partial,Q}^{\rm BM,\check C}
=
\bigoplus_{(S,H)\notin F_V}
R[X]\bigl[u_a^{-1}:a\in S\setminus H\bigr]\,[S,H].
}
\]

Its differential is forced, not fitted:

\[
d_{\check C}[S,H]
=
\sum_{a\ {m addable}}
\epsilon(S,a)\frac{X_a}{u_a}[S+a,H]
+
(-1)^{3-|S|}
\sum_{h\in H}(-1)^{\operatorname{pos}(h)}[S,H-h].
\]

Indeed the finite absolute differential has radial coefficient \(X_a\)
and normal coefficient \(u_h\), so the diagonal map

\[
\boxed{
\kappa[S,H]=\lambda(S,H)[S,H]_{\check C}
}
\]

satisfies

\[
d_{\check C}\kappa
=
\kappa d_{\rm abs}
\]

term by term.  The exact checker enumerates all 215 generators and verifies
both squares, every mixed radial/normal square, minimal denominator support,
the strict filtration

\[
F_V\subset F_B\subset F_K,
\]

the seven-generator \(Q\) quotient, and full \(D_3\) covariance.  In
particular the generic chamber retains the three physical long-facet arrows
\(X_D/u_D\); the \(Q\)-leg is not erased.  No occurrence variable and no
integer is inverted, and the normal inverses occur only inside their
indicated Cech summands.

This closes the global **target** Cousin gluing problem.  It does not identify
the reciprocal-regular normalization-sheet source with the Borel--Moore
target, and it does not point the endpoint butterfly.  The remaining problem
is therefore smaller than the blocker stated initially: construct one
mixed-variance bivariant sheet kernel and its two endpoint connector cells.
Do not manufacture another endpoint object.

## The theorem

The actual labelled triple

\[
V\subset B_{\rm short}\subset K_6
\]

canonically realizes the road-side endpoint-orientation carrier required by
entry 142. Its relative \(H_1\) is the saturated three-road module, its
endpoint boundary is \(\epsilon=(1,1,1)\), and its long-facet connector is the
integral Tate map \(1-r\) after an explicit unimodular basis change. The
entry-105 support construction restricts strictly to this triple and retains
the seven-generator \(Q\)-quotient.

More precisely, \(F_K/F_V\) is the canonical original-twist endpoint/\(Q\)
object, filtered by \(F_B/F_V\) with quotient \(Q\). Its carrier has the
single primitive orientation homology line required by entry 142. No new
endpoint object is needed until the reciprocal/multi-Rees/PC promotion.

The closed normalization-conductor fibre maps by exact labels to
\(V\), and the three marked sheetwise half-gallery pairs concatenate to the
three primitive road corridors.  Their special-leg sheetwise sums obey
\(\Gamma_\Sigma^+-\Gamma_\Sigma^-=N_{\rm road}\) strictly, with
boundary \(3(v_--v_+)\).  This is a spatial carrier identification of the
closed endpoints and the carrier-level endpoint defect; it is not entry
113's generic \(q_\Sigma\) leg.  It is not a ringed
identification of the full normalization sheets or their loaded PC costalks.

## Boundary of the claim

Three promotions are not earned by the theorem:

1. no ringed map from the full normalization--Cech branches of entry 93 to a
   loaded endpoint object has been constructed; only their two closed
   conductor points map to \(v_\pm\);
2. the target-side object \(\mathcal E_{\partial,Q}^{\rm BM,\check C}\)
   is now constructed, but no mixed-variance bivariant kernel maps the
   reciprocal normalization sheets into its supported Verdier dual while
   retaining both endpoint connector cells;
3. contracting to \(H_1\) forgets the distinguished chain-level \(Q\)
   representatives, so any loaded promotion must retain the full filtered
   cellular triple.

In particular, the theorem does not yet define

\[
d_{\rm sp,sc},
\qquad
G_{03}^{\rm Cousin},
\]

and it does not prove Cut/Beck--Chevalley naturality.

## Sharp blocker

The road-side target and its Cech differential are now fixed:

\[
\iota_{\rm road}^{\check C}:
(F_B/F_V)^{\rm BM,\check C}
\longrightarrow
\mathcal E_{\partial,Q}^{\rm BM,\check C}.
\]

The first missing datum is a support-typed mixed-variance kernel

\[
\boxed{
\alpha_{\rm sh}^{!,\check C}:
\mathcal S_{\rm sh}^{\rm norm,reg}
\longrightarrow
\mathbb D_{\rm supp}
\bigl(\mathcal E_{\partial,Q}^{\rm BM,\check C}\bigr)
\otimes\chi_N
}
\]

together with the two endpoint comparison 2-cells making
\(\alpha_{\rm sh}^{!,\check C}\) and
\(\iota_{\rm road}^{\check C}\) a pointed butterfly in the
two-extension category.  It must:

- extend the exact closed-point label map to the full
  normalization--Cech object rather than stopping at \(v_--v_+\);
- retain the based nonzero \(q_\Sigma\) leg and both endpoint connector cells;
- induce the established target map \(\kappa\) rather than a global
  localization of the source;
- preserve reciprocal-regular/Borel--Moore variance and both Tor grades;
- retain occurrence and independent multi-Rees filtrations;
- make the three half-corridor Cartier/central-flip counits commute with the
  entry-131 edge purity maps.

At carrier level the canonical AW roof exists, but its endpoint-fixed mapping
space is an unpointed \(\mathbb Z/2\)-torsor.  The front/back AW collars are
strictly \(D_3\)-homotopic and preserve any eventual parity; they do not
select it.  Equivalently, the missing finite data are precisely the coupled
endpoint connector cells defining

\[
r_{\partial,Q}(\beta_+,-\beta_-).
\]

Choosing their reflection one-cochain would choose the answer.  They must be
derived from the normalization--conductor geometry.  Until then
\(d_{\rm sp,sc}\) and \(G_{03}^{\rm Cousin}\) remain untyped.

That is now the single canonical blocker.  Another target complex, road
module, residue normalization, or group-cohomology calculation cannot close
it.

## Next experiment

Keep

\[
\mathcal E_{\partial,Q}^{\rm BM,\check C},
\qquad
\iota_{\rm road}^{\check C},
\qquad
F_V\subset F_B\subset F_K
\]

fixed. Construct only
\(\alpha_{\rm sh}^{!,\check C}\) and its two endpoint connector cells.
Then:

1. form the filtered derived pullback;
2. verify the mandatory ordinary-forgetting contraction of entry 133;
3. compute its integral rank and torsion;
4. only afterward test
   \[
   \operatorname{gr}_{\mathfrak c}^1
   =K_{\rm alt}\otimes L_{\rm pol},
   \qquad
   \operatorname{gr}_Q=+[q_\Sigma],
   \qquad
   \operatorname{Res}_{x_3}
   =\operatorname{pur}_{x_3,\partial}^{\rm PC};
   \]
5. read the residual reflection parity and apply entry 141's Bockstein rather
   than prescribing either value.

A zero pullback falsifies the local synthesis. A primitive rank-one result
gives uniqueness up to orientation. Higher rank or torsion demands an
additional coherence datum.

## Evidence

Exact certificate:

- research/voevodsky/check_two_endpoint_tate_carrier.rs
- SHA-256
  6c3166d0bdeee467b81d0dd335a7fdcd40373c6e1da67fc3fde01abdb946e8bf
- research/voevodsky/check_global_k6_koszul_cech_promotion.rs
- SHA-256
  3ee572a2d2f17d5a24d7ce5691397604551156baa577cbafde452ae4c7130ece

Verification:

~~~text
rustfmt --edition 2021 --check: pass
rustc --edition=2021 -D warnings -O: pass
executable assertions: pass
JSON output parse: pass, status=proved
pnpm check: pass
pnpm build: pass
git diff --check: pass
~~~

Dependencies:

- entry 93: normalization--conductor sheets and their difference;
- entry 94: the augmented triangle and primitive normalization;
- entry 105: absolute unlocalized original-twist/BM support complex;
- entry 100: one-normal Koszul--Cech comparison and support variance;
- entry 115: geometric Tate window;
- entry 131: endpoint edge purity;
- entry 142: degree-correct coefficient endpoint pullback.

The initial evidence packet is attached to delegated cross-audit task #2515
as artifact artifact-bf17feaf-4206-44ec-9938-7c5389475c8c.  The final
support-typed identity and checker hash were admitted as artifact
artifact-c6ed2877-ba88-45ee-b47a-97075dbbb295, superseding the ambiguous
\(q_\Sigma^\pm\) notation in the intermediate observation.  The task remains
routed to the builder workboard.  The target-side Cech checker was attached
to delegated task #2516 as artifact
artifact-f86a549f-2db8-4774-b820-e5c035e8259b.  The endpoint mapping-fibre
blocker was attached to task #2515 as artifact
artifact-53a96ea0-823e-4895-a79d-bccf30457af8.  Epistemic graph admission
remains pending because the graph surface is unavailable in the current MCP
carrier.

## Outcome contract

~~~json
{
  "claim": "The actual labelled pair V={v_plus,v_minus} subset B_short subset K6 canonically realizes the integral road-side endpoint-orientation carrier. H1(B_short,V)=Z^3 is saturated and torsion-free; after one physical road-orientation twist its boundary is epsilon=(1,1,1) into Z_or, and the long-facet connector is the unsplit Tate map 1-r up to an explicit unimodular tag rebase. Entry 93's odd/even closed conductor points map by exact labels to v_plus/v_minus, the two marked D03 half-galleries concatenate to a primitive corridor, and the rotated special-leg sums satisfy Gamma_Sigma_plus-Gamma_Sigma_minus=N_road with boundary 3(v_minus-v_plus), distinct from entry-113 q_Sigma in the generic Q leg. Entry 105 restricts to support ranks 16 subset 208 subset 215 and retains Q rank 7. The canonical original-twist endpoint/Q object is F_K/F_V, and it has the canonical target-side extended Cech promotion kappa[S,H]=prod_{a in S minus H}u_a^-1[S,H], with radial X_a/u_a and normal unit differential. The full reciprocal normalization-sheet kernel and endpoint pointing remain unconstructed.",
  "status": "proved",
  "assumptions": [
    "The theorem is scoped to the labelled K6 cellular pair and the already established entry-105 original-twist/BM support model.",
    "The complete pair triangle is tensor-twisted exactly once by the physical road-orientation character.",
    "The exact label map is claimed only for the two closed conductor points, not for the full normalization-Cech branches or PC costalks."
  ],
  "factorization_test": {
    "face_census": [1, 9, 21, 14],
    "pair_chain_ranks": [6, 21, 12],
    "pair_differential_ranks": [6, 12],
    "relative_homology": "H1=Z^3, saturated, torsion-free; all other relative homology zero",
    "geometric_middle": "I-R^2",
    "entry_142_middle": "I-R after signed cyclic tag rebase -R",
    "endpoint": [1, 1, 1],
    "closed_conductor_endpoint_map": "J_plus=(x1,x3,x5) to v_plus and J_minus=(x0,x2,x4) to v_minus",
    "D03_marked_half_corridor": "two primitive two-edge half-galleries concatenate at {D03,x0,x3} to the four-edge corridor",
    "special_leg_sheet_difference": "Gamma_Sigma_plus-Gamma_Sigma_minus=N_road strictly; boundary=3(v_minus-v_plus); this is not entry-113 q_Sigma in the generic Q leg",
    "entry_105_support_ranks": [16, 208, 215],
    "Q_rank": 7,
    "carrier_endpoint_Q_object": "C_*(K6,V) ranks (1,9,21,12), differential ranks (1,8,12), H1=Z_or after the road-orientation twist and all other homology zero; saturated and torsion-free",
    "absolute_endpoint_Q_object": "F_K/F_V with loaded degree ranks (12,57,87,43)",
    "absolute_endpoint_Q_filtration": "0 -> F_B/F_V degrees (12,57,84,39) -> F_K/F_V -> Q degrees (0,0,3,4) -> 0",
    "target_Cech_promotion": "proved on all 215 generators: kappa[S,H]=prod_{a in S minus H}u_a^-1[S,H], d_Cech kappa=kappa d_abs, strict endpoint/Q filtration, D3 covariance, and three nonzero generic long-facet arrows X_D/u_D",
    "finite_reciprocal_dual": "D_iota(F_K/F_V) exists canonically with reversed exact filtration 0 -> D_iota(Q) -> D_iota(F_K/F_V) -> D_iota(F_B/F_V) -> 0; this is not the full PC/Cousin cospan",
    "D3_covariance": "strict after one global road-orientation twist"
  },
  "counterevidence": [
    "No ringed map from the full normalization-Cech branches to the loaded endpoint object is constructed; the proved map is on the closed conductor fibre.",
    "The strict quotient, target-side Cech realization, and semilinear finite dual are canonical, but they do not construct the mixed-variance normalization-sheet kernel or its two endpoint connector cells.",
    "Passing only to H1 erases the distinguished chain-level Q representatives."
  ],
  "sharp_blocker": "With E_endpoint,Q^{BM,Cech}, its road inclusion, finite dual, and subquotient filtration fixed, construct the reciprocal normalization-sheet bivariant kernel and the coupled endpoint connector 2-cells. They must retain q_Sigma and induce the entry-131 edge purities without choosing the Z/2 butterfly point.",
  "next_experiment": "Construct only alpha_sh^{!,Cech}:S_sh^{norm,reg}->D_supp(E_endpoint,Q^{BM,Cech}) tensor chi_N and its two endpoint connector cells, perform the ordinary-forgetting ablation, and only then test K_alt, q_Sigma, the x3 residue, and reflection parity."
}
~~~
