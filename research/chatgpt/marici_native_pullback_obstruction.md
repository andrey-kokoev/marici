# Branch C: native derived-pullback target and its first endpoint obstruction

Date: 2026-09-08

## Decision and scope

Decision 3 applies to the canonical **native derived-pullback target** constructed in this note. This target is genuinely a complex of modules over the native node ring. It is neither the conductor coefficient object nor the derived coinduced target of the already-falsified ambient comparison.

The endpoint's primitive underlying coefficient class exists. It does not extend to a normalized native branch-source morphism. The first failure occurs in resolution degree two, where each mixed relation would require a primitive, nonzero Tor class to be a boundary. A two-row matrix and an integral detector prove this for all possible replacement maps in the prescribed frame.

This is not a nonexistence theorem for every native supported target. In particular it does not test an independently specified native action on D35. It falsifies the direct derived-pullback route before the outer-Q-symmetry and three-layer gates.

The binding previous result, concerning the literal outer ambient Hom and its canonical reverse restriction, is retained and is not recomputed here.

## 1. Rings, source, target, and variance

Keep the spectator ring from the physical change-of-rings input:

\[
C=\mathbb Z[X_{D03},X_{D14},X_{D25},t_0,\ldots,t_5,
 u_{D03},u_{D14},u_{D25}],\qquad A=C[X_0,\ldots,X_5].
\]

In words: all long occurrences, short-Rees parameters and long normals remain independent. The short-normal relation is still u_i=t_i X_i. Extra already-declared spectator or regulator variables can be adjoined without changing the integral detector below.

Set

\[
I_E=(X_0,X_2,X_4),\quad I_O=(X_1,X_3,X_5),\quad
\mathfrak B=A/(I_EI_O),\quad
\mathfrak B_+=A/I_E,\quad \mathfrak B_-=A/I_O.
\]

In words: the plus sheet carries odd occurrences and the minus sheet carries even occurrences. Write q for the ring map A to the native node, and epsilon for its conductor augmentation to C.

For each of the four prescribed underlying channels T, retain

\[
P_T=K_A(X_0,\ldots,X_5,p_T),\qquad p_T=\prod_{i\in T}t_i,
\]

\[
D_\sigma=R\operatorname{Hom}_A(K_A(t_{I_\sigma}),A),\quad
\widetilde L_\sigma=A\ell_\sigma,\quad
I_+=(1,3,5),\ I_-=(0,2,4),
\]

\[
G_{\sigma,T}=(P_T\otimes_A D_\sigma\otimes_A\widetilde L_\sigma)
\langle\lambda_T\rangle[-4],\qquad
\lambda_T=\sum_\ell e_{u_\ell}-\sum_{i=0}^5e_{X_i}-\sum_{i\in T}e_{t_i}.
\]

In words: G is exactly the complete, normalized framed endpoint source. It retains the seven coefficient equations, ordered occurrence determinant, product-Cartier generator, endpoint duality shift and external conormal line. The line has internal degree equal to the sum of its three endpoint Rees degrees. The two excess-channel labels remain distinct spectator lines. No Euler evaluation is used.

The endpoint complex V_sigma is the supplied eight-state subcomplex. Its coefficients on a state are

\[
(V_\sigma)_{[v_\sigma,H]}
=A[(t_iX_i)^{-1}:i\in I_\sigma\setminus H].
\]

In words: only the unmarked endpoint coordinates admit the original normal inverses. A factorization such as 1/X_i=t_i/u_i is legal only inside such a stalk. No occurrence inverse is admitted on the base.

Let

\[
\mathcal H_\sigma=R\operatorname{Hom}_A(G_{\sigma,T},V_\sigma).
\]

The new native-linear candidate is

\[
\boxed{Y_\sigma^{\mathrm{pb}}=
\mathfrak B\otimes_A^L\mathcal H_\sigma.}
\]

In words: use left-derived extension of scalars, not right-derived coinduction. Since G is a bounded finite-free complex, evaluation and base change give a canonical equivalent presentation

\[
Y_\sigma^{\mathrm{pb}}
\simeq R\operatorname{Hom}_{\mathfrak B}
\left(\mathfrak B\otimes_A^L G_{\sigma,T},
      \mathfrak B\otimes_A^L V_\sigma\right).
\]

In words: both the physical coefficient source and the actual endpoint target are transported to the native ring. The B-action is multiplication on every base-changed target stalk. These arrows have cohomological and internal degree zero; Hom is contravariant in its source and covariant in its target. The perfectness used here is only that of G, not of the native node over itself or its endpoint bar resolution. Standard Hom and derived tensor conventions are [M1, M2].

Each original localization term is flat over A, so its displayed base change is its genuine derived base change. Passing to B does not discard the derived occurrence relations: the full Koszul factor remains in the source-Hom construction. The Tor calculation below records its effect before any homology truncation.

The support is contained in the conductor occurrence support together with the existing product-Cartier and endpoint normal support. There is no new physical support stratum or additional target cell.

## 2. An explicit model with its full native action

Use the established, line-retaining occurrence-purity projection from the retained change-of-rings input. It supplies an A-linear quasi-isomorphism

\[
\mathcal H_\sigma\xrightarrow{\simeq}W_\sigma.
\]

In words: W is the complete conductor-valued complex that still contains the product-Cartier dual, the endpoint normal Koszul block, and all endpoint/determinant frames. It is not replaced by a scalar. This earlier projection is an input; this note does not count its earlier checks as new verification.

The important point is what happens **after** left-derived native base change. Resolve the conductor over A by the entire six-equation Koszul complex. This gives

\[
Y_\sigma^{\mathrm{pb}}\simeq
K_{\mathfrak B}(X_0,\ldots,X_5)\otimes_C W_\sigma.
\]

In words: the new target retains every Tor direction of the derived native conductor. Replacing this Koszul factor by its zeroth homology would change the target and remove precisely the obstruction computed below.

Write k_i for its degree-one homological generators. Its differential and B-action are

\[
d k_i=\bar X_i,\qquad
\bar b\,(\bar a k_I\otimes w)=\overline{ba}\,k_I\otimes w.
\]

In words: all 64 exterior states are B-free before taking cohomology. Native mixed products vanish in their coefficients, not by deleting the exterior states. Multiplication by X_i is homotopic to zero through exterior multiplication by k_i, but is not the zero chain operator. The compatibility of these annihilator homotopies is the next nontrivial condition.

### The precise endpoint frame

Retain all occurrence weights while fixing the spectator/Rees/long-normal frame of the prescribed primitive endpoint. In the purity quotient, let z be zero or one according as the product-Cartier generator is absent or present, and let H index the dual-normal subset. The required short-Rees exponent vector of a coefficient is

\[
-(1-z)\sum_{i\in T}e_{t_i}-\sum_{i\in H}e_{t_i}.
\]

In words: the fully marked endpoint stalk has no allowable negative short-Rees exponents. Thus the only legal row has z=1 and H empty. Its coefficient is U_L, the product of the three long normals, on the actual fully marked endpoint state.

This is a calculation from the source and target degrees, not a choice to discard other rows. The checker enumerates all sixteen possible rows for every T and endpoint, and repeats this test on all 64 central short-Rees faces. It never sets U_L to one or inverts it. The symbol w_sigma below denotes the primitive vector in this fixed line, with coefficient U_L in the original target basis.

Consequently the endpoint-frame restriction of Y is exactly the native six-variable Koszul complex tensored with that retained line. The argument applies separately to all channels and both external excess labels.

## 3. Tor is computed before the endpoint map

For a fixed nonnegative occurrence weight alpha, a basis of the native Koszul complex consists of

\[
X^{\alpha-\mathbf 1_I}k_I
\]

whenever the exponent vector is nonnegative and its coefficient is a legal pure-sheet monomial in B. In words: a coefficient involving both an even and an odd variable is zero, but no mixed exterior wedge is deleted.

The homological ranks are

\[
\operatorname{rank}_C\operatorname{Tor}^A_n(\mathfrak B,C)
=(1,9,18,15,6,1)_n.
\]

In words: there are nine first relation classes and all their higher syzygy classes. In positive degree n the classes occur in squarefree occurrence weight n+1. A nonempty even support U together with a nonempty odd support V contributes one primitive class in degree |U|+|V|-1.

This result is computed directly from K_B, not imported as a rank assumption. The checker reduces all 729 weights with entries zero, one or two using signed-unit chain contractions. All non-squarefree weights are acyclic.

For the all-exponent assertion, suppose alpha_j is at least two. If j is absent from I, restore k_j, divide the residual coefficient by X_j, and use the usual exterior insertion sign; if j is already present, assign zero. The division is a monomial divisibility operation, not localization: the coefficient still contains X_j afterwards. It therefore remains in the same legal pure-sheet coefficient domain. This homotopy satisfies

\[
dh+hd=1.
\]

In words: any weight with a repeated exponent is contractible. The 64 squarefree calculations plus this argument cover arbitrary occurrence exponents, with no bounded-polynomial extrapolation.

The rank pattern resembles the degrees of the 49 mixed primitives, but this note does not identify the Tor groups with the relative Hopf algebra or equate its products with Tor products.

### The derived branch source is not silently truncated

There is a different, canonical derived source:

\[
Lq^*\mathfrak B_\sigma
=\mathfrak B\otimes_A^L\mathfrak B_\sigma
\simeq K_{\mathfrak B}(J_\sigma),
\qquad J_+=I_E,\quad J_-=I_O.
\]

In words: left base change of the ambient branch quotient retains an eight-state Koszul complex. It is not the underived native module B_sigma appearing in the requested outer Hom.

The exterior inclusion of its killed-coordinate generators into the six-coordinate Koszul target gives a primitive native chain map. It sends the source's mixed cycle X_o a_e to X_o k_e and therefore retains its nonzero Tor image. The checker verifies this map on all eight states and all nine mixed cycles per endpoint.

This map cannot be used as a map out of B_sigma. Its factorization through the augmentation to B_sigma would kill all positive homology of the source, including those nine nonzero target images. The next section tests exactly this missing factorization. Replacing B_sigma by the derived branch source would change the operation-bearing endpoint problem and would need its own native operation comparison; no such identification is asserted.

## 4. The native primitive test and its first unsolvable equation

The augmentation K_B to C induces a normalization map

\[
\epsilon_Y:Y_\sigma^{\mathrm{pb}}\longrightarrow W_\sigma.
\]

In words: this is an actual comparison to the established framed endpoint coefficient object, not a declaration that the two targets are equal.

A successful primitive-preserving b from any physical endpoint source with its prescribed degree-zero witness would have to produce an element

\[
\widetilde m_\sigma\in
H^0R\operatorname{Hom}_{\mathfrak B}
(\mathfrak B_\sigma,Y_\sigma^{\mathrm{pb}})
\]

whose image under epsilon_Y is the endpoint augmentation times w_sigma. This is a necessary condition on b independent of how its remaining operation generators are presented.

### The actual native branch resolution starts as follows

Let e be a coordinate killed on the endpoint sheet, and o a coordinate surviving there. The B-free branch resolution has generators

\[
d a_e=X_e\,1,\qquad d z_{o,e}=X_o a_e.
\]

In words: the mixed relation X_o X_e=0 produces a genuine second syzygy. There are three first generators and twelve second generators: three internal-sheet Koszul relations and nine mixed relations. The displayed skeleton is exact through degree one. Its syzygies are generated by the ordinary Koszul relations on the killed-coordinate polynomial ring and the three positive surviving-coordinate ideals annihilating each killed coordinate.

No higher resolution generator is needed to detect the obstruction, because any full chain map must already solve its equations on these columns.

### A single labelled pair is decisive

For the plus endpoint choose e=4 and o=3. In the source's diagonal labels these are 04 and 35. Thus

\[
d a_{04}=X_{04}\,1,\qquad
 d z_{35,04}=X_{35}a_{04}.
\]

In words: this is the specific mixed pair named in the Q-symmetry task, now tested as a native source relation. It is not an identification of its Tor cycle with the shifted operation bracket.

Primitive normalization and the first chain equation force, in the prescribed internal frame,

\[
F_0(1)=w_+,\qquad F_1(a_{04})=k_{04}\otimes w_+.
\]

In words: there is only one legal occurrence-weight-one target generator with this boundary. The full frame calculation in Section 2 accounts for the remaining normal factors.

The next equation would be

\[
dF_2(z_{35,04})=X_{35}k_{04}\otimes w_+.
\]

But in this occurrence weight the complete target is

\[
C\langle k_{35}\wedge k_{04}\rangle
\xrightarrow{\binom{1}{-1}}
C\langle X_{35}k_{04},X_{04}k_{35}\rangle,
\]

with no degree-zero coefficient term, since the mixed monomial vanishes in B.

In words: every possible second-stage filler is a multiple of the one displayed mixed wedge. Its boundary always contains both terms.

The required coefficient equation is

\[
a\binom{1}{-1}=\binom{1}{0}.
\]

The detector is

\[
\ell=(1,1),\qquad
\ell\binom{1}{-1}=0,\qquad
\ell\binom{1}{0}=1.
\]

In words: every boundary has detector value zero and the required image has value one. There is no integral or polynomial solution. The contradiction persists after any extension of spectator coefficients in which the primitive endpoint unit remains nonzero.

This is not the previous ambient bar equation. The Hom is now genuinely native and its target carries the entire derived pullback. The obstruction is a retained Tor class of that target, not the ambient exactness of a native operation.

## 5. All replacements and all nine mixed blocks

For either endpoint the same calculation gives

\[
\kappa_{e,o}=[X_o k_e]=[X_e k_o]
\in H_1(K_{\mathfrak B}(X_0,\ldots,X_5)).
\]

In words: these are nine independently weighted primitive classes. Each detector annihilates every target boundary in its complete occurrence weight.

The first endpoint obstruction is represented on the nine source relations by

\[
z_{o,e}\longmapsto\kappa_{e,o}\otimes w_\sigma.
\]

In words: its nine mixed coordinates are all primitive. It has infinite additive order, not order two or three. These are relation-obstruction coordinates; no action of the Hopf generators on this failed endpoint witness is being fabricated.

Equivalently this is the first obstruction from the negative Postnikov layers of Y to lifting the normalized H0 endpoint map. It lies in the appropriate internally framed component of

\[
\operatorname{Ext}^2_{\mathfrak B}
(\mathfrak B_\sigma,H^{-1}(Y_\sigma^{\mathrm{pb}})).
\]

In words: the degree-one Tor layer prevents a homotopy-coherent action of the branch quotient on the chosen primitive vector. The explicit resolution equation supplies its nonzero detector without assuming a collapse of a spectral sequence.

As an independent finite check, the code constructs **every homogeneous degree-zero map** on the source skeleton through degree two. There are sixteen possible coefficients: one on the unit, three on the first generators, and twelve on the second generators. The necessary chain equations have rank sixteen with unit pivots. Appending primitive normalization gives 28 equations with an explicit integral inconsistency detector. This is done separately for both endpoints.

The stored detector combines four equations to produce a zero left-hand side and right-hand side one. Thus no different first homotopy, second filler, polynomial coefficient, or higher comparison can repair the failed normalization in this fixed frame. A homotopy-coherent morphism in the derived category is represented by a chain map from a projective resolution; its restriction to this skeleton would contradict that detector [M1].

The normalized relative lift space

\[
\operatorname{hofib}_{m_\sigma w_\sigma}
\left(
\operatorname{Map}_{\mathfrak B}(\mathfrak B_\sigma,Y_\sigma^{\mathrm{pb}})
\longrightarrow
\operatorname{Map}_{\mathfrak B}(\mathfrak B_\sigma,W_\sigma)
\right)
\]

is empty. In words: this expresses the failed lifting problem; it does not adjoin a physical cone to force a solution.

## 6. Labels, normal faces, and symmetry

Rotation of short labels is i to i+2 modulo six; use the endpoint-exchanging reflection i to 1-i. The latter exchanges 04 and 35. Both preserve the native mixed ideal and exchange the endpoint branch ideals as required.

They act on the target Koszul factor by the corresponding permutation of the k_i and the induced exterior signs. On the complete target, W and all determinant/excess lines are transported with their endpoint labels. The obstruction transforms as

\[
g(\kappa_{e,o}\otimes w_\sigma)
=\kappa_{g(e),g(o)}\otimes g(w_\sigma).
\]

In words: reflection exchanges the two obstruction problems. An orientation change only changes the primitive detector by a unit. It cannot change nonzero to zero. No physical reflection parity is selected.

The code verifies all six label actions, their composition equations on all 64 Koszul wedges, and the full B-linearity of the differential. It separately checks the endpoint frame on all 64 short-Rees faces for every T and endpoint. The obstruction matrix has no Rees coefficient; it is unchanged on those faces whenever the prescribed endpoint line is retained.

The independent excess label is tensored through by the identity. It is not identified with a Koszul k_i, a Tor class, or a scalar. No regulator or occurrence unit is inverted.

## 7. Why this blocks the requested operation and Q-symmetry tests

The operation-preserving b requested in Part I would first have to send the physical primitive witness to a normalized class in the native endpoint Hom. No such class exists for Y-pb. Consequently there is no input for its nine primitive mixed-operation intertwiner equations. This is earlier than a possible failure of those operation equations, and is sufficient to falsify this candidate b.

A full B-action on a coefficient complex is not, on its own, an action of Ext_B(C,C) on that coefficient complex. Such an operation action needs its actual Yoneda variance or a chain-level module comparison. None is inferred here merely from the existence of native multiplication.

No vector fields on a substitute associative algebra are introduced. No operators X04 or X35 on an unprovided physical Q-manifold, no Q-commuting bracket, and no three-layer cyclic map are certified by this test. The conditional Part II and Part III gates have not been reached for this candidate.

This result does not rule out an outer Q-symmetry realization after a different, successfully constructed native endpoint comparison. Nor does it reprove the binding ambient-forward no-go.

## 8. Minimal requirement on a different native target

The problem is now more specific than asking for an arbitrary native action. A different target Y-prime with a primitive vector y must supply actual, source-defined maps satisfying

\[
dH_e=X_e y,\qquad dJ_{o,e}=X_o H_e
\]

for the killed and surviving branch labels, with the corresponding same-sheet and higher relations.

In words: the first annihilator homotopies must admit their native mixed-relation comparisons. In Y-pb the second right-hand sides are the nonzero classes just computed.

Any proposed native supported trace out of Y-pb must therefore have a controlled effect on these nine Tor classes. It cannot be declared an equivalence while removing them. Passing to the conductor coefficient object would remove this obstruction, but would also change the specified coefficient target; it is not performed in this note. Adding a cone or an arbitrary filler is not a physical construction.

A target such as D35 is a genuinely different test. It requires the actual native action and the physical-source mate of its operation variance. The present result supplies no obstruction to all such alternatives and no successful comparison to them.

## 9. Reproduction and exact verification scope

Run:

```sh
python check_marici_native_pullback_obstruction.py \
  --output marici_native_pullback_obstruction_certificate.json
```

The standalone standard-library checker executes **31,028 new assertions**. It imports no prior checker and includes no inherited assertion counts.

Its computations include:

- all 729 native Koszul weights with exponents zero, one or two, comprising 1,936 complete coefficient columns;
- explicit contractions for every non-squarefree weight and the complete squarefree Tor profile;
- the actual branch-resolution skeleton and its homogeneous exactness through degree one, with 614 columns per endpoint across the same 729 weights;
- the two eight-state derived branch-source maps, with their nonzero Tor images retained;
- both sixteen-unknown affine primitive systems and their integral inconsistency rows;
- all eighteen first mixed-relation blocks and their primitive detectors;
- native module-linearity, all six labelled transformations and exterior composition signs;
- the precise endpoint-purity frame on all 64 central short-Rees faces for each prescribed underlying T and endpoint.

A second run from a different working directory with PYTHONHASHSEED=37 reproduced the certificate byte for byte. The all-degree impossibility follows from the explicit low-degree detector and the proved frame reduction, not from finite sampling. No proof-assistant check is claimed.

## 10. Input provenance and limitations

Read and retained locally:

- `marici_physical_change_of_rings.md` and its checker: binding ambient result, exact endpoint source, full target domains, and the previously verified occurrence-purity projection;
- `marici_comparison_fibre_adjunction_bar.md`: line-retaining frame, primitive endpoint cochain, and distinction between the candidate and the physical endpoint target;
- `marici_physical_endpoint_pullback.md`: endpoint normal-duality source and primitive normalization;
- the attached `9ed7e068-20f4-45b6-9c52-a70aa8f82e40.md`: current task and decision gates.

The task's separate `marici_primitive_conormal_column_20260908.md` and the three named DGPyramid Agda files were not present in the mounted inputs and could not be fetched at the provided default-branch paths in this session. Searches returned references to them, not their contents. No theorem or matrix is attributed to those unread files. The present candidate is defined without using D35, so its falsification does not depend on their unspecified entries. No claim of having exhausted all native targets is made.

### Mathematical references

[M1] Stacks Project, *Hom complexes*, tag 0A8H. Used for the mapping differential and the interpretation of chain maps from projective resolutions.

[M2] Stacks Project, *The Koszul complex*, tag 0621; *bounded-above complexes of flat modules are K-flat*, tag 06YB. Used for the explicit derived pullback model and tensor conventions.

The native obstruction itself is the calculation of Sections 3–5, not a claim imported from these references.
