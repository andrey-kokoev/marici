# Branch C: physical endpoint/Gysin pullback over the bare generic Q-class

Date: 2026-09-08  
Pinned coefficient source: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result and status

This note constructs and tests an explicit endpoint-facing Gysin candidate, its source comparison, and its comparison-space pullback. It also gives the obstruction theory for the genuinely enhanced physical pullback and tests the nine quadratic relative operations in the native endpoint-module presentation.

There are three distinct conclusions.

1. The unchanged bare-Q coefficient lifting problem is contractible after the whole generic class is fixed. Its endpoint composites are exact. This is the established input, not a new physical existence theorem.
2. Three-normal endpoint duality by itself leaves the endpoint mapping complex acyclic in that same frame. Including the actual endpoint conormal frame gives a primitive endpoint class, but removes the degree-four generic class from that new endpoint-source frame. The line-retaining counit is constructed; evaluating its frame by the Euler section gives an explicitly nullhomotopic source comparison. In the resulting same-target pullback, independently prescribing primitive endpoint differences gives the nonzero obstruction `(1,1)` in two integral endpoint lines. All replacement homotopies are included.
3. An exterior-factorized, augmentation-only occurrence action cannot map its unit to either native endpoint unit while intertwining the nine mixed operations. All nine actions on each endpoint are independently nonzero. Conversely, an augmentation projection *from* an endpoint operation module to a scalar generic module is compatible with those actions. Thus nontrivial endpoint actions and a scalar generic action are not, by themselves, a no-go for a full collar.

These results do not identify the proposed Gysin candidate with the independently prescribed physical collar. They specify an actual candidate, compute its failure, and isolate the additional operation-compatible bivariant comparison that a physical realization must supply. No physical reflection parity is assigned.

## 1. Coefficients, support, and degree conventions

Let

\[
A=\mathbb Z[X_0,\ldots,X_5,X_{D03},X_{D14},X_{D25},
t_0,\ldots,t_5,u_{D03},u_{D14},u_{D25}].
\]

In words: the six short occurrence variables, three long occurrence variables, six short Rees parameters, and three long normal parameters are independent. The short normal equations are `u_i=t_i X_i`. Harmless monodromy-unit localizations may subsequently be made; none is needed for the calculations in this note.

Put

\[
I_+=\{1,3,5\},\quad I_-=\{0,2,4\},\quad
\gamma=\sum_{\ell\in\{D03,D14,D25\}}e_{u_\ell},\quad
U_L=\prod_\ell u_\ell.
\]

In words: the two endpoint labels are the odd and even triples, while gamma is the retained three-long-normal degree.

The supplied target `K` has one state `[F,H]` for each noncrossing hexagon face `F` and subset `H` of its marked normals. Its homological degree is `3-|F|+|H|`. In cohomological conventions it lies in degree `|F|-|H|-3`. The radial differential has coefficient `X_a/u_a`; a normal differential removes a mark through a signed localization inclusion. Each stalk is

\[
A[u_a^{-1}:a\in F\setminus H].
\]

In words: only the normals of unmarked labels may be inverted. After the short Rees substitution, inverting a short `u_i` also makes `t_i` and `X_i` units **inside that stalk**, not on the ambient base. The endpoint complexes `V_+` and `V_-` have eight states each. Let `V=V_+\oplus V_-`, let `B` be full short-boundary support, and put `E=K/V`, `Q=K/B`. There are 215, 16, 208, 199, and 7 states respectively in `K,V,B,E,Q`. [S1]

The maps `K -> E -> Q` are covariant, degree-zero quotient maps with their actual coefficient domains. The endpoint connecting maps

\[
e_\sigma:E\longrightarrow V_\sigma[1]
\]

are the connecting morphisms of `V -> K -> E`. In a chosen graded splitting, they are the actual differential entries entering `V`; a graded projection onto endpoint coordinates alone is not a chain map.

For a prescribed channel let `T` be a two- or three-element subset of `I_+`, and retain its excess label `epsilon`. Define

\[
p_T=\prod_{i\in T}t_i,\qquad
P_T=K_A(X_0,\ldots,X_5,p_T),\qquad S_T=A/(X_0,\ldots,X_5,p_T),
\]

\[
\lambda_T=\gamma-\sum_{i=0}^5e_{X_i}-\sum_{i\in T}e_{t_i}.
\]

In words: `P_T` is the complete 128-generator free resolution of the seven-equation source. The first six generators are occurrence conormals; the seventh, `z_T`, is the product-Cartier conormal. The product equation has its own line: it is not three independent Cartier equations.

Koszul resolutions use cohomological degrees `-n,...,0`. A symbol `<lambda>` raises every source internal degree by `lambda`. Define the normalized source

\[
\mathsf S_T=P_T\langle\lambda_T\rangle[-4].
\]

In words: the established cohomological degree-four, internal-degree-lambda map becomes a degree-zero, internal-degree-zero map out of this precisely shifted source. The shift does not identify the eight originally labelled objects; the excess trace's specified determinant/dual-excess line and its input channel remain part of the frame. Four underlying seven-equation complexes occur, each with two trace-channel labels.

The differential on a mapping complex is always

\[
\partial f=d_Yf-(-1)^{|f|}fd_X.
\]

In words: cochain degree, internal degree, and support are separate. All homotopies below are elements of this mapping complex, with the stated degree. [M1]

## 2. The coefficient lifting space, with actual endpoint nullhomotopies

Fix the constructed primitive map `g:mathsf S_T -> Q`, not just the number read from one coefficient. Its unnormalized top column is

\[
\omega=U_LT-\sum_\ell X_\ell\frac{U_L}{u_\ell}M_\ell.
\]

In words: the chamber and three marked-long-normal corrections are one generic cycle. The fractions displayed here are polynomial products of the other two long normals.

Define

\[
\mathscr A_g=\operatorname{hofib}_{g}
\bigl(\operatorname{Map}(\mathsf S_T,E)\to
\operatorname{Map}(\mathsf S_T,Q)\bigr).
\]

A point includes a representative `f` and its comparison with `g`. Define

\[
\mathscr L_g=
\mathscr A_g\times^h_{
\operatorname{Map}(\mathsf S_T,V_+[1]\oplus V_-[1])}\{0\}.
\]

In words: a point also contains both endpoint nullhomotopies, including their higher comparisons. If `a_sigma=e_sigma f` is written as a degree-one cochain into `V_sigma`, its nullhomotopy is `h_sigma` of degree zero with `partial h_sigma=a_sigma`. With the target shifted to `V_sigma[1]`, these are respectively degrees zero and minus one.

The established full Hom calculation gives

\[
\mathscr L_g\simeq *.
\]

This includes the unique coefficient lift to `K`. It says nothing about a new source's independently normalized physical Gysin connector. The new checker embeds the previously constructed candidate matrices and **rechecks** the closed generic map, full cap equation, and both nullhomotopy equations against a freshly reconstructed target and source. It does not use their old certificate as proof.

## 3. Explicit physical-endpoint-source candidate

### 3.1 A regular ambient endpoint support

For each endpoint put

\[
J_\sigma=(t_i:i\in I_\sigma),\qquad
\tau_\sigma=\prod_{i\in I_\sigma}t_i,\qquad
\beta_\sigma=\sum_{i\in I_\sigma}e_{t_i}.
\]

Let `j_sigma:Z_sigma=V(J_sigma) -> Spec A`. This is the actual simultaneous three-Rees intersection. The ordered conormal determinant is

\[
L_\sigma=\det(J_\sigma/J_\sigma^2).
\]

It is a line on `Z_sigma`. Let `tilde L_sigma` denote the free ambient line with the declared ordered frame `ell_sigma` of degree `beta_sigma`. This distinction prevents accidentally performing an extra non-flat base change by tensoring a support line as though it were an ambient free line.

The supported-dual normal factor is

\[
D_\sigma=R\operatorname{Hom}_A(K_A(t_{I_\sigma}),A)
\cong K_A(t_{I_\sigma})\otimes\widetilde L_\sigma^\vee[-3].
\]

In words: it has cohomological degrees zero through three and the dual determinant. This is iterated Cartier duality for the three independent ambient parameters, with the ordered Koszul signs. [M2]

The unframed supported candidate is `P_T tensor D_sigma`, a model of `j_*j^!P_T`. The independently conormal-framed candidate is

\[
P^G_{\sigma,T}=(P_T\otimes D_\sigma)\otimes\widetilde L_\sigma,
\qquad
\mathsf P^G_{\sigma,T}=P^G_{\sigma,T}\langle\lambda_T\rangle[-4].
\]

In words: retain both the dualizing determinant and its separately framed conormal input. The external frame is part of the requested endpoint Gysin datum, not an integer substitution for it.

The unnormalized free complex has **1024 generators**, cohomological degrees `-7,...,3`. It is supported on

\[
V(X_0,\ldots,X_5,p_T,J_\sigma).
\]

All its coefficients are polynomial. It retains the complete `P_T`, including the product-Cartier generator, and adds only the explicit three-normal Koszul dual resolving a specified support. These are resolution generators, not cells inserted into the physical target.

When `T subset I_+`, the product-Cartier equation is redundant after the plus support restriction. Its derived excess remains in this full complex. It is not legitimate to drop `z_T` or call that excess the earlier independently labelled `eta`. Regularity of `j_sigma` in the ambient polynomial ring does not assert transverse intersection with the support of `S_T`.

### 3.2 The typed comparison is a counit followed by an Euler section

The closed-immersion adjunction has a counit

\[
\epsilon_\sigma:P_T\otimes D_\sigma\longrightarrow P_T.
\]

It is covariant and degree zero. On a source basis `(s,e_H^vee)` it sends the empty dual-normal subset to `s` and all nonempty subsets to zero. It is not a degree-zero scalar counit on the removed raw/excess factor.

Before evaluating any line, the actual counit is

\[
c_\sigma^L:P^G_{\sigma,T}\longrightarrow P_T\otimes\widetilde L_\sigma,
\qquad c_\sigma^L=\epsilon_\sigma\otimes1.
\]

In words: this map keeps the conormal frame in its target. Composing with the generic map gives a map to `Q tensor tilde L_sigma`, not an identification with the unshifted, unframed bare generic object. The corresponding endpoint targets are also line-twisted.

The endpoint conormal frame supplies the polynomial section

\[
\widetilde L_\sigma\longrightarrow A,
\qquad \ell_\sigma\longmapsto\tau_\sigma.
\]

Therefore the framed source comparison is the explicit homogeneous degree-zero map

\[
c_\sigma:P^G_{\sigma,T}\longrightarrow P_T,
\qquad
c_\sigma(s\otimes e_H^\vee\otimes\ell_\sigma)=
\begin{cases}
\tau_\sigma s,&H=\varnothing,\\
0,&H\ne\varnothing.
\end{cases}
\]

In words: the line degree is paid for by its actual Euler coefficient. There is no map setting `ell_sigma` to an ungraded scalar unit. This comparison commutes with the complete differential on all 1024 states. Both target endpoint nullhomotopies transport by precomposition with it.

**This last Euler-evaluated map is nullhomotopic.** This is an important negative control, not a proposed solution of the physical transition. If `i` is the first endpoint normal and `p` has homological degree `n`, the homotopy is

\[
k_\sigma(p\otimes e_i^\vee\otimes\ell_\sigma)
=(-1)^{n+1}\frac{\tau_\sigma}{t_i}p,
\qquad dk_\sigma+k_\sigma d=c_\sigma,
\]

and zero on the other dual-normal subsets. Its coefficient is polynomial. The checker verifies this identity on all 1024 columns in every endpoint/source case. A genuine Gysin transition must retain its degree and line; replacing it by this Euler-evaluated ordinary map kills it.

### 3.3 Complete Hom results distinguish the two candidates

At the original frame `lambda_T`, the new calculation gives the following degree-four groups:

| Source | Mapping to the chosen endpoint | Mapping to bare Q |
|---|---:|---:|
| `P_T tensor D_sigma` | zero | one integral line |
| `P^G_sigma,T` | one integral line | zero |

The endpoint column is stronger than a degree-four test: in the unframed case the full endpoint complex is acyclic, and in the framed case its only cohomology is the displayed degree-four line. The framed generic complex may have cohomology in **other** degrees; the certificate records all of it. There is no degree-four generic class for the framed endpoint source.

Both assertions were computed over the original chart and after the full central short-Rees specialization, for each of four `T` and both endpoint labels. They are not extrapolated from a single endpoint or a single coefficient entry. All full-target and short-support groups are also recorded; those groups can acquire additional lower-degree classes and must not be called acyclic indiscriminately.

Consequently `g c_sigma` is nullhomotopic in this new endpoint-source frame. The endpoint candidate has not preserved the primitive bare generic class as a same-degree map out of that same source. The original `g` in Section 2 is still retained as a separate component of the proposed pullback.

### 3.4 Eight-row primitive endpoint class

The framed candidate has an explicit degree-four cocycle `nu_sigma`, zero on nonempty dual-normal subsets. If `H subset I_sigma`, it sends the source occurrence subset `I_sigma^c union H`, together with `z_T`, to

\[
\nu_\sigma(e_{I_\sigma^c\cup H}\wedge z_T\otimes1^\vee\otimes\ell_\sigma)
=\varepsilon_\sigma(H)
\frac{U_L}{\prod_{i\in I_\sigma\setminus H}X_i}[v_\sigma,H].
\]

In words: this is the complete eight-row normal residue. Any `1/X_i` occurs only on the unmarked endpoint stalk, where it is represented by the allowed `t_i/u_i`. There is no occurrence inverse on the base or on a marked state.

The source occurrence indices are increasingly ordered; endpoint marks use the actual lexicographic diagonal order. With the fully marked value normalized positive, the signs are:

| `H` on the plus side | sign | `H` on the minus side | sign |
|---|---:|---|---:|
| empty | -1 | empty | +1 |
| 1 | +1 | 0 | +1 |
| 3 | -1 | 2 | -1 |
| 5 | +1 | 4 | +1 |
| 13 | +1 | 02 | -1 |
| 15 | -1 | 04 | +1 |
| 35 | -1 | 24 | +1 |
| 135 | +1 | 024 | +1 |

In particular,

\[
\nu_\sigma(e_0\wedge\cdots\wedge e_5\wedge z_T\otimes1^\vee\otimes\ell_\sigma)
=U_L[v_\sigma,I_\sigma].
\]

This is primitive in the fixed long-normal frame. The full mapping complex proves that it is not any boundary. Under the full central short-Rees restriction, the fully marked row survives and all other rows vanish with their localized stalks.

Define a concrete independently residue-framed connector by

\[
\theta_\sigma=h_\sigma c_\sigma+\nu_\sigma,
\qquad \partial\theta_\sigma=a_\sigma c_\sigma.
\]

Here the equation is in normalized mapping degrees: `theta` and `h c` have degree zero, `a c` has degree one. In unnormalized degrees these are respectively four and five. This constructs a candidate connector with a nonzero endpoint difference. It does **not** name that difference the already exact coefficient endpoint composite.

## 4. An instantiated pullback and its obstruction

For a point `(f,h_+,h_-)` of `mathscr L_g`, define

\[
\mathscr Z(f)=\prod_{\sigma\in\{+,-\}}
\operatorname{Null}(a_\sigma c_\sigma).
\]

`Null(a)` is the path space from `a` to zero in `Map(mathsf P_sigma^G,V_sigma[1])`, not the set of cochain primitives. These fibres form a mapping-space diagram over `mathscr A_g`. The coefficient arrow is

\[
u:\mathscr L_g\longrightarrow\mathscr Z,
\qquad (f,h_+,h_-)\longmapsto(f,h_+c_+,h_-c_-).
\]

Let `mathscr C_cand` be the candidate endpoint connector subspace whose difference classes are the two positive primitive `nu_sigma` classes in Section 3. There is a genuine inclusion `v_cand:mathscr C_cand -> mathscr Z`. Form

\[
\begin{array}{ccc}
\mathscr H_g^{\rm cand}&\longrightarrow&\mathscr C_{\rm cand}\\
\downarrow&&\downarrow v_{\rm cand}\\
\mathscr L_g&\xrightarrow{u}&\mathscr Z.
\end{array}
\qquad
\mathscr H_g^{\rm cand}=\mathscr L_g\times^h_{\mathscr Z}\mathscr C_{\rm cand}.
\]

In words: its points would include the generic comparison, full coefficient lift, both coefficient nullhomotopies, both framed candidate connectors, and homotopies identifying those endpoint paths.

Such an identification needs degree-minus-one cochains `k_sigma` with

\[
\partial k_\sigma=\theta_\sigma-h_\sigma c_\sigma=\nu_\sigma.
\]

The obstruction is

\[
([\nu_+],[\nu_-])=(1,1)\in\mathbb Z\oplus\mathbb Z.
\]

It is nonzero. Therefore

\[
\mathscr H_g^{\rm cand}=\varnothing.
\]

This is an all-homotopy nonexistence theorem for the stated **same-target, independently primitive-difference framing**. Its inputs, sources, target, and connecting comparison are explicit. It is not a no-go for every possible physical support/duality operation.

Before requiring identification with the coefficient paths, each endpoint's choices form a discrete integral torsor in this frame. Their joint torsor is `Z^2`. Fixing a primitive value chooses its specified component. It does not produce a path to the coefficient component zero. The generic rank-one class fixes neither of those independent primitive differences.

## 5. The enhanced physical pullback and the minimal missing arrow

The actual physical construction must provide a diagram `mathscr C_phys` of independently defined collar sources, support conditions, ordered normal lines, endpoint connectors, and their operation action. For the concrete candidate above these objects have all been specified; what fails is its identity-target comparison.

A different physical construction must supply a **degree-zero, support- and determinant-typed comparison of whole endpoint path diagrams**

\[
b:\mathscr C_{\rm phys}\longrightarrow\mathscr Z_{\rm cmp}.
\]

The coefficient side must have its corresponding map `u_cmp:mathscr L_g -> mathscr Z_cmp`. The enhanced problem is then

\[
\begin{array}{ccc}
\mathscr H_g&\longrightarrow&\mathscr C_{\rm phys}\\
\downarrow&&\downarrow b\\
\mathscr L_g&\xrightarrow{u_{\rm cmp}}&\mathscr Z_{\rm cmp},
\end{array}
\qquad
\mathscr H_g=\mathscr L_g\times^h_{\mathscr Z_{\rm cmp}}\mathscr C_{\rm phys}.
\]

This is the requested endpoint/generic pullback. The top-right object and right arrow are **not asserted constructed merely by writing this diagram**. Section 4 is its fully instantiated minimal-candidate test. A genuine alternative requires its bivariant source and comparison functor to be derived from the prescribed geometry.

Here `mathscr Z_cmp` is the homotopy limit of the whole comparison diagram: both endpoints, their plus/minus difference, Čech overlaps, normal specialization cube, labelled dihedral transport, and the bar construction for the relative operations. It is not a product of scalar endpoint values. A functor inducing `b` must supply every arrow of that diagram, not just an isomorphism of determinant lines.

There is a precise necessary property of any changed comparison. If it sends a nonzero primitive endpoint difference into the same coefficient path component, it must kill that difference **in the comparison object**, while retaining its source as relative data. For a linear comparison `pi_sigma:C_sigma -> Z_sigma^cmp`, write `J_sigma^cmp=fib(pi_sigma)`. Then

\[
\mathbb Z[\nu_\sigma]\subseteq
\operatorname{im}\bigl(H^0(J_\sigma^{\rm cmp})\to H^0(C_\sigma)\bigr)
\]

is necessary. This is a required property of a source-derived relative operation. It is not permission to adjoin a cone that forces `nu_sigma` to become a boundary. The nine mixed operations below impose additional necessary classes in the same relative kernel.

### Existence and uniqueness once the arrows are supplied

Fix the sources, targets, their actual action structures, and their normal/Čech restrictions. Let `mathbb U`, `mathbb P`, and `mathbb Z` be the full linear deformation complexes of the coefficient, physical, and comparison diagrams. They are totalized derived Hom complexes; their bar, Čech, and group directions are retained. Define

\[
\mathbb F=
\operatorname{fib}\bigl(\mathbb U\oplus\mathbb P
\xrightarrow{u_*-b_*}\mathbb Z\bigr).
\]

For an affine discrepancy `o in Z^0(mathbb Z)`, existence requires

\[
[o]\in\operatorname{im}\bigl(H^0(\mathbb U\oplus\mathbb P)\to H^0(\mathbb Z)\bigr).
\]

Equivalently, its connecting obstruction in `H^1(mathbb F)` vanishes. With both endpoint objects fixed, this reduces to `[o]=0` in the actual comparison complex. [M3]

If inhabited, the linear space of solutions is a torsor for the mapping space of `mathbb F`; its homotopy groups are

\[
\pi_n\simeq H^{-n}(\mathbb F),\qquad n\ge1,
\]

and its components form an `H^0(mathbb F)` torsor. If the module/action structures themselves vary, their deformation problem is nonlinear and these groups are only the fixed-structure fibre or tangent calculation. No physical global rank or parity is inferred before `b` exists.

## 6. Nine relative-operation tests

The user's 49-generator Hopf-kernel theorem is retained as an established input. The following calculation independently reconstructs the nine quadratic tests in the native endpoint-module model. It does not claim that an action of that cohomology Hopf algebra on the actual physical target has already been constructed.

Use the quadratic native presentation

\[
\mathcal E=\Lambda_C(\xi_0,\xi_1,\xi_2)*_C
\Lambda_C(\eta_0,\eta_1,\eta_2),\qquad |\xi_i|=|\eta_j|=1.
\]

In words: there are exterior relations within each sheet and no imposed anticommutation between different sheets. Normal forms are alternating, increasing squarefree blocks. The projection to the exterior algebra on all six generators kills the mixed anticommutators. This is the native two-branch algebra model; its direct normal-word verification here is integral.

The induced endpoint modules used for the test are

\[
M_+=\mathcal E\otimes_{\Lambda(\xi)}C,
\qquad M_-=\mathcal E\otimes_{\Lambda(\eta)}C.
\]

An alternating word ending in a `xi` block is zero in `M_+`; a word ending in an `eta` block is zero in `M_-`. Let their unit vectors be `m_+` and `m_-`.

For every `i,j=0,1,2`,

\[
r_{ij}m_+=\xi_i\eta_jm_+\ne0,
\qquad
r_{ij}m_-=\eta_j\xi_i m_-\ne0.
\]

Each list consists of nine different normal words, hence nine independent classes. The program constructs both matrices: each has rank nine with unit pivots. These tests match the stated Branch B nonzero quadratic endpoint actions. They do not equate `M_sigma` with the physical state space.

A comparison taking an augmentation-source unit to either endpoint unit would need, at the first homotopy-coherent stage,

\[
\partial h_{ij}=r_{ij}m_\sigma.
\]

The right side has nonzero cohomology. No chain homotopy, and therefore no higher coherence correction, can solve this first equation while keeping those endpoint classes. This excludes the **augmentation-source / exterior-factorized comparison**, not every endpoint-to-generic map.

Indeed the reverse augmentation projection

\[
M_\sigma\longrightarrow C
\]

is an ordinary `mathcal R`-module map. It kills positive-degree operation orbits. Nontrivial endpoint actions can therefore extend over a generic augmentation **quotient**, provided the relative kernel and its action are retained. One must not mistake the permitted quotient for a forbidden equivariant unit section.

The native relative kernel contains the nine quadratic images on each side and their higher products. For example,

\[
(r_{00})^n m_+=(\xi_0\eta_0)^n m_+\ne0,
\qquad n\ge1.
\]

Thus a source intended to retain these entire native operation modules cannot replace them by a finite exterior quotient. At minimum its derived relative endpoint kernel must retain these orbit directions. This is a condition on existing coefficient/module structure, not a proposal to glue new spheres or moment-angle cells into `K`.

### A source model that retains the operation module

There is a concrete replacement for an exterior-only source resolution; its existence is not the missing geometric comparison. For the native node `mathfrak B` with conductor augmentation to `C`, use the normalized relative bar resolution of each actual sheet:

\[
(P^{\rm nat}_\sigma)^{-n}
=\mathfrak B\otimes_C\overline{\mathfrak B}^{\otimes_C n}
\otimes_C\mathfrak B_\sigma,\qquad n\ge0.
\]

Its differential multiplies adjacent factors, with alternating signs, including the final sheet action. The monomial presentations make the coefficient modules `C`-free, so this is a valid free native resolution. It has no newly admitted coefficient inverse. Its support is the labelled normalization sheet and its cohomology is that sheet in degree zero.

The derived coefficient module `RHom_mathfrak B(mathfrak B_sigma,C)` carries the native derived endomorphism action by postcomposition. The two-exterior-block description above is its specified cohomology presentation. At chain level, one must retain a dg or A-infinity enhancement; no integral formality of this enhancement is assumed. The normal block and complete seven-equation occurrence/product-Cartier block can be retained as separate derived tensor factors. No equation or determinant may be contracted merely to expose the native action.

What is still missing is an action-compatible bivariant map from that **native, supported, normally framed diagram** to the actual endpoint/Q comparison diagram. The target `K` does not acquire a native-node module structure just because its matrices are `A`-linear. This is the same missing arrow identified in Section 5, now with an explicit non-exterior source model available. The bar resolution is not a set of physical cells or a moment-angle state space.

### Degree limitation of the bare Q conclusion

The fixed primitive generic line has only the augmentation action in its currently computed homogeneous sector. Positive operations shift operation and internal degrees. This does not prove that the entire multigraded seven-state `Q` has no nontrivial operation action. Such an assertion would require maps between those other degrees and the physical chain-level realization of the algebra.

### Decomposable dihedral correction

Choose labels `xi_i=(X1,X3,X5)` and `eta_i=(X0,X4,X2)`. Then the actual six-label transformations induce

\[
r(\xi_i)=\xi_{i+1},\quad r(\eta_j)=\eta_{j-1},\qquad
s(\xi_i)=\eta_i,\quad s(\eta_i)=\xi_i.
\]

In words: indices are modulo three; `r` is the two-step hexagon rotation and `s` the endpoint-exchanging reflection. These give `r^3=s^2=1`, `srs=r^{-1}` on every word.

On the nine primitives,

\[
r(r_{ij})=r_{i+1,j-1},\qquad s(r_{ij})=r_{ji}.
\]

But take the higher primitive

\[
W=[\xi_1,[\eta_1,r_{00}]].
\]

The full substitution gives

\[
s(W)=-W+[r_{11},r_{00}]
=-W+r_{11}r_{00}-r_{00}r_{11}.
\]

The decomposable term is nonzero. It is retained in the checker, including the exact square of reflection and the mixed dihedral relation. This does not rely on pretending that `W` is a particular named member of Branch B's chosen 49-generator basis. It is a specific primitive in the same Hopf kernel, and it exhibits why an indecomposable signed-permutation table is insufficient. Full action on any word is obtained by the displayed six-generator substitution followed by native normal-form reduction.

## 7. Complete coherence equations

This section specifies the equations a full physical comparison must satisfy. The checker verifies the instantiated source, normal, and nine-operation calculations identified above. It does **not** claim to verify unknown physical maps by setting their symbols to zero.

### 7.1 Primary endpoint and comparison equations

After the explicit normalization of Section 1,

\[
\partial f=0,\qquad \partial q=g-\pi_Qf,
\]

\[
\partial h_\sigma=e_\sigma f,\qquad
\partial\theta_\sigma=a_\sigma^{\rm phys}.
\]

Here `f` and `g` have degree zero, `q` degree minus one, `h_sigma,theta_sigma` degree zero when written into unshifted endpoint targets, and their displayed boundaries degree one. The source comparison and target comparison must first make the two endpoint boundaries agree, strictly or by a supplied comparison `j_sigma^A`.

If `b_sigma` is represented by a degree-zero chain map and those boundaries agree strictly, the endpoint comparison equation is

\[
\partial k_\sigma=b_\sigma\theta_\sigma-h_\sigma c_\sigma,
\qquad |k_\sigma|=-1.
\]

If the boundaries agree only through `j_sigma^A`, its term must be subtracted on the right and `partial j_sigma^A` must equal their boundary discrepancy. The equation belongs to the total mapping cone of that square. Omitting this correction would be an unclosed equation.

Plus/minus compatibility uses the supplied normalization difference. In the strictly matched model,

\[
\partial(k_+-k_-)
=b_+\theta_+-b_-\theta_--h_+c_++h_-c_-.
\]

There is no independent reset of the minus sign. A separate joint comparison with the native normalization homotopy is also required as part of the same square/triangle diagram.

### 7.2 Čech coherences

Apply the following to the **closed tuple of primary map, its boundary map, and its endpoint homotopy** in its mapping-cone complex, denoted `boldsymbol theta`. Do not apply a closed-cocycle formula to a single unclosed endpoint cochain while dropping its boundary terms.

On chart intersections,

\[
\partial k_{ab}=\boldsymbol\theta_b-\boldsymbol\theta_a,
\]

\[
\partial k_{abc}=k_{bc}-k_{ac}+k_{ab},
\]

\[
\partial k_{abcd}=k_{bcd}-k_{acd}+k_{abd}-k_{abc}.
\]

Restrictions are understood on every term. These comparison cochains have degrees minus one, minus two, and minus three. With total Čech/Koszul signs included, the complete all-order statement is closure in the normalized Čech total complex. A nonzero cohomology class on a right-hand side is the corresponding obstruction.

### 7.3 Normal and Gysin coherence: an explicit finite test

On the odd endpoint there are actual maps

\[
f_i:K(p_T)\to K(t_1,t_3,t_5),\qquad
f_i(1)=1,\quad f_i(z_T)=(p_T/t_i)e_i,
\quad i\in T.
\]

All quotients are polynomial factors. Pair homotopies are

\[
h_{ij}(z_T)=\frac{p_T}{t_it_j}e_i\wedge e_j,
\qquad \partial h_{ij}=f_j-f_i.
\]

For `T={1,3,5}` there is a triple comparison

\[
k_{135}(z_T)=e_1\wedge e_3\wedge e_5,
\qquad
\partial k_{135}=h_{35}-h_{15}+h_{13}.
\]

These are homological degrees zero, plus one, and plus two, equivalently cohomological map degrees zero, minus one, and minus two. Tensor them with the **whole six-occurrence Koszul source**, not its degree-zero quotient. The checker verifies every equation and every central short-Rees face.

On the opposite even endpoint, a unit-preserving map with the same degree and equations would require

\[
p_T\in(t_0,t_2,t_4),
\]

which is false for these odd `T`. Thus a product-divisor source cannot simply be identified with both independent endpoint intersections. The upper-shriek/Euler comparison in Section 3 is an honest different operation and avoids claiming such a quotient map.

For any face `F` of the six-short-Rees cube, use derived restriction `L i_F^*`, implemented by the retained free and flat-localization complexes. All existing maps and comparison equations specialize as maps of complexes. If `p_T` becomes zero, `z_T` stays with zero differential; it is not deleted. Two orders of face restriction are compared by the canonical tensor associator and the induced cube coherences. No additional regular-immersion purity formula is assumed after a nontransverse specialization.

### 7.4 Rotation and reflection

With semilinear ordered-frame transport written as `g dot`, require

\[
\partial k_g=g\cdot\boldsymbol\theta-\boldsymbol\theta,
\]

\[
\partial k_{g,h}=g\cdot k_h-k_{gh}+k_g,
\]

\[
\partial k_{g,h,k}=g\cdot k_{h,k}-k_{gh,k}+k_{g,hk}-k_{g,h}.
\]

These are equations for the entire transported tuple, including its branch, occurrence, product-Cartier, Gysin determinant, and excess labels. Reflection can exchange source objects or coefficient frames; it is not assumed to fix them individually. The group bar construction supplies all higher relations. Label covariance alone does not compute physical reflection parity.

### 7.5 Mixed-operation coherence

Once actual chain actions are supplied on source and target, let `f` be a degree-zero closed comparison. For a closed operation `a`, its first compatibility is

\[
\partial h_a=\rho_Y(a)f-f\rho_X(a),\qquad |h_a|=|a|-1.
\]

For multiplication, the next compatibility is

\[
\partial k_{a,b}=h_{ab}-h_a\rho_X(b)
-(-1)^{|a|}\rho_Y(a)h_b.
\]

For three **even** quadratic operations the next equation can be written

\[
\partial l_{a,b,c}
=k_{ab,c}-k_{a,bc}+k_{a,b}\rho_X(c)-\rho_Y(a)k_{b,c}.
\]

The mixed-operation test of Section 6 fails already at the first equation for the augmentation-source unit. No higher operation term repairs a nonzero first cohomology obstruction. In a successful non-augmentation comparison, all product and higher equations must be retained, including their action on endpoint homotopies.

For a labelled algebra automorphism `phi_g`, require

\[
\partial S_{g,a}=U_g\rho(a)U_g^{-1}-\rho(\phi_g(a)).
\]

In particular, the equation for `W` contains

\[
\rho(\phi_s(W))=-\rho(W)+\rho(r_{11})\rho(r_{00})-\rho(r_{00})\rho(r_{11}).
\]

Replacing this by just `-rho(W)` discards a nonzero actual algebra term. Decomposable corrections do not force a nonlinear physical state space: a strict module over the full associative algebra can represent products. They do force retention of the full product action, or its homotopy-coherent replacement, rather than only the indecomposable linear quotient.

### 7.6 All degrees at once

Let `B mathcal R=T^c(s bar{mathcal R})` be the reduced bar coalgebra, with its signed bar differential. A homotopy-coherent module is specified by a degree-one codifferential `b_M` on `B mathcal R tensor M`; a module comparison is a degree-zero comodule map `F`. The complete operation equations are

\[
b_M^2=0,\qquad b_NF=Fb_M.
\]

Tensor this structure with the normalized Čech and group cochains and the normal-face diagram, using total-complex signs. This is the precise all-order completion of the displayed pair and triple equations. It includes the internal differential, multiplication, all operation words, their dihedral substitution, and every normal/Čech interchange. [M4]

Here a chain-level/A-infinity realization of Branch B's homology Hopf algebra on the physical target is genuinely additional data. It is not furnished by writing the bar equations, and it has not been assumed formal.

## 8. Existence and uniqueness classification obtained now

| Problem actually specified | Result |
|---|---|
| Established bare-Q coefficient lift, whole generic class fixed | contractible |
| Unframed ambient three-normal upper-shriek source in original frame | endpoints acyclic; generic degree-four line persists |
| Conormal-framed endpoint candidate | one primitive endpoint difference; no degree-four generic class on that source |
| Same-target identification with primitive plus/minus differences | empty; obstruction `(1,1)` |
| Augmentation-source unit mapped equivariantly to a native endpoint unit | impossible; nine nonzero first operation obstructions per endpoint |
| Native endpoint module projected to a generic augmentation quotient | algebraically possible; operation kernel must be retained |
| Full physical pullback with a source-derived bivariant comparison and actions | not yet determined by supplied data |

The additional indispensable data are therefore not another scalar normalization. They are a geometrically prescribed comparison of the three-normal endpoint frames with the six-occurrence/product-Cartier source, **together with** a non-exterior relative-operation module structure on its endpoint data. The new comparison must explain the fate of the explicit primitive `nu_sigma` classes and their mixed-operation orbits. The present same-target Euler-counit comparison does not do that.

This gives a falsifiable next gate: construct that single operation-compatible comparison of endpoint path diagrams and compute its image on `nu_+`, `nu_-`, and the eighteen quadratic endpoint classes. If it is faithful on the primitive endpoint differences while demanding agreement with the coefficient zero component, the computed pullback is empty. If a source-derived relative operation changes the comparison component, its kernel, Gysin degree, determinant, and full bar/Čech coherence must be exhibited.

## 9. Verification, reproduction, and limits

Run:

```sh
python check_marici_physical_endpoint_pullback.py \
  --output marici_physical_endpoint_pullback_certificate.json
```

The checker uses the Python 3 standard library and passes **824,081 counted exact assertions**. It reconstructs the target's polynomial/normal localization rules, the 128-state coefficient sources, both 1024-state endpoint sources, their counits, the full endpoint candidate cochains, and all homogeneous Hom columns used here. It performs signed-unit integral reductions on **24,891 complete Hom columns**, with no nonunit residual in the computed frames.

The endpoint algebra calculation covers four underlying seven-equation sources and two endpoint labels, both unframed and conormal-framed, before and after full central specialization. The two excess trace-channel labels are retained from the established operation; identical post-trace source matrices do not identify their earlier trace data. The 64-face checks are checks of complete specialized chain equations, not claims that the full cohomology of all 64 faces was computed. All 32 complete Hom frame/center cases and their other cohomology groups are serialized.

The nine operation matrices are calculated in the explicit native induced-module presentation. The full 49-generator freeness theorem is an established user input and is not reproved. No table of physical chain-level actions of all 49 generators is claimed. The nonzero decomposable correction is checked in the full native word algebra, including group relations.

A clean run with only the checker in a temporary directory and `PYTHONHASHSEED=47` reproduced the certificate byte for byte. Certificate SHA-256:

```text
4bffcad170e9091b7153d7d354bfcbd7e4c162c8834b719ac406767597cff6d5
```

This is executable exact verification with algebraic arguments, not proof-assistant verification. No repository files were modified. No full physical collar, full supported-Verdier equivalence, or reflection parity was declared from these tests.

## Sources

[S1] Pinned Marici source: `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`: target state degrees, differential, allowed normal inverses, and support filtration.

[S2] Pinned Marici source: `src/ledger/20260814-115 Boundary-Triad Tate Realization and the Multi-Rees Cartier Bicomplex.md`, blob `63da17cb5d641705056c5d5b9bc6f53cda72baf5`: separate Rees/conormal degree, Cartier Bockstein, and boundary of its physical interpretation.

[S3] Conversation input `marici_source_relative_excess_trace.md` and its executable checker: the established primitive bare-Q maps, exact endpoint composites, and coherent endpoint nullhomotopies. The new checker explicitly rechecks its embedded candidate matrices.

[S4] User's Branch B brief: the relative Hopf kernel, 49 primitive mixed generators, nonzero quadratic endpoint actions, and decomposable dihedral action. The nine-generator compatibility test uses the explicit native two-exterior-block algebra and induced modules, with every word normalized directly.

[M1] Stacks Project, Hom complexes, tag `0A8H`: https://stacks.math.columbia.edu/tag/0A8H .

[M2] Stacks Project, effective Cartier duality, tag `0B4B`: https://stacks.math.columbia.edu/tag/0B4B . This is a one-divisor result; the three-normal formula here is its explicitly ordered Koszul tensor iteration for independent ambient parameters.

[M3] Stacks Project, Cones and termwise split sequences, tag `014D`: https://stacks.math.columbia.edu/tag/014D .

[M4] Bernhard Keller, Introduction to A-infinity algebras and modules, arXiv:math/9910179: https://arxiv.org/abs/math/9910179 .

Further background for the native fibre-product Ext presentation: W. Frank Moore, Cohomology over fiber products of local rings, Journal of Algebra 321 (2009), 758–773, DOI `10.1016/j.jalgebra.2008.10.015`. The finite integral normal-word checks above do not rely on a field-only topological identification.
