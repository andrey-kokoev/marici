# Normalization source and the endpoint-framed support fibre

Date: 2026-09-06. Repository inputs remain pinned to `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

## Results and scope

The previously constructed target boundary map has a simpler exact interpretation:

\[
\operatorname{fib}\bigl(E\xrightarrow{(\pi,\kappa)}Q\oplus V[1]\bigr)\simeq B.
\]

In words: retaining the quotient and the endpoint connecting homotopies reconstructs the full short-boundary support complex, including both endpoint packets. Here B is the 208-generator short-boundary complex, **not** its endpoint-relative quotient B/V. An explicit integral deformation retraction below proves the statement on every generator, with the permitted coefficient localizations unchanged.

Replacing the preceding free probe by the complete polynomial normalization–road coefficient source does not select a unique boundary homotopy. In the conductor-supported coefficient category, its secondary ambiguity is still R/(Delta), with Delta the product of the six short normals. On the recomputed Rees family it is R'/(Delta_t), with Delta_t the product of the six short Rees parameters. This conclusion remains true when derived Hom is computed over the nodal ring rather than merely over R: the extra node-resolution degrees have zero contribution to this particular secondary cokernel.

There are explicit node-linear comparisons with the same ambient map and identical strict target-boundary values, but different Q-homotopies: one is nonzero as a framed class, the other is exact. Both examples are equivariant for the source's triangle-dihedral action. This proves insufficiency of those strict coefficient data for selecting the homotopy. It does not compute an independently specified physical homotopy or identify the constructed comparisons with the full spatial Gysin functor.

## 1. Fixed target and coefficients

Use the notation of `actual_boundary_restriction.md`:

\[
V\subset B\subset K,\qquad E=K/V,\qquad P=B/V,\qquad Q=K/B.
\]

In words: V contains both endpoint normal packets, B the short-boundary support, and K the full K6 complex. Their generator counts are 16, 208, and 215. Q has seven generators. P must not be confused with the polynomial normalization source introduced below.

The independent base is

\[
R=\mathbb Z[X_a,u_a,(1+u_a)^{-1}\mid a\in\mathcal D],
\]

where the nine diagonals form the set D. In words: occurrence and normal variables remain independent; the base contains monodromy units, not normal inverses. In the target Cech realization, additional inverses of u_a are permitted only on a generator [F,H] with a in F minus H. The source's finite and Cech differentials are implemented separately, not identified through a global localization.

Let j_E:E -> K be the graded inclusion of nonendpoint generators. Let j_Q:Q -> K be the graded inclusion of quotient generators. Neither is assumed to be a chain map. The endpoint connector and short-boundary attaching map are

\[
\kappa=\operatorname{pr}_V d_Kj_E,
\qquad
\alpha=\operatorname{pr}_B d_Kj_Q.
\]

In words: each is the corresponding component of the actual differential. Both have homological degree minus one. The target boundary is

\[
\rho=(\pi,\kappa):E\longrightarrow Q\oplus V[1].
\]

In words: the endpoint shift is part of the definition. It incorporates both endpoints without truncating their normal states. These constructions use the source's K6 support flag and Koszul–Cech differential [S1,S2].

## 2. Exact contraction of the framed target

Use homological grading. The homotopy fibre F has

\[
F_n=E_n\oplus Q_{n+1}\oplus V_n,
\]

\[
d_F(e,q,v)=
\bigl(d_Ee,\ \pi e-d_Qq,\ \kappa e+d_Vv\bigr).
\]

In words: the fibre restores an endpoint coefficient and adds a shifted quotient coefficient. The signs are those of the previous cohomological mapping-fibre convention after reversing grading.

Its inclusion, projection, and homotopy are

\[
\begin{aligned}
I(b)&=(\operatorname{pr}_E b,0,\operatorname{pr}_V b),\\
\Pi(e,q,v)&=\operatorname{pr}_B e+v-\alpha q,\\
H(e,q,v)&=(j_Qq,0,0).
\end{aligned}
\]

In the third formula j_Qq is viewed in E; quotient generators are not endpoint generators. In words: projection corrects the short-boundary component by the boundary of the retained quotient homotopy. H moves a quotient-frame term to the identical ambient generator. It does not restore any spectator mark or introduce an inverse.

The complete identities are

\[
\Pi I=1,
\qquad d_FH+Hd_F=1-I\Pi,
\qquad H^2=0,
\qquad \Pi H=0,
\qquad HI=0.
\]

In words: F retracts onto B, not merely onto B's cohomology.

### Proof

Write K=B direct-sum j_Q Q as graded modules. Its differential is the block matrix with entries d_B, alpha, zero, d_Q. The identity d_K squared equals zero gives d_B alpha + alpha d_Q = 0. In these coordinates F is B_n direct-sum Q_n direct-sum Q_(n+1), with differential

\[
(b,q_0,q_1)\longmapsto
(d_Bb+\alpha q_0,\ d_Qq_0,\ q_0-d_Qq_1).
\]

The displayed maps become Pi(b,q0,q1)=b-alpha q1 and H(b,q0,q1)=(0,q1,0). Direct substitution proves every identity. This is the standard cone contraction for a termwise split quotient [M1].

The coefficient module of a quotient generator is identical to that of its ambient copy. Every term of alpha is an actual differential term into B. Consequently this contraction is permitted in both the finite and target-local Cech models. It commutes with the finite-to-Cech comparison and the supplied dihedral action. In categorical terms, it is also the iterated-fibre identity: first take the fibre of E -> V[1], obtaining K, and then the fibre of K -> Q, obtaining B.

The 222 fibre generators consist of 199 ambient endpoint-relative generators, seven shifted Q generators, and sixteen restored endpoint generators. The contraction removes the two copies of each quotient generator and leaves 208 generators.

## 3. Interpretation of the preceding secondary class

Retain theta, its graded lift s, beta, and Omega from `actual_boundary_restriction.md`. Thus

\[
d_Q\theta=0,\qquad s=j_Q\theta,\qquad
\beta=d_Ks=\alpha\theta\in B_2,
\qquad d_K\Omega=0.
\]

In words: beta is the actual connecting class of the primitive Q-cycle. Its support contains no endpoint-crossing term, so its endpoint-relative image has literal zero target boundary.

For a closed boundary homotopy with Q-class lambda theta, the framed cycle is represented by (beta,lambda theta,v). Under Pi it becomes

\[
\Pi(\beta,\lambda\theta,v)=(1-\lambda)\beta+v.
\]

In words: the residual becomes an ordinary support class in B. Over the retained base, every degree-two cycle v in the endpoint packet is an endpoint boundary and hence a boundary in B.

The previously computed top map is

\[
H_3(K)=R\Omega\longrightarrow H_3(Q)=R\theta,
\qquad \Omega\longmapsto\Delta\theta,
\qquad \Delta=\prod_{a\in\mathcal D_{\mathrm{short}}}u_a.
\]

In words: the six short-normal factors are the exact lift obstruction. The divisibility proof establishing all top cycles is in the preceding note; the present checker reruns its chain identities.

The long exact sequence for B -> K -> Q gives

\[
\ker\bigl(H_2(B)\to H_2(K)\bigr)
=R[\beta]\cong R/(\Delta),
\qquad H_3(B)=0.
\]

In words: this identifies a particular cyclic subgroup of H2(B), not necessarily all of H2(B). There is no top homology in B, because multiplication by Delta is injective over this base.

The explicit annihilating primitive now has a single support expression:

\[
Z=\Delta s-\Omega\in B_3,
\qquad d_KZ=\Delta\beta.
\]

In words: Z includes both endpoint top corrections automatically. Its endpoint-relative projection is the earlier W, and its endpoint component is minus Omega_V. Omitting those endpoint terms would not give the complete primitive.

Under the earlier identification of the secondary cokernel by h-r(s), the same class has coordinate lambda minus one. Under Pi it has the opposite coordinate, (1-lambda) beta. This is only the connecting-map sign, not a different vanishing test.

## 4. Insert the full polynomial normalization source

Keep node coordinates separate from all X, u, and t parameters. Define

\[
\mathcal A=R[z_+,z_-]/(z_+z_-),
\qquad
\mathcal N=R[z_+]\oplus R[z_-].
\]

In words: these are the two normalization branches and their node. Their normalization sequence uses the difference of conductor values, as in the source [S3].

Let r cyclically permute three road coordinates, let n(c)=(c,c,c), and let epsilon be their sum. The complete source complex C has

\[
\begin{array}{ll}
C_3=R,&d_3(c)=(0,n(c)),\\
C_2=\mathcal A\oplus R^3,&d_2(a,t)=(\nu(a),(1-r)t),\\
C_1=\mathcal N\oplus R^3,&d_1(f,g,q)=f(0)-g(0)-\epsilon(q),\\
C_0=R. &
\end{array}
\]

In words: retain node relations, both sheet functions, all road/tag terms, the norm term, and the endpoint quotient. This is the polynomial version of the source's conductor–road pullback [S3,S4], already developed in `source_defined_branch_comparison.md`.

The source-defined readout is

\[
\varphi:C\longrightarrow R[1],\qquad
\varphi_1(f,g,q)=\epsilon(q).
\]

In words: the unit is the common sheet-difference/road-sum coefficient on cycles. It is not the common constant value of a node function. The differential maps and phi are A-linear, with A acting on roads and the target through the conductor quotient A -> R.

### Explicit proof of the source quasi-isomorphism

The primitive cycle is z=((1,0);(1,0,0)); it has phi(z)=1. An R-linear contraction onto R z is as follows. Lift the degree-zero endpoint to the constant plus sheet. For an arbitrary degree-one vector (f,g;q0,q1,q2), use the node function whose two restrictions are (f-f(0)+g(0),g), and the tag vector (0,q1,q1+q2). For a degree-two vector (a;t0,t1,t2), send it to t0 times the norm generator. These give dS+Sd=1-z phi, with no division.

This proves that phi is a quasi-isomorphism; the section and contraction need not be A-linear. Positive branch powers are boundaries of the corresponding node functions, and all polynomial degrees remain present in the complex. Since phi itself is A-linear, it is a quasi-isomorphism also in D(A).

To retain the grading of the preceding R[2] test, set

\[
\mathcal S=C[1],\qquad
\varphi[1]:\mathcal S\xrightarrow{\sim}R[2].
\]

In words: the source unit is placed in homological degree two. This is the declared comparison-degree convention for the present test, not a separately derived physical Gysin degree shift.

## 5. Nodal derived Hom does not alter this obstruction degree

Let the target coefficient complexes carry the conductor A-action, so z-plus and z-minus act as zero. A free resolution of R over A is

\[
\cdots\longrightarrow\mathcal A^2
\xrightarrow{\operatorname{diag}(z_+,z_-)}\mathcal A^2
\xrightarrow{\operatorname{diag}(z_-,z_+)}\mathcal A^2
\xrightarrow{(z_+\ z_-)}\mathcal A\longrightarrow R.
\]

In words: the resolution does not terminate. Exactness follows from Ann(z-plus)=(z-minus) and Ann(z-minus)=(z-plus); no perfectness of R over the node is assumed.

For any of our bounded conductor-supported target complexes T, applying Hom from this resolution makes its node-coordinate differentials zero. Only the internal differential of T remains. Consequently, on underlying coefficient modules,

\[
H^m\operatorname{RHom}_{\mathcal A}(\mathcal S,T)
\cong H_{2-m}(T)
\oplus\bigoplus_{j\ge1}H_{2+j-m}(T)^{\oplus2}.
\]

In words: each positive node-resolution degree supplies two shifted target homology groups. For fixed m the sum is finite because the target is bounded. The standard Hom-complex grading accounts for the shifts [M2]. This formula is not a claim about equivariant-derived group cohomology.

In degree minus one, E contributes only H3(E). The boundary target Q direct-sum V[1] could also contribute two copies of H3(V), but these vanish: the complete endpoint normal sequences are regular over the retained independent or Rees base [M3]. Thus

\[
\operatorname{coker}H^{-1}\!\left(
\operatorname{RHom}_{\mathcal A}(\mathcal S,E)
\longrightarrow
\operatorname{RHom}_{\mathcal A}(\mathcal S,Q\oplus V[1])
\right)
\cong R/(\Delta).
\]

In words: replacing the free probe by the full ringed normalization source does not eliminate or fix the secondary coordinate.

The fibre equivalence gives a further conclusion:

\[
\operatorname{fib}\bigl(
\operatorname{RHom}_{\mathcal A}(\mathcal S,E)
\to\operatorname{RHom}_{\mathcal A}(\mathcal S,Q\oplus V[1])
\bigr)
\simeq\operatorname{RHom}_{\mathcal A}(\mathcal S,B).
\]

Since H3(B)=0 and B has no homological degrees above three, its mapping space has no positive homotopy groups in this grading. Its connected components are H2(B). The subgroup which becomes zero after forgetting the support frame is precisely the displayed R/(Delta).

No conclusion about specialization at vanishing normal parameters is inferred from these generic-base homology calculations. Such base changes can produce new endpoint homology.

## 6. Two explicit comparisons with different framed classes

Let psi=phi[1]. Define on the complete source

\[
f=\beta\psi,\qquad
s=\widetilde\theta\psi,\qquad
h_\lambda=(\lambda\theta\psi,0,0).
\]

In words: these formulas act on every source generator using the actual readout. Only the degree-two road-sum contributes; the sheet and node generators remain in the domain with their full differentials. The equations are

\[
d_Ms=f,\qquad r(f)=0,\qquad d_Nh_\lambda=0,
\qquad [h_\lambda-r(s)]=\lambda-1\pmod\Delta.
\]

The special cases are

\[
\lambda=0:\quad [h_0-r(s)]=-1\ne0,
\qquad
\lambda=1:\quad(f,h_1)=D(s,0).
\]

In words: the zero boundary path gives a nonzero framed class; the boundary path induced by the known primitive gives an exact framed class. The ambient f is identical, and both endpoint-homotopy components are zero in both cases. These are different coherent Q-boundary paths, not different strict endpoint values.

The source readout and theta have the same orientation character: rotation is even and reflection odd. Therefore f, s, h0, and h1 are equivariant. Symmetry does not choose between these two examples. This does not classify all equivariant mapping groups or claim that either example already has the complete physical endpoint comparison.

The source-normalized unit maps to beta for the support-valued comparison at lambda=0. Thus we have constructed an actual A-linear coefficient comparison with a nonzero secondary class, rather than merely postulating a value for h. Its nonzero class is the canonical connecting morphism of the target support sequence composed with the source readout. No claim is made that this composition is the required spatial normalization/Gysin operation.

## 7. Rees version and the remaining identification

Repeat the target construction with u_a=t_a X_a. The retraction F -> B is unchanged as a structural formula. The primitive top cycles must be recomputed; their ratio gives

\[
\Delta_t=\prod_{a\in\mathcal D_{\mathrm{short}}}t_a,
\qquad [h_\lambda-r(s)]=\lambda-1\pmod{\Delta_t}.
\]

In words: occurrence factors cancel in the top-cycle equations, without being inverted in the base. Every formula in Sections 2, 3, and 6 is checked again in the Rees finite and Cech models.

The remaining physical identification is now specific: determine which support-valued morphism from the full spatial normalization source to B is produced by the actual Gysin/recollement construction, including its Q-homotopy. The target coefficient differential, source readout, branch relations, and strict endpoint values do not supply that homotopy. The inspected normalized-blowdown checker constructs a Morse roof relation; it does not provide its map into the presently fixed coefficient frame [S5].

One cannot conclude physical nonvanishing from the existence of the lambda=0 comparison. Nor can one conclude physical vanishing from the lambda=1 comparison. Their coexistence proves that an additional independently constructed coherent comparison is necessary.

## Verification

Run:

```sh
python check_normalization_framed_support.py --output normalization_framed_support_certificate.json
```

The standalone standard-library checker passed 30,713 exact assertions. It reconstructs the original target, verifies the 222-to-208 integral contraction, all permitted localizations, dihedral covariance, the full polynomial source through branch exponent twelve without truncating multiplication, its source quasi-isomorphism identities, node linearity, and the explicit two-frame comparisons. It checks the node-resolution identities through degree fourteen; the annihilator proof establishes the unbounded resolution. All target calculations are repeated for independent and Rees coefficients, each in finite and Cech form.

The derived-Hom and nonvanishing statements use the accompanying algebraic proofs; assertion counts alone are not proof-assistant certification. No repository files were modified.

## Sources

[S1] `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`.

[S2] `src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md`, blob `02cedbb15dd385a75bab759dfcdb4daa28bd3b3c`.

[S3] `research/voevodsky/check_normalization_conductor_bimodule_kernel.py`, blob `2982163ca939dd1e09bb0b66b4229e31430e3c30`.

[S4] `research/voevodsky/check_conductor_road_endpoint_pullback.rs`, blob `cfe13e928e911f8914de6670f34cc4c8859b3402`; and the prior project artifact `source_defined_branch_comparison.md`, re-read from the File Library.

[S5] `research/voevodsky/check_d03_normalized_blowdown_counit.py`, blob `0fcbbf37a4f70dc0c2787ad7cb954287b9e97403`.

[M1] Stacks Project, Section 13.9, tag 014D, cones and termwise split sequences.

[M2] Stacks Project, Section 15.73, tag 0A8H, Hom complexes.

[M3] Stacks Project, Section 15.31, tag 062D, Koszul regular sequences.

Preceding derivation: `actual_boundary_restriction.md`; its definitions and top-cycle divisibility proof are retained. The new checker is self-contained and does not require the preceding program to be installed.
