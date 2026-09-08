# Native mixed-short-edge attachments in the actual generic Q diagram

Date: 2026-09-07  
Project: Marici, native-source comparison lane  
Pinned repository: `andrey-kokoev/marici`  
Commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## 1. Result and scope

The three supported mixed-edge occurrence modules from the preceding native-to-short-face comparison now have an explicit derived attachment diagram in the original 215-state target. The construction retains the original stalk domains, the complete native normalization source, its two endpoint maps, and the generic marked-normal correction.

The comparison is not an identification of three mixed edges with three long facets. Each edge module has a codimension-four occurrence resolution. It maps to the actual generic quotient through a degree-one derived class. The three classes have the native degree-two generic class as their common source connecting image. The resulting connecting row is `(1,1,1)`, derived from explicit resolution maps.

An individual edge class cannot be lifted independently into the endpoint quotient: its actual eighteen-term short-support transgression is primitive. Nevertheless, the complete native source has the previously constructed primitive lift. A full source-cone comparison now explains why these facts are compatible. Three short-supported presentations of the same native cap have been constructed; they have exactly the same two endpoint maps, and their comparison homotopies have zero endpoint component.

All assertions about Hom groups, primitives and replacement homotopies are in the declared six-occurrence determinant and three-long-normal frame. This does not identify the source with the independent branch-pair excess/Rees channel, identify these endpoint homotopies with the separately specified physical collar operators, or prove an equality of ringed six-functor constructions. Physical reflection parity remains unassigned.

## 2. Rings, source modules and target objects

Work over the independent polynomial chart

\[
A=\mathbb Z[X_0,\ldots,X_5,X_{D03},X_{D14},X_{D25},
 u_0,\ldots,u_5,u_{D03},u_{D14},u_{D25}].
\]

In words: occurrence and normal parameters are different coordinates. No occurrence variable is inverted. A target summand may invert only the normal coordinates prescribed by its unmarked face.

Put

\[
J_E=(X_0,X_2,X_4),\qquad J_O=(X_1,X_3,X_5),
\qquad \mathfrak B=A/(J_EJ_O).
\]

In words: this is the native normalization node. Its plus sheet is `A/J_E`, its minus sheet is `A/J_O`, and the two sheet values agree on their common conductor. These are the source labels of the normalization square [S1].

The actual noncrossing short-face complex has coordinate ring

\[
T=A/(X_iX_{i+1}:i\in\mathbb Z/6).
\]

In words: its forbidden pairs are the six adjacent short labels. Relative to the two native filled triangles, its only extra faces are the three opposite mixed pairs.

For the even-to-odd ordered pairs `(0,3)`, `(2,5)`, `(4,1)`, set

\[
A_{eo}=A/(X_j:j\notin\{e,o\}),\qquad
L_{eo}=X_eX_oA_{eo},\qquad
L=L_{03}\oplus L_{25}\oplus L_{41}.
\]

In words: retain both the four-coordinate annihilator and the principal pair-occurrence factor. Each summand is a supported module, not a free road label.

The native inclusion of face complexes supplies

\[
0\longrightarrow L\xrightarrow{\mu}T\xrightarrow{q}\mathfrak B\longrightarrow0.
\]

In words: a nonzero monomial in the kernel has support on exactly one opposite pair. It is divisible by that pair product; no other mixed short face exists. This proves exactness for every polynomial exponent, not only squarefree monomials.

For the target, use the original signed 215-state complex `K`, endpoint subcomplex `V`, and short-boundary subcomplex `B_s` from [S2]. Define

\[
E=K/V,\qquad Q=K/B_s,\qquad S=B_s/V.
\]

In words: the endpoint quotient and generic quotient are different objects. The target triangle is `S -> E -> Q -> S[1]`. Their underlying module-summand counts are 199, 7 and 192, respectively; their coefficients remain the original localized polynomial modules.

The comparison frame is

\[
\lambda=\sum_{\ell\in\{D03,D14,D25\}}e_{u_\ell}
        -\sum_{i=0}^{5}e_{X_i}.
\]

In words: all six short occurrence determinant directions and all three long-normal directions are retained. Negative coordinates here are degrees of a map, not licenses to invert occurrence coefficients in target stalks.

## 3. The complete source attachment triangle is executable

The native node has the fifty-generator product-ideal resolution `P`, with ranks `(1,9,18,15,6,1)`. The short-face ring has a sixty-four-generator Taylor resolution `T_bullet`; its twenty-four-generator minimal resolution has ranks `(1,6,9,6,2)`. Each bridge module has the sixteen-generator Koszul resolution on its four complementary short coordinates, shifted by its actual pair product. Their direct sum `L_bullet` has ranks `(3,12,18,12,3)`.

These source resolutions are exact integrally. For `P`, tensor the truncated Koszul resolutions of the disjoint even and odd coordinate ideals and then use their product inclusion. For `T_bullet`, each monomial-degree augmented Taylor complex is the simplex on the crossing generators dividing that monomial. For a bridge, the four complementary coordinates are a regular sequence. All these arguments hold with the unused occurrence and normal variables as polynomial spectators [M1].

### Canonical bridge inclusion

For a bridge `(e,o)` and a complementary coordinate `j`, exactly one of `(j,e)` and `(j,o)` is an adjacent crossing pair. Let `ell(j)` be that endpoint and `c(j)` the Taylor-generator label of the pair `{j,ell(j)}`. The bridge wedge on an ordered subset `J` maps to the Taylor wedge on the labels `c(J)` with coefficient

\[
\operatorname{sgn}(c|_J)\,
\frac{X_eX_o\prod_{j\in J}X_j}
 {\operatorname{lcm}_{j\in J}(X_jX_{\ell(j)})}.
\]

In words: the numerator is the source occurrence label, and the denominator is the target least-common-multiple label. The denominator divides the numerator. The formula is a polynomial monomial, not a ring localization. For the empty subset the coefficient is `X_e X_o`.

This gives all 48 source columns of `mu`. The checker verifies its chain equation and strict semilinear covariance under all six labelled dihedral transformations.

The ring quotient lifts to a polynomial chain map

\[
\phi:T_\bullet\longrightarrow P.
\]

In words: it lifts the identity on ambient coefficients in degree zero. Its construction uses only signed-unit contractions of exact monomial-degree subcomplexes of the native resolution.

The composition is supplied with a complete nullhomotopy

\[
d_Ph+hd_L=\phi\mu.
\]

In words: the mixed-pair inclusion becomes zero on the native node, but its resolution-level nullhomotopy is retained as data. The constructed `phi` has 67 nonzero polynomial entries and `h` has 33.

The source cone therefore maps to the native resolution by

\[
\Psi:\operatorname{Cone}(\mu)\longrightarrow P,
\qquad \Psi(t,l)=\phi(t)+h(l).
\]

In words: both the short-face map and its mixed-edge comparison occur in one chain map. Cone differentials and signs are the standard termwise-split conventions [M2].

The source cone has 112 generators, with ranks `(1,9,27,38,27,9,1)`. The cone of `Psi` has 162 generators and contracts to zero through exactly 81 signed-unit cancellations over the polynomial ring. The full homotopy identity is checked on every generator. An independent check in all 64 zero/positive short-occurrence support patterns also gives zero. Thus `Psi` is a polynomial chain equivalence, not a proposed identification inferred from matching homology ranks.

An inverse `P -> Cone(mu)` is also constructed. In the exhibited representatives, its composite back to `P` is exactly the identity.

## 4. Carry the entire endpoint-coupled cap through this triangle

The preceding joint-source computation supplied a polynomial map `F` into the actual target, of homological degree minus two, with defect

\[
d_KF-Fd_P=a,
\qquad a=a_+f_+-a_-f_-.
\]

In words: its only defect is the prescribed difference of the two native endpoint composites. It lies in `V`. The map has 43 nonzero entries and uses the actual complementary-face operation and all long-normal corrections. Neither source sheet is discarded.

Compose with the whole source triangle:

\[
A_T=F\phi,\qquad G_L=Fh.
\]

In words: these are a short-source cap and its mixed-edge comparison, not independently fitted maps. In the deterministic resolution representatives used here, the generic projection of `A_T` is zero term by term.

The complete equations are

\[
\begin{aligned}
d_KA_T-A_Td_T&=a\phi,\\
d_KG_L+G_Ld_L&=A_T\mu+ah.
\end{aligned}
\]

In words: the bridge equation retains its source attachment and the endpoint correction simultaneously. Removing either term would change the comparison problem.

The induced cap on the 112-generator cone satisfies

\[
d_K(F\Psi)-(F\Psi)d_{\operatorname{Cone}(\mu)}=a\Psi.
\]

In words: the whole attachment cone has the same two endpoint composites as the native source through the explicit source equivalence. This equation is verified on all columns with their full polynomial and normal exponents.

After quotienting by `V`, this is a closed map into `E`. The original native class is nonzero in `E` and `Q`; the precomposed short-source class is nonzero in `E` but has zero generic projection. This difference is expected from the source triangle and is not a contradiction between the two computations.

## 5. What an individual mixed edge sends to the actual generic target

Let

\[
U=u_{D03}u_{D14}u_{D25},\qquad
\omega=UT-\sum_{\ell\in\{D03,D14,D25\}}
X_\ell\frac{U}{u_\ell}M_\ell.
\]

In words: this is the actual corrected generic top cycle. The quotient `U/u_ell` is the product of the other two normal parameters, so every coefficient is polynomial. The marked states are the existing states, not new norm coordinates.

For a bridge, its source top wedge has all four complementary occurrence coordinates. Together with the bridge's pair product, its total source occurrence label contains all six short variables. The oriented generic cocycle is

\[
\theta_{eo}(e_{\widehat{eo}})=s_{eo}\omega,
\qquad (s_{03},s_{25},s_{41})=(-1,-1,+1).
\]

In words: the signs use the numerical complement-wedge order and the even-to-odd bridge orientation. All other source columns are zero. These are degree-one derived maps `L_eo -> Q[1]`. Their codimension-four occurrence residue and the target's degree-three top class account for the shift.

The maps commute with the full source and quotient differentials. With the source polarity character, all six labelled transports preserve the complete ordered family.

Lift each cocycle into the same original target summands, before quotienting by short support. Its boundary is

\[
\beta_{eo}=d\theta_{eo},\qquad
\beta_{eo}(e_{\widehat{eo}})=s_{eo}\,d_K\omega.
\]

In words: each has the actual eighteen-term short-support boundary. It has no endpoint term on this column. The entire target source-Hom calculation proves that the class is primitive and nonzero.

In particular, an individual edge class does not lift independently to `E`. This is a statement about every cochain and replacement homotopy in the prescribed frame, not just the displayed top wedge.

## 6. The complete derived groups and the commuting attachment square

All the following groups are the indicated fine-degree parts of full derived Hom complexes. Entries not displayed vanish in this frame.

| Source | Endpoint complex V | Short support S | Endpoint quotient E | Generic quotient Q |
|---|---|---|---|---|
| Native node | \(\operatorname{Ext}^3=\mathbb Z^2\) | Zero | \(\operatorname{Ext}^2=\mathbb Z\) | \(\operatorname{Ext}^2=\mathbb Z\) |
| Short-face ring | \(\operatorname{Ext}^3=\mathbb Z^2\) | \(\operatorname{Ext}^2=\mathbb Z^3\) | \(\operatorname{Ext}^2=\mathbb Z\) | \(\operatorname{Ext}^1=\mathbb Z^2\) |
| Three bridge modules | Zero | \(\operatorname{Ext}^2=\mathbb Z^3\) | Zero | \(\operatorname{Ext}^1=\mathbb Z^3\) |

All displayed groups are free abelian. There is no integer torsion in these homogeneous mapping complexes.

The endpoint entry for the bridges is acyclic, so adding arbitrary endpoint comparison homotopies cannot remove their independent generic transgressions. For the native source, in contrast, the map from `E` to `Q` is an isomorphism on the primitive degree-two group.

The source exact triangle gives

\[
0\longrightarrow\operatorname{Ext}^1_A(T,Q)_\lambda
\xrightarrow{\mu^*}\operatorname{Ext}^1_A(L,Q)_\lambda
\xrightarrow{\partial_s}\operatorname{Ext}^2_A(\mathfrak B,Q)_\lambda
\longrightarrow0.
\]

In words: the three edge residues give the native generic class through a connecting morphism. Their two differences come from the short-face source's generic comparison classes.

In the ordered bridge basis this is

\[
0\longrightarrow\mathbb Z^2\longrightarrow\mathbb Z^3
\xrightarrow{(1,1,1)}\mathbb Z\longrightarrow0.
\]

In words: each oriented bridge cocycle connects to the same positive native unit. This row is evaluated using the actual inverse `P -> Cone(mu)` and the actual generic target reduction. For each bridge the checker constructs the homotopy comparing that connecting cocycle with the original `F_Q`.

The computed initial columns for `mu*` are `(1,-1,0)` and `(-1,0,1)`. Signed integral combinations give the familiar primitive difference basis `(1,-1,0)`, `(0,1,-1)`. Their maximal nonzero minors include a unit. The kernel is therefore saturated over the integers.

The target connecting map gives another isomorphism

\[
\operatorname{Ext}^1_A(L,Q)_\lambda
\xrightarrow{\partial_t}
\operatorname{Ext}^2_A(L,S)_\lambda.
\]

In words: the three generic edge cocycles map to the three primitive actual short-support transgressions. Precomposition by `mu` also gives an integral isomorphism from `Ext2(T,S)` to `Ext2(L,S)`.

Consequently, each transgression has a short-source representative `U_eo:T -> S[2]`. They are computed explicitly, with 99, 85 and 109 nonzero target entries. Each maps to the same primitive `A_T` class in `E`. The checker retains cochain homotopies for every square, including the two distinct source and target connecting operations. It does not identify maps from equality of their ranks alone [M3].

### Both endpoints are preserved, not only their scalar values

For each short-source representative, the calculation gives

\[
U_{eo}-A_T=d_EH_{eo}+H_{eo}d_T.
\]

In words: an explicit homotopy inside the actual endpoint quotient compares the bridge presentation with the native cap.

Its endpoint component vanishes, and the endpoint defects agree exactly:

\[
\pi_V(d_KH_{eo})=0,\qquad
d_KU_{eo}-U_{eo}d_T=a\phi.
\]

In words: all three representatives have the same full plus and minus endpoint maps. In these representatives their endpoint correction 2-cells can be zero because the maps already agree, not because the endpoint object was omitted. Both independent endpoint classes are checked to be primitive. The endpoint complex has not been replaced by a pair of readout integers before this calculation.

The independently specified physical collar operators have different normal/Rees frames. The calculation does not assert that they are these particular endpoint-preserving Hom homotopies.

## 7. The actual long-diagonal geometry supplies differences, not a bijection

There is an independent label check in the actual noncrossing two-sphere on the nine scalar diagonals. The star of the long label `D03` is a cone on the short four-cycle `(0,3,1,4)`. The stars for `D25` and `D14` are obtained by adding two and four to the short labels. Every disk uses four existing noncrossing triangles.

After passing modulo the two native triangles, their boundaries have mixed-edge coordinates

\[
\begin{pmatrix}
1&-1&0\\
0&1&-1\\
-1&0&1
\end{pmatrix}.
\]

In words: rows are the bridges `03,25,41`, and columns are the long-labelled stars `D03,D25,D14`. Every long label compares two bridges. It does not correspond to one bridge module.

These three columns lie in the saturated kernel of the preceding augmentation. For each disk, the checker constructs the corresponding cocycle in the actual `Hom(T,Q)` complex and a cochain homotopy identifying its source restriction with that specific difference of bridge residues. The three generic comparison cocycles sum to zero exactly.

The native endpoint triangles remain in the complete geometric norm equation. If `D_ell` denotes the four-triangle star with the displayed orientation, then

\[
\partial\sum_\ell D_\ell
=\partial[0,2,4]-\partial[1,3,5].
\]

In words: the sum closes only after restoring the two native triangles with their opposite signs. The complete fourteen-triangle sphere is

\[
\sum_\ell D_\ell-[0,2,4]+[1,3,5],
\]

and its boundary is zero. In words: both native components are present in the actual closed chain. This is checked using the enumerated noncrossing faces; no disk or physical filling cell is added.

This geometric check labels the two generic comparison directions. It does not replace any polynomial module or support condition by its constant coefficient lattice.

## 8. What is, and is not, a choice

The native normalized cap is already a well-defined derived map with its two endpoint composites. Choosing a vector of three edge residues that presents it is additional data. In the oriented basis such a vector has coefficient sum one, and any two choices differ by the two-dimensional image of `Ext1(T,Q)`.

The deterministic contraction in this checker gives the presentation `(0,1,0)`. That vector is not declared physically preferred. A strictly rotation-invariant integral vector has three equal entries, so its readout is a multiple of three. The failure of an invariant readout-one representative is an optional strict-splitting obstruction, not a failure of the coupled native map.

The kernel injection is strictly equivariant on its whole Koszul/Taylor resolutions. The quotient lift is verified equivariant up to six explicit polynomial resolution homotopies. Its canonical derived equivariance follows from the underlying equivariant module quotient; the coordinate choices in a resolution do not supply a physical parity. The native cap and the oriented bridge generic cocycles retain the source's polarity compensation.

## 9. Verification, all-degree scope and the remaining physical comparison

Run:

```sh
python check_marici_mixed_short_edge_generic_attachment_triangle.py \
  --output marici_mixed_short_edge_generic_attachment_triangle_certificate.json
```

The standalone standard-library checker passes 72,862 exact assertions. It also records all principal maps and homotopies as sparse polynomial/Laurent matrices. The preceding joint-cap checker (20,522 assertions) and native-short-face checker (13,623 assertions) were rerun separately before this computation; their counts are not added to the new count.

The source-cone equivalence has a global polynomial contraction. Its 64 homogeneous checks are an independent verification, not an extrapolation from low exponents. For each derived Hom group, every allowed source/target pair in the fixed eighteen-coordinate fine degree has its unique possible coefficient monomial; the entire resulting complex is enumerated. The signed-unit contractions prove integral exactness and absence of torsion in those groups. Different-degree cochains cannot cancel a prescribed homogeneous unit because the differential preserves fine degree.

All occurrence multiplications and all positive normal multiplications commute with the displayed polynomial maps. This is verified symbolically; no occurrence coefficient is inverted. No assertion is made that all derived Hom groups in other normal frames have been computed.

The concrete advance is a completed derived attachment diagram from the native short-face quotient into the actual generic and endpoint target, with an exact dictionary for the three mixed edges and their two long-labelled differences. The remaining physical test is not another unconstrained edge identification. It is the Rees/Gysin transport of this entire coupled source triangle into the independent excess channel, retaining the six-occurrence determinant, both nonzero native endpoint maps, and the explicit normal corrections. This document does not establish that transport or assign physical reflection parity.

## Sources and conventions

[S1] `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`, blob `840258522d45e450e4f1e8bb927d9aae58c75566`, at the pinned commit: native node, sheet labels, normalization difference and polarity.

[S2] `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`: actual labelled faces, 215 target states, signed differential and individual localization domains. The target differential was fetched again for this computation.

[S3] `research/voevodsky/check_two_endpoint_tate_carrier.rs`, blob `0147e2e42dafac0da7289c571cb0331b51338be1`: original physical labels and distinction between carrier endpoint data and the full physical comparison.

[M1] Stacks Project, *The Koszul complex*, tag `0621`: https://stacks.math.columbia.edu/tag/0621.

[M2] Stacks Project, *Cones and termwise split sequences*, tag `014D`: https://stacks.math.columbia.edu/tag/014D.

[M3] Stacks Project, *Hom complexes*, tag `0A8H`: https://stacks.math.columbia.edu/tag/0A8H.

Direct input artifacts: `marici_native_short_face_comparison.md` and `marici_joint_conductor_spatial_cap_comparison.md`, with their self-contained checkers. The new checker incorporates the relevant algorithms and does not require these earlier files at runtime. Their distinctions between occurrence dualizing diagrams, normal-graded targets and full ringed supported-Verdier functors remain in force.
