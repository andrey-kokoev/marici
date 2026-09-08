# Native normalization pullback of the independent excess

Date: 2026-09-07  
Project: Marici  
Input commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`  
Continuation of `marici_completed_toric_descent.md` and `marici_joint_triangle_rees_gysin.md`

## 1. Result and scope

The selected branch/pair Koszul source has now been pulled back through the **actual two-sheet normalization diagram**, not appended as an unnamed exterior line to an endpoint readout. The resulting derived source has different excess packets on its two sheets and a nonzero conductor connecting map. Its complete homology and the raw-to-selected comparison are computed below.

The main result distinguishes two statements which are easily conflated.

* The source-prescribed selection preserves the independent excess generator eta with coefficient one.
* On the joint native conductor it reaches six first-conormal attachment channels primitively, but its images in eight higher-wedge channels lie in proper quadratic or cubic short-Rees ideals.

At the central **short**-Rees face the six first-conormal channels survive; the eight higher-wedge images vanish, although their selected-source target classes remain nonzero. The surviving map is the native first conormal symbol, with an actual Koszul homotopy. Looking only at the original connecting representatives would incorrectly conclude that all fourteen images vanish: six have different, explicitly constructed source lifts.

These are statements about a derived **source** correspondence and its base-changed cap. They do not yet identify the conductor channels with the two physical spatial collar 2-cells. The normalizations, shifts, endpoint coefficients, and physical parity have not been inferred from a count of exterior generators.

Throughout this note, `t0,...,t5` denote the six **short-Rees** parameters. The three long-Rees parameters of the completed toric-descent theorem are independent spectators. The calculation does not identify either family with occurrence coordinates or with physical normal lines.

## 2. The actual source diagram

Let S be a polynomial spectator ring over the integers. Put

\[
R=S[t_0,\ldots,t_5],\qquad A=R[X_0,\ldots,X_5],
\]

\[
I_E=(X_0,X_2,X_4),\qquad I_O=(X_1,X_3,X_5).
\]

In words: the occurrence and Rees coordinates remain independent. Long occurrence and normal coordinates can be included in S. The stated monodromy-unit localizations may be restored afterwards; they are units equal to one on the conductor and do not invert a short Rees parameter.

The native source [S1] is

\[
B=A/(I_EI_O),\qquad B_+=A/I_E,\qquad B_-=A/I_O,\qquad C=A/(I_E+I_O)=R.
\]

In words: the plus sheet carries odd occurrence coordinates and the minus sheet carries even occurrence coordinates. The selected normal branch below is not silently identified with either of these two coordinate-ring embeddings.

Keep the normalization sequence and its specified difference:

\[
0\longrightarrow B\longrightarrow B_+\oplus B_-
\xrightarrow{\varepsilon_+-\varepsilon_-}C\longrightarrow0.
\]

In words: the two zero-section maps remain coupled.

For the selected plus-normal/D03 intersection, use the complete source

\[
D_x=K_A(X_1,X_3,X_5,t_0X_0,t_3X_3).
\]

In words: select the three odd occurrence equations but retain the opposite pair's original product equations. The fifth normal is the second copy of the shared direction. The original support-directed source and the reciprocal-twist normalization are [S2]; the product-Rees selection is the one already constructed in the preceding branch-purity and endpoint calculations.

Write the degree-one generators in order as

\[
h_1,h_3,h_5,h_0,h_3^{03},\qquad
\eta_x=t_3h_3-h_3^{03}.
\]

In words: eta is an independent closed difference. Its internal degree is the sum of the X3 and t3 degrees, even after t3 is set to zero.

The integral basis change has determinant minus one and gives

\[
D_x\cong K_A(X_1,X_3,X_5,v)\otimes\Lambda(\eta_x),
\qquad v=t_0X_0.
\]

In words: only four independent equations remain in the differential; the fifth exterior generator has zero differential. No parameter is divided out. The standard functoriality of the Koszul complex justifies the induced map on every exterior degree [M1].

Define the derived source objects

\[
\mathcal D_B=B\otimes_A D_x,\quad
\mathcal D_\pm=B_\pm\otimes_A D_x,\quad
\mathcal D_C=C\otimes_A D_x.
\]

In words: since D_x is bounded finite free, these are the actual derived tensor products. They are the affine derived pullbacks of the supplied normalization diagram along the derived zero locus represented by D_x. This does not claim that a derived normalization morphism has been constructed anew.

There is a strict exact sequence of complexes

\[
0\longrightarrow\mathcal D_B\longrightarrow
\mathcal D_+\oplus\mathcal D_-\longrightarrow\mathcal D_C
\longrightarrow0.
\]

In words: all five source wedges occur at both sheets and at the conductor, with the original augmentation difference. Taking degree-zero quotients before this tensor product would lose the result below.

## 3. The two sheet packets are different

Set

\[
R_E=R[X_0,X_2,X_4],\qquad M=R_E/(v).
\]

In words: M retains the opposite product-normal equation; it is not the conductor ring C.

The exact sheet homology is

\[
H_*(\mathcal D_+)\cong C\otimes\Lambda(h_0,\eta_x),
\]

\[
H_*(\mathcal D_-)\cong
M\otimes\Lambda(h_1,h_3,h_5,\eta_x),
\]

\[
H_*(\mathcal D_C)\cong
C\otimes\Lambda(h_1,h_3,h_5,h_0,\eta_x).
\]

In words: the plus sheet has two excess generators, the minus sheet has four, and the conductor retains all five. Their exterior multiplicities are respectively (1,2,1), (1,4,6,4,1), and (1,5,10,10,5,1), over the distinct rings displayed above.

**Proof.** On B+, the three odd occurrence equations are a regular sequence, while v vanishes identically. On B-, all three odd equations vanish, while v is a non-zero-divisor before quotient. At C every equation is zero. Apply the displayed integral excess basis change on each object. The maps on homology are the labelled exterior inclusions and the even-variable augmentation; they are not independently chosen identifications.

This is not a dimension-count obstruction to every physical correspondence. It is an exact statement of the source data that such a correspondence must use. In particular, a single eta line is not the full source restriction at either endpoint.

## 4. Complete native homology and its conductor submodules

Let

\[
I=(X_0,X_2,X_4)R_E,\qquad J=I/(vI).
\]

In words: J is the augmentation ideal modulo its product with v. It is **not** the image ideal I/(v) inside M. The distinction is essential.

Let V_O denote the free labelled module with basis h1,h3,h5, including their occurrence degrees. As a graded homology module,

\[
H_*(\mathcal D_B)
\cong
\left(M\oplus\bigoplus_{k=1}^{3}J\otimes\Lambda^kV_O\right)
\otimes\Lambda(\eta_x).
\]

In words: M is in homological degree zero; the term with k odd wedges is in degree k; eta adds one degree and its own internal conormal degree. This is a **homology-module formula**, not a formality or splitting theorem for the whole coupled differential graded object.

**All-degree proof.** First tensor the normalization sequence with K(X1,X3,X5). The plus complex has only its degree-zero C, the minus complex has zero differential, and its map to the conductor is surjective in every exterior degree. The long exact sequence therefore gives B- in degree zero and I tensor exterior-k V_O in degrees k=1,2,3. Multiplication by v is injective on B- and on I. Adding K(v) gives their quotients by v, with no new kernel groups. Finally retain the independent eta factor. This proves the formula for arbitrary polynomials, not only for the homogeneous matrices checked by the executable.

There is an exact sequence

\[
0\longrightarrow C\langle v\rangle
\xrightarrow{1\mapsto[v]}J\longrightarrow M\longrightarrow C
\longrightarrow0.
\]

In words: the map J to M has a primitive conductor-supported kernel generated by [v]. Although v is zero in M, its class in J is not zero. Its annihilator is the full short-occurrence ideal, and no integer or Rees parameter annihilates it.

This kernel explains the conductor connecting map. For a nonempty ordered subset T of {1,3,5}, write h_T for its wedge and let e be zero or one. With the source order (h1,h3,h5,h0,eta),

\[
\partial\left[(-1)^{|T|+1}h_T\wedge h_0\wedge\eta_x^e\right]
=
[vh_T\wedge\eta_x^e].
\]

In words: lift the conductor wedge on the minus sheet with the prescribed difference sign and take its actual boundary. It is zero on the plus sheet and is the indicated native cycle on the minus sheet.

All fourteen right-hand classes are nonzero, primitive conductor lines. They occupy homological degrees one through four with multiplicities (3,6,4,1). Their distinct exterior and determinant degrees are retained; they are not fourteen alternative units.

The existing Koszul cells give every occurrence-annihilator homotopy. Multiplication by an odd coordinate is already zero by the node relation. For an even coordinate, the boundary of its multiple of h_T wedge h0 wedge eta is the corresponding multiple of v h_T wedge eta, with the displayed Koszul sign. The monomial basis of J proves that there are no additional coefficient annihilators.

## 5. Raw-to-selected transport: fourteen representatives are not the whole image

The raw source is

\[
D_u=K_A(t_1X_1,t_3X_3,t_5X_5,t_0X_0,t_3X_3),
\qquad \eta_u=h_3^+-h_3^{03}.
\]

In words: both copies of the shared normal now have the same product equation. The source-prescribed selection s is

\[
s(h_i)=t_i h_i\quad(i=1,3,5),\qquad
s(h_0)=h_0,\qquad s(\eta_u)=\eta_x.
\]

In words: it preserves the excess primitively but scales the three branch normal generators. These formulas are checked on all 32 wedges, before and after the integral excess basis changes, on all six labelled branch/pair charts.

On the original conductor connecting representatives,

\[
s_*[vh_T\wedge\eta_u^e]
=
\left(\prod_{i\in T}t_i\right)
[vh_T\wedge\eta_x^e].
\]

In words: the original representative acquires its full branch-Rees product. It follows that all fourteen **such images** vanish on the central branch Rees face. That observation alone does not determine the image of the complete derived map.

### Primitive first-conormal lifts

For a single branch label i, use the different source cycle

\[
X_i h_0\wedge\eta_u^e.
\]

In words: it is closed in the raw native complex because Xi times v is a forbidden mixed product in B. Selection preserves this cycle coefficientwise.

In the selected complex,

\[
d(h_i\wedge h_0\wedge\eta_x^e)
=
X_i h_0\wedge\eta_x^e-vh_i\wedge\eta_x^e.
\]

In words: the existing two-normal cell identifies its image with the primitive conductor attachment. Thus all six first-conormal/eta channels have primitive lifts, including at the central branch Rees face.

The induced first-conormal map has the explicit form

\[
\theta:I_Oh_0\longrightarrow C\langle v\rangle\otimes V_O,
\qquad
\theta(gh_0)
=
v\sum_{i\in\{1,3,5\}}
\left(\frac{\partial g}{\partial X_i}\right)_{X_1=X_3=X_5=0}h_i.
\]

In words: the first odd normal symbol maps to the corresponding conductor attaching class. Its kernel is I_O squared times h0. The eta-labelled version is obtained by retaining the eta factor.

This map is A-linear **into its conductor-supported target**: all short occurrence coordinates annihilate that target. It is not the non-A-linear operation of extracting a monomial coefficient and calling it a polynomial scalar unit. It is the same first-conormal quotient intrinsic to the native normalization square, now obtained from an explicit source-to-source Koszul homotopy.

### Exact higher-wedge image ideals

On a prescribed conductor line, the full raw-to-selected homology map has image

\[
\operatorname{im}_T=
\begin{cases}
C,&|T|=1,\\
\left(\prod_{i\in T}t_i\right)C,&|T|=2,3.
\end{cases}
\]

In words: the six first-conormal channels are primitive; the six two-wedge channels have pair-product image ideals; the two top-wedge channels have the full triple-product image ideal. The statement includes both eta degrees.

**Completeness proof.** Before adjoining K(v), the raw branch Koszul complex on B has I tensor exterior-k of the raw branch normals in all positive degrees. The branch products form a regular sequence on the plus sheet, so there is no additional positive-degree plus homology. Adding K(v) is injective on those positive-degree I modules. Therefore in degrees k at least two the full raw homology is exactly J tensor exterior-k, and selection is multiplication by the indicated product on each labelled wedge. There are no other raw classes or homotopies that can enlarge that image.

Degree one is different. The kernel of multiplication by v on the raw degree-zero module contributes additional classes. The cycles Xi h0 constructed above are precisely what restores the primitive conductor image in that degree. This is why using only the original connecting representatives gives the wrong answer.

At the central branch Rees face,

\[
t_1=t_3=t_5=0,
\]

in words: keep the opposite Rees parameter t0 as a spectator. The complete comparison reaches six of the fourteen selected conductor lines and misses eight. Each of the eight is still a nonzero selected-source target class, since its coefficient module C is free over the branch Rees parameters. Homotopic replacements of the selection cannot alter this image after derived base change.

The raw connecting representatives themselves become boundaries at this center: their branch differentials are zero, and the boundary of h_T wedge h0 is, up to sign, v h_T. The selected first-jet classes must not be confused with those specialized raw representatives.

The executable computes the complete source and target homology maps and their cones in all fourteen relevant central frames. It additionally checks the full polynomial image ideals in 189 Rees-degree frames. The proof above supplies the all-exponent statement.

These are short-Rees divisor-support defects, not order-two or order-three integer torsion. There is no numerical averaging procedure that turns their proper ideals into the unit ideal.

## 6. The cap and both endpoint equations remain coupled

The preceding native source P has fifty free generators and the actual target K has 215 loaded states. Reconstruct its complete 43-term cap F and the six-term native endpoint composite a, on the declared short-Rees graph. They obey

\[
d_KF-Fd_P=a,\qquad d_Ka+ad_P=0.
\]

In words: both endpoint composites belong to the same source-to-target mapping equation. The target localization domains are the ones supplied in [S3].

The derived source pullback has free model P tensor D_x. Its 1,600 generators map to the 6,880-state target K tensor D_x. The cap contains 1,376 terms and the endpoint composite contains 192 terms. The executable checks on every source generator

\[
\mathsf d(F\otimes1)=a\otimes1,\qquad
\mathsf d(a\otimes1)=0.
\]

In words: no endpoint is dropped when the actual excess source is introduced. The raw-to-selected squares commute for both parts of this complete map.

The target here is the **derived-base-changed** target. The calculation does not construct an additional counit back to the original physical target or identify a selected source Gysin channel with a framed collar. Such a counit would be the extra geometric assertion still requiring proof.

At a fixed common ambient ring, tensoring with D_x is a perfect operation. It therefore preserves the previous finite-stage diagrams and commutes with their intrinsic derived inverse limits. The completed long-normal descent theorem does not enlarge the image of the specified short-source selection. This statement does not interchange an inverse limit with adjoining a new polynomial ring or with naive chart completion.

## 7. A direct source-identification control

One possible shortcut would identify the native conductor dual with the selected excess-top dual by a degree-zero polynomial map from P to D_x. Allow even the internal determinant adjustment necessary for a unit top coefficient:

\[
\lambda=e_{X_3}-e_{X_2}-e_{X_4}+e_{t_0}+e_{t_3}.
\]

In words: the selected five-wedge and the native six-occurrence top have different labelled determinants. The negative entries specify a mapping degree, not permitted denominators.

The entire homogeneous Hom complex in this degree has 180 coefficient columns, including every possible polynomial map and homotopy. Its 90 signed-unit cancellations leave no cohomology, and it has no positive homological-degree term. Consequently its degree-zero cycle space is itself zero. In particular no degree-zero map has the required unit top coefficient.

This control is scoped to an ordinary ambient-ring-linear source map. It does not exclude the different supported, Gysin, or mixed-variance comparison required by the physical problem. It does prove that the primitive excess generator cannot simply be identified with the native conductor top by forgetting their surrounding complexes. Derived Hom is computed with the differential in [M2].

## 8. Verification and boundary of the result

Run:

```sh
python check_marici_native_excess_conductor_transport.py \
  --output marici_native_excess_conductor_transport_certificate.json
```

The full run performs **136,179 exact assertions**. It includes 8,748 occurrence/Rees domain patterns across all four source objects, hence 34,992 complete homogeneous complexes; 6,660 integral unit cancellations in that census; every labelled wedge and selection square on six charts; all fourteen conductor connectors and their occurrence-annihilator witnesses; the full central selection maps rather than selected representatives alone; the 189 all-image test frames; the complete base-changed cap and both endpoint equations; and the all-replacement source-identification control.

The all-degree homology and image-ideal results are established by the module arguments above. The executable verifies their exact chain models. It is not proof-assistant certification, and the assertion count is not a count of independent theorems.

The concrete remaining physical test is now sharper. A candidate collar correspondence must realize the first-conormal maps already constructed, retain eta, and explain how its supported operations act on the eight quadratic/cubic short-Rees attachment channels. It may not replace the two actual sheet excess packets by identical eta lines, or infer all-channel preservation from the coefficient-one image of eta alone.

The complete physical collar identification and reflection parity remain unassigned.

## Sources

[S1] `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`, blob `840258522d45e450e4f1e8bb927d9aae58c75566`, at the pinned commit: actual branch ring quotient, conductor difference, and first conormal symbol.

[S2] `src/ledger/20260814-100 Support-Directed Can-Var Packet and Three Local Cousin Traces.md`, blob `d5ed0c89e804284a4bf45bfa1e0c0bc2eab6eb12`: reciprocal/original support convention, repeated-normal excess, and its forced Laurent-unit normalization.

[S3] `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`: actual loaded target differential and legal coefficient domains.

[M1] Stacks Project, tag `0621`, The Koszul complex: exterior basis changes, tensor products, and multiplication-cone interpretation.

[M2] Stacks Project, tag `0A8H`, Hom complexes: complete source-to-target differential and tensor–Hom sign rules.

[M3] Stacks Project, tag `014D`, Cones and termwise split sequences: mapping cones and their homotopies.

Preceding locally retained constructions: `marici_joint_triangle_rees_gysin.md`, `marici_joint_conductor_spatial_cap_comparison.md`, and `marici_completed_toric_descent.md`. Their scope qualifications remain in force.
