# dP6 Common Refinement and the Log-Boundary Gysin Gate

## Record

Date: 2026-08-15

Status: proved in the exact integral fan, divisor-support, and reduced
log-boundary scope. The individual-Cartier no-go is scoped and does not
obstruct a future full-log excess-Gysin construction. No graph admission,
ringed support comparison, or physical endpoint/\(Q\) map is claimed.

## The common toric refinement

Let \(\Sigma_{dP_6}\) be the complete fan with cyclic rays

\[
v_0=(1,0),\quad v_1=(1,1),\quad v_2=(0,1),\quad
v_3=(-1,0),\quad v_4=(-1,-1),\quad v_5=(0,-1).
\]

Every consecutive determinant is one:

\[
\det(v_i,v_{i+1})=1.
\]

Hence the six consecutive cones form a smooth complete toric surface, the
degree-six del Pezzo surface \(dP_6\), equivalently the two-dimensional
permutohedral variety.

The identity lattice map refines the ordinary \(\mathbb P^2\) fan, with
cone targets

\[
(0,0,1,1,2,2),
\]

while \(-I\) refines its quadratic-Cremona transform, with cone targets

\[
(1,2,2,0,0,1).
\]

Thus there are toric morphisms

\[
\mathbb P^2\xleftarrow{\ \pi\ }dP_6
\xrightarrow{\ \pi_{\rm Cr}\ }\mathbb P^2,
\qquad
\pi_* = I,quad (\pi_{\rm Cr})_*=-I,
\]

and their composite resolves the quadratic Cremona transformation. This is
the minimal integral toric common refinement: each ordinary two-cone sector
is subdivided once, and all six primitive rays are required.

## Exact symmetry and polarity

On the lattice put

\[
R=\begin{pmatrix}0&-1\\1&-1\end{pmatrix},
\qquad
S=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
P=-I.
\]

Then

\[
R^3=S^2=I,
\qquad
SRS=R^{-1},
\qquad
PR=RP,
\qquad
PS=SP.
\]

The central polarity sends \(v_i\mapsto v_{i+3}\). Therefore the
entry-164 paired-incidence \(D_3\) action and sheet-polarity exchange lift
strictly to the permutohedral fan; polarity is geometrically the central
half-turn interchanging the two toric contractions.

## Individual Cartier pullbacks do not agree

For the first coordinate divisor of the ordinary \(\mathbb P^2\), the
reduced support of its total transform is

\[
\operatorname{Supp}\pi^*D_1=\{v_0,v_1,v_5\}.
\]

The Cremona-side pullback is its polar triple

\[
\operatorname{Supp}\pi_{\rm Cr}^*D_1
=\{v_2,v_3,v_4\}.
\]

These are disjoint alternating three-component divisors. Rotation gives the
same mismatch for the other two coordinate divisors. Consequently an
individual ordinary Cartier-edge square between the two \(\mathbb P^2\)
models is not Cartesian. In particular, one may not identify an entry-131
Cartier purity line across the Cremona correspondence by ordinary pullback.

This is a scoped no-go. It concerns individual Cartier total transforms; it
does not say that the full logarithmic boundary lacks a common refinement.

## The full log boundary is common

Let

\[
D_{\log}=D_0+D_1+D_2+D_3+D_4+D_5
\]

be the reduced toric boundary of \(dP_6\). The union of the three rotated
supports of \(\pi^*D_i\) is all six rays, and the same is true for
\(\pi_{\rm Cr}^*D_i\). Hence

\[
\boxed{
\operatorname{Supp}\pi^*D_{\mathbb P^2}^{\rm red}
=D_{\log}
=\operatorname{Supp}\pi_{\rm Cr}^*D_{\mathbb P^2}^{\rm red}.
}
\]

The common object is therefore the full six-component log boundary, not an
individual Cartier divisor. Multiplicities, conormal tensor factors, and
intersection strata have not been discarded: they are precisely the data a
future logarithmic excess-Gysin comparison must retain.

## Relation to paired incidence

Entry 164 proves the paired labels, branch incidences, generic
\(\mathbb P^2\) conductor fibre, and deep \(\mathbb P^3\) fibre at finite
coefficient level. The fan theorem supplies a common smooth toric carrier
for the generic \(\mathbb P^2\) and its polarity/Cremona transform. It does
not construct the Rees normalization of the paired fibre product, a global
cdh base change, or a support-graded map from this hexagon to the entry-143
endpoint filtration.

Accordingly, the fan resolves the rational map and validates the common
carrier refinement, but it does not identify the two alternating Cartier
triples or turn their equality after union into an individual purity square.

## Exhaustive codimension-two support no-go

There are exactly two bijections from the six fan rays to the six short
labels compatible simultaneously with \(D_3\) and polarity:

\[
(2,3,4,5,0,1),
\qquad
(5,0,1,2,3,4).
\]

They are the two allowed central shifts. Each is a bijection, so at ray level
the hexagon matches all six literal short grades in \(\delta_s\), once each.
This positive ray census does not extend across codimension two.

For either labeling, every adjacent fan cone
\(\langle v_i,v_{i+1}\rangle\) maps to two consecutive short labels whose
diagonals cross in the labelled hexagon. No face of \(K_6\), hence no
support grade of \(F_B/F_V\), contains that pair. Sending every such cone to
zero is not a chain-map repair: its boundary consists of two distinct,
nonzero ray-grade coordinates. Therefore

\[
\boxed{
\text{no direct support-graded cellular map }
C_*(dP_6,D_{\log})\longrightarrow F_B/F_V
\text{ extends either ray labeling.}
}
\]

This is stronger than an unconstructed-map statement. It is an exhaustive
finite no-go for the direct hexagonal cellular candidate. It remains scoped:
a full-log excess-Gysin correspondence may add the required pairwise
intersection Cech grades rather than identify them with nonexistent
associahedral faces.

## Positive unweighted bivariant repair boundary

Entries 95 and 143 already provide the unweighted carrier relations that a
future logarithmic construction must refine. In the augmented triangle,

\[
d_2^{\rm QTDS}=0,
\qquad
\partial_\triangle K_{\rm alt}=C_{\rm QTDS},
\qquad
K_{\rm alt}d_2=\Delta(1,-1),
\]

with the declared orientation convention. The marked road corridors retain

\[
\partial N_{\rm road}=3(v_--v_+).
\]

Thus the one-dimensional paths and their endpoint/norm data are fixed. The
remaining two-cell and top fillers are not fixed by these equations: they
retain the integral affine rank-nine freedom and the loaded \(\mathbb Z/2\)
existence test recorded by the endpoint-fixed butterfly audit.

At the first weighted overlap of adjacent boundary components \(a,b\), the
uncancelled radial term is, up to the declared incidence sign,

\[
\frac{X_a}{u_a}-\frac{X_b}{u_b}.
\]

It belongs on the pairwise boundary-intersection Cech grade. The full
endpoint object \(E=F_K/F_V\) can retain such lower grades; the quotient
\(Q=F_K/F_B\) alone cannot. A strict rank-one edge comparison therefore
fails, while a bivariant full-log repair remains open provided it constructs
the pairwise intersections, higher coherences, and proper push--pull rather
than fitting a filler. No graph admission follows.
## Two distinct local weighted tests

The codimension-two fan obstruction has an exact coefficient companion. For
one ordered adjacent pair \((a,b)\), the abstract line-valued
Koszul--Cech span \(W_{ab}\) closes: the weighted marked path has intermediate
coefficient

\[
w_a-w_b,
\]

and the unique double-localization correction has coefficient

\[
w_b-w_a.
\]

The cancellation and all signs are forced up to one global orientation, with
no source inversion. Nevertheless, for each of the six cyclic adjacent
pairs the two short diagonals cross. The face-indexed target
\(P=F_B/F_V\) has no simultaneous \((u_au_b)^{-1}\) summand. Thus the
abstract \(W_{ab}\) closure is proved, but its ordinary facewise pushforward
to \(P\) is falsified for all six pairs. Principal-line bookkeeping cannot
create a nonexistent face.

The actual marked \(D03\) packet is a separate test. Here

\[
\{D03,x_1,x_3\}
\]

is a genuine noncrossing \(K_6\) face, so its support labels do exist. Put

\[
y_a=\frac{X_{x_1}}{u_{x_1}},
\qquad
y_b=\frac{X_{x_3}}{u_{x_3}},
\qquad
z=y_aA+y_bB.
\]

In the fully Laurent-trivialized packet, the unique primitive is

\[
\boxed{
h=-y_aN_a-y_bN_b-y_ay_bC_{ab}.
}
\]

Its integral kernel is zero with unimodular pivots. But all three terms are
illegal in entry 143's target-side BM--Cech packet: the summand rule permits
\(u_a^{-1}\) only when \(a\in S\setminus H\), whereas \(N_a\), \(N_b\),
and \(C_{ab}\) carry the corresponding circled states in \(H\). Tensoring
the \(D03\) normal row changes signs only and cannot repair the forbidden
short-circle denominators.

Therefore the marked-face failure is not the dP6 crossing-face obstruction.
It is a reciprocal/Borel--Moore variance gate. Entry 131 alone supplies the
Cartier purity line but not this primitive.

There is nevertheless a positive coefficient/sign compatibility, recorded
here as an audit inference rather than a theorem of the compatible-face
checker. Entry 100's reciprocal packet \(K(I_+^\vee)\) provides the distinct
lines \(u_1^\vee,u_3^\vee\) and their wedge evaluation. Paired bivariantly
with the original-BM road packet, these evaluations reproduce

\[
-y_aN_a-y_bN_b-y_ay_bC_{ab}
\]

with the required signs and without placing inverse \(u_1\) or \(u_3\) on a
target circled state. They also retain the repeated-\(u_3\) excess line and
both Tor grades.

This does not close the actual face-indexed local packet. No single \(K_6\)
face carries the full \(Q_{03}\) denominator/support. The lower terms must be
distributed across the two marked half-corridor charts by a support-typed
bivariant \(\alpha_{\rm sh}\) map. Entry 100 proves the abstract local
coefficient pairing and sign pattern conditional on that spatial
correspondence; it does not legalize \(h\) as a class or map in entry 143's
BM--Cech packet. The spatial central-flip support map into the literal entry
143 states and \(Q\) remains missing.
## The literal entry-143 Q-section defect

Write the three long facets as

\[
\mathcal D=\{03,14,25\}
\]

and their four incident short labels as

\[
A_{03}=\{0,1,3,4\},\qquad
A_{14}=\{1,2,4,5\},\qquad
A_{25}=\{2,3,5,0\}.
\]

Let \(s\) denote only a candidate graded section from the abstract
seven-generator projective packet to a hexagonal lift of entry 143's
\(Q=F_K/F_B\). Its literal chain defect is

\[
\delta_s:=d_{\rm hex}s-sd_{\mathbb P}.
\]

On the projective top generator \(p\), the omitted short-facet grade is

\[
\boxed{
\delta_s(p)
=\sum_{a=0}^{5}\epsilon(p,a)\frac{X_a}{u_a}[F_a].
}
\]

Thus the top defect contains all six short \(X_a/u_a\) grades. On a long
generator \(p_D\), the next grade is

\[
\boxed{
\delta_s(p_D)
=\sum_{a\in A_D}\epsilon(D,a)
\frac{X_a}{u_a}[F_D\cap F_a],
\qquad D\in\mathcal D.
}
\]

Each long facet therefore carries four short \(X_a/u_a\) grades. These are
literal terms in the full hexagonal support differential. Entry 143's
quotient \(Q\), of ranks \((0,0,3,4)\), retains the three long-facet states
and the top but omits the short facets and their vertex/intersection terms.

It follows that \(\delta_s\) is not presently a class in \(Q\), nor may its
six- and four-short components be declared zero merely because the quotient
forgets their generators. The defect is untyped until one constructs a
support-graded hexagon-to-projective map

\[
\Phi_{\rm supp}:C_{\rm hex}^{\rm BM,\check C}
\longrightarrow C_{\mathbb P}^{\rm log}
\]

or a variance-correct correspondence inducing it, with a specified action
on every omitted short stratum. Only then can one ask whether
\(\delta_s\) is killed, pushed forward, or transgressed to a supported
boundary class.

## The toric excess-Gysin gate

The smallest admissible next morphism is a full-boundary logarithmic
excess-Gysin/proper push--pull

\[
\mathsf G_{dP_6}:
(\pi_{\rm Cr})_*\pi^!
\Longrightarrow
\mathsf{Corr}_{\rm supp}
\]

defined from the entire \(dP_6\) boundary correspondence. It must not be
assembled from three fictitious Cartesian individual-edge squares. For a
selected entry-131 Cartier line it must push the appropriate
three-component total transform to the purity generator with unit
orientation, while retaining:

- every pairwise and higher boundary-intersection Cech term;
- the lower radial and normal differentials;
- both conductor Tor grades;
- the separate occurrence and monodromy labels; and
- the six/four short components of \(\delta_s\) until their image is proved.

Only after this proper push--pull is typed may it be compared with the
entry-160 one-road Beck--Chevalley square or used in the entry-164 framed
mapping-fiber problem.

## Anti-circularity controls

- Do not identify the two disjoint alternating Cartier triples.
- Do not infer an individual Cartesian edge square from equality of the full
  reduced log boundary.
- Do not quotient the six/four short terms before defining
  \(\Phi_{\rm supp}\).
- Do not infer a ringed support map, Rees normalization, Gysin morphism,
  graph admission, endpoint connector, or parity from the fan refinement.
- Do not discard boundary multiplicities, lower Cech intersections, or Tor
  grades.
- Do not invert an occurrence variable, monodromy parameter, \(2\), or
  \(3\).

## Falsifiers and boundary

The fan theorem would be falsified by a non-unimodular consecutive cone,
failure of the two lattice maps to refine the ordinary and Cremona fans,
failure of the stated \(D_3\) relations, equality of an individual pair of
polar Cartier supports, or inequality of the two full reduced log-boundary
supports.

The construction boundary would be crossed only by a multiplicity-sensitive
logarithmic conormal comparison and proper excess-Gysin push--pull that
preserves every lower intersection term and yields a support-typed map to
\(F_B/F_V\). A fan map or equality of reduced supports alone is not such a
construction.

No global no-go is claimed. A full-log construction may exist even though
the individual ordinary Cartier squares do not.

## Exact certificate

The exact checker is

- `research/voevodsky/check_d03_dp6_common_refinement.rs`;
- `research/voevodsky/check_d03_weighted_adjacent_pair.rs`; and
- `research/voevodsky/check_d03_compatible_face_bm_cech_primitive_obstruction.rs`.

Their SHA-256 hashes are, respectively,

- `c0838591bfb2e2f6ddf143951636e9d5346ab1cca6cfde43d50ab6f6123a9229`;
- `5e6375625b0f51fbebcf7f46cf38c6b97b45f13f5a3c45da19a74bd117adf5c0`; and
- `3374caf4c3a45fb5ff00d1c970922d4200f56414b19b523a616ac602f39b3c43`.

It verifies all six rays and cones, smoothness, the identity and \(-I\)
refinements, the \(D_3\) and polarity relations, every rotated
three-component Cartier pullback, the disjoint alternating-triple no-go,
the common full log boundary, both exhaustive equivariant ray labelings,
the crossing-cone support failure, failure of the zero-cone chain-map
repair, and absence of integer torsion.

## Next experiment

Construct the toric full-boundary excess-Gysin/proper push--pull from the
hexagonal \(dP_6\) correspondence to the abstract projective packet and the
fixed entry-143 target. Require it to preserve all lower Cech intersections,
both Tor grades, and the six/four short \(X_a/u_a\) components. Then test
whether the three-component transform pushes to one entry-131 Cartier
purity line with unit orientation and whether the induced support-graded map
types \(\delta_s\). Only afterward test Beck--Chevalley and endpoint framing.

## Outcome contract

~~~json
{
  "claim": "The smooth six-ray dP6 fan is the minimal integral toric common refinement of the ordinary P2 fan and its quadratic-Cremona transform; D3 and central polarity act strictly, individual Cartier pullbacks are disjoint alternating triples, and the full reduced six-component log boundary is common.",
  "status": "proved",
  "scope": "exact integral fan, divisor-support, reduced-log-boundary, and literal Q-section-defect audit; individual-edge no-go only, with no graph admission or global support map",
  "assumptions": [
    "The entry-164 paired-incidence P2 and polarity labels are fixed.",
    "The entry-131 Cartier purity lines and entry-143 endpoint/Q support filtration remain fixed.",
    "Reduced boundary equality does not erase multiplicities, conormal factors, or lower intersections.",
    "The symbols X_a/u_a occur only in their legal target Cech summands."
  ],
  "factorization": {
    "fan_rays": 6,
    "maximal_cones": 6,
    "smoothness": "all consecutive determinants +1",
    "ordinary_P2_map": "identity lattice refinement",
    "Cremona_map": "-I lattice refinement",
    "D3": "R^3=S^2=1 and SRS=R^-1",
    "polarity": "central -I shifts rays by three",
    "individual_Cartier_pullbacks": "three components each",
    "individual_supports": "disjoint alternating triples",
    "individual_edge_Cartesian": "falsified",
    "full_reduced_log_boundary": "common six-ray support",
    "equivariant_ray_labelings": [[2, 3, 4, 5, 0, 1], [5, 0, 1, 2, 3, 4]],
    "ray_defect_grades": "all six short labels match exactly once",
    "codimension_two_support": "every adjacent cone maps to crossing short diagonals",
    "direct_support_graded_hexagon_map": "falsified",
    "zero_cone_chain_map": "falsified because cone boundaries have two nonzero ray grades",
    "integer_torsion": "none",
    "Q_section_top_defect": "six short X_a/u_a grades",
    "Q_section_long_defect": "four short X_a/u_a grades per long facet",
    "Q_section_defect_class": "untyped",
    "support_graded_hexagon_to_P_map": "unconstructed",
    "toric_excess_Gysin_proper_push_pull": "unconstructed",
    "lower_Cech_and_Tor_preservation": "required",
    "unweighted_QTDS_d2": "zero",
    "unweighted_partial_K_alt": "QTDS",
    "unweighted_K_alt_d2": "Delta(1,-1)",
    "marked_corridor_norm_boundary": "3(v_minus-v_plus)",
    "one_paths": "fixed",
    "two_cell_top_fillers": "rank-nine and loaded Z/2 remain",
    "weighted_first_overlap": "X_a/u_a-X_b/u_b requires pairwise intersection Cech in E; Q alone fails",
    "abstract_W_ab": "closes with coefficients w_a-w_b and w_b-w_a",
    "cyclic_adjacent_pair_pushforward": "falsified for all six crossing pairs",
    "actual_marked_face": "{D03,x1,x3} exists",
    "full_Laurent_primitive": "h=-y_a*N_a-y_b*N_b-y_a*y_b*C_ab, unique",
    "legal_BM_Cech_primitive": "falsified by circled-state denominator rule",
    "marked_face_failure_type": "reciprocal/BM variance gate, distinct from dP6 face obstruction",
    "entry100_dual_line_inference": "abstract bivariant coefficient/sign compatibility reproduces h without target inverses and retains repeated-u3 excess/Tor",
    "entry100_actual_BM_Cech_legalization": "not proved",
    "half_corridor_distribution": "requires missing support-typed bivariant alpha_sh",
    "spatial_central_flip_to_entry143_Q": "unconstructed"
  },
  "evidence_refs": [
    "research/voevodsky/check_d03_dp6_common_refinement.rs",
    "research/voevodsky/check_d03_weighted_adjacent_pair.rs",
    "research/voevodsky/check_d03_compatible_face_bm_cech_primitive_obstruction.rs",
    "research/voevodsky/check_paired_incidence_fibre_product.rs",
    "src/ledger/20260814-95 Conductor Normal-Link Fold and the Occurrence-Loaded Trace Boundary.md",
    "src/ledger/20260814-100 Support-Directed Can-Var Packet and Three Local Cousin Traces.md",
    "src/ledger/20260814-131 D03 Cartier Edge Purity and the Scoped PC Promotion.md",
    "src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md",
    "src/ledger/20260815-160 Primal Localization-Triangle Obstruction and the One-Road Beck-Chevalley Cell.md",
    "src/ledger/20260815-164 Paired-Incidence Descent and the Reduced cdh Vertex Connector.md"
  ],
  "checker_sha256": "c0838591bfb2e2f6ddf143951636e9d5346ab1cca6cfde43d50ab6f6123a9229",
  "weighted_adjacent_pair_checker_sha256": "5e6375625b0f51fbebcf7f46cf38c6b97b45f13f5a3c45da19a74bd117adf5c0",
  "compatible_face_bm_cech_checker_sha256": "3374caf4c3a45fb5ff00d1c970922d4200f56414b19b523a616ac602f39b3c43",
  "counterevidence": [
    "The two individual Cartier total transforms have disjoint alternating three-component supports.",
    "The fixed Q quotient omits the short strata supporting the literal section defect.",
    "No multiplicity-sensitive log conormal comparison or proper push-pull has been constructed.",
    "Equality of reduced full boundaries does not provide an individual Cartesian purity square.",
    "The only equivariant ray labelings send every adjacent fan cone to a crossing short-diagonal pair with no target support grade."
  ],
  "next_experiment": "Construct the toric full-boundary excess-Gysin/proper push-pull from the dP6 hexagon to the projective packet and fixed entry-143 target, preserving every lower Cech intersection, both Tor grades, and the six/four short section-defect terms before testing Cartier purity, Beck-Chevalley, or endpoint framing."
}
~~~
