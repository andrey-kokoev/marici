# Branch A: the W03 Cartier map retains a nonzero native/occurrence excess component

## Result

The previously constructed opposite-edge conductor map has an exact decomposition

\[
\mathcal G_E^+=\beta\mathcal P+\mathcal E.
\]

The first term carries its primary image. The second term has zero primary image, is a nonzero derived map, and remains nonzero after the correctly source-shifted X03-Cartier operation. Identifying the native 35-circle with beta times the separate occurrence-35 partner deletes precisely this second term from the specified map. It is not a homotopy of the original map.

The full occurrence-map-degree-zero local costalk is computed in an explicit integral basis:

\[
\mathscr H\cong\mathbb Z[\beta](-2)[\mathcal P]
\oplus\mathbb Z[\beta](-3)[\mathcal E]
\oplus\mathbb Z[\beta](-3)[\mathcal R].
\]

The last two summands have zero primary image. The given source map has coordinates (1,1,0) in the grade-three basis (beta P,E,R). This is a coefficient-level identification from the recorded source columns, not a selection by matching a scalar residue.

No physical Delta_J or global support-changing six-functor identification is asserted.

## 1. Coefficients, source resolution, and support

Use

\[
R=\mathbb Z[\beta,X_d:d\in\{02,03,04,13,14,15,24,25,35\}]/(I_-I_+),
\]

\[
I_-=(X_{02},X_{04},X_{24}),\qquad
I_+=(X_{13},X_{15},X_{35}),\qquad A=R/(I_-+I_+).
\]

These are the normalization-sheet relations. The long occurrences remain independent. This is the polynomial normal-graph model with native differential beta X_d after removal of the invertible power-series factors in the fixed-beta physical graph. The extension through beta=0 remains a coefficient calculation.

The target is reconstructed on all 430 states [F,H,e], with H a subset of the noncrossing face F, and e=0 or 1 recording the independent occurrence-35 factor. Its degree is 3-|F|+|H|+e. The differential uses the actual signed radial coefficient X_d, the native coefficient beta X_d, and the separate occurrence coefficient X35.

The full edge

\[
E=\{02,35\}
\]

has endpoints

\[
W_{03}=\{02,03,35\},\qquad W_{25}=\{02,25,35\}.
\]

Its complete packet C_E has 40 states. Quotienting the full 16-state W25 packet gives the 24-state relative packet C_rel. Both original physical vertices V+={13,15,35} and V-={02,04,24} remain in the ambient 430-state target. All maps below have zero values and incoming boundaries at those physical endpoints and zero projection to the actual fourteen-state Q quotient.

Use a free resolution P_A[2] of the conductor module, with ranks 1,6,24,92 in degrees 2,3,4,5. Its unit is p_A, its first generators are e_i, and

\[
d e_i=X_i p_A.
\]

For same-sheet i<j,

\[
d c_{ij}=X_i e_j-X_j e_i.
\]

For opposite-sheet i,j, the ordered mixed relation has differential X_i e_j. There are six same-sheet and eighteen mixed first relations.

For completeness, the resolution can be continued using alternating words of nonempty exterior blocks from the two sheets. The differential applies the Koszul differential to the first block; if that block becomes empty it is removed. Adjacent blocks belong to opposite sheets. The differential squares to zero: the same-block terms cancel by exterior signs, and any cross-block term has a mixed-sheet product.

Exactness over the integral long/beta coefficient ring does not require a field argument. As a module over that coefficient ring, decompose every coefficient into its constant, positive-sheet, and negative-sheet parts. For each fixed tail word and permitted preceding sheet, the resulting summand is a shifted augmented positive Koszul complex of the three polynomial variables on that sheet. Its degree-zero target is the sheet's augmentation ideal. These summands are exact. The sole remaining constant term is the augmentation A. This also establishes the relevance of all 92 second relations, rather than assuming that d squared equals zero implies a resolution.

The target ends in degree four. Thus degree-zero maps require all equations through source degree five; map homotopies have components only on the source unit and first generators. No later part of the resolution contributes to this calculation.

## 2. Retain both endpoint normals and both 35 factors

Write

\[
x=X_{03},\quad v=X_{25},\quad y=X_{02},\quad z=X_{35}.
\]

The previously checked signed tensor description of the full edge is

\[
C_E=P_E\otimes M,
\qquad
M=K_R(\beta y,\beta z,z).
\]

The interval/normal factor has

\[
P_{E,1}=R\langle g,h_{03},h_{25}\rangle,
\quad P_{E,0}=R\langle p_{03},p_{25}\rangle,
\]

\[
dg=xp_{03}+vp_{25},\quad
 dh_{03}=\beta xp_{03},\quad dh_{25}=\beta vp_{25}.
\]

The common degree-one generators are a,b,k, with

\[
da=\beta y,\qquad db=\beta z,\qquad dk=z.
\]

Here a is native 02, b is native 35, and k is the distinct occurrence-35 partner.

Define the full-edge cycle

\[
\xi=h_{03}+h_{25}-\beta g,
\qquad d\xi=0.
\]

It contains both endpoint terms. Its image after the relative quotient is

\[
\zeta=h_{03}-\beta g.
\]

In the native bases,

\[
\xi\otimes ab=
\beta[E,E,0]-[W_{03},W_{03},0]-[W_{25},W_{25},0]=L_E.
\]

The tensor orientation is g=-[E,empty,0]; moving h03 or h25 past the native 02 mark supplies the minus sign on the fully marked vertices.

The source-defined positive conductor map is therefore

\[
\mathcal G_E^+(p_A)=\beta z\,\xi\otimes a,
\]

\[
\mathcal G_E^+(e_i)=X_i\,\xi\otimes ab\quad(i\in\{13,15,35\}),
\]

with zero values on negative-sheet generators and all first relations. The full source equations, including the 92 next relations, are verified.

## 3. Split the native/occurrence excess without inverting beta

Set

\[
\eta=b-\beta k,\qquad d\eta=0.
\]

Then

\[
M\cong K_R(\beta y,z)\otimes\Lambda(\eta).
\]

This is an invertible polynomial exterior-basis change, not a quasi-isomorphism inferred from ranks. In the order (a,k,eta),

\[
a\wedge k\wedge\eta=-a\wedge b\wedge k.
\]

The ordered determinant is -1. No beta or occurrence factor is cancelled. The checker exports the complete eight-by-eight basis change and its inverse and checks every tensor differential.

Projection onto eta-degree zero gives an idempotent chain map. Written in the old basis,

\[
\Pi_0(a)=a,\quad \Pi_0(k)=k,\quad \Pi_0(b)=\beta k.
\]

It extends over the full edge and over all 430 states. It preserves face support but does not fix the endpoint normal bases pointwise: a native 35 mark is sent to its occurrence partner, and a state carrying both is sent to zero. It must not be substituted for an endpoint-frame-preserving equivalence.

## 4. Three explicit local supported classes

Define P by

\[
\mathcal P(p_A)=z\,\xi\otimes a,
\quad
\mathcal P(e_i)=X_i\,\xi\otimes ak\quad(i\in I_+),
\]

and zero on the negative generators and all relations.

Define E by

\[
\mathcal E(p_A)=0,
\quad
\mathcal E(e_i)=X_i\,\xi\otimes a\eta\quad(i\in I_+),
\]

and zero otherwise. Each positive Xi annihilates y, so the generator-image differential is zero. Same-sheet source relations cancel by commutativity, and opposite-sheet products vanish.

Since ab=a eta+beta ak, the original map satisfies the literal identity

\[
\mathcal G_E^+=\beta\mathcal P+\mathcal E.
\]

There is no comparison homotopy omitted from this equality.

The third map R has zero unit value, agrees with E on e13 and e15, and is zero on e35 and all negative generators. It has the two nonzero relation columns

\[
\mathcal R(c_{i,35})=X_i\,\xi\otimes abk,
\qquad i=13,15.
\]

All other first-relation columns are zero. Their differential is

\[
d(X_i\xi\otimes abk)=-zX_i\xi\otimes a\eta.
\]

This is exactly R applied to Xi e35-z ei. The 92 next compatibility equations hold. Thus this third zero-primary map depends on actual source-relation homotopies.

The full native matrices contain 12,18,18 polynomial terms for P,E,R. The twelve-term original G+ is beta P+E after the two occurrence-partner terms cancel in each generator column.

Projection onto eta-degree zero gives

\[
\Pi_0\mathcal P=\mathcal P,
\qquad
\Pi_0\mathcal E=\Pi_0\mathcal R=0,
\]

\[
\Pi_0\mathcal G_E^+=\beta\mathcal P.
\]

The primary unit image is unchanged. The discarded map is precisely E.

## 5. Complete integral local classification

Fix occurrence-map degree zero and regulator-normal grade g, where beta and every native normal carry regulator weight one and the occurrence partner carries weight zero.

For a source generator s with occurrence weight w_s and target state [F,H,e], the coefficient exponents are forced:

\[
\alpha_X=w_s+\sum_{a\in F}\epsilon_a-\sum_{a\in H}\epsilon_a-e\epsilon_{35},
\qquad
\alpha_\beta=g-|H|.
\]

A coefficient exists exactly when these exponents are nonnegative and the monomial survives the mixed-sheet ideal. Hence each homogeneous map component has a finite integral matrix, with no polynomial-degree cutoff.

The complete Hom calculations on the 40-state edge are:

| g | Hom degrees (+1,0,-1) | Differential ranks | H0 rank |
|---|---|---|---|
| 0 | (0,1,5) | (0,1) | 0 |
| 1 | (1,14,47) | (1,13) | 0 |
| 2 | (5,50,133) | (5,44) | 1 |
| 3 | (9,78,177) | (9,66) | 3 |
| 4 | (9,78,177) | (9,66) | 3 |

In grade two, the homotopy-boundary columns together with P have determinant -1 in the integral free-coordinate cycle basis. In grade three, the homotopy-boundary columns together with beta P,E,R have determinant +1. These are explicit unimodular bases, not rational rank tests.

No target has more than three native marks. Multiplication by beta identifies all of these cochain bases and differentials for successive grades once g is at least three. The grade-two generator maps to the primitive beta P coordinate in grade three. Thus

\[
\mathscr H\cong\Lambda(-2)[\mathcal P]
\oplus\Lambda(-3)[\mathcal E]
\oplus\Lambda(-3)[\mathcal R],
\qquad \Lambda=\mathbb Z[\beta].
\]

The primary of P is nonzero with exact conductor annihilator. After relative projection and projection onto zeta it is z a in M1. The conductor-linear functional

\[
\ell(v)=\beta[z]v_a+\beta[y]v_b+[y]v_k
\]

kills every boundary and has value beta on z a. Its target is the polynomial long/beta coefficient ring. Every conductor generator annihilates the primary through the displayed source map; conversely this functional detects every coefficient with nonzero conductor augmentation. Therefore no nonzero polynomial in beta kills this primary. The local primary kernel is exactly the two free summands generated by E and R.

## 6. An independent nonvanishing test for the discarded map

Specialize to beta=1, x=0, and set the other four short variables to zero, retaining

\[
B_0=\mathbb Z[y,z]/(yz).
\]

First take the actual relative quotient, then project onto the zeta/eta component. In the resulting signed four-state packet, the common differential is

\[
da=-y p,\qquad dk=-z p,\qquad d(ak)=z a-y k.
\]

The source retains p_A,e35, with de35=z p_A. Define a functional on map cochains by

\[
\ell_\eta(F)=[z]F(e_{35})_a+[y]F(e_{35})_k+[y]F(p_A).
\]

For an arbitrary map homotopy, write its relevant values as H(p_A)=A a+B k and H(e35)=C ak. The three contributions to the functional on delta H are

\[
(C_0+A_0),\qquad -C_0,\qquad -A_0.
\]

Their sum is zero. Nonconstant coefficients contribute only conductor order at least two, so this proves the assertion for every polynomial homotopy, not only for a finite coefficient test.

For the discarded map,

\[
\mathcal E(p_A)=0,\qquad \mathcal E(e_{35})=z a,
\qquad\ell_\eta(\mathcal E)=1.
\]

Hence E is not a boundary. In particular the original G+ and its collapsed beta P have the same primary and physical endpoint/Q values but are not homotopic as the specified resolved-source maps.

## 7. Apply the correct W03 Cartier functor to all three maps

The coefficient x=X03 is regular on R and A. The same signed Cartier Hom functor is applied to the source and the relative target. Its counit and purity maps are reconstructed, including the dual conormal line:

\[
i_x^!(A[2])\simeq A/(x)[1]\otimes\mathfrak n_x^\vee.
\]

The target is C_rel reduced modulo x, shifted by -1 and tensored with the same normal line. This is the source change already required by the preceding Cartier calculation. It is not a claim that the original A[2] lifts through the target counit.

The induced decomposition is still literal:

\[
i_x^!\mathcal G_E^+=\beta i_x^!\mathcal P+i_x^!\mathcal E.
\]

The split projection commutes with the complete Cartier Hom differential, the counit, and the purity comparison.

Recomputing the entire homogeneous Hom complex in the relative divisor model gives:

| g | Hom degrees (+1,0,-1) | Differential ranks | H0 rank | Image from the full-edge classes |
|---|---|---|---|---|
| 2 | (4,34,64) | (4,26) | 4 | 1 |
| 3 | (6,48,86) | (6,36) | 6 | 3 |

In grade three the transported beta P,E,R, together with the six homotopy-boundary columns, have a 9-by-9 minor of determinant +1 in the integral cycle-coordinate basis. Thus their image is a saturated rank-three submodule. All three classes survive, including both zero-primary excess maps. Additional relative-divisor classes exist; no claim that this image exhausts the six-dimensional group is made.

The elementary detector in the preceding section also proves directly that i_x^!E is nonzero, after its common purity shift and normal line are retained.

## 8. Opposite-endpoint and physical-reflection data

For each of P,E,R, the checker retains the complete W25 component F25, the relative component F_rel, and the connecting map kappa25. Every source column satisfies

\[
d_{25}F_{25}+\kappa_{25}F_{\mathrm{rel}}=F_{25}d_{P_A}.
\]

The full cycle xi includes h25. Only after taking the actual relative quotient does it become zeta. Neither the W25 term nor its connecting equation is replaced by zero in the full-edge calculation.

The physical reflection v maps to 3-v modulo six. It sends the 35 occurrence correction to the 04 correction, sends the retained long corner to its reflected 03 corner, and carries W25 to the corresponding W14 endpoint. Both 430-state targets are reconstructed. Every reflected basis map satisfies its source equations, and reflecting twice is the identity. The reflected selected sum is the source's negative-sheet representative on the reflected edge:

\[
f_3\mathcal G_E^+=\beta f_3\mathcal P+f_3\mathcal E.
\]

No new endpoint scalar or averaging is introduced. The determinant -1 in the common normal-basis change remains recorded. In the unnormalized physical graph, eta corresponds to the closed vector b_phys-lambda35 k; the formal unit relating it to the displayed eta must remain with its normal line.

## 9. Consequence and limitation

The relative Cartier operation does not justify discarding the native/occurrence excess. The recorded conductor map has a specified nonzero coordinate in it, and that coordinate is invisible on the primary. A comparison matching only the primary, endpoint values, or a scalar residue cannot identify the two maps.

The next spatial/Gysin comparison must therefore specify its action on this excess summand and on the source-relation components. It may supply an additional projection or quotient, but such an operation is not a homotopy of the map constructed here.

This result does not manufacture a generic Q component. It does not identify any local class with the physical Delta_J. It supplies a concrete source-level test for a proposed reciprocal/Gysin realization.

## Reproduction and certificate

Run:

```sh
python branch_a_w03_native_occurrence_excess_checker.py --output branch_a_w03_native_occurrence_excess_certificate.json
```

The checker uses only the Python standard library. It reads no companion files and makes no network requests. The certificate includes the full local source and target matrices, normal-basis change and inverse, three resolved maps, original map, W25 components, Cartier Hom matrices, reflected maps, all homogeneous Hom matrices, integral kernel coordinates, unit minors, and class detectors.

This run verified 20,918 counted exact identities. It includes reconstruction checks on both 430-state corrected targets; it does not add assertion totals from previous executions. A separate clean-directory replay with a different hash seed reproduced the certificate byte-for-byte.

## Source references

Project repository andrey-kokoev/marici, pinned commit d1947b67a60d3e88ba77f4ca60ea02c2a306ee61:

- `research/voevodsky/check_absolute_unlocalized_support_pc.rs`: actual face enumeration, differential, and cellular orientation.
- `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`: two-sheet coefficient algebra and conductor.
- `src/ledger/20260814-96 Factorization-Marked Normal-Crossing Span and the Pair-Local Relation Obstruction.md`: independent W03 marking.
- `src/ledger/20260814-131 D03 Cartier Edge Purity and the Scoped PC Promotion.md`: radial/native separation, retained excess, and scoped Cartier comparison.
- `src/ledger/20260814-140 Physical-Reflection Naturality of the D03 Edge Purity.md`: physical reflection and normal-line conventions.

Mathematical references: Stacks Project tags 0621 (Koszul functoriality), 0A8H (Hom differential), 064B (maps from projective resolutions), 0A74 (closed-immersion right adjoint), and 0B4B (Cartier duality). W. Frank Moore, *Cohomology of Fiber Products of Local Rings*, arXiv:0704.3631, gives the alternating-block resolution framework; the integral polynomial-base exactness used here is supplied by the decomposition in Section 1.
