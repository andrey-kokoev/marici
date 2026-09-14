# Branch B: filtered normalization and the relative-operation interface

Date: 2026-09-08.

## Result and limits

This note constructs the normalization-facing coefficient leg requested in the attached Branch B brief. It does not identify a new geometric collar with the native physical source.

The main additional calculation is that each endpoint operation module is free over the relative algebra on 56 explicitly graded seeds. This gives a complete classification of its maps to an augmentation module and an explicit obstruction to reversing its normalization quotient. Nontrivial endpoint operations are compatible with a trivial generic action through a quotient; they are incompatible with an operation-preserving section of that quotient. These are different questions.

A canonical derived-Hom interface puts the complete normalization diagram, its row filtration, its total comparison and its endpoint fibre into an operation-module category. It reverses arrows and retains the original coefficient diagram as a separate component. It does not assert that Yoneda operators already act on every unmodified physical chain complex.

For the free relative algebra, an explicit length-one bimodule resolution computes the equivariant mapping complex. The full labelled symmetry acts on that resolution by the universal noncommutative derivative. In particular, it retains the decomposable reflection terms. This supplies existence and uniqueness complexes for an actual collar square once its native attaching maps are specified.

The current data do not specify those complete attaching maps and their actions. Thus the full physical lifting space is not assigned either emptiness or nonemptiness. The normalization/operation coefficient diagram constructed here is inhabited. A more restrictive comparison requiring a section of the exterior endpoint quotient is proved empty.

## 1. Rings, degrees and categories

Use the rings and labels fixed by the input calculations:

\[
S=C[x_1,x_2,x_3,y_1,y_2,y_3],\quad
U=S[a,b]/(ab),\quad
B=S/(x_i y_j),\quad I=I_+\oplus I_-,\quad C=B/I.
\]

The positive labels are `(13,15,35)` and the negative labels are `(02,04,24)`. Here C retains the independently admitted spectator parameters. Physical short Rees parameters, long occurrences, long normals, regulator parameters and orientation lines are not identified with each other. Extending the spectator ring to compare with Branch A must use the declared coefficient map; its regulator beta is not the parameter introduced below.

Original coefficient complexes have homological differential of degree minus one. Operation modules use cohomological degree q, corresponding to original homological degree minus q. A categorical shift satisfies X[k]^q=X^{q+k}. The endpoint word-module reindexing below is specified explicitly, rather than relying on an unstated module-shift sign.

Let e_i be the six short occurrence weights. An occurrence coefficient has internal weight +e_i. Its Ext operator has cohomological degree one and internal weight -e_i. For a relative generator indexed by a mixed subset J, its cohomological degree is |J| and its internal weight is -sum_{i in J} e_i. We also report the positive occurrence multiplicity vector when describing words; that vector is not the internal weight of an Ext operation.

The bookkeeping parameter lambda has homological degree zero, short occurrence weight zero, and row-filtration weight one. It is not physical Rees time. All relative operators have row-filtration weight zero.

The coefficient category is the unbounded derived category of multigraded B-modules, with a two-step row filtration or its graded B[lambda]-Rees model. Existing stalk localizations are retained as modules. The category is not restricted to perfect objects. The action-facing category is the derived category of left dg R-modules over C, or over C[lambda] for the row-Rees diagram. Both categories also retain the specified support labels and semilinear dihedral transports.

## 2. Explicit filtered normalization diagram

### 2.1 The two rows

The auxiliary exact sequence is

\[
0\longrightarrow U\longrightarrow U/(b)\oplus U/(a)
\xrightarrow{\epsilon_+-\epsilon_-}S_{\rm or}\longrightarrow0.
\]

The native exact sequence is

\[
0\longrightarrow B\longrightarrow N_B:=B/I_-\oplus B/I_+
\xrightarrow{\epsilon_+-\epsilon_-}C_{\rm or}\longrightarrow0.
\]

Derive the coefficient change U to B in both rows. Let M be the derived normalization term and L the derived conductor term. Their chosen free-resolution models have zero internal differential after this coefficient change:

\[
M_n=B^2\ (n\ge0),\qquad L_0=B_{\rm or},\quad L_n=B^2\ (n\ge1).
\]

The row comparison c:M to L is

\[
c_0=(1,-1),\qquad
c_n=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\quad(n\ge1).
\]

These are derived maps between the two actual periodic resolutions, not scalar identities assigned after computing their ranks.

For completeness, auxiliary internal weights in the normalization resolution on U/(b) are k(a+b) in degree 2k and k(a+b)+b in degree 2k+1. Exchange a and b for the other branch. The conductor resolution has weights k(a+b) in degree 2k and k(a+b)+a or k(a+b)+b in its two degree-(2k+1) generators. This makes c homogeneous. Auxiliary weights are separate from the six native occurrence weights.

Set

\[
\mathcal T_n=M_n\oplus L_{n+1},\qquad
 d_{\mathcal T}(m,l)=(0,c_nm).
\]

Thus the conductor row L[-1] is a subcomplex and the normalization row M is its quotient. The native total K_B has N_B in homological degree zero and C_or in degree minus one.

The total comparison alpha:T to K_B evaluates the degree-zero normalization terms in their native branch quotients, sends L_0=B to C, and sends positive auxiliary resolution degrees to zero. It is B-linear, homogeneous, filtration preserving, and dihedrally covariant. Its underlying total map is a quasi-isomorphism.

### 2.2 Retain its complete row defect

The row kernels are

\[
(D_M)_0=I_-\oplus I_+,\quad (D_L)_0=I,\qquad
(D_M)_n=(D_L)_n=B^2\quad(n\ge1).
\]

On degree zero, the comparison is (y,x) maps to y-x; on positive degrees it is the displayed matrix J. Its inverse gives the integral homotopy h from the conductor defect to the normalization defect. It obeys

\[
dh+hd=1.
\]

This homotopy raises row filtration by one. It is not a filtered contraction.

Assign row weight one to D_M and zero to D_L. The Rees defect has

\[
d_\lambda(m,l)=(0,\lambda\bar c m),\qquad
d_\lambda h+h d_\lambda=\lambda\,1.
\]

Its homology is

\[
H_{-1}=I\otimes_B B[\lambda]/(\lambda),\qquad
H_n=(B[\lambda]/(\lambda))^2\quad(n\ge0).
\]

All occurrence and auxiliary weights on these terms are inherited from the explicit row models. Specializing lambda to one gives the total equivalence. The associated grade at lambda zero retains both defect rows. A zero filtered deformation group is not inferred from the unfiltered contraction.

### 2.3 The relative quotient and roads are separate data

The endpoint construction retains the normalization quotient resolution and the complete norm/triangle/augmentation road resolution. At auxiliary resolution degree zero its chain modules have ranks (1,4,5,1) in homological degrees (3,2,1,0). Positive auxiliary resolution degree n retains the corresponding two conductor copies and their complete road windows. Every differential and symmetry matrix is in the retained input checker.

Write p_partial:P_der to P_nat for that comparison. It has fibre

\[
D\simeq I_{\rm or}[1]\oplus\bigoplus_{n\ge2}B^2[n].
\]

This fibre is not the contractible total conductor-kernel defect. A free B[2] is a retract. A uniform tensor functor with nonzero coefficient K retains K[2]; a uniform coefficient dual into nonzero K retains K[-2]. The assertion is about these functors, or exact functors not killing the unit retract. It is not a claim about every arbitrary exact functor that might annihilate B.

The complete filtered normalization object in this note is the diagram consisting of the two row arrows, their totals, alpha, its defect and homotopy, the lambda-Rees diagram, and the quotient-and-road comparison and fibre. None is reconstructed from the homology of another.

## 3. The typed operation interface

### 3.1 Chain representatives, rather than an action inferred from ranks

Let P_C be the native B-free resolution of C on alternating words of nonempty exterior blocks. Its differential deletes labels from the first block and multiplies by their occurrence variables.

For each label i define T_i on P_C by deletion from the last exterior block, with sign

\[
(-1)^{\ell(w)-\ell(A_{\rm last})+\operatorname{pos}_{A_{\rm last}}(i)}.
\]

The operator has cohomological degree one and internal weight -e_i. The chain identities are

\[
dT_i+T_id=0,\qquad T_i^2=0,\qquad
T_iT_j+T_jT_i=0
\]

for i,j in the same sheet. There is no imposed mixed-sheet anticommutation. These formulas construct a C-dg-algebra map

\[
\mathcal E_B\longrightarrow\operatorname{End}_B(P_C).
\]

After composition with the augmentation P_C to C, the ordered operator words are the complete dual resolution basis. Hence the map induces the established Yoneda algebra isomorphism. This gives chain representatives for the relative subalgebra as nested compositions, not only an abstract cohomology algebra.

### 3.2 The canonical functor and its variance

For a B-complex X define

\[
\mathbf K(X)=R\operatorname{Hom}_B(X,C).
\]

It carries a left E_B action by postcomposition into a resolution of C, and hence a left R action. The functor is contravariant in X. A B-linear map X to Y gives an R-linear map K(Y) to K(X). A specified homotopy gives the corresponding homogeneous module homotopy, with the ordinary dg-Hom signs.

Apply this functor to the entire filtered normalization diagram, not separately to its homology modules. Over the bookkeeping ring use RHom_{B[lambda]}(-,C[lambda]); retain both row weights, now dualized. The total equivalence remains an equivalence; the filtration defect is not declared zero. In particular,

\[
\mathbf K(D)\simeq\mathbf K(I_{\rm or})[-1]
\times\prod_{n\ge2}C^2[-n].
\]

The free endpoint retract becomes a nonzero augmentation-module retract C[-2]. Equivariant forgetful functors detect zero objects, so an operation enhancement cannot make that defect disappear.

This interface has two components: the original support-labelled B-diagram, and its contravariant conductor-operation diagram. They must be retained together. K need not detect noncoherent punctured terms; for instance RHom_B(B[X_i^{-1}],C)=0. Thus replacing the whole physical diagram by K(X) would discard the previously established punctured closure data.

The action inherited through auxiliary operations and H is different from this native derived-Hom action. On an inherited H-module all positive R-operations act by zero. It cannot be substituted for the native endpoint action. Transporting the total equivalence does not identify the two actions on individual normalization rows.

### 3.3 An explicit operation-cohomology normalization row

Put J_sigma=E_B E_sigma^{>0}, the left ideal of nonempty words ending on sheet sigma. The native normalization modules have

\[
\operatorname{Ext}_B^*(B/I_-,C)=E_B/J_+,
\qquad
\operatorname{Ext}_B^*(B/I_+,C)=E_B/J_-.
\]

The induced operation-cohomology row is exact:

\[
0\longrightarrow E_B
\xrightarrow{(q_+,-q_-)}(E_B/J_+)\oplus(E_B/J_-)
\xrightarrow{\epsilon+\epsilon}C\longrightarrow0.
\]

Every positive-degree word ends on exactly one sheet, so the first map is injective and is an isomorphism onto the positive-degree middle part. In degree zero its matrix is (1,-1), with cokernel C. All maps are R-linear.

This explicitly exhibits the mixed operations in the rows even though the total coefficient output is the augmentation module. It is the cohomology row of the resolved diagram, not a replacement for its filtered chain complex. No rowwise splitting follows.

### 3.4 Choice of interface

Modules over R, retaining their E_B provenance, are sufficient for this coefficient leg. The E_B-H bimodule defined by rho makes the exterior restriction precise; positive R acts trivially on H. The ordinary kernel ideal of rho is not substituted for R.

The ambient right H-coaction does not restrict to J_sigma: the coaction of xi_i contains 1 tensor xi_i, and 1 is not in that ideal. A comodule formulation therefore requires an additional specified comodule or completed dual, not a relabelling of the present action. A cofree R-coaction on the R-free presentation below is possible, but its augmentation quotient is not colinear: the coproduct of g produces the term g tensor w that the quotient kills. Module linearity and colinearity are distinct tests.

## 4. Both endpoint modules and the 56-seed theorem

Use the actual endpoint coefficient modules

\[
M_\sigma^q=\operatorname{Ext}_B^q(I_\sigma,C)
=(J_\sigma)^{q+1},\qquad q\ge0.
\]

Their differentials are zero in this operation model. Left multiplication is the specified action under the prior word-resolution identification. Tensor the source endpoint/polarity line without dropping its grading. The word has internal weight minus its label multiplicity. The degree reindexing here is part of this explicit identification; categorical shifts used later also carry their module signs.

Choose the exterior tail order with the opposite sheet first and the endpoint's own sheet last. Define W_sigma to have basis

\[
u_Ou_P,\qquad O\subseteq S_{-\sigma},\quad
\varnothing\ne P\subseteq S_\sigma.
\]

Its degree is |O|+|P|-1 and its internal weight is -sum_{i in O union P}e_i. There are 56 seeds, with counts

\[
(3,12,19,15,6,1)
\]

in degrees zero through five.

The multiplication map is an isomorphism of graded left R-modules:

\[
R\otimes_C W_\sigma\xrightarrow{\cong}M_\sigma.
\]

Proof: use the established Hopf-module factorization E_B=R tensor Lambda(C^6) with this exterior tail order. The ordered product section of the exterior coalgebra is a right-comodule section for any chosen ordering. It is convolution-invertible because the coalgebra is connected, so changing the exterior order preserves the Hopf-module factorization. Multiplying an ordered tail by a same-sheet endpoint generator only changes its final own-sheet exterior block. Consequently the left ideal generated by that sheet is exactly the sum of tails with nonempty own-sheet part. Their independence and spanning follow from the factorization. The proof applies over the retained integral spectator ring. The checker independently performs unit-pivot decompositions through total word degree six on both endpoint modules.

The exterior normalization map is therefore

\[
\pi_\sigma:M_\sigma\longrightarrow(W_\sigma)_\epsilon,
\qquad \pi_\sigma(r\otimes w)=\epsilon_R(r)w.
\]

It is R-linear, with exact kernel R^+M_sigma. Moreover

\[
C\otimes_R^L M_\sigma\simeq W_\sigma.
\]

There are no extra derived resolution-length Tor terms in this formula because M_sigma is induced-free. This does not erase its internal grading or say that any physical conductor operation equals these coinvariants.

### 4.1 Forward normalization and reverse selection have different answers

The forward normalization above is an operation-linear quotient. Its nonzero kernel does not obstruct that forward map.

No nonzero augmentation module can have an operation-preserving section into M_sigma with the corresponding quotient fixed. A generator g acts injectively on T(V) tensor W_sigma, whereas it acts by zero on an augmentation module. In particular a putative image of a seed would have to be simultaneously nonzero and annihilated by g.

For the original C-linear seed section, the first explicit defects are

\[
r_{ij}\xi_i=\xi_i\eta_j\xi_i\ne0,\qquad
r_{ij}\eta_j=\eta_j\xi_i\eta_j\ne0.
\]

Each has relative operation degree two and endpoint input/output degrees zero and two. Its full occurrence multiplicity is 2e_i+e_j or e_i+2e_j; its Ext internal weight is the negative of that vector. Its filtration degree is zero, and its support is the occurrence conductor. These zero-differential module classes cannot be removed by a homotopy. The same argument excludes a derived section, since it would split the induced operation modules on cohomology.

The 49 relative generators all act; the remaining forty are not products of the nine quadratics inside the relative subalgebra. The seed theorem retains their independent action types while deriving every product action from multiplication.

### 4.2 Exact maps to an augmentation target

For any C-complex G with augmentation action,

\[
R\operatorname{Hom}_R(M_\sigma,G_\epsilon)
\simeq R\operatorname{Hom}_C(W_\sigma,G).
\]

Thus 56 graded seed maps per endpoint determine every operation-linear comparison to G. In particular a nontrivial endpoint action can map to a trivial generic action; all R^+ directions then map into the kernel of the readout.

This statement is in the conductor operation category. It does not identify an arbitrary C-linear seed map with a B-linear physical endpoint arrow. Actual geometric shifts, line factors, supports and B-linearity must be supplied through the physical coefficient diagram.

## 5. Generic Q: four different objects

### 5.1 Bare coefficient complex

Write the seven-state complex, up to a uniform placement shift, as

\[
Q_{a+1}=BT\oplus\bigoplus_{l\in L}BM_l,\qquad
Q_a=\bigoplus_{l\in L}BE_l,
\]

\[
dT=\sum_l X_lE_l,\qquad dM_l=u_lE_l.
\]

It has amplitude one and is free over B. None of its seven basis states carries a short occurrence weight. The long coefficients and any prescribed long localizations remain independent of the short occurrence variables. Choosing a=3 displays the generic coefficient class in homological degree four; this uniform placement is not an identification of Branch C's Koszul source with a one-state source.

Every relative generator has degree at least two, so a strict degree-preserving B-linear action on the bare complex must annihilate R^+. More strongly, its internal degree is a nonzero negative short weight, whereas End_B(Q) has no coefficient in such a weight. The homogeneous derived action space is therefore contractible at the augmentation action. This also eliminates its higher action homotopies in that specified fine-graded B-linear category.

If internal weights are discarded, the degree argument still forces the strict action and the component of its derived equivalence class to be augmentation. It does not alone prove contractibility of the space of actions: higher homotopies of maps from the free generators into End(Q) must be retained. If differential operators that are only C-linear are admitted, their additional internal-weight maps also need a separate analysis.

The generic coefficient line has the same augmentation action. The polynomial cycle

\[
\omega=U_LT-\sum_{l\in L}X_l\prod_{j\in L\setminus\{l\}}u_j\,M_l,
\qquad U_L=\prod_{l\in L}u_l,
\]

is retained with all its long coefficients. Its closure and all six labelled transport equations are checked. A nonzero value of this one class supplies no nontrivial action on endpoints.

### 5.2 Conductor operation target

The canonical contravariant interface assigns K(Q)=RHom_B(Q,C), not Q itself. Its finite C-projective model has amplitude one and augmentation action for the same grading reasons. The derived restriction C tensor_B^L Q is a third object; finite duality over C relates it to K(Q). No bare B-coefficient data are silently replaced by this specialization.

The classification in Section 4.2 applies to K(Q), or to a separately declared C-complex specialization. To compare with the raw physical Q one must use the corresponding B-map and correct variance.

### 5.3 Branch C's resolved source and marked class

The attached brief supplies a primitive degree-four bare-Q trace. It does not supply an R-action on its full Koszul source or all native endpoint/normal/Cech attaching matrices. Keep the trace in its supplied degree and support. Do not replace its source by the bare generic coefficient line.

For a source P_C with specified action and a degree-zero placement of its trace f_C:P_C to G, the first requirements are

\[
dh_g=f_C\theta_{P_C}(g)-\theta_G(g)f_C
\]

for each actual relative generator g, with solvability tested in the permitted Hom complex. For augmentation G this becomes d h_g=f_C theta_{P_C}(g). Homotopies have degree |g|-1 and internal weight -nu_g. A source resolution can carry these operations even though the bare target cannot. An actual map or its comparison complex must be tested, not inferred from its scalar primitive.

### 5.4 Mapping spaces

An R-module structure induces maps between appropriately shifted mapping spaces; a degree-two operator is not an unshifted path automorphism. The underlying mapping space is obtained from the degree-zero connective part of its derived Hom complex. Its higher homotopies are H^{-n} of that Hom complex. A bare Q action, a source action, and an action on a mapping space are consequently separate assertions.

## 6. Exact obstruction complex for R-linearity

The free algebra R=T_C(V) has the explicit bimodule resolution

\[
0\longrightarrow R\otimes_CV\otimes_CR
\xrightarrow{\partial}R\otimes_CR
\xrightarrow{\mu}R\longrightarrow0,
\]

\[
\partial(a\otimes g\otimes b)=ag\otimes b-a\otimes gb.
\]

For any word in the free generators, its splittings into a left and a right word form a path. Consecutive cuts give the columns of partial. The augmented path complex is integrally exact. This is an all-word proof, with no finiteness or characteristic-zero assumption.

With derived C-Hom where necessary, it gives

\[
R\operatorname{Hom}_R(X,Y)
\simeq\operatorname{fib}\left(
R\operatorname{Hom}_C(X,Y)
\xrightarrow{\delta}
R\operatorname{Hom}_C(V\otimes_C X,Y)\right).
\]

For a homogeneous cochain f of degree k,

\[
\delta(f)(g,m)=f(gm)-(-1)^{k|g|}g f(m).
\]

For a closed degree-zero f, the obstruction to lifting that fixed map to an R-linear derived map is

\[
[\delta(f)]\in H^0\mathbb B(X,Y),\qquad
\mathbb B(X,Y)=R\operatorname{Hom}_C(V\otimes X,Y).
\]

The first nine components have operation degree two; the forty others have degrees three through six. In fixed total occurrence degree zero,

\[
H^k\mathbb B(X,Y)_{0}
=\prod_{g}H^{k+|g|}\!R\operatorname{Hom}_C(X,Y)_{-\nu_g}.
\]

Include filtration-preserving, support-preserving, and line-valued restrictions in this Hom before computing cohomology.

If the class vanishes, choices over the fixed underlying map form a torsor for Omega Map_C(V tensor X,Y). At a chosen lift,

\[
\pi_n\mathscr L_f=H^{-n-1}\mathbb B(X,Y)\quad(n\ge0),
\]

where pi-zero is interpreted as a torsor. Freeness imposes no additional multiplication relations among the 49 generators. This does not remove coefficient, Cech, filtration, or symmetry obstruction groups.

The product homotopies are explicit:

\[
h_{ab}=h_a A_b+(-1)^{|a|}B_a h_b,
\qquad dh_a=fA_a-B_af.
\]

Their differentials telescope to the defect for the product. The same formula on an arbitrary word is independent of parenthesization by associativity of composition. It supplies the required coherent multiplicative extension in the module mapping problem. It is not a claim that geometric Cech faces have already been filled.

## 7. Full labelled symmetry, including relation complexes

The six occurrence permutations are induced by the hexagon maps v maps to v+2k and v maps to 1-v+2k. On E_B substitute those labels into words and restore the exterior signs within each same-sheet block. On every relative generator, expand this actual substituted word in R. On products, use multiplication of the full expansions.

For the fixed reflection,

\[
s(\xi_1)=\eta_2,\quad s(\xi_2)=\eta_1,\quad s(\xi_3)=\eta_3,
\]

with the inverse exchanges on the eta generators. In the example from the input,

\[
s(g)=-g+[r_{21},r_{12}].
\]

This acts on both endpoint modules by the actual word substitutions and swaps their endpoint labels. In the free endpoint basis it acts on the R factor by the full nonlinear expression and on W by the oriented opposite-then-own exterior permutation. All 294 generator images and their endpoint actions are exported.

A signed action on V alone does not make the length-one bimodule resolution equivariant. Use its canonical realization as the module of noncommutative differentials. For any label transport s,

\[
s(d_{\rm nc}g)=d_{\rm nc}(s(g)),\qquad
 d_{\rm nc}(ab)=(d_{\rm nc}a)b+a(d_{\rm nc}b).
\]

Thus the reflected relation generator is

\[
-d_{\rm nc}g+(d_{\rm nc}r_{21})r_{12}
+r_{21}(d_{\rm nc}r_{12})
-(d_{\rm nc}r_{12})r_{21}
-r_{12}(d_{\rm nc}r_{21}).
\]

The extra four terms are mandatory. The identity

\[
\partial d_{\rm nc}(w)=w\otimes1-1\otimes w
\]

proves covariance of the bimodule differential. The noncommutative chain rule proves all group composition laws, including reflection squared. This defines the full symmetry on the mapping obstruction complex, not merely its indecomposable ranks. The checker tests every generator under every pair of the six transports.

For a homogeneous map space, apply the transported actions to both source and target, and to these differential-generator terms. The strict coefficient model can equivalently use the semilinear crossed product, whose multiplication is

\[
(r[g])(r'[h])=r\,g(r')[gh].
\]

The group acts on the spectator coefficients by their prescribed labelled transport. For derived coherent symmetry use the homotopy fixed points of the full diagram and mapping complexes, not averaging by six. Group cohomology may introduce further obstructions; it is not set to zero by freeness of R.

All row objects carry their already specified semilinear label action. Lambda is fixed. Conductor orientation changes sign under sheet exchange; normal/endpoint orientation factors are transported rather than fitted. This fixes the coefficient convention. The physical polarity character remains a source line supplied by Branches A/C and must be matched to this convention; the operation algebra alone does not choose it.

## 8. The operation-equivariant collar pullback

### 8.1 Objects and arrows that are already constructed

The following table fixes the coefficient types. Every displayed comparison is homogeneous of degree zero after the object placements above. An occurrence multidegree on a coefficient is retained, not replaced by zero.

| Item | Source and target | Variance and degree | Row/support/action |
|---|---|---|---|
| Auxiliary row | M to L | Covariant; h degree 0, occurrence degree 0 | Normalization to conductor row; whole native coefficient base; before K no raw Yoneda action is inferred |
| Total comparison | T to K_B | Covariant; h degree 0, occurrence degree 0 | Filtered map; equivalence only after forgetting the row filtration |
| Total contraction | conductor defect to normalization defect | Homological +1, occurrence degree 0 | Raises row filtration by 1; not an admissible filtered equivalence |
| Rees homotopy | same defect rows over B[lambda] | Homological +1, occurrence degree 0 | d_lambda h+h d_lambda=lambda; support V(lambda) retained |
| Endpoint comparison | P_der to P_nat | Covariant; h degree 0, occurrence degree 0 | Full roads and endpoints; fibre D retained |
| Operation functor | a B-arrow X to Y gives K(Y) to K(X) | Contravariant; same map degree with dg signs | Native postcomposition E and R action; dual row labels retained |
| Endpoint operation maps | M_sigma to W_sigma,epsilon | Covariant in the operation category; cohomological 0 | Occurrence weight 0; row 0; conductor support; R-linear quotient |
| Bare generic marking | B[4] to the uniformly placed Q | Covariant; h degree 0; short occurrence degree 0 | Bare-Q support; augmentation action; all independent long weights retained |
| Dual generic marking | K(Q) to C[-4] | Contravariant image of the preceding arrow | Augmentation R-modules; not the native Koszul trace source |
| Branch A two-grade output | Hom_B(C[2],Y_A) | Contravariant source operations | Right E and R action; conductor and X35 conormal lines both retained |

The complete native normal/Cech attachment is not one of the maps provided by these operations. To instantiate a physical pullback it must supply its source/target B-complexes, actual map degree and occurrence weight, filtration action, support restrictions and endpoint boundary homotopies. The generic primitive alone supplies none of those matrices. A zero matrix is not inserted for an absent connector.

### 8.2 Precise enhancement space

Let J be the actual collar-diagram index, including normalization rows, their totals and endpoint comparison, both endpoint objects, the complete normal/Cech attachment, and the generic Q map. Let J_0 contain the fixed boundary data. For any supplied underlying conductor-facing diagram D:J^op to D(C[lambda]), define its R-enhancements with the prescribed boundary actions by the homotopy fibre of

\[
\operatorname{Fun}(J^{op},\operatorname{Mod}_{R[\lambda]})^\simeq
\longrightarrow
\operatorname{Fun}(J^{op},D(C[\lambda]))^\simeq
\times^h_{\operatorname{Fun}(J_0^{op},D(C[\lambda]))^\simeq}
\operatorname{Fun}(J_0^{op},\operatorname{Mod}_{R[\lambda]})^\simeq.
\]

The basepoint includes the supplied total-kernel comparison and generic marking, not just the objects' isomorphism types. Use the full labelled group action described in Section 7. The original B-diagram remains in the enhancement as a separate fixed datum, linked by K. This avoids claiming that K is faithful on the complete punctured target.

For the known normalization subdiagram, the construction of K supplies a point. The full native J-diagram has not been supplied, so its enhancement space is a well-defined interface awaiting those actual arrows, not a claimed inhabited physical moduli space.

### 8.3 The lifting square and all uniqueness groups

After fixing a variance and all actual actions, any one collar square has the form

\[
\begin{matrix}
A&\xrightarrow{a}&X\\
\downarrow b&&\downarrow c\\
Y&\xrightarrow{p}&Z.
\end{matrix}
\]

Here the requested additional map is F:X to Y with Fa=b and pF=c, together with their homotopies. A denotes the complete fixed boundary datum, not only a scalar endpoint. In a particular collar it includes the endpoint, normal/Cech and generic constraints according to the actual index. All four arrows have degree zero after the supplied placements and preserve the declared internal, filtration and support conditions.

Its exact lifting space is

\[
\mathscr P_{\mathcal R}=
\operatorname{hofib}_{(b,c,H)}\!\left(
\operatorname{Map}_{R}(X,Y)\longrightarrow
\operatorname{Map}_{R}(A,Y)
\times^h_{\operatorname{Map}_{R}(A,Z)}
\operatorname{Map}_{R}(X,Z)\right).
\]

The datum H is the specified compatibility between pb and ca. The relative control complex is

\[
\mathbb L=R\operatorname{Hom}_{R}(\operatorname{cofib}a,\operatorname{fib}p).
\]

Compute it using Section 6, the actual Cech resolution and the prescribed row/occurrence degree. Its H^1 contains the obstruction to solving this fixed square. If the obstruction vanishes, the set of components of solutions is an H^0(L)-torsor, and the based higher groups are H^{-n}(L), n at least one. Contractibility requires all these groups to vanish; it is not inferred from a primitive trace.

With labelled symmetry replace the complete global control complex by its homotopy fixed points. The spectral sequence H^p(D_3,H^q L) converging to the cohomology of L^{hD_3} keeps the additional group-coherence obstructions. No integer is inverted.

Thus all higher groups forced by the free algebra have an explicit two-column model; unresolved physical coefficient groups and overlaps remain genuine inputs to that model.

## 9. Branch A and Branch C compatibility

### 9.1 Branch A's actual two-grade output

The fetched Branch A normalization calculation has, in homological notation,

\[
Y_A=Ce_0[2]\oplus(C\otimes\mathcal L_{35})e_1[3].
\]

The source is its complete conductor resolution P_C[2]. The occurrence line L35 has weight +e_35. The two normalized readout columns differ by the primitive Ext^1 class xi35 paired with this line. The scalar coordinate alone loses that distinction.

Retaining the full source resolution gives the right operation module

\[
R\operatorname{Hom}_B(C[2],Y_A)
\simeq E_B\oplus(E_B[1]\otimes\mathcal L_{35}).
\]

The cohomological shift puts xi35 in the second summand in map degree zero, matching the actual conormal readout column. Its positive relative descendants are explicit:

\[
\xi_{35}r_{35,j}=\xi_{35}\eta_j\xi_{35}\ne0.
\]

After the readout shifts this is a degree-two mapping operation, with the paired internal line retained. It is not a new degree-zero scalar residue.

The adjacent two raw C-lines admit no strict positive R action in their own two-degree model. Their resolved mapping object above does detect R. These statements concern different objects. In particular, keeping two output ranks is not a substitute for retaining the source resolution and its precomposition action.

For the specific tangential duality readout, relative duality gives RHom_B(C,D_{B/C})=C in degree zero with the prescribed orientation convention. Its scalar evaluation therefore annihilates the positive R operation outputs. This statement is about that trace: the resolved scalar conductor object RHom_B(C,C)=E_B is not itself an augmentation line.

The full Branch A dualizing triangle remains

\[
C_{\rm or}\longrightarrow(\omega_+\oplus\omega_-)[3]
\longrightarrow D_{B/C}\longrightarrow C_{\rm or}[1],
\]

with its nonzero Gysin attachment. The scalar tangential functional has two essential ambient entries; deleting its conormal entry leaves the actual coefficient defect z times the volume. Nothing here splits this triangle.

Derived duality turns each recorded trace into a reversed map with its full chain data. Its resolved Hom complexes have the natural right or left E actions furnished by composition. It does not automatically give a strict raw R action on D(T). To assert that stronger structure, supply a dg map R to the appropriate endomorphism algebra and solve its intertwining defects as in Section 6.

Equivariance alone does not require that both trace grades be retained: a quotient can still be R-linear. Retaining the known nonzero conormal/source-relation trace difference does require both the conormal output and its resolved source action. Their mere degree-zero ranks are insufficient.

The right module in the displayed readout can be converted to a left one using the graded antipode when needed; the conversion must include its signs. It cannot be silently inserted into a left-module pullback with unchanged arrow variance.

### 9.2 Branch C's required interface

Its primitive bare-Q class is accepted as supplied in the task. The action on the generic coefficient and bare complex is augmentation. Its actual endpoint source must additionally provide: a resolved coefficient action (or a native B-map inducing it under K); the 56 seed images per endpoint with all physical shifts and normal lines; the images of all positive relative-operation descendants in the normal/Cech fibre; the homotopies for all 49 generator intertwining equations; and their Cech and labelled-symmetry comparisons. The product homotopies are then supplied by the free-algebra formula, not independent fitted cells.

A forward quotient may discard relative descendants from the generic readout while retaining them in the normal/endpoint fibre. An equivalence factoring through the exterior quotient while preserving the endpoint modules is impossible. A collar source carrying those fibre terms is not ruled out.

The brief does not include the complete maps needed to evaluate the physical L in Section 8. It is therefore not enough to determine whether that final native pullback is empty, contractible, or has automorphisms. This limitation is different from the explicit empty section problem of Section 4.1.

## 10. Nonlinear coherence and minimal changes

The coefficient operation comparison already detects a failure of replacing full symmetry by signed action on indecomposables: [r21,r12] acts nontrivially on both endpoint types. Ordinary cellular homology of the coefficient space, without its loop multiplication, cannot encode this equation.

A strict dg module over T(V) does encode it. The current tests therefore do not force a new physical Whitehead product or a space-level loop action. E_1 modules, with dg or A-infinity models for their maps and Cech descent, are sufficient for the operation-facing coefficient interface. A later loop-space enhancement requires a specified map from chains on that actual loop space and a check of its higher structure; an isomorphism of graded loop homology with R alone does not provide it.

The minimal correction depends on the intended arrow:

* For a forward normalization/readout, keep its R-linear quotient and the kernel R^+M. No enlargement of bare Q is forced.
* For operation-faithful transport of endpoint data, use the already constructed R-free envelopes R tensor W_sigma, or an equivalent resolved native source carrying them. A finite exterior endpoint module alone cannot receive an operation-preserving section.
* For a full physical collar, retain the existing support-changing normal/Cech object and supply its actual maps into this interface. The free envelopes and the bimodule relation generators resolve coefficient operations; they are not licensed additions of physical carrier cells.
* A row-dependent operation can avoid the uniform-retract argument only by changing the arrow or mixing its rows. The known total contraction does that, but fails the retained row filtration. A new admissible row-dependent map must keep the lambda defect and satisfy the displayed filtered action and symmetry equations; it is not supplied by renaming the old contraction.

## Verification and provenance

Run from the extracted bundle:

```sh
python check_marici_operation_collar_interface_20260908.py
```

The run passed 179,709 exact assertions. It includes both endpoint free-basis calculations through total word degree six, all 294 relative generator transports, full universal-derivative covariance and group laws, eighteen first endpoint obstruction witnesses with complete weights, Branch A's conormal descendants, the actual normalization/Rees/endpoint formulas, bare-Q cycle and relabelling equations, the operation-cohomology normalization row, and all-word intertwiner formulas in the stated finite window.

The all-degree statements follow from the Hopf-module factorization, the alternating-word chain operators, the word-path bimodule resolution, and the noncommutative chain rule. They are not extrapolated from bounded checks. The executable does not assign a value to the missing native physical attachment.

Two complete prerequisite scripts were independently rerun from their supplied copies: the derived-normalization checker passed 59,808 assertions; the relative-operation checker passed 22,479. All source script SHA-256 hashes and finite transport expansions are recorded in the new certificate. No repository files were modified, and this is not proof-assistant certification.

Retained input sources:

1. Attached task `Pasted text(1).txt`, dated by upload 2026-09-08; required established inputs and physical interface.
2. `marici_derived_normalization_diagram_20260907.md` and its checker: the two complete rows, their lambda defect, endpoint fibre, support and grading qualifications.
3. `marici_all_degree_conductor_comparison_20260907.md`: conductor comparison and chain-level operation restrictions.
4. `marici_relative_operation_fibre_20260908.md` and its checker: relative Hopf algebra, primitive generators, endpoint actions and full dihedral formulas.
5. `research/chatgpt/branch_a_full_normalization_duality_and_two_grade_trace_proof.md`, read at GitHub commit `538594ab137c4459e11a5ee9d8e0bf6e1dfd1bf0`: actual two-grade trace and nonsplit dualizing triangle.
6. `research/chatgpt/branch_a_tangential_duality_scalar_pairing_proof.md`, same commit: two-term tangential dualizing functional, trace pairings, and precise scalar loss.

Framework references used, separately from the new calculations:

* Stacks Project, tag `0FQ2`, Hom complexes and dg modules: actions through dg endomorphisms, composition, right/left variance and signs.
* Stacks Project, tag `09LF`, Derived Hom: exact derived module functors and functorial morphisms.
* F. Vylegzhanin, *Loop homology of moment-angle complexes in the flag case*, arXiv `2403.18450v3`, Theorem 1.1 and Proposition 3.7: the already established relative-algebra and Hopf-module factorization used in the endpoint-free-module proof.

The new 56-seed calculation and explicit operation-collar obstruction interface are constructions in this note. They are not claims that the cited sources have constructed Marici's physical collar.
