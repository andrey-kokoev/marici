# The actual generic-Q incidence excludes the detached norm-parity loop

Date: 2026-09-06  
Repository: `andrey-kokoev/marici`  
Pinned commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result and scope

The canonical target-side restriction to the **two endpoint connecting augmentations and the actual generic-Q quotient** is now computed in the target's unit multidegree. Its normalized coherent source is contractible. Its target has a diagonal integral endpoint value and three discrete Q components. The coherent unit has endpoint values `(1,1)` and a nonzero Q class. The homotopy fibre over a matching prescribed target object is contractible; it is empty over an incompatible component.

This is **not** a correction to the earlier two-component calculation for the detached node/norm detector. That calculation concerned a different restriction. Here the actual norm-to-three-facet differential is retained. The earlier order-two norm-detector loop cannot lift through this differential: a reflection-fixed facet would require an even integer to equal an odd integer.

The result does not construct the full reciprocal normalization-sheet arrow, the physical butterfly's two framed endpoint comparison 2-cells, or their comparison on the retained Tor grades. In particular, the target-side restriction below is not declared equal to the source's still-missing physical `r_{partial,Q}`. Both endpoint **augmentations** are included; both physical endpoint **connector 2-cells** are not thereby supplied.

## 1. Fixed loaded target

There are nine diagonals of the labelled hexagon: six short diagonals and three long diagonals. Write the independent coefficient ring as

\[
R=\mathbb Z[X_a,u_a:a\in\mathcal D].
\]

In words: every diagonal has an independent occurrence variable and an independent normal variable. No occurrence variable or integer is inverted.

The pinned target has a generator `[S,H]` for each noncrossing dissection S and subset H of S. Its degree and coefficient module are

\[
|[S,H]|=3-|S|+|H|,
\qquad
R[u_a^{-1}:a\in S\setminus H]\,[S,H].
\]

In words: normal inverses are permitted only in the individual indicated stalks. The target has 215 such generators.

Its differential is

\[
d[S,H]=
\sum_{a\ \mathrm{addable}}\epsilon(S,a)\frac{X_a}{u_a}[S\cup\{a\},H]
+(-1)^{3-|S|}\sum_{j=1}^{|H|}(-1)^{j-1}[S,H\setminus\{h_j\}],
\]
\[
\epsilon(S,a)=(-1)^{\#\{b\in S:b<a\}}.
\]

In words: radial incidences have the prescribed occurrence-over-normal coefficient; a normal-removal incidence is a localization inclusion with coefficient one. The diagonals and marked normals are ordered lexicographically.

Keep the exact support filtration

\[
F_V\subset F_B\subset F_K,
\qquad
E=F_K/F_V,
\qquad Q=F_K/F_B.
\]

In words: V consists of the two labelled odd/even endpoints, B is the union of the short facets, and K is the entire associahedron. The loaded generator counts are 16, 208, and 215. E has 199 generators; Q has seven.

## 2. The unit homogeneous summand is forced by the incidence degrees

Give every occurrence and every normal its own grading coordinate. Require the differential to have multidegree zero and the chamber T to have multidegree zero. The normal-removal incidences force all choices of H over the same S to have equal multidegree. The radial incidences then force

\[
\deg[S,H]=-\sum_{a\in S}e_{X_a}+\sum_{a\in S}e_{u_a}.
\]

In words: this grading is determined by the fixed differential and the degree of the chamber; it is not selected by discarding unwanted generators.

The unique possible coefficient monomial of total multidegree zero on `[S,H]` is

\[
w_S=\prod_{a\in S}\frac{X_a}{u_a}.
\]

In words: the coefficient exactly compensates the generator's multidegree. It is allowed in that stalk precisely when H is empty. If H contains a, the coefficient would require the forbidden inverse of u-a on a marked-normal generator.

Consequently the degree-zero summand has the chain identification

\[
C_*(K_6;\mathbb Z)\xrightarrow{\ \sim\ }(F_K)_{\mathbf0},
\qquad [S]\longmapsto w_S[S,\varnothing].
\]

In words: the carrier is an actual homogeneous summand of the loaded target, embedded with its real coefficients. This is **not** specialization of every occurrence and normal coefficient to one.

The chain identity follows termwise from

\[
w_S\frac{X_a}{u_a}=w_{S\cup\{a\}}.
\]

In words: weighting before or after a radial incidence gives the same legal target monomial. The same identification respects all three supports and their quotient maps.

The zero-grade counts, in the order `V, B, K, E, B/V, Q`, are `2, 41, 45, 43, 39, 4`. In particular,

\[
E_{\mathbf0}\cong C_*(K_6,V;\mathbb Z),
\qquad
Q_{\mathbf0}\cong C_*(K_6,B;\mathbb Z).
\]

In words: no new endpoint object is introduced. These are homogeneous summands of the fixed source target.

Positive occurrence-degree shifts preserve this underlying cellular census, by the same stalk argument. A non-invariant shifted multidegree must nevertheless be transported through its group orbit; the equivariant conclusions below are made for the invariant zero multidegree, not automatically for an individually chosen first-Rees chart.

## 3. Physical reflection is checked rather than silently identified

The target-promotion checker uses the labelled reflection `v -> 2-v mod 6`; the endpoint-carrier checker uses `v -> 3-v mod 6`. The former fixes each odd/even endpoint, whereas the latter exchanges them. They cannot be silently substituted when comparing the labelled normalization endpoints.

This calculation implements the latter action on the full loaded target:

\[
r(v)=v+2\pmod6,
\qquad s(v)=3-v\pmod6,
\qquad r^3=s^2=1,
\qquad srs=r^{-1}.
\]

In words: use the rotation and reflection of the actual two-endpoint carrier. The top reflection sign is minus one, matching the earlier compensated convention in which the norm is reflection-odd and the normalized corridor readout is invariant.

For a group element g, its sign on a loaded generator is

\[
g[S,H]=\chi(g)\,\operatorname{sgn}(g|_S)\operatorname{sgn}(g|_H)
[gS,gH],
\qquad \chi(r)=1,
\qquad\chi(s)=-1.
\]

In words: permute the occurrence and normal coefficients, propagate the chamber orientation through the ordered face incidence, and retain the marked-normal exterior sign. The checker verifies this action against the full differential and all group multiplication relations on all 215 generators. It preserves the support filtration and the weight-zero summand.

Thus the physical carrier reflection has been extended to this target. This is an action/covariance construction, not a construction of the normalization-sheet comparison itself.

## 4. Integral target homology

Signed-unit chain cancellations on the exact cellular summands give

\[
H_j(E_{\mathbf0})=
\begin{cases}\mathbb Z,&j=1,\\0,&j\ne1,\end{cases}
\qquad
H_j((F_B/F_V)_{\mathbf0})=
\begin{cases}\mathbb Z^3,&j=1,\\0,&j\ne1.\end{cases}
\]

In words: the endpoint quotient has one primitive orientation line; the road-relative subobject has three primitive corridor classes. The calculation is integral and has no torsion. It is not merely a rank computation over a field.

The checker performs complete elementary chain contractions with signed-unit pivots: 21 pivots for E, 18 for B/V, and one for Q. It checks the square-zero identity after every cancellation. All remaining differentials vanish, certifying the full integral homology in these finite complexes.

## 5. A coherent unit in the actual 43-generator endpoint quotient

In the literal lexicographic incidence basis choose the labelled four-edge D03 corridor

\[
z=[x_0,D03]+[x_0,x_4]-[D03,x_3]-[x_1,x_3].
\]

In words: this is the difference of the two source-labelled half-galleries. Each displayed face is understood in lexicographic order and, in the loaded target, carries its weight monomial.

Its full boundary is

\[
dz=v_++v_-.
\]

In words: both literal endpoint coefficients are plus one. The plus sign on both coordinates is the source's vertex-orientation gauge; after ordinary vertex reorientation this is the usual terminal-minus-initial boundary of a path. In E both endpoints are quotiented, so z is a cycle. Its endpoint readout is primitive.

For every group element g the checker solves the actual cellular equation

\[
dh_g=gz-z
\]

with an integral nine-facet chain. In words: transport of the actual corridor is compared using existing facets, not newly introduced homotopy generators.

For every group pair it then computes an integer k such that

\[
gh_h-h_{gh}+h_g=k_{g,h}\,dT.
\]

In words: the comparison between two transport paths uses the existing chamber. The expression `g h_h` denotes the group action on the facet chain indexed by h.

All group triples satisfy

\[
\chi(g)k_{h,\ell}-k_{gh,\ell}+k_{g,h\ell}-k_{g,h}=0.
\]

In words: the existing chamber comparisons satisfy the full next coherence equation. This is checked on all 216 triples and also follows from injectivity of the chamber boundary.

The certificate contains every facet chain h and every integer k. The facet order is the literal lexicographic order of the nine diagonals, so these witnesses are directly reproducible. The endpoint augmentations and the actual E-to-Q quotient map are checked as equivariant chain maps.

## 6. What the actual Q differential retains

Let the long facets, with their actual coefficient weights, be

\[
f_i=\frac{X_{D_i}}{u_{D_i}}[D_i,\varnothing],
\qquad (D_0,D_1,D_2)=(D03,D14,D25).
\]

In words: these are the three allowed facet generators at total degree zero. The three marked-normal generators of the full seven-generator Q do not occur in this homogeneous summand, because their required weight monomials are illegal in their stalks.

The actual zero-grade generic quotient is

\[
(Q_{\mathbf0})_3=\mathbb ZT,
\qquad
(Q_{\mathbf0})_2=P=\mathbb Z f_0\oplus\mathbb Z f_1\oplus\mathbb Z f_2,
\qquad dT=f_0+f_1+f_2.
\]

In words: the chamber is attached to all three facets. It is not an independent closed norm detector.

Put

\[
N=f_0+f_1+f_2,
\qquad M=P/\mathbb ZN.
\]

In words: the norm relation is primitive, so M is a free integral lattice of rank two. There is no Q homology in degree three; its degree-two homology is M.

In the basis given by the classes of f-zero and f-one, with f-two equal to their negative sum, the literal action is

\[
R_M=\begin{pmatrix}-1&1\\-1&0\end{pmatrix},
\qquad
S_M=\begin{pmatrix}-1&1\\0&1\end{pmatrix}.
\]

In words: these matrices are computed from the actual long-facet permutation, its reflection sign, and the integral norm quotient.

## 7. Complete group-cohomology calculation, without averaging

Since the determinant of rotation minus identity is three, the invariant subgroup is zero:

\[
\det(R_M-I)=3,
\qquad H^0(D_3,M)=0.
\]

In words: there is no nonzero invariant vector even rationally, and hence none in this torsion-free lattice.

A group one-cocycle is determined by its values on r and s. Evaluating the relations `r^3`, `s^2`, and `srsr` gives exactly

\[
c(r)=(A,B),
\qquad c(s)=(A,0),
\qquad A,B\in\mathbb Z.
\]

In words: the cocycle lattice has two free integral coordinates. Conversely every such pair satisfies all the relators and defines a cocycle; there are no additional constraints hidden by a finite sample.

A coboundary coming from the vector `(x,y)` has cocycle coordinates

\[
(A,B)=(-2x+y,-x-y).
\]

In words: its coordinate sum is divisible by three. Conversely, if that sum is divisible by three, the integral choices

\[
x=-\frac{A+B}{3},
\qquad y=-B-x
\]

produce the required coboundary. In words: this classifies every integral replacement, not merely one chosen representative.

Therefore

\[
H^1(D_3,M)\cong\mathbb Z/3,
\qquad [c]\longmapsto A+B\pmod3.
\]

In words: the actual generic quotient has precisely the order-three coherent component, and no invariant loop direction.

## 8. The actual unit has a nonzero Q component

Project the constructed h-chains to the three long facets. At the two group generators they are

\[
a_r=(-1,-1,0),
\qquad a_s=(-1,0,0).
\]

In words: these are the literal long-facet coordinates of the actual corridor's transport comparisons. Reducing modulo the norm yields the cocycle values `c(r)=(-1,-1)` and `c(s)=(-1,0)`.

Its class is

\[
(-1)+(-1)=1\pmod3.
\]

In words: the normalized unit lies in a nonzero Q component. The norm two-cochain obtained by projecting k gives the same residue. These statements come from the constructed target chains, not from identifying the earlier coefficient norm with the chamber by name.

Changing the integral h-solutions changes the data by the appropriate Q homotopy. Changing the unit cycle by a boundary changes the projected cocycle by a coboundary. Thus the computed component is independent of those solving choices. Changing orientation or the generator convention can interchange the two nonzero classes, but cannot make this class zero or produce an order-two loop.

## 9. The actual augmentation/Q relative fibre

Reindex the target marking complex by

\[
K^E_0=\ker(d:E_{\mathbf0,1}\to E_{\mathbf0,0}),
\qquad K^E_1=E_{\mathbf0,2},
\qquad K^E_2=E_{\mathbf0,3}.
\]

In words: actual cycles are marking objects, facets are paths, and the chamber provides comparisons between paths.

Let `delta` be the full boundary at the two endpoints and let `pi` be the canonical quotient to Q. Reindex Q into degrees one and two as L. These define an actual equivariant chain map

\[
\rho_{\mathrm{aug},Q}^{(0)}:K^E\longrightarrow
\mathbb Z\{v_+,v_-\}[0]\oplus L,
\qquad L_2=\mathbb ZT,
\qquad L_1=P,
\qquad d_L(T)=N.
\]

In words: degree-zero markings retain both endpoint connecting values; their higher comparisons retain the actual generic quotient. This map is explicitly narrower than the physical sheet-butterfly restriction.

Let X-E be the Dold-Kan space of endpoint-normalized markings in K-E. Since the integral endpoint readout is an equivariant quasi-isomorphism to the trivial integral line, its normalized homotopy-fixed space is contractible. Since L is equivariantly quasi-isomorphic to M in degree one,

\[
\pi_0((\operatorname{DK}L)^{hD_3})\cong\mathbb Z/3,
\qquad
\pi_n((\operatorname{DK}L)^{hD_3})=0\quad(n\ge1).
\]

In words: the actual Q target has three contractible components, rather than components with an order-two loop group.

The two endpoint coordinates are exchanged by reflection and are discrete. The complete target of the displayed restriction therefore has component group

\[
\mathbb Z\oplus\mathbb Z/3,
\qquad n\longmapsto(n,\overline n).
\]

In words: the first coordinate records the common endpoint value; the second records the Q component. The unit maps to common endpoint value one and residue one.

For a prescribed actual target object b, with the compatibility path retained, the normalized homotopy fibre is

\[
\operatorname{hofib}_b\bigl((X_E)^{hD_3}\to Y\bigr)
\simeq
\begin{cases}
*,&[b]=(1,\overline1),\\
\varnothing,&[b]\ne(1,\overline1).
\end{cases}
\]

In words: a matching prescribed object gives one contractible relative class; any incompatible component gives no lift. This follows from the actual source's contractibility and the target components' contractibility, not from replacing a homotopy fibre by a strict kernel.

## 10. Why the old parity loop cannot lift

There is a chain projection from L to the detached norm complex in degree two. The old order-two detector loop is represented by a sign-module one-cocycle eta whose reflection value is odd. A lift to a loop of the actual Q target would require a facet zero-cochain v with, up to the harmless totalization sign,

\[
(s-1)v=\eta(s)N.
\]

In words: its facet component must supply the boundary of the norm-loop component. Reflection fixes the D03 facet label and acts on its coefficient by minus one. Taking that coefficient gives

\[
-2v_0=\eta(s).
\]

In words: the left side is even and the right side is odd. No integral solution exists. Replacing eta by a cohomologous representative changes its reflection value by an even integer, so the obstruction persists for every representative of the nonzero parity class.

Thus the old order-two loop is **not an admissible Q-compatible comparison in this homogeneous target sector**. This is exclusion by the retained incidence, not choosing a parity by hand and not a claim that two distinct physical states were merged.

The node portion of the earlier detector is not identified with a normalization-sheet map by this argument. Only the norm-loop mechanism responsible for its order-two relative ambiguity has been tested against the actual Q attachment.

## 11. Relation to the preceding support obstruction

The previous all-polynomial calculation showed that the top boundary cannot be filled with zero top coefficient in the prescribed stalks unless the product of the long normals divides the coefficient. That result remains intact.

Here `dT=N` is retained, not cancelled. At unit multidegree its principal-part boundary is precisely the primitive norm relation among the three legal facet weights. The new coherent restriction uses this nonzero attachment. It does not construct a forbidden zero-top filler, invert an occurrence variable, or identify a chamber homotopy with a strict closed top state.

Likewise, considering this homogeneous sector does not justify discarding the marked-normal states of the full complex. Those states remain in other multidegrees and are essential candidates for the retained Tor-grade comparison. The full physical first-Rees/Cartier problem must establish its grading and support transport before inheriting this result.

## 12. Remaining physical comparison

The next required map is still the support-typed reciprocal normalization-sheet comparison into the fixed supported-dual target, with its two framed endpoint connector 2-cells. This calculation provides an actual target-side restriction and explicit coherent boundary data against which such a construction can be tested.

The physical comparison must establish how its source degrees and orientations map to the homogeneous sector computed here, transport the required Tor grades, and identify its prescribed based-Q roof with the relevant target mapping object. A scalar endpoint match or matching abstract cohomology groups would not establish those identifications.

No value of the full physical reflection parity is asserted. Any order-two ambiguity in that fuller problem must involve structure not present in the graded augmentation/Q restriction computed above; it cannot be inferred from the detached generic norm loop alone.

## Reproduction and evidence

Run with Python 3.10 or later:

```sh
python check_actual_q_graded_restriction.py --output actual_q_graded_restriction_certificate.json
```

The checker is self-contained and standard-library-only. The completed run passes **21,144 exact assertions**. It reconstructs all 215 generators; checks fine grading, legal denominators, differential squares, and the physical action; identifies the unit homogeneous sector; performs integral chain contractions; constructs the actual coherent unit and all its pair/triple witnesses; derives the rank-two cocycle equations; and verifies the parity-loop obstruction. The all-degree grading argument and complete homotopy-fibre claims are proved above. This is not proof-assistant certification.

No repository files were modified.

Pinned source records:

- `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`: loaded differential, stalks, filtration, and original target action.
- `research/voevodsky/check_two_endpoint_tate_carrier.rs`, blob `0147e2e42dafac0da7289c571cb0331b51338be1`: physical labelled reflection and the two marked half-galleries.
- `src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md`, blob `02cedbb15dd385a75bab759dfcdb4daa28bd3b3c`: fixed endpoint/Q object and the distinction between endpoint readouts and the physical mixed-variance butterfly.
- `research/voevodsky/check_dp6_endpoint_q_mapping_fiber.rs`, blob `592811b138855554c921dcf4269581632e8f0050`: explicitly conditional physical parity calculation.

General mathematical conventions: Stacks Project, *Graded rings*, tag `00JL` (graded exactness), and *Dold-Kan*, tag `019D` (chain complexes and simplicial abelian objects). The new specific cohomology and restriction conclusions are derived in this note, not attributed to those general references.
