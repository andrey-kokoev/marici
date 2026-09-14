# Native cup-to-precomposition mate: algebraic construction and outstanding physical interface

Date: 2026-09-08

## Decision and input status

Decision 3 applies to the requested fully framed calculation. A normalized native algebraic variance mate is constructed below, but the actual line/support adapter into the marked target has not been imported or certified.

The task attachment reports that the first-jet equations, the primitive homogeneous detector, and the nine native quadratic actions have passed in eight framed cases. Those statements are used as supplied premises. This note does not reopen those tests or reinterpret them as ambient `RHom_A` calculations.

Of the seventeen files named in that attachment, two are available in this runtime: the primitive-column note and standalone checker. The nine Branch C files and six new adapter/result files are not mounted. A local filesystem and archive inventory is recorded in `local_input_status.json`. This is not a claim about the user's separate working tree. No GitHub or File Library search was used. It is not possible to truthfully say that all seventeen files were consumed.

The new executable uses only the native algebra and retained primitive-column definition. It reconstructs the native endpoint bar differential, the relative-module word decomposition, and the conductor-resolution Hom differential. It does not simulate a missing physical adapter by assigning it zero matrices.

## 1. Rings, complexes, and variance

Retain the spectator ring C, including beta and all source-admitted spectator parameters. Put

\[
B=C[X_{13},X_{15},X_{35},X_{02},X_{04},X_{24}]/(I_+I_-),
\]

\[
I_+=(X_{13},X_{15},X_{35}),\qquad I_-=(X_{02},X_{04},X_{24}).
\]

The normalization branch B_sigma is the quotient by the opposite occurrence ideal. It is not the ideal I_sigma. The source in the new task is

\[
M_\sigma^{\mathrm{bar}}=\operatorname{Hom}_B(\operatorname{Bar}_B(B_\sigma),C).
\]

This is contravariant in its source B_sigma and covariant in its output C. Derived endomorphisms of C act on the left by cup/postcomposition. The branch augmentation is the primitive cochain epsilon_sigma.

The target is the native conductor-resolution Hom

\[
N_k=\operatorname{Hom}_B(P_C,E_{\beta,k}),
\]

where X_k u=beta v, every X_i v=0, and every other X_i u=0. Endomorphisms of the conductor source act on the right by precomposition. The v inclusion is the retained conormal primitive.

A right module cannot be identified with a left module by retaining the same order of multiplication. The graded opposite multiplication is

\[
a\cdot_{\mathrm{op}}b=(-1)^{|a||b|}ba.
\]

Let S be the Hopf antipode of the native Yoneda algebra. It obeys

\[
S(ab)=(-1)^{|a||b|}S(b)S(a).
\]

It converts the right target into a left module by

\[
a\star n=(-1)^{|a||n|}nS(a).
\]

This is an explicit convention, not a claim that the unspecified physical adapter already realizes the antipode. It has the required associativity and differential signs. The graded opposite and shift conventions agree with Stacks Project 0FPZ and 0FQ2.

The algebra used here is

\[
\mathcal E_B=\Lambda_C(\eta_{13},\eta_{15},\eta_{35})*_C
\Lambda_C(\eta_{02},\eta_{04},\eta_{24}).
\]

Its relative Hopf subalgebra R is the previously retained free algebra on 49 primitive nested commutators. For a primitive generator g,

\[
S(g)=-g.
\]

On a word of n degree-one occurrence generators, an explicit formula is reversal multiplied by (-1)^{n(n+1)/2}, followed by the same-sheet exterior normalization. This does not identify an ordered mixed product with its anticommutator.

## 2. A chain projection out of the full native endpoint bar

Write a normalized bar cochain basis element as a coefficient extractor on

\[
[b_1|\cdots|b_n]m,
\]

where each b_i is a positive-degree native monomial and m is a monomial on the selected endpoint branch. All monomials are retained; the bar complex is not truncated by polynomial relations beyond the actual alternating ring.

The differential is dual to adjacent multiplication and the final branch-module action. The leading B coefficient acts through the conductor and its positive-degree part contributes zero. The executable uses the bar cochain convention delta f=f d. To convert to the standard internal-Hom convention, rephase degree n by (-1)^{n(n+1)/2}, with the corresponding conjugation of cup actions. This convention change does not remove any source term.

There is a degree-preserving cochain map

\[
q_\sigma:M_\sigma^{\mathrm{bar}}\longrightarrow
\mathcal E_B/(\mathcal E_B\mathcal E_\sigma^{>0}).
\]

It is defined on coefficient extractors as follows. If m=1 and every b_i is a single occurrence variable, send that extractor to the corresponding ordered Yoneda word. Otherwise send it to zero. Then impose the same-sheet exterior relations and the final own-sheet ideal relation.

This is an actual map on the complete bar cochains, not an assertion that their differentials were zero. To verify q_sigma delta=0 in every degree, only three cases are needed.

* Splitting a quadratic same-sheet monomial gives an exterior anticommutator or square, which vanishes in E_B.
* Splitting a degree-one final own-sheet monomial gives a word ending in an own-sheet generator, which vanishes in the quotient.
* All other off-diagonal monomial degrees remain off the linear diagonal and project to zero.

These statements also apply to arbitrary coefficients in C. No coefficient-field argument, factorial division, or normal localization is used.

The chosen relative generators have closed native bar representatives obtained by nested graded commutators of the six linear coefficient extractors. The projection sends those representatives to the corresponding elements of R. Thus q_sigma is strictly R-linear for this source bar action.

The endpoint branch, rather than its augmentation ideal, is essential here. The quotient above has eight relative seeds, not the 56 seeds of Ext_B(I_sigma,C).

## 3. Project onto the primitive relative orbit

Use the inherited multiplication factorization with the opposite-sheet exterior block last:

\[
\mathcal E_B/(\mathcal E_B\mathcal E_\sigma^{>0})
\cong\mathcal R\otimes_C\Lambda_C(C^3_{-\sigma}).
\]

Define P_sigma as the R-linear projection onto the exterior-empty seed:

\[
P_\sigma(r\otimes w)=r\,\epsilon(w).
\]

The seven positive-degree exterior seeds are set to zero in this newly chosen algebraic map. This is an explicit choice defining one possible mate; it is not a statement that those native classes vanish, or that a physical comparison has those seven columns. The primitive and its whole relative-operation orbit are retained.

The executable constructs the factorization using actual native-word columns and integer inverse matrices. In degrees zero through four, the branch module ranks are 1,3,12,46,177. Every elimination pivot is a signed unit. It does not replace the source branch module by the ideal endpoint module.

The normalized algebraic mate is

\[
\Phi^0_\sigma(f)=v\,S(P_\sigma q_\sigma(f)).
\]

Its target is N_k. In the inherited native conductor-resolution convention,

\[
\partial(\alpha u+\gamma v)=\beta\eta_k\alpha\,v.
\]

The image of Phi^0 is in the closed v part. Since P_sigma q_sigma kills the bar differential, Phi^0 is a chain map.

For a homogeneous r and f,

\[
\Phi^0_\sigma(r\smile f)
=(-1)^{|r||f|}\Phi^0_\sigma(f)S(r)
=r\star\Phi^0_\sigma(f).
\]

The equality follows from strict R-linearity of P_sigma q_sigma and graded antimultiplicativity of S. It proves the intertwining formula in every degree for this normalized native model. In that model the required intertwining homotopies are zero because the equations hold strictly. This is not an assignment of zero to unprovided physical homotopies.

In particular,

\[
\Phi^0_\sigma(\epsilon_\sigma)=v,
\qquad
\Phi^0_\sigma(r\smile\epsilon_\sigma)=vS(r).
\]

For a primitive relative generator this equals -v r. Raw right precomposition by r and the antipode-converted left action are not silently identified.

## 4. Primitive detectors and the product-order control

For every mixed pair (i,j), with i positive and j negative, the target word

\[
[\eta_j|\eta_i]
\]

has coefficient -1 in the image of r_ij acting on the primitive. No boundary in the degree-two conormal Hom has this row: its v component is in beta eta_35 E_B^1, whose nonzero words begin with a positive block containing 35. The displayed word begins with a negative block. These nine rows have distinct occurrence weights, so they give integral independent detectors. The source bar witnesses are [X_i|X_j]1 on the positive branch and [X_j|X_i]1 on the negative branch.

There is also a negative control for using right precomposition without reversing multiplication. Let

\[
a=r_{13,02},\qquad b=r_{15,04}.
\]

Left cup multiplication composes in the order ab; raw right-precomposition operators compose in the order ba. Their difference has the coefficient-one detector

\[
\operatorname{coeff}_{[13|02|15|04]}(ab-ba)=1.
\]

This row is outside the eta_35 boundary rows. This is a failure of the unconverted product-order prescription, not a first-quadratic obstruction to the requested correctly typed mate. The antipode-corrected construction above retains all 81 ordered quadratic products.

## 5. Endpoint lines and support: the remaining adapter

Write L_sigma for the actual retained endpoint normal/line factor. It may contain a resolved support packet; it is not silently treated as a scalar line merely because a homogeneous primitive has one coordinate.

The exact remaining datum is a supported, framed map

\[
\chi_\sigma:\mathcal L_\sigma
\longrightarrow Cv\otimes\Pi^\vee[3]
\longrightarrow\mathbb D_{35},
\]

together with the comparison identifying the complete framed endpoint source with the native bar factor tensored with this L_sigma. If the final geometric realization uses a different variance or shriek functor, that functor must be part of chi_sigma rather than inferred from a coordinate normalization.

Given this datum, the universal formula is

\[
\Phi_\sigma(f\otimes\ell)
=(-1)^{|f||\ell|}\chi_\sigma(\ell)\,S(P_\sigma q_\sigma(f)).
\]

The sign is the Koszul interchange moving the endpoint factor past the cochain. It gives the same converted left-action identity on the total degree |f|+|ell|. The executable checks both endpoint-factor parities for every tested action; it does not assert a physical determinant identification from those parity tests.

This formula keeps the primitive coefficient equal to one whenever chi_sigma is the normalized primitive adapter. It does not require an inverse occurrence or regulator. The weight of the line map must satisfy

\[
\mathrm{wt}(\mathcal L_\sigma)
=\mathrm{wt}(v)+\mathrm{wt}(\Pi^\vee),
\qquad
\mathrm{wt}(v)=\mathrm{wt}(u)+e_{35}-\mathrm{wt}(\beta),
\]

with the supplied total shift, any endpoint determinant factors, and all actual support terms accounted for. The task brief reports the degree-three primitive match, but does not give the matrices and normal-factor dictionary implementing this factorization.

In particular, its reported homotopy ideal is

\[
(t_T,t_{i_1},t_{i_2},t_{i_3}).
\]

The target support must use that same retained normal data, or a specified adjunction transporting it. One cannot replace it by (t_T), assume these four displayed equations are a regular sequence, or remove a redundant Koszul factor. An unshifted scalar module quotient does not specify the required derived support operation.

This is why the native algebraic construction cannot be labelled a certified eight-frame physical mate without the new adapters. The statement is about unavailable evidence in this runtime, not a theorem that the user's working tree lacks chi_sigma.

## 6. Labelled symmetry

The native bar projection is natural under the six admitted label permutations. The exterior-empty seed is preserved when both endpoint types are transported together. The antipode commutes with the Hopf action. Therefore Phi^0 is equivariant for the full labelled family of normalized coefficient objects.

A reflection transports the marked target E_beta,35 to E_beta,s(35); it is not automatically an automorphism of fixed D35. The missing physical line map must transport accordingly, including Pi-dual, endpoint conormal and determinant factors.

For the recorded quartic generator,

\[
s(g)=-g+[r_{15,02},r_{13,04}],
\]

the product correction is retained in the whole native-word polynomial. Applying S gives

\[
S(s(g))=g-[r_{15,02},r_{13,04}]=s(S(g)).
\]

The actual correction is nonzero. The executable checks this identity on both endpoint modules; it also checks the full word-module transport through operation degree four and all 294 antipode/generator transport squares through degree six. It does not replace those formulas by a signed permutation of indecomposables.

## 7. What was verified

The standalone executable checks the native bar differential and its projection on every coefficient-extractor basis vector of total occurrence degree at most four. Both endpoint branches are retained. It checks all nine quadratic, eighteen cubic and fifteen quartic primitive generators at each endpoint, all 81 ordered quadratic products at each endpoint, and the full R-intertwining equations allowed by the degree bound. It includes the nonzero u-to-v differential of the target Hom model and the graded opposite action signs.

The all-degree argument consists of the bar projection identity, the retained relative-module factorization, and the Hopf antipode formula. Finite enumerations test these formulas but are not claimed to prove them by extrapolation.

Only the new checker is replayed. It does not count any unavailable adapter test as an assertion and does not rerun the earlier 80,087-assertion target calculation as new work.

The deterministic certificate reports decision 3, the verified normalized algebraic mate, and `physical_framed_mate_certified: false`. The separate local-input inventory gives every required file's availability.

## References and provenance

* Current attached task: `36580000-6268-4eb7-92cd-0cf1cfb4d2b2.md`. Its reported adapter successes are premises, not imported checker results.
* Retained local target note and checker: `marici_primitive_conormal_column_20260908.md` and `check_marici_primitive_conormal_column_20260908.py`.
* Retained operation interfaces and native bar audit: `marici_operation_collar_interface_20260908.md` and `marici_collar_control_audit_20260908.md`.
* Stacks Project, tags 0FPZ and 0FQ2: graded opposites, shifts, and precomposition module conventions.

No repository files were modified.
