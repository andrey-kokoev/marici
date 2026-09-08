# Conductor operations, globally framed transports, and the endpoint descent class

Date: 2026-09-07  
Lane: Branch B  
Repository baseline: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result and scope

The previously constructed unbounded conductor resolution now has explicit composition operators. Six signed last-block contractions give a multiplicative model of the conductor's derived endomorphisms, over the spectator ring. The fourteen resolved coefficient channels carry its corresponding operation modules.

The globally framed automorphisms of the actual normalization source also have explicit lifts to this resolution. After derived conductor restriction, their action on normalized markings is translation by the first conductor derivatives. The action kernel consists exactly of quadratic-and-higher occurrence tails. This gives a computable action infinity-groupoid with infinitely many nonzero higher homotopy groups.

Nevertheless, no number of these higher conductor paths changes a nonzero global endpoint extension class while preserving the generic quotient and labelled kernel channels. We compute the separate, globally framed extension groupoid, including all its equivalences and automorphisms. It is a 1-type, not the same object as the unbounded derived conductor marking space.

All statements concern the already specified seven-chart coefficient model. This is not an identification with the native physical normalization/PC source, not a new choice of physical inverses, and not an RH criterion. The generic quotient in the normalization extension is not silently identified with the full seven-state physical Q complex. Existing occurrence, normal, residue-channel and endpoint lines remain labelled; rank formulas below suppress their fixed trivializations.

## 1. Coefficients and the fixed open

Let the positive short labels be 13, 15, 35 and the negative short labels be 02, 04, 24. Let the long labels be 03, 14, 25. Put

\[
\mathcal C=\mathbb Z[t_s,X_l,u_l\mid s\in S_+\cup S_-,\ l\in L],
\qquad
\mathcal B=\mathcal C[X_s\mid s\in S_+\cup S_-]/(X_pX_m:p\in S_+,m\in S_-).
\]

In words: the two occurrence sheets share the full Rees and independent long-parameter ring. Opposite-sheet occurrence products vanish; normal parameters are not identified with each other.

Write I-plus and I-minus for their occurrence ideals. Set

\[
\tau_+=\prod_{p\in S_+}t_p,\qquad
\tau_-=\prod_{m\in S_-}t_m,\qquad T=\tau_+\tau_-,
\qquad
\mathfrak a=(T,\tau_+I_+,\tau_-I_-).
\]

In words: T is the six-normal product and the displayed ideal is the previously proved local lifting ideal. Our test open is

\[
V=\operatorname{Spec}\mathcal B\setminus V(\mathfrak a).
\]

Its seven charts are D(T), the three D(tau-plus X-p), and the three D(tau-minus X-m). Positive and negative occurrence charts have empty intersections with each other. The nonempty Cech summands have counts 7, 12, 8, 2 in degrees zero through three.

Use

\[
\mathcal C_+=\mathcal C[\tau_+^{-1}],\qquad
\mathcal C_-=\mathcal C[\tau_-^{-1}],\qquad
C=\mathcal C_T=\mathcal C[T^{-1}].
\]

In words: each sheet permits its own normal inverses; the central chart permits all six. These rings are existing rings of the test open, not enlargements of the native physical coefficient domain.

On the central chart, abbreviate

\[
B=C[x_1,x_2,x_3,y_1,y_2,y_3]/(x_i y_j),\qquad
I=(x_1,x_2,x_3,y_1,y_2,y_3),\qquad B/I=C.
\]

Here x-labels are the ordered positive occurrences and y-labels the ordered negative ones. These lower-case symbols do not denote Rees parameters.

## 2. The existing all-degree resolution

Let P be the conductor resolution. A basis word is an alternating list of nonempty ordered exterior blocks, each block wholly on one sheet. Its homological degree is the sum of its block lengths. The empty word is the degree-zero generator. The differential is

\[
d[A_1|\cdots|A_k]
=\sum_{i\in A_1}(-1)^{\operatorname{pos}_{A_1}(i)}
X_i[A_1\setminus\{i\}|A_2|\cdots|A_k].
\]

In words: act on the first block, remove one label with its exterior sign, and multiply by the corresponding occurrence. Delete an empty block. Positions are zero-based. Cross-sheet products make the successive-block part of the square of the differential zero; usual Koszul cancellation handles a single block.

For completeness, the earlier integral contraction can be described on a pure occurrence monomial times a word. If the monomial is constant, set the contraction to zero. Otherwise select its sheet. If the first word block has that sheet, take it as A; otherwise take A empty and leave the entire word as suffix. Let i be the least index in the monomial support together with A. If i lies in A, set the result to zero. Otherwise remove one factor X-i from the monomial and insert i in A with its exterior insertion sign. This operator is C-linear, not B-linear. It satisfies

\[
dh+hd=1-\iota\epsilon.
\]

In words: P resolves the conductor integrally. This formula proves exactness in every degree and at arbitrary polynomial exponents. The word construction is the explicit fibre-product resolution underlying the known fibre-product cohomology method [M1]; the present calculation retains the integral spectator coefficients and source labels.

As a cohomological complex P is bounded above and termwise free, hence K-projective. Tensoring it with C makes every differential zero. The series of free conductor Tor ranks is

\[
a(z)=\frac{(1+z)^3}{1-3z-3z^2-z^3}.
\]

In words: these are the previously proved ranks 1, 6, 24, 92, 354, 1362, 5240, and so on. They count free coefficient generators, not integer-prime torsion.

## 3. Six operators give the complete Yoneda algebra

For each of the six labels i define the B-linear operator T-i on P by acting on the last block:

\[
T_i[A_1|\cdots|A_k]
=(-1)^{|A_1|+\cdots+|A_{k-1}|+\operatorname{pos}_{A_k}(i)}
[A_1|\cdots|A_k\setminus\{i\}].
\]

In words: remove the chosen last-block label with the displayed total-degree sign. The result is zero when the label is absent; delete an emptied last block. Each operator lowers homological degree by one, so has cohomological endomorphism degree one.

The identities are

\[
dT_i+T_id=0,\qquad T_i^2=0,
\qquad T_iT_j+T_jT_i=0\quad(i,j\text{ on the same sheet}).
\]

In words: these are actual cocycles and relations in the endomorphism differential graded algebra. The last condition applies only within one exterior block's sheet.

Here is an all-degree verification. When first and last blocks are distinct, the two differential orders operate on disjoint blocks; removing a first-block label changes the prefix sign of T-i by one, so they cancel. When there is only one block, the usual exterior contraction calculation gives the same equation. If a singleton block disappears, the first-block boundary term across the two sheets is zero by the ring relation, or the same prefix-sign cancellation applies. The square and same-sheet anticommutators are exterior contraction identities on the last block; after its deletion, the next block is on the opposite sheet, so no extra same-sheet term occurs. No division is used.

Let

\[
\mathcal E=
\Lambda_C(\xi_{13},\xi_{15},\xi_{35})
*_C
\Lambda_C(\eta_{02},\eta_{04},\eta_{24}).
\]

In words: take the free product of the two associative exterior algebras over their shared coefficient ring. This is not their graded-commutative tensor product. Its defining relations are six squares and six within-sheet anticommutators. A normal basis is again given by alternating nonempty exterior words.

Sending these generators to the T-i gives a unital C-dg-algebra map from E, with zero differential, to End-B(P). To prove it is a quasi-isomorphism, let T-w be the ordered product for a normal word w, with the rightmost operator acting first. For degree-n words w and v,

\[
\epsilon T_w(v)=(-1)^{n(n-1)/2}\delta_{w,v}.
\]

In words: the products pair, up to one common degree sign, as the complete dual basis of the resolution. This follows by deleting labels in reverse word order. If the block patterns differ, at the first mismatch the requested label is absent. If they agree, each successive prefix produces the displayed total sign.

The augmentation-induced map End-B(P) to Hom-B(P,C) is a quasi-isomorphism of complexes because P is K-projective and P to C is a quasi-isomorphism. The latter Hom complex has zero differential. The displayed dual-basis identity is therefore an isomorphism on every cohomology group. Consequently

\[
\mathcal E\xrightarrow{\simeq}\operatorname{End}_B(P)
\simeq R\operatorname{Hom}_B(C,C)
\]

as C-dg algebras, with the endomorphism convention fixed by actual composition [M2]. In words: this supplies a multiplicative, locally formal model, not just its Hilbert series. The first arrow is the constructed multiplicative map; the second denotes the endomorphism model of the derived endomorphism algebra, not an assertion that the augmentation-induced map is multiplicative.

**Scalar scope:** individual operators are B-linear. The displayed algebra map is a C-dg-algebra map, not a strict B-dg-algebra map. Positive occurrences act trivially on Ext but multiplication by an occurrence is not literally the zero endomorphism of P.

There are no cross-sheet relations. For example, xi-13 eta-02 and eta-02 xi-13 evaluate on different degree-two basis words. Arbitrarily long alternating products remain independent. This explicit integral operator construction is an application of the fibre-product algebra phenomenon [M1], not a claim to have discovered that general phenomenon.

## 4. Operations on every source channel

Let E-sigma be the corresponding exterior subalgebra and let

\[
J_\sigma^{\mathcal E}=\mathcal E\,\mathcal E_\sigma^{>0}.
\]

In words: it is the left ideal of normal words ending on sheet sigma. The resolution of I-sigma is the conductor resolution's words ending there, with their degrees reduced by one and the first differential augmented to I-sigma.

The normalization ideal sequence and its connecting morphism give

\[
\operatorname{Ext}_B^n(I_\sigma,C)
\cong (J_\sigma^{\mathcal E})^{n+1}.
\]

In words: the channel's operations are left Yoneda multiplication on these words. The connecting map is an isomorphism starting in degree zero: Hom(B,C) restricts to zero on I, while higher Ext from B is zero. Its two summands are exactly the two ending-sheet word subspaces. Naturality of the connecting map verifies the module structure, including the degree reindexing.

Every word in this module ends in a final label. Removing that label leaves a left factor. Therefore each I-sigma module is generated by its three degree-zero classes, with the exterior relations inherited from its own sheet.

The actual central normalization coordinates identify the fourteen-channel source with B plus seven copies of each ideal. Hence

\[
\operatorname{Ext}_B^*(\mathcal S_{14},C)
\cong C_{\mathrm{aug}}\oplus
\bigoplus_{j=1}^{7}(J_+^{\mathcal E})^{*+1}
\oplus\bigoplus_{j=1}^{7}(J_-^{\mathcal E})^{*+1}.
\]

In words: the generic coefficient contributes degree zero only, while forty-two labelled degree-zero channel generators generate the entire higher operation module. The positive-degree algebra kills the generic contribution. Both endpoint channels are complete such modules, not single isolated classes.

The ranks for one channel are the coefficients b-n of

\[
b(z)=\frac{3+3z+z^2}{1-3z-3z^2-z^3}.
\]

Thus b-n are 3, 12, 46, 177, 681, 2620, and the full source ranks are 43, 168, 644, 2478, 9534, 36680 in successive homological degrees.

There is also a useful degreewise matrix-dual coalgebra. Choose the word bases dual to these Yoneda bases. Its coproduct includes cuts between blocks and all nontrivial ordered subset splits of a block, with the exterior shuffle sign. The channel coaction omits terms having an empty right suffix. The construction is matrix-dual to the verified associative multiplication and module action, so is coassociative. It provides a necessary operation-naturality test on the degreewise free Tor groups with this stated convention. We do not claim an independently constructed E-infinity coalgebra or a geometric diagonal on a native spatial source.

A map swapping [13|02] and [02|13] while fixing degree one preserves ranks and occurrence multidegrees, but not the matrix-dual reduced coproduct: their respective terms are 13 tensor 02 and 02 tensor 13. Within one positive channel, swapping [13|02|15] and [15|02|13] while fixing the lower degrees likewise fails E-linearity. The first is xi-13 acting on the already fixed eta-02 xi-15 class. This gives concrete falsifiers of a ranks-only identification.

These Yoneda products are operations on derived coefficients. They are not the composition of paths in the additive marking space and are not Whitehead products. The additive Dold-Kan model does not acquire nonlinear homotopy torsion merely because this associative operation algebra is noncommutative.

## 5. The actual normalization residues and global frame group

Retain the fourteen channels indexed by a sheet sigma and a nonempty subset N of the opposite short triple. Let P-N and L-N be the same-sheet short labels and long labels compatible with every member of N in the labelled hexagon. In fixed channel frames the residue is

\[
r_{\sigma,N}=
\frac{\prod_{l\in L\setminus L_N}u_l}
{\prod_{n\in N}t_n\prod_{p\in P_N}t_p}.
\]

In words: retain its exact opposite-sheet pole subset, all additional allowed own-sheet denominators, and its independent long-normal numerator. The two endpoint residues are U-L divided by tau-minus and U-L divided by tau-plus, where U-L is u-03 u-14 u-25. Overall orientation signs can be included in the fixed channel lines and do not alter the tests below.

Let

\[
\mathcal M=\widetilde I_+^{\oplus7}\oplus\widetilde I_-^{\oplus7}
\]

on V. For a general residue vector r in C to the fourteenth power, the same normalization pullback defines an extension

\[
0\longrightarrow\mathcal M\xrightarrow{\iota}\mathcal S(r)
\xrightarrow{q}\mathcal O_V\longrightarrow0.
\]

In words: the sheet coefficient's conductor value is multiplied by each r-channel and matched by its branch residue coordinate. Branch coordinates on the other sheet supply the remaining normalization equations. All source channels and both endpoints are kept.

An automorphism fixing the kernel and quotient pointwise is necessarily

\[
g_f=1+\iota f q,\qquad f\in\operatorname{Hom}_V(\mathcal O_V,\mathcal M)
=\Gamma(V,\mathcal M).
\]

In words: the difference from the identity factors through the quotient and then into the kernel. Since q-iota is zero, these shears compose by addition and invert by negation. There are no missing choices of automorphism under this specified framing.

The global sections are

\[
G_{\mathrm{fr}}=
I_+[\tau_+^{-1}]^{\oplus7}
\oplus I_-[\tau_-^{-1}]^{\oplus7}.
\]

In words: global frame changes can contain arbitrary polynomial occurrence tails on each sheet, with only that sheet's normal denominators. They are treated here as a discrete additive group, not the complete automorphism infinity-group of an unframed local fibre.

One direct proof of the section formula uses normalization. The positive normalization over V is the complement of V(tau-minus,x1,x2,x3) in Spec(C-plus[x1,x2,x3]); the negative case is symmetric. Those four elements form a regular sequence. Sections of its structure sheaf are the full polynomial ring and its first cohomology is zero. This also follows from the explicit monomial Cech complex used by the checker: a positive tail can glue exactly when it has nonnegative occurrence exponents and no opposite-normal poles.

## 6. Lift the global transports to the entire resolution

Use the central splitting B plus fourteen ideal summands. It is obtained from the actual normalization equations on D(T), not presumed global. A global f is a fourteen-tuple of branch polynomials with zero conductor constant. For each pure branch monomial in f-j, choose its least occurrence divisor X-i and lift it to

\[
\widetilde f_j=\sum_m c_m\frac{m}{X_{i(m)}}[i(m)]_j.
\]

In words: remove a factor already known to divide the monomial and put its label in the corresponding degree-zero ideal-resolution generator. This operation divides no base parameter and admits no new pole. It is additive in f. Each individual resulting map from B into the channel resolution is B-linear.

On the whole free resolution of S(r), act by the identity on all ideal columns, and send its one generic degree-zero column b to b together with b times the tuple of these lifts. All ideal degree-zero columns are cycles in their unaugmented resolutions, so this is a chain map. All positive-resolution-degree columns are fixed. The square of the off-diagonal shear is zero. Consequently these lifts give a strict action of the discrete global frame group, not merely an action specified on its homology.

After tensoring with C, every term except the first occurrence-degree part disappears. Thus

\[
j_1(f)_j=
\sum_{i\in\sigma(j)}
\left.\frac{\partial f_j}{\partial X_i}\right|_{I=0}[i]_j.
\]

In words: the induced action is its first conductor derivative, with all spectator coefficients retained. These are ordinary branch first normal symbols, not derivatives of primes.

For a normalized conductor marking, write its generic coordinate as one and its forty-two degree-zero channel coordinates as v. The action is

\[
(1,v)\longmapsto(1,v+j_1(f)).
\]

In words: only those degree-zero coordinates translate. Every positive-degree Tor coordinate is fixed by the full chosen chain-level action. Since after conductor tensor the operator is determined only by the first derivative, the choice of monomial divisor does not change this induced action.

Its kernel and image are exactly

\[
K_2=I_+^2[\tau_+^{-1}]^{\oplus7}\oplus
I_-^2[\tau_-^{-1}]^{\oplus7},
\qquad
\operatorname{im}j_1=\mathcal C_+^{21}\oplus\mathcal C_-^{21}
\subset C^{42}.
\]

In words: quadratic and higher occurrence tails act identically on the derived conductor fibre; every allowed linear coefficient is realized by the corresponding linear branch polynomial. The kernel acts strictly trivially in this explicit fibre model, which is stronger than vanishing only on its homotopy groups.

## 7. Compute the transported conductor marking infinity-groupoid

Let X14 denote the intrinsic conductor marking space with its generic coefficient normalized to one. In the chosen central word resolution its differential is zero, and

\[
\pi_0(X_{14})=C^{42},\qquad
\pi_n(X_{14})=C^{14b_n}\quad(n\ge1).
\]

In words: it has forty-two independent marking coordinates and the unbounded higher groups computed previously. A simplicial abelian model is given by Dold-Kan [M3]. Fix the globally framed source S(r), and define

\[
\mathcal Y_r=X_{14}//G_{\mathrm{fr}}.
\]

In words: identify conductor markings through the actual global frame automorphisms, while retaining their stabilizers and higher comparisons. This is a specified action groupoid, not a quotient by all automorphisms of the conductor fibre.

By Section 6, the group acts only by translations on the discrete degree-zero factor of the zero-differential complex. Its orbits and stabilizers therefore give

\[
\pi_0(\mathcal Y_r)=
(C/\mathcal C_+)^{21}\oplus(C/\mathcal C_-)^{21}.
\]

In words: conductor markings with an opposite-sheet pole in a linear channel cannot be related by a permitted global frame change.

Choose a representative of a component and a basepoint there. Its action component is the product of the positive-degree conductor marking space with B-K2. Hence

\[
\pi_1(\mathcal Y_r)\cong C^{168}\oplus K_2,
\qquad
\pi_n(\mathcal Y_r)\cong C^{14b_n}\quad(n\ge2).
\]

In words: the first path group includes both the original degree-one conductor paths and the globally nontrivial quadratic frame changes that are invisible on the fibre. Higher groups remain the original unbounded ones; in degrees two and three their ranks are 644 and 2478. The splitting is stated in the chosen labelled model and component, not as an unframed canonical decomposition of a physical moduli problem.

The quotients C/C-sigma and the homotopy-group direct sums here are additive groups, or modules over the unlocalized spectator ring. They are not quotient rings, and are not generally modules over C itself: C-sigma is a subring of C, not an ideal.

This computation uses an actual strict action on a resolution. Triviality on homology alone would not suffice to infer the product or these stabilizers' higher coherence.

## 8. Compute the separate global extension groupoid

Retain identity framings on both the generic quotient and all fourteen labelled kernel channels. The groupoid of such extensions is

\[
\mathfrak X_{\mathrm{ext}}
=\operatorname{Map}_{D(\mathcal O_V)}(\mathcal O_V,\mathcal M[1]).
\]

In words: objects are the full global extensions, paths are their frame-preserving equivalences, and loops are their frame-preserving automorphisms. Here [1] uses cohomological notation. The standard identification of first cohomology and extension classes is [M4].

For either branch there is a normalization sequence on V with kernel I-sigma and conductor quotient the structure sheaf on D(T) inside the occurrence conductor. The preceding normalization computation of sections and first cohomology gives

\[
H^1(V,\widetilde I_\sigma)=C/\mathcal C_\sigma.
\]

In words: conductor Laurent functions modulo those extendable to the whole relevant sheet measure the gluing problem. Therefore

\[
\pi_0(\mathfrak X_{\mathrm{ext}})=
(C/\mathcal C_+)^{7}\oplus(C/\mathcal C_-)^{7},
\qquad
\pi_1(\mathfrak X_{\mathrm{ext}})=G_{\mathrm{fr}},
\qquad
\pi_n(\mathfrak X_{\mathrm{ext}})=0\quad(n\ge2).
\]

In words: this global extension problem is a 1-type. Negative Ext between sheaves is zero, so even an unbounded choice of free resolution supplies no missing higher equivalence that can change its extension component.

An explicit ordinary action groupoid presents it. Its objects are residue vectors in C to the fourteenth power. Its acting group is

\[
\mathcal C_+[X_p:p\in S_+]^{7}\oplus
\mathcal C_-[X_m:m\in S_-]^{7}.
\]

In words: add the conductor values of globally defined branch polynomials to the respective residue coordinates. A branch polynomial f supplies the actual normalization coordinate change z-j to z-j plus f-j times the sheet's generic coordinate. Its stabilizer is precisely G-fr. The group of orbits is the displayed first-cohomology quotient. Every framed extension class has a representative from this residue-vector construction, because the normalization branch first cohomology vanishes. Thus the presentation is not merely a subfamily with matching ranks.

For the actual channel r-sigma-N, the annihilator under multipliers from the original spectator ring is

\[
\operatorname{Ann}_{\mathcal C}[r_{\sigma,N}]
=\left(\prod_{n\in N}t_n\right).
\]

In words: an opposite-sheet pole must actually be removed; own-sheet denominators are already allowed, and the independent long-normal numerator cannot remove a missing t-factor. The original spectator polynomial ring is a domain, so this divisibility statement covers arbitrary polynomial sums, not just squarefree test monomials.

In particular, hold the twelve nonendpoint residues fixed and scale the two endpoint residues by a-plus and a-minus from the original C-script ring. Two such globally framed sources are equivalent exactly when

\[
a_+-a'_+\in(\tau_-),\qquad
 a_--a'_-\in(\tau_+).
\]

In words: the two endpoint parameter classes lie in C-script modulo tau-minus and C-script modulo tau-plus, respectively. The original endpoint multipliers (1,1) are not equivalent to deleting them (0,0).

This is not the endpoint-restoration problem of the earlier sequence from S14 to S12: that problem's obstruction lies in Ext-one(S12,N-end) and has the different annihilator involving the product of the two normal ideals. Here the entire fourteen-channel kernel and the generic quotient are fixed, and we classify their generic extensions. These questions must not be interchanged.

## 9. Why higher conductor paths cannot remove this attachment

On the central chart, subtracting the residue vector times the generic coefficient is a B-linear triangular isomorphism from the actual source to B plus its fourteen ideal summands. It exists for any residue vector because all normal denominators are present there. Accordingly, changing the endpoint entries leaves equivalent intrinsic conductor fibres in every degree and also preserves their derived coefficient operation structure.

This does not give a global isomorphism: the opposite-sheet denominators needed for that triangular change are unavailable on the whole occurrence charts. Section 8 classifies exactly that failure.

Suppose a homotopy-coherent, B-linear equivalence of any free resolutions preserved the actual global kernel and quotient framings while deleting a nonzero endpoint residue class. Passing to degree-zero cohomology would give an isomorphism of the two framed short exact sequences. That would make their nonzero first-cohomology difference zero, contradicting the computed quotient. Thus no higher word length, additional resolution homotopy or infinite comparison ladder repairs the missing framed equivalence within this category.

Nor does Section 7 contradict this. Y-r concerns conductor markings transported by automorphisms of one already fixed global source S(r). Its extra K2 loops do not allow a change of that source's extension component. Different globally inequivalent residue sources may have isomorphic local marking action groupoids.

A prospective native comparison therefore has three distinct compatibility requirements: the conductor operation algebra and its channel modules; the induced first-conductor-derivative action of admitted global transports; and the actual global residue attachment. The first two strengthen a ranks-only comparison but do not replace the third. Changing support, variance or the native source remains a different possible construction; none is ruled out by this fixed-category test.

## 10. Exact verification and limits

Run the standalone standard-library checker:

```sh
python check_marici_conductor_yoneda_and_global_frames_20260907.py \
  --output marici_conductor_yoneda_and_global_frames_certificate_20260907.json
```

The default run has maximum resolution degree six and passes **3,164,764 exact assertions**. It checks first/last differential compatibility, same-sheet exterior relations, actual products of resolution operators, complete dual-basis matrices through degree four, associative normal products, the matrix-dual coalgebra and channel coactions, all labelled dihedral maps in the stated degrees, and both complete endpoint channels. It separately constructs the full and endpoint-forgotten module actions and verifies their intertwining.

For the global calculation it performs 3,456 complete integral monomial-sign-pattern Cech calculations, covering every sign pattern relevant to the section and first-cohomology formulas. It verifies all fourteen actual residue cocycles, all proper overlap equations, their lack of degree-zero fillers in their exact multigrades, and all squarefree patterns of potential annihilating t-factors. General exponents follow from the divisibility and localization proofs, not the finite list.

For global transport it lifts 266 pure branch monomials of total occurrence degrees one through three across all fourteen channels. It checks the exact source shears, their pairwise additive composition and inverses, all tested higher ideal differential columns, the conductor first-derivative formula, its quadratic kernel, and the global first-jet coefficient lattice.

The predecessor `check_marici_intrinsic_conductor_resolution_20260907.py` was independently rerun, passing **280,920** assertions. The replayed certificate has SHA-256:

```text
03e7e2e0c687859039406b5bb553c420dc803061a7f0f396c43e3419d3c6b447
```

The new checker does not need the old checker to run. When the replay certificate is present it records its hash as provenance, rather than claiming to rerun it internally. Every all-degree conclusion above has an algebraic proof; no finite rank table is substituted for that proof. No proof assistant was used, no repository files were modified, and no native geometric endpoint equivalence or integer-prime torsion is claimed.

## Sources and dependencies

[M1] W. Frank Moore, *Cohomology of Fiber Products of Local Rings*, Journal of Algebra 321 (2009), 758-773; arXiv:0704.3631. Explicit fibre-product resolutions and structures on Ext algebras and modules. The integral operator argument for the displayed augmented polynomial ring is supplied in Sections 2-4 rather than inferred solely from the paper's residue-field hypothesis. `https://arxiv.org/abs/0704.3631`

[M2] Stacks Project, *Hom complexes*, tag 0A8H: endomorphism differential, composition, and mapping-complex grading. `https://stacks.math.columbia.edu/tag/0A8H`

[M3] Stacks Project, *Dold-Kan*, tag 019D: conversion of nonnegative chain complexes to simplicial abelian groups. `https://stacks.math.columbia.edu/tag/019D`

[M4] Stacks Project, *First cohomology and extensions*, tag 0B39: Ext-one from the structure sheaf and the associated first-cohomology class. `https://stacks.math.columbia.edu/tag/0B39`

Preceding Branch B artifacts defining the model: `marici_intrinsic_conductor_resolution_20260907.md`, `marici_normalization_endpoint_extension_20260907.md`, `marici_endpoint_complete_reverse_cone_20260907.md`, and `marici_obstruction_complement_descent_20260907.md`. The distinction between target-selected normalization source and independent native physical source remains in force.

The retrieved Branch A normalization-sheet extension calculation independently emphasizes the need to retain source relations and allowed homotopies. Its regulator-specialized 430-state target is not identified here with our independent-normal coefficient model; its ranks are not used as input to this proof.
