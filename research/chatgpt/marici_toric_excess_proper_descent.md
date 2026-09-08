# Global long-Rees excess, primitive proper trace, and descent of the coupled comparison

Date: 2026-09-07  
Project: Marici  
Continuation of `marici_toric_rees_cartier_endpoint_comparison.md`  
Repository coefficients remain pinned to `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

## 1. Result and scope

The two long-Rees excess directions found in the previous calculation glue to a specific nontrivial rank-two vector bundle. Their duality-twisted proper trace is primitive, with value **one**, and uses the top excess degree. Deleting the excess before taking that trace gives zero. The independent short-normal excess passes through unchanged; neither of the two long directions can be identified with it as a global regular generator.

The full, already constructed Cartier/native map also has a computable proper descent. Its descended two-term source is the original product-Cartier complex, and its descended map is exactly the original coupled pair: the forty-three-term cap and the six-term sum of the two endpoint composites. Thus the new primitive geometric trace does not turn the previously vanishing original central generic map into a unit map. On the original central Rees face the descended lower component is zero and the upper endpoint component remains.

This is a construction in the explicit algebraic normal-space modification and its complete finite coefficient map. It does not identify that map with a separately specified full support-PC/Verdier correspondence, its physical collar comparisons, or a physical reflection parity. No commutation of proper pushforward with the infinite completed normal-dual inverse limit is assumed.

The proper-descent theorem uses actual sheaves, bundles, and derived pushforward, not only an integer transpose of a homogeneous coefficient slice. The calculation of the primitive trace includes an explicit six-chart Cech representative and an integral contraction. The all-character cohomology proof is given below; a finite weight audit is not substituted for it.

## 2. The fixed geometry and coefficient map

Let R be the polynomial spectator ring over the integers, retaining the six short occurrence variables, their independent normal parameters, the three long occurrences, and any other polynomial spectator data of the previous finite model. Original monodromy units can be added by localization. Set

\[
X=\operatorname{Spec}R[t_0,t_1,t_2],\qquad
\tau=t_0t_1t_2,\qquad
J=(t_1t_2,t_0t_2,t_0t_1).
\]

In words: here the three indices denote the long-Rees parameters, not the six short-normal labels. The base contains no inverse occurrence or Rees variable.

The morphism b from Y to X is the blowup of the Rees origin followed by blowup of the three disjoint strict transforms of its coordinate axes. Its six charts have

\[
t_i=s,\qquad t_j=sr,\qquad t_k=srq,
\qquad (i,j,k)\in S_3.
\]

In words: these are the actual affine blowup charts. The previous calculation established

\[
J\mathcal O_Y=(g),\qquad g=s^2r,\qquad
z=\tau/g=srq,\qquad
\mathcal L=J\mathcal O_Y\cong\omega_{Y/X}^{-1}.
\]

In words: the pulled-back image ideal is the relative Jacobian ideal, and z defines the residual reduced boundary D. The relative canonical line here has relative dimension zero, since both X and Y are smooth of relative dimension three over R.

The complete native source P is its fifty-generator free resolution. The target K is the original 215-state finite normal complex after the specified long-Rees substitution and the already justified principal long-occurrence-line pairing. Its endpoint and short-boundary subcomplexes remain V and B. Put

\[
\mathcal C=\underline{\operatorname{Hom}}(P,K),\qquad
A=a_+f_+-a_-f_-.
\]

In words: A retains both native sheet maps and both actual endpoint maps. The cap F has Hom degree two and A has degree three. The fixed identities are

\[
D_{\mathcal C}F=\tau A,\qquad D_{\mathcal C}A=0.
\]

In words: the two endpoint composites are the boundary of the full cap, with the product-Rees coefficient retained.

On Y the preceding normalized cap satisfies

\[
b^*F=g\widehat F,\qquad
D_{b^*\mathcal C}\widehat F=zA.
\]

In words: every term of the cap factors through the Jacobian line, and both endpoints remain in the same equation. It defines the global map

\[
\Phi_Y:\mathcal K_D=[\mathcal I_D\hookrightarrow\mathcal O_Y]
\longrightarrow b^*\mathcal C,
\qquad
\Phi_Y(z)=\widehat F,\quad \Phi_Y(1)=A,
\]

where the source terms have cohomological degrees two and three. In words: this is the complete two-term Cartier morphism already constructed; it is not a scalar trace with independently assigned endpoints.

## 3. Identify the entire exceptional geometry

Let

\[
\pi:Z=\operatorname{Bl}_{p_0,p_1,p_2}\mathbf P^2_R\longrightarrow\mathbf P^2_R,
\qquad H=\pi^*c_1(\mathcal O_{\mathbf P^2}(1)).
\]

In words: the three centers are the three coordinate sections of projective space. The origin exceptional divisor in Y is Z.

There is a global description

\[
Y\cong\operatorname{Tot}_Z\mathcal O_Z(-H).
\]

In words: the whole resolved threefold is the total space of the pulled-back tautological line, and Z is its zero section.

Proof. The first blowup is the total space of the tautological line on projective two-space. Each strict coordinate axis is the entire line fibre over one coordinate point. Blowing up these three fibres is the flat pullback of blowing up the corresponding points of the base. Hence the resulting total space is the one displayed above. This uses the usual affine blowup construction and its flat-base-change property [M1]. In particular, the second blowup centers are not contained in the first exceptional divisor; its normal line remains the pulled-back tautological line.

Consequently

\[
N_{Z/Y}=\mathcal O_Z(-H),\qquad
\omega_{Z/R}=\mathcal O_Z(-3H+E_0+E_1+E_2),
\]

\[
\mathcal W:=\omega_{Y/X}|_Z
=\mathcal O_Z(-2H+E_0+E_1+E_2).
\]

In words: E_i in these formulas are the three exceptional curves of the surface Z; they are not the endpoint quotient of the target. The second formula follows from the canonical bundle of a line-bundle total space, or directly from the six chart Jacobians. These identities preserve the ordered long-normal determinant inherited from the original coordinates.

## 4. The two excess directions form a nontrivial bundle

The original central fibre is cut out by the three functions t_i, not by the three coordinates of one resolved chart. Its pulled-back Koszul complex is locally

\[
K(s,sr,srq)\cong K(s)\otimes\Lambda(\zeta_j,\zeta_k),
\qquad
\zeta_j=e_j-re_i,\quad
\zeta_k=e_k-rq e_i.
\]

In words: the two repeated directions are closed. The basis change has determinant one, but it depends on the chart.

Their global conormal excess bundle is

\[
0\longrightarrow\mathcal F
\longrightarrow\mathcal O_Z^{\oplus3}
\xrightarrow{(v_0,v_1,v_2)}\mathcal O_Z(H)
\longrightarrow0,
\]

\[
\mathcal F\cong\pi^*\Omega^1_{\mathbf P^2_R/R}(1),
\qquad
\det\mathcal F\cong\mathcal O_Z(-H).
\]

In words: divide the three original equations by their common exceptional equation; the resulting projective coordinate row has this kernel. The exact sequence is the pulled-back, twisted Euler sequence [M2]. The original labelled conormal determinant is part of the determinant identity; the display uses its fixed ordered frame.

The transition matrices are explicit. From chart (i,j,k) to (j,i,k), the new kernel basis expressed in the old basis is

\[
\begin{pmatrix}-r^{-1}&-q\\0&1\end{pmatrix}.
\]

In words: the first new excess vector is minus r-inverse times the first old one, and the second is the old second vector minus q times the old first. Here r is inverted only on this chart overlap.

From (i,j,k) to (i,k,j) it is

\[
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

In words: the two excess vectors exchange. The checker constructs all 36 ordered overlap matrices from the original three conormals and verifies all 216 triple cocycles, not only these generators.

The relative canonical frame changes by one under the first swap and by q-inverse under the second. Therefore the product of its transition with the excess determinant is exactly the Jacobian of the surface-coordinate change. This gives the global, orientation-compatible identity

\[
\det\mathcal F\otimes\mathcal W\cong\omega_{Z/R}.
\]

In words: the top excess degree and the relative dualizing line together are the actual surface canonical line. This is the line needed for the proper trace, not an arbitrarily trivialized excess factor.

There are no nonzero global regular sections of F:

\[
H^0(Z,\mathcal F)=0.
\]

In words: the two local symbols are not two global constant generators. On global sections, the Euler row is the isomorphism from R cubed to the three coordinate sections of O(H). In particular, neither local excess vector can be identified with the independent globally framed short excess by a degree-zero regular inclusion of a trivial line.

## 5. Primitive proper trace, with the excess retained

Projective-space cohomology, the Euler sequence, and proper blowup duality give

\[
R\Gamma(Z,\mathcal O_Z)\simeq R,\qquad
R\Gamma(Z,\mathcal F)\simeq0,\qquad
R\Gamma(Z,\det\mathcal F)\simeq0,
\]

\[
R\Gamma(Z,\mathcal W)\simeq0,\qquad
R\Gamma(Z,\mathcal W\otimes\mathcal F)\simeq0,\qquad
R\Gamma(Z,\mathcal W\otimes\det\mathcal F)\simeq R[-2].
\]

In words: ordinary pushforward sees the degree-zero scalar. Duality-twisted pushforward sees only the **top** excess degree, through degree-two surface cohomology.

Here is an all-character proof. For the blowup pi, its structure sheaf has derived pushforward O, and its relative canonical bundle has the corresponding duality trace. Thus pullbacks of O, O(H), O(-H), and O(-2H) have the same cohomology as on projective space. The only relevant nonzero groups there are H-zero of O, rank one, and H-zero of O(1), rank three; O(-1) and O(-2) are acyclic [M3]. The Euler sequence then makes F acyclic. The bundles W and W(H) have cohomology dual to O(-H) and O(-2H), hence are acyclic. Tensoring the Euler sequence by W proves acyclicity of W tensor F. Finally, W tensor det F is the canonical bundle, whose degree-two trace is R. The proper birational structure-sheaf and duality facts used here are [M4] and [M5]. This proof is over the stated regular polynomial spectator base, not merely over a field of characteristic zero.

Let K_t be the original homological Koszul complex on the three t_i. Its pulled-back cohomology sheaves are

\[
\mathcal H^{-q}(Lb^*K_t)\cong i_*\Lambda^q\mathcal F,
\qquad q=0,1,2,
\]

where i is the zero-section inclusion of Z. In words: these are the actual Tor sheaves of the derived central fibre. We do **not** assume a global formal splitting of the complex into its Tor sheaves.

For its duality-twisted proper pushforward, the hypercohomology spectral sequence has just one nonzero term:

\[
E_2^{2,-2}
=H^2(Z,\mathcal W\otimes\det\mathcal F)
\cong R.
\]

In words: two units of excess degree are exactly compensated by two units of proper cohomological degree. This is why the excess can be integrated without changing the original central degree.

The canonical map is

\[
Rb_*\bigl(Lb^*K_t\otimes\omega_{Y/X}\bigr)
\xrightarrow{\operatorname{Tr}_{b,K_t}}K_t,
\]

and it is an isomorphism. In words: apply the actual proper duality trace and the projection formula to the perfect original three-equation Koszul complex [M5, M6]. After identifying K_t with the original central structure sheaf, the coefficient of this map is one in the fixed orientation.

### Explicit six-chart residue and its normalization

The exceptional surface has six toric rays, in counterclockwise order,

\[
(1,0),\ (1,1),\ (0,1),\ (-1,0),\ (-1,-1),\ (0,-1).
\]

In words: these are the three original projective rays and the three rays introduced by the point blowups. Its chart orders are

\[
(2,1,0),\ (2,0,1),\ (0,2,1),\ (0,1,2),\ (1,0,2),\ (1,2,0).
\]

In words: adjacent entries share one toric boundary ray.

In canonical weight zero, the six-chart Cech complex has ranks

\[
(0,9,20,15,6,1)
\]

in degrees zero through five. In words: a torus logarithmic two-form extends on an intersection exactly when that intersection has no remaining boundary-ray constraint. Every single chart and every adjacent pair is therefore absent in this weight.

An explicit degree-two cocycle has coefficient one on the four triples

\[
(0,1,2),\ (0,1,3),\ (0,1,4),\ (0,1,5)
\]

and zero on the other triples. In words: it is the Cech boundary of a lift of one oriented edge cochain on the hexagon; that edge cochain is not itself allowed in the canonical complex.

Signed-unit cancellation reduces it to coefficient one on the sole surviving degree-two generator. Its orientation was independently compared to the pullback of the standard three-chart projective-plane residue: that pullback has eight terms and differs from the four-term cocycle by an integral boundary. Thus

\[
\operatorname{Tr}_{Z/R}[\rho]=1.
\]

In words: there is no factor of three, six, or an averaged chart count. The trace kills every Cech boundary. All six permutations of the labelled coordinates preserve its value, including the canonical-form orientation sign.

The checker also independently computes 343 exact line-bundle Cech complexes: seven bundles over 49 character weights each. This verifies every contributing character and a surrounding symmetric window. The preceding all-character theorem, not extrapolation from that finite window, proves the unbounded statement.

### Necessary-excess control

If the derived central fibre is replaced by its ordinary structure sheaf before taking the same duality twist, the result is

\[
R\Gamma(Z,\mathcal W)=0.
\]

In words: that truncation kills the primitive proper trace. The top excess degree is necessary, not decoration.

As a separate intersection-theoretic check,

\[
c_2(\mathcal F^\vee)=H^2,\qquad
\int_{Z/R}H^2=1.
\]

In words: the excess normal bundle has top Chern number one. This agrees with the explicitly computed trace; the Chern number is not used in place of the chain and derived-pushforward calculation.

## 6. The independent short excess is preserved, not identified

Retain the actual selected short-normal factor

\[
\eta=t_3h_3^+-h_3^{03}.
\]

In words: the subscript three in this equation is the original short shared-normal label. It is unrelated to the three long indices used above. The prior unimodular source basis change makes this an independent closed exterior factor; at its short-central face it becomes minus the pair generator, not zero.

The proper trace tensors with the identity on this factor:

\[
\operatorname{Tr}_{b,K_t}\otimes1_{\Lambda(\eta)}.
\]

In words: no short-normal map is invented from either local zeta vector. The duality-twisted spectral sequence now has the two terms coming from top long excess without eta and top long excess with eta. Its total cohomology is

\[
R\oplus R\eta[1].
\]

In words: both independently labelled channels survive, with coefficient one. This is a statement about the normal-space trace of the retained source factor. It does not establish a new identification with a target internal marked state or with the separately prescribed physical collar input.

## 7. Descend the whole Cartier/native comparison

The global line identity from Section 2 is stronger than a local formula. Using the actual section tau,

\[
\mathcal I_D=\tau\,\omega_{Y/X}
\]

as invertible subsheaves of the rational function sheaf in the fixed relative-volume frame. In words: multiplication by tau identifies the relative canonical line abstractly with the residual Cartier ideal. Its embedding into O is still nontrivial.

The proper birational trace gives

\[
Rb_*\mathcal O_Y\simeq\mathcal O_X,
\qquad
Rb_*\omega_{Y/X}\simeq\mathcal O_X.
\]

In words: higher direct images vanish; the trace agrees with the identity on the dense open where b is an isomorphism. These hypotheses hold for the explicit smooth, projective birational modification of the regular excellent base [M4, M5].

It follows that

\[
Rb_*\mathcal K_D
\simeq
[\mathcal O_X\xrightarrow{\tau}\mathcal O_X]
\]

in degrees two and three. In words: proper descent restores the **original product-Cartier complex**, not a unit differential and not the three independent central Koszul equations.

The descended map is determined on the full source generators:

\[
Rb_*\Phi_Y=(F,A).
\]

In words: the lower map is exactly the original forty-three-term cap, and the upper map is exactly both endpoint composites together.

This equality does not come from scalar signatures. The global generator of the lower pushed line is tau. On a chart it is g times the local Cartier generator z, so its image is

\[
\Phi_Y(\tau)=\Phi_Y(gz)=g\widehat F=b^*F.
\]

In words: restoring the line transition recovers every cap coefficient. The upper generator is one and maps to A unchanged. The checker verifies this on every native source column, on all six charts, and for both endpoint factorizations separately. Together with the proper-direct-image vanishing, this determines the entire derived map.

### Original central base change

To compare to the original central fibre, use its perfect Koszul complex K_t through the projection formula:

\[
Rb_*(\mathcal K_D\otimes Lb^*K_t)
\simeq
(Rb_*\mathcal K_D)\otimes K_t.
\]

In words: do not replace the pulled-back three equations by s,r,q, and do not use ordinary restriction to Z as if it were the derived fibre. The identity remains valid after tensoring with the independent eta factor [M6].

After descent and derived base change to the original center, the finite free source and target allow the displayed representative to be reduced modulo the three t_i. The two map components become

\[
(F,A)|_{t_0=t_1=t_2=0}=(0,A).
\]

In words: the old cap has no order-zero coefficient and its ordinary generic image is zero; both endpoint composites remain in the upper extension channel. All six endpoint-composite terms survive. The individual framed endpoint maps retain coefficients plus one and minus one in the established source orientations.

This is compatible with the primitive excess trace. **A unit geometric trace does not imply that every coefficient-map component to which it is applied becomes nonzero.** In particular, proper descent of this complete Cartier map does not promote its local normalized generic unit into an ordinary central generic unit downstairs.

The complete tensor chain map was checked with all original central Koszul generators and both eta degrees: 1,600 source columns and 3,440 target columns per chart and on the original base. The inherited generic, endpoint, and source differentials all remain present.

## 8. What is settled and what is not

The two long excess directions are now globally identified, with their transition matrices, determinant, primitive proper trace, and interaction with the independent short excess. This closes a normal-space excess-descent calculation that the previous local basis change did not supply.

The full Cartier/native map has also been descended, rather than its generic and endpoint values treated independently. It recovers the original coupled map exactly. The output is not a new polynomial scalar normalization and does not select a physical parity.

The unresolved physical comparison is still the identification of this filtered/relative construction with the specified support-PC/Verdier correspondence and its independently framed collar two-cells. Any proposed primitive physical observable must use that retained relative or filtered structure. Ordinary principalization, proper trace, and a local unit coefficient alone do not establish such an observable. This conclusion is specific to the constructed map and its canonical proper descent; it is not a no-go for a different source-defined bivariant comparison.

The finite-level proof does not interchange proper pushforward with an unbounded completed inverse limit. Compatible finite stages can be treated separately; a claim about the full completed supported-dual kernel requires its own limit argument.

## 9. Reproduction and verification

Run:

```sh
python check_marici_toric_excess_proper_descent.py \
  --output marici_toric_excess_proper_descent_certificate.json
```

The executable is self-contained and uses the Python standard library. It embeds and reruns the preceding toric audit, then executes the new calculation.

It passed **169,549 exact assertions**: 32,428 from the rerun preceding construction and **137,121 new assertions**. These include the global excess transition matrices and all triple cocycles; the relative-canonical determinant identity; 343 integral six-chart Cech computations; a primitive trace row and its standard-projective normalization; all six trace symmetries; and the whole cap/endpoint map tensored with both excess packets.

Every matrix cancellation uses a signed unit. No proof-assistant certification is claimed. The global direct-image and all-character conclusions use the algebraic proofs above and the primary mathematical results cited below, not a finite numerical approximation.

## 10. Sources

### Supplied Marici input

The immediately preceding uploaded derivation and executable define the six-chart modification, the global Cartier map, and the actual finite native and target complexes. Their source provenance remains:

- `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`, blob `840258522d45e450e4f1e8bb927d9aae58c75566`.
- `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`.
- `research/voevodsky/check_two_endpoint_tate_carrier.rs`, blob `0147e2e42dafac0da7289c571cb0331b51338be1`.

The current executable reconstructs and checks the relevant matrices; it does not read a success flag from a previous certificate. No repository file was changed.

### Primary mathematical references

[M1] Stacks Project, *Blowing up*, tag 01OF. Affine blowup charts and flat base change. https://stacks.math.columbia.edu/tag/01OF

[M2] Stacks Project, *de Rham cohomology of projective space*, Lemma 50.11.1, tag 0FMG. Euler exact sequence over a general base ring. https://stacks.math.columbia.edu/tag/0FMG

[M3] Stacks Project, *Cohomology of projective space*, tag 01XS. Integral cohomology of the Serre twists and the standard Cech description. https://stacks.math.columbia.edu/tag/01XS

[M4] Andre Chatzistamatiou and Kay Rulling, *Vanishing of the higher direct images of the structure sheaf*, arXiv:1404.1827. Projective birational vanishing between excellent regular schemes. https://arxiv.org/abs/1404.1827

[M5] Stacks Project, Example 48.20.11, tag 0B6X. Proper trace and derived duality for normalized dualizing complexes. https://stacks.math.columbia.edu/tag/0B6X

[M6] Stacks Project, Lemma 20.54.3, tag 0B54. Projection formula with a perfect complex. https://stacks.math.columbia.edu/tag/0B54

[M7] Stacks Project, *Hom complexes*, tag 0A8H. Grading and tensor-Hom chain-map signs. https://stacks.math.columbia.edu/tag/0A8H
