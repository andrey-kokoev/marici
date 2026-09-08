# Occurrence-supported reverse trace and normalization-conductor specialization

Date: 2026-09-07  
Project: Marici  
Repository input: `andrey-kokoev/marici`  
Pinned commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## 1. Result and exact scope

The reverse trace that previously had image `(X2,X4)` admits a coefficient-linear supported continuation. Its output is the local-cohomology object on that *occurrence* support, not the original polynomial ring. In the prescribed oriented homogeneous frame, a lift of the primitive residue exists and its comparison space is contractible. This does not turn the old proper ideal into the unit ideal.

The supported operation can also be applied to the actual normalization-conductor square. The two sheet maps and their difference then remain in one explicit complex. This gives a source-defined coefficient continuation rather than two separately selected endpoint values.

There is a necessary distinction at the conductor. The generic residue-valued map from the free generic line specializes to zero. A different morphism, represented on the **whole occurrence Koszul complex**, survives with bottom coefficient one. It is a codimension-two Gysin extension. Both morphisms are constructed and their degrees are different; they must not be identified.

The whole Koszul morphism has four literal rows in the unreduced target-source Hom complex. Its short-support restriction is the closed comparison class that appears when one forgets occurrence degree. That class is not an allowed automorphism in the primitive residue's fixed frame. This identifies the determinant/degree information required to relate the trace to the endpoint continuation.

These results close a coefficient-support calculation. They do not identify it with the complete ringed supported-Verdier or logarithmic spatial kernel, and do not identify the source zero-section maps with the two spatial endpoint connector 2-cells. No physical reflection parity is assigned.

## 2. Retain the exact polynomial source calculation

Let

\[
A=\mathbb Z[X_0,\ldots,X_5,X_{D03},X_{D14},X_{D25}],
\qquad x=X_2,\quad y=X_4,\quad I=(x,y).
\]

In words: the occurrence variables remain independent. The nine normal parameters are separate variables, not renamed occurrence coordinates.

The reference excess source remains

\[
D=K_R(u_1,u_3,u_5)\otimes_R K_R(u_0,u_3),
\qquad \eta=h_3^+-h_3^{03}.
\]

In words: the two copies of the repeated normal and their independent excess difference are retained. The source's actual normal ideals and orientation are inputs [S2].

The original 215-state target still has its source-prescribed localized modules and radial coefficient `X_a/u_a` [S1]. No occurrence inverse is added to one of those target modules in this continuation. The checker reconstructs the complete repeated-normal source, all target support complexes, and the supported-purity comparison over the polynomial occurrence ring. The reference comparison cones contract using only signed units.

For the critical excess normal frame, let `C_T` denote the previously defined source-Hom complex with target `T`. Suppressing only the displayed orientation signs, its exact polynomial reduction is

\[
C_K\simeq C_E\simeq
\left[A\xrightarrow{(x,y)^T}A^2\xrightarrow{(-y,x)}A\right],
\]

in cohomological degrees two, three, four. In words: this is the actual residual occurrence Koszul complex, not its occurrence-zero integer slice. Here `E=K/V`, with `V` the two-endpoint support.

The compatible support reductions are

\[
C_B\simeq[A^2\xrightarrow{(-y,x)}A],
\qquad C_Q\simeq A[-2],\qquad C_V\simeq0.
\]

In words: the short-boundary complex is the two-term subcomplex; the generic quotient is the first term; the full endpoint complex is contractible **in this critical frame**. The separate endpoint residue frames are not declared contractible.

Choose the displayed core basis `q,a_x,a_y,a_xy`. Its occurrence shifts are

\[
\deg q=0,\quad \deg a_x=-e_x,\quad
\deg a_y=-e_y,\quad \deg a_{xy}=-e_x-e_y.
\]

In words: these shifts make the weighted differential homogeneous. The transgression is represented by `x a_x+y a_y`.

The preceding obstruction follows from

\[
A^2/A(-y,x)\longrightarrow A,
\qquad [(a,b)]\longmapsto xa+yb,
\qquad \operatorname{im}=(x,y).
\]

In words: all polynomial covectors and homotopies are already included, and a polynomial-valued unit trace is impossible. The present construction changes the **output support object** explicitly instead of contradicting this theorem.

## 3. The supported output and its coefficient-linear trace

Use the ordered extended Cech complex

\[
\mathcal C_I=[A\longrightarrow A_x\oplus A_y\longrightarrow A_{xy}],
\qquad d^0(a)=(a,a),\qquad d^1(b,c)=c-b.
\]

In words: every inverse belongs to a declared output localization. This flat complex computes cohomology with support on `V(I)` [M1]. It is not a replacement of the original spatial target's stalk domains.

Let

\[
\mathcal H=H_I^2(A)
=A_{xy}/(A_x+A_y),\qquad
\mathcal C_I\simeq\mathcal H[-2].
\]

In words: the local-cohomology module has the double-pole classes. If `S` denotes the polynomial ring in the other seven occurrences, then

\[
\mathcal H=\bigoplus_{a,b\ge1}S\,e_{ab},
\qquad e_{ab}=[x^{-a}y^{-b}].
\]

In words: a monomial with a nonnegative exponent in either residual variable is zero in the quotient. Multiplication by `x` or `y` lowers a pole order and kills the corresponding order-one boundary mode.

After applying `RHom_A(-,C_I)` to the complete support sequence, the reverse connecting map reduces to

\[
\mathcal H^2/\{(-yc,xc):c\in\mathcal H\}
\xrightarrow{\ \sim\ }\mathcal H,
\qquad [(a,b)]\longmapsto xa+yb.
\]

In words: the supported reverse map is an isomorphism of `A`-modules. Its proof includes every cochain homotopy, not a selected trace formula.

For the primitive ordered residue

\[
\epsilon=e_{11},
\qquad
\ell_x=(e_{21},0),\qquad
\ell_y=(0,e_{12}),
\]

we have

\[
(x,y)\ell_x=(x,y)\ell_y=\epsilon,
\qquad \ell_y-\ell_x=(-y,x)e_{22}.
\]

In words: either representative gives the same residue value and the displayed pole class is their comparison homotopy. These are `A`-linear coefficient-row maps into `H`; no coefficient-extraction functional into `A` is used.

Their extension to the unreduced target is explicit. The first covector reads the negative unmarked-`x2` row of the residual-pair top source input with coefficient `e21`; the second reads the negative unmarked-`x4` row with coefficient `e12`. The checker verifies that their boundaries have **only actual generic support**, and that evaluating the original nine-term transgression and its generic representative gives the same `epsilon`. The actual coefficient rows and their comparison are recorded for all six branch/pair transports.

The residue is not the scalar unit:

\[
\operatorname{Ann}_A(\epsilon)=I,
\qquad A\epsilon\cong A/I.
\]

In words: the supported primitive value forgets multiples of the two residual occurrences. It cannot be treated as a faithful replacement for an `A`-valued readout.

### All-order exactness proof

Define `s_x(e_ab)=e_(a+1,b)` and `s_y(e_ab)=e_(a,b+1)`. Let `P_x` and `P_y` project onto pole order one in the indicated variable. Then

\[
xs_x=1,\qquad s_xx=1-P_x,\qquad
ys_y=1,\qquad s_yy=1-P_y.
\]

In words: both multiplication operators are surjective; their failure to have two-sided inverses is precisely the order-one pole part.

For the Koszul complex with maps `(-y,x)` and `(x,y)`, set

\[
h_0(v)=(s_xv,0),\qquad
h_1(a,b)=s_xb-s_yP_xa.
\]

In words: these give exact preimage and homotopy formulas in every pole order. Direct substitution gives identity in degrees zero and one and `1-P_xP_y` at the top. Consequently its only homology is the residue socle at the top. This proves the displayed quotient isomorphism for all coefficients.

These homotopies are `S`-linear, **not `A`-linear**. They prove kernel/cokernel statements for an `A`-linear complex; no `A`-linear contracting homotopy of this nonprojective local-cohomology complex is asserted. The induced reverse-map isomorphism itself is `A`-linear.

## 4. The trace comparison space and its occurrence frame

Before imposing internal degree, objects lifting `epsilon` are pairs `(a,b)` with `xa+yb=epsilon`. A morphism from `(a,b)` to `(a',b')` is a `c` with

\[
a'-a=-yc,\qquad b'-b=xc.
\]

In words: these are the actual short-support cochain homotopies. Exactness proves the space is connected. Its automorphisms are

\[
\{c:xc=yc=0\}=S\epsilon.
\]

In words: forgetting occurrence degree yields a space equivalent to `K(A/I,1)`, with no higher homotopy groups. The same conclusion follows from the support triangle and the full Hom-complex grading [M2].

That is **not** the fixed-frame physical answer. The primitive trace has Hom occurrence degree

\[
\nu=-e_x-e_y.
\]

In words: the prescribed residue includes both ordered negative occurrence degrees, or equivalently the corresponding explicit determinant twist. In this frame the only primitive source-free modes are `e21` on `a_x`, `e12` on `a_y`, and `e22` on the homotopy column `a_xy`.

By contrast, a socle automorphism `epsilon` on `a_xy` has Hom occurrence degree zero. A polynomial multiple cannot move it to `nu`, since the quotient `A/I` has no negative residual occurrence degrees. Therefore the matching homogeneous trace fibre is contractible.

Over the spectator ring its fibre complex is simply

\[
S\xrightarrow{(-1,1)}S^2\xrightarrow{(1,1)}S.
\]

In words: it is exact. With all nine degrees fixed, replace `S` by its prescribed homogeneous piece. This conclusion was obtained **after** the `A`-linear calculation; it is not another coefficient-extraction shortcut.

The cohomological calculation, with ordered internal frames understood, is

\[
\begin{aligned}
H^0\operatorname{RHom}_A(C_Q,\mathcal C_I)&=\mathcal H,\\
H^{-1}\operatorname{RHom}_A(C_B,\mathcal C_I)&=\mathcal H,\\
H^{-2}\operatorname{RHom}_A(C_B,\mathcal C_I)&\cong A/I,\\
H^{-2}\operatorname{RHom}_A(C_K,\mathcal C_I)&\cong A/I.
\end{aligned}
\]

In words: the last line accounts for the ungraded comparison loops; its generator is in a different occurrence frame. All other groups are zero for these reduced complexes. The endpoint complex remains contractible in this frame after the supported output change because its original signed-unit contraction is `A`-linear.

## 5. Apply the same support operation to the actual normalization square

The source normalization is not an arbitrary pair of identical polynomial rings [S3]. In its label-preserving ambient occurrence presentation, with the other coefficients carried as spectators, write

\[
\begin{aligned}
\mathfrak B_+&=A/(X_0,X_2,X_4),\\
\mathfrak B_-&=A/(X_1,X_3,X_5),\\
C&=A/(X_0,\ldots,X_5),\\
\mathfrak B&=\mathfrak B_+\times_C\mathfrak B_-.
\end{aligned}
\]

In words: the plus sheet has the odd occurrence coordinates as its free branch variables; the minus sheet has the even ones. The common conductor is the zero section. The ring `B` has all mixed even-times-odd products zero.

The ideal `J_+=(X1,X3,X5)` **inside the plus sheet** is its conductor ideal. It is not the ambient ideal defining that sheet. This distinction also prevents equating an earlier normal-purity branch with a normalization sheet merely because both were labelled plus.

The source sequence is

\[
0\longrightarrow\mathfrak B
\longrightarrow\mathfrak B_+\oplus\mathfrak B_-
\xrightarrow{\varepsilon_+-\varepsilon_-}C
\longrightarrow0.
\]

In words: the two endpoint augmentations and their sign are supplied by the normalization square. No splitting or division by two is made.

Tensor this **entire sequence** with `C_I`. Its terms are flat over `A`, so the result is a degreewise exact sequence of complexes, naturally preserving both zero sections:

\[
0\longrightarrow\mathcal C_I(\mathfrak B)
\longrightarrow\mathcal C_I(\mathfrak B_+)\oplus\mathcal C_I(\mathfrak B_-)
\longrightarrow\mathcal C_I(C)\longrightarrow0.
\]

In words: this is a source-defined occurrence-support cospan. It is not built by assigning endpoint outputs after taking a scalar residue.

Since `x,y` are zero on the plus sheet and form a regular sequence on the minus sheet, its terms have

\[
\begin{aligned}
\mathcal C_I(\mathfrak B_+)&=\mathfrak B_+[0],\\
\mathcal C_I(\mathfrak B_-)&\simeq H_I^2(\mathfrak B_-)[-2],\\
\mathcal C_I(C)&=C[0].
\end{aligned}
\]

In words: one sheet is wholly contained in this occurrence support; on the other sheet it has codimension two. The same operation cannot be replaced by two identical unshifted residue maps.

The source total object has

\[
H^0\mathcal C_I(\mathfrak B)=J_+,\qquad
H^2\mathcal C_I(\mathfrak B)=H_I^2(\mathfrak B_-),
\qquad H^j=0\quad(j\ne0,2).
\]

In words: the plus-sheet conductor ideal and the minus-sheet residue channel are both retained. This is a cohomology calculation, not a declaration that the full supported source splits into these groups.

The checker verifies the source maps, integral exactness, and cohomology on all 729 negative/zero/positive exponent patterns. Exponent magnitudes do not change the incidence matrices; the proof therefore covers arbitrary polynomial degrees and pole orders.

## 6. The generic residue and the whole Gysin morphism specialize differently

A residue-valued generic map has the form

\[
\gamma:A[-2]\longrightarrow\mathcal C_I,
\qquad \gamma(1)=\frac1{xy}
\]

in the top Cech summand. In words: it is the map detected by the supported reverse trace.

At the conductor both localized variables are zero, so the nonempty Cech summands vanish under derived base change. This is computed on the flat complex, not by substituting zero into a fraction [M1]. Hence

\[
\mathcal C_I\otimes_A^LC\simeq C,
\qquad \gamma\otimes_A^LC=0.
\]

In words: the support **object** survives but this particular generic **morphism** does not. Every replacement of the same residue class has the same derived specialization. Indeed the resulting generic mapping group is

\[
\operatorname{Hom}_{D(C)}(C[-2],C)=0.
\]

In words: no same-degree map from that free generic line can carry a nonzero conductor value. The plus-sheet specialization of this free generic morphism is zero for the same reason.

The correct nonzero endpoint morphism uses the complete occurrence Koszul complex. Let

\[
\mathsf K_I^\bullet=[A\xrightarrow{(x,y)^T}A^2\xrightarrow{(-y,x)}A]
\]

in degrees zero, one, two, with its ordered dual conormal basis. Define

\[
\rho_I(e_H)=\left(\prod_{i\in H}X_i^{-1}\right)e_H,
\qquad H\subseteq\{2,4\}.
\]

In words: the bottom component is one, each middle component is its permitted single pole, and the top component is the double pole. The chain equation follows termwise from the actual localization maps. This construction is functorial over the node ring and both normalization sheets as well, even though the sequence is not regular on the node.

At the conductor,

\[
(\rho_I\otimes_A^LC)^0=1,
\qquad (\rho_I\otimes_A^LC)^1=(\rho_I\otimes_A^LC)^2=0.
\]

In words: the whole morphism retains a primitive bottom component. Its source Koszul differential is now zero, so no homotopy can remove that component. Before base change, and with the ordered determinant frame restored, its composite with the support counit is the regular codimension-two Gysin morphism.

The relevant normal-line statement is

\[
\operatorname{Ext}^2_A(A/I,A)
\cong(A/I)\otimes\det(I/I^2)^\vee.
\]

In words: its two-degree shift and dual determinant are substantive data, not a scalar normalization [M3]. Regular-immersion purity is used only on the ambient polynomial ring or the regular minus-sheet chart, not on the singular node ring.

An equivalent endpoint check is

\[
\operatorname{Tor}^A_2(\mathcal H,C)\cong C,
\qquad \operatorname{Tor}^A_j(\mathcal H,C)=0\quad(j\ne2).
\]

In words: the endpoint value is recovered through the top Tor of the local-cohomology module. Keeping only its ordinary tensor product would give zero. Ordinary `A`-linear maps from `H` to `C` are also zero: multiplication by `x` is surjective on `H` and annihilates `C`.

Thus neither taking the residue element alone nor inventing an unshifted evaluation `H -> C` supplies the endpoint continuation.

### The actual four target rows

The complete Gysin morphism lifts through the polynomial contraction to the original source-Hom complex. In the source's actual sign convention its only reference-chart rows are

| Input row | Output Cech component | Coefficient |
|---|---|---|
| `11 -> T` | Empty localization | 1 |
| `11 -> x2` | X2-localized | -1/X2 |
| `11 -> x4` | X4-localized | -1/X4 |
| `11 -> {x4,x2}` | X2,X4-localized | -1/(X2 X4) |

In words: `11` means the full residual-pair input, including the independent excess generator; the displayed target states are unmarked. These fractions are values of a covector into the output support complex, not coefficients inserted into the original unlocalized target states.

The checker verifies this complete degree-minus-two cochain on all unreduced columns, for all six transported charts. Its Hom occurrence degree is zero. Projecting its short-support restriction to top local cohomology gives exactly the socle comparison class from Section 4. That class had a different occurrence degree from the primitive residue trace.

This establishes a precise connection between the two constructions: the endpoint-surviving Gysin class is not an additional homotopy allowed in the residue trace's original frame. Its source determinant and shift must be transported explicitly.

## 7. What the whole source map retains over the singular normalization carrier

There is no need to assume Koszul exactness over the zero-divisor node ring. The same monomial calculation gives

\[
\begin{aligned}
H^0(\mathsf K_I^\bullet\otimes_A\mathfrak B)&=J_+,\\
H^1(\mathsf K_I^\bullet\otimes_A\mathfrak B)&=J_+e_2\oplus J_+e_4,\\
H^2(\mathsf K_I^\bullet\otimes_A\mathfrak B)&=(\mathfrak B/I\mathfrak B)e_{24}.
\end{aligned}
\]

In words: the selected occurrence pair is zero on one normalization sheet, so its Koszul source has additional grades. They are not silently discarded.

Under `rho_I`, degree zero maps identically to `J_+`; degree one maps to zero; degree two kills its positive odd-sheet part and maps `B_-/I` primitively into the residue socle. The full source map nevertheless keeps the lower components and both conductor augmentations. Taking only the induced degree-two map would again lose the endpoint extension.

All these maps come from the same functorial Koszul-to-Cech formula, so the normalization square and both zero-section squares commute before taking cohomology. Reflection exchanges the two branch roles and transports the ordered residue determinant. No reflection one-cochain or parity is selected by these coefficient identities.

## 8. Compatibility with the independent supported Rees operation

The residual occurrence pair and the already selected branch coordinates are disjoint. On the ambient regular coefficient chart, the product map is ordered by

\[
(X_2,X_4,X_1,X_3,X_5).
\]

In words: compose the residual occurrence support with the previous three-normal branch support without identifying the variables. The resulting ambient Gysin class has codimension five and the product determinant, not codimension three. A physical construction cannot erase the extra two shifts merely because both factors have primitive local representatives.

For the declared branch equations `u_i=t_i X_i`, the branch residue is `t_i/u_i` in its own localized summand. Tensoring the **complete** occurrence map with that support map gives a chain map on all 128 states after the residual pair and independent excess are included. On each of the eight central Rees faces, a target summand localizing a vanished product disappears; the lower coefficients remain. Every tensor chain equation is checked with the degree signs intact.

The independent excess factor has coefficient one on both sides of the tensor comparison. It is not replaced by a product of internal normal parameters. This is a tensor statement about explicit support morphisms, not a claim that the bare excess has a nonzero same-degree physical homology image.

No regularity is inferred after passing to the singular normalization carrier. There the full derived Koszul complexes, including their additional grades, are retained.

## 9. Consequence for the physical source-to-kernel construction

The residual occurrence-support operation is now explicit over the full coefficient family and natural on the actual normalization square. It supplies a primitive supported reverse trace and a separate, primitive endpoint Gysin morphism.

It also proves that the two cannot be identified as the same unshifted generic map. The residue-valued generic map dies at the conductor; the whole occurrence Koszul map survives through its lower coefficient and determinant shift. The source-level zero-section comparisons are coupled by the conductor difference rather than assigned independently.

What remains is an exact source-to-spatial-kernel comparison carrying this full occurrence Koszul/Gysin morphism to the two previously constructed spatial collar operators, in their actual occurrence, normal, and Rees frames. This calculation does not prove that those coefficient maps are the physical connector 2-cells. It does not repair the earlier null generic ordinary-blowdown morphism, and it does not select physical parity.

The new requirement is therefore sharper than “add an occurrence residue”: retain the entire occurrence extension and prove its endpoint and spatial transport, with the extra codimension-two determinant accounted for.

## 10. Verification and sources

Run:

```sh
python check_marici_occurrence_support_conductor_trace.py \
  --output marici_occurrence_support_conductor_trace_certificate.json
```

The checker passes **35,051 exact assertions**; their categories are recorded in the accompanying certificate. The checker is self-contained and requires only the Python standard library. It reconstructs the previous polynomial source-Hom models, verifies the signed-unit reductions and reference full-source purity cones, constructs both supported reverse covectors and the full four-row Gysin cochain, checks all six transports, classifies every source-normalization exponent-sign pattern, and verifies the complete 128-state tensor maps on eight Rees faces.

The arbitrary-pole and arbitrary-polynomial statements follow from the all-order formulas and monomial-support arguments in this note. Finite tests are not presented as proof of an infinite-rank Smith calculation. The pole-shift homotopy is explicitly not claimed to be `A`-linear. No proof assistant or repository write was used.

### Pinned source data

[S1] `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`.

[S2] `research/voevodsky/check_d03_plus_excess_beck_chevalley.rs`, blob `df8448271089910a90c8e641af5b8ae95f1472dd`.

[S3] `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`, blob `840258522d45e450e4f1e8bb927d9aae58c75566`. Its spectator ring is extended harmlessly to the retained occurrence base; no new identification of its spectator variables with physical normal lines is assumed.

Immediate predecessor: `marici_occurrence_linear_reverse_pairing.md` and its checker. That checker was rerun successfully before this continuation. Its distinction between the full coefficient family and one numerical homogeneous slice remains in force.

### General mathematical constructions

[M1] Stacks Project, Local cohomology, tag `0952`, especially the flat extended Cech model, exactness, and derived base change: https://stacks.math.columbia.edu/tag/0952.

[M2] Stacks Project, Hom complexes, tag `0A8H`: https://stacks.math.columbia.edu/tag/0A8H.

[M3] Stacks Project, The Koszul complex, tag `0621`: https://stacks.math.columbia.edu/tag/0621. The two-variable exactness and the endpoint Gysin representative used here are also proved by the displayed explicit complexes.
