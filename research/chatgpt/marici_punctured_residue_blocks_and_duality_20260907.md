# Punctured-PC residue blocks, endpoint transgression, and the completed-duality test

Date: 2026-09-07  
Lane: Branch B — coefficient reconstruction and comparison maps  
Baseline: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result and limits

The entire 128-term punctured subcomplex of the existing PC target has an explicit, coefficient-linear, unit-triangular decomposition into twenty signed Čech/long-normal blocks. This is an isomorphism of the actual complexes, not just a homology calculation. It computes every homological degree and retains all allowed occurrence and long-normal pole orders.

Two of the blocks are the endpoint three-occurrence Čech complexes. Each has both a nonzero degree-two endpoint obstruction and a nonzero degree-zero triple-occurrence residue. In the derived occurrence-conductor fibre, an explicitly constructed third differential links these two degrees. Intrinsically over the singular alternating ring, that differential cancels the entire unbounded pair of Tor towers, not merely their first terms.

A further test is decisive for reverse comparisons. The completed affine coefficient dual sends the entire nonzero punctured subcomplex to zero. It therefore cannot distinguish the full target from its jet-visible quotient. This is a correct vanishing theorem for derived module Hom, not a physical repair of the missing closure equations. The punctured complex is not coherent, so coherent biduality does not apply to it. Its actual local dual on a punctured occurrence chart is nonzero.

The calculation is on the existing common chart, where the short Rees parameters were already units. It does not invert new physical parameters, identify a native source, identify occurrence residues with opposite-normal Gysin residues, or manufacture the missing spatial endpoint connectors. The earlier reverse comparisons of the coherent source remain unaffected by the noncoherence warning about the full localized target.

## 1. Fixed coefficient ring and complex

Write

\[
S_+=\{13,15,35\},\qquad S_-=\{02,04,24\},\qquad L=\{03,14,25\},
\]

\[
C=\mathbb Z[X_l,u_l:l\in L][t_s^{\pm1}:s\in S_+\cup S_-],
\qquad
B=C[X_s:s\in S_+\cup S_-]/(X_pX_m:p\in S_+,m\in S_-).
\]

In words: retain both occurrence sheets, the already permitted short Rees units, and all independent long occurrence and normal parameters. Put

\[
A_+=B/I_-,\qquad A_-=B/I_+,\qquad I_\sigma=(X_s:s\in S_\sigma),\qquad I=I_++I_-.
\]

In words: each normalization branch is a polynomial ring in its three occurrences over C. Its conductor is C.

The original 215 loaded states are noncrossing pairs \([F,H]\), with \(H\subseteq F\). Their homological degrees and modules are

\[
|[F,H]|=3-|F|+|H|,
\qquad
B[u_a^{-1}:a\in F\setminus H],
\qquad u_s=t_sX_s.
\]

In words: precisely the unmarked labels are localized. An opposite-sheet pair of localized occurrences makes the coefficient module zero. Fifteen states have this property.

The supplied differential is

\[
d[F,H]=\sum_a(-1)^{\#\{b\in F:b<a\}}\frac{X_a}{u_a}[F+a,H]
+(-1)^{3-|F|}\sum_{h\in H}(-1)^{\operatorname{pos}_H(h)}[F,H-h].
\]

In words: retain the actual radial ratios and signed normal-localization maps. Indices in positions start at zero. On a short radial arrow, the ratio is the existing unit \(t_s^{-1}\), inside its localized target module.

The 128 states with at least one short occurrence inverted form a subcomplex P. The full target F and its 72-term quotient F0 satisfy

\[
0\longrightarrow P\longrightarrow F\longrightarrow F_0\longrightarrow0.
\]

In words: this is the exact target sequence already used to construct the seventeen-channel top obstruction. P has 66, 54, and 8 coefficient summands in homological degrees two, one, and zero, respectively.

## 2. An actual twenty-block decomposition

### 2.1 Why the index set is small

P splits into its two localized polarities. Once a positive occurrence is inverted, every negative occurrence acts by zero, and any differential that would invert a negative occurrence has zero target. Thus every negative short label already present is permanently marked.

There are only four possibilities for that marked opposite support: the empty set, or one of the three negative singletons. A negative singleton has exactly one compatible positive short label. The three mixed edges are

\[
\{02,35\},\quad\{04,13\},\quad\{15,24\}.
\]

In words: they form a matching between the two short triangles, not an additional triangle.

On each polarity there are seven blocks indexed by nonempty subsets J of its three active occurrences, plus three mixed-singleton blocks. This gives ten blocks per polarity and twenty altogether.

### 2.2 Explicit triangular basis change

A new generator is specified by: a polarity; fixed opposite marked support N; a nonempty active subset J; a nonempty unmarked subset \(U\subseteq J\); and a long state that is absent, marked, or unmarked. At most one long label is present. Let \((F_0,H_0)\) be the resulting leading loaded cell. Every other compatible active label may enter as a closed short factor.

For a subset K of those remaining compatible labels, let \(q=|K|\). Define

\[
\mathcal T(b)=
\sum_K
(-1)^{q(3-|F_0|)+q(q-1)/2+
\sum_{i\in K}\#\{a\in F_0\setminus H_0:a<i\}}
\left(\prod_{i\in K}t_i^{-1}\right)
[F_0\cup K,H_0\cup K].
\]

In words: expand the unused active directions as closed combinations of their absent and marked states. The leading coefficient is one. Other terms have more marked labels but exactly the same unmarked/localized set.

This map is unit triangular by face size. Its inverse is finite triangular elimination. It never divides an occurrence, long normal, integer, or nonunit coefficient. Since all terms have the same localization domain, it is a map of the supplied coefficient modules, including arbitrary allowed negative occurrence powers.

The short radial contribution that adds an unused label cancels the normal contribution removing that label from the next summand. The remaining differential either unmarks a label in J or changes the long state. It cannot change the block. The source's short-face incidence guarantees all the cancellations are on existing faces. The checker verifies this identity on all 128 generators and gives both inverse identities.

The same construction is covariant under rotation by two vertices and the reflection \(v\mapsto3-v\), with the product of the induced face and marking permutation signs. No averaging or equivariant section is used. The final conversion to standard tensor signs is an explicitly solved diagonal sign change, with every sign-cycle equation checked.

### 2.3 Identify the blocks, retaining long-localization degrees

For nonempty J on a branch, define the positive-degree Čech complex

\[
\mathcal C_J^r=
\bigoplus_{U\subseteq J,\ |U|=r} A_\sigma[X_U^{-1}],
\qquad 1\le r\le |J|,
\qquad X_U=\prod_{i\in U}X_i.
\]

In words: retain every nonempty occurrence intersection. The differential is the alternating localization map. This complex starts in cohomological degree one, one degree above the usual open-cover Čech placement.

For a compatible long-label set H define

\[
\mathcal L_H^0=C\oplus\bigoplus_{l\in H}C,
\qquad
\mathcal L_H^1=\bigoplus_{l\in H}C[u_l^{-1}],
\]

\[
d(a,(h_l))=(X_lu_l^{-1}a+h_l)_{l\in H}.
\]

In words: retain the long radial comparison and every long marked-normal term. In particular, the marked-to-localized map is an inclusion, not an isomorphism unless that long normal is actually inverted on a further open.

If H is empty this is just C in degree zero. Write

\[
\ell_H=H^0(\mathcal L_H)=C\cdot v_H,
\qquad
v_H=\left(\prod_{l\in H}u_l,
\left(-X_l\prod_{k\in H\setminus\{l\}}u_k\right)_{l\in H}\right),
\]

\[
\mathcal V_H=H^1(\mathcal L_H)
=
\frac{\bigoplus_{l\in H}C[u_l^{-1}]}
{\bigoplus_{l\in H}C+C\cdot(X_l/u_l)_{l\in H}}.
\]

In words: the first is the primitive polynomial long-cycle line, with its actual homogeneous label. The second retains all remaining long poles and their single shared radial relation. These modules are not replaced by their values on a unit.

Let H(J) be the long labels compatible with J. Each singleton has two compatible longs, each same-sheet pair has one, and the full triple has none. The mixed-singleton block has the same two longs as its active singleton.

After the explicit orientation changes,

\[
P_\sigma\cong
\left[
\bigoplus_{i\in S_\sigma}
(\mathcal C_{\{i\}}\otimes_C\mathcal L_{H(i)})^{\oplus2}
\oplus
\bigoplus_{J\subseteq S_\sigma,\ |J|=2}
\mathcal C_J\otimes_C\mathcal L_{H(J)}
\oplus\mathcal C_{S_\sigma}
\right][3].
\]

In words: this is a chain isomorphism, retaining 64 original summands on each sheet. The two singleton copies have different labels: the empty-opposite-mark block and its actual matched opposite-mark block. The brackets use cohomological shift conventions. A Čech term of degree r and long term of degree s is in homological degree \(3-r-s\).

The numbers per sheet are six singleton blocks with five terms each, three pair blocks with nine terms each, and one endpoint block with seven terms: 30+27+7=64.

## 3. Complete homology of the punctured subcomplex

The block formula is already a complete presentation in the derived category, with every extension and localization map retained. Here is its homology in a form that does not assert unproved splittings.

For \(|J|\ge2\), put

\[
\mathcal T_J=H^{|J|}_{(X_j:j\in J)}(A_\sigma).
\]

In words: these are the ordinary coordinate-supported local-cohomology modules, represented by Laurent monomials negative in every label of J. They are free over C as additive coefficient modules. The nonaugmented occurrence Čech complex has its usual regular functions in degree one and \(\mathcal T_J\) in degree \(|J|\); singleton Čech is just its localization in degree one. This follows directly by selecting an occurrence outside the negative support to contract the corresponding monomial simplex [M1].

The top homology is

\[
H_2(P_\sigma)\cong
A_\sigma\ell_\varnothing
\oplus\bigoplus_{|J|=2}A_\sigma\otimes_C\ell_{H(J)}
\oplus\bigoplus_{i\in S_\sigma}
(A_\sigma[X_i^{-1}]\otimes_C\ell_{H(i)})^{\oplus2}.
\]

In words: four regular branch lines and six localized branch lines survive per sheet, with all their different homogeneous labels. This is much larger than the finite seventeen-channel image of the old top connecting map.

The bottom homology is

\[
H_0(P_\sigma)\cong
\mathcal T_{S_\sigma}
\oplus\bigoplus_{|J|=2}\mathcal T_J\otimes_C\mathcal V_{H(J)}.
\]

In words: retain the endpoint triple-occurrence residues and the three pair-occurrence/long-normal residue families on each sheet.

For the middle homology define

\[
A_\sigma^{(1)}=
\bigoplus_i(A_\sigma[X_i^{-1}]\otimes_C\mathcal V_{H(i)})^{\oplus2}
\oplus\bigoplus_{|J|=2}A_\sigma\otimes_C\mathcal V_{H(J)},
\]

\[
A_\sigma^{(2)}=
\bigoplus_{|J|=2}\mathcal T_J\otimes_C\ell_{H(J)}.
\]

In words: the first module retains long-pole contributions and the second retains double-occurrence poles with the correct long-cycle coefficient. There is a canonical exact sequence

\[
0\longrightarrow A_\sigma^{(1)}
\longrightarrow H_1(P_\sigma)
\longrightarrow A_\sigma^{(2)}\longrightarrow0.
\]

In words: the complete block complexes, not a direct sum of these two modules, specify the middle attachment. The sequence splits after forgetting to C-modules using monomial Čech contractions; no branch-ring-linear or geometrically natural splitting is asserted.

All other homological degrees vanish. These descriptions follow by tensoring independent occurrence and long complexes. Occurrence cohomology is C-free, so the indicated Künneth calculation has no suppressed coefficient Tor terms. All homology is torsion-free as an abelian group. The long quotients may have polynomial-parameter torsion; no claim of flatness over C is made for them.

### The previous seventeen-channel image is proper

The preceding connecting columns are differentials of polynomial top cycles and contain no negative short-occurrence coefficient. The triangular change uses only t units, so it preserves this property.

In a singleton block, let \(\Psi_i\) be its primitive top cycle, including its two-long polynomial correction. Then

\[
X_i^{-1}\Psi_i\in H_2(P),
\qquad
X_i^{-1}\Psi_i\notin\operatorname{im}\bigl(H_3(F_0)\longrightarrow H_2(P)\bigr).
\]

In words: this is an actual additional punctured class. Its negative occurrence coefficient is available in its own localized module, but cannot be produced by any coefficient in the preceding polynomial top source. The checker supplies the full chain for i=13. Since P has no degree-three terms, this comparison cannot be altered by a boundary entering H2.

This is not permission to add that pole to a native source; it is a class already present in the actual target localization.

## 4. The two endpoint blocks and their hidden lower residues

For an endpoint polarity let \(S_\sigma=(i_1,i_2,i_3)\) in its fixed order. Its block has no long labels. In homological degrees two, one, zero it is

\[
\mathcal P_\sigma=
\left[
\bigoplus_i A_\sigma[X_i^{-1}]
\longrightarrow\bigoplus_{i<j}A_\sigma[(X_iX_j)^{-1}]
\longrightarrow A_\sigma[(X_{i_1}X_{i_2}X_{i_3})^{-1}]
\right].
\]

In words: it is the actual three-occurrence Čech complex on the endpoint, not a newly attached resolution. It is a direct summand of P under the constructed chain isomorphism.

The fully marked endpoint e-sigma lies in F but not P. Its boundary becomes the Čech augmentation. Thus

\[
H_2(\mathcal P_\sigma)=A_\sigma[de_\sigma],
\qquad H_1(\mathcal P_\sigma)=0,
\qquad H_0(\mathcal P_\sigma)=\mathcal T_{S_\sigma}.
\]

In words: the endpoint closure obstruction in degree two is joined to an independent lower residue module in degree zero.

The primitive lower residue is represented by the fully unmarked endpoint with coefficient

\[
\frac{1}{X_{i_1}X_{i_2}X_{i_3}}.
\]

In words: all three occurrence denominators are allowed at exactly that endpoint summand. In its all-negative occurrence degree there is no degree-one term from which it could be a boundary. Multiplication by an active occurrence makes it a boundary through the corresponding singly marked endpoint; opposite occurrences annihilate the localized module. Its coefficient annihilator over B is I.

These are occurrence-coordinate residues. They are not the opposite-normal pair-supported operation from Branches A or C.

### The third differential, with an explicit chain witness

Let \(b_U\) be the oriented endpoint Čech basis

\[
b_U=(-1)^{\sum_{i\in U}\operatorname{pos}_{S_\sigma}(i)}
[S_\sigma,S_\sigma\setminus U],\qquad U\ne\varnothing.
\]

In words: this orientation makes its differential the usual alternating Čech differential, and \(de_\sigma=\sum_i b_{\{i\}}\).

In the ordered Koszul complex on the three occurrence coordinates, write \(e_U\) for its exterior basis. The seven-term element

\[
Z_\sigma=
\sum_{\varnothing\ne U\subseteq S_\sigma}
(-1)^{|U|(|U|+1)/2-1}
\frac{e_U\otimes b_U}{\prod_{i\in U}X_i}
\]

satisfies

\[
d_{K\otimes\mathcal P}(Z_\sigma)=1\otimes de_\sigma.
\]

In words: three singleton terms, three pair terms, and one triple term supply the entire comparison. Every denominator is allowed in its own Čech coefficient. This is a homotopy after applying the actual derived conductor operation, not a boundary of \(de_\sigma\) in P itself. Replacing coordinates by any common positive powers gives the same verified identity with those powers in the denominators and Koszul differential.

Intrinsic to B, the hyper-Tor spectral sequence has only the two homology rows q=0 and q=2. All terms of the endpoint Čech block become zero after tensoring with the conductor because they invert an occurrence. The local-cohomology triangle gives

\[
\operatorname{Tor}_{p+3}^{B}(C,\mathcal T_{S_\sigma})
\cong\operatorname{Tor}_{p}^{B}(C,A_\sigma),
\qquad p\ge0,
\]

with the left side zero for degrees below three. Consequently its first possible nonzero differential is

\[
d_3:E^3_{p+3,0}\xrightarrow{\ \cong\ }E^3_{p,2}
\qquad(p\ge0).
\]

In words: the lower occurrence-residue tower and the upper endpoint-obstruction tower cancel through a third differential. Over the regular normalization branch, the first of these is the primitive map from the top Koszul residue to the endpoint class. Over the singular alternating ring, it continues through every higher Tor degree.

Using the preceding intrinsic resolution, the ranks on either side, indexed by p, are

\[
1,\ 3,\ 12,\ 46,\ 177,\ 681,\ldots.
\]

In words: these are the branch quotient's free conductor ranks. Their disappearance in the total derived fibre is caused by the displayed differential, not by their individual vanishing. The local-cohomology triangle and the two-row spectral sequence prove the all-degree assertion; the explicit seven-term calculation fixes its ordered primitive sign.

## 5. A reverse-duality test that changes the category requirement

### 5.1 The completed affine dual forgets all 128 punctured summands

Let \(\widehat B\) be the I-adic completion. Let \(\widehat{\mathfrak D}\) be the completed relative dualizing complex previously used for the coherent source. More generally, the argument applies to any derived I-complete target complex L.

For every short occurrence x,

\[
R\operatorname{Hom}_{\widehat B}(\widehat B[x^{-1}],L)=0.
\]

In words: a derived-complete object is right orthogonal to complexes in which that occurrence is invertible. This is the defining localization test for derived completeness [M2], not a claim that the localization module is zero.

For clarity, a free telescope resolution of the localization gives the product map

\[
(a_n)_{n\ge0}\longmapsto(a_n-xa_{n+1})_{n\ge0}.
\]

Its inverse on complete coefficient modules is

\[
a_n=\sum_{k\ge0}x^k b_{n+k}.
\]

In words: the series converges in the existing occurrence-adic completion. The inverse is unique by separation. The checker verifies its exact finite-precision identities; this convergent formula proves the infinite statement. Further long localizations in the first argument do not change the orthogonality, by restriction–Hom adjunction.

Every one of the 128 terms in P inverts a short occurrence. P is bounded, so

\[
\widehat P\ne0,
\qquad
R\operatorname{Hom}_{\widehat B}(\widehat P,\widehat{\mathfrak D})=0.
\]

In words: the full completed punctured complex is nonzero, but its completed affine coefficient dual is zero.

Dualizing the actual exact sequence therefore gives an equivalence

\[
R\operatorname{Hom}_{\widehat B}(\widehat F_0,\widehat{\mathfrak D})
\xrightarrow{\ \simeq\ }
R\operatorname{Hom}_{\widehat B}(\widehat F,\widehat{\mathfrak D}).
\]

In words: this functor cannot distinguish the jet-visible target from the target containing the seventeen closure equations and all the lower punctured residues. Using this equality as a physical comparison would discard the precise information the preceding steps recovered.

This does not contradict coherent biduality. P has noncoherent localization and local-cohomology data; it is outside the bounded coherent category on which the dualizing functor is an anti-equivalence [M3]. The earlier finite/coherent source comparisons remain in their stated domain.

### 5.2 The polynomial endpoint dual and its actual local restriction

Before completion, let \(\omega_\sigma=\bigwedge^3\Omega^1_{A_\sigma/C}\), with the ordered occurrence-volume frame. Write \(U_\sigma=\operatorname{Spec}A_\sigma\setminus V(I_\sigma)\). The endpoint block is

\[
\mathcal P_\sigma\simeq R\Gamma(U_\sigma,\mathcal O)[2].
\]

In words: this placement agrees exactly with its degree-two regular class and degree-zero top residue.

Dualize the local-cohomology/open triangle. Derived completion is Hom from the extended Čech complex [M2], and completion of a finite module over this Noetherian ring is concentrated in degree zero [M4]. Therefore

\[
R\operatorname{Hom}_{A_\sigma}(\mathcal P_\sigma,\omega_\sigma[3])
\simeq\widehat\omega_\sigma/\omega_\sigma.
\]

In words: the polynomial affine endpoint dual is a nonzero formal-versus-polynomial quotient, in cohomological degree zero, carrying its full occurrence-volume line. Finite-normalization adjunction identifies this with the same component in the relative B-dual. No formal series has been admitted as a new physical transport by this calculation.

After instead working over the completed branch, the same affine Hom is zero. But on a punctured chart \(D(X_i)\),

\[
\widehat{\mathcal P}_\sigma|_{D(X_i)}
\simeq\mathcal O_{D(X_i)}[2],
\]

\[
R\mathcal Hom_{D(X_i)}
(\widehat{\mathcal P}_\sigma|_{D(X_i)},
 \widehat\omega_\sigma|_{D(X_i)}[3])
\simeq\widehat\omega_\sigma|_{D(X_i)}[1]\ne0.
\]

In words: the actual local reverse object is a nonzero volume line in cohomological degree minus one. It does not equal the localization of the zero completed affine derived Hom. The required Hom/localization base-change statement fails for this noncoherent input.

This supplies a concrete nonzero local datum for the reverse formal-punctured diagram. Its occurrence-chart restrictions are the natural volume-line restrictions. Identifying its support-changing extension and endpoint connectors with the native physical operation remains additional work; an affine-dual vanishing does not perform that work.

## 6. Consequence for native-source comparison

The original seventeen-channel test is complete for top-cycle lifting, but it is not a complete model of the punctured target. The twenty-block decomposition now supplies that model in every degree. In particular, both endpoint obstructions are tied to lower triple-occurrence residues through nontrivial attachments.

A supported operation may legitimately change the object and kill or transpose a class. Its target and variance must be stated. At the occurrence conductor, the whole endpoint Čech block has zero derived fibre even though both its homology modules have nonzero derived fibres. Under completed affine coefficient duality, the entire punctured subcomplex disappears. Neither vanishing proves that the original full target comparison was satisfied.

A reverse native comparison must retain its local punctured dual data and the formal-punctured comparison maps, or provide an independently justified functor that replaces them. The previous mapping-space gluing theorem remains the appropriate reconstruction test after every source and target is placed in its actual category. There is no newly established equality with the native source or its generic-Q/endpoint connector.

## 7. Verification and provenance

Run:

```sh
python check_marici_punctured_residue_blocks_20260907.py \
  --output marici_punctured_residue_blocks_certificate_20260907.json
```

The standalone checker passes **40,130 exact assertions**. These include all 128 basis comparisons and both inverse maps; exact localization-domain preservation; all six labelled dihedral transports; every block differential; all 3,456 homogeneous coefficient-domain types, checked independently against the Čech/long-factor homology formula; both endpoint Koszul–Čech transgressions; and the telescope identities through the stated finite orders.

The homogeneous classification is exhaustive: negative active occurrence supports give eight cases per sheet, while each long total occurrence degree has two possible nonempty domain types and each long total normal degree has three. More-negative occurrence total degrees have no terms. Larger magnitudes within a type change only monomial labels, not its differential matrix. Every nonzero Smith factor in these integer matrices is one. The symbolic block isomorphism and Čech proof establish the all-polynomial claim; completed results use flatness or the stated completeness theorem, not a monomial direct-sum assertion for arbitrary formal series.

The preceding target-obstruction checker was separately rerun and passed **68,561 assertions**. Its replay count and the input hashes are recorded. The new checker does not silently execute its predecessor. No repository files were modified, no zip bundle is required, and this is not proof-assistant certification.

### Sources

- The fixed 215-state PC differential: `research/voevodsky/check_ringed_alexandrov_pc_target.py` at the baseline commit, reconstructed in the preceding local artifact and in the new standalone checker.
- Input artifact: `marici_punctured_target_obstruction_20260907.md`, with the exact top obstruction and formal-punctured mapping-space gluing calculation.
- Input artifact: `marici_intrinsic_conductor_resolution_20260907.md`, with the integral alternating-word conductor resolution and its all-degree exactness proof.
- [M1] Stacks Project, Section 51.2, *Generalities*, tag `0DWQ`: local-cohomology and open-complement Čech triangles. https://stacks.math.columbia.edu/tag/0DWQ
- [M2] Stacks Project, Section 15.93, *Derived Completion*, tag `091N`, especially Lemmas 15.93.1, 15.93.3, 15.93.8 and 15.93.10: localization orthogonality, the telescope product, complete finite complexes, and Hom from the extended Čech complex. https://stacks.math.columbia.edu/tag/091N
- [M3] Stacks Project, Section 47.15, *Dualizing complexes*, tag `0A7A`: the precise coherent category for dualizing anti-equivalence. https://stacks.math.columbia.edu/tag/0A7A
- [M4] Stacks Project, Lemma 15.96.4, tag `0A06`: derived completion of finite cohomology over Noetherian rings. https://stacks.math.columbia.edu/tag/0A06
