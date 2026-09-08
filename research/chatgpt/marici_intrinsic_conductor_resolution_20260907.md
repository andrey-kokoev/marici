# Intrinsic conductor resolution of the complete endpoint source

Date: 2026-09-07  
Lane: Branch B — source comparison, endpoint descent, and derived duality  
Source baseline: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result and scope

The previous reverse-cone calculation used finite free resolutions over the smooth six-occurrence ambient ring. It explicitly did not compute the intrinsic derived conductor fibre over the singular alternating ring. This note constructs the latter in every degree, for the conductor, the two normalization branches, both branch ideals, and the entire fourteen-channel source S14. It also gives the corresponding intrinsic exceptional restriction of the reverse diagram.

The all-degree result is an explicit alternating-word free resolution with an integral augmentation contraction. This is a specialization of the general fibre-product resolution method in Moore [M1]; the new work here is its coefficient-ring proof, the application to the actual S14 and native relative source, and the endpoint-labelled chart comparisons. It is not a claim to have discovered infinite resolutions of fibre-product rings.

There are two substantive consequences. First, the intrinsic conductor marking space is genuinely unbounded: its first positive homotopy ranks are 168, 644, 2478, 9534, and so on. These are syzygies forced by the existing coefficient algebra, not added geometric cells or artificially chosen degree shifts. Second, the entire intrinsic fibre still fails to determine the global endpoint attachment. Setting both endpoint off-diagonal residues to zero leaves this fibre unchanged in every degree. The full seven-chart comparison below retains the data that distinguish those diagrams.

S14 remains the target-selected normalization-pullback source. Nothing here identifies it with a native physical six-functor kernel. The comparison with the actual eleven-state endpoint source gives a necessary test for an equivalence, not a no-go theorem for arbitrary maps or support-changing correspondences. Homological grading is used for resolutions and Tor; reverse exceptional restriction is explicitly cohomological.

## 1. Coefficients and the chart containing the conductor

Retain the labelled sets

\[
S_+=\{13,15,35\},\qquad S_-=\{02,04,24\},\qquad L=\{03,14,25\}.
\]

In words: the first two are the occurrence sheets; the last set contains the three independent long channels. Within a sheet the displayed order fixes the exterior signs.

Keep the same rings and products as in the preceding source presentation:

\[
\mathcal C=\mathbb Z[t_s\ (s\in S_+\cup S_-),X_l,u_l\ (l\in L)],\qquad
\mathcal B=\mathcal C[X_s]/(X_pX_m:p\in S_+,m\in S_-),
\]

\[
\tau_+=\prod_{p\in S_+}t_p,\qquad \tau_-=\prod_{m\in S_-}t_m,\qquad
T=\tau_+\tau_-,\qquad I=I_+\oplus I_-.
\]

In words: opposite-sheet occurrence products vanish. The Rees parameters and independent long parameters remain part of the coefficient ring. The occurrence conductor ideal I is not the ideal of a regular six-coordinate sequence in this singular ring.

The test open is still

\[
V=\operatorname{Spec}\mathcal B\setminus V(T,\tau_+I_+,\tau_-I_-).
\]

Its conductor is contained entirely in the central chart U0=D(T). On that chart abbreviate

\[
C=\mathcal C[T^{-1}],\qquad
B=C[x_1,x_2,x_3,y_1,y_2,y_3]/(x_i y_j),\qquad C=B/I.
\]

In words: x names the positive occurrences in their displayed order, y the negative ones. This localizes only on the already specified central chart. It does not adjoin any new inverse to the original physical base or identify V with a physical generic deformation.

The algebraic resolution below works over any commutative spectator ring C. In particular it works before this localization, after it, after a field specialization of C, or after adjoining monodromy units whose conductor value is one.

## 2. A free conductor resolution in every degree

Let a block be a nonempty ordered subset of the three positive labels or of the three negative labels. A word is a sequence of blocks with alternating sheet labels. Its degree is the total number of labels, counted with repetition across different blocks:

\[
w=[A_1|\cdots|A_k],\qquad |w|=\sum_{j=1}^k|A_j|.
\]

In words: within a block a variable occurs at most once, but it may recur in a later block after an opposite-sheet block. The empty word has degree zero.

Let P_n be the free B-module on words of degree n. If the first block is A1=(i1<...<ir), define

\[
d[A_1|A_2|\cdots|A_k]
=\sum_{j=1}^{r}(-1)^{j-1}v_{i_j}
[A_1\setminus\{i_j\}|A_2|\cdots|A_k].
\]

An empty first block is removed. In words: apply the ordered Koszul differential only to the first block. Here v_i is the actual x or y occurrence coordinate with that label.

This is a B-linear differential. When the first block has at least two entries, the usual exterior signs cancel d squared. When it has one entry, removing it exposes a block on the opposite sheet; the next coefficient product is zero by x_i y_j=0. Thus d squared is zero on every word. Augment the empty word by B -> C.

Examples are

\[
\begin{aligned}
d[x_i,x_j]&=x_i[x_j]-x_j[x_i],\\
d[y_j|x_i]&=y_j[x_i],\\
d[x_i|y_j|x_k]&=x_i[y_j|x_k].
\end{aligned}
\]

In words: the second line keeps one of the mixed syzygies separately, rather than merging it with its opposite-ordered partner. The last line is a higher relation required because the two consecutive occurrence coefficients multiply to zero.

### An explicit integral exactness proof

Every coefficient is a unique C-linear combination of the constant monomial, positive-sheet monomials, and negative-sheet monomials. It suffices to define a C-linear contraction on one such monomial times one word. No division by an integer is used.

For m=1 set h(mw)=0. For a nonconstant monomial m on sheet sigma, take A to be the first block if it lies on sigma, and otherwise take A empty. Let v be the remaining suffix in the former case and all of w in the latter. Set

\[
i=\min(\operatorname{supp}(m)\cup A).
\]

If i lies in A set h(mw)=0. Otherwise put

\[
h(m[A|v])=(-1)^{|\{j\in A:j<i\}|}\frac{m}{v_i}[A\cup\{i\}|v].
\]

In words: move the smallest available occurrence from the monomial into the first exterior block. The quotient m/v_i removes a known factor of the monomial; it is a polynomial, not a localization. If A was empty, prepend its new singleton block.

This gives

\[
dh+hd=1-\iota\epsilon,\qquad h^2=0,
\]

where epsilon is nonzero only in degree zero, and iota includes C as constant polynomials. The maps h and iota are C-linear, not B-linear.

Here is the all-degree verification. If the coefficient is nonconstant on the opposite sheet to the first block, the differential of mw is zero; h prepends a singleton and its differential is mw. If the coefficient and first block are on the same sheet, the ordinary monomial Koszul contraction applies, with the suffix held fixed; after a block disappears, the next block lies on the opposite sheet, so the same calculation still applies. If m=1 and w is nonempty, exactly the differential term that removes the least label is returned by h; its two signs multiply to one. The only remaining case is the constant empty word, for which both sides vanish. Applying h twice gives zero because its selected least label is already in the first block after one application.

Therefore P resolves C in all degrees. This proof is independent of a finite enumeration, the characteristic of C, or the size of polynomial exponents.

### Branch and ideal resolutions

To resolve B_plus, retain P0=B and all nonempty words ending on the negative sheet. To resolve B_minus, retain words ending on the positive sheet. These are subcomplexes. The same contraction works, except that in degree zero it fixes all monomials on the retained sheet. Thus the augmentation targets are the actual polynomial normalization branches, not merely their constant values.

A resolution Q_sigma of I_sigma is the shifted nonempty tail of the resolution of the opposite branch. Its degree-n basis consists of words of degree n+1 ending on sigma. In degree zero the augmentation sends a singleton [i] to v_i in I_sigma. This gives explicit B-linear free resolutions of both ideals, with every normal and occurrence label retained.

## 3. Compute every conductor Tor group

All entries of every resolution differential lie in I. Tensoring with C therefore sets the differential identically to zero. The displayed resolution is minimal relative to this augmentation; no claim that C itself is a field is required.

Put

\[
a(z)=3z+3z^2+z^3.
\]

In words: one nonempty block has three singleton choices, three two-label choices, and one three-label choice. There are two choices of its sheet, and later sheets alternate. Counting words gives

\[
P_C^B(z)=1+2\sum_{k\ge1}a(z)^k
=\frac{(1+z)^3}{1-3z-3z^2-z^3}.
\]

In words: the coefficients count the free C-bases of Tor_n^B(C,C), not integer torsion orders.

Similarly,

\[
P_{B_\sigma}^B(z)=\frac1{1-3z-3z^2-z^3},\qquad
P_{I_\sigma}^B(z)=\frac{3+3z+z^2}{1-3z-3z^2-z^3}.
\]

The first conductor ranks, starting with degree zero, are

\[
1,6,24,92,354,1362,5240,20160,77562,\ldots.
\]

In words: there are nonzero syzygies in every degree. All these modules are free over C. Over the polynomial/Laurent integral spectators in this problem they are also torsion-free as abelian groups. Neither the growth of the ranks nor the two-sheet construction creates new p-torsion or a nonzero integral Bockstein.

This recovers the field-specialized fibre-product Poincare formula [M1]. The explicit contraction above proves the integral spectator version used here, without extending a field theorem by an unproved flatness argument.

## 4. Compare the actual native endpoint and relative sources

Branch A's retrieved source-admissibility proof supplies an exact integral retraction

\[
J_B\simeq B[1],\qquad
F=\operatorname{fib}(J_B\xrightarrow{\epsilon r}C[1])\simeq I[1].
\]

In words: J_B is the finite free eleven-state endpoint source; r is its actual road readout. The universal source F on which that conductor readout can be nullhomotopic is the conductor ideal, shifted once. This does not identify F with the physical Morse source. In particular, the old primitive z is not a closed unit in F.

The new checker independently verifies all four degrees of the supplied J retraction matrices. Applying the ideal resolutions gives the complete continuation of Branch A's previously computed ranks 6 and 24:

\[
H_n(C\otimes_B^L F)=\operatorname{Tor}_{n}^{B}(C,C)
\quad(n\ge1),\qquad H_0(C\otimes_B^L F)=0.
\]

In words: the higher groups of that relative source have ranks 6,24,92,354,1362,... in homological degrees one,two,three,four,five,... . This dimension shift follows also from the exact sequence 0 -> I -> B -> C -> 0. It does not make the forbidden nullhomotopy of the nonzero unit-valued map exist on J_B.

## 5. Resolve S14 and all its chart comparisons

The previous source S14 has one generic coefficient and seven channels on each sheet. Each channel j has the same conductor residue r_j as before. The central chart contains the conductor, so every r_j is a regular scalar in C there. The change of coordinates

\[
z'_j=z_j-r_j b_{\sigma(j)}
\]

converts the normalization equations into common generic value plus zero conductor channel values. It follows, on U0 and in the specified channel frames, that

\[
\mathcal S_{14}|_{U0}\cong B\oplus I_+^{\oplus7}\oplus I_-^{\oplus7}.
\]

In words: this is a local splitting by actual branch functions, not a global splitting of the source on V. Channel fine-degree lines are retained; the rank notation omits only those line labels. The inverse sends z'_j to z'_j+r_j b_sigma.

The central free resolution is thus B in degree zero, together with seven copies of each Q_sigma. Its generic projection is the identity on the first B and zero on every ideal resolution. Forgetting the endpoints removes exactly one Q_plus and one Q_minus, leaving S12. All these maps are explicit in every degree.

### The other six charts and their overlaps

On a positive occurrence chart D(tau_plus X_p), a positive X_p is invertible. The negative sheet is zero and the conductor is absent. The original normalization source is therefore a free module of rank eight, with coordinates its generic branch coefficient and its seven positive channel functions. The analogous statement holds for a negative chart. Every nonempty intersection not consisting solely of U0 is on exactly one such sheet.

On a central/positive overlap, the comparison from the central resolution to those original eight coordinates is

\[
b\longmapsto(b,(r_jb)_j),\qquad
[i]_j\longmapsto X_i z_j.
\]

In words: the generic basis supplies the actual residue vector, while a degree-zero ideal generator supplies its occurrence multiple in the actual channel. Opposite-sheet channels vanish. Every higher component of this comparison is zero. The ordered relations in the free resolution make this a chain map.

Restrictions among positive charts are the identity in the original normalization coordinates, as are restrictions among negative charts. These maps commute on all higher intersections. Their complete Cech diagram has 7,12,8,2 nonzero terms in successive degrees, exactly as in the preceding construction. It is a homotopy-cartesian diagram of local resolutions of the existing sheaf, not a replacement of its coefficients by a constant diagram.

The quasi-isomorphisms are explicitly invertible up to homotopy. On D(X_p), insert the label p into the first positive block, with its exterior sign, and multiply by X_p^{-1}. If the first block is negative, prepend [p]. This contracts the conductor resolution, since the conductor is empty there. On the ideal resolution it contracts the positive ideal onto the free coefficient line and the negative ideal onto zero. A section of the positive ideal augmentation is [p]/X_p.

For p<q on the same sheet,

\[
d\frac{[p,q]}{X_pX_q}=\frac{[q]}{X_q}-\frac{[p]}{X_p}.
\]

For p<q<r,

\[
d\frac{[p,q,r]}{X_pX_qX_r}
=\frac{[q,r]}{X_qX_r}-\frac{[p,r]}{X_pX_r}+\frac{[p,q]}{X_pX_q}.
\]

In words: these are the pairwise comparison homotopy and its triple compatibility. The denominators are allowed on exactly the named overlap. The generic inverse has the additional terms minus r_j[p]/X_p in all seven channels; its equations follow from the same formulas with the residues retained. No endpoint term is dropped.

Relabelling the variables acts on each exterior block with its permutation sign. Products of these signs give a semilinear chain action of all six admitted hexagon dihedral relabellings. It also permutes the channel residues by their actual long-normal/short-Rees formula and exchanges the endpoint channels correctly. The order-dependent integral augmentation contraction is not claimed to be equivariant; the free differential and the chart maps are equivariant, and the labelled local inverse homotopies transport with their named variable.

### The gluing obstruction has not disappeared

The endpoint terms of the generic central-chart section remain

\[
\frac{U_L}{\tau_-},\qquad\frac{U_L}{\tau_+}.
\]

In words: each requires all three opposite-sheet normal inverses. They are regular on U0 and its relevant overlaps, but not on the whole corresponding occurrence chart. For instance, on a positive occurrence chart one negative t can vanish while U_L remains one; the first fraction cannot extend over that point.

The coordinate change therefore cannot be used as a global diagonalization on V. The generic transition terms are exactly the preceding fourteen-residue cocycle, and endpoint forgetting retains the same non-split endpoint extension. In sheaf terms the complete source is the original extension

\[
0\longrightarrow\bigoplus_j\widetilde I_{\sigma(j)}\otimes\ell_j
\longrightarrow\mathcal S_{14}\longrightarrow\mathcal O_V\longrightarrow0.
\]

Here ell_j records the channel grading frame. In words: locally its kernel consists of seven copies of each native conductor-vanishing sector, but globally they attach to the generic coefficient through the existing residue class. The all-degree resolutions do not choose a splitting of this sequence or of the separate endpoint-forgetting sequence.

## 6. Exact intrinsic fibre and reverse exceptional restriction

Set

\[
b(z)=\frac{3+3z+z^2}{1-3z-3z^2-z^3}=\sum_{n\ge0}b_nz^n.
\]

Then, with all channel labels understood,

\[
\operatorname{rank}_C\operatorname{Tor}_n^B(C,\mathcal S_{14}|_{U0})
=\delta_{n0}+14b_n.
\]

In words: one generic degree-zero coefficient plus fourteen labelled ideal resolutions survive on the intrinsic conductor. Starting in degree zero, the ranks are

\[
43,168,644,2478,9534,36680,141120,\ldots.
\]

For S12 replace fourteen by twelve. The exact difference is two copies of the branch-ideal resolution, giving ranks 6,24,92,354,... . Thus the endpoint channels contribute in every intrinsic degree, rather than only at their visible degree-zero coordinates.

This is not the earlier smooth-ambient fibre. Over the regular ambient ring A=C[x,y], the primal S14 fibre has ranks 43,177,284,225,90,15 and ends. Over B it has the infinite sequence just displayed. Both calculations use derived pullback, but along different maps of rings. In particular the failure of the six occurrences to form a regular sequence in B cannot be repaired by reusing the finite ambient Koszul resolution as a free B-resolution.

Let i:Spec C -> Spec B be the intrinsic conductor immersion, and use the preceding relative dualizing normalization D_{B/C}=RHom_A(B,Omega^6_{A/C}[6]). Derived tensor-Hom adjunction gives

\[
i^!\mathbb D_{B/C}(\mathcal S_{14}|_{U0})
\simeq R\operatorname{Hom}_C
\left(C\otimes_B^L\mathcal S_{14}|_{U0},C\right).
\]

In words: exceptional conductor restriction of the reverse object is dual to the intrinsic derived conductor fibre of the original source. This uses i-exclamation, not ordinary pullback of the reverse object. The coefficient determinant lines cancel under the specified relative-dualizing convention; channel lines are dualized, not discarded. The identity follows by currying RHom_B(C,RHom_B(S14,D_{B/C})) and using RHom_B(C,D_{B/C})=C. No commutation of global sections and duality is assumed.

Since the displayed C-complex has zero differential and finite free terms in each homological degree, the exceptional reverse restriction has dual free groups of the same ranks in cohomological degrees zero,one,two,... . It is unbounded above. This does not say that the reverse object itself is unbounded coherent on V; the non-perfect conductor immersion is the additional operation producing these degrees.

### An all-degree negative control

The central normalization matrix for arbitrary residue scalars r is related to the zero-residue matrix by the explicit invertible triangular change z_j -> z_j+r_jb_sigma. Therefore changing or deleting either endpoint off-diagonal term leaves the whole intrinsic conductor fibre unchanged up to equivalence, not merely its ranks through some finite order. The same holds for the exceptional reverse conductor restriction.

The full chart diagrams do change. Their overlap coefficients retain the triple-normal poles that cannot be globally diagonalized. The nonzero endpoint extension and its previously proved annihilator remain the global discriminator. Hence even a match of every local Tor degree is insufficient for the missing source identification.

## 7. A genuinely unbounded coefficient infinity-groupoid

Let K14=C tensor_B^L S14 on the intrinsic conductor, with S14 in its coefficient degree zero, before any external carrier suspension. The actual generic projection gives K14 -> C. Define

\[
\mathscr X_{14}=\operatorname{hofib}_{1}
\left(\operatorname{Map}_{D_\infty(C)}(C,K14)\longrightarrow C_{\rm disc}\right).
\]

In words: mark the derived conductor coefficient object and require its generic coefficient to be one. This is a precisely specified linear marking problem, not the native physical moduli problem.

The displayed free resolution becomes a zero-differential nonnegative complex over C. Dold-Kan supplies its simplicial abelian model [M4]. In the chosen local channel frames,

\[
\pi_0(\mathscr X_{14})\cong(C^{42})_{\rm aff},\qquad
\pi_n(\mathscr X_{14},*)\cong C^{14b_n}\quad(n\ge1).
\]

In words: normalized components have forty-two independent coefficient coordinates. Within each component the first higher homotopy groups have ranks 168,644,2478,9534,... . There is no finite homotopy truncation that recovers the whole space.

The component count and higher groups come from a non-flat conductor operation on existing algebra. They are not additional physical particles, integer-prime torsion, or proof that the entire Marici target is this space. The global endpoint attachment is still part of the chart-level arithmetic packet; the isolated conductor infinity-groupoid forgets it, as the negative control shows.

## 8. Consequence for identifying the native source

At any field-valued conductor point, all the positive-degree ranks above remain nonzero. Thus S14 is not perfect as a B-complex near the conductor. By contrast, J_B and every bounded free native coefficient packet are perfect. Perfect complexes are closed under finite cones, shifts, retracts, tensoring with perfect complexes, and derived duality into B [M2]. Consequently no procedure confined to those operations over the same B can make such a packet equivalent to S14.

This is only an obstruction to an identification by the stated operations. It does not prohibit a map from a perfect source into S14, a source with a non-perfect conductor quotient, a normalization pushforward, or the supported duality operations being investigated in other lanes. In particular the native universal relative source F already contains I[1] and is not perfect. The all-degree construction identifies its conductor-vanishing sectors as the local building blocks of S14, with the extra channel labels and nontrivial global attachment still required.

No such global physical attachment has been independently constructed here. The concrete next identification target is the whole diagram: the generic coefficient, the fourteen resolved conductor-vanishing channels, their actual transition residues, both endpoint-forgetting maps, and their reverse Gysin attachments. Matching only a primitive unit, a finite ambient Tor packet, or even the entire isolated intrinsic conductor fibre is insufficient.

## 9. Exact verification and provenance

Run:

```sh
python check_marici_intrinsic_conductor_resolution_20260907.py --output marici_intrinsic_conductor_resolution_certificate_20260907.json
```

The default run performs **280,920 exact assertions**. It generates all words through homological degree six (ranks 1,6,24,92,354,1362,5240), checks the differential on them, and checks the integral contraction through degree five against all nineteen pure occurrence monomials of degree at most two. It also verifies the normalization-branch resolutions, named-chart contractions, actual residue covariance, all six admitted dihedral transports, chart comparison maps, endpoint forgetting, pair and triple inverse homotopies, and the arbitrary-residue triangular matrix identity. The rational generating functions are checked against exhaustive word counts, and their coefficients are exported through degree twenty.

The infinite exactness statement follows from the monomial contraction proof in Section 2. Large normal or occurrence powers are not inferred from sampled degrees. No monomial is multiplied in a truncated ring. The comparison maps are coefficient-natural; they act as the identity on the retained spectator parameters.

The preceding full reverse-cone checker was independently rerun and passed **51,635 exact assertions**. The replay certificate hash is recorded in the new certificate. That prior checker still verifies the original global residue diagram and its finite ambient model. The present native-matrix check is an independent check of the source retraction; it does not claim to have rerun the entire Branch A physical-source workflow.

No repository writes, proof-assistant certification, or geometric physical-connector construction is claimed.

### Inputs

- `marici_endpoint_complete_reverse_cone_20260907.md` and its checker/certificate: full S14 normalization presentation, actual channel residues, endpoint and generic maps, finite ambient duality, and source-identification scope.
- Branch A, `proof.md`, uploaded 2026-09-07T15:21:53Z, file id `file_00000000cf9881f59f583c1b4880630b`, title within text *Source admissibility of the proposed conductor–Morse primitive*: actual eleven-state matrices, F equivalent to I[1], and the first two conductor Tor ranks 6 and 24. Its explicit warning that F is not identified with the physical Morse source is retained.
- `marici_normalization_endpoint_extension_20260907.md`: prior nonzero global endpoint extension and its exact annihilator. This theorem is retained, not newly inferred from a local rank test.
- Source baseline Entry 93: the alternating normalization-conductor ring; Entry 436 checker: the finite endpoint complex. Both use the pinned commit above.

### Primary mathematical references

[M1] W. Frank Moore, *Cohomology of Fiber Products of Local Rings*, arXiv:0704.3631, Construction 2.3, Theorem 2.6, and Corollary 2.7; Journal of Algebra 321 (2009), 758–773. General alternating-word resolution and Poincare-series method in the local/graded field setting.

[M2] Stacks Project, *Perfect complexes*, tag 0656: definition, finite Tor dimension, closure operations, and perfect duality.

[M3] Stacks Project, *Hom complexes*, tag 0A8H, and *Dualizing complexes*, tag 0A7A: tensor-Hom signs, adjunction, and coherent duality. The exceptional-costalk formula in Section 6 includes its algebraic derivation.

[M4] Stacks Project, *Dold–Kan*, tag 019D: connective complexes and simplicial abelian groups.
