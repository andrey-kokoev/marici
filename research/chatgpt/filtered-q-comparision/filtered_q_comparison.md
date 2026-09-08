# The actual filtered Q comparison and its six-normal connecting class

Date: 2026-09-06  
Repository: `andrey-kokoev/marici`  
Pinned input commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result and category

This calculation constructs the honest support-quotient comparison on the source's full, original-twist loaded hexagon and its supplied target-side extended Cech version. It also constructs a compatible barycentric model containing every mixed flag. It is not a further projection onto top/long-only flags.

The genuine loaded generic quotient has a free rank-one top homology module. Its generator is not the one-dimensional marked roof `q_J` from the preceding discussion. The connecting class of this top generator in the endpoint-relative boundary has exact annihilator equal to the product of the six **short-normal** parameters. Both endpoint cubes are retained before taking the specified quotient.

Consequently, the generic unit has no closed lift to this unlocalized endpoint target. Its six-normal multiple has a unique degree-three lift. There is nevertheless an explicit morphism of obstruction triangles, with the nonzero boundary retained. This is the relevant constructive outcome for a prospective bivariant comparison: its supported source boundary must map to the computed connecting class, rather than being silently set to zero.

The previously constructed logarithmic normal-link pairing preserves this obstruction. It does not remove it. This does not prohibit a logarithmic/Gysin realization with a nonzero supported boundary or a different explicitly specified variance. It does rule out identifying the generic unit with a closed endpoint class in the present unlocalized complex.

## 1. The actual source complexes and coefficient ring

Let D be the nine diagonals of a labelled hexagon. Write S for its six short diagonals and L for its three long diagonals. The coefficient ring is the universal polynomial ring

\[
R=\mathbb Z[X_a,u_a\mid a\in D].
\]

In words: occurrence and normal parameters remain distinct. No normal, occurrence parameter, or integer is inverted. The results also hold after adjoining independent variables or units by a base change preserving the stated divisibility argument; no assertion for arbitrary nonflat coefficient change is made.

For a noncrossing diagonal set F and a subset H of F, use the source generator [F,H], of homological degree

\[
|[F,H]|=3-|F|+|H|.
\]

In words: H records the retained normal circles. In particular every degree-three generator is fully marked, H=F.

The differential is precisely the supplied original-twist differential:

\[
\begin{aligned}
d[F,H]={}&\sum_{a\text{ addable}}(-1)^{\#\{b\in F:b<a\}}X_a[F+a,H]\\
&+(-1)^{3-|F|}\sum_{h\in H}(-1)^{\operatorname{pos}_H(h)}u_h[F,H-h].
\end{aligned}
\]

In words: add a compatible radial label with coefficient X, or remove a normal mark with coefficient u. Positions are numbered from zero. The code checks the square-zero identity on every generator over the polynomial ring, not just at a numerical specialization. This is the formula in [S1].

The actual two endpoint faces are the alternating triangulations v-plus and v-minus of [S2]. Define F-V to be the subcomplex on those two faces, F-B to be the subcomplex of faces containing any short diagonal, and F-K to be the full complex. These are strict subcomplexes because adding diagonals cannot leave the short boundary, and a maximal endpoint face has no addable diagonal.

The resulting exact sequence is

\[
0\longrightarrow A_\partial:=F_B/F_V
\longrightarrow E:=F_K/F_V
\xrightarrow{\pi}Q:=F_K/F_B\longrightarrow0.
\]

In words: keep the complete endpoint-relative target, its boundary subobject, and the genuine generic quotient. Quotienting by F-V is not the same as forgetting which two endpoint cubes were specified.

The complete ranks, in degrees zero through three, are:

| Complex | Ranks |
|---|---|
| F-K | 14, 63, 93, 45 |
| F-V | 2, 6, 6, 2 |
| F-B | 14, 63, 90, 41 |
| E | 12, 57, 87, 43 |
| A-boundary | 12, 57, 84, 39 |
| Q | 0, 0, 3, 4 |

Thus the target uses all 215 loaded generators, including all sixteen endpoint generators, before the prescribed quotients. The generic quotient has seven generators, not three isolated barycentric edges.

## 2. A filtered barycentric comparison that really is a chain map

Take **all** strictly increasing flags of noncrossing faces

\[
F_0\subsetneq\cdots\subsetneq F_k,
\qquad H\subseteq F_0.
\]

In words: a loaded flag retains its initial coefficient face and its marks. Its degree is k plus the number of marks. There are 509 unmarked flags and 973 loaded flag generators.

Deleting the first flag vertex multiplies its coefficient by

\[
\prod_{a\in F_1\setminus F_0}X_a.
\]

In words: this is the source's occurrence transport between the two coefficient faces. Other deletions have only their alternating signs. Normal-mark removal has the tensor sign (-1) to the flag degree, followed by the ordered normal sign and multiplication by u. The differential on a vertex is unaugmented. This agrees with the prior marked edge and triangle identities.

Support is determined by the initial face: a flag is boundary-supported when F-zero already contains a short label. The first deletion moves to a subface of that same closed geometric support. Every other deletion leaves it unchanged. Therefore these are genuine support subcomplexes, and their quotients retain mixed flags such as [top,D,b].

Construct subdivision on a cell [F,H] by summing all saturated flags from F to a triangulation, with their incidence orientations and the same H. The vertex orientation gauges are fixed integrally from the source edge incidence. The checker verifies, on every loaded cell,

\[
d\,\operatorname{sd}=\operatorname{sd}\,d.
\]

In words: subdivision is a chain map over the actual polynomial ring and preserves F-V, F-B, and F-K separately.

Here is an integral proof that it is a filtered equivalence, not merely a map with matching ranks. Filter the subdivisions by their geometric carrier cells. The relative barycentric block over a cell of dimension p is the subdivision of that cell relative to its boundary. The checker cancels only unit incidence entries and verifies that this block has one primitive class in degree p, represented by the subdivision of the cell. It does this for all 45 cells. Adding the normal-mark factor tensors that comparison with its finite free Koszul complex and hence preserves the equivalence. Induction over the finite carrier filtration gives an equivalence on each support subcomplex and each support quotient. This is the standard finite filtered-complex argument; the matrices realizing its hypothesis are checked, rather than assumed [M1].

Accordingly the genuine derived Q comparison is represented by the commuting diagram

\[
\begin{array}{ccccc}
F_B/F_V&\longrightarrow&F_K/F_V&\longrightarrow&Q\\
\downarrow\operatorname{sd}&&\downarrow\operatorname{sd}&&\downarrow\operatorname{sd}\\
B_{\rm bar}/V_{\rm bar}&\longrightarrow&K_{\rm bar}/V_{\rm bar}&\longrightarrow&Q_{\rm bar}.
\end{array}
\]

In words: every vertical arrow is an actual filtered equivalence. No map in this diagram discards a mixed triangle while keeping its boundary.

The earlier identity still implies that the marked one-chain q-J bounds in the ordinary relative quotient. This agrees with, rather than contradicts, the existence of a different loaded top class below. They have different degrees and normal data.

## 3. Compute the genuine loaded generic class

Write t for the top generator, e-i for the unmarked i-th long facet, and h-i for that facet with its normal marked. The seven-generator quotient is

\[
Q_3=Rt\oplus\bigoplus_{i\in L}Rh_i,
\qquad Q_2=\bigoplus_{i\in L}Re_i,
\qquad dt=\sum_{i\in L}X_i e_i,
\qquad dh_i=u_i e_i.
\]

In words: the three marked-long generators and the top generator all occur in degree three. The normal coefficients are not erased.

Put U-L equal to the product of the three long-normal parameters. Then

\[
\vartheta=U_Lt-\sum_{i\in L}X_i\!\left(\prod_{j\in L\setminus\{i\}}u_j\right)h_i.
\]

In words: this polynomial cycle uses no division. Each long-facet differential cancels exactly. The displayed products sometimes written U-L divided by u-i are honest polynomial products, not localizations.

A general top cycle with top coefficient a satisfies

\[
X_i a+u_i b_i=0\quad(i\in L).
\]

In words: u-i must divide a because X-i and u-i are independent, relatively prime variables. The three distinct u-i therefore have product dividing a. Every b-i is then uniquely determined. Since there is no degree four,

\[
H_3(Q)=R\vartheta.
\]

In words: the generic quotient really has a free rank-one top class. This is an R-module generator; its top coefficient is U-L, not one. Its identification with any differently normalized physical `q_Sigma` remains a separate issue. It must not be renamed q-J.

## 4. Compute its exact endpoint-relative connecting class

Let Delta be the product of the six short-normal parameters. Define the full top cycle

\[
\Omega=\sum_{F\text{ noncrossing}}
(-1)^{|F|(|F|+1)/2}
\left(\prod_{a\in F}X_a\right)
\left(\prod_{a\in D\setminus F}u_a\right)[F,F].
\]

In words: use every fully marked face, with its independently retained occurrence and normal coefficients. This is a sum of 45 terms. Its endpoint-relative image Omega-E has 43 terms; the two omitted terms are exactly the fully marked v-plus and v-minus terms of the stated quotient.

Direct cancellation gives

\[
d\Omega=0,
\qquad \pi(\Omega_E)=\Delta\vartheta.
\]

In words: the global top class reaches the six-normal multiple of the generic class, not the generic unit.

This determines **all** possible top lifts. For any degree-three cycle in E, let a be its top coefficient. The equations at each of the nine unmarked facets give X-j a plus u-j times its marked coefficient equal to zero. None of these facets is an endpoint. Thus every u-j divides a. The remaining equations force the coefficients on marked pairs and nonendpoint triangulations recursively. If a is zero, every coefficient is zero; if a is the product of all nine normals times c, the unique solution is c times Omega-E. Consequently

\[
H_3(E)=R\Omega_E,
\qquad H_3(\pi):R\longrightarrow R,
\quad c\longmapsto\Delta c.
\]

In words: the full top-cycle classification is an exact polynomial divisibility statement, not an inference from a finite number of multigrades.

Lift vartheta to F-K by the same four-term formula and put

\[
\beta=d\widetilde\vartheta\in (A_\partial)_2,
\qquad W=\Delta\widetilde\vartheta-\Omega\in (F_B)_3.
\]

In words: beta is its actual boundary; W is an explicitly boundary-supported null-homotopy for its six-normal multiple. Beta has eighteen terms: six short-facet terms and twelve mixed short/long-normal terms. It has no endpoint-supported terms. W has 41 terms, including the two prescribed endpoint top terms; its image in A-boundary has 39 terms.

The identities are

\[
d\beta=0,
\qquad dW=\Delta\beta.
\]

In words: beta is a legitimate connecting cycle, and the displayed W is its polynomial annihilation witness.

The long exact sequence of the strict support quotient and the computed H-three map give the stronger exact statement

\[
\operatorname{Ann}_R[\beta]=(\Delta),
\qquad R[\beta]\cong R/(\Delta)
\subseteq H_2(A_\partial).
\]

In words: the connecting class is nonzero, and no proper subproduct of the six short normals annihilates it. This statement identifies a cyclic submodule, not all of H-two of the boundary. It is normal-parameter torsion, not integer-prime torsion; the abelian group R divided by this monomial ideal is torsion-free.

### Checks at all 64 relevant normal multigrades

In fine X-degree zero and fine normal degree one on the three longs, the exact integral reductions give:

- E has four free classes in degree one and no degree-three class;
- A-boundary has four free classes in degree one and one in degree two;
- Q has one free class in degree three;
- beta is primitive in the remaining degree-two group.

Adding any proper subset of the six short-normal degrees still leaves the corresponding beta multiple nonzero. Adding all six makes it exact and permits the top lift. The checker verifies all 64 cases using unit chain cancellations and tracks the actual beta vector through them. This is a finite control of the polynomial proof, not a replacement for it. These are homogeneous components of a polynomial complex, not substitutions setting variables to one.

## 5. The supplied Cech realization retains the obstruction

On [F,H], the source's Cech summand allows inverse powers of u-a only for a in F minus H. The differential replaces radial X-a by X-a divided by u-a and replaces the normal coefficient u-h by one. Its comparison with the polynomial complex is

\[
\kappa[F,H]=\left(\prod_{a\in F\setminus H}u_a^{-1}\right)[F,H]_{\check C}.
\]

In words: these are local summand denominators, not inversion of all normals in the base. The checker verifies every original and barycentric Cech comparison square and its denominator admissibility.

Every degree-three cell is fully marked, so its coefficient ring remains R and kappa is the identity there. The equation at an unmarked facet in the Cech target is X-i a divided by u-i plus b-i equal to zero in R with u-i inverted, but a and b-i still belong to R. Injectivity of that localization turns this into exactly the same polynomial equation u-i b-i equals minus X-i a. The same argument applies to each higher fully marked face.

It follows that the H-three kernels and the multiplication-by-Delta map are unchanged. By the exact Cech support sequence,

\[
\operatorname{Ann}_R[\kappa\beta]=(\Delta).
\]

In words: the stipulated Cech denominators do not eliminate the obstruction. Claiming that its normal coefficient has become one everywhere would conflate summandwise localizations with a forbidden global base localization.

## 6. An explicit morphism of obstruction triangles

The nonzero boundary must be retained, not declared to vanish. Its minimal algebraic resolution is

\[
A_{\min}=[Rk\xrightarrow{\Delta}Rb],
\qquad |k|=3,\quad |b|=2.
\]

In words: the connecting class has the two-term polynomial resolution associated to its exact annihilator.

Adjoin one degree-three generic lift a with differential b:

\[
(E_{\min})_3=Ra\oplus Rk,
\qquad (E_{\min})_2=Rb,
\qquad da=b,\quad dk=\Delta b.
\]

In words: this is a filtered complex in which the generic generator is relative, with the required nonzero supported boundary. Its quotient by A-min is R in degree three. Its global cycle is Delta times a minus k.

The maps

\[
a\longmapsto\widetilde\vartheta,
\qquad b\longmapsto\beta,
\qquad k\longmapsto W
\]

define a commuting morphism of exact triangles into

\[
A_\partial\longrightarrow E\longrightarrow Q.
\]

In words: the middle chain equation, supported boundary, generic class, and six-normal lift are all implemented by explicit source-target columns. Using the full W first, and adjoining F-V by the identity on the source side, gives the corresponding morphism before endpoint quotienting. Thus the sixteen endpoint generators can be kept literally, rather than reconstructed from their ranks afterward.

This minimal source is an **algebraic obstruction presentation derived from the target**. It is not claimed to be a normalization-provenanced logarithmic source. Using it to claim the full physical comparison would be circular. Its value is that it specifies the exact class and identity an independently derived source must realize.

For a morphism of localization or support triangles, the remaining condition is the nonzero boundary compatibility

\[
\alpha_\partial\bigl(\delta_{\mathcal S}(s)\bigr)=[\beta]
\quad\text{when}\quad
\alpha_Q(s)=[\vartheta].
\]

In words: the actual source connecting class must map to beta. A morphism of triangles does not require beta to be zero. The empty closed-lift fibre below is therefore not a no-go theorem for every bivariant comparison.

## 7. Closed lifts, endpoint framing, and the logarithmic factor

In the ordinary derived R-module category, the specified closed lifting space is

\[
\operatorname{hofib}_{\vartheta}
\left(\operatorname{Map}_{D(R)}(R[3],E)
\longrightarrow\operatorname{Map}_{D(R)}(R[3],Q)\right)=\varnothing.
\]

In words: there is no closed degree-three lift of the generic unit over the unlocalized polynomial ring. Both mapping spaces here are discrete: their higher homotopy groups would require homology above degree three. At Delta times vartheta the lifting space is a point, represented by Omega-E. Any further endpoint-fixed restrictions cannot create a lift when the larger space is already empty.

This is a different problem from the earlier normalized degree-zero coefficient-marking extension. The degree, normal weight, and comparison target have changed. The earlier coefficient-level uniqueness does not imply existence here.

The preceding logarithmic construction supplies the closed degree-two coefficient class

\[
w=\gamma\otimes z,
\qquad \Xi_t(w)=1.
\]

In words: it retains the primitive first normal class and the correctly normalized endpoint unit. The previous endpoint and log checkers were independently rerun.

Tensoring the present support diagram with that factor and then evaluating by Xi-t is a retraction of the coefficient inclusion. In particular,

\[
(1\otimes\Xi_t)(\beta\otimes w)=\beta.
\]

In words: if the tensorized beta were a boundary, beta would also be a boundary. Thus this local log/endpoint factor preserves the connecting obstruction; it cannot silently cure the global support problem. No coherent/Betti category identification is used in this argument: all its tensor products are in the same R-linear coefficient category as the already checked pairing.

The original one-road Morse roof still bounds after the honest generic quotient. A filtered map cannot change that fact by keeping only its top/long edge. The nonzero loaded vartheta above instead uses the complete normal top data. Neither a factor-of-two endpoint correction nor an order-three road average is involved in the six-normal obstruction.

## 8. Symmetry and allowed changes

The full polynomial formulas are covariant under the hexagon's physical D3 relabellings, with simultaneous permutation of occurrence and normal coordinates and ordered-face/mark signs. The checker verifies these equations on every loaded generator. In the top-positive orientation convention, vartheta, Omega, beta, and W are invariant. Tensoring by the source's common orientation character changes the character of these classes together and does not alter the multiplication-by-Delta statement. No conclusion about a separately defined global parity is claimed.

Changing coefficients by globally inverting Delta would make the closed lift possible, but that is expressly outside the unlocalized source model. Pairing a principal support line with its dual, or applying a supported extraordinary operation, is not the same operation as that scalar inversion. Such a construction must still specify its source, shifts, support, and the connecting-class comparison in Section 6. The present calculation does not authorize deleting the six normals, setting them to one, identifying them with each other, or replacing them by a single Rees parameter.

## 9. Reproduction and evidence

The bundle contains the new checker and the two earlier coefficient checkers it imports. Run:

```sh
python check_source_defined_branch_comparison.py --output endpoint_recheck.json
python check_logarithmic_excess.py --output log_recheck.json
python check_filtered_q_comparison.py --output filtered_q_comparison_certificate.json
```

The runs pass 2,966, 5,797, and 11,083 exact assertions respectively. The new run rebuilds all cells and mixed flags; checks the support subcomplexes, subdivision, polynomial and Cech chain maps; proves the hypotheses of the finite filtered subdivision argument by 45 integral relative-block contractions; verifies the full polynomial cycles and annihilator witness; checks D3 covariance; and tracks beta through every one of the 64 normal multigrades.

Arbitrary polynomial-degree conclusions are proved by the explicit coefficient recurrences and divisibility argument above. No proof-assistant verification is claimed. No source repository file was modified.

### Pinned sources

[S1] `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`: all nine labels, 215 generators, original differential, Cech differential, and allowed local denominators. The actual `boundary` function was inspected, not only its printed summary.

[S2] `src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md`: the actual support triple F-V inside F-B inside F-K, both endpoint labels, and the endpoint-relative/generic quotient ranks. The carrier implementation `research/voevodsky/check_two_endpoint_tate_carrier.rs`, blob `0147e2e42dafac0da7289c571cb0331b51338be1`, supplies the labelled hexagon and integral vertex-gauge convention.

[S3] `research/voevodsky/check_d03_normalized_blowdown_counit.py`, blob `0fcbbf37a4f70dc0c2787ad7cb954287b9e97403`: the marked Morse identity. The prior log checker reproduces it and distinguishes the honest relative quotient from the invalid erasure.

[S4] `research/voevodsky/check_d03_descended_yoneda_roof.py`, blob `26a81b87e2cbc025a7cf385f9137462fd28b02da`: the top/long-only test whose absent mixed triangles motivated the current corrected comparison.

[S5] `src/ledger/20260817-392 Physical Realization Is a Recollement Morphism.md`, blob `358bd28fc624f9511f3bfb1e801f19cdaaf765f4`: a physical realization must compare both the generic leg and its nonzero supported connecting data, not use one operation uniformly at both supports.

[M1] Stacks Project, Section 12.24, *Spectral sequences: filtered complexes*, tag `012K`: finite filtration, associated graded, and the filtered-complex comparison framework. The unit contractions implementing the local hypotheses are part of this computation.

Previous artifacts: `logarithmic_excess_comparison.md`, `source_defined_branch_comparison.md`, and their executable checkers. Their limits on raw ringed/logarithmic six-functor identification remain in force.
