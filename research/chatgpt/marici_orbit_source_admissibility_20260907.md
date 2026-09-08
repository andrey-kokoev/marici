# Testing the three-pair operation against source locality

Date: 2026-09-07  
Lane: Branch B — the fixed target, supported coefficients, and lifting spaces  
Repository inputs: `andrey-kokoev/marici`, pinned commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result and scope

The previously constructed three-pair tensor is a valid supported operation. Its strict section of the specialized seven-state PC quotient remains valid. It is **not** the closed-support descent of the three local pair operations: the tensor restricts to the common intersection, whereas closed-support descent retains their union and overlap data.

This note constructs and computes that union coefficient object, its finite derived dual, and a counit cone retaining any supplied generic data. The union has a 28-generator free resolution, with ranks `(1,8,12,6,1)`, and its derived dual has nonzero cohomology in degrees two, three, and four. The triple-intersection dual instead has its sole coefficient cohomology in degree six.

More decisively, the union-dualized PC projection has **no derived section**. On an explicit open set it reduces to the one-pair lifting problem, where the exact residual image ideal is `(t13*t15,I_minus)`, a proper ideal. The intersection-dualized projection does have the section computed previously. These are different lifting spaces over different coefficient objects.

This is not a theorem that the native physical source must be this union object. It is an exact test of the previously unresolved tensor-versus-descent alternative. In particular, an operation being available for each of three rotated local comparison resolutions does not identify their tensor product with their physical assembly.

A separate generic-support check is also exact: the triple tensor is contractible where all six short Rees parameters are invertible. A source required to be nonzero on that same open cannot be replaced by it. The support-filtration quotient called Q is not, by that name alone, a localization at those parameters; an independent deformation time is not identified with any short parameter here.

No native-to-target geometric correspondence or new endpoint connector is asserted. The supplied native gamma comparison is used only through its proved specialization/quotient; no claim is made to have reconstructed a newer full native source matrix.

## 1. Coefficients, labels, and the operation under test

Set

\[
(s_1,t_1)=(t_{04},t_{35}),\qquad
(s_2,t_2)=(t_{02},t_{15}),\qquad
(s_3,t_3)=(t_{24},t_{13}).
\]

In words: these are exactly the three ordered pairs in the previous composite. Here the second symbol of a pair is denoted t-i; every actual geometric label remains explicit in the dictionary.

Work over

\[
\mathcal B=\mathcal A[s_1,t_1,s_2,t_2,s_3,t_3],
\]

where

\[
\mathcal A=
\mathbb Z[X_l,u_l\ (l\in\{03,14,25\}),X_p\ (p\in S_+),X_m\ (m\in S_-)]
/(X_pX_m:p\in S_+,m\in S_-).
\]

In words: retain the alternating occurrence ring and all independent long parameters. The six short Rees parameters are independent polynomial variables over it. Opposite-sheet occurrence products vanish, but none of these six Rees parameters is a zero divisor. Short normals remain `u_s=t_s X_s`.

Write

\[
J_i=(s_i,t_i),\quad J_\cap=J_1+J_2+J_3,
\quad \mathcal B_6=\mathcal B/J_\cap.
\]

In words: J-cap defines the common intersection of the three pair supports.

The supplied pair resolution P-i has homological degrees zero, one, two and ranks three, four, one. Its differential matrices, in the supplied endpoint frame, are

\[
M_i=\begin{pmatrix}0&-t_i&s_i&0\\1&0&-1&0\\0&1&0&-1\end{pmatrix},
\qquad w_i=(t_i,s_i,t_i,s_i)^T.
\]

In words: these are the actual conductor comparison columns, not just their Koszul homology. The supplied ordered reduction identifies this complex with `K(s_i,t_i)` tensored with its endpoint line. The dual has cochain differentials `-M_i^T,w_i^T` and positive supported generator `-z_i^vee` [S1].

Consequently

\[
\mathcal D_\cap=P_1^\vee\otimes P_2^\vee\otimes P_3^\vee
\simeq \mathcal B_6[-6]\otimes\mathscr L_\cap.
\]

In words: the previous operation is supported on the common intersection and retains degree six, three endpoint-dual lines and the six-normal determinant dual. This is the regular-sequence tensor calculation [M1, M2]. The line is not identified with the channel orientation or an independent long-normal line.

Throughout, a cohomological shift `[-r]` places a degree-zero module in cohomological degree r. The loaded target has homological degrees zero through three. Thus the top generic cycle tensored with the triple dual occupies homological degree minus three. Removing the six-degree placement for a comparison would require an actual additional operation.

## 2. An exact localized contraction, and its proper interpretation

Order the pair-dual bases as

\[
(r_0^\vee,r_c^\vee,r_d^\vee),\quad
(e_0^\vee,e_1^\vee,e_2^\vee,e_3^\vee),\quad z^\vee.
\]

In words: these are the three degree-zero, four degree-one, and one degree-two columns of the supplied dual complex.

On the open set where s is a unit, an explicit degree-minus-one contraction is

\[
h^1=\begin{pmatrix}-s^{-1}&0&-s^{-1}&0\\-1&0&0&0\\0&0&0&1\end{pmatrix},
\qquad h^2=(0,s^{-1},0,0)^T.
\]

In words: the formula uses a permitted inverse only on this localized test open. It does not insert an inverse into the unlocalized source or the supported residue.

Direct multiplication gives

\[
\delta h+h\delta=1,\qquad h^2=0.
\]

In words: every pair-dual class becomes zero there. Tensoring the contraction with the other two pair factors gives a contraction of the entire 512-column triple complex. For a further complex N, the tensor signs cancel the mixed terms, so the same identity holds on `D_cap tensor N`. This proof applies to the full target, a native source, the endpoint subcomplexes, and every existing map between them.

The three choices of localized factor contraction have explicit comparisons. If H-i and H-j denote their totalized versions,

\[
\delta(H_iH_j)-(H_iH_j)\delta=H_j-H_i.
\]

In words: the localized nullhomotopies are coherently comparable without averaging.

Putting `T=s_1t_1s_2t_2s_3t_3`,

\[
(\mathcal D_\cap\otimes N)\otimes_{\mathcal B}\mathcal B[T^{-1}]\simeq0.
\]

In words: the composite has no generic fibre on this specific open. Thus it cannot replace a kernel whose prescribed map to Q is nonzero there. Entry 108 explicitly requires generic support of the particular source, not merely of the ambient deformation [S2].

**Scope of the generic test.** Q is also used in this project to name the quotient of a support filtration. Its seven-state complex can be nonzero after all six short Rees parameters are zero. That is consistent with the displayed localized vanishing. If the physical generic leg uses a separate deformation parameter, the vanishing above does not prove that leg vanishes. Such an identification of parameters would need to be supplied independently.

The actual triple counit also does not turn the special section into an unshifted ordinary lift. It selects the product of the three `r0^vee` columns and is zero on the top-dual column. Therefore it sends the previously constructed cycle `(-z1^vee) tensor (-z2^vee) tensor (-z3^vee) tensor theta` to zero. This is compatible with its degree. The primitive supported purity value and the adjunction counit are different arrows of the duality roof.

## 3. Ordinary native gamma cannot provide the missing six-normal inclusion

The supplied native comparison contains the nonzero class gamma and first primitives

\[
\gamma=X_{04}p_{04},\qquad
U_s=-r_{04},\qquad U_t=-t r_0+r_{35},
\]

\[
dU_s=s\gamma,\qquad dU_t=t\gamma,
\qquad g_*=sU_t-tU_s=-st r_0+t r_{04}+s r_{35}.
\]

In words: the first two normal nullhomotopies exist, but their compatibility is the exceptional class g-star, not an automatically supplied second nullhomotopy [S1].

Use the genuine specialization and chain quotient already established in that source:

\[
B'=\mathbb Z[x,y,s,t]/(xy),\qquad
T_2=(B')^3\xrightarrow{\begin{pmatrix}-x&-sx&0\\-y&0&-ty\end{pmatrix}}T_1=(B')^2.
\]

In words: the quotient retains the gamma detector and has no degree-three target. The detector taking the x-coefficient of the first component minus the y-coefficient of the second annihilates boundaries and gives one on gamma. Thus gamma is not a boundary.

Any ordinary chain map from the pair Koszul resolution, shifted so its quotient generator reaches gamma, requires primitives A and B with

\[
dA=s\gamma,\qquad dB=t\gamma,\qquad sB-tA=0.
\]

In words: the last equation is the missing top coherence. Regularity of s,t in B' gives A=sV and B=tV. The first equation, followed by cancellation of the regular element s in the free target module, would imply `dV=gamma`, contradicting the detector. The argument applies to any homologous representative [S1].

There is a canonical inclusion of differential graded algebras

\[
K(s_1,t_1)\longrightarrow K(s_1,t_1,s_2,t_2,s_3,t_3).
\]

In words: include the first two exterior generators and keep the degree-zero unit. A proposed six-normal ordinary inclusion realizing gamma would restrict to the impossible pair inclusion. Therefore tensoring four additional normals cannot repair that particular native lifting problem.

This is not a prohibition on the supported dual Gysin operation. That operation acts on the dual comparison resolution and evaluates a different extension. No equation here identifies its unit with native gamma or with the generic top class theta.

## 4. Construct the closed-support union and its resolution

Consider the alternative of assembling the three pair supports by closed-cover descent. Their union is defined by

\[
J_\cup=J_1\cap J_2\cap J_3=J_1J_2J_3.
\]

In words: a monomial belongs to this ideal exactly when it contains at least one variable from each pair. The equality holds coefficientwise over the alternating ring; it does not assume that ring is a domain. There are eight squarefree generators, one for each choice of one parameter from each pair.

There is an exact augmented closed-cover complex

\[
0\longrightarrow\mathcal B/J_\cup
\longrightarrow\bigoplus_i\mathcal B/J_i
\longrightarrow\bigoplus_{i<j}\mathcal B/(J_i+J_j)
\longrightarrow\mathcal B/J_\cap\longrightarrow0.
\]

In words: retain the three local objects, all three pairwise overlaps, and the triple overlap. This is not the tensor product of the three local quotients.

For a monomial, let V be the set of pair ideals in which none of its variables occurs. The corresponding coefficient row is the augmented simplex on V. If V is empty every term is zero. Otherwise the simplex contraction has integer unit coefficients. This proves exactness for arbitrary exponents and arbitrary coefficient modes; it is not a general assertion that arbitrary closed covers have this exactness property.

A small free resolution is obtained from the three ideal resolutions

\[
0\longrightarrow\mathcal B e_{i,st}
\xrightarrow{(-t_i,s_i)^T}
\mathcal B e_{i,s}\oplus\mathcal B e_{i,t}
\longrightarrow J_i\longrightarrow0.
\]

In words: each ideal has its existing ordered Koszul relation. Tensor these resolutions in the three disjoint variable blocks, then augment the product ideal into the coefficient ring. The result is

\[
F_4\longrightarrow F_3\longrightarrow F_2\longrightarrow F_1
\longrightarrow F_0\longrightarrow\mathcal B/J_\cup\longrightarrow0,
\]

\[
(\operatorname{rk}F_0,\ldots,\operatorname{rk}F_4)=(1,8,12,6,1).
\]

In words: this is a 28-generator coefficient resolution. It does not add carrier cells to the native geometry. Its exactness follows from the tensor factorization over independent polynomial blocks, or from the explicitly split integral fine-degree complexes.

An implementation formula uses a triple `b=(b1,b2,b3)` with each entry 0,1,2. Entries 0 and 1 choose s and t; entry 2 denotes that pair's syzygy. Its homological degree in F is one plus the number of 2 entries. If no entry is 2, the map to F0 multiplies the three chosen variables. Otherwise replace an entry 2 by 0 with coefficient minus t-i or by 1 with coefficient s-i, multiplied by minus one to the number of preceding syzygy entries. These formulas and all matrices are exported in the certificate.

## 5. Compute the dual assembly, including its overlap degrees

Define the scalar coefficient dual

\[
\mathcal U=\operatorname{RHom}_{\mathcal B}(\mathcal B/J_\cup,\mathcal B)
\simeq\operatorname{Hom}_{\mathcal B}(F,\mathcal B).
\]

In words: the complete 28-generator dual retains the differential and therefore the assembly information, not just a list of residue lines. In the Hom convention its differential from degree q is `(-1)^(q+1)` times the transpose of the next chain differential [M3].

In fixed ordered normal and cover frames, its cohomology is

\[
H^2(\mathcal U)\cong\bigoplus_{i=1}^3\mathcal B/J_i,
\]

\[
H^3(\mathcal U)\cong\bigoplus_{1\le i<j\le3}\mathcal B/(J_i+J_j),
\qquad H^4(\mathcal U)\cong\mathcal B/J_\cap,
\]

\[
H^q(\mathcal U)=0\quad(q\notin\{2,3,4\}).
\]

In words: the three pair residues occupy degree two, their three overlap classes degree three, and their triple compatibility degree four. In particular, a triple-overlap contribution in descent has degree four, not the degree six of a triple composition.

### Explicit generators and normal lines

For a nonempty subset A of the three pair labels, choose syzygy entries in those positions. In each complementary position, sum over the two variable entries, with coefficient that chosen variable. Explicitly, if `b(A,epsilon)` is that basis triple,

\[
z_A=\sum_{\epsilon\in\{s,t\}^{A^c}}
\left(\prod_{i\notin A}\epsilon_i\right)b(A,\epsilon)^\vee.
\]

In words: each selected pair contributes a syzygy dual, and each unselected pair contributes its augmentation. There are three four-term cycles in degree two, three two-term cycles in degree three, and one one-term cycle in degree four. They are closed by cancellation of `-t_i*s_i+s_i*t_i`.

The parameters in the selected pairs kill z-A through explicit primitives. No other coefficient relation occurs. To verify completeness, use the fine normal grading: every generator weight has entries zero or one. In the dual, a homogeneous component is present according to whether `g+weight` is nonnegative. Degrees below minus one have no entries. The homogeneous matrix therefore depends only on which coordinates have degree minus one. Its nonzero cohomology occurs exactly when those negative coordinates form a union of complete pairs, in degree one plus their number. The 64 possible negative-coordinate patterns exhaust all degrees. Integral unit reductions prove each surviving coefficient is primitive and the other components are exact.

Invariantly, each displayed summand also carries the dual determinant of its selected normal pairs and the orientation of its ordered cover-index set. Permuting selected pair blocks changes the cover orientation; exchanging two normals inside one selected pair changes that conormal determinant. The checker verifies all 48 signed permutations of the three blocks and their two internal labels on the full resolution and dual.

The source endpoint lines have not been identified with these conormal/cover lines. The calculation here strips only the explicit endpoint frame to isolate the underlying coefficient descent. Restoring a single common endpoint local system requires compatible descent identifications of the three labelled endpoint lines. Taking three endpoint lines in a tensor product is not itself such an identification. None of these line twists can repair the support distinction below.

These cohomology isomorphisms do **not** claim that U splits as the direct sum of its shifted cohomology modules in the derived category. The complete dual differential is retained.

## 6. A local witness separating descent from composition

Localize at

\[
f=s_2s_3=t_{02}t_{24}.
\]

In words: only the first parameter from each of the other two pairs is inverted. The first pair can still vanish on this open. These inverses are used as a mathematical local test; they do not alter the unlocalized source.

There,

\[
(\mathcal B/J_\cup)_f\cong(\mathcal B/J_1)_f,
\qquad (\mathcal B/J_\cap)_f=0.
\]

In words: the union restricts to its first component, while the common intersection is absent. The regular-pair duality gives

\[
\mathcal U_f\simeq(\mathcal B/J_1)_f[-2]\otimes\det(J_1/J_1^2)^\vee,
\qquad (\mathcal D_\cap)_f\simeq0.
\]

In words: descent retains the known nonzero first pair operation on this open; the triple tensor kills it. No degree shift or orientation-line identification can make these objects equivalent.

This proves that the tensor construction is not the assembly of the three supported coefficient objects along their closed-cover intersections. It does not prove that the native geometry uses this particular closed-cover assembly. It gives a decisive locality test for any proposed identification.

## 7. The honest union target still has a Q-lifting obstruction

Let E-PC, A-boundary and Q-PC be the existing full support triangle; no change of its carrier is made. Compare

\[
\mathcal U\otimes E^{\rm PC}\longrightarrow\mathcal U\otimes Q^{\rm PC}.
\]

In words: apply the constructed coefficient-descent operation to the actual target and its generic support quotient. On the open f above this is the supplied first-pair operation, with its degree and normal line.

The preceding target theorem, independently rerun for this note, gives for that pair

\[
\mathfrak a_{04,35}
=(t_{13}t_{15}t_{02}t_{24},\ t_{13}t_{15}I_+,\ t_{02}t_{24}I_-)
\]

in `B/(t04,t35)`. In words: these are exactly the coefficients of the genuine generic cycle theta that admit closed target lifts, not a guessed ideal of desirable coefficients [S3].

After the present localization,

\[
(\mathfrak a_{04,35})_f=(t_{13}t_{15},I_-).
\]

In words: the remaining positive-sheet two-parameter product still matters. This is a proper ideal: its quotient by `I_minus,t13,t15` is nonzero. Hence the unit does not lie in the image.

There is also a direct independent obstruction in a single target row. The top component of a lift of theta must be `U_L`, where `U_L=u03*u14*u25`. On the positive branch, the unmarked-13 equation would require

\[
t_{13}a_{13}=-U_L.
\]

In words: the marked-13 coefficient would have to divide by t13 in a top coefficient module where that inverse is not present. Reduction modulo t13 leaves zero on the left and the nonzero independent long-normal product on the right. The equation is obtained by multiplying the actual PC row by its normal and cancelling the positive-sheet occurrence in that polynomial domain; it is not an illegal global cancellation in the alternating ring.

Therefore the localized union projection has no derived section. Any global section would restrict to one, so the global section space is empty. If

\[
\mathscr S_\cup=
\operatorname{hofib}_{1}\!\left(
\operatorname{Map}(\mathcal U\otimes Q^{\rm PC},\mathcal U\otimes E^{\rm PC})
\longrightarrow
\operatorname{Map}(\mathcal U\otimes Q^{\rm PC},\mathcal U\otimes Q^{\rm PC})
\right),
\]

then

\[
\mathscr S_\cup=\varnothing,
\qquad \mathscr S_\cap\ne\varnothing.
\]

In words: the union-dualized projection cannot split even up to homotopy, while the intersection-dualized projection has the previous strict section. Adding endpoint constraints cannot turn the empty union section space into a nonempty one. This does not exclude a morphism from a different native source that is not required to split the entire Q module.

The previous coefficient-linearity obstruction similarly restricts to a cyclic class with annihilator `I_plus+I_minus+(t13*t15)` on this open. Thus descent does not inherit the simultaneous-intersection cancellation of either lifting problem.

## 8. Construct a generic-preserving comparison triangle

The quotient unit lifts canonically to the degree-zero generator of F. Dualizing gives a coefficient counit

\[
\epsilon_\cup:\mathcal U\longrightarrow\mathcal B.
\]

In words: select the degree-zero dual coefficient, with every other cochain degree mapping to zero. This is the dual of the quotient map, not a scalar trace on native gamma. In its invariant endpoint version the common endpoint-dual line appears on both sides.

For any supplied complex N define

\[
\mathcal U\otimes N\xrightarrow{\epsilon_\cup\otimes1}N
\longrightarrow\mathcal R_\cup(N),
\qquad
\mathcal R_\cup(N)=\operatorname{Cone}(\epsilon_\cup\otimes1).
\]

In words: retain the supported comparison and its cone instead of replacing the whole object by its supported term. This construction is coefficient-linear and natural in N. Since U has a bounded free model, it preserves the target's support triangles, quotient maps and any endpoint connector maps actually supplied as input. Naturality does not create a missing connector.

On the open where all six Rees parameters are invertible,

\[
\mathcal R_\cup(N)[T^{-1}]\simeq N[T^{-1}].
\]

In words: the cone retains all generic data that N already carried on that open. For the scalar complex N=B its cohomology is B in degree zero and the three successive Ext groups of Section 5 in degrees one, two and three. Its 29-generator cone differential is included in the checker.

This is a finite derived-support comparison layer. It is not the full local-cohomology functor for a closed support, which would require its appropriate derived support construction over all thickenings, nor is it claimed to be a nearby-cycle functor. The physical source might require a different bivariant gluing object.

The construction provides concrete data for a native-source test: a full comparison triangle, a retained generic map, all overlap degrees, and normal/endpoint-line obligations. It does not identify the native source with the cone, map gamma to a unit, or establish either missing spatial endpoint connector.

## 9. Verification, provenance, and the next falsifiable requirement

Run:

```sh
python check_marici_orbit_source_admissibility_20260907.py --output marici_orbit_source_admissibility_certificate_20260907.json
```

The standalone checker passes **65,252 exact assertions**. It verifies all 512 triple-dual columns, three localized contractions and their three higher comparisons, the actual triple counit, the 28-generator union resolution and its dual, seven explicit Ext cycles and their annihilation primitives, 48 signed symmetries, all closed-cover support patterns, and 1,458 integral fine-degree calculations. It also rechecks the native specialization's gamma detector and the first-pair Koszul inclusion used by the six-normal no-lift argument. Its localized Q obstruction uses the exact target image ideal and a separate impossible singleton equation.

The previous complete supported-pair/orbit target checker was independently rerun and passed **446,156** assertions, including its 10,206 exact target-kernel calculations. The replay is recorded as `marici_pair_input_recheck_for_source_20260907.json` in this runtime. The new script itself is standalone; it does not silently replay that larger calculation on every run.

The all-degree conclusions use the regular-sequence, monomial exactness, fine-grading and local obstruction proofs, not numerical extrapolation. No proof assistant or repository write is claimed.

The remaining source requirement is sharper than before: determine the actual source's assembly operation and give its comparison to the full supported/generic triangle. An identification by tensoring the three rotations would have to survive the open-set locality test above, which it does not if the intended assembly is closed-support descent. A different native bivariant source must explain why it is neither that union section problem nor a replacement that deletes its required generic fibre.

## References

[S1] Supplied library artifact `supported_gysin_proof.md`, version 1, 2026-09-07: the actual 3–4–1 pair resolution, ordered signs, dual purity and counit, native gamma specialization/quotient, and the distinction between an extension residue and a direct native trace. No assertion is made that this is the newest complete source geometry in parallel branches.

[S2] Marici, `src/ledger/20260814-108 Local D03 Exit Class and the Generic-Q Kernel Criterion.md`, at the pinned commit; blob `0be216e2b24d0df5b6ccbc6135e7a46bcc190a5e`. This specifies nonzero generic support of the particular kernel as a necessary condition. Applying it to the six short parameters requires the same generic-open identification; that identification is not inferred from notation.

[S3] Previous local artifact `marici_q_supported_pair_and_orbit_20260907.md`, its standalone checker and certificate: exact one-pair PC lifting ideal, all 64 support patterns, and the strict triple-intersection Q section. Hashes of these runtime inputs are recorded in the new certificate.

[M1] Stacks Project, The Koszul complex, tag 0621: ordered differential, multiplication nullhomotopies, and tensor products. https://stacks.math.columbia.edu/tag/0621

[M2] Stacks Project, regular sequences imply Koszul regularity, tag 062F. https://stacks.math.columbia.edu/tag/062F

[M3] Stacks Project, Hom complexes, tag 0A8H: the dual differential convention. https://stacks.math.columbia.edu/tag/0A8H

[M4] Stacks Project, Cartier duality, tag 0B4B: the supported dual normal line and degree. https://stacks.math.columbia.edu/tag/0B4B
