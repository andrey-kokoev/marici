# Which supported endpoint choices extend to the full conductor diagram?

Date: 2026-09-07  
Lane: Branch B — global normalization descent and reverse endpoint comparisons  
Pinned coefficient model: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result and scope

This calculation keeps the actual endpoint extension, its nonzero conductor attachment, its old twelve-channel object, and its generic coefficient arrow fixed. It classifies the triangular automorphisms of that extension and computes exactly which changes of the supported reverse endpoint lifts arise from them.

There are global filtration-raising transformations, so filtration preservation plus the generic coefficient arrow does not imply rigidity. However, many of the formerly allowed supported variations do not extend across the whole normalization diagram. In particular, the constant corrections into the three double-subset channels at either endpoint do not extend. Their obstruction is visible even when every independent long normal is retained, or made invertible for a separate mathematical test.

The obstruction to extending a prescribed finite normal jet is an explicitly presented seven-generator ideal modulo its own normal-adic submodule. It is **not** obtained by setting its polynomial generators to zero in the ambient ring. The full derived normal fibre has three additional first-Tor lines and one second-Tor line, with explicit representatives. These are Tor groups of this restriction-obstruction module, not homotopy groups of the original arithmetic infinity-groupoid.

All claims concern the existing target-selected sheaves S12 and S14 on the test open V. The transformations fix their endpoint triangle; they do **not** hold the full map into the 215-state target pointwise fixed. That stronger condition would force the transformation to be the identity, since the constructed source identifies with the target's top kernel. No native physical source identification is asserted.

## 1. Fix the whole endpoint extension

Retain the ordered labels

\[
S_+=(13,15,35),\qquad S_-=(02,04,24),\qquad L=(03,14,25).
\]

In words: the two short sets label occurrence sheets; the three long directions remain independent.

Use the existing rings and open

\[
\mathcal C_0=\mathbb Z[X_\ell,u_\ell:\ell\in L],\qquad
\mathcal C=\mathcal C_0[t_s:s\in S_+\cup S_-],
\]
\[
\mathcal B=\mathcal C[X_s:s\in S_+\cup S_-]/(X_pX_m:p\in S_+,m\in S_-),
\]
\[
I_+=(X_p:p\in S_+),\quad I_-=(X_m:m\in S_-),\quad
\tau_+=\prod_{p\in S_+}t_p,\quad\tau_-=\prod_{m\in S_-}t_m,
\qquad V=D(\tau_+\tau_-,\tau_+I_+,\tau_-I_-).
\]

In words: this is exactly the previous alternating occurrence model and seven-chart test open. The short normals still obey their specified Rees relations; no long normal is identified with a short normal or assigned a scalar value.

The endpoint extension is

\[
0\longrightarrow\mathcal N\xrightarrow\iota\mathcal S_{14}
\xrightarrow q\mathcal S_{12}\longrightarrow0,
\qquad
\mathcal N=\mathcal I_+\Gamma_{+,S_-}\oplus\mathcal I_-\Gamma_{-,S_+}.
\]

In words: N is the pair of actual endpoint-ideal lines. The map q forgets only their normalization coordinates. The old twelve coordinates and their residues are not contracted.

For any global sheaf map h, define

\[
h:\mathcal S_{12}\longrightarrow\mathcal N,\qquad
U_h=1+\iota hq,\qquad U_h^{-1}=1-\iota hq.
\]

In words: h changes endpoint values without changing the old quotient. The square of its off-diagonal term is zero because q followed by iota is zero. These are all automorphisms inducing the identity on N and S12: subtract the identity from any such automorphism, factor through the kernel N, then through the quotient S12. This is the usual framed-extension calculation [M1].

The group law is addition of h. The generic coefficient map factors through q, so it is fixed. Under the full coherent duality already constructed, these maps become

\[
\mathbb D(U_h)=1+\mathbb D(q)\mathbb D(h)\mathbb D(\iota).
\]

In words: the reversed automorphism fixes the old reverse object and the endpoint quotient. In particular it preserves their actual connecting morphism kappa, rather than scaling or deleting its conductor attachment. It acts on the supported endpoint lift by an old-channel correction.

This is a precise comparison problem. It is not a classification of every possible native physical morphism, nor a declaration that these transformations preserve the full physical target map.

## 2. Derive every global transformation from normalization

Work on one sheet sigma. Let its opposite normal coordinates, in order, be a1, a2, a3. Set

\[
D_\sigma=\mathcal C_0[t_p^{\pm1}:p\in S_\sigma],\qquad
C_\sigma=D_\sigma[a_1,a_2,a_3],\qquad
A_\sigma=C_\sigma[X_p:p\in S_\sigma].
\]

In words: the active normal parameters are units on the entire normalization sheet inside V; the opposite normals are not. All occurrence variables and long parameters remain as specified.

The normalization sheet is the union of the open where all opposite normals are invertible and the three active occurrence opens. Its complement in Spec A-sigma is the locus where all three active occurrences and the opposite normal product vanish. That complement has codimension at least four. Direct intersection of the corresponding polynomial localizations, or the coordinate Cech complex, gives

\[
\Gamma(V_\sigma,\mathcal O_{V_\sigma})=A_\sigma.
\]

In words: these localizations do not introduce any new global occurrence pole or opposite-normal pole. This elementary coordinate statement is independently checked in the script. It can also be viewed as the normal/reflexive extension principle [M2].

On a dense occurrence chart, S12 has its generic coordinate and six proper-subset normalization coordinates. A map into the endpoint ideal must therefore have a row of seven branch functions. The row extends regularly to the whole normalization sheet: near the conductor the earlier splitting uses the regular conductor residues, and endomorphisms of the three-occurrence ideal are multiplication by regular branch functions. There are no cross-sheet maps into the opposite ideal, since such a map would have image supported on the conductor inside a torsion-free branch ideal.

Writing rho-N for the actual conductor residues, the full criterion is

\[
h_\sigma(a,z)=\alpha a+\sum_{\varnothing\ne N\subsetneq\{1,2,3\}}\beta_N z_N,
\qquad \alpha,\beta_N\in A_\sigma,
\]
\[
\overline\alpha+\sum_N\overline\beta_N\rho_N=0.
\]

In words: the bar is the actual occurrence-conductor evaluation. The last equation says that the endpoint output vanishes on the conductor and hence belongs to its branch ideal. It permits every global sheaf-linear correction, not just selected monomials.

### Retain the source's unit dictionary

The actual residues reduce to a particularly transparent form after rescaling only singleton coordinate frames by already invertible active normal parameters. These frame factors are:

| Active sheet | Opposite normals a1,a2,a3 | Long numerators v1,v2,v3 | Singleton frame units |
|---|---|---|---|
| Positive | t02,t04,t24 | u14,u25,u03 | t35,t13,t15 |
| Negative | t13,t15,t35 | u25,u03,u14 | t04,t24,t02 |

For a singleton i, write zeta-i for its displayed unit times z-i; leave double-subset coordinates unchanged, and set zeta-empty equal to the generic coordinate a. The conductor formulas become

\[
\rho'_N=\prod_{i\in N}\frac{v_i}{a_i},
\qquad \rho'_\varnothing=1,
\qquad |N|\le2.
\]

In words: these fractions occur only on the conductor where the denominators are units. The table retains all unit factors and all long-normal numerators. This is not scalar normalization by the long product.

Let b-N be the row coefficients in these frames. Multiplying the conductor relation by the opposite normal product gives a polynomial equation

\[
\sum_{|N|\le2}m_N\overline b_N=0,
\qquad
m_N=\prod_{i\in N}v_i\prod_{i\notin N}a_i.
\]

In words: there are seven fixed monomials, one for each old coordinate. Multiplication by the product is only a way to write the equality in the polynomial ring; it is not a division operation or a new support restriction.

Explicitly these monomials generate

\[
\mathfrak L_\sigma=
(a_1a_2a_3,\ v_1a_2a_3,\ v_2a_1a_3,\ v_3a_1a_2,
\ v_1v_2a_3,\ v_1v_3a_2,\ v_2v_3a_1)\subset C_\sigma.
\]

In words: every product chooses either the normal parameter or its independent long numerator in each of the three positions, except that the all-long-numerator product is absent.

The global transformation module on this endpoint is exactly

\[
H_\sigma=
I_\sigma A_\sigma^{\oplus7}
+A_\sigma\operatorname{Syz}_{C_\sigma}(m_N:|N|\le2).
\]

In words: arbitrary occurrence-tail coefficients are allowed, while their conductor constants must satisfy the seven-term relation. The equality follows by uniquely separating each row coefficient into its occurrence constant and occurrence-ideal part.

## 3. Construct the global maps and their coefficient coherences

There are nine elementary constant-row relations:

\[
h_{N,i}=v_i\zeta_N-a_i\zeta_{N\cup\{i\}},
\qquad |N|\le1,\quad i\notin N.
\]

In words: compare adjoining one normal label by the two actual conductor routes. Their conductor values cancel identically. Thus each expression is an endpoint-ideal-valued map on the whole source.

For each active occurrence p and each of the seven old coordinates, there is also the map X-p times that coordinate. These give twenty-one occurrence-tail generators. The nine relations together with these twenty-one maps generate every global H-sigma over A-sigma. The full coefficient relations involving occurrence tails are specified by the kernel formula above; the count thirty is not a claim that the module is free.

For example, on the positive sheet a global map is

\[
h=u_{14}a-t_{02}t_{35}z_{+,\{02\}}.
\]

In words: its conductor value is zero by the actual singleton residue. Adding it to the endpoint coordinate preserves the generic coefficient and the complete endpoint extension. No normal inverse has been introduced.

### Complete normal-row resolution

The seven-term ideal has an exact integral free resolution

\[
0\longrightarrow C_\sigma^{\oplus3}
\xrightarrow{d_2}C_\sigma^{\oplus9}
\xrightarrow{d_1}C_\sigma^{\oplus7}
\longrightarrow\mathfrak L_\sigma\longrightarrow0.
\]

In words: nine first relations have three independent square relations. The displayed modules are coefficient-resolution modules, not added geometric carrier cells.

With e-N the seven coefficient generators and E-N,i the nine relation generators,

\[
d_1E_{N,i}=v_i e_N-a_i e_{N\cup\{i\}}.
\]

In words: the differential is precisely the elementary conductor relation just constructed.

For i less than j the square boundary is

\[
d_2F_{ij}
=v_jE_{\varnothing,i}-v_iE_{\varnothing,j}
+a_iE_{\{i\},j}-a_jE_{\{j\},i}.
\]

In words: the two routes around each lower square agree, with all coefficients retained. The checker verifies the square identities as maps of the full ambient source resolutions, not merely as formal scalar equations.

Here is an all-degree exactness proof. Label the seven vertices of the three-cube other than its all-one vertex by the monomials m-N. Its lower three square faces have nine edges and seven vertices. Every pairwise least-common-multiple relation between two vertices is a polynomial combination of edges along the path through their intersection. No inverse is required. Those pairwise relations generate every monomial-homogeneous syzygy.

For the higher exactness, fix any monomial degree. For each coordinate pair, the available factors force the cube coordinate to zero, to one, leave it free, or exclude every cell. If a coordinate is forced to zero, the surviving subcomplex is a cube face. If none is forced to zero but some remain free, it is the union of their lower coordinate faces, which is contractible. If all are forced to one, it is empty. Thus every nonempty degree strand has exact augmented integral chains. This proves the resolution over the integers and with arbitrary polynomial exponents. All remaining variables and the allowed active units are unchanged coefficient extensions.

### The occurrence-tail maps require real chain homotopies

The source and endpoint sheaves have their existing ambient free resolutions. For a normal-row relation the branch and conductor row maps commute strictly, because the polynomial residue relation is exact on the common chart.

For a tail map X-p times an old channel, setting X-p to zero inside a free conductor resolution would be incorrect. I constructed the required occurrence-Koszul correction explicitly. If e-p denotes exterior insertion in the conductor resolution, it satisfies

\[
d(e_p\wedge -)+(e_p\wedge -)d=X_p.
\]

In words: multiplication by the occurrence equation is nullhomotopic on the conductor resolution, not literally zero there [M3].

For the tail map X-p times the generic coordinate, insert this wedge into the endpoint conductor column. For the tail map X-p times channel N, multiply the wedge by the actual residue rho-N, only in the conductor-supported part of the resolution. These terms make the map from the S12 resolution into the endpoint-kernel resolution commute with the differential.

The implementation checks every column of those maps on the 944-column S12 resolution and the 144-column endpoint resolution. It then constructs the automorphisms and their inverses on the 1088-column S14 resolution, and verifies the signed derived dual maps. There are 2,640 nonzero conductor-wedge columns across the tail constructions; they have not been suppressed.

The generic coefficient inclusion, old reverse object, and endpoint quotient remain fixed. The maps preserve the labelled dihedral transports. They raise the opposite-normal filtration strictly, while their diagonal identity has degree zero. Thus they are compatible with the weak filtration test and are generally excluded by the exact homogeneous test of the preceding step.

## 4. Compute which supported variations extend globally

Let j-sigma,n be the opposite-normal thickening from the preceding supported-lift calculation, defined by

\[
\mathfrak q_{\mathbf n}=(a_1^{n_1},a_2^{n_2},a_3^{n_3}),\qquad n_i>0.
\]

In words: retain every normal jet below the three indicated orders. On this support S12 and the endpoint ideal are free in the already fixed coordinate and line frames. The supported reverse differences therefore have coefficient module

\[
P_{\sigma,\mathbf n}=(A_\sigma/\mathfrak q_{\mathbf n}A_\sigma)^{\oplus7}.
\]

In words: these are global coefficients on the punctured active-occurrence support, with its endpoint, volume and conormal lines retained. The missing occurrence zero section does not add global functions: the three-coordinate Cech calculation gives the displayed polynomial coefficients, also over the finite normal-thickening rings.

Let res-n restrict a global transformation h to this supported difference module. The exact cokernel is

\[
\operatorname{coker}(H_\sigma\xrightarrow{\mathrm{res}_{\mathbf n}}P_{\sigma,\mathbf n})
\cong\mathfrak L_\sigma/\mathfrak q_{\mathbf n}\mathfrak L_\sigma.
\]

In words: a local supported choice extends to an automorphism of the fixed global endpoint triangle precisely when its class in this module is zero.

The isomorphism is explicit. Choose lifts b-N of the seven jet coefficients, take their occurrence constants, and form

\[
\operatorname{ob}_{\sigma,\mathbf n}(b)
=\left[\sum_{|N|\le2}m_N\overline b_N\right]
\in\mathfrak L_\sigma/\mathfrak q_{\mathbf n}\mathfrak L_\sigma.
\]

In words: the result is independent of the coefficient lifts, because changing a lift by a powered normal changes this expression by that powered normal times an element of L. The original normalization equation identifies its kernel with the image of the global maps. This is a presentation calculation, not merely a dimension count.

The formula is an equality of ungraded modules in the displayed frames. The grading is also retained: the polynomial-ideal presentation has a common internal offset by minus the degree of the full long product. That is the inherited Hom-line placement; it does not mean dividing the coefficient ring by the long product or inverting it.

### Reduced-support answer

For first powers, write n for the ideal (a1,a2,a3). Reducing the relation matrix gives

\[
\left.d_1E_{N,i}\right|_{\mathfrak n=0}=v_i e_N.
\]

In words: the generic coordinate has three long-normal relations, each singleton coordinate has two, and the doubleton coordinates have none. All occurrence-tail coefficients are already in the image of global maps.

Hence

\[
\mathfrak L_\sigma/\mathfrak n\mathfrak L_\sigma
\cong
\frac{D_\sigma}{(v_1,v_2,v_3)}
\oplus\bigoplus_{i=1}^{3}\frac{D_\sigma}{(v_j:j\ne i)}
\oplus D_\sigma^{\oplus3},
\]

with the seven original channel degrees and labels. In words: four long-normal quotient sectors and three unrestricted coefficient sectors measure the remaining global extension failure. They are not seven new physical states, and this is not a sheaf cokernel on W: locally on an occurrence chart the ideal I is a unit ideal and the choice does extend. It is the cokernel for **global** transformations on all of V.

In particular the constant correction into any doubleton channel is nonzero in this quotient. On the positive side, the correction into the channel (04,24) by coefficient one is an explicit example. It raises the opposite-normal filtration by one, preserves the supported endpoint counit, and has zero leading graded correction. It cannot be induced by any global triangular automorphism fixing the old object and the endpoint quotient. Multiplying it by an active occurrence does permit a global map; multiplying it by an independent long-normal polynomial does not remove its nonzero occurrence-constant part.

### Why naive specialization misses this result

Every m-N has at least one opposite-normal factor. Evaluating these polynomial expressions at zero would give zero for all seven. But

\[
\mathfrak L_\sigma/\mathfrak n\mathfrak L_\sigma\ne0.
\]

In words: taking the fibre of the actual coefficient module is not the same as evaluating its inclusion into the ambient ring. In particular the three degree-one-normal corner generators remain nonzero modulo n times L. This distinction is necessary even before the additional derived Tor terms below are considered.

The same argument applies to every positive triple of powers. Exact completion on finite modules gives the compatible formal criterion: the seven-term row must vanish in the completed coefficient ring [M4]. This describes formal limits of globally extendable transformations. It is not the entire automorphism group of the formal neighborhood, where the conductor is absent; nor does an arbitrary formal series satisfying the criterion automatically arise from a single polynomial global transformation.

## 5. Compute the full derived normal fibre

The resolution in Section 3 supplies more than its degree-zero cokernel. Reduce all its matrices modulo n without dropping any relation degree. The nine edge columns separate into three generic-root edges and six singleton edges. The three square columns map only to the root edges.

Let D-sigma denote the coefficient ring with the opposite normals set to zero, as above. The resulting derived groups are

\[
\operatorname{Tor}^{C_\sigma}_0(\mathfrak L_\sigma,D_\sigma)
=\mathfrak L_\sigma/\mathfrak n\mathfrak L_\sigma,
\]
\[
\operatorname{Tor}^{C_\sigma}_1(\mathfrak L_\sigma,D_\sigma)
\cong D_\sigma^{\oplus3},\qquad
\operatorname{Tor}^{C_\sigma}_2(\mathfrak L_\sigma,D_\sigma)
\cong D_\sigma,
\qquad \operatorname{Tor}^{C_\sigma}_i=0\quad(i>2).
\]

In words: the complete normal restriction retains three first-Tor families and one second-Tor family, in addition to the previously displayed seven-sector zeroth fibre. All lines keep their coefficient degree shifts. These are not additional homotopy groups assigned to the original marking space.

For each i let j,k be the other two labels. An explicit first-Tor generator is

\[
z_i=v_kE_{\{i\},j}-v_jE_{\{i\},k}.
\]

In words: the two singleton-edge routes have equal long-normal output. After normal restriction the square boundaries have only generic-root edge components, so they cannot bound this singleton-edge cycle.

The second-Tor generator is

\[
w=v_1F_{23}-v_2F_{13}+v_3F_{12}.
\]

In words: this is the top cubical compatibility among the three square relations. Its boundary is zero, and the resolution has no next term to bound it.

These generators are complete, not merely independent examples. The root block is the Koszul complex of the three independent long normals truncated before its last term; its top kernel is one free line. Each singleton block is the first part of a two-variable Koszul complex and has one free kernel line. The doubleton blocks have no incoming reduced edge. Regularity of the independent long variables gives the stated groups [M3].

No integer prime torsion occurs in these groups. The quotient sectors are torsion with respect to named long-normal parameters, not integers. A later non-flat specialization of those long parameters would require its own derived calculation.

### The missing corner is the actual triple-normal endpoint residue

For comparison, the full eight-corner product ideal is

\[
\mathfrak P_\sigma=\prod_{i=1}^{3}(a_i,v_i).
\]

In words: it includes the one omitted all-long-numerator corner. The exact sequence is

\[
0\longrightarrow\mathfrak L_\sigma
\longrightarrow\mathfrak P_\sigma
\longrightarrow (C_\sigma/\mathfrak n)\,[v_1v_2v_3]
\longrightarrow0.
\]

In words: the quotient is supported on the opposite triple-normal intersection, with its original full long-normal numerator. The bracket denotes the named generator and its degree, not a scalar division. Multiplication by any one opposite normal sends that corner into L; no polynomial without an opposite-normal factor does.

This identifies the origin of the omitted corner: S12 has every proper-subset channel but not the full endpoint channel. The sequence is an algebraic comparison of coefficient ideals already present in the calculation. It does not authorize adding a new physical filling cell or replacing S12 by a different native source.

## 6. What has been resolved

The complete global endpoint-triangle automorphism problem is now explicit. There are global, filtration-raising transformations preserving the genuine normalization attachment and the existing generic coefficient map. Their supported restrictions have the exact jet-level obstruction module described above. In particular the simplest doubleton-supported corrections cannot cross the conductor globally, even though they exist on every supported occurrence chart.

The earlier exact-grading rigidity remains correct: every nonidentity generator here raises the opposite-normal filtration and hence is excluded by exact weight preservation. The new result does not assume that the native physical source imposes that stronger condition. Instead it supplies a second, independent test of any proposed filtered comparison: its endpoint variation must satisfy the full global seven-term normalization relation, including its derived normal fibre.

If the full map into the 215-state target is also fixed pointwise, these triangular transformations are no longer allowed: they change actual top endpoint chains, and the source map into the top kernel is injective. This calculation therefore distinguishes automorphisms of the coefficient endpoint triangle from equivalences of a fully target-framed physical realization. It does not select such a realization by declaring its target map unchanged.

The native source remains to be independently mapped into this diagram. The unresolved task is not another scalar normalization: it is compatibility with the computed global relation maps, their conductor homotopies, and the triple-normal endpoint data while retaining the actual generic-Q source.

## 7. Verification

Run:

```sh
python check_marici_global_endpoint_transformations_20260907.py \
  --output marici_global_endpoint_transformations_certificate_20260907.json
```

The standalone standard-library checker passes **600,682 exact assertions**. It constructs all sixty global generator maps on the full ambient free resolutions, checks their inverse triangular automorphisms and signed duals, the generic and endpoint framing, all normal-row square coherences, and labelled dihedral covariance. The source maps are checked at chain level; occurrence-tail conductor nullhomotopies are explicitly retained.

The independent coefficient calculations include 729 untruncated integral multidegrees of the seven-nine-three resolution, all twenty-one pairwise Taylor reductions into its nine edges, 9,261 finite normal-jet cokernel multidegrees, and 512 full derived-normal-fibre multidegrees. All integral rank reductions use unit pivots and reject a nonunit residual. The all-polynomial and all-order results follow from the normalization-row classification, monomial/cubical exactness proof, and finite-module completion, not from extrapolating bounded samples.

The preceding reverse-endpoint checker was independently rerun and passed **49,961 exact assertions**. Its certificate hash is recorded in the new certificate. No repository files were modified, no current-head audit was claimed, and no carrier generator was added. This is an algebraic proof with executable verification, not proof-assistant certification.

## Sources and references

[P1] `marici_reverse_endpoint_gysin_20260907.md` and its standalone checker: the actual normalization residues, reverse endpoint triangle, supported Gysin domains, ambient free resolutions, and ungraded variation families.

[P2] `marici_normalization_endpoint_extension_20260907.md`: S12 and S14 as normalization pullbacks, identification with actual top kernel sheaves, the nonzero endpoint extension, and the global branch-function rings.

[P3] `marici_endpoint_multiplier_coherence_20260907.md`: endpoint ideal maps and the distinction between local multiplier choices and global coherent selection.

[P4] The preceding conversation's graded endpoint selection calculation: exact weight preservation eliminates the supported variation families, while the induced decreasing filtration allows strictly increasing corrections. The present checker independently verifies the relevant residue weights and filtration degrees; the corresponding later artifact was not available for a separate rerun in this runtime.

[M1] Stacks Project, *Extensions*, tag `010I`: https://stacks.math.columbia.edu/tag/010I.

[M2] Stacks Project, *Weil divisors on normal schemes*, tag `0EBK`, including extension of reflexive objects across codimension-two complements: https://stacks.math.columbia.edu/tag/0EBK. In the present coordinate rings the required statement is also proved directly by polynomial localization intersections.

[M3] Stacks Project, *The Koszul complex*, tag `0621`: https://stacks.math.columbia.edu/tag/0621.

[M4] Stacks Project, *Completion for Noetherian rings*, tag `0BNH`, and Lemma `00MA`: https://stacks.math.columbia.edu/tag/0BNH and https://stacks.math.columbia.edu/tag/00MA.

[M5] Stacks Project, *Global derived Hom*, tag `0B6A`: https://stacks.math.columbia.edu/tag/0B6A. The full derived dual is that of the actual coherent normalization diagram; no cohomology-only replacement is used.
