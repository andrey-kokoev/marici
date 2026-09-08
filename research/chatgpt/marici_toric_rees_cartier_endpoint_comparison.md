# The toric Jacobian of the native trace ideal and the coupled Cartier endpoint map

Date: 2026-09-07  
Project: Marici — continuation of the completed normal-derived dual comparison  
Repository coefficients pinned to `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## 1. Result and scope

The pair-product ideal left by the preceding actual ring-linear dual calculation is not an arbitrary normalization defect. On an explicit symmetric modification of the three-long-Rees parameter space, its pullback is **exactly the relative Jacobian ideal**. The modification is obtained by blowing up the original Rees origin and then the three disjoint strict transforms of the coordinate axes. It has six smooth affine charts.

The complete forty-three-term native comparison factors through that invertible ideal. Its reverse map is therefore naturally corrected by the modification's relative canonical line. On every chart, the corrected generic class is primitive, including on all resolved central faces. Both endpoint composites become the same reduced boundary equation times the original endpoint pair. They have not become ordinary nonzero central-fibre endpoint maps.

More precisely, the full comparison defines one global morphism from the **two-term Cartier complex of the residual boundary** into the complete native-source mapping complex. Its lower component retains the generic cap; its upper component retains both endpoint composites. This is the actual chain-level Cartier/Gysin datum, with its line and degree, rather than a derivative applied to a scalar output alone.

There is also an essential excess calculation. The pullback of the original three-Rees central fibre has **two new excess generators**. Its Koszul complex is not the Koszul complex of the three resolved coordinates. These two generators are not identified with the already independent source excess eta. Consequently this note does not identify the new residual Cartier morphism with the original codimension-three physical Gysin, or with the full support-PC/Verdier correspondence and its prescribed collar maps. Physical reflection parity remains unassigned.

## 2. Fixed input and conventions

Only in this note's long-parameter formulas, indices 0, 1, 2 label the long diagonals D03, D14, D25. Their occurrence coordinates are denoted by Y_i to avoid confusing them with the six short occurrences X_0,...,X_5. Put

\[
u_i=t_iY_i,\qquad W=Y_0Y_1Y_2,\qquad \tau=t_0t_1t_2,
\qquad J=(t_1t_2,t_0t_2,t_0t_1).
\]

In words: use the declared long product-Rees chart and keep its three parameters independent. All short occurrences and short normals remain independent spectator coordinates during this modification.

Let R be the polynomial ring over the integers in those spectator coordinates and Y_0,Y_1,Y_2. The parameter space is

\[
X=\operatorname{Spec}R[t_0,t_1,t_2].
\]

In words: no occurrence, Rees parameter, or integer is inverted on the base. Any original monodromy units may be adjoined as a separate localization; they do not change the identities below.

The input P is the actual fifty-generator free resolution of the native normalization node. Its ranks are (1,9,18,15,6,1). The target is the complete 215-state finite normal complex K_1. Its individual localization maps to the original target and its normal-resolution tower are retained. Its support filtration is

\[
V\subset B\subset K_1,\qquad E=K_1/V,\qquad Q=K_1/B.
\]

In words: V is the sum of the two endpoint complexes, B is short-boundary support, E retains the endpoints as relative data, and Q is the genuine generic quotient. No state or support map is replaced by a scalar readout.

The previous comparison F_1 and its endpoint discrepancy have a common factor W after long Rees substitution. Because this common factor is proved on the entire map, pair the principal occurrence line (W) with its dual frame. Denote the resulting map by F and its endpoint coefficient by A. Then

\[
\partial F-F\partial_P=\tau A,
\qquad
A=a_+f_+-a_-f_-,
\qquad
\partial A+A\partial_P=0.
\]

In words: A retains the two native branch maps f_+,f_- and both endpoint maps a_+,a_-. F has cohomological Hom degree two and A has degree three. A is supported in V. Pairing (W) with its dual is not a ring homomorphism sending W to one.

At the individual endpoint source wedges,

\[
a_+(e_E)=[v_+,\varnothing],\qquad
 a_-(e_O)=-[v_-,\varnothing].
\]

In words: each is a primitive, framed endpoint map. The relative minus sign is already fixed by the original complement map and conductor difference. The composites with f_+,f_- have six polynomial terms and are not replaced by these two values.

The complete generic value on the top native generator is

\[
F(p_{E,O})=\tau T-\sum_{i=0}^2\left(\prod_{j\ne i}t_j\right)M_i.
\]

In words: the chamber and all three existing marked-long states remain together. The finite generic differential is

\[
\partial T=\sum_iY_iF_i,\qquad
\partial M_i=t_iY_iF_i.
\]

In words: this is the Rees base change of the original source-defined finite normal differential. F(p_{E,O}) is closed in Q. The notation F_i here denotes a long facet, not a component of the comparison map F.

## 3. The six-chart modification is an actual blowup construction

First blow up the ideal (t_0,t_1,t_2). On the chart where t_i is the leading coordinate, write

\[
t_i=s,\qquad t_j=sa,\qquad t_k=sb.
\]

In words: the strict transform of the i-th coordinate axis is cut out by (a,b). The three strict axis transforms are disjoint after the origin is blown up, so their union can be blown up without choosing an ordering between them.

One of the two resulting charts is

\[
t_i=s,\qquad t_j=sr,\qquad t_k=srq.
\]

In words: a=r and b=rq. Running over the six permutations (i,j,k) gives the six affine charts of Y. Each chart has ring R[s,r,q]. The composite

\[
b:Y\longrightarrow X
\]

is a projective birational morphism and is an isomorphism away from the three coordinate axes. It is constructed from the original Rees boundary stratification, with no choice of an endpoint sign or a preferred road. The affine chart and universal-property facts used here are [M1].

On this chart,

\[
J\mathcal O_Y=(s^2r),\qquad
\tau=s^3r^2q.
\]

In words: the three generators of J become s^2r times 1, q, and rq, in their appropriate order. Thus the whole ideal, not just one element, is principal. The universal property also gives a canonical map from this explicit regular refinement to the blowup of J [M2]. We do not assert that every possible principalization has this particular refinement.

### The image ideal is the relative Jacobian

Direct differentiation gives

\[
b^*(dt_i\wedge dt_j\wedge dt_k)
=s^2r\,ds\wedge dr\wedge dq.
\]

In words: in the ordered chart orientation the relative Jacobian has coefficient exactly s^2r, with no additional monomial or integer. Restoring the fixed global order of the long labels supplies only the sign of the permutation.

Consequently,

\[
\mathcal L:=J\mathcal O_Y
\cong\omega_{Y/X}^{-1},
\qquad
\omega_{Y/X}=\omega_{Y/R}\otimes b^*\omega_{X/R}^{-1}.
\]

In words: the invertible image ideal is the inverse relative canonical line. This equality is established by the explicit top-form map; it is not inferred from an asserted equality of physical six-functors.

Let D_0 be the origin exceptional divisor, D_{ij} the exceptional divisor over a coordinate axis with vanishing coordinates i,j, and H_i the strict transform of t_i=0. The divisor identities are

\[
\operatorname{div}(J\mathcal O_Y)=2D_0+\sum_{i<j}D_{ij},
\]

\[
 b^*\operatorname{div}(\tau)
=3D_0+2\sum_{i<j}D_{ij}+\sum_iH_i.
\]

In words: the Jacobian consumes two orders at the origin and one order over every axis. The endpoint product has exactly one more order on every boundary component.

Therefore the residual divisor is reduced:

\[
D=b^*\operatorname{div}(\tau)-\operatorname{div}(J\mathcal O_Y)
=D_0+\sum_{i<j}D_{ij}+\sum_iH_i.
\]

In words: D is the full seven-component toric boundary. Its equation on an ordered chart is

\[
z=srq=t_k.
\]

In words: the residual local equation is the trailing original Rees coordinate in that chart. It is an effective Cartier equation, although its zero locus is reducible.

The logarithmic identity retains all three coordinate directions:

\[
b^*\left(\frac{dt_i}{t_i}\wedge\frac{dt_j}{t_j}\wedge\frac{dt_k}{t_k}\right)
=\frac{ds}{s}\wedge\frac{dr}{r}\wedge\frac{dq}{q}.
\]

In words: the log-characteristic change has determinant one. This is not a claim that the ordinary three-equation Koszul complexes are equivalent; Section 8 calculates their difference.

## 4. Factor the complete native comparison through the Jacobian line

Every coefficient of the entire map b^*F lies in L. There is therefore a unique factorization into K_1 tensored with L. In the local generator g=s^2r, let its coefficient matrix be F-hat:

\[
b^*F=g\widehat F.
\]

In words: all coefficients of F-hat are polynomials on the chart. This is factorization through an invertible ideal, not permission to use 1/g in an original target stalk.

Write C_top for the sixteen-term unmarked block and C_i for the signed nine-term marked-i block, with all native source columns retained. Then

\[
\widehat F=C_k+qC_j+rqC_i+srqC_{\rm top}.
\]

In words: the full map has four ordered levels on a chart. It has not been replaced by its marked unit alone. Its exact identity is

\[
\partial\widehat F-\widehat F\partial_P=zA.
\]

In words: the complete generic comparison and both native endpoint composites remain coupled. The factor z is the residual boundary equation derived above, not an inserted scalar.

On the top native generator,

\[
\widehat F(p_{E,O})=srq\,T-rq\,M_i-q\,M_j-M_k.
\]

In words: the marked k-state has coefficient minus one. In the corresponding relative canonical frame, the generic reverse covector minus M_k dual has primitive value one.

This is a nonzero derived generic class, not only a nonzero matrix coefficient. Every cochain boundary can change the top-native/top-target coefficient only by an element of the six-short-occurrence ideal: the source's top differential has those occurrence coefficients, and the target has no degree-four state. The displayed unit is not in that ideal. This argument remains valid on every closed chart face and in the localized generic target, whose four top states are unlocalized.

The reverse factorization is a sheaf map of the form

\[
(b^*Q_1^\vee)\otimes\omega_{Y/X}
\longrightarrow (b^*P)^\vee[2].
\]

In words: the correction occurs in the domain of the reverse map, through the actual relative canonical line. The map still lands in the complete native dual, not a conductor summand split from its branch attachments. The all-order extension to the actual normal-derived dual is described in Section 7.

## 5. A single global Cartier morphism retains the endpoints

Set

\[
\mathcal I_D=(\tau)\mathcal L^{-1}\subset\mathcal O_Y.
\]

In words: its local generator is z=srq. Because the image ideal contains tau, this is an actual invertible ideal, not merely a fractional module.

Use the global two-term complex

\[
\mathcal K_D=[\mathcal I_D\hookrightarrow\mathcal O_Y]
\]

in cohomological degrees two and three. In words: this is the shifted Cartier resolution of the residual boundary. Its only cohomology is O_D in degree three. The shift and conormal line are part of the input.

Define

\[
\mathcal K_D\longrightarrow
\underline{\operatorname{Hom}}(b^*P,b^*K_1),
\qquad z\longmapsto\widehat F,
\qquad 1\longmapsto A.
\]

In words: the lower component is the whole normalized cap and the upper component is both endpoint composites together. The chain-map equations are precisely

\[
D_{\rm Hom}\widehat F=zA,
\qquad D_{\rm Hom}A=0.
\]

In words: this is a constructed morphism of complete complexes. It is not obtained by assigning endpoints after taking the generic class. Hom signs are those in [M3].

Both endpoint source maps are retained separately through the factorization

\[
A=a_+f_+-a_-f_-.
\]

In words: the actual native sheet maps determine how the two primitive endpoint channels enter. The checker constructs the adjoint total chain map from the two-term complex tensored with all fifty native generators. It also checks that map after tensoring with the independent excess factor.

### What survives on the residual boundary

The ordinary endpoint composite zA becomes zero on D. The **Cartier morphism** does not discard its upper component: its derived restriction is the map from the two zero-differential Cartier degrees that sends the upper generator to A modulo z. This retains a shifted endpoint channel.

The individual plus endpoint is nonzero against every polynomial homotopy: a homotopy changes its bottom coefficient only by the ideal

\[
(X_0,X_2,X_4,u_1,u_3,u_5).
\]

In words: the first three coordinates come from the source branch differential and the last three from the target endpoint normal differential. They cannot generate the coefficient one. The minus endpoint has the corresponding exchanged ideal and the same primitive conclusion. These classes remain nonzero after restricting any resolved long-coordinate face, because none of the defining short variables is changed.

At the level of the support connecting map, the full relation is

\[
\partial_{\rm supp}[\widehat F_E]=z[A].
\]

In words: its first residual-Cartier symbol is the ordered native endpoint pair with its conormal factor. Reading that symbol as A requires its dual conormal frame; it is not an unshifted scalar evaluation.

For each separate coordinate,

\[
\frac{D_{\rm Hom}\widehat F}{s}=rqA,\qquad
\frac{D_{\rm Hom}\widehat F}{r}=sqA,\qquad
\frac{D_{\rm Hom}\widehat F}{q}=srA.
\]

In words: the other two boundary factors remain. At component intersections one cannot discard them or identify the total-divisor Cartier class with the original three-normal Gysin. The source's warning about retaining conormal symbols [S3] applies here.

### All chart faces

| Vanishing chart coordinates | Full normalized comparison terms | Ordinary endpoint-composite terms |
|---|---:|---:|
| None | 43 | 6 |
| s | 27 | 0 |
| r | 18 | 0 |
| q | 9 | 0 |
| s,r | 18 | 0 |
| s,q | 9 | 0 |
| r,q | 9 | 0 |
| s,r,q | 9 | 0 |

The primitive marked generic coefficient remains minus one in every row. The upper Cartier endpoint channel remains present, although the ordinary endpoint composite in the last column is zero. These are different components of the constructed two-term morphism.

## 6. The whole diagram glues with its line transitions

For adjacent chart orders, the coordinate changes are

\[
(i,j,k)\longleftrightarrow(j,i,k):
(s',r',q')=(sr,r^{-1},rq),
\]

\[
(i,j,k)\longleftrightarrow(i,k,j):
(s',r',q')=(s,rq,q^{-1}).
\]

In words: r is invertible only on the first overlap, q only on the second. These are ordinary affine overlaps of the constructed blowups, not inversions in the original target coefficient domains.

The first swap preserves g and z. The second has

\[
g'=qg,\qquad z'=q^{-1}z,
\qquad \widehat F'=q^{-1}\widehat F.
\]

In words: the cap and the residual Cartier generator have exactly the same transition; the upper endpoint A is unchanged. Thus the two components define the global map in Section 5, with no choice of a separate endpoint transition.

All triple-overlap cocycles hold on monomial exponents and on the Cartier line. All six dihedral actions transport the full 215-state differential, the whole native map, and both endpoint composites. The inherited conductor polarity is retained. The relative Jacobian orientation is supplied by the actual top-form map, not an averaging argument.

No global scalar unit has thereby been introduced on X. The original map is recovered locally by multiplying F-hat by g, restoring the original proper ideal J.

There is a stronger distinction even on Y. A global regular degree-three covector in the relative canonical twist would require rational coefficient functions with poles allowed only on the exceptional Jacobian divisor. Its image in X has codimension at least two. Since the polynomial base is normal, such a function has no pole along any codimension-one base divisor and is a polynomial. Hence

\[
\Gamma(Y,\mathcal L^{-1})=R[t_0,t_1,t_2].
\]

In words: global regular covectors of this form still have trace values in J; none has value one. The local primitive sheaf-level trace and a global polynomial covector are different claims. This argument concerns regular representatives, not an uncomputed global derived splitting of the completed kernel.

## 7. Compatibility with the original localization target

The normal tower from the preceding calculation uses the same 215 states with finite-free differentials and diagonal transition maps

\[
j_{\mathbf n,\mathbf m}[S,H]
=\left(\prod_{a\in S\setminus H}u_a^{m_a-n_a}\right)[S,H].
\]

In words: these are the source-admitted localization transitions; no occurrence inverse enters them.

At each order n, first perform the same long Rees substitution and then factor the complete comparison through W and the pulled-back ideal L. The transition maps preserve that factorization, the residual z, and the two endpoint equations. The all-order statement follows directly because the transitions are diagonal polynomial multiplications on the existing target states. The checker verifies two additional anisotropic/higher order choices on all six charts.

The colimit map into the actual normal-localized target and the reverse derived-inverse-limit map therefore retain this normal-space line factorization. This does not assume that arbitrary nonflat base changes commute with underived inverse limits: the compatible maps are built at the finite-free level, then passed to their stated limits. Nor does it identify ambient ring-duality with the full physical supported-Verdier functor.

## 8. The original central fibre acquires rank-two excess

The ordinary pullback of the original long Cartier equations is

\[
K(t_i,t_j,t_k)\otimes\mathcal O_Y=K(s,sr,srq).
\]

In words: those are the equations inherited from the original Rees space. They are not the three regular equations s,r,q.

The integral change of generators

\[
\zeta_j=e_j-re_i,\qquad
\zeta_k=e_k-rq e_i
\]

has determinant one and gives

\[
K(s,sr,srq)\cong K(s)\otimes\Lambda(\zeta_j,\zeta_k),
\qquad d\zeta_j=d\zeta_k=0.
\]

In words: the central pullback has two actual excess directions, with no denominator. Its homology is

\[
H_n\bigl(K(s,sr,srq)\bigr)
\cong\mathcal O_Y/(s)\otimes\Lambda^n\langle\zeta_j,\zeta_k\rangle,
\qquad n=0,1,2.
\]

In words: the ranks are one, two, one on the origin exceptional divisor. Higher homology vanishes. All eight wedge equations and the integral inverse change are explicit.

This calculation also explains why the residual divisor must not be used to erase the independent original normal directions. The residual one-Cartier Gysin in Section 5 is a constructed morphism, but it is not automatically the pullback of the original codimension-three Gysin.

The original selected SHORT-normal excess is separately retained:

\[
\eta=t_3h_3^+-h_3^{03}.
\]

In words: the subscript three here is the original short shared normal, not one of the three long labels used in this note. The original five-normal selected source has a unimodular decomposition into its four regular equations and this zero-differential factor. The checker verifies all thirty-two wedges; at its central short-Rees face eta is minus the pair generator, not zero.

The complete Cartier/native map is checked with this independent factor tensored through. Neither zeta direction is identified with eta, and none is replaced by an internal target marked state. Identifying the resulting excess bundles with the prescribed physical source is a remaining comparison, not an algebraic cancellation.

## 9. What this establishes, and the remaining physical test

This construction identifies the formerly unexplained trace ideal with an actual relative Jacobian, factors the **complete** native comparison through the corresponding canonical line, and constructs one globally glued Cartier morphism carrying its primitive generic cap and both endpoint composites in their correct adjacent degrees.

It does not turn the old zero ordinary central-fibre map into an ordinary unit map. The corrected map is line-valued, and its endpoint continuation is an extension morphism with retained conormal information. Multiplying back by the Jacobian recovers the original vanishing and the original image ideal.

The next physical identification has concrete inputs: this complete Cartier/native diagram, the two-dimensional long-Rees excess, the independently retained short excess, and the earlier framed spatial collars. A comparison must account for all of these simultaneously. No full physical parity or supported-Verdier equivalence is concluded here.

## 10. Reproduction and evidence

Run:

```sh
python check_marici_toric_rees_cartier_endpoint_comparison.py \
  --output marici_toric_rees_cartier_endpoint_comparison_certificate.json
```

The self-contained Python 3 checker uses only the standard library and passes **32,428 exact assertions**. It reconstructs the native resolution and actual target matrices; checks the six charts and every chart face; verifies the whole Cartier tensor map on all native source generators, with independent excess; checks twelve ordered adjacent overlaps and all 216 chart triple comparisons; verifies every dihedral transport; and checks the Jacobian, all seven boundary valuations, primitive-class detectors, and both excess basis changes.

The polynomial and all-order proofs are given above. The assertion count is an execution statistic, not proof-assistant certification. The preceding full 2,595,690-check run was not claimed as a new run here; the present checker independently reconstructs and checks the portions it uses. No repository file was changed.

### Project inputs

[S1] `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`: target states, incidence coefficients, and localization domains.

[S2] `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`, blob `840258522d45e450e4f1e8bb927d9aae58c75566`: native source and conductor difference.

[S3] `src/ledger/20260814-115 Boundary-Triad Tate Realization and the Multi-Rees Cartier Bicomplex.md`, blob `63da17cb5d641705056c5d5b9bc6f53cda72baf5`: conormal-valued Bockstein, independent Rees directions, and distinction from the full physical correspondence.

Preceding artifact: `marici_completed_normal_dual_comparison.md` and its checker. The source-reconstruction functions in the current executable are retained from that checker; its hash is recorded in the new certificate.

### Primary mathematical references

[M1] Stacks Project, *Blowing up*, tag `01OF`, especially affine charts and projectivity: https://stacks.math.columbia.edu/tag/01OF .

[M2] Stacks Project, *Universal property blowing up*, tag `0806`: https://stacks.math.columbia.edu/tag/0806 .

[M3] Stacks Project, *Hom complexes*, tag `0A8H`: https://stacks.math.columbia.edu/tag/0A8H .

[M4] Stacks Project, *Right adjoint for an effective Cartier divisor*, Lemma 48.14.1, tag `0B4B`: https://stacks.math.columbia.edu/tag/0B4B . The Cartier resolution here is explicitly constructed and retains its line and degree; no identification with the full physical functor is inferred solely from this reference.
