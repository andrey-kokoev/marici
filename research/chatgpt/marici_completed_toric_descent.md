# Completed normal-dual descent of the whole Cartier–endpoint comparison

Date: 2026-09-07  
Project: Marici  
Continuation of `marici_toric_excess_proper_descent.md` and `marici_completed_normal_dual_comparison.md`  
Pinned source commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## 1. Result and exact category

The finite proper-descent construction extends to the **entire derived normal-dual inverse system**. The completed object is not assumed perfect. Proper duality, together with limits taken in the quasi-coherent derived category, supplies the extension.

The conclusion concerns the existing ambient coefficient-ring derived dual. It includes the original 215-state target, its endpoint/short-support/generic diagram, the whole native-source Cartier comparison, and the two endpoint composites. It is not an identification with an independently prescribed physical supported-Verdier functor or with differently framed physical collar maps.

There are three new conclusions.

1. The completed dual on the modification has canonical proper trace back to the original completed dual, and that trace is an equivalence. The complete reverse Cartier comparison descends to the dual of the already constructed pair `(F,A)`, not merely to its generic scalar value.
2. After derived restriction to the original three-long-Rees center, the completed generic dual is four free coefficient lines in cohomological degree three. There is no extra first-derived-limit term in this calculation. The normalized reverse trace is still zero there; the coupled Cartier morphism still retains its upper endpoint component.
3. A chartwise formal-power-series shortcut is false, even on a chart of this same modification. An explicit formal series proves that naive local completion and pullback cannot replace the quasi-coherent derived-limit construction.

Here and below, `D_qc` means the unbounded derived category with quasi-coherent cohomology, or its stable infinity-category enhancement. Its limits are intrinsic to that category. For arbitrary nonperfect inputs, an internal Hom in this category includes the derived quasi-coherator. Neither its limits nor its internal Hom are silently identified with their counterparts in the category of all sheaves. References [M1–M4] explain the necessary distinction.

## 2. Fixed geometry, coefficients, and complete map

Let S be the regular Noetherian polynomial spectator ring used in the preceding construction, allowing its stated monodromy-unit localizations. The intrinsic singular normalization ring is a module source, not the ambient base for this assertion. Set

\[
R=S[t_0,t_1,t_2],\qquad X=\operatorname{Spec}R,\qquad
\tau=t_0t_1t_2.
\]

In words: these three indices denote the long-Rees parameters for D03, D14, D25. The six short-normal parameters and the independent selected short excess remain separate.

The proper morphism `b:Y -> X` is the blowup of the origin, followed by blowup of the three disjoint strict transforms of the axes. Its six affine charts have

\[
t_i=s,\qquad t_j=sr,\qquad t_k=srq.
\]

In words: `(i,j,k)` ranges over permutations of the three long labels. Its relative Jacobian and residual Cartier equation are

\[
g=s^2r,\qquad z=srq,\qquad \tau=gz.
\]

In words: the line and its transition functions, not division in the original base ring, explain this factorization. Let

\[
\omega_b=b^!\mathcal O_X=\omega_{Y/X},\qquad
\mathcal I_D=\tau\omega_b\subset\mathcal O_Y.
\]

In words: the relative dualizing complex is an invertible sheaf in degree zero; multiplication by the specified section tau identifies it with the residual Cartier ideal. This was proved with the explicit chart and bundle transitions in the preceding derivation.

Both schemes are smooth of relative dimension three over S. The graph of b in `Y x_S X` is a regular immersion of codimension three, and the projection to X is smooth of relative dimension three. Thus b is perfect of virtual relative dimension zero, as well as proper. The proper-perfect duality theorem applies to **all** objects of `D_qc(X)`, not only to perfect objects [M1, M2]:

\[
b^!C\simeq Lb^*C\otimes\omega_b.
\]

In words: this is the actual right adjoint of proper pushforward for this morphism. No assertion about a nonproper shriek functor is substituted here.

The established geometric calculation gives, with the canonical maps,

\[
\mathcal O_X\xrightarrow{\sim}Rb_*\mathcal O_Y,\qquad
Rb_*\omega_b\xrightarrow{\operatorname{Tr}_b}\mathcal O_X.
\]

Both arrows are equivalences. In words: the structure-sheaf map is the identity on the birational open, and the duality trace is its dual. For the explicit model, the first result also follows from the description `Y=Tot_Z O_Z(-H)` and the vanishing of higher cohomology of nonnegative projective twists. The preceding four-term exceptional-surface Cech residue fixes the trace coefficient to one. No new normalization is imposed in the present calculation.

Let P be the native fifty-generator free resolution. Its two sheet maps are `f_+` and `f_-`. Write K for the finite target at order one, and write

\[
\mathcal A=a_+f_+-a_-f_-,\qquad
D_{\operatorname{Hom}}F=\tau\mathcal A,\qquad
D_{\operatorname{Hom}}\mathcal A=0.
\]

In words: F contains all forty-three cap terms. The degree-three cochain A contains all six terms of the two native endpoint composites. A here denotes a cochain, not a coefficient ring.

The corresponding closed map uses the complete two-term source

\[
C_\tau=[R\xrightarrow{\tau}R],\qquad
\Phi:P\otimes C_\tau\longrightarrow K.
\]

The two terms of `C_tau` are in cohomological degrees two and three. In words: the evaluation map has components F and A, so the endpoint comparison is part of a single chain map.

## 3. The normal system and its completed dual

For each independent positive order vector `n=(n_a)`, keep the same 215 labelled states `(S,H)`. The finite normal-resolution differential is

\[
\begin{aligned}
\partial_{\mathbf n}[S,H]
={}&\sum_{a\notin S}\epsilon(S,a)X_a u_a^{n_a-1}[S\cup\{a\},H]\\
&+(-1)^{3-|S|}\sum_{h\in H}(-1)^{\operatorname{pos}_H(h)}u_h^{n_h}[S,H\setminus\{h\}],
\end{aligned}
\]

where the first sum is over compatible additions. In words: every state remains free at finite order, and both incidence types retain the source's polynomial coefficients and signs.

For `m>=n`, the transition is

\[
j_{\mathbf n,\mathbf m}[S,H]
=\left(\prod_{a\in S\setminus H}u_a^{m_a-n_a}\right)[S,H].
\]

In words: only the unmarked normal coordinates of the target state occur in the transition. The identities

\[
\partial_{\mathbf m}j_{\mathbf n,\mathbf m}
=j_{\mathbf n,\mathbf m}\partial_{\mathbf n},\qquad
j_{\mathbf m,\mathbf l}j_{\mathbf n,\mathbf m}=j_{\mathbf n,\mathbf l}
\]

hold because the corresponding exponent sums agree in every source incidence. This proves the all-order identities. The executable also checks actual anisotropic orders and every state.

The colimit recovers precisely the supplied localization modules

\[
K_\infty=\operatorname*{colim}_{\mathbf n}K_{\mathbf n},\qquad
(K_\infty)_{S,H}=R[u_a^{-1}:a\in S\setminus H].
\]

In words: no normal inverse is introduced on a marked state, and occurrence coefficients remain polynomial. Long coordinates are then replaced by their declared products `u_i=X_i t_i`. The same tower and colimit identities survive that coefficient change. Diagonal orders are cofinal.

Every support subquotient has its own compatible tower. Denote any one of `K,V,B,E=K/V,Q=K/B` by T. On X, define

\[
\mathcal D_X(T)
=R\operatorname{Hom}_R(T_\infty,R)
\simeq R\!\lim_n\operatorname{Hom}_R(T_n,R).
\]

In words: this is the actual ambient ring-derived dual from the previous normal-completion calculation, regarded as a quasi-coherent derived object on affine X. Its inverse-limit terms are retained.

Define its modification-side counterpart by

\[
\mathcal D_Y(T)
=R\!\lim_n^{\mathrm{qc}}
R\mathcal Hom_Y(Lb^*T_n,\omega_b).
\]

In words: finite-stage sheaf duals are ordinary derived internal Homs because their first inputs are perfect. The infinite limit is taken in `D_qc(Y)`.

### Completed descent theorem

There are canonical compatible equivalences

\[
\mathcal D_Y(T)\simeq b^!\mathcal D_X(T),\qquad
Rb_*\mathcal D_Y(T)\xrightarrow{\sim}\mathcal D_X(T).
\]

In words: the proper trace extends to the full completed object, preserving every support subquotient and its connecting maps.

**Proof.** At every finite stage, perfect duality gives

\[
R\mathcal Hom_Y(Lb^*T_n,\omega_b)
\simeq b^!\operatorname{Hom}_R(T_n,R).
\]

In words: the finite normal complex is perfect; this does not assert that its completed dual is perfect. The functor `b^!` is a right adjoint, so it preserves the intrinsic derived inverse limit. This gives the first equivalence.

For any `C` in `D_qc(X)`, the projection formula and proper-perfect duality give

\[
Rb_*b^!C
\simeq Rb_*(Lb^*C\otimes\omega_b)
\simeq C\otimes_R^L Rb_*\omega_b
\xrightarrow{\sim}C.
\]

In words: the equivalence is exactly the counit trace, since the pullback–duality comparison is defined using that trace [M1, M3]. Apply it to the completed object. Alternatively, both `Rb_*` and `b^!` preserve the relevant limits, and their finite-stage traces form the same equivalence after taking the limit. No Mittag-Leffler assumption on the full 215-state tower is required for this theorem: its derived limit is kept rather than replaced by an underived limit.

The object also has the intrinsic description

\[
\mathcal D_Y(T)
\simeq R\mathcal Hom_Y^{\mathrm{qc}}(Lb^*T_\infty,\omega_b).
\]

In words: internal Hom turns the colimit in its first argument into a limit. Thus the constructed object is not an arbitrary completion assembled from chart power series. Proper duality for arbitrary quasi-coherent inputs has exactly this quasi-coherator qualification [M4].

## 4. The completed theorem applies to the whole coupled map

The finite cap and endpoint maps satisfy

\[
\Phi_n=j_{1,n}\Phi_1.
\]

In words: the entire hundred-column native/Cartier evaluation map, including the upper endpoint cochain, is already defined at the first normal stage. Its subsequent representatives are related by the actual transitions.

The source on Y is

\[
S_Y=Lb^*P\otimes[\mathcal I_D\hookrightarrow\mathcal O_Y].
\]

In words: this is not assumed to be the ordinary pullback of `P tensor C_tau`. Its lower line is the actual residual Cartier ideal. On every chart and every normal stage,

\[
\Phi_{Y,n}(z\otimes p)=\widehat F_n(p),\qquad
\Phi_{Y,n}(1\otimes p)=\mathcal A_n(p),\qquad
b^*F_n=g\widehat F_n.
\]

In words: the Jacobian transition acts on the complete lower map, while both native endpoint composites remain in the upper degree. These maps form one compatible direct system with fixed source `S_Y`.

Dualizing the full maps and taking the inverse limit gives

\[
\Psi_Y:\mathcal D_Y(K)
\longrightarrow R\mathcal Hom_Y(S_Y,\omega_b).
\]

In words: both endpoint composites and their source maps remain present before the limit. The map factors through the first dual normal stage, since every forward map factors through that first stage.

The previously proved proper descent of the source is

\[
Rb_*S_Y\simeq P\otimes C_\tau.
\]

In words: the original product-Cartier differential returns; no unit differential is substituted. Proper duality and its naturality identify

\[
Rb_*R\mathcal Hom_Y(S_Y,\omega_b)
\simeq R\operatorname{Hom}_R(P\otimes C_\tau,R).
\]

In words: the whole source is perfect and its proper image is perfect; the duality isomorphism carries the actual comparison maps [M4]. Under these identifications,

\[
Rb_*\Psi_Y=\Psi_X,
\]

where `Psi_X` is the derived dual of the original complete `(F,A)` map. In words: the completed construction descends exactly, not only on generic or endpoint cohomology.

The executable reconstructs fourteen independent normal orders. At each order it checks every column of the complete map and its dual, all six blowup charts, the two endpoint factorizations separately, and the transition factorization through stage one. These polynomial checks verify the specified source coefficients. The all-order conclusion is the exponent law and functorial proof above, not extrapolation from fourteen samples.

## 5. Mapping spaces and the proposed infinity-groupoid

The trace equivalence proves that `b^!` is fully faithful. Indeed, adjunction gives

\[
\operatorname{Map}_Y(b^!C,b^!D)
\simeq\operatorname{Map}_X(Rb_*b^!C,D)
\simeq\operatorname{Map}_X(C,D).
\]

In words: all comparison morphisms and higher homotopies are retained, not just cohomology groups. The same assertion holds for diagrams:

\[
\operatorname{Map}_{\operatorname{Fun}(J,D_{\mathrm{qc}}(X))}(S,T)
\simeq
\operatorname{Map}_{\operatorname{Fun}(J,D_{\mathrm{qc}}(Y))}(b^!S,b^!T).
\]

In words: transport the whole source and target diagrams, including their prescribed endpoint and generic data. Their relative homotopy fibres are then equivalent as well. This covers the completed normal diagram and its already admitted coherent transports.

The restriction is important. Every framing source must also be transported. In particular the original unit object becomes `b^!O_X=omega_b`; replacing it by an unrelated trivial line changes the marking problem. Nor is `b^!` essentially surjective onto all objects on Y. Additional exceptional objects are not silently admitted as new replacements for the fixed comparison.

Thus this normal-space modification introduces no new ambiguity into the correctly transported completed comparison problem. It cannot select a physical parity that has not been specified by the original physical collar data.

## 6. The original central fibre of the completed generic dual

Let `Z` now denote a subset of the three long labels, not the exceptional surface. Write

\[
R_Z=R/(t_i:i\in Z).
\]

In words: these are the eight original coordinate faces of long-Rees space. Each is a perfect R-module, with its finite Koszul resolution. Therefore tensoring with it preserves derived limits; a perfect object is dualizable, so its tensor functor is also a right adjoint.

In particular,

\[
R_Z\otimes_R^L\mathcal D_X(Q)
\simeq R\!\lim_n
\left(R_Z\otimes_R\operatorname{Hom}_R(Q_n,R)\right).
\]

In words: this interchange is justified by the **perfect base-change module**, not by perfection of the completed generic object. We do not use a false ordinary base-change assertion for the underived exceptional fibre of b.

The generic dual at stage n has three degree-two columns and four degree-three columns. In the ordered degree-three basis `(T^vee,M_0^vee,M_1^vee,M_2^vee)`, its relations are

\[
X_i(t_iX_i)^{n-1}(T^\vee+t_iM_i^\vee),\qquad i=0,1,2.
\]

In words: the marked coefficient in each relation is unique to that relation. The transition is multiplication by `t_i X_i` on its degree-two column, and the identity on all four degree-three columns.

For `n>=2` and `i in Z`, both the differential and transition of that degree-two column are zero. Those columns form a direct summand tower killed by one transition. Its derived limit is zero: in the standard product model for `Rlim`, the map `1-shift` on that summand is literally the identity [M5]. This is a strict pro-zero splitting, not an informal deletion of a normal state.

The remaining differential is injective because each column has a private marked coefficient `(t_i X_i)^n` that is nonzero in the remaining polynomial ring. Its cokernel transitions are surjective, since the four top columns have identity transitions. Thus no first-derived-limit cohomology remains in this generic calculation [M5].

At the full center, with `R_0=R/(t_0,t_1,t_2)`, all three degree-two columns disappear by this pro-zero argument. Hence

\[
R_0\otimes_R^L\mathcal D_X(Q)\simeq R_0^{\oplus4}[-3].
\]

In words: four generic covectors survive in cohomological degree three and there is no other cohomology. Completion has not made the generic dual object vanish. What vanishes is the particular reverse comparison map.

### Exact trace image after completion

After the existing principal long-occurrence-line pairing, the trace row is

\[
\psi(T^\vee)=\tau\xi,\qquad
\psi(M_i^\vee)=-\prod_{j\ne i}t_j\,\xi.
\]

In words: xi is the native conductor frame. The map still factors through the first finite normal stage. Every polynomial top covector gives a compatible tower element, while the entire kernel of that projection is killed by this trace. Consequently its exact completed image is still

\[
\operatorname{im}\psi=(t_1t_2,t_0t_2,t_0t_1)\,\xi.
\]

In words: there is no new unit-valued covector supplied by completion. On a face `t_i=0`, the image is generated by the product of the other two parameters. On any two-parameter face, including the full center, the map is zero.

For the complete Cartier morphism, the central specialization remains

\[
(F,\mathcal A)|_{t_0=t_1=t_2=0}=(0,\mathcal A).
\]

In words: the generic lower component vanishes, but the upper endpoint extension retains all six native endpoint-composite terms. The completed trace calculation gives no mechanism for replacing this zero lower map by a unit. It also does not erase the upper extension.

## 7. A concrete reason naive chartwise completion is unsafe

Consider the same chart

\[
t_0=s,\qquad t_1=sr,\qquad t_2=srq.
\]

In words: this is one of the six actual charts, not a different auxiliary geometry. For the simple test tower `R/(t_0^n)`, the base inverse limit is `S[t_1,t_2][[t_0]]`, whereas the chartwise inverse limit is `S[r,q][[s]]`.

The natural map

\[
S[s,r,q]\otimes_{S[t_0,t_1,t_2]}S[t_1,t_2][[t_0]]
\longrightarrow S[r,q][[s]]
\]

is not surjective. In words: ordinary pullback of the completed base module is not arbitrary completion in the chart coordinates.

A specific missing element is

\[
f(s,r)=\sum_{n\ge0}s^n r^{n^2}.
\]

In words: it is a legitimate formal s-adic series, with a finite polynomial coefficient at each s-degree. It is not a convergence claim.

To prove non-surjectivity, a base monomial `t_0^a t_1^b t_2^c` becomes `s^(a+b+c) r^(b+c) q^c`. Its r-exponent minus its s-exponent is `-a`, hence nonpositive. Multiplying by a fixed chart polynomial changes this difference by a uniformly bounded amount. Every element of the tensor product is a finite sum of such products, so every monomial in its image has a common upper bound on that exponent difference. In f the differences are `n^2-n`, which are unbounded. Cancellation cannot create terms outside the union of the bounded supports. This proves the claim for every proposed tensor representative.

There is no contradiction with Section 3. Limits in `D_qc(Y)` include the derived quasi-coherator of the sheafwise limit. Restriction to one affine chart need not preserve such intrinsic limits. The relation is precisely the one stated in Stacks tag 0CSB [M6]. The theorem uses the quasi-coherent category appropriate to the ambient ring-derived dual, not a sheafwise collection of all local power series.

This control does not claim that the particular completed Marici dual has every pathology of an arbitrary completion. It rejects the general interchange that would have been needed to replace the proved global functor by a naive chart procedure.

## 8. Excess and remaining physical scope

Tensoring with the original three-equation Koszul packet, or with the independently identified finite exterior factor `Lambda(eta)`, commutes with the inverse limit because those factors are perfect. Proper trace remains the identity on eta. The two geometric long-excess directions are still the nontrivial bundle computed previously; neither is identified with eta. No ordinary replacement of the derived exceptional fibre is used.

The completed theorem is compatible with the full quadratic/cubic coupling, the two endpoint maps, and every existing support triangle. It closes the finite-to-completed normal-space descent gap for this ambient coefficient construction.

It does not provide the remaining identification of the independent short excess with the two physical collar inputs, nor identify the entire ambient quasi-coherent dual with the intended constructible/support-PC Verdier functor. Those are different categories and different comparison data. Physical reflection parity is therefore still unassigned. The completed proper modification itself does not add a further unknown to the fixed comparison problem.

## 9. Reproduction, verification, and proof boundary

Run:

```sh
python check_marici_completed_toric_descent.py \
  --output marici_completed_toric_descent_certificate.json
```

The self-contained standard-library checker passes **107,071 exact assertions**. It reconstructs the actual native and target differentials and does not read success flags from older certificates. It checks fourteen independent normal orders, all 215 target states, all hundred source columns of the whole Cartier/native map, every corresponding dual column, all six chart maps at each order, both endpoint factorizations, the stage-one reverse factorization, all eight perfect central base changes, and the strict pro-zero splittings of the generic towers.

The proof of the infinite-limit theorem uses proper-perfect duality and right-adjoint limit preservation. The proof of the chartwise counterexample uses an unbounded exponent invariant. Finite assertions are not presented as proofs of either theorem. No proof assistant was used, and no repository file was modified.

## 10. Sources

### Fixed project data

- `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`: literal 215-state differential and permitted localizations; refetched at the pinned commit during this computation.
- `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`, blob `840258522d45e450e4f1e8bb927d9aae58c75566`: native source and coupled endpoint maps.
- `research/voevodsky/check_two_endpoint_tate_carrier.rs`, blob `0147e2e42dafac0da7289c571cb0331b51338be1`: endpoint support labels.
- Supplied derivations `marici_completed_normal_dual_comparison.md`, `marici_toric_rees_cartier_endpoint_comparison.md`, and `marici_toric_excess_proper_descent.md`: finite tower, normal-space modification, exact line identities, and primitive trace. The current checker independently reconstructs the finite coefficient equations needed here.

### Primary mathematical references

[M1] Stacks Project, Section 48.13, *Right adjoint of pushforward for perfect proper morphisms*, tag `0AA9`, especially Lemma 48.13.3. The arbitrary-object pullback/duality formula is used under the stated proper and perfect hypotheses; the flat-only version would not suffice.

[M2] Joseph Lipman and Amnon Neeman, *Quasi-perfect scheme-maps and boundedness of the twisted inverse image functor*, arXiv `math/0611760v2`, Theorem 1.2 and Proposition 2.1. This independently supplies the unbounded quasi-coherent formulation.

[M3] Stacks Project, Lemma 36.22.1, *Projection formula*, tag `08EU`; Section 48.8, tag `0B6N`, for the trace-defined pullback comparison.

[M4] Stacks Project, Lemma 48.3.6, tag `0A9Q`, for proper internal duality after the derived quasi-coherator. Its qualification is retained, not discarded.

[M5] Stacks Project, Section 15.88, *Rlim of abelian groups*, tag `07KV`, for the product model of the derived limit and the Mittag-Leffler vanishing used in the explicit generic calculation.

[M6] Stacks Project, Example 36.21.5, tag `0CSB`, for the distinction between limits in the quasi-coherent derived category and sheafwise limits. See also Lemma 36.10.8, tag `0A6H`, for when ordinary sheaf internal Hom is quasi-coherent; those perfection hypotheses are not silently applied to the completed object.
