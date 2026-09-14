# Primitive conormal column and the first framed-source matrix equations

Date: 2026-09-08  
Branch: B  
Status: target-side coefficient construction; physical endpoint map not instantiated

## 1. What is supplied and what is not

The recovered Branch A brief specifies the two-layer module E_beta,35 and its mixed continuation obstruction. The recovered Branch C brief specifies the conclusions of its framed endpoint calculation and asks for a new bivariant comparison. It does not contain the ordered differential matrices of the 128-state source or either 1024-state endpoint source. Searches of the available repository and uploaded-file sources did not recover those named matrix bundles.

This note therefore does not claim a map on either complete framed physical source. It constructs the primitive column on the target side, gives a precise first-jet compiler for the missing source equations, and proves that the conormal inclusion retains a complete relative-operation orbit in one specified derived-Hom variance. Neither the coefficient conductor resolution nor the older conductor-road resolution is substituted for the physical source.

The target calculation uses the previously declared pullback definition of D35. Its block differential is a formula for any strict models of its two defining maps. It is not a recovered numerical matrix for the complete dualizing complex. The full nonsplit dualizing object and its conductor map remain inputs.

## 2. Coefficients and the primitive column

Let C be the retained spectator coefficient ring, with beta a nonzero divisor, and let

\[
B=C[X_{13},X_{15},X_{35},X_{02},X_{04},X_{24}]/(I_+I_-),
\quad I_+=(X_{13},X_{15},X_{35}),\quad I_-=(X_{02},X_{04},X_{24}).
\]

Write I=I_++I_- and epsilon:B -> C for its conductor quotient. The spectator normal and Rees variables stay in C; this is not evaluation of those variables at zero. Where the source has already localized a short occurrence, epsilon is not a unital map on that localization. Such summands must be handled by the actual support functor, not by this polynomial coefficient compiler.

Branch A's conormal module has ordered C-basis (u,v), with

\[
X_{35}u=\beta v,\qquad X_i v=0,\qquad X_i u=0\quad(i\ne35).
\]

Thus its occurrence matrices, projection, and inclusion are

\[
N_{35}=\begin{pmatrix}0&0\\\beta&0\end{pmatrix},\qquad
N_i=0\ (i\ne35),\qquad
\pi_\beta=(1,0),\qquad j_\beta=\binom01.
\]

These give the exact B-module sequence

\[
0\longrightarrow Cv\xrightarrow{j_\beta}E_{\beta,35}
\xrightarrow{\pi_\beta}C\longrightarrow0.
\]

The letter v denotes its retained conormal generator; it is not an unframed scalar replacement.

A map C -> E_beta,35 sends one to A u+B v. Since every short occurrence annihilates its source, B-linearity forces beta A=0. Therefore

\[
\operatorname{Hom}_B(C,E_{\beta,35})=Cv.
\]

The normalized conormal inclusion is one -> v. The proposed scalar lift one -> u fails the actual 35 relation by beta v. This is a calculation for the conductor-domain map, not a claim about the primitive class of Branch C's differently framed source.

On the complete native alternating-word free resolution P_C of C, the map has only the bottom column e_empty -> v; all higher columns vanish. Every incoming first differential is multiplication by an occurrence and kills v. Higher source differentials impose no further equation on this map. The scalar column e_empty -> u instead gives the nonzero equation beta v on e_35. No occurrence or regulator inverse is used.

At beta=0 the two-layer module becomes C u direct-sum C v, and both conductor columns are allowed. That change does not split the independent nonsplit dualizing attachment.

## 3. A canonical target-side choice of p

For the declared marked pullback, set

\[
Z=\omega[2],\qquad L=C\Pi^\vee[3],\qquad
E'=E_{\beta,35}\Pi^\vee[3],\qquad
Y=Z\times^h_L E'.
\]

Here omega is the complete relative dualizing object, q:Z -> L its recorded conductor map, and E' -> L is the shifted pi_beta. The determinant and polarity factor Pi-dual is retained. This supplies a natural target-side candidate Y=D35 and p:Y -> Z; it does not determine the source-side objects A and X of the physical collar.

In cohomological conventions, a model for the homotopy pullback is

\[
Y^n=Z^n\oplus E'^n\oplus L^{n-1},
\qquad
 d_Y(z,e,h)=(d_Zz,d_Ee,qz-\pi_\beta e-d_Lh).
\]

Equivalently,

\[
d_Y=
\begin{pmatrix}
d_Z&0&0\\
0&d_E&0\\
q&-\pi_\beta&-d_L
\end{pmatrix},
\qquad p=(1,0,0).
\]

The complete d_Z and q blocks are not replaced by their cohomology or set to zero. The identities d_Z squared=0, d_E squared=0, d_L squared=0, d_L q=q d_Z and d_L pi=pi d_E prove d_Y squared=0.

The target primitive is

\[
j_{35}:Cv\Pi^\vee[3]\longrightarrow Y,
\qquad j_{35}(v)=(0,v,0).
\]

It is closed and p j35=0. Because pi_beta is degreewise surjective,

\[
\operatorname{fib}(p)\simeq Cv\Pi^\vee[3].
\]

This is a statement about the fibre of this candidate target projection. It is not a computation of the entire collar control complex or an assertion that an independently specified physical restriction equals p.

For any actual resolved endpoint source P, a map b:P -> Y consists of components (c,e,h) with

\[
\partial c=0,\qquad \partial e=0,\qquad
\partial h=qc-\pi_\beta e.
\]

The first obstruction to lifting a given c through p is the pullback of the conormal extension along qc. In fixed frames it is the composite with beta eta35, with its conormal line and degree-one shift. An ambient cohomology rank or a scalar primitive value does not evaluate that composite.

A kernel-valued candidate has the particularly explicit form

\[
b_\sigma=j_{35}\kappa_\sigma=(0,j_\beta\kappa_\sigma,0).
\]

The still-unknown part is the actual B-linear closed covector kappa_sigma on the complete framed endpoint source, including its normal and determinant factors. There is no assertion that its prescribed value on nu_sigma exists.

## 4. Compile the first source equation exactly

For an arbitrary native polynomial f, define

\[
f_0=\epsilon(f),\qquad f_{35}=\epsilon(\partial_{X_{35}}f).
\]

Its action on E_beta,35 is exactly

\[
[f]_{(u,v)}=
\begin{pmatrix}f_0&0\\\beta f_{35}&f_0\end{pmatrix}.
\]

This is exact for every polynomial, not a first-order approximation: all products of two occurrence matrices are zero. Both f0 and f35 retain the complete spectator coefficient.

Suppose, after the actual degree and line identifications, the E'-valued part of a degree-zero map is a row on free B source terms

\[
P_4\xrightarrow{D}P_3,
\qquad b_E(e_j)=A_j u+B_j v.
\]

The index 3 is the homological placement of the shifted E' module in this target choice. It is not assigned to Branch C's endpoint generator without its frame table. If its endpoint is presented as a map rather than a chain vector, the corresponding composition equations must first be formed in its actual Hom complex.

Let D0 and D35 be the entrywise conductor constant and first-35 coefficient matrices. With D having n rows and m columns, the unknowns A and B are rows of length n. The incoming chain equation is precisely

\[
A D_0=0,\qquad B D_0+\beta A D_{35}=0.
\]

For a specified cycle nu in that source degree, mapping it to v adds

\[
A\nu_0=0,\qquad B\nu_0+\beta A\nu_{35}=1.
\]

All four equations compile to

\[
\begin{pmatrix}
D_0^\top&0\\
\beta D_{35}^\top&D_0^\top\\
\nu_0^\top&0\\
\beta\nu_{35}^\top&\nu_0^\top
\end{pmatrix}
\binom{A^\top}{B^\top}
=
\begin{pmatrix}0_m\\0_m\\0\\1\end{pmatrix}.
\]

The executable function `primitive_linear_system` constructs this matrix over a supplied commutative coefficient ring. It accepts D0, D35, nu0, nu35 and the ring operations. It does not claim to solve arbitrary polynomial systems or to contain the missing physical arrays. Its instantiated diagnostic uses the full native conductor resolution's first differential, not a replacement physical source.

For the especially restrictive conormal-kernel factorization b=j35 kappa, A=0 and these become

\[
B D_0=0,\qquad B\nu_0=1.
\]

Thus the first missing physical data are concrete: the conductor restriction of the incoming differential, the conductor primitive column, and their degree/line dictionary. Allowing a general E-valued component additionally uses D35 and nu35. The full target and further support coherences may impose additional equations even when this finite test succeeds.

For an actual boundary inclusion a:A_boundary -> X, the E-components of the equation ell a=b satisfy

\[
A_X a_0=A_{\partial},\qquad
B_Xa_0+\beta A_Xa_{35}=B_{\partial}.
\]

This constructs the coefficient block to be appended once a is supplied. It does not infer a from the number of states or identify a with the primitive inclusion j35.

## 5. Relative operations on this target primitive

This section concerns right precomposition on RHom_B(C,E_beta,35). It is not identified with Branch B's contravariant postcomposition interface K(X)=RHom_B(X,C), nor with the physical endpoint modules M_sigma. A bridge between those variances is still required.

Use the established native Yoneda algebra

\[
\mathcal E_B=\Lambda_C(\xi_{13},\xi_{15},\xi_{35})
 *_C\Lambda_C(\eta_{02},\eta_{04},\eta_{24}).
\]

For a uniform label in this section write eta35 for the positive generator xi35. Choose the Yoneda convention in which the connecting homomorphism for E_beta,35 is left multiplication by beta eta35. Then the kernel of the map induced by j_beta is

\[
\ker\bigl(\operatorname{Ext}^*_B(C,Cv)
\xrightarrow{j_{\beta *}}\operatorname{Ext}^*_B(C,E_{\beta,35})\bigr)
=\beta\eta_{35}\mathcal E_B.
\]

This follows directly from the long exact sequence. Right precomposition makes the equation right E_B-linear; it does not assert that this kernel is a two-sided ideal.

The relative subalgebra satisfies

\[
\mathcal R\cap\eta_{35}\mathcal E_B=0.
\]

Proof: the established multiplication factorization E_B=R tensor H, followed by the antipode, gives a multiplication factorization H' tensor R=E_B with eta35 among the degree-one exterior basis elements of H'. Hence r -> eta35 r is injective on R. But eta35 squared=0, so left multiplication by eta35 kills every element of eta35 E_B. The intersection is therefore zero. The same conclusion holds for beta eta35 E_B.

Consequently

\[
\mathcal R\longrightarrow\operatorname{Ext}^*_B(C,E_{\beta,35}),
\qquad r\longmapsto j_{\beta *}(r)
\]

is injective. Projecting Y onto its E' component proves that the corresponding classes under j35 are also nonzero in RHom_B(C Pi-dual[3],Y), with the appropriate source line identifications for this conductor-domain statement.

Thus the conormal primitive can retain an entire relative-operation orbit even though the conormal coefficient line is rank one over C. This is an action on a resolved mapping object, not a strict positive-degree action assigned to the two-term coefficient module itself.

The executable records all 49 nested-generator images. It independently checks integral injectivity on all relative words of operation degree at most six. Arbitrary-degree injectivity is proved by the factorization argument, not by extrapolation.

### Reflection

The construction is a labelled family E_beta,k. Relabelling transports both the distinguished conormal label and its line. A reflection taking 35 to 04 maps the 35 target to the 04 target; it is not an automorphism of a fixed marked D35 without additional reflected-target data.

For the previously recorded degree-four generator and its particular reflection permutation, the exact relation remains

\[
s(g)=-g+[r_{15,02},r_{13,04}].
\]

The product correction has nonzero image under the conormal comparison. The checker uses that particular reflection's actual transported conormal label and verifies all six labelled transports on all 49 generator images. It does not replace the correction by a signed permutation. It does not certify the unimported six-state physical compensator or its group-cochain data.

## 6. Optional intrinsic Hom calculation

This calculation is for C as source, not the missing physical source. On the dual of the complete alternating-word resolution, a cochain is alpha u+gamma v. Up to the displayed standard Hom rephasing, its differential is

\[
\partial(\alpha u+\gamma v)=\beta(\eta_{35}\alpha)v.
\]

Left multiplication by eta35 has kernel equal to its image in each positive degree. In the alternating-block basis, a word is in the kernel exactly when its first positive exterior block contains 35; those are exactly the preceding multiplication images. All nonzero columns have signed-unit entries.

Let b_n be the native word rank and let a_0=0, a_n=b_{n-1}-a_{n-1}. With beta a nonzero divisor,

\[
\operatorname{Ext}^0_B(C,E_{\beta,35})=Cv,
\qquad
\operatorname{Ext}^n_B(C,E_{\beta,35})
\cong C^{b_n}\oplus(C/(\beta))^{a_n}\quad(n\ge1).
\]

This is a coefficient-module decomposition with the separately retained internal shifts; it is not an action-compatible canonical splitting. The first a_n are 1,5,19,73,281,1081. On the beta=0 fibre the Hom differential becomes zero, and its ranks are 2 b_n. Inverting beta gives free ranks b_n. These are not the cohomology groups of the physical collar control complex.

## 7. Frame assignments and precise physical input boundary

The following assignments are determined by this calculation:

| Datum | Assignment |
|---|---|
| Candidate target Y | Declared marked pullback D35 |
| Candidate target Z | Complete omega[2] |
| Target restriction p | Projection (z,e,h) -> z |
| Its relative coefficient line | Cv Pi-dual[3] |
| Primitive target column | (0,v,0) |
| Homological placement | Three for the displayed shifted coefficient module |
| Weight relation | wt(v)=wt(u)+wt(X35)-wt(beta) |
| Row-Rees bookkeeping | All displayed structural maps have lambda-degree zero |
| Reflection | Transport of the entire labelled target family |

The following are not assigned: the complete physical A and X, the boundary map a, the endpoint covectors kappa_plus and kappa_minus, and isomorphisms between their actual determinant/excess/normal-cube lines and the displayed target line. The 128/1024 state counts do not determine them.

In particular, there is no justified simultaneous identification of the two physical primitive endpoints with the single vector v. Separate endpoint frames and their support maps must be used. Nor does existence of a kernel-valued target primitive prove that the source's generic Q map can be retained through the same map.

The first numerical physical block to supply is D0 together with nu0 in their ordered source bases; the general E-valued comparison also needs D35 and nu35. Source generators in other total degrees, incoming endpoint maps, and their normal/Cech/group and operation intertwiners are then used in the remaining equations. When an ambient free source rather than a B-free source is supplied, the appropriate derived comparison must first identify the B-linear Hom problem.

All physical control groups H1, H0 and H-minus-one remain unset. This note proves neither existence nor nonexistence of the requested complete bivariant physical endpoint map.

## 8. Verification and reproduction

Run:

```sh
python check_marici_primitive_conormal_column_20260908.py \
  --output marici_primitive_conormal_column_certificate_20260908.json
```

The default run passed 80,087 exact assertions. It checks the actual two-layer occurrence matrices, primitive relations, the native resolution differential, the independently transposed Hom differential, all 49 relative generators and words through degree six, the decomposable reflection relation and family covariance, the formal pullback block identities, and the first-jet system compiler. Its certificate explicitly leaves the physical source map a, physical endpoint covectors and physical control groups unset.

The native resolution is checked through degree seven. Its all-degree exactness is the established alternating-word resolution theorem; the all-degree operation conclusion uses the retained Hopf-module factorization. The pullback identities are formal identities of full differential blocks, not a test of numerical matrices for the missing dualizing model. No proof-assistant verification or repository update is claimed.

## Source record

- Branch A task brief, uploaded 2026-09-08 13:17 UTC: *Two-grade duality and obstructed conormal-extension leg of the physical-collar pullback*. Supplies E_beta,35, its lines and the distinction between coefficient trace and physical endpoint comparison.
- Branch C task brief, uploaded 2026-09-08 14:04 UTC: *Construct the comparison-fibre Hom complex and test the minimal bivariant endpoint map*. References `marici_physical_endpoint_pullback.md`, states the framed endpoint obstruction, and requests the new bivariant map. The brief is not the 128/1024-state matrix bundle.
- Retained `marici_operation_collar_interface_20260908.md`, `marici_relative_operation_fibre_20260908.md`, and `marici_collar_control_audit_20260908.md`: native resolution, operation algebra, factorization, variance and earlier missing-input boundary.
- The previously declared D35 homotopy-pullback definition is used as the target-side model. Its current full physical strict matrix and frame bundle was not retrieved.
- Stacks Project, *Hom complexes*, tag 0A8H; *Extensions*, tag 010I; *Cones and termwise split sequences*, tag 014D. These support the standard Hom, connecting-map and cone conventions; the explicit calculations above are performed here.
