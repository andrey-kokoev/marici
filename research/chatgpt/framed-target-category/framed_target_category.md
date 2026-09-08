# Source-filtered, boundary-framed target category for Marici

Date: 2026-09-06. Repository inputs are pinned to `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

## Status

This is a target-category specification, a calculation of its relative mapping complex, and two exact algebraic controls. It does not assert that the complete physical correspondence has been constructed, that a prescribed boundary frame extends, or that the generic chain has become a nonzero homology class.

The correct invariant can be a comparison between independently supplied trivializations. It cannot be obtained by declaring a known boundary nonzero or by deleting a homotopy after seeing its effect.

## 1. Ambient coefficient category

Fix the actual source ringed incidence diagram, denoted by J with coefficient-ring diagram R. Its objects retain the support stratum, branch, occurrence labels, normal labels, and source-versus-target variance. For ordinary restriction/localization legs, a module diagram consists of an R(j)-module at each j and semilinear structure maps for the specified ring maps. The category of these diagrams is abelian, with kernels and cokernels computed objectwise.

Write

\[
\mathcal A=\operatorname{Mod}(J,\mathcal R),\qquad
\mathscr C_0=D_\infty(\mathcal A),\qquad
\mathscr C_\Lambda=\operatorname{Fun}(\Lambda,\mathscr C_0).
\]

In words: first take derived coefficient diagrams without erasing the incidence index, then retain the full filtration diagram indexed by Lambda.

For the present finite support problem, Lambda contains the three source support stages. Independent Cartier and Rees filtrations supply additional, separately labelled indices. A convenient presentation uses the product of the finite support index with one decreasing-filtration index for each independent normal filtration. This notation does not identify occurrence, monodromy, Rees, or physical channel coordinates.

Equivalences in this model are equivalences at every retained filtration stage. For finite exhaustive filtrations this agrees with requiring quasi-isomorphisms on all associated grades; for infinite filtrations we retain the levels explicitly and do not infer equivalence from associated grades without the needed separatedness/completeness hypotheses. This avoids killing a filtered diagram merely because its final total complex is acyclic. [M1]

A mixed-variance geometric operation needs its actual derived bimodule or correspondence realization before becoming a structure map in J. Placing two unrelated complexes in D(Z) does not construct that realization. The specification applies to the existing coefficient diagrams, and describes the interface required of additional physical diagrams.

If a source symmetry group permutes supports or rings, its action is semilinear. Encode the full action on the diagram, for example using the action category J semidirect G when the action is strict. Do not replace this by separately taking invariants on each homology group. With coherent rather than strict action, use its homotopy-coherent diagram. No averaging over the group order is part of the construction.

## 2. The support flag that must remain visible

The source's endpoint and short-boundary supports give

\[
F_V\longrightarrow F_B\longrightarrow F_K.
\]

In words: retain the endpoint complex, short-boundary complex, and full complex, together with their actual maps. The source names V as the two endpoints and B as the short boundary. [S1]

Their derived quotients are

\[
P=\operatorname{cofib}(F_V\to F_B),\qquad
E=\operatorname{cofib}(F_V\to F_K),\qquad
Q=\operatorname{cofib}(F_B\to F_K).
\]

In words: P is road-relative, E is endpoint-relative, and Q is the support quotient. Q is not automatically the open fibre where a Rees parameter is invertible.

Retain the resulting triangle

\[
P\longrightarrow E\longrightarrow Q\xrightarrow{\partial}P[1].
\]

In words: the connecting arrow is part of the target data, not a scalar inferred from the homology groups.

The original endpoint terms must remain elsewhere in this diagram even when E is formed. Otherwise an endpoint-relative quotient has already forgotten information later requested as a frame. Neither the diagram nor its normal blocks may be replaced by their ranks or final primitive lines.

The coefficient rings at individual target Cech terms retain only the inverses allowed by their source support. A map or homotopy requiring an inverse unavailable at its target is not a morphism in the specified module diagram. The same restriction applies in every homotopy degree, not only to degree-zero chain maps.

## 3. What is fixed by a frame

Let K be a simplicial indexing shape for the complete comparison diagram: source and target support flags, normal specializations, localizations, quotient triangles, and the required comparison squares. Let K-boundary be its specified subdiagram. A simplicial subdiagram can retain an already constructed comparison homotopy without filling an as-yet-unconstructed square.

The frame records the source-derived endpoint objects and their existing restriction maps; the complete prescribed Q object and any independently defined marking/readout; the principal/conormal lines with their source frames and connecting degrees; and any already constructed endpoint connector homotopies and their boundary values. Group-action and coefficient-localization data remain attached to all these objects.

A frame does **not** fix an unknown Gysin map, insert a desired Q image, stipulate a nullhomotopy of an obstruction, or impose the desired parity. Those are extension data or tests. If a connector has only been matched numerically, it is not yet a supplied simplex of the frame.

Let

\[
\mathscr C=\operatorname{Fun}_{\mathrm{ex}}(K,\mathscr C_\Lambda),\qquad
\mathscr B=\operatorname{Fun}(K_\partial,\mathscr C_\Lambda),\qquad
b:\mathscr C\longrightarrow\mathscr B.
\]

In words: C contains coherent comparison diagrams satisfying the specified cofiber-square conditions; B contains their boundary diagrams; b is restriction. The subscript only enforces the cofiber or fiber squares explicitly designated in K. It does not impose missing physical equalities. Functor infinity-categories retain transformations and transformations between them. [M2]

For an independently supplied boundary diagram F, define

\[
\mathscr T_{\mathbb F}
=\mathscr C\times^h_{\mathscr B}\{\mathbb F\},\qquad
\mathfrak M_{\mathbb F}=(\mathscr T_{\mathbb F})^\simeq.
\]

In words: the target category consists of whole diagrams together with a specified equivalence of their boundary with F. Its core is the infinity-groupoid of those framed diagrams and their equivalences.

An object is a pair (A,alpha), with alpha identifying b(A) and F. A morphism to (A',alpha') consists of a map f:A to A' and a specified homotopy

\[
\alpha'\circ b(f)\simeq\alpha.
\]

In words: the boundary identification is preserved coherently. Higher morphisms preserve this comparison and its higher relations. Taking literal equalities instead would be a stronger, model-dependent rigidification.

This category can be empty. For a nonzero frame it is generally not stable and has no canonical zero object. Its linear relative deformation complexes are constructed in the stable ambient categories, not by assigning a zero object to the framed fibre.

## 4. Mapping spaces and the exact admissibility test

A physical source and target may have different boundary diagrams. Fix objects A,E and an independently supplied boundary comparison theta. The corresponding space of lifts is

\[
\mathfrak L_\theta(A,E)
=\operatorname{hofib}_{\theta}
\left(
\operatorname{Map}_{\mathscr C}(A,E)
\longrightarrow
\operatorname{Map}_{\mathscr B}(bA,bE)
\right).
\]

In words: an object is a full comparison together with a homotopy identifying its boundary with theta. This is a homotopy fibre, not an ordinary kernel.

For a fixed diagram model with its derived mapping complexes, set

\[
M=\operatorname{RHom}_{\mathscr C}(A,E),\qquad
N=\operatorname{RHom}_{\mathscr B}(bA,bE),\qquad
F=\operatorname{Cone}(r:M\to N)[-1].
\]

In words: F computes differences of framed comparisons. Use derived mapping complexes of the diagrams, including their coherent comparison components, rather than just a product of stalkwise Hom groups.

A concrete cochain model is

\[
F^n=M^n\oplus N^{n-1},\qquad
D(f,h)=(d_Mf,\,r(f)-d_Nh).
\]

In words: a degree-zero element contains both a full map and its boundary-comparison homotopy. The cochain identity follows because r is a cochain map. These signs are the cohomological mapping-cone convention. [M3,M4]

For nonzero theta, objects satisfy

\[
d_Mf=0,\qquad r(f)-\theta=d_Nh.
\]

In words: their boundary agrees with the prescribed one up to the supplied homotopy. Subtracting two such solutions gives a cocycle in F. Once a reference solution is chosen, connected components form a torsor for H-zero of F; the positive homotopy groups at that solution are

\[
\pi_n(\mathfrak L_\theta,f_0)\cong H^{-n}(F),\qquad n\ge1.
\]

In words: negative cohomological degrees give higher comparisons. A torsor need not have a preferred zero. In particular, a zero ambient map need not satisfy the nonzero boundary condition and must not be used as an artificial reference lift.

### Secondary test for an ambient nullhomotopy

Suppose (f,h) is a zero-boundary cocycle in F and f=d_Ms for a filtered, diagram-compatible s in M-minus-one. Then

\[
(f,h)-D(s,0)=(0,h-r(s)),\qquad d_N(h-r(s))=0.
\]

In words: the ordinary nullhomotopy removes f but may leave a boundary-comparison class.

Changing s by a closed degree-minus-one map changes that residual class by the image of H-minus-one of M. Consequently

\[
[(f,h)]=0\quad\Longleftrightarrow\quad [h-r(s)]=0,
\qquad
[h-r(s)]\in\operatorname{coker}
\bigl(H^{-1}(M)\to H^{-1}(N)\bigr).
\]

In words: nullhomotopy in the framed problem requires the boundary residue of the contraction to be removable by an allowed higher comparison. Failure of one particular strict equality r(s)=0 is not enough to prove survival.

This criterion follows directly from the displayed cone differential and its long exact cohomology sequence. If s exists only after forgetting the filtration, first test whether it lifts to M. That is an additional lifting problem; the formula must not silently treat an unfiltered primitive as filtered.

## 5. An exact test of the minimal proposed filtration

Use the source's mixed complex, in homological degrees two, one, one, zero:

\[
dH=q-x\xi,\qquad dq=xb,\qquad d\xi=b,\qquad db=0.
\]

In words: the generic chain and special chain are related before quotienting. The ordinary contraction is already recorded in source entry 162. [S2]

Set

\[
s(q)=H,\qquad s(b)=\xi,\qquad s(H)=s(\xi)=0.
\]

In words: each unit boundary pair is contracted. Direct calculation gives

\[
ds+sd=1,\qquad s^2=0.
\]

In words: all four generators are contracted integrally.

This contraction is R-linear, so it preserves the uniform x-adic coefficient filtration. It also preserves the road subcomplex spanned by xi and b. Therefore a category retaining only this two-stage road filtration plus uniform coefficient filtration does not remove the contraction.

The quotient by that road subcomplex is

\[
Q=[RH\xrightarrow{1}Rq].
\]

In words: q remains a boundary in Q. No additional endpoint label changes this identity inside the same quotient complex.

A finer endpoint subcomplex Rb is not preserved by s, since s(b)=xi. That proves a failure of this particular contraction to preserve that finer support. It does not prove a nonzero physical comparison class. It is necessary to compute the complete relative mapping fibre and to justify that support filtration geometrically.

There is an additional control: with the three-level diagram Rb contained in the road complex contained in the full mixed complex, the latter two stages are acyclic. As a derived diagram it is equivalent to Rb mapping to zero mapping to zero. Fixing its Rb stage leaves no deformation supplied by these two acyclic stages. Thus even a visible failure of a particular strict contraction need not yield a new Q-invariant.

## 6. The class that can replace an ordinary Q-class

Source entry 109 already formulates a suitable secondary comparison. Suppose the following maps and cochains have been constructed in one correctly graded, source-filtered mapping category:

\[
q_J:J_0\to Q,\qquad e_F:Q\to F_0[2],\qquad
\partial h_{\mathrm M}=q_J,\qquad
\partial H_{\mathrm C}=e_Fq_J.
\]

In words: the Morse construction trivializes q-J, while the conductor construction trivializes its composite with the degree-two extension. Here h-M has cochain degree minus one and H-C degree plus one. [S3]

Their difference is

\[
\Delta_J=H_{\mathrm C}-e_Fh_{\mathrm M},\qquad
\partial\Delta_J=0,\qquad
[\Delta_J]\in H^1\operatorname{RHom}(J_0,F_0).
\]

In words: the invariant compares the two trivializations. It does not assert that the exact chain q-J has acquired ordinary homology. Endpoint and normal framings determine which changes of the two trivializations are allowed; the relative mapping complex computes their actual indeterminacy.

If only homotopy classes of the two trivializations are supplied, retain their allowed differences rather than claiming a unique Delta. If one construction is still absent, Delta is a specified research target, not an already defined physical class.

No Verdier quotient of the ordinary stable category can change an already zero morphism into a nonzero one: an exact functor sends zero morphisms to zero morphisms. The extra filtration and comparison data must be retained before the forgetful functor. A later quotient cannot recover them. This is why the phrase “framed Yoneda quotient” should not be used as a replacement for the explicit fibre construction above.

## 7. Nonlinear geometric information

The target above is the coefficient category. Its core need not reproduce the homotopy type of the source geometric carrier.

To incorporate the nonlinear investigation, retain pairs (Y,E), where Y is the actual source stratified/ringed geometric diagram and E is its coefficient packet. A permitted transport must give the admitted geometric transport of Y, its compatible coefficient map, and the boundary-frame comparison. Equivalence of coefficient complexes alone is not sufficient for equivalence of pairs.

For a varying source geometry, these coefficient categories may be organized by the Grothendieck construction once the needed coherent transport functors are supplied. Calling this construction a physical six-functor theory does not supply those functors. The existing deck/stratum audit is a concrete warning: a coefficient retraction can pass while its geometric equivariant lift fails. [S4]

This keeps the geometric homotopy question separate from, but comparable with, the framed coefficient question. Arithmetic coefficient changes and Bocksteins act in the coefficient fibre and must preserve the frame through their derived functoriality.

## 8. Required next input and decision test

The immediate object to serialize is the actual boundary diagram: both endpoints, the complete Q quotient, normal ideal lines and their source evaluations, and all independently constructed connector homotopies. Give every component its degree, support, coefficient ring, and source formula. Unknown comparison cells remain unknown.

For the candidate map, compute its restriction in that diagram, the induced restriction r on mapping complexes, and the image of each known ambient nullhomotopy. A nonzero class in the cone fibre would establish a framed comparison invariant. A zero class would reject that candidate under those actual boundary conditions. Neither outcome is stipulated by this definition.

Defined here: the coefficient target category, its core, its mapping-space fibre, and the exact secondary-nullhomotopy criterion. Not established here: the complete physical spatial realization of the diagram, a nonempty physical comparison fibre, or a nonzero physical Delta-J.

## Verification

Run:

```sh
python check_framed_target_category.py --output framed_target_category_certificate.json
```

The standalone standard-library checker passed 5,614 assertions. It checks the mixed contraction, its uniform-filtration and road-subcomplex compatibility, its failure on the endpoint subcomplex, the quotient unit pair, and the exact mapping-fibre control below.

For the control, take M to be the two-term identity complex in degrees minus one and zero, N to be Z in degree minus one, and r-minus-one to be multiplication by an arbitrary integer m. The relative complex has differential s mapping to (s,ms). Its integral H-zero is Z, with coordinate h-ma. Thus the ambient map is always exact, while its framed comparison can be nonzero. This is an algebraic control of the criterion, not a physical Marici calculation.

The source formulas are R-linear and the mapping-fibre reduction is unimodular; their unbounded coefficient statements follow from those identities, not extrapolation of finite tests. No proof-assistant verification or repository write is claimed.

## References and provenance

[M1] Stacks Project, filtered derived categories, tags `05RX`, `03T9`, and `0287`:
`https://stacks.math.columbia.edu/tag/05RX`
`https://stacks.math.columbia.edu/tag/03T9`
`https://stacks.math.columbia.edu/tag/0287`

[M2] Kerodon, functor infinity-categories, tag `005Z`:
`https://kerodon.net/tag/005Z`

[M3] Stacks Project, Hom complexes, tag `0A8H`:
`https://stacks.math.columbia.edu/tag/0A8H`

[M4] Stacks Project, mapping cones, tag `014D`:
`https://stacks.math.columbia.edu/tag/014D`

[S1] `src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md`, read through GitHub at the pinned commit.

[S2] `src/ledger/20260815-162 Cartier-Filtered Primal Bridge and the Absolute Contraction No-Go.md`, read through GitHub at the pinned commit.

[S3] `src/ledger/20260814-109 Closed Dual-Star No-Go and the Seven-Triangle Secondary Cobordism.md`, read through GitHub at the pinned commit.

[S4] Uploaded `deck_sphere_retraction_falsification.md`, dated 2026-09-05; retrieved from File Library. Its scope is the specified deck- and stratum-preserving lift test, not every possible nonlinear comparison.

The earlier conversational attribution of every result to Branch B versus Branch C is not used as mathematical evidence. The formulas above are grounded in the named source records and explicit controls.
