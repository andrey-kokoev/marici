# Gysin normalization of the retained normal factors

Date: 2026-09-06. Repository source pinned to `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

## Result and scope

The source's one-normal Cartier block determines a primitive, integral **conormal-symbol evaluation**. Its normalized value is one after retaining the connecting degree and the dual normal line. It does not send the polynomial coefficient `t*x` to one by an ordinary specialization, ordinary residue, or unfiltered extraordinary restriction.

The factor-retaining correction from the preceding calculation was `sigma_c=w_c rho_c`. Applying Cartier restriction to that map as a map of the original free coefficient complexes makes it null-homotopic. On the source's simple-pole physical normal sector, multiplying the normalized propagator by `q_c-1` also makes its residue zero. These are direct tests against identifying the raw weighted correction with the physical residue map.

A local normal-symbol comparison is constructed below. A full filtered, support-admissible physical natural transformation on the octagon is not constructed. In particular, the new local comparison does not identify unrelated occurrence coordinates, Rees coordinates, conductor branch coordinates, and physical channel coordinates.

## 1. Source data and distinctions

Entry 115 supplies the one-normal complex

\[
A=B[t,x,(1+tx)^{-1}],\qquad
P=[Ah\xrightarrow{tx}Ap].
\]

In words: `B` contains spectator coefficients, `h` is in homological degree one, `p` in degree zero, and the normal differential is multiplication by `tx`. The only displayed inverse is the source unit `1+tx`; neither `t` nor `x` is inverted.

The same entry keeps the Cartier connecting map and its Rees symbol. Entry 111 explicitly distinguishes a map into a principal-ideal lattice from its inclusion into an ambient free module. The principal-line variance checker independently states that the Cartier scalar is an Ext-one class, not a degree-zero pullback of that inclusion. [S1–S3]

Entry 38 provides a different realization: a loaded normal circle with boundary `(q-1)p`, its nonresonant Pochhammer normalization, and the nearby-cycle simple-pole symbol. Its physical channel coordinate is `X`, not an automatically identified occurrence or Rees coordinate. [S4]

## 2. Compute the Cartier connecting symbol

Put `C=A/(x)` and `B_0=C/(t)`. On the Cartier fibre the displayed differential is zero. The first `x`-filtered connecting map is nonetheless

\[
\beta_x([h])=t[p].
\]

In words: lift the class to `P`, take its boundary `tx p`, use the known divisibility by `x`, and reduce modulo `x`. This is an operation on the filtered complex, not inversion of a scalar in `A`.

For an arbitrary regular coefficient `a(t,x)`,

\[
\beta_x([a(t,0)h])=t\,a(t,0)[p].
\]

In words: the complete spectator coefficient remains, and the Rees factor `t` has not been removed.

Let

\[
L_t=(t)/(t^2).
\]

In words: this is the conormal line of the second, Rees divisor in `Spec C`, viewed over `B_0`.

Because `beta_x` has order one in the `t` filtration, its leading symbol is the well-defined map

\[
\overline\beta_x:B_0[h]\longrightarrow L_t\otimes_{B_0}B_0[p],
\qquad \overline\beta_x(\bar a[h])=[t]\otimes\bar a[p].
\]

In words: the symbol has a conormal-valued target. Changing a representative by a multiple of `t` changes its image by a multiple of `t^2` and hence does not change this symbol.

### The shifted Gysin line

The regular divisor `t=0` has the resolution `C --t--> C`. Applying `Hom_C(-,C)` gives

\[
\operatorname{RHom}_C(B_0,C)\simeq L_t^\vee[-1].
\]

In words: its only cohomology is the dual conormal line in cohomological degree one. This is the effective-Cartier-divisor duality calculation. [M1]

The evaluation pairing is canonical:

\[
L_t\otimes_{B_0}L_t^\vee\longrightarrow B_0.
\]

In words: a conormal vector pairs with its dual normal vector. The source's labelled positive normal supplies a frame `theta_t` satisfying

\[
\theta_t([t])=1.
\]

In words: this fixes the primitive normalization with the already chosen normal coordinate and orientation. Orientation alone on an unframed algebraic line is not being asserted to choose a trivialization.

Consequently

\[
(\theta_t\otimes1)\overline\beta_x(\bar a[h])=\bar a[p].
\]

In words: after taking the Cartier connecting map, retaining its first Rees symbol, and pairing the conormal with its framed dual, the coefficient becomes its restriction to the two specified fibres. There is no division by `t`, `x`, or an integer in the coefficient ring.

In the dual notation of entry 115 this is

\[
(\theta_{t_c}\otimes1)\operatorname{gr}_{t_c}^{1}\beta_{x_c}^{\vee}
=\epsilon_c.
\]

In words: the primitive normal operation is recovered from the conormal-valued first symbol. This is the local coefficient comparison that the earlier formula omitted. It is not a degree-zero endomorphism of the original polynomial complex.

These operations commute with localizations of spectator coefficients and leave unrelated polynomial variables unchanged. In particular they do not, by themselves, quotient away the earlier independent normalization-branch polynomials.

## 3. Why the raw weighted map does not acquire unit residue

### Ordinary and derived Cartier restriction

Ordinary specialization gives

\[
(tx)|_{x=0}=0.
\]

In words: multiplication by the normal equation vanishes on the Cartier fibre.

The derived statement is equally explicit. Resolve `A/(x)` by the homological complex `K_x=[Ae --x--> A]`. On the two-term complex let `H` send the degree-zero basis to `t e` and send `e` to zero. Then

\[
dH+Hd=tx\operatorname{id}_{K_x}.
\]

In words: multiplication by `tx` is null-homotopic on the resolution of the Cartier fibre.

Tensoring this identity with any complex, with the usual tensor-product signs, preserves the null-homotopy. If `rho` is a chain map, then

\[
A/(x)\otimes_A^{\mathbf L}(tx\rho)\simeq0.
\]

In words: derived Cartier pullback of the *ambient-module map* `tx rho` is zero. Applying derived Hom from `A/(x)` gives the analogous zero result for unfiltered extraordinary restriction. A retained filtered connecting class is extra information lost by either unfiltered operation.

This directly applies to the previous candidate `sigma_c=w_c rho_c` under the declared substitution `w_c=t_c x_c`. It rejects that route to the physical unit, not the existence of every possible filtered Gysin comparison.

### Changing the target must be explicit

A map whose image lies in the principal ideal `(x)` can be factored through that ideal before taking the Cartier fibre. These are different morphisms:

\[
(x)\hookrightarrow A,\qquad
(x)/(x^2)\xrightarrow{x^\vee}A/(x).
\]

In words: the first is the ambient inclusion; the second is evaluation of the *conormal* generator using its frame. Pulling back the first gives zero. The second sends `[x]` to one. A principal-ideal target and its filtration must be justified by the source; changing them after the fact is not a proof that the old comparison had unit residue. [S2,S3]

Moreover, `w=tx` does not provide an invertible identification of the `w` and `x` normal directions over the whole Rees chart. The induced map on the `x`-conormal is

\[
[w]\longmapsto t[x].
\]

In words: its coefficient is `t`; it degenerates at `t=0`. The divisor of `tx` contains both coordinate components. The source's positive `x` component and its spatial support cannot be selected merely by giving the product ideal a frame. Entry 115 records precisely this component-selection issue for several normals. [S1]

## 4. Compare with the physical normalized simple pole

Write `lambda=2 pi i alpha'`. On the physical normal germ in entry 38,

\[
q(X)=e^{\lambda X},\qquad
\kappa(X)=\frac{\lambda}{e^{\lambda X}-1}
=\frac{U(X)^{-1}}{X},
\qquad
U(X)=\frac{e^{\lambda X}-1}{\lambda X},\quad U(0)=1.
\]

In words: the normalized loaded propagator is a simple pole times a unit whose constant term is one. The analytic/formal-unit assertion is over characteristic zero; it is separate from the integral Cartier calculation above. The formula has the usual limiting interpretation at `lambda=0`.

For any coefficient `f` regular at this channel,

\[
\operatorname{Res}_{X=0}\bigl(f(X)\kappa(X)\,dX\bigr)=f(0).
\]

In words: its normalized physical residue is the restricted coefficient. Poincare residue extracts the coefficient of `dX/X`; the remaining regular forms contribute zero. [M2,S4]

For nonzero `lambda` there is also the exact local identity

\[
\kappa(X)\,dX=d\log(q(X)-1)-\lambda\,dX.
\]

In words: the normalized loaded pole represents the same residue class as the logarithmic normal generator. Their difference is regular. This supplies a local normal-line normalization; it does not identify arbitrary spatial coefficient complexes.

Multiplying by the retained raw factor produces instead

\[
(q(X)-1)\kappa(X)\,dX=\lambda\,dX,
\qquad
\operatorname{Res}_{X=0}\bigl((q(X)-1)f(X)\kappa(X)\,dX\bigr)=0.
\]

In words: the pole is canceled and the primitive residue is lost. Thus on this regular primitive sector, the extra multiplier in `sigma_c` cannot be interpreted as the physical Gysin normalization. A comparison must act on the normal class and its filtration, not on a scalar polynomial multiplier as though it were that class.

The source generic log-Thom audit gives a compatible elementary normalization: on its generic chart `u=Xt`, relative logarithmic differentials have `dlog u=dlog t` and trace coefficient one. That audit works in its stated generic localization and on the relative interval generator; it does not identify a global normal equation at the central crossing or a map on arbitrary branch polynomials. [S5]

## 5. Ordered products and local coherence

For independent normal directions the Cartier resolutions tensor, and the dual normal classes are odd. Let `iota_c` be contraction of the exterior normal basis with its framed dual. Then

\[
\iota_c^2=0,\qquad
\iota_c\iota_d+\iota_d\iota_c=0\quad(c\ne d).
\]

In words: ordered normal residues carry the Koszul sign. For an ordered normal word, contracting in its specified order has coefficient one; exchanging two labels changes the determinant orientation sign.

Under a dihedral relabelling, the determinant normal line and its dual acquire the same permutation sign. Their pairing is unchanged. This verifies the normal-line sign comparison on the eight physical Cut labels and all twelve compatible Cut pairs. It is not a computation of spatial Gysin maps on the 12,425 loaded cells.

The several-normal null-homotopy has the uniform formula

\[
d_x\bigl(t_c e_c\wedge-\bigr)+
\bigl(t_c e_c\wedge-\bigr)d_x=t_cx_c\operatorname{id},
\qquad d_x=\sum_c x_c\iota_c.
\]

In words: no higher normal tensor product changes the zero test for the raw multiplier. The anticommutation relations cancel all off-diagonal terms.

## 6. Consequence for the proposed infinity-groupoid

The source allows a precise normalization of the *first connecting symbol*. It does not supply a functor which replaces every independent normal polynomial by one in the original octagon diagram.

The next required comparison has a fixed test: on each source-defined normal symbol, its oriented coefficient must be the primitive unit just computed, and it must commute with the actual chart, overlap, endpoint-relative, and generic-Q operations. It must retain the correct principal-ideal/conormal targets and the connecting degree. It cannot be certified solely by the polynomial identity for the earlier weighted overlap filler.

Our earlier integer boundary extension and its pair-local homotopy remain valid in their stated unit-coefficient model. The weighted repair remains a valid polynomial chain map. Neither is promoted here to a normalized physical extension.

## 7. Verification

Run:

```sh
python check_gysin_normal_comparison.py --output gysin_normal_comparison_certificate.json
```

The checker uses exact integer Laurent polynomials in spectator coefficients and exact rational formal series for the separate physical normal-pole test. It verifies the Cartier division-on-its-ideal calculation, lift independence, first conormal symbols, spectator localization, the explicit derived null-homotopies, ordered exterior signs, and dihedral normal-frame evaluations. It also checks the inverse analytic-unit series through order twelve and computes the residues before and after multiplication by the normal factor.

The all-polynomial and all-normal-degree statements follow from the resolution and exterior identities in this note, not extrapolation from test bounds. No complete spatial Gysin pipeline or proof-assistant check is claimed. No files were written to the source repository.

## Sources

[S1] Marici, entry 115, `src/ledger/20260814-115 Boundary-Triad Tate Realization and the Multi-Rees Cartier Bicomplex.md`, blob `63da17cb5d641705056c5d5b9bc6f53cda72baf5`.

[S2] Marici, entry 111, `src/ledger/20260814-111 One-Sheet Rees-Cartier Symbol and the Missing Marked Conductor Lattice.md`, blob `5079643c5ed6d66ea77a270818453b4d455207a8`.

[S3] `research/voevodsky/check_principal_line_trace_variance.rs`, blob `242da84955dc839b23ffe65c5825dde129a1c33e`.

[S4] Marici, entry 38, `src/ledger/20260813-38 Finite-Alpha-Prime Normal-Torus Lift and Nearby-Cycle Unit Theorem.md`, blob `40504f31e8bbc9e984f97d5eef73b5cadf4bda95`, especially its local normal Koszul block and nearby-cycle unit theorem. The entry's own forward corrections and its transverse/fixed-mark scope remain in force.

[S5] `research/voevodsky/check_generic_log_dnc_thom_trace.py`, blob `95fd466d144bafea6838cfeacc4aaf485b124275`.

[M1] Stacks Project, Lemma 48.14.1, effective Cartier duality, https://stacks.math.columbia.edu/tag/0B4B .

[M2] Stacks Project, Section 50.15, especially Lemma 50.15.2, logarithmic residue, https://stacks.math.columbia.edu/tag/0FMU .

Prior input: `source_admissible_overlap.md` and its standalone checker, from this conversation. The independent-normal weighted complex in that note is a declared algebraic lift, not a source-established physical coefficient complex.
