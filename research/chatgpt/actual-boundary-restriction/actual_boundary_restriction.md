# Endpoint/Q boundary restriction and its secondary class

Date: 2026-09-06. Source commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

## Scope and result

The complete source-defined K6 original-twist support flag, and its target-side Borel–Moore–Čech realization, determine an explicit coefficient boundary map. It has seven quotient columns and twelve columns into each endpoint packet. No endpoint normal degree is removed.

For the canonical connecting class of the top Q-cycle, this map gives the secondary representative `h-r(s)=(-theta,0,0)` when the literal zero boundary is framed by its zero homotopy. Its exact indeterminacy is multiplication by the product of the six short normal parameters. Thus this particular framed class is nonzero, with annihilator that product. A general boundary homotopy changes the result to `lambda-1` modulo that product.

This is an explicit instantiation of the preceding mapping-fibre test for the canonical Q-extension. It is not an identification with the full normalization-source/physical Gysin comparison. That problem still requires its source, comparison, and independently constructed endpoint comparison homotopies. In particular, the target's connecting morphisms computed here must not be renamed as those missing source-to-target homotopies.

The source probe in this calculation is one free module in homological degree two. The primitive called `s` below is the lifted Q-cycle. It is not the four-generator source contraction used in the preceding control.

## 1. Complete coefficient flag

Let D be the nine diagonals of the hexagon. Let L be its three long diagonals and S its six short diagonals:

\[
L=\{03,14,25\},\qquad S=\{02,13,24,35,04,15\}.
\]

In words: diagonal labels use the actual polygon vertices; the short variable with index i in earlier records belongs to the diagonal joining i and i+2 modulo six.

Work first over

\[
R=\mathbb Z[X_a,u_a,(1+u_a)^{-1}\mid a\in D].
\]

In words: occurrence parameters and normal parameters remain independent. Only the source Laurent units corresponding to monodromies are inverted in the base.

A loaded generator is `[F,H]`, with F a noncrossing face and H a subset of F. Its homological degree and finite differential are

\[
|[F,H]|=3-|F|+|H|,
\]

\[
\begin{aligned}
d[F,H]={}&\sum_{a\notin F\,;\,F\cup\{a\}\in K_6}
 (-1)^{\#\{b\in F:b<a\}}X_a[F\cup\{a\},H]\\
&+\sum_{a\in H}(-1)^{3-|F|+\operatorname{pos}_H(a)}
 u_a[F,H\setminus\{a\}].
\end{aligned}
\]

In words: use the source's radial occurrence maps and normal-circle boundaries, in lexical diagonal order. Positions start at zero.

Write K for the whole complex, B for the subcomplex of faces containing a short diagonal, and V for the sum of the two endpoint subcomplexes. Their endpoint faces are

\[
v_+=\{13,35,15\},\qquad v_-=\{02,24,04\}.
\]

In words: retain all eight circle states at each endpoint, not just its degree-zero vertex.

The actual counts are

\[
\operatorname{rk}K=215,\quad \operatorname{rk}B=208,\quad
\operatorname{rk}V=16.
\]

In words: these are generator counts before localization, not ranks of cohomology.

Set

\[
E=K/V,\qquad P=B/V,\qquad Q=K/B.
\]

In words: E retains the full endpoint-relative target, P its road-relative support, and Q the genuine seven-generator quotient. The degree ranks, in increasing homological degree, are:

| Complex | Degree 0 | Degree 1 | Degree 2 | Degree 3 |
|---|---:|---:|---:|---:|
| K | 14 | 63 | 93 | 45 |
| B | 14 | 63 | 90 | 41 |
| V | 2 | 6 | 6 | 2 |
| E | 12 | 57 | 87 | 43 |
| P | 12 | 57 | 84 | 39 |
| Q | 0 | 0 | 3 | 4 |

These agree with the source's support quotients. The executable reconstructs them from noncrossing faces rather than assigning the ranks.

## 2. Actual endpoint connecting maps

Let j be the graded section of E into K that retains every nonendpoint basis generator, and let p-plus and p-minus project onto the endpoint summands. This is a graded section, not a claimed chain splitting. Define

\[
\kappa_+=p_+dj,\qquad \kappa_-=p_-dj.
\]

In words: take the part of the actual boundary that enters the relevant endpoint. These are the connecting morphisms of the endpoint quotient, with their targets shifted by one.

On a basis generator, the complete formula is

\[
\kappa_\pm[F,H]=
\begin{cases}
(-1)^{\#\{b\in F:b<a\}}X_a[v_\pm,H],
 &F=v_\pm\setminus\{a\},\\
0,&\text{otherwise}.
\end{cases}
\]

In words: only a radial incidence from a two-diagonal endpoint face enters the endpoint. Normal mark removal leaves F unchanged and supplies no additional endpoint-crossing column.

There are three two-diagonal predecessors of each endpoint and four possible marking subsets on each predecessor: twelve nonzero columns per endpoint. The columns occur across three homological degrees. All twenty-four are included in the certificate.

The chain equations are

\[
d_V\kappa_\pm+\kappa_\pm d_E=0.
\]

In words: each connector is a chain map to the shifted endpoint complex, whose differential is minus the endpoint differential.

Let pi be the quotient map to Q. Define the boundary target and its restriction by

\[
\mathcal B=Q\oplus V_+[1]\oplus V_-[1],
\qquad
\rho=(\pi,\kappa_+,\kappa_-):E\longrightarrow\mathcal B.
\]

In words: retain the entire Q quotient and both endpoint connecting morphisms, with the correct connecting degree. The boundary differential is `(d_Q,-d_V,-d_V)`. It satisfies

\[
d_{\mathcal B}\rho=\rho d_E.
\]

In words: the combined boundary restriction is a chain map. Its nonzero columns number 31: seven quotient columns and twenty-four endpoint columns. Its target ranks in degrees zero through four are `(0,2,9,10,2)`.

For example, in the original-twist complex,

\[
\kappa_+[\{13,15\},H]=X_{35}[v_+,H]
\qquad(H\subseteq\{13,15\}).
\]

In words: inserting diagonal 35 gives the positive endpoint coefficient dictated by the lexical incidence orientation.

### Target-side Čech realization

On the Čech version, the coefficient module at `[F,H]` is

\[
R[u_a^{-1}:a\in F\setminus H].
\]

In words: a normal inverse is available only when that normal is present and uncircled at the target state.

The radial coefficient is `X_a/u_a` and normal mark-removal coefficient is one. The same construction of rho applies. Its endpoint formula replaces `X_a` by `X_a/u_a`; the newly inserted a is uncircled, so this inverse is legal. Input coefficient modules map by permitted localization inclusions.

The source map from the finite complex to this target multiplies `[F,H]` by the product of `u_a^{-1}` over `F\H`. The checker verifies its chain identity and its commutation with pi and both endpoint connectors on every generator. No inverse is transported back to the source or to a circled state.

## 3. Mapping restriction r and the specified comparison

Regard homological complexes as cohomological complexes by placing homological degree k in cohomological degree minus k. Let U be the free probe in homological degree two:

\[
U=R[2],\qquad
M=\operatorname{RHom}_R(U,E),\qquad
N=\operatorname{RHom}_R(U,\mathcal B),\qquad
r(g)=\rho\circ g.
\]

In words: degree-zero comparisons are degree-two cycles in E; their boundary data lie in the complete quotient-and-endpoint target. The source probe is perfect, so these derived Hom complexes are computed by the displayed chain modules.

In particular,

\[
M^n=E_{2-n},\qquad
N^n=Q_{2-n}\oplus(V_+)_{1-n}\oplus(V_-)_{1-n}.
\]

In words: these equalities fix every degree of r, not merely its effect on homology.

Let T be the empty-face generator and h-l the circled long-facet generator. Let e-l be the corresponding uncircled generator. The Q differential is

\[
d_QT=\sum_{l\in L}X_le_l,\qquad d_Qh_l=u_le_l.
\]

In words: keep the top and all three long-normal terms. In the Čech realization the corresponding coefficients are `X_l/u_l` and one, into the specified localized bottom modules.

Put

\[
U_L=\prod_{l\in L}u_l,
\qquad
\theta=U_LT-\sum_{l\in L}X_l\!\prod_{m\in L\setminus\{l\}}u_m\,h_l.
\]

In words: theta is the primitive polynomial top cycle of the complete Q complex. Its coefficient ideal has no common polynomial factor; it is not a unit coefficient on T.

Let s be its actual graded lift to E on the same four generators. Define

\[
s=\widetilde\theta,\qquad f=d_Es=\beta.
\]

In words: beta is the connecting class obtained by differentiating the lifted Q-cycle. This independently source-defined f is the comparison tested below. It is not an assertion that an unspecified physical trace equals beta.

The eighteen terms of beta are supplied in the certificate. They lie in P. Their endpoint components vanish directly: the terms have either a singleton short face or a two-diagonal face containing a long diagonal. None has the two-short face required to enter v-plus or v-minus. Consequently

\[
d_Ef=0,\qquad \rho(f)=0,\qquad \rho(s)=(\theta,0,0).
\]

In words: f is ambient-exact and has literal zero boundary; its displayed primitive moves the generic Q frame by theta but moves neither endpoint connector at this degree.

Choose the literal zero-boundary homotopy h=0. For

\[
F=\operatorname{Cone}(r)[-1],\qquad
D(a,b)=(d_Ma,r(a)-d_Nb),
\]

the residual is exactly

\[
h-r(s)=(-\theta,0,0).
\]

In words: retaining the boundary homotopy leaves the negative Q-cycle. This is a computation in the stated frame, not a numerical normalization assumption.

## 4. Compute its exact indeterminacy

A full top cycle of K is

\[
\Omega=
\sum_{F\in K_6}
(-1)^{|F|(|F|+1)/2}
\left(\prod_{a\in F}X_a\right)
\left(\prod_{a\in D\setminus F}u_a\right)[F,F].
\]

In words: all forty-five fully circled faces occur, including the two endpoints. Consecutive radial and normal contributions cancel. Its projections to E and V are denoted by Omega-E and Omega-V.

### Proof that these are all top cycles

Every degree-three chain is supported on fully circled faces. Let its coefficient on the empty face be c. The singleton equations force each `u_a` to divide `X_a c`. Independence of occurrence and normal parameters implies each `u_a` divides c, and pairwise coprimality implies the product of all nine `u_a` divides c. Every further coefficient is then forced by its radial/normal equation. They are exactly the coefficients of a common polynomial multiple of Omega. Conversely, Omega satisfies every equation. Thus

\[
H_3(K)=R\Omega.
\]

In words: the whole top-cycle module is determined, not only an exhibited submodule.

Each finite endpoint packet is the Koszul complex on its three independent normal parameters. Hence it has no positive homology. For the Čech endpoint packet, the three one-variable complexes are `R -> R[u_a^{-1}]`; the integral monomial decomposition is contractible unless all three normal exponents are negative, in which case its one remaining copy is in degree zero. This also gives no positive homology. Localization at the global monodromy units is flat and preserves these conclusions.

The exact sequence `V -> K -> E` therefore gives

\[
H_3(E)=R[\Omega_E],\qquad H_2(V_+)\oplus H_2(V_-)=0.
\]

In words: removing the endpoints introduces no new top cycles. In the Čech model every top state is fully circled and still has polynomial coefficients, so the preceding divisibility proof remains valid.

The same divisibility argument applied to the three Q equations proves

\[
H_3(Q)=R\theta.
\]

In words: every top Q cycle is a polynomial multiple of theta, including in the legal Čech target.

Define

\[
\Delta=\prod_{a\in S}u_a.
\]

In words: multiply the six short-normal parameters. The exact top restriction is

\[
\pi(\Omega_E)=\Delta\theta.
\]

In words: an interior top cycle can lift a Q-cycle precisely when its coefficient belongs to the principal ideal generated by Delta.

Thus

\[
H^{-1}(M)\xrightarrow{H^{-1}(r)}H^{-1}(N)
\cong
\left(R\xrightarrow{\,\Delta\,}R\right).
\]

In words: the endpoint summands contribute no cohomology in this degree; the Q component is multiplication by the explicitly computed product.

The required cokernel and class are

\[
\operatorname{coker}H^{-1}(r)\cong R/(\Delta),
\qquad
[h-r(s)]=-1\pmod\Delta.
\]

In words: the literal zero-framed connecting class is nonzero, and its annihilator is exactly `(Delta)`. This determines the part of the mapping-fibre cohomology that becomes zero after forgetting the frame. It does not assert that the entire mapping fibre has no other cohomology.

No nonzero integer kills this class. The quotient has normal-parameter torsion, not prime-integer torsion. Its underlying abelian group is torsion-free.

## 5. The endpoint correction in the annihilating homotopy

The endpoint summands matter even though their homology vanishes in the preceding cokernel. Their top terms are

\[
\Omega_{V_\pm}=
\left(\prod_{a\in v_\pm}X_a\right)
\left(\prod_{a\in D\setminus v_\pm}u_a\right)[v_\pm,v_\pm].
\]

In words: neither endpoint coefficient is omitted or replaced by a scalar.

Set

\[
W=\Delta\widetilde\theta-\Omega_E.
\]

In words: cancel the complete Q part, leaving an element of P in degree three. Its identities are

\[
d_EW=\Delta\beta,
\qquad
\pi(W)=0,
\qquad
(\kappa_++\kappa_-)(W)=d_V\Omega_V.
\]

In words: W kills Delta times the connecting class in the endpoint-relative target, but its boundary comparison has six nonzero endpoint terms. The certificate lists them all.

In the full mapping fibre the correct primitive is

\[
D\bigl(W,(0,-\Omega_{V_+},-\Omega_{V_-})\bigr)
=(\Delta\beta,0).
\]

In words: the two actual endpoint top terms cancel those six connector contributions. W alone is not a framed nullhomotopy. This identity is checked with the shifted endpoint signs in both the finite and Čech realizations.

This explicit primitive proves annihilation by Delta while retaining every endpoint normal degree. Exactness of the cokernel calculation proves that no smaller coefficient ideal suffices.

## 6. General boundary homotopy: what has not been selected

For this f, any supplied boundary comparison homotopy is closed. Its degree-minus-one cohomology has the form

\[
[h]=(\lambda\theta,0,0),\qquad\lambda\in R.
\]

In words: the endpoint components are boundaries in this degree; the Q component supplies the remaining coefficient. Hence the general answer is

\[
[h-r(s)]=\lambda-1\pmod\Delta.
\]

In words: the value is determined once the coherent Q part of h is supplied.

Two explicit choices have different outcomes. The literal zero homotopy gives the nonzero generator minus one. The homotopy `h=r(s)` gives the exact pair `D(s,0)` and has zero residual. Both agree with the strict equation `r(f)=0`; they differ in the retained boundary comparison data. No calculation of the strict differential, endpoint values, or Q ranks can distinguish these two framings.

The vanishing condition is exact:

\[
[h-r(s)]=0\quad\Longleftrightarrow\quad\lambda-1\in(\Delta).
\]

In words: the supplied Q homotopy must differ from the lifted Q-cycle by an interior-liftable multiple.

For `lambda=1+Delta g` and zero endpoint part, an explicit full primitive is

\[
D\bigl(\widetilde\theta+g\Omega_E,
(0,g\Omega_{V_+},g\Omega_{V_-})\bigr)
=(\beta,(\lambda\theta,0,0)).
\]

In words: the endpoint terms are again necessary. The code verifies this identity with polynomial g, not only scalar choices.

The previous conversation did not specify an independent physical h in the common filtered mapping complex. Therefore the above class cannot be reported as a computed physical defect. The canonical connecting-class calculation determines its target-side mechanism and indeterminacy.

## 7. Recompute on the Rees family

Now use the declared source graph

\[
u_a=t_aX_a,\qquad
R'=\mathbb Z[X_a,t_a,(1+t_aX_a)^{-1}\mid a\in D].
\]

In words: the normal and occurrence parameters are no longer independent. The top-cycle calculation must be repeated; tensoring the old answer and calling it saturated is invalid.

The primitive cycles are now

\[
\theta_t=
\left(\prod_{l\in L}t_l\right)T
-\sum_{l\in L}\left(\prod_{m\in L\setminus\{l\}}t_m\right)h_l,
\]

\[
\Omega_t=
\sum_{F\in K_6}(-1)^{|F|(|F|+1)/2}
\left(\prod_{a\notin F}t_a\right)[F,F].
\]

In words: cancellation of the common occurrence factors changes the primitive lattices. Every singleton top-cycle equation is `X_a(c+t_a c_a)=0`; the domain property permits cancellation of X-a in the equation, not inversion in the ring. It follows that the empty coefficient is divisible by every t-a and that these are all top cycles.

Accordingly

\[
\pi(\Omega_{t,E})=\Delta_t\theta_t,
\qquad
\Delta_t=\prod_{a\in S}t_a,
\qquad
\operatorname{coker}H^{-1}(r_t)=R'/(\Delta_t).
\]

In words: the saturated Rees obstruction is controlled by the six short Rees parameters, not by their products with occurrence coordinates.

The same endpoint formulas and the same full annihilating-homotopy identity hold, with the new Omega-t, theta-t, and Delta-t. The executable checks them directly in both original and Čech realizations. In the latter, an inverse of t-a or X-a is allowed only in a summand where the product t-a X-a has been inverted.

Where Delta-t is a unit, the explicit annihilating homotopy can be divided by it and the class vanishes. This is a localized control, not a base inversion used to obtain the main result. At a central fibre the homology can change; no exact central-fibre result is inferred by naively specializing the displayed cokernel.

## 8. Relation to the earlier four-generator contraction

The previous s-C obeyed `s_C(q)=H` and `s_C(b)=xi`. It is a homotopy of a different source complex. It is not an element of the mapping complex from U to E used here, and it does not preserve the endpoint subcomplex R-b of its own support flag.

Consequently this calculation does not silently evaluate `r(s_C)` in a category where it is not defined. The primitive used here is the actual graded lift theta-tilde, whose degree, coefficients, support, and endpoint restrictions have all been specified.

To evaluate the originally intended normalization-source/physical class, one must give that comparison's f, the common diagram model, and its independent h. The target maps above can then be applied where the source comparison has been proved to land in this target. The coefficient computation alone does not construct the mixed-variance Gysin transformation or its framed source connectors.

## Verification and provenance

Run:

```sh
python check_actual_boundary_restriction.py --output actual_boundary_restriction_certificate.json
```

The standalone script passes 9,188 exact assertions. It uses sparse untruncated Laurent polynomials and verifies all differentials, support inclusions, every endpoint connecting column, every restriction chain identity, the Koszul–Čech comparison, the complete top cycles, the eighteen-term connecting class, all six endpoint correction terms, and the full annihilating homotopy. It repeats the construction on the saturated Rees family.

All 31 restriction columns and every nonzero term of theta, beta, Omega-E, Omega-V, W, and the endpoint correction are exported. The rank-one top-cycle and exact-annihilator proofs are the divisibility and endpoint-exactness arguments above, not extrapolations from bounded testing. This is not proof-assistant verification. No repository files were modified.

Source definitions:

- `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, at the pinned commit: all 215 generators, differential signs, occurrence and normal coefficients, target-local denominator rule, and finite-to-Čech comparison.
- `src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md`: the actual endpoint/short-boundary/full support flag, its fixed quotients, and the scope of the target-side realization.
- `src/ledger/20260814-115 Boundary-Triad Tate Realization and the Multi-Rees Cartier Bicomplex.md`: independent Rees and occurrence parameters and the need to retain their conormal data.
- The preceding `framed_target_category.md`: the mapping-fibre convention and distinction between an ordinary nullhomotopy and a framed one.

General homological references:

- Stacks Project, tag `0A8H`, Hom complexes: differential on the mapping complex and its cohomological grading.
- Stacks Project, tag `014D`, cones and termwise split sequences: connecting morphisms and the cone-fibre convention.
- Stacks Project, tag `062D`, Koszul regular sequences: acyclicity in positive homological degrees for the endpoint normal resolutions.
