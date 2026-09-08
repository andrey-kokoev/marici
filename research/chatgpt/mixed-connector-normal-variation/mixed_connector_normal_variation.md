# Mixed 03/13 action on connector models

Date: 2026-09-06  
Branch: A  
Marici reference: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

## Results and scope

The coefficient calculation now distinguishes the Gysin-collapsed source from the uncollapsed exceptional-normal source.

1. For every R-linear chain map from the source's constant-differential Gysin-collapsed module to the independent-normal PC/Čech target, the mixed operator admits an explicit R-linear nullhomotopy. This nullhomotopy has zero Q component. Its endpoint components vanish when the *complete* fixed endpoint comparison is independent of the long-normal parameter. It preserves the independent external Cartier filtration when the connector does.
2. The uncollapsed geometric source is not constant in that parameter. Its actual exceptional monodromy is q_E=q_03 q_13. Two explicit toric normal-chart chain isomorphisms retain this dependence and the ordered double-normal coefficient +1.
3. Composing either normal-chart isomorphism with the finite-to-Čech comparison on the complete twenty-generator closed mixed-face complex gives a nullhomotopic secondary operator. The primitive is coefficient-legal and has zero endpoint and Q components.
4. On a complete, not necessarily closed-face-supported connector, the remaining class is the negative of a five-row incoming-radial composite. The target-side row formula is explicit. The inspected integration checker does not contain the corresponding full source-to-target matrix.

The first result computes an action in the specified finite coefficient model. It is not an equivalence between that model and the raw normalized/logarithmic source. The second result prevents incorrectly applying the first result to the uncollapsed source without transporting its normal-variation operators.

All calculations below are integral Laurent-polynomial identities. Their origin as secondary operations from rational stabilizer cochains retains the rational qualification of `mixed_normal_chern_comparison.md`. No integral formality theorem or full six-functor equivalence is asserted.

## 1. Target, operator, and coefficient connection

Let D be the nine diagonals of the labelled hexagon, and put

\[
R=\mathbb Z[X_d,u_d:d\in D].
\]

The finite complex has a generator [F,H] for every noncrossing F and H subset F, in homological degree 3-|F|+|H|. The Čech coefficient at that generator is

\[
R[u_d^{-1}:d\in F\setminus H].
\]

Its differential has radial coefficient X_d/u_d and normal coefficient 1, with the source's exterior and incidence signs. Quotienting the sixteen complete endpoint states gives E. Write E_fin for the corresponding bounded free finite source and Lambda for its finite-to-Čech map.

Set a=03, b=13. The previously computed secondary operation is

\[
T_{ab}=\frac{1}{u_a u_b}\,\iota_b\iota_a.
\]

It has homological degree -2. It is zero unless both marks occur; all inverses occur on legal target summands.

For a target chain coefficient f, define

\[
\nabla_a(f[F,H])
=\left(\frac{\partial f}{\partial u_a}
 +\frac{\mathbf1_{a\in F\setminus H}}{u_a}f\right)[F,H].
\]

This is a connection, not an R-linear operator. It is defined on every actual Čech coefficient module. If a is not inverted, the second term is absent and differentiation does not introduce an inverse; if a is inverted, differentiation stays inside the same localization.

The connection is horizontal on the finite-to-Čech basis:

\[
\nabla_a\Lambda=\Lambda\partial_{u_a}.
\]

The derivative of the coefficient u_a^{-1} in a radial arrow cancels the change in the displayed diagonal connection term. The normal arrow removing a instead contributes

\[
J_a=[\nabla_a,d_E]
=\frac{(-1)^{3-|F|}}{u_a}\,\iota_a.
\]

These are R-linear maps. Directly,

\[
d_EJ_a+J_ad_E=0,\qquad
J_bJ_a=T_{ab},\qquad
[\nabla_a,\nabla_b]=0.
\]

The connection does not identify u_a with a Chern class or with a Rees parameter. It differentiates the independent coefficient u_a of this model.

## 2. General connector identity

Let S be a complex equipped with coefficient connections nabla_a^S,nabla_b^S, and let kappa:S -> E be an R-linear degree-zero chain map. Define

\[
J_i^S=[\nabla_i^S,d_S],\qquad
A_i=\nabla_i^E\kappa-\kappa\nabla_i^S.
\]

Although the connections themselves obey a Leibniz rule, their difference A_i is R-linear. For the cohomological mapping differential

\[
\delta(f)=d_Ef-(-1)^{|f|}fd_S,
\]

one obtains

\[
\delta A_i=\kappa J_i^S-J_i^E\kappa.
\]

Consequently, setting

\[
\mathcal H_{ab}=J_b^E A_a-A_bJ_a^S,
\]

gives the exact identity

\[
\delta\mathcal H_{ab}
=T_{ab}^E\kappa-\kappa J_b^S J_a^S.
\]

Here A_i has homological degree zero, J_i has degree -1, and H has degree -1. This is an equality of full coefficient maps, not a formula obtained only after taking homology.

If J_a^S=0, the simpler formula suffices:

\[
\mathcal H_{ab}=J_b^E A_a,
\qquad
\delta\mathcal H_{ab}=T_{ab}^E\kappa.
\]

No source contraction is needed. In particular, there is no need to choose a non-equivariant spanning-tree contraction of the Tate window for this result.

### Constant-differential collapsed source

The inspected source module of Entry 417 is

\[
\mathcal P_{\rm fil}=C_{\rm Tate}\otimes\Lambda^\bullet N_{\rm Cart}^\vee,
\qquad d=d_{\rm Tate}\otimes1.
\]

Its differential has integer entries and is independent of u_a. With the coefficientwise connection partial/partial u_a, J_a^S=0. Thus every R-linear chain map from this module satisfies the displayed nullhomotopy identity. The same statement applies to other sources with this flatness property; it is not specific to a presentation of the Tate window.

The external Cartier states are retained at their original filtration levels. The target connection and J_b act on the PC coefficient factor, not the external Cartier factor. If kappa intertwines the independently represented external Cartier operators, so does the homotopy.

For a morphism of *whole ringed diagrams*, the source connection must also be compatible with its structural arrows. Checking only d_Tate is insufficient to establish that extra condition. The total diagram mapping complex has additional arrow and coherence terms. This note does not delete them or claim that they are constant.

## 3. Endpoint and Q restrictions of the homotopy

Use the complete target boundary map

\[
\rho=(\pi_Q,\kappa_+,\kappa_-):E\to Q\oplus V_+[1]\oplus V_-[1].
\]

The endpoint maps are the actual differential terms entering the removed endpoint packets. The endpoint differentials acquire the negative sign appropriate to the displayed shift.

The connections commute with this boundary map:

\[
\rho\nabla_i^E=\nabla_i^\partial\rho,
\qquad
\rho J_i^E=J_i^\partial\rho.
\]

For a flat source and H=J_b A_a this gives

\[
\rho H
=J_b^\partial
\left(\nabla_a^\partial\rho\kappa-\rho\kappa\nabla_a^S\right).
\]

All Q representatives omit the short b-mark, so J_b^Q=0. Both endpoint supports omit the long a-coordinate; their a-connection has no diagonal term and is ordinary coefficient differentiation. Therefore, when the full endpoint comparison matrices are independent of u_a, the homotopy satisfies

\[
\pi_QH=\kappa_+H=\kappa_-H=0.
\]

This is a sufficient condition on the full boundary maps, not a consequence merely of an endpoint permutation matrix or the scalar residue +1. If those maps contain additional long-normal dependence, the preceding formula computes the boundary defect that must be retained.

Because the connection fixes the target face and J_b changes only the mark subset, the homotopy introduces no additional face support. Its fine weight is the same as T_ab. It may be transported with the ordered pair under ordinary label relabelling. No claim about a raw reciprocal-twist action or a stronger source-relative mapping complex is inferred solely from this coefficient calculation.

### Negative control

Taking kappa=Lambda and S=E_fin does not force the nonzero target operator to vanish. In this case

\[
J_a^S=(-1)^{3-|F|}\iota_a\ne0,\qquad A_a=0,
\]

and the general identity reduces to the previously checked naturality

\[
T_{ab}^{\check C}\Lambda=\Lambda T_{ab}^{\rm fin}.
\]

The script rechecks the integral covector detecting this map with value one. It therefore distinguishes a flat source from the actual finite PC source rather than accidentally proving all target operations exact.

## 4. The actual exceptional normal is not flat

Entry 111 identifies the exceptional ray over the center (D03,x1), where x1 is diagonal 13, by

\[
q_E=q_aq_b.
\]

The source's normal-circle rule is d e_i=(q_i-1)p. Hence, writing q_i=1+u_i,

\[
u_E=u_a+u_b+u_au_b,
\qquad
\frac{\partial}{\partial u_a}(d e_E)=q_b p\ne0.
\]

Thus the coefficient-flatness argument cannot simply be applied to this uncollapsed source. A change of grading does not by itself eliminate that source operation. The Gysin comparison would have to transport it explicitly.

### Two local normal-chart comparisons

Let R_q=Z[q_a^{+/-1},q_b^{+/-1}]. Write K(r,s) for the homological Koszul complex with bases 1; e_1,e_2; e_1 wedge e_2, and differential

\[
d e_1=r,\qquad d e_2=s,\qquad
 d(e_1\wedge e_2)=r e_2-s e_1.
\]

On the first blowup chart use the ordered normal variables (E,b). Define

\[
F_A:K(u_E,u_b)\to K(u_a,u_b),
\]

\[
F_A^0=1,\qquad
F_A^1=\begin{pmatrix}1&0\\q_a&1\end{pmatrix},\qquad
F_A^2=1.
\]

The image of e_E is e_a+q_a e_b. Its boundary is u_a+q_a u_b=u_E. This is the loaded concatenation of the two oriented normal loops. Both the basepoint and all normal grades are retained.

On the other chart, with order (a,E), use

\[
F_B:K(u_a,u_E)\to K(u_a,u_b),
\]

\[
F_B^0=1,\qquad
F_B^1=\begin{pmatrix}1&q_b\\0&1\end{pmatrix},\qquad
F_B^2=1.
\]

Its exceptional image is q_b e_a+e_b. Both middle matrices have determinant one; their inverses are integral triangular matrices. The overlap comparison is

\[
(F_B^1)^{-1}F_A^1
=\begin{pmatrix}1-q_aq_b&-q_b\\q_a&1\end{pmatrix},
\]

also of determinant one. These are local normal-torus comparisons. They do not specify the global source's radial, endpoint, or Q images.

The geometric ordered double cap satisfies

\[
\iota_b\iota_a F_A=F_A\iota_b\iota_E,
\]

and the corresponding equality for F_B. Its coefficient on the double-normal state is +1.

For coefficient-derivative variation, the source operation is slightly different at chain level. In chart (E,b),

\[
J_a^S=q_b\iota_E,
\qquad J_b^S=q_a\iota_E+\iota_b,
\qquad J_b^S J_a^S=q_b\iota_b\iota_E.
\]

The discrepancy from coefficient one is (1-q_b)=-u_b and is the explicit homotopy in Section 2. In the other chart the discrepancy is -u_a. These differences disappear in the supported quotient, not by setting q_b to one before constructing the chain maps.

At u_a=u_b=0 the normal differentials are zero and the ordered cap remains one from the double-normal state to the basepoint. As both source and target are bounded free resolutions, this proves a nonzero derived normal-torus class. Its degree-two self-Ext coefficient is R_q/(u_a,u_b), with the ordered determinant orientation. It does not prove survival after Čech localization or Gysin integration.

## 5. Complete twenty-state local Čech comparison

The closed mixed-face subcomplex contains every F with a,b in F and every mark subset H. It has twenty states; its two maximal faces are {03,04,13} and {03,13,35}.

Extend F_A and F_B exteriorly on the a,b slots and by the identity on any spectator circle. The source normal differential uses u_E in the exceptional slot; the radial and spectator terms remain. This gives an explicit local change of normal basis over the whole twenty-state complex. It is not a new assertion identifying its labels with the entire global blowup diagram.

Composing with Lambda gives two local maps kappa_A,kappa_B into the actual Čech target. Let H_ab be the earlier legal local homotopy:

\[
H_{ab}[F,H]=
\frac{(-1)^{3-|F|}}{u_au_b}\iota_b[F,H]
\]

when a is present unmarked and b is marked; otherwise it is zero.

For both charts,

\[
d_E(H_{ab}\kappa_i)+(H_{ab}\kappa_i)d_{S_i}
=T_{ab}\kappa_i.
\]

All twenty columns, including the coface attachments, are checked. The primitive has zero Q and endpoint components.

For example, on the minimal face {a,b}, whose base dimension is one, the first chart has

\[
(H_{ab}\kappa_A)(e_E)
=-\frac{q_a}{u_a^2u_b}p,
\qquad
(H_{ab}\kappa_A)(e_b)
=-\frac{1}{u_a^2u_b}p.
\]

It is zero on the double-normal and unmarked states. The inverses occur only on the unmarked target p, where both are legal. The source normal equation yields the cap coefficient +1/(u_a u_b). In particular, the nonzero ordinary torus cap in Section 4 is not automatically a surviving local PC/Čech action.

## 6. Exact remaining global composite

On the full target, the same local homotopy satisfies

\[
d_EH_{ab}+H_{ab}d_E=T_{ab}+\mathcal R_{ab}.
\]

Thus for any complete coefficient chain map kappa,

\[
[T_{ab}\kappa]=-[\mathcal R_{ab}\kappa].
\]

This equality also holds with the target Q and endpoint comparisons retained: H_ab and R_ab have zero boundary components.

There are exactly five incoming rows. In the following table every displayed coefficient is multiplied by X_03/(u_03^2 u_13).

| Input [F,H] | Output [F',H'] | Sign |
|---|---|---:|
| [{13},{13}] | [{03,13},empty] | -1 |
| [{04,13},{13}] | [{03,04,13},empty] | +1 |
| [{04,13},{04,13}] | [{03,04,13},{04}] | -1 |
| [{13,35},{13}] | [{03,13,35},empty] | +1 |
| [{13,35},{13,35}] | [{03,13,35},{35}] | +1 |

Therefore the full action can be computed once the components of the actual source-to-target connector on these five marked states and its full source differential are supplied. They are not the scalar Q roof, the endpoint swap, or the bare first residue.

The inspected integration file `check_global_mixed_variance_transform.py` reruns several component audits and then defines `unique_connector_signature = dict(transform_signature)`. That equality does not provide these five component maps. This is a statement about what that file certifies, not a claim that no mathematical construction can supply them.

## 7. Verification

Run:

```
python check_mixed_connector_normal_variation.py
```

The script is standalone and uses only the Python standard library. It writes `mixed_connector_normal_variation_certificate.json` beside itself.

The run executes 82,427 exact assertions. These include the previous nonzero Hom detector; coefficient-connection commutators and localization legality on all 215 cells; the complete target connecting maps; flat-source identities on elementary Hom generators; both exceptional normal-chart chain isomorphisms and their overlap; the nonzero source normal derivative; and both twenty-state Čech nullhomotopies. The tests include 1,380 elementary Hom-boundary seed maps from the full Tate coefficient complex, of which 1,260 have long-normal-independent endpoint values. Those seed maps are tests of the universal identity, not surrogate physical connectors.

The all-polynomial results follow from the displayed Leibniz and Hom identities. Finite assertions do not certify a raw algebraic realization or an absent full spatial matrix.

## Sources

Pinned Marici files:

- `research/voevodsky/check_ringed_alexandrov_pc_target.py`: target coefficient rings, normal and radial differentials.
- `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`: finite-to-Čech comparison.
- `research/voevodsky/check_collapsed_filtered_pc_module.py`: the complete constant-differential Tate source with eight external Cartier states.
- `src/ledger/20260814-111 One-Sheet Rees-Cartier Symbol and the Missing Marked Conductor Lattice.md`: exceptional ray q_E=q_03 q_1 and its actual blowup center.
- `src/ledger/20260813-38 Finite-Alpha-Prime Normal-Torus Lift and Nearby-Cycle Unit Theorem.md`: the loaded normal-circle boundary and tensor-product convention.
- `research/voevodsky/check_global_mixed_variance_transform.py`: inspected integration signature and its scope.

Stacks Project:

- `https://stacks.math.columbia.edu/tag/0A8H`: mapping differential and composition signs.
- `https://stacks.math.columbia.edu/tag/0A5W`: derived Hom from bounded free sources.
- `https://stacks.math.columbia.edu/tag/014D`: shifted connecting maps and cone conventions.

The previous target operator, homogeneous mapping slice, and proof of its nonvanishing are retained in `mixed_normal_chern_comparison.md` and are rechecked by the new script.
