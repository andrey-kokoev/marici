# Supported occurrence-line duality, logarithmic branch restriction, and the surviving excess transgression

Date: 2026-09-07  
Repository input: `andrey-kokoev/marici`  
Pinned commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result and scope

A concrete part of the requested mixed-variance comparison is now constructed. The previously computed endpoint map has a unique factorization through its actual principal occurrence line. Pair that line with its prescribed dual **before** taking the selected logarithmic branch. The resulting map retains a primitive endpoint class and the independent repeated-normal excess generator. Direct branch restriction, without this line-valued factorization, kills every column of the old endpoint map.

This operation also identifies a common fine-degree frame for the endpoint and the generic class. In that frame the generic representative carries the product of the three branch Rees parameters. Neither that product nor its determinant line is silently evaluated to one.

The complete selected-branch calculation nevertheless has a nonzero generic transgression. In the excess channel, the endpoint quotient has four derived classes, but all four have zero generic projection. The primitive generic class maps to a primitive nine-term short-support obstruction. Its coefficient dual evaluates it to +1; duality does not make it a boundary.

The positive result is therefore an explicit supported-line endpoint operation and a correctly framed test of its generic compatibility. It is **not** the complete spatial supported-Verdier-dual/logarithmic correspondence, and it assigns no physical reflection parity. The precise boundary between these statements is maintained below.

## 1. Fixed source, target, and actual logarithmic base change

Retain the original coefficient ring R, polynomial over the integers in nine occurrence variables and nine normal variables, and the source

\[
D=K_R(u_1,u_3,u_5)\otimes_R K_R(u_0,u_3),
\qquad \eta=h_3^+-h_3^{03}.
\]

In words: all 32 exterior generators remain present, including the two different copies of the shared normal. The branch order is `(1,3,5)` and the opposite-pair order is `(0,3)`.

The 215 target stalks, their permitted localizations, and their differential are unchanged inputs. Write

\[
V\subset B\subset K,\qquad E=K/V,\qquad Q=K/B.
\]

In words: V is the complete two-endpoint complex, B is the complete short-boundary complex, K is the whole target, E is the endpoint quotient, and Q is the seven-generator generic quotient. No endpoint or marked-normal summand is removed before applying the indicated functor.

The logarithmic coefficient base used here is

\[
A=\mathbb Z[X_0,\ldots,X_5,t_0,\ldots,t_5,
 X_{D_0},X_{D_1},X_{D_2},u_{D_0},u_{D_1},u_{D_2}],
\qquad u_i\longmapsto X_i t_i\quad(0\leq i\leq5).
\]

In words: impose the actual short-normal Rees graphs; the three long normals remain independent. This is the integral polynomial version, before harmless monodromy-unit localizations. It is not a global inversion of occurrence or normal parameters.

This ring map is not assumed flat. The source is bounded free and every target term is a localization, hence flat over R. Their displayed tensor complexes therefore compute the derived base change. After base change, a target stalk that inverts `u_i` inverts `X_i t_i`, hence each factor on **that stalk**. This follows from the ring equation; it is not permission to localize the source everywhere.

For the source-selected positive occurrence branch set

\[
i_+:\operatorname{Spec}\bar A\hookrightarrow\operatorname{Spec}A,
\qquad \bar A=A/(X_1,X_3,X_5).
\]

In words: select the admitted component with the three odd occurrence coordinates zero. Reflection transports it to the even component rather than acting as an automorphism of the selected component.

The derived restriction of a target stalk is zero whenever that stalk already inverts one of `X1,X3,X5`. Otherwise its coefficient ring is the corresponding localization of \(\bar A\). Thus an odd short label can survive in a target face only as a **marked** normal. The source differentials for all four odd-normal wedge generators become zero, but those generators are retained. The complementary `u0=X0 t0` differential remains.

This non-flat branch selection introduces additional derived classes. It does not justify retaining only the source's former two homology groups. In particular, the ordinary excess-channel frame below contains two classes after restriction; the specified original state is their diagonal combination.

## 2. Why direct restriction kills the old endpoint map

Use

\[
X_+=X_1X_3X_5,\qquad
U=u_{D_0}u_{D_1}u_{D_2},\qquad
v_+=\{x_1,x_3,x_5\}.
\]

In words: these are respectively the endpoint occurrence product, the independent long-normal product, and the actual endpoint label.

The previous Koszul-to-Cech map was

\[
\kappa_+(e_H)=\varepsilon(H)
\frac{U X_+}{\prod_{i\in\{1,3,5\}\setminus H}u_i}[v_+,H].
\]

In words: the inverse of each normal occurs only in its unmarked target stalk; epsilon is the ordered-wedge-to-lexicographic orientation sign.

After the logarithmic substitution its coefficient is

\[
\varepsilon(H)U
\frac{\prod_{i\in H}X_i}{\prod_{i\notin H}t_i}.
\]

In words: on any proper marked subset H, an unmarked odd-normal localization becomes the zero module on the selected branch. For the fully marked subset, the coefficient has the factor `X1 X3 X5`, which becomes zero. Therefore every column of the direct restriction of kappa vanishes. The same is true of both previously constructed source endpoint cochains F-zero and F-one.

This is a statement about the images of those maps, not a claim that the entire selected endpoint complex is zero. Its fully marked normal states survive, and are exactly what the corrected operation uses.

## 3. Principal occurrence-line duality gives a nonzero endpoint comparison

Let

\[
\mathcal I_+=(X_+)\subset R,
\qquad X_+^\vee\in\mathcal I_+^\vee,
\qquad X_+^\vee(X_+)=1.
\]

In words: keep the actual principal occurrence ideal as a free rank-one module with its source-labelled positive frame. Its dual frame is not an inverse element of the coefficient ring.

All columns of the old endpoint map factor through multiplication by this ideal. The factorization is

\[
\widehat\kappa_+(e_H)=X_+\otimes\kappa_+^{\mathrm{nor}}(e_H),
\qquad
\kappa_+^{\mathrm{nor}}(e_H)=\varepsilon(H)
\frac{U}{\prod_{i\notin H}u_i}[v_+,H].
\]

In words: the normalized map still uses only the permitted target normal inverses. No occurrence inverse is added to R. The inclusion of the ideal line sends this factorization back to the original kappa. Multiplication by `X_+` is injective on each original target localization, so the factorization is unique.

The normalized map is itself a chain map. Removing a source normal multiplies by `u_i`, while the corresponding target localization changes the displayed denominator by the same factor. The checker verifies every endpoint source column and the full complementary-normal/excess cochains, not only the bottom residue.

Pair the displayed occurrence line with its dual, then restrict to the selected branch. All proper marked subsets still vanish, but now the fully marked coefficient is U:

\[
L i_+^*\kappa_+^{\mathrm{nor}}(e_{\{1,3,5\}})
=U e_+^{(3)}.
\]

In words: the ordered top branch wedge maps to the fully marked endpoint state with primitive coefficient U in its fixed long-normal frame. Here the oriented endpoint basis includes epsilon; no new sign is fitted afterward.

The original excess cochains use the complementary generator `c=h0`:

\[
F_0(e_H\wedge c)=(-1)^{|H|}\kappa_+(e_H),
\qquad
F_1(e_H\wedge c\wedge\eta)=\kappa_+(e_H).
\]

In words: normalize these same maps through the same occurrence line and apply the same branch restriction. For the excess top wedge

\[
\zeta_1=h_1^+\wedge h_3^+\wedge h_5^+\wedge c\wedge\eta,
\qquad
\bar F_1(\zeta_1)=Ue_+^{(3)}.
\]

In words: the independent eta input is still present and has a primitive nonzero endpoint image. It is not replaced by an internal product of target normals.

A subtle base-change distinction is essential: \(\mathcal I_+\otimes\bar A\) is still a free line with its formal frame. Its **multiplication map** to \(\bar A\) is zero. Replacing the line by its zero image before pairing would destroy precisely the data being retained.

## 4. Actual supported purity and what it does not assert

The selected immersion is regular of codimension three. Its ordered conormal determinant is

\[
\mathcal L_X=\det((X_1,X_3,X_5)/(X_1,X_3,X_5)^2).
\]

In words: this line belongs to the occurrence-branch immersion. It is distinct from the original u-normal determinant, the Rees symbols, and the separately framed physical normal.

Write the ordered Koszul resolution as \(K_X=K_A(X_1,X_3,X_5)\). Its dual has the explicit supported purity map

\[
K_X^\vee\longrightarrow i_{+*}\mathcal L_X^\vee[-3],
\qquad
\varphi\longmapsto
\overline{\varphi(e_1\wedge e_3\wedge e_5)}
([X_1]\wedge[X_3]\wedge[X_5])^\vee
\]

on dual degree three, and zero on the other degrees. In words: evaluate the ordered dual top coefficient on the support, while keeping the dual conormal line. The regular-sequence Koszul theorem proves it is a quasi-isomorphism. The adjunction counit on the dual resolution evaluates its degree-zero component; it is not an unshifted residue map on its top cohomology.

For every displayed target complex T,

\[
i_{+*}i_+^!T\simeq K_X^\vee\otimes_A T
\simeq i_{+*}(L i_+^*T\otimes_{\bar A}\mathcal L_X^\vee)[-3].
\]

In words: this is the actual closed-immersion duality operation on the coefficient diagram. The checker verifies the tensor chain equation on all 1,720 dual-Koszul/target columns, with the minus sign on the odd cohomological shift. It also verifies ordered-frame permutation covariance. All source and target Tor grades are retained.

For clarity, the Ext tables below are stated **before** this common purity twist, using the branch-pulled-back source and target. Applying the same supported purity twist to both objects preserves the mapping groups; applying it only to the target changes their degree and line frame. These two conventions must not be mixed.

For comparison, applying upper shriek along the original normal ideal alone cannot be a new escape from the preceding obstruction. With `P=K(u0,u3)` and `Aplus=K(u1,u3,u5)`, the exact adjunction is

\[
\operatorname{RHom}_R(D,T)
\simeq\operatorname{RHom}_R(P,\operatorname{RHom}_R(A_+,T)).
\]

In words: that original normal-supported restriction was already present in the old full Koszul Hom calculation. The checker constructs the signed currying map on every critical generator. Its sign is \((-1)^{pq}\) for branch and pair wedge degrees p and q.

The full original source dual also retains both excess channels: its supported cohomology is in degrees four and five, with the regular four-normal dual determinant and the additional eta-dual line. This agrees with, but does not identify parameters with, the independent supported-Gysin construction in the parallel work.

## 5. The common endpoint/generic frame retains a Rees determinant

Let

\[
\tau=t_1t_3t_5,\qquad \gamma=\deg U.
\]

In words: tau is the product of the three branch Rees parameters. It is **not** `u1 u3 u5`, and is not the six-short-normal multiplier that previously killed endpoint homology.

The fully marked endpoint state has fine degree \(e_{t_1}+e_{t_3}+e_{t_5}\). Therefore the endpoint image \(Ue_+^{(3)}\) and the actual generic cycle have the same degree only when the generic representative is

\[
\tau\omega,
\qquad
\omega=UT-\sum_{i=0}^2 X_{D_i}\frac{U}{u_{D_i}}M_i.
\]

In words: the prescribed generic top cycle retains the branch Rees determinant in this common frame. Setting tau to one would change the coefficient problem.

For the excess source wedge, that common mapping degree is

\[
\lambda_\sharp=\gamma+e_{t_1}+e_{t_3}+e_{t_5}-\deg\zeta_1.
\]

In words: subtract the actual full source wedge degree from the common target degree. In the old exponent notation this is the previous endpoint frame minus the three **occurrence** degrees. The normal, occurrence, and Rees frame changes have all been accounted for.

Both maps are primitive in this homogeneous frame. This does not claim that the unframed generic readout is the scalar one, nor that the source's full physical Q connector has been identified with this Rees-decorated class.

A uniform division of the original generic map by the endpoint occurrence factor is not a valid substitute. In that putative common-division frame the selected generic Hom complex has no generators at all. The endpoint line factorization does not extend automatically to the entire original cospan.

## 6. Complete selected-branch generic obstruction

Use \(\bar D=L i_+^*(D\otimes_R A)\) and analogous bars for all target complexes. In the frame \(\lambda_\sharp\), the complete excess-channel calculation is

| Target | Hom-complex generators | Nonzero Ext groups |
|---|---:|---|
| \(\bar V\) | 3 | \(\operatorname{Ext}^2=\mathbb Z\) |
| \(\bar E\) | 86 | \(\operatorname{Ext}^2=\mathbb Z^4\) |
| \(\bar Q\) | 7 | \(\operatorname{Ext}^2=\mathbb Z\) |
| \(\bar B\) | 82 | \(\operatorname{Ext}^2=\mathbb Z^5,\ \operatorname{Ext}^3=\mathbb Z\) |
| \(\bar K\) | 89 | \(\operatorname{Ext}^2=\mathbb Z^5\) |

All groups are integral and torsion-free. In words: the normalized endpoint really survives, including in the full target. Its survival is not inferred from a scalar signature. However, every one of the four endpoint-quotient classes has zero generic image.

The exact connecting morphism is

\[
\operatorname{Ext}^2_{\bar A}(\bar D,\bar Q)_{\lambda_\sharp}
\xrightarrow{\ \partial\ }
\operatorname{Ext}^3_{\bar A}(\bar D,\bar B)_{\lambda_\sharp},
\qquad \partial[\bar G_1]=[\beta_\sharp],
\]

and is an isomorphism between two copies of the integers. In words: the nine-term short-support boundary is primitive and nonzero. No derived replacement cochain in this frame lifts the nonzero generic class into the endpoint quotient.

The nine terms are the actual surviving terms of the generic cycle's differential after the selected branch and coefficient-frame operations. The terms with odd unmarked short normals disappear because their **target modules** become zero; the even-short terms remain. No extra relation is adjoined to kill them.

### Independent small reduction

There is a checked coordinate projection of the full critical Hom complexes onto actual short faces with no `x0` and no long label. Its mapping cone is integrally contractible. After that projection, odd marks O are fixed and only the optional even labels `x2,x4` can be added:

| Fixed odd marks O | Available even labels |
|---|---|
| empty | 2,4 |
| 1 | 4 |
| 3 | none |
| 5 | 2 |
| 1,3 | none |
| 1,5 | none |
| 3,5 | none |
| 1,3,5 | none |

Each nonempty set of available even labels gives an augmented simplex complex, with signed-unit contraction. Five sectors have no available even label, producing the five full-target classes. The fully marked endpoint is one of them; quotienting it out leaves four.

For the empty odd sector, excluding the chamber to pass to B leaves one reduced boundary class. The generic chamber maps primitively onto it. This gives an independent explanation of the connecting isomorphism rather than merely a list of matrix ranks.

The ordinary source channel gives two copies of this pattern, shifted by one. In its frame, V and Q each have two Ext-one classes, E has eight, K has ten, and B has ten Ext-one plus two Ext-two classes. The selected images of the original F-zero and G-zero are diagonal primitive vectors. The extra class is retained; no post-restriction uniqueness is asserted.

### Ambient logarithmic control

Before branch selection, the full critical excess-channel logarithmic Hom complex has exactly the same generators and integer differential matrices as before the Rees substitution: V has 18 generators, E 202, Q 7, B 213, and K 220. Their coefficient monomials change by the explicit exponent transformation, but no new critical filler appears. This is checked directly, not deduced from an unjustified flatness assumption.

## 7. Duality evaluates the obstruction; it does not null-homotope it

Let

\[
\mathcal H_T=\operatorname{Hom}_{\bar A}(\bar D,\bar T)_{\lambda_\sharp},
\qquad
\mathcal H_T^\star=\operatorname{Hom}_{\mathbb Z}(\mathcal H_T,\mathbb Z).
\]

In words: dualize the **entire finite homogeneous coefficient complex**. This is a bounded finite free integral dual, not an asserted identification with the complete spatial supported Verdier dual, whose sheaf-level variance and dualizing object remain to be constructed.

The dual support triangle is reversed:

\[
\mathcal H_Q^\star\longrightarrow\mathcal H_K^\star
\longrightarrow\mathcal H_B^\star\longrightarrow\mathcal H_Q^\star[1].
\]

In words: an original lifting obstruction becomes a dual extension obstruction; it does not become zero merely because the arrows reverse.

Here the primitive dual representative is particularly simple. In the original ordered five-generator source basis, take the coefficient functional on the single Hom column

\[
11111\longrightarrow [\{x_2,D25\},\{D25\}].
\]

In words: evaluate the forced coefficient monomial of the actual even-short/marked-long target state on the full source wedge. This is a legal coefficient-residue functional in the indicated finite frame. Denote it by \(\ell_B\).

Extend it by zero to the full target Hom complex and apply the dual differential. The result is the generic functional \(\ell_Q\) on the column `11111 -> D25[D25]`. Exact calculation gives

\[
d^\star\ell_B\big|_{\mathcal H_B}=0,
\qquad
\partial^\star[\ell_B]=[\ell_Q],
\qquad
\ell_B(\beta_\sharp)=\ell_Q(\bar G_1)=1.
\]

In words: the new supported residue has unit evaluation on the actual obstruction, and its dual transgression has unit evaluation on the actual generic class. Different extensions of the functional change the latter by a dual boundary only. Both classes remain nonzero.

This is a positive, explicit dual calculation. It does not turn the functional into a physical observable or prove that the physical kernel evaluates the same class. That additional identification must use the independently specified spatial normalizations and endpoint connector cells.

## 8. Consequence for the remaining physical construction

The normal-line part of the comparison is no longer only a proposed shift. Its principal occurrence-line factorization, selected-branch restriction, ordered purity map, excess endpoint image, common Rees frame, and residual generic obstruction are explicit.

Three shortcuts are now decided on the actual classes. Original-normal upper shriek merely curries the previous Hom problem. Direct occurrence-branch restriction kills the old endpoint maps. Correct principal-line normalization retains the endpoint, but its generic compatibility still has the primitive transgression above. The finite coefficient dual reads that transgression as a unit extension class rather than a nullhomotopy.

A successful full correspondence must therefore do more than append a determinant line, reverse all arrows, or change coordinates. It must supply the actual branch-selected exceptional/logarithmic support comparison and its two coupled endpoint cells, explaining how the displayed extension is used in the supported-dual target. If it were to claim a lift of the same nonzero generic class into precisely the ordinary selected target diagram computed here, the calculation would contradict it.

An independently constructed parallel Gysin normalizes a supported two-extension rather than producing a forbidden ordinary lift of its native class. That result is consistent with the distinction here. Its different spectator parameters and native source are not identified with this branch/pair calculation.

No physical parity, global Cut compatibility, arithmetic positivity, or completed infinity-groupoid is claimed by this note.

## 9. Reproduction and verification

Run:

```sh
python check_marici_supported_dual_log_branch_comparison.py \
  --output marici_supported_dual_log_branch_comparison_certificate.json
```

The checker is self-contained and uses Python 3.10+ and the standard library. It checks 82,073 exact assertions, including original polynomial differentials, supported purity, all 1,720 purity tensor columns, full source currying, actual logarithmic and branch-restriction maps, both occurrence-normalized excess channels, integral deformation retractions, the independent fixed-mark reduction, all six transported branch/pair frames, and the explicit dual connecting pairings.

The certificate includes the explicit source cochains, primitive endpoint coordinates, nine-term excess obstruction, all critical cohomology groups, dual functionals, source hashes, and scope boundaries. Assertion counts are not used as substitutes for the regular-sequence, localization, or degreewise completeness arguments. This is not proof-assistant verification. No repository file was changed.

## 10. Provenance and references

Pinned repository input paths:

- `research/voevodsky/check_d03_plus_excess_beck_chevalley.rs`, blob `df8448271089910a90c8e641af5b8ae95f1472dd`: repeated-normal source, branch selection and excess orientation.
- `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`: all target stalks, localization domains and support filtration.
- `research/voevodsky/check_two_endpoint_tate_carrier.rs`, blob `0147e2e42dafac0da7289c571cb0331b51338be1`: endpoint labels and physical relabelling convention.
- `src/ledger/20260814-115 Boundary-Triad Tate Realization and the Multi-Rees Cartier Bicomplex.md`, blob `63da17cb5d641705056c5d5b9bc6f53cda72baf5`: actual Rees graphs, independent conormal symbols and selected occurrence branch.
- `src/ledger/20260815-173 Component-Supported Semistable Node and the vplus Coefficient Counit.md`: distinction between selected component, principal-line counit, conductor Tor grades and spatial identification.

Conversation/library inputs:

- `marici_branch_excess_endpoint_q_obstruction.md` and its checker: previous complete source-Hom obstruction calculation.
- `supported_gysin_proof.md`: independently constructed ordered supported Gysin; used to compare variance and scope, not to identify different source parameters.

Primary mathematical references:

- Stacks Project, tag `0621`, *The Koszul complex*: exterior differential, tensor-product signs and normal homotopies.
- Stacks Project, tag `0A8H`, *Hom complexes*: internal Hom differential, tensor-Hom adjunction and coefficient dual signs.
- Stacks Project, tag `0B4B`, Cartier duality: upper-shriek normal line and its cohomological shift, iterated in the ordered regular sequence.
- Stacks Project, tag `0ATZ`, *Properties of upper shriek functors*: closed-immersion duality and its variance.

The full supported-dual/spatial exceptional correspondence is not deduced from these general references. They justify the operations explicitly constructed above.
