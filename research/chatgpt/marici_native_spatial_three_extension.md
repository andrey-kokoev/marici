# A polynomial spatial realization of the native conductor three-extension

Date: 2026-09-07  
Project: Marici — native normalization source to complementary-support geometry  
Pinned repository: `andrey-kokoev/marici` at `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## 1. Result

The complete native normalization dual, including its two nonzero branch attachments, has an explicit spatial realization over the occurrence polynomial ring. It is a three-term complex with one central coefficient module, three long-facet-link modules, and three mixed-short-pair modules. Its maps are restrictions between actual labelled coordinate strata. They are not arbitrary integer matrices extended by scalars.

The construction gives the exact polynomial three-extension

\[
0\longrightarrow M\longrightarrow T\xrightarrow{r}
G_{14}\oplus G_{03}\oplus G_{25}
\xrightarrow{m}
P_{14}\oplus P_{03}\oplus P_{25}
\xrightarrow{\epsilon}C\longrightarrow0.
\]

In words: the two endpoint canonical ideals, the full short-face ring, the three genuine long-facet links, the three genuine cross-branch pairs, and the conductor occur in one exact sequence.

With the three middle terms placed in cohomological degrees minus three, minus two, and minus one, this complex is quasi-isomorphic to the **entire** normalized native dual. Consequently its three-extension is the native nonsplit attachment, with the explicitly recorded orientation dictionary. This is stronger than matching the two cohomology groups or a primitive residue value.

Both endpoint triangles are essential. The full spatial cycle consists of twelve triangles in the three long-facet stars and the two endpoint triangles with coefficients minus one and plus one. Removing the endpoint triangles destroys the chain equation.

The result is an **occurrence-level coordinate-face realization** on the actual noncrossing geometry. It is not an identification of these face-ring modules with the original PC stalks that localize selected normal variables. Those stalks have not been replaced. The required comparison to the complete normal/Rees-supported Verdier functor, the existing collar operators in their separate frames, and the physical parity remain unproved.

## 2. Source ring and determinant convention

Let S be the spectator ring, including the three long occurrence variables, and set

\[
A=S[X_0,X_1,X_2,X_3,X_4,X_5],\qquad
E=\{0,2,4\},\qquad O=\{1,3,5\}.
\]

In words: all six short occurrences remain independent in the ambient ring. Normal and Rees parameters can be adjoined as distinct coefficients; none is identified with an occurrence coordinate here.

The native source is

\[
B=A/(J_EJ_O),\qquad
B_+=A/J_E,\quad B_-=A/J_O,\quad C=A/(J_E+J_O),
\]

\[
J_E=(X_0,X_2,X_4),\qquad J_O=(X_1,X_3,X_5).
\]

In words: the plus sheet carries the odd variables, the minus sheet carries the even variables, and their conductor is the common zero section. These are the actual source equations [S1], not the earlier one-dimensional node model.

Use the normalized ambient dual

\[
\mathcal D_B=R\operatorname{Hom}_A(B,\omega_A)[6],\qquad
\omega_A=A(-\mathbf1)\otimes\det\langle dX_0,\ldots,dX_5\rangle.
\]

In words: the six-coordinate canonical line and six-degree normalization are retained. Relative to the preceding unnormalized dual, cohomology in degrees three and five now occurs in degrees minus three and minus one. This normalization does not erase the sixth determinant coordinate.

Write

\[
w_E=X_0X_2X_4,\qquad w_O=X_1X_3X_5,
\qquad M=w_OB_+\oplus w_EB_-.
\]

In words: after the canonical-line normalization the two branch duals are represented by their principal top-occurrence ideals. Their reflection identifications include their exterior orientation signs.

The source normalization sequence is the supplied difference sequence

\[
0\longrightarrow B\longrightarrow B_+\oplus B_-
\xrightarrow{\varepsilon_+-\varepsilon_-}C\longrightarrow0.
\]

In words: both branch maps and the conductor difference must be retained before dualizing.

## 3. The source first becomes a ringed spatial complex on its two endpoint simplices

For a set F of short labels, define

\[
A_F=A/(X_i:i\notin F).
\]

In words: this is the coordinate ring of that labelled occurrence stratum. A deletion of one label acts by the corresponding zero-section quotient.

Let

\[
\Delta_0=2^E\cup2^O.
\]

In words: the source face complex consists of the two endpoint triangles and all their faces, with the empty face shared. There are fifteen faces including the empty face.

For any downward-closed face family Delta define

\[
\mathcal I_\Delta^{-p}=\bigoplus_{F\in\Delta,\ |F|=p}A_F[F],
\]

\[
d(a[F])=\sum_{j\in F}(-1)^{\operatorname{pos}_F(j)}
\bigl(a|_{X_j=0}\bigr)[F\setminus\{j\}].
\]

In words: these are oriented face boundaries with their actual coordinate quotient maps. Positions start at zero in the order of short indices. A missing variable is killed in a quotient module, not inverted. The empty-face term is retained.

There is an explicit polynomial quasi-isomorphism

\[
\mathcal D_B\simeq\mathcal I_{\Delta_0}.
\]

In words: the whole native dual, not merely its residue line, is now realized on the two endpoint simplices.

### Complete free-source verification

The actual free model uses the dual Koszul normalization cone. Write K-cochains on E, O, and all six variables with exterior differential given by wedge multiplication by the coordinate vector. Shift them by six and tensor with the canonical line. The cone of the signed projections from the six-variable complex to the two branch complexes has eighty free generators.

A branch generator on a subset H has degree `|H|-6`; a conductor-cone generator on H has degree `|H|-7`. Both have fine degree equal to the indicator of the complement of H. This makes every admissible map entry a uniquely determined monomial times an integer.

The checker constructs a map from this complete eighty-column source to the fifteen face-ring terms. Its nonzero entries are:

| Source column | Image |
|---|---|
| plus, 024 | `X1 X3 X5 [135]` |
| minus, 135 | `-X0 X2 X4 [024]` |
| conductor, 0245 | `-X1 X3 [135]` |
| conductor, 1345 | `X0 X2 [024]` |
| conductor, 02345 | `X1 [13]` |
| conductor, 12345 | `X0 [02]` |
| conductor, 012345 | `[0]-[1]` |

All other source columns map to zero. The table has eight terms in seven nonzero columns.

These are maps of quotient modules over A. The complete chain equation is checked on every source generator. In particular the last image is a primitive conductor cycle, while the first two images are the nonzero branch canonical classes.

The map's cone is integrally acyclic in all sixty-four possible positive occurrence-support types. This covers all polynomial exponents: a coordinate is either absent or has positive exponent, and all matrix entries are fixed by that support. Negative occurrence degrees give no coefficient columns in these normalized models. Every reduction uses signed-unit pivots.

For an independent proof, a single endpoint simplex has face complex whose only cohomology is its top principal ideal in degree minus three. Joining the two such complexes through their common empty-face term gives exactly the dual normalization triangle and its two bottom-component three-variable Gysin maps. The free-source comparison above fixes their coefficient and orientation rather than invoking an unspecified uniqueness assertion.

### Equivariant coherence is checked, not inferred from invariant homology

Rotation sends short index i to i+2. Reflection sends it to 1-i and exchanges the branches. The canonical-line action and conductor difference character are retained in the free-source action.

The degree-zero homogeneous Hom complex from the free source to the face model has dimensions

\[
(2,12,26,15)
\]

in degrees minus two, minus one, zero, and one. In words: these are the complete spaces of admissible polynomial comparison entries in the normalized frame.

Its three differential ranks are

\[
(2,10,15).
\]

In words: negative comparison cohomology vanishes and the degree-zero cohomology is one integral scalar. The checker solves for six transport homotopies and all thirty-six pair comparisons, then verifies all 216 triple equations. There are no columns below degree minus two, so these equations finish the higher coherence conditions. No averaging or division by two or three occurs.

This fixes a coherently equivariant source-to-face equivalence. It does not fix a physical comparison torsor involving additional normal/Rees data.

## 4. Actual short-face geometry adds exactly three bridges

Enumerate the genuine hexagon diagonals by the source's crossing test. The noncrossing complex on the six short diagonals is

\[
\Delta_{\rm sh}=\Delta_0\cup
\bigl\{\{0,3\},\{1,4\},\{2,5\}\bigr\}.
\]

In words: the only extra faces are the three compatible mixed even–odd pairs. All their proper faces already belong to the two endpoint simplices. The face count increases from fifteen to eighteen.

Its coordinate ring is

\[
T=A/(X_0X_1,X_1X_2,X_2X_3,X_3X_4,X_4X_5,X_5X_0).
\]

In words: the six crossing mixed pairs vanish; the three noncrossing mixed pairs remain. The native source quotient additionally kills precisely those three remaining pair monomials.

There is an exact source-derived sequence

\[
0\longrightarrow\bigoplus_{\{e,o\}\in\mathcal P}
X_eX_oA_{\{e,o\}}
\longrightarrow T\longrightarrow B\longrightarrow0,
\quad
\mathcal P=\{\{1,4\},\{0,3\},\{2,5\}\}.
\]

In words: its kernel consists of the three actual bridge ideals. This is a monomial support decomposition, not an artificial cone added to obtain a desired boundary.

The corresponding face-complex inclusion is strict:

\[
0\longrightarrow\mathcal I_{\Delta_0}
\longrightarrow\mathcal I_{\Delta_{\rm sh}}
\longrightarrow\bigoplus_{p\in\mathcal P}A_p[2]
\longrightarrow0.
\]

In words: the three relative bridge terms lie in degree minus two and have zero quotient differential. Their endpoints remain in the native subcomplex.

Orient a bridge from its even endpoint to its odd endpoint. Its connecting map to the native conductor is zero-section evaluation, with the recorded common sign. Thus in the bridge-oriented conductor frame it is

\[
\delta(a_{14},a_{03},a_{25})
=a_{14}(0,0)+a_{03}(0,0)+a_{25}(0,0).
\]

In words: each primitive bridge reaches the same conductor difference. This is an A-linear map to C. It is not extraction of an arbitrary monomial coefficient.

The native conductor class becomes a boundary in the absolute short-face complex. That fact is true but is **not** the end of the construction: its attachment must be retained through the entire relative filtration. The next section does that.

## 5. The three long-facet links supply the spatial three-extension

The full noncrossing complex has forty-five faces, with counts

\[
(1,9,21,14)
\]

by face cardinality zero through three. In words: it is the actual associahedral link, not a new simplicial complex chosen to fit a resolution.

Each long diagonal has a four-cycle as its short link. Its ring is

\[
\begin{aligned}
G_{03}&=A/(X_2,X_5,X_0X_1,X_3X_4),\\
G_{14}&=A/(X_0,X_3,X_1X_2,X_4X_5),\\
G_{25}&=A/(X_1,X_4,X_2X_3,X_5X_0).
\end{aligned}
\]

In words: these are the three actual square-road coordinate rings, with both their missing-coordinate and crossing-pair equations retained.

The bridge rings are

\[
P_{14}=A_{\{1,4\}},\qquad
P_{03}=A_{\{0,3\}},\qquad
P_{25}=A_{\{2,5\}}.
\]

In words: these are the three compatible mixed-pair strata, in the inherited road order.

The first differential is the three genuine restrictions:

\[
r(f)=\bigl(f|_{G_{14}},f|_{G_{03}},f|_{G_{25}}\bigr).
\]

In words: restrict a short-face function to each long-facet link.

The second is

\[
\begin{aligned}
m(g)_{14}&=g_{14}|_{P_{14}}-g_{03}|_{P_{14}},\\
m(g)_{03}&=g_{03}|_{P_{03}}-g_{25}|_{P_{03}},\\
m(g)_{25}&=g_{25}|_{P_{25}}-g_{14}|_{P_{25}}.
\end{aligned}
\]

In words: compare the two incident long-facet-link functions on each actual bridge. Each restriction is a quotient map of coordinate rings. The maps are not identities between three copies of A.

These maps and the conductor augmentation give the exact sequence in Section 1. Its all-polynomial proof is particularly small. For each monomial, classify its positive support:

* the empty support gives the ordinary exact norm–incidence–augmentation sequence;
* a singleton or a mixed bridge gives the exact sequence with ranks one, two, one;
* a same-branch two-face gives an isomorphism between the unique two surviving terms;
* a full endpoint triangle lies precisely in its endpoint principal ideal;
* a nonface gives no coefficient at all.

These possibilities exhaust all sixty-four supports and all exponent magnitudes. The executable also constructs and verifies the complete augmented sequence on every support, not only its Euler characteristic. There is no integral torsion.

## 6. The two endpoint cells are essential to the actual chain map

Let z-D be the cone on the oriented four-cycle linking long diagonal D. It consists of four actual triangles. Its boundary is that four-cycle. These cones are determined before any matrix comparison.

The full link cycle is

\[
Z=z_{14}+z_{03}+z_{25}-[024]+[135],
\qquad dZ=0.
\]

In words: twelve long-star triangles and the two endpoint triangles form the actual fourteen-triangle closed cycle. Both endpoint coefficients are forced by cancelling the remaining six pure-branch edges. Omitting them gives a nonzero boundary.

Projecting each long-star boundary onto the three oriented mixed bridges gives the matrix

\[
\begin{pmatrix}
1&-1&0\\
0&1&-1\\
-1&0&1
\end{pmatrix}
=1-R^2,
\qquad
R=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}.
\]

In words: the incidence is derived from the actual three squares. The signed cyclic tag change minus R gives the source's alternative convention:

\[
(1-R^2)(-R)=1-R.
\]

In words: this is a unimodular basis dictionary, not a fitted off-diagonal or a division by three. It reproduces the carrier matrix in the pinned source [S3], now with the entire polynomial restriction diagram and endpoint ideals present.

Put

\[
\mathcal P_{\rm sp}
=\left[T\xrightarrow r\bigoplus_DG_D\xrightarrow m\bigoplus_pP_p\right]
\]

in degrees minus three, minus two, and minus one. In words: this is the seven-module spatial representation of the native dual.

There is a literal A-linear cochain map to the native endpoint-face model. On the central term it is

\[
f\longmapsto f|_O[135]-f|_E[024].
\]

In words: the two endpoint triangles occur together, with opposite prescribed coefficients.

On a long-link term, take minus its two pure-branch boundary edges. On a bridge term, take its oriented two endpoint vertices. For example, on the D03 and P03 terms these maps are

\[
g_{03}\longmapsto g_{03}|_{\{1,3\}}[13]
+g_{03}|_{\{0,4\}}[04],
\]

\[
p_{03}\longmapsto p_{03}|_{\{3\}}[3]
-p_{03}|_{\{0\}}[0].
\]

In words: these are actual coordinate restrictions on actual edge and vertex cells. The D14 and D25 formulas are listed in the certificate, together with every sign.

The chain equation follows by taking the boundary of each long-star cone and then the boundary of the full fourteen-triangle cycle. It is checked on all seven module generators, all module relations, and every homogeneous coefficient support.

The cone of this map is integrally acyclic on all sixty-four occurrence supports. Therefore

\[
\mathcal P_{\rm sp}\xrightarrow{\ \simeq\ }
\mathcal I_{\Delta_0}\xleftarrow{\ \simeq\ }
\mathcal D_B.
\]

In words: this is an explicit polynomial comparison of the whole native derived object with the spatial complex. It is not inferred merely from equal cohomology ranks.

The spatial map is strictly equivariant under the actual labelled D3 actions. The free-source comparison on the other side has the six one-cells and thirty-six two-cells constructed in Section 3. Thus the roof gives a coherently equivariant derived identification without requiring a strict symmetric choice of Koszul contraction.

## 7. The native nonsplit attachment is transported, not removed

The spatial complex has

\[
H^{-3}(\mathcal P_{\rm sp})=M,\qquad
H^{-2}(\mathcal P_{\rm sp})=0,\qquad
H^{-1}(\mathcal P_{\rm sp})=C\otimes\chi.
\]

In words: the two branch canonical channels and the conductor channel occur in their correct degrees and character. The latter is still coupled to the former.

The displayed exact polynomial sequence is the three-extension representing the connecting map

\[
(C\otimes\chi)[1]\longrightarrow M[4].
\]

In words: it is the native degree-three attachment from the conductor to the branch module, in the normalized degree convention. The explicit quasi-isomorphism of complete complexes identifies this attachment, including its two components, with the native one.

The certificate uses exterior Koszul cochains. Passing from the literal Hom differential to this wedge convention multiplies degree-p basis vectors by the known sign `(-1)^(p(p+1)/2)`. This is plus one in branch degree three and minus one in conductor degree six. Accordingly the free-source top conductor column maps to `[0]-[1]`, while an even-to-odd bridge maps to the opposite oriented conductor class. The comparison records this sign. It is a basis convention, not a selected physical parity or an untracked scalar normalization.

Restricting to constant occurrence degree gives the exact integral window

\[
0\longrightarrow\mathbb Z
\xrightarrow{(1,1,1)^T}\mathbb Z^3
\xrightarrow{1-R^2}\mathbb Z^3
\xrightarrow{(1,1,1)}\mathbb Z
\longrightarrow0.
\]

In words: the earlier carrier norm, road relation, and augmentation are the constant coefficient part of the full spatial source extension. At that degree the branch canonical ideals have no coefficient. Away from that degree they are indispensable, and one cannot recover their extension by tensoring this integer sequence with A.

This explains the fate of the conductor in the absolute short-link inclusion. It disappears as an ordinary degree-minus-one class because the bridges fill the disconnected source link. Its correct spatial information is nevertheless retained by the complete three-extension above. The native source is neither an isolated conductor line nor a unit generic cycle.

## 8. What is and is not identified with the original target

The spatial faces in this construction are literal noncrossing faces. The two endpoint triangles and three long-facet links are already present in the associahedral/cubical carrier. Their ordering, D3 labels, and incidence signs are checked independently.

The coefficient functor is explicit: short face F carries the coordinate ring A-F. This is the natural ringed coordinate-strata realization of the normalization source and its compatible bridge strata. The original PC target instead carries normal-localized coefficient modules on states `(S,H)`. **No equality between these different coefficient functors is asserted.** In particular, no quotient by an occurrence variable is silently applied to the original target, and no occurrence inverse is introduced there.

The seven modules above are coordinate rings of entire face families, not seven free A-lines and not the seven generators of the earlier generic Q packet. Their constant-grade incidence agrees with the source Tate window, but the generic Q support, independent source excess, and normal/Rees conormal frames must still be carried by a correctly typed comparison.

Adjoining independent coefficient parameters and tensoring with bounded free normal/excess packets preserves the displayed chain equations. A nonflat occurrence or product-Rees specialization must be derived on the complete diagram, not taken after splitting its two cohomology modules. This note does not perform the remaining normal-frame identification with the existing collar 2-cells.

Thus the new construction closes a specific missing step: **the native nonsplit source attachment has an explicit, polynomial-linear, coherently equivariant spatial realization.** It does not yet prove the full support-PC/Verdier physical comparison or assign its reflection parity.

## 9. Verification

Run:

```sh
python check_marici_native_spatial_three_extension.py \
  --output marici_native_spatial_three_extension_certificate.json
```

The self-contained standard-library checker passes **19,809 exact assertions**. It constructs:

* the full eighty-column free native dual and its map to fifteen face-ring terms;
* the complete Hom spaces, transport homotopies, pair comparisons, and all 216 triple equations;
* all sixty-four source and target polynomial support modes and the actual comparison cones;
* the eighteen-face short link, all three bridge attachments, and all forty-five full-link faces;
* the three actual long-star four-cycles, the fourteen-triangle cycle with both endpoint corrections, and the complete seven-module spatial comparison;
* the exact augmented polynomial three-extension, all 192 squarefree coefficient multiplications, and all 240 commuting coefficient squares.

All matrix reductions use signed-unit pivots. The polynomial completeness argument is supportwise exact, not extrapolation from bounded exponent samples. No proof assistant or external symbolic algebra package is required. No repository files were written.

## 10. Sources and mathematical context

Pinned project sources:

[S1] `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`, blob `840258522d45e450e4f1e8bb927d9aae58c75566`: native source ring, two branch augmentations, conductor difference, and polarity.

[S2] `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`: literal noncrossing faces and the distinct original normal-localized target. Its stalks are not replaced by the face rings used in this source realization.

[S3] `research/voevodsky/check_multirees_cartier_pl_cap.rs`, blob `ef8c2ed7807d285ea413f471c112c2080c2e6c17`: established integral carrier Tate matrix and explicit warning that the carrier/coefficient tensor is not yet the support-PC correspondence.

Immediate preceding artifacts: `marici_native_conductor_dual_endpoint_attachment.md` and `marici_cubical_supported_dual_kernel.md`. Their normal/occurrence/Rees distinctions and physical scope boundaries remain in force.

Background: Kohji Yanagawa, *Stanley-Reisner rings, sheaves, and Poincare-Verdier duality*, arXiv `math/0301030`; Hans-Gert Gräbe, *A dualizing complex for Stanley-Reisner rings*, Mathematical Proceedings of the Cambridge Philosophical Society 96 (1984), 203–212. They explain the general connection between face-ring duality and spatial duality. The integral result here does not assume an unproved extension of a field-only theorem: its free-source map, both actual cones, module relations, and all polynomial support modes are constructed directly.
