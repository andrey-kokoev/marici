# Endpoint-complete descent and the coefficient dual that scalar pushouts miss

Date: 2026-09-07  
Lane: Branch B — the fixed alternating/Rees target and its comparison objects

## Result and scope

This calculation continues the seven-open lifting atlas of `marici_divisor_complement_descent_20260907.md`. It makes three changes in what can be tested precisely.

First, both endpoint terms are restored to the top boundary module. The resulting fourteen-component cocycle has two endpoint projections that, together, detect every nonzero coefficient multiple of its cyclic descent class. These projections are maps on the calculated top cycle module; a coordinate erasure on the entire target complex is not being claimed.

Second, all ordinary coefficient functionals defined over the original alternating base are classified. Their pushouts detect only three mixed-pole classes. Six proper-subset components and both endpoint components become actual Cech coboundaries after this coefficient projection. The joint kernel is calculated exactly. In particular, a nonzero multiple of the complete obstruction passes every one of these scalar tests. This statement is deliberately not extended to new sheaf functionals available only after restricting to the open: such maps can contain additional allowed denominators.

Third, the actual alternating ring's relative dualizing complex is constructed from a fifty-generator ambient resolution. It has a branch term and an additional conductor term in distinct cohomological degrees, joined by a nonzero extension. The supported derived dual of the complete cyclic obstruction retains the information that the base-defined scalar tests miss. Its coefficient lies on the conductor divisor, with its own conormal line and shift; it is not an unrestricted scalar trace.

These are coefficient-side constructions. They neither turn the non-split covariant lifting problem into a split one nor identify the independently defined native physical source with the constructed dual. They do not supply either missing physical endpoint connector. The ordinary and PC targets share the top modules used here, but are not identified in their other degrees. All claims about biduality below concern bounded coherent objects, not arbitrary noncoherent localization modules.

## 1. The fixed rings, complexes and open

Use the labelled short sets

\[
S_+=\{13,35,15\},\qquad S_-=\{02,24,04\},\qquad L=\{03,14,25\}.
\]

In words: the two short sets are the alternating endpoint triangulations. The long parameters stay independent.

Let

\[
\mathcal C=\mathbb Z[t_s\ (s\in S_+\cup S_-),X_l,u_l\ (l\in L)],
\]

\[
\mathcal B=\mathcal C[X_s:s\in S_+\cup S_-]/(X_pX_m:p\in S_+,m\in S_-),
\quad I_\pm=(X_s:s\in S_\pm).
\]

In words: opposite-sheet occurrence products vanish, but no normal or occurrence parameter is inverted on this base.

Write

\[
\tau_\pm=\prod_{s\in S_\pm}t_s,\qquad T=\tau_+\tau_-,\qquad U_L=u_{03}u_{14}u_{25},
\]

\[
\mathfrak a=(T,\tau_+I_+,\tau_-I_-),\qquad
V=\operatorname{Spec}\mathcal B\setminus V(\mathfrak a).
\]

In words: the open is precisely the local lifting locus already computed, not a newly identified physical generic fibre. Its seven charts are the central chart with T invertible and the three branch charts on either sheet. The cover has 7, 12, 8, 2 nonzero terms in successive Cech degrees.

The supplied support sequence is

\[
0\longrightarrow F_B/F_V\longrightarrow F_K/F_V\longrightarrow Q\longrightarrow0.
\]

In words: the notation F_V denotes the two endpoint cubes; it is distinct from the coefficient open V. The target retains all 215 loaded states before taking quotients. Its homological degrees range from zero through three.

The previous calculation supplies the boundary module and local lifts

\[
M=H_3(F_B/F_V)=I_+^{\oplus6}\oplus I_-^{\oplus6},\qquad
\pi(s_i)=\theta,\qquad ds_i=0.
\]

In words: differences of the local generic-unit lifts are top boundary cycles. The inherited labels and orientations on these summands remain fixed.

## 2. Restore both endpoint families

At the positive endpoint the three normal coefficients are the positive-sheet products t_s X_s. A top coefficient is killed by all three precisely when it belongs to I_-. At the negative endpoint the corresponding annihilator is I_+. Therefore

\[
H_3(F_V)=I_-\,e_+\oplus I_+\,e_-.
\]

In words: the top endpoint cycles carry the opposite branch ideal, not an unrestricted coefficient line.

Each of the twelve previously constructed proper inactive-subset generators is already a full boundary cycle when multiplied by its indicated branch ideal; none has an endpoint coordinate. They provide a section of the map on top cycles. Restoring the two fully inactive subsets thus gives

\[
\widehat M=H_3(F_B)
=M\oplus I_+e_-\oplus I_-e_+
\cong I_+^{\oplus7}\oplus I_-^{\oplus7}.
\]

In words: this is an exact statement about the top cycle module. It is not an assertion that the whole endpoint support sequence splits as chain complexes. Completeness follows from the previous twelve-summand classification, the endpoint kernel above, and the explicit lifted generators. The checker verifies all fourteen actual cycle families in the full target, and their overlap identities also in its specified PC realization.

For a positive family indexed by a nonempty inactive subset N of S_-, define P_N and L_N to be the positive short and long labels compatible with every element of N. The coefficient in the overlap difference is

\[
r_{+,N}=
\frac{\prod_{l\in L\setminus L_N}u_l}
{\left(\prod_{n\in N}t_n\right)\left(\prod_{p\in P_N}t_p\right)}.
\]

In words: use exactly the coefficient already obtained from the full local lift. The negative families are obtained by labelled reflection. No new denominator is placed in the native base; these expressions are regular on the specified overlaps.

The full overlap decomposition is

\[
s_0-s_+=\sum_{\varnothing\ne N\subseteq S_-}r_{+,N}\Gamma_{+,N},
\qquad
s_0-s_-=\sum_{\varnothing\ne N\subseteq S_+}r_{-,N}\Gamma_{-,N}.
\]

In words: unlike the endpoint-relative formula, these sums include the full inactive subset. Its generator is the actual fully marked endpoint cell. The cocycle convention is omega_ij=s_j-s_i, so the central-to-branch cocycle has the negative of these coefficients.

The endpoint components are consequently

\[
\widehat\omega_{e_-}=-\left[\frac{U_L}{\tau_-}\right]
\in\mathcal C[T^{-1}]/\mathcal C[\tau_+^{-1}],
\]

\[
\widehat\omega_{e_+}=-\left[\frac{U_L}{\tau_+}\right]
\in\mathcal C[T^{-1}]/\mathcal C[\tau_-^{-1}].
\]

In words: neither class is zero in its branch-ideal cohomology. The long-normal product is retained.

A coefficient c in C kills the first class precisely when tau_- divides c; it kills the second precisely when tau_+ divides c. This follows coefficientwise in the Laurent monomial basis. All long variables are independent, and their product introduces no further annihilator. Positive occurrence coefficients annihilate the corresponding first cohomology, by the ideal-to-branch-to-conductor exact sequence used in the previous note. Thus

\[
\operatorname{Ann}_{\mathcal B}
(\widehat\omega_{e_-},\widehat\omega_{e_+})
=I_++I_-+(T)
=\operatorname{Ann}_{\mathcal B}[\widehat\omega].
\]

In words: the two endpoint projections detect every nonzero coefficient multiple of this particular cyclic torsor. They do not detect every arbitrary class in the fourteen-component cohomology group.

Let

\[
W=\mathcal B[\widehat\omega]\cong\mathcal C/(T).
\]

In words: this is the finite cyclic module of global descent obstructions. Its support on the affine coefficient base is the missing conductor with T zero. In particular W restricts to the zero sheaf on V. A nonzero class in global cohomology is not being confused with a nonzero stalkwise section of W on V.

## 3. Classify every ordinary base-defined coefficient functional

Here a scalar coefficient target means B, not the integers or a numerical period. Define

\[
\mathcal B_+=\mathcal C[X_p:p\in S_+],\qquad
\mathcal B_-=\mathcal C[X_m:m\in S_-].
\]

In words: these are the two actual normalization-branch rings.

One has

\[
\operatorname{Hom}_{\mathcal B}(I_+,\mathcal B)\cong\mathcal B_+,
\qquad
\operatorname{Hom}_{\mathcal B}(I_-,\mathcal B)\cong\mathcal B_-.
\]

Proof: the image of a map from I_+ is annihilated by I_-, so it lies in I_+. On the positive polynomial branch the relations X_i f(X_j)=X_j f(X_i), together with coprimality of distinct occurrence variables, force f(X_i)=X_i a for one polynomial a in B_+. Conversely multiplication by any such a is an allowed map. This argument uses no fraction field projector or division by a parameter. The negative side is identical.

Therefore every B-linear functional on the full top boundary module is a sum of the fourteen labelled coordinate inclusions, followed by multiplication by branch polynomials. On first cohomology, only their conductor values act: positive-degree occurrence terms act by zero. This proves the classification of all base-defined functionals, not merely a test of fourteen examples.

The normalization sequence on V gives

\[
H^1(V,\mathcal O_V)
\cong\frac{\mathcal C[T^{-1}]}
{\mathcal C[\tau_+^{-1}]+\mathcal C[\tau_-^{-1}]}
\cong H^2_{(\tau_+,\tau_-)}(\mathcal C).
\]

In words: a coefficient survives in this scalar target only if it has poles from both sheets. The last description is the actual two-element localization complex, with the usual cohomological degree. The vanishing of branch H^1 is inherited from removing its codimension-four regular-sequence locus. See [M1].

The inclusion I_+ to B induces the quotient map from C_T/C_+ to C_T/(C_++C_-). The negative inclusion has the opposite connecting orientation. This sign is checked directly on the seven-open complex: the positive and negative mixed-pole cocycles sum to the coboundary of the central zero-cochain.

### Exactly three mixed-pole images

The six singleton families give three classes, paired with opposite signs between the two sheet coordinates:

\[
\rho_{14}=\left[\frac{u_{14}}{t_{02}t_{35}}\right],\qquad
\rho_{25}=\left[\frac{u_{25}}{t_{04}t_{13}}\right],\qquad
\rho_{03}=\left[\frac{u_{03}}{t_{24}t_{15}}\right].
\]

In words: each has one pole on either sheet and the unaltered missing long-normal coefficient. All six double-inactive families and both endpoint families map to zero.

The latter vanish by explicit Cech boundaries, not by omitting terms. For a positive-family residue with no positive normal pole, place its coefficient at the central chart and all negative charts, and place zero at all positive charts. These are regular scalar sections. Their Cech differential is exactly the original central-to-positive cocycle. This correction is not an I_+-valued correction: the negative chart module of I_+ is zero. It therefore does not trivialize the original descent torsor. The reflected construction treats negative families.

The three pairs

\[
K_1=(t_{02},t_{35}),\qquad K_2=(t_{04},t_{13}),\qquad K_3=(t_{24},t_{15})
\]

involve compatible labelled short diagonals. In particular they are not the previous crossing support pairs (04,35), (02,15), (24,13). A source comparison cannot identify the two collections solely because both contain three pairs.

For each displayed residue, its annihilator in C is exactly its indicated pair ideal. Different pair residues have different negative-support monomials, so their nonzero coefficient-generated submodules do not cancel one another. The joint kernel of every base-defined scalar pushout, on the original cyclic module, is therefore

\[
\ker\bigl(W\longrightarrow\textstyle\prod_{\lambda\in\operatorname{Hom}_{\mathcal B}(\widehat M,\mathcal B)}
 H^1(V,\mathcal O_V)\bigr)
\cong\frac{K_1\cap K_2\cap K_3}{(T)}
=\frac{K_1K_2K_3}{(T)}.
\]

In words: the three pairs use disjoint sets of coordinates, so the intersection equals their eight-generator product ideal. The map in the formula sends a coefficient multiple of the torsor to all its pushed-out cohomology classes; it is not evaluation of an arbitrary cohomology class without specifying the torsor.

In particular

\[
\tau_+[\widehat\omega]\ne0,
\qquad H^1(\lambda)(\tau_+[\widehat\omega])=0
\quad\text{for every }\lambda\in\operatorname{Hom}_{\mathcal B}(\widehat M,\mathcal B).
\]

In words: a nonzero endpoint-sensitive obstruction passes every ordinary scalar coefficient test descended from the original base. This is information loss, not a successful gluing theorem.

**Boundary of this result.** After restricting to V, extra sheaf maps become available. For example, multiplication by 1/tau_+ on the positive branch ideal is a legitimate sheaf map on that open, though it does not come from a B-linear map over the original affine base. Applying it to a positive singleton component detects the blind multiple again. No claim that all scalar sheaf tests on V fail is made. Nor are these additional inverses admitted into the native source.

## 4. Construct the actual relative dualizing complex

Let the smooth ambient ring be

\[
\mathcal S=\mathcal C[X_p:p\in S_+,X_m:m\in S_-],\qquad
\mathcal B=\mathcal S/(X_pX_m:p\in S_+,m\in S_-).
\]

In words: unlike the target coefficient ring, S has all six occurrence variables independent. Its quotient is exactly the alternating ring already used. Its embedding is not another geometric carrier.

Define

\[
\mathscr D_{\mathcal B/\mathcal C}
=\operatorname{RHom}_{\mathcal S}
\left(\mathcal B,\bigwedge^6\Omega^1_{\mathcal S/\mathcal C}[6]\right).
\]

In words: use the dualizing complex supplied by this polynomial embedding, with the actual six occurrence-volume line. B is flat over C and of finite presentation. These formulas are the usual relative-duality construction [M3].

### A fifty-generator resolution

Resolve each three-generated occurrence ideal by its truncated Koszul complex. Tensor these two ideal resolutions; their variables are disjoint, and the ideals are free over C in their monomial bases. The tensor resolves their product. Augment that product inclusion into S. This gives free resolution ranks

\[
(1,9,18,15,6,1).
\]

In words: fifty coefficient-resolution generators, not fifty added target cells.

Apart from the degree-zero unit, a generator is e_(A,B) for nonempty subsets A of the three positive indices and B of the three negative indices; its homological degree is the size of A plus the size of B minus one. At degree one its differential is the corresponding mixed occurrence product. In higher degrees it removes an index with the ordinary Koszul sign; the negative-factor differential has the additional tensor sign given by the degree of the positive ideal resolution. These complete formulas are implemented in the standalone checker.

The ideal-resolution argument proves exactness for arbitrary polynomial exponents. Independently, the checker verifies every differential square, 729 homogeneous resolution calculations, and 4,096 homogeneous calculations of the transposed dual. All nonzero integral Smith factors in those calculations are one.

Put

\[
\lambda_\pm=\bigwedge^3\Omega^1_{\mathcal B_\pm/\mathcal C}.
\]

In words: these are the branch occurrence-volume lines, not Rees conormal lines or the physical channel orientation.

The result is

\[
H^{-3}(\mathscr D_{\mathcal B/\mathcal C})=\lambda_+\oplus\lambda_-,\qquad
H^{-1}(\mathscr D_{\mathcal B/\mathcal C})=\mathcal C_{\mathrm{or}},
\]

\[
H^q(\mathscr D_{\mathcal B/\mathcal C})=0\quad(q\notin\{-3,-1\}).
\]

In words: the full coefficient dual has two branch contributions and an additional conductor contribution. The latter is odd under sheet exchange. Replacing it with a single shifted coefficient line, or only the branch top forms, is not a quasi-isomorphism.

The orientation is checked, not inferred from the cohomology ranks. In the top of the tensor ideal resolution the two factors have homological degree two, so exchanging them introduces no tensor-flip sign. Exchanging the two blocks of three occurrence differentials reverses the six-dimensional volume. The remaining conductor character is therefore odd. All six source-labelled dihedral actions commute with the full resolution differential.

### The two degrees do not split apart

The actual normalization difference sequence, with its polarity character, is

\[
0\longrightarrow\mathcal B\longrightarrow\mathcal B_+\oplus\mathcal B_-
\xrightarrow{\varepsilon_+-\varepsilon_-}\mathcal C_{\mathrm{or}}\longrightarrow0.
\]

Dualizing gives

\[
\mathcal C_{\mathrm{or}}
\longrightarrow(\lambda_+\oplus\lambda_-)[3]
\longrightarrow\mathscr D_{\mathcal B/\mathcal C}
\longrightarrow\mathcal C_{\mathrm{or}}[1].
\]

In words: the conductor term and the branch terms remain joined by the dual of the actual normalization difference. This triangle does not split. Indeed its first map is the derived dual of a nonzero map between bounded finite modules over the regular ambient ring; biduality is faithful on these objects [M2]. Equivalently, it is the nonzero Postnikov attachment between the two displayed cohomological degrees.

For an explicit chain model of that map, include the negative-variable Koszul resolution of B_+ into the six-variable Koszul resolution of C with sign plus, and include the positive-variable resolution of B_- with sign minus. These inclusions lift the normalization difference. Their transposes supply the dual map. The checker verifies both complete chain maps.

Thus the additional conductor term is not a disposable direct summand or an extra scalar degree added by convention.

## 5. A supported dual that retains the scalar-blind cyclic class

For the finite cyclic module W, adjunction gives

\[
\operatorname{RHom}_{\mathcal B}(W,\mathscr D_{\mathcal B/\mathcal C})
\simeq
\operatorname{RHom}_{\mathcal S}
\left(W,\bigwedge^6\Omega^1_{\mathcal S/\mathcal C}[6]\right).
\]

In words: its derived coefficient dual can be calculated over the same smooth ambient ring. This is not ordinary Hom into B, and it reverses variance.

The defining sequence for W over S consists of the six short occurrence variables followed by T. It is regular: after removing the occurrence variables the remaining ring is C, and T is a non-zero-divisor there. The Koszul resolution therefore has ranks

\[
(1,7,21,35,35,21,7,1).
\]

In words: this keeps all seven conormal generators and every comparison degree. No normal parameter is inverted.

Let ell_T be the conormal line of the divisor T in the conductor ring C. The first six conormal determinant factors pair with the six occurrence-volume factors. The result is

\[
\operatorname{RHom}_{\mathcal B}(W,\mathscr D_{\mathcal B/\mathcal C})
\simeq W\otimes\ell_T^\vee[-1],
\qquad \ell_T=(T)/(T^2).
\]

In words: the entire cyclic obstruction survives, in cohomological degree one, with the inverse of its own conductor-divisor conormal line. The remaining line is even under the source relabellings, which preserve T. Neither this line nor the occurrence-volume frame is identified with the physical normal [dX03].

The top dual Koszul generator, paired with the ordered conormal determinant, has coefficient one. For every coefficient c,

\[
(\overline c\otimes[T]^\vee)([T])=\overline c\in\mathcal C/(T).
\]

In words: this is supported line evaluation, not division by T and not a map into the unrestricted base ring. The quotient coefficient remains visible. In particular the class of tau_+ is nonzero, whereas T is a boundary. The checker verifies the complete Koszul chain pairing, all 128 antidiagonal unit entries, the primitive top class, and explicit incoming-boundary witnesses for monomials in the defining ideal.

This establishes a precise coefficient-side repair of the scalar-test information loss: use the full derived dualizing object with its conductor attachment and supported output. It does not make the original torsor vanish. Also, it does not identify the cyclic coefficient module with the independently supplied native source. The dual of multiplication by tau_+ is still nonzero; this statement does not require a covariant identification of every original state with a dual state.

## 6. The correctly reversed comparison triangle

The endpoint-inclusive top-module extension restricts on V to

\[
0\longrightarrow\widetilde{\widehat M}|_V
\longrightarrow\widetilde{\widehat H}|_V
\longrightarrow\mathcal O_V\longrightarrow0,
\qquad \widehat H=H_3(F_K).
\]

In words: keep the seven actual local unit lifts and their complete fourteen-family descent cocycle. Its boundary class is the nonzero class calculated above.

Using the dualizing complex restricted to V defines a well-typed reverse triangle

\[
\mathbb D_V(\mathcal O_V)
\longrightarrow\mathbb D_V(\widetilde{\widehat H}|_V)
\longrightarrow\mathbb D_V(\widetilde{\widehat M}|_V)
\longrightarrow\mathbb D_V(\mathcal O_V)[1].
\]

In words: duality reverses the generic and boundary arrows, while keeping the two endpoint factors through their actual inclusion and projection maps. The dual connecting morphism is nonzero by coherent biduality. A correct reverse pairing must account for that morphism rather than silently converting it into a zero boundary.

This is the canonical coefficient-side reversed triangle. The note has not constructed an independently normalization-provenanced geometric map from the native source into it. In particular, a dual connecting morphism is not automatically either of the two required endpoint connector two-cells.

The supported calculation of W in Section 5 is on the affine coefficient base. It is not an interchange of derived global sections with duality on the nonproper open V. Such an interchange would require a correctly typed supported/proper comparison, which is not supplied here. This qualification prevents the boundary-supported cyclic module from being mistaken for a nonzero sheaf on V.

## 7. Verification and next comparison

Run:

```sh
python check_marici_descent_duality_20260907.py \
  --output marici_descent_duality_certificate_20260907.json
```

The new standalone checker passes **50,010 exact assertions**. It verifies the complete endpoint-inclusive overlap formulas; all fourteen coordinate pushouts and their exact Cech boundaries; the three mixed-pole images; all 64 squarefree normal multiplier cases for the joint annihilator; occurrence annihilation; the open-only scalar-map qualification; the fifty-generator resolution and its source-labelled action; 729 primal and 4,096 dual homogeneous calculations; the normalization-difference comparison; and the ordered supported Koszul pairing and boundary witnesses.

The previous divisor-complement checker was independently rerun in this session and passed **44,523** assertions. Its result and replay hash are recorded separately. The new checker does not execute that prerequisite automatically and does not need its files for its mathematics. No proof assistant was used. The unbounded coefficient assertions are proved by the polynomial, regular-sequence, and localization arguments, rather than extrapolated from finite sample sizes.

The next physical comparison now has an explicit target on the dual side: it must match the non-split conductor attachment, the endpoint-sensitive descent components, and the surviving T-conormal placement. Agreement of ordinary scalar pushouts, even all base-defined ones, is provably weaker.

## Sources

[P1] `marici_divisor_complement_descent_20260907.md` and its standalone checker: the seven actual local lifts, twelve proper-subset families, both endpoint discrepancies, and the previous annihilator theorem.

[P2] `marici_q_graded_lift_naturality_20260907.md`: the exact top-module presentation and the labelled boundary-ideal summands.

[P3] Pinned source repository `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`: the original alternating normalization ring and loaded coefficient differential. This calculation uses the locally available, previously fetched source model; it does not claim to inspect newer repository revisions.

[M1] Stacks Project, Section 51.2, tag `0DWQ`: localization Cech complexes and open/support comparison.

[M2] Stacks Project, Section 47.15, tag `0A7A`, especially Lemmas 47.15.3 and 47.15.8: coherent biduality and finite-map dualizing complexes. Lemma 47.15.6, tag `0A7G`: localization of dualizing complexes.

[M3] Stacks Project, Sections 47.25 and 47.27, tag `0E2B`: relative dualizing complexes for flat finite-presentation morphisms.

[M4] Stacks Project, Section 15.29, tag `0621`: the ordered Koszul differential and its tensor signs.
