# Formal conductor gluing that retains the endpoint attachment

Date: 2026-09-07  
Lane: Branch B — coefficient sources, intrinsic conductor towers, and global comparisons  
Baseline: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result and exact scope

The preceding formal conductor tower was a faithful test of polynomial shears of one fixed source, but could not distinguish different global endpoint extensions. Here the missing comparison is constructed: retain the completed conductor module, the source on the occurrence complement, and their actual maps on the punctured spectrum of the completed ring.

For the specified fourteen-channel framed extension problem, this produces a complete reconstruction, not just another necessary test. Every formal overlap vector has an explicit constant-residue normal form. Its fourteen constants, modulo the functions extendable to the two algebraic sheets, recover exactly the original global extension classes. Both genuine endpoint attachments are detected.

The construction also computes the full derived global-sections complex of the ambiguity sheaf. Besides its known degree-one residues, it has degree-three classes combining opposite-normal poles with three occurrence poles. These are sheaf cohomology classes, not new third homotopy groups of the old extension groupoid.

A further distinction is necessary for the actual PC target: flat base change to the completed ring is not the same as taking its occurrence-jet limit. Of the 215 original coefficient summands, 128 are nonzero after flat base change but zero at every finite conductor jet. They must be retained in the gluing comparison. This is a summand count, not a claim that 128 cohomology classes disappear.

The construction stays in the already specified coefficient category. It does not identify the target-selected normalization source with the native physical source, identify the mathematical occurrence complement with the physical generic deformation, or supply a new spatial Gysin correspondence. No physical inverse, endpoint cell, or normalization rule is added.

## 1. The fixed rings and opens

Keep the labelled triples

\[
S_+=\{13,15,35\},\qquad S_-=\{02,04,24\},\qquad L=\{03,14,25\}.
\]

In words: the first two triples label the occurrence sheets; the long parameters remain independent.

Write

\[
\mathcal C=\mathbb Z[t_s,X_l,u_l\mid s\in S_+\cup S_-,\ l\in L],\quad
\tau_\pm=\prod_{s\in S_\pm}t_s,\quad T=\tau_+\tau_-,
\]

\[
\mathcal C_\pm=\mathcal C[\tau_\pm^{-1}],\qquad C=\mathcal C[T^{-1}].
\]

In words: these are precisely the prior spectator, sheet, and central coefficient rings. The displayed localizations describe the existing mathematical test open, not newly allowed native physical poles.

Set

\[
\mathcal B=\mathcal C[X_s:s\in S_+\cup S_-]/(X_pX_m:p\in S_+,m\in S_-),
\quad I_\pm=(X_s:s\in S_\pm),\quad I=I_++I_-.
\]

In words: products crossing the two occurrence sheets vanish. The conductor ideal being completed is the occurrence ideal I, not an ideal of Rees parameters.

The existing open and its occurrence complement are

\[
V=D(T,\tau_+I_+,\tau_-I_-),\qquad Z=V\cap V(I),\qquad U=V\setminus Z.
\]

In words: Z is the occurrence conductor inside the already chosen seven-chart open. It lies entirely in the central chart D(T).

Use x for the ordered positive occurrence triple and y for the negative one. Then

\[
B=\mathcal B[T^{-1}]=C[x_1,x_2,x_3,y_1,y_2,y_3]/(x_i y_j),
\]

\[
U=U_+\sqcup U_-,\qquad
U_\sigma=\operatorname{Spec}(A_\sigma)\setminus V(X_\sigma),\qquad
A_\sigma=\mathcal C_\sigma[X_\sigma].
\]

In words: away from the conductor the sheets separate. Each is a three-occurrence punctured affine scheme. All same-sheet double and triple intersections remain; the two punctured sheets have no mutual intersection.

The coefficient source fits into the existing exact sequence

\[
0\longrightarrow\mathcal M\longrightarrow\mathcal S(r)
\xrightarrow{\rho}\mathcal O_V\longrightarrow0,\qquad
\mathcal M=\mathcal I_+^{\oplus7}\oplus\mathcal I_-^{\oplus7}.
\]

In words: the fourteen kernel channels include both endpoint channels, each with its original label and degree. The quotient is the generic coefficient; it is not silently identified with the complete seven-state physical Q complex.

## 2. Construct the correct formal overlap

The completed central ring is

\[
\widehat B=\varprojlim_n B/I^n
=C[[x_1,x_2,x_3]]\times_C C[[y_1,y_2,y_3]].
\]

In words: the two formal power-series branches share their constant term. Completing is done on the existing central chart after its specified spectator localization.

Put

\[
\widehat V_{\rm alg}=\operatorname{Spec}\widehat B,\qquad
W=\widehat V_{\rm alg}\times_V U
=\operatorname{Spec}\widehat B\setminus V(I\widehat B).
\]

In words: use the punctured spectrum of the completed ring. It is not a topological puncture of the formal scheme Spf, whose underlying points lie on the conductor. It has two branches

\[
W_\sigma=\operatorname{Spec}(H_\sigma)\setminus V(X_\sigma),
\qquad H_\sigma=C[[X_\sigma]].
\]

In words: each punctured completed sheet is covered by its three occurrence localizations, with their pair and triple overlaps.

This overlap cannot be obtained by first truncating and then puncturing. For every finite n,

\[
(B/I^n)[x_i^{-1}]=0,
\qquad
\widehat B[x_i^{-1}]\ne0.
\]

In words: an invertible nilpotent forces the finite ring to be zero; the completed branch localization is a nonzero ring. Thus localization does not commute with this inverse limit. Discarding W would repeat the very loss of endpoint data that the preceding formal calculation detected.

The ring B is Noetherian, the map to its completion is flat, and the maps modulo I agree. These are the hypotheses of formal module gluing [M1, M2]. Hence modules and actual maps on the central chart are recovered from their flat base change to the completed ring, their restrictions to the occurrence principal opens, and their compatible overlap maps. This applies to nonperfect finite modules; no perfectness assumption is inserted.

For the global V, apply this theorem on D(T) and ordinary localization descent on U. Their overlap is precisely the one already displayed. Consequently a coherent module on V is reconstructed from the formal factor, its restriction to U, and the complete comparison on W. The theorem also preserves exact diagrams and their morphisms.

For an actual coefficient complex M there is a corresponding natural reconstruction

\[
R\Gamma(V,M)\simeq
\operatorname{fib}\!\left(
R\Gamma(U,M|_U)\oplus(M|_{D(T)}\otimes_B^L\widehat B)
\longrightarrow R\Gamma(W,M_W)
\right).
\]

In words: subtract the two restriction maps on the completed puncture and keep their homotopy fibre. The formal factor here is flat base change. For a finite coherent module it agrees with completion; that agreement is not assumed for arbitrary localization modules.

On an affine chart this formula follows from the quasi-isomorphism of extended Cech complexes in formal gluing [M1]. Those complexes have bounded flat terms. Tensoring preserves their comparison, so the formula also applies to the bounded-flat PC diagram. It does not require identifying a naive fibre product of arbitrary unbounded derived categories.

## 3. The actual source becomes an explicit bridge matrix

In the formal factor the source splits as

\[
\widehat{\mathcal S}(r)\cong
\widehat B\oplus\widehat I_+^{\oplus7}\oplus\widehat I_-^{\oplus7}.
\]

In words: subtract the residue vector times the generic coefficient, exactly as in the previous formal tower. The ideal summands, not their images in finite quotient rings, are retained.

On each punctured sheet the corresponding ideal becomes the structure sheaf, so

\[
\mathcal S(r)|_{U_\sigma}\cong\mathcal O_{U_\sigma}^{\oplus8}.
\]

In words: keep its generic coordinate and seven sheet channels. With these fixed local frames the overlap map is

\[
\phi_{b,\sigma}(a,m)=(a,m+b_\sigma a),\qquad
\phi_{b,\sigma}=
\begin{pmatrix}1&0\\ b_\sigma&1_7\end{pmatrix},
\quad b_\sigma\in H_\sigma^{\oplus7}.
\]

In words: the formal generic coordinate acquires the actual sheet residue on the overlap. For our source the bridge b is the existing Laurent vector r, constant in occurrences. Arbitrary formal b describes the full framed gluing problem with these local factors.

The three occurrence coordinates form a regular sequence on both A-sigma and H-sigma. The punctured Cech calculation gives

\[
\Gamma(U_\sigma,\mathcal O)=A_\sigma,\qquad
\Gamma(W_\sigma,\mathcal O)=H_\sigma,
\qquad
H^1(U_\sigma,\mathcal O)=H^1(W_\sigma,\mathcal O)=0.
\]

In words: regular functions extend across each missing codimension-three origin, and there is no first-cohomology ambiguity in choosing these local splittings. The higher punctured cohomology is retained below rather than declared zero [M3, M4].

A frame-preserving coordinate change is a shear. Write u-sigma for its algebraic-sheet coefficient and h-sigma for its formal ideal coefficient:

\[
u_\sigma\in A_\sigma^{\oplus7},\qquad
h_\sigma\in\widehat I_\sigma^{\oplus7},\qquad
b'_\sigma=b_\sigma+u_\sigma-h_\sigma.
\]

In words: the formula is the exact compatibility square for the two coordinate changes. Formal shears have zero occurrence constant; punctured-sheet shears may have a constant, but that constant must lie in the sheet ring C-script-sigma. The group law is addition, and inverses are negation.

Every formal vector b decomposes uniquely into its constant and positive-occurrence part. Choosing h to be the positive part gives

\[
b_\sigma\sim b_\sigma(0).
\]

In words: there is an actual formal coordinate change reducing the bridge to its fourteen constant residues. This is valid for arbitrary formal series, not only bounded polynomial jets.

Two such constant bridges are equivalent exactly when

\[
r'_{\sigma,N}-r_{\sigma,N}\in\mathcal C_\sigma
\quad\text{for every labelled channel }(\sigma,N).
\]

In words: their difference must extend over the entire corresponding algebraic sheet. This supplies a necessary and sufficient coefficient comparison test, not merely a nonvanishing detector.

Conversely, every residue vector r already has the coherent normalization-pullback source constructed earlier. Thus every bridge in this framed problem algebraizes explicitly, by removing its positive formal tail and using that source. Formal gluing does not choose r; it classifies it.

## 4. Compute the gluing groupoid, with all transports retained

Let

\[
\mathcal H=H_+^{\oplus7}\oplus H_-^{\oplus7},
\quad
\mathcal A=A_+^{\oplus7}\oplus A_-^{\oplus7},
\quad
\mathcal F=\widehat I_+^{\oplus7}\oplus\widehat I_-^{\oplus7}.
\]

In words: these are overlap functions, algebraic sheet shears, and formal ideal shears. Their action is the bridge equation above. Define

\[
\mathfrak G_{\rm glue}=\mathcal H//(\mathcal A\oplus\mathcal F).
\]

In words: the objects are full overlap bridges, arrows are compatible two-sided shears, and higher simplices retain their composition. This is an ordinary action groupoid viewed as an infinity-groupoid. It is not a replacement for the ringed source's unbounded derived conductor fibre.

The exact additive sequence is

\[
0\longrightarrow G\longrightarrow\mathcal A\oplus\mathcal F
\xrightarrow{(u,h)\mapsto u-h}\mathcal H
\xrightarrow{b\mapsto[b(0)]}\mathcal E\longrightarrow0,
\]

\[
G=(I_+\mathcal C_+[X_+])^{\oplus7}\oplus
(I_-\mathcal C_-[X_-])^{\oplus7},
\qquad
\mathcal E=(C/\mathcal C_+)^{\oplus7}\oplus(C/\mathcal C_-)^{\oplus7}.
\]

In words: the stabilizers are exactly the original polynomial global shears; the components are exactly the original global residue-extension classes. The quotients here are additive, or modules over the appropriate unlocalized spectator ring. They are not quotient rings or unrestricted C-modules.

The sequence proves

\[
\pi_0(\mathfrak G_{\rm glue})=\mathcal E,
\qquad
\pi_1(\mathfrak G_{\rm glue},r)=G,
\qquad
\pi_n(\mathfrak G_{\rm glue},r)=0\quad(n\ge2).
\]

In words: the formal-punctured bridge groupoid recovers the complete framed extension groupoid. Its one-type does not imply that the coefficient module is perfect: derived conductor restriction still has the all-degree alternating-word resolution.

This is a positive reconstruction statement beyond the earlier warning. The formal tower alone is insufficient; the formal factor plus the actual punctured-sheet objects and their bridge is sufficient for this coefficient category.

### Both actual endpoints are recovered

The two endpoint entries are

\[
r_{+,S_-}=\frac{U_L}{\tau_-},\qquad
r_{-,S_+}=\frac{U_L}{\tau_+},\qquad U_L=u_{03}u_{14}u_{25}.
\]

In words: their opposite-sheet normal poles and independent long-normal numerator remain unchanged.

They define nonzero elements of the two respective summands of E. Formal ideal shears cannot alter their occurrence constants; algebraic sheet shears cannot introduce the required opposite-sheet poles. Therefore the genuine source and the endpoint-deleted source remain inequivalent in this reconstructed groupoid, even though their formal factors are equivalent.

For comparison of any two candidate bridges b and b-prime, the constructive test is to take their fourteen occurrence constants and subtract them modulo the two sheet rings. When the classes vanish, choose u to be the constant difference and h to be the remaining formal difference. These are explicit compatible frame-preserving maps. When an endpoint class is nonzero, no compatible such map exists.

This conclusion concerns generic-quotient and labelled-kernel frames. Fixing the entire map to the 215-state target is stronger and removes the previously classified nontrivial global shears. The formal gluing theorem transports that stronger arrow condition as well; agreement only on its generic coefficient does not impose it.

## 5. Polynomial-versus-formal transport is resolved by the punctured side

A globally compatible automorphism has h=u on W. Since u is a regular function on the whole punctured algebraic sheet, the extension-of-functions calculation forces it to be a polynomial in A-sigma. Since h lies in the formal ideal, its constant term is zero. Thus the formal tail is forced back into G.

The prior example

\[
f=\frac{x_1}{1-x_1}=x_1+x_1^2+x_1^3+\cdots
\]

is a legal formal ideal shear but is not a compatible global shear. In words: it has a pole at the allowed punctured-sheet point x-one equal to one. Algebraically an identity (1-x-one)p=x-one with p polynomial would give zero equal to one after evaluating x-one at one.

Its polynomial truncations are still allowed separately. For every n,

\[
(1-x_1)(x_1+\cdots+x_1^n)-x_1=-x_1^{n+1}.
\]

In words: each finite-order approximation passes its jet test, while the actual overlap requires an algebraic regular function at all punctured-sheet points. Formal gluing does not enlarge the physical transport group to arbitrary power series.

## 6. Retain the entire derived gluing complex

For one channel define

\[
\mathcal C_\sigma^\bullet=
\operatorname{fib}\!\left(
\widehat I_\sigma[0]\oplus
\check C^\bullet(A_\sigma;X_{\sigma,1},X_{\sigma,2},X_{\sigma,3})
\longrightarrow
\check C^\bullet(H_\sigma;X_{\sigma,1},X_{\sigma,2},X_{\sigma,3})
\right).
\]

In words: keep the three principal opens, their three pair intersections, and their triple intersection on both the algebraic and completed sides. The map on formal ideal sections is inclusion into the punctured formal functions. The map between punctured complexes is coefficient localization and completion, not a fitted coefficient projection.

This computes R-Gamma of the actual ideal sheaf I-sigma on V. At each monomial mode, it is isomorphic term by term to the original seven-chart Cech complex restricted to this ideal: the central vertex is the formal ideal term, intersections not containing it are algebraic puncture terms, and intersections containing it are the shifted formal puncture terms. The signs are the same alternating-cover signs.

The result is

\[
H^q(V,\mathcal I_\sigma)=
\begin{cases}
I_\sigma\mathcal C_\sigma[X_\sigma],&q=0,\\
C/\mathcal C_\sigma,&q=1,\\
0,&q=2,\\
\displaystyle\bigoplus_{\alpha_1,\alpha_2,\alpha_3\ge1}
(C/\mathcal C_\sigma)X_\sigma^{-\alpha},&q=3,\\
0,&q\ge4.
\end{cases}
\]

In words: the full gluing complex has the old polynomial automorphisms and residue extensions, zero degree-two cohomology, and an additional degree-three family requiring all three occurrence poles. For all fourteen channels take the corresponding labelled direct sum. No claim of a canonical direct-sum decomposition of the derived object follows from this cohomology formula.

Proof: on a three-coordinate puncture, the Cech complex has H-zero equal to its ring and H-two equal to the direct sum of monomials with all three occurrence exponents negative. All other positive cohomology vanishes. For a formal numerator and fixed localization denominator, only finitely many monomials with all three exponents negative survive, so the same finite-principal-part description works over H-sigma. The map on H-two is the injective coefficient inclusion from C-script-sigma to C. The long exact sequence of the displayed fibre gives the formula.

Equivalently, in the original cover take an occurrence Laurent exponent alpha and an opposite-normal exponent beta. There are exactly three nonzero possibilities:

- nonnegative, nonzero alpha and no forbidden opposite-normal pole give one degree-zero class;
- alpha equal to zero with an opposite-normal pole gives one degree-one class;
- all three alpha entries negative with an opposite-normal pole give one degree-three class.

Every other monomial mode is acyclic. These alternatives depend on negative supports and on whether alpha is zero, not on an exponent bound. The checker verifies the complete integral differential matrices in 6,750 exponent modes and their chain isomorphisms to the formal gluing cone. All nonzero Smith factors are one.

For instance the positive endpoint channel contains

\[
\left[\frac{U_L}{\tau_-x_1x_2x_3}\right]\ne0
\quad\text{in}\quad H^3(V,\mathcal I_+).
\]

In words: the existing opposite triple-normal pole survives together with three occurrence poles on the central-plus-triple intersection. In that exact monomial degree there is one top Cech term and no lower term that could fill it.

This is not a claim that the endpoint extension class has become a third homotopy group. The framed extension groupoid uses H-one for components and H-zero for loops [M5]. The H-three class belongs to the full derived coefficient diagram and matters only for a comparison with the corresponding degree placement. Occurrence multiplication on these principal parts follows the usual local-cohomology rule; the displayed summands describe the spectator-module decomposition, not independent B-module factors.

## 7. The actual PC target requires flat base change, not substitution of its jet limit

The absolute finite-free target and the coherent source satisfy the finite-module completion theorem. The PC target has localized coefficient summands, so the theorem cannot be applied to its individual summands as though they were finite modules over B.

A short-normal localization is, on the central chart,

\[
B[(t_sX_s)^{-1}]=B[X_s^{-1}],
\]

because t-s is already a central spectator unit. In words: its flat base change is a nonzero punctured completed branch module, while its finite occurrence jets are zero.

The complete 215-state census is:

| State-localization type | Number | After flat base change to the completed ring | At every finite occurrence jet |
|---|---:|---|---|
| No short occurrence inverted | 72 | Retained | Retained, with truncated coefficients |
| At least one short occurrence inverted, all from one sheet | 128 | Retained | Zero |
| Opposite-sheet short occurrences both inverted | 15 | Already zero in the alternating ring | Zero |

The 128 states have homological degree counts 8,54,66 in degrees zero, one, two. The 72 retained states have counts 27 and 45 in degrees two and three. Both fully marked endpoint states are in the latter group.

The checker reconstructs all these original faces and marks, all induced PC differential terms, and the comparison from flat-basechanged coefficients to their finite jets. The full and reduced differentials square to zero. The 15 zero states are not arbitrarily deleted: inverting a product X-positive times X-negative would invert zero.

This calculation does not infer cohomology from a summand census. Nor does it identify the flat base change of a localization containing only long-normal inverses with its occurrence-adic limit: even there, uniform bounds on denominators distinguish base change from unrestricted completed series. The formal gluing target is always the specified flat-basechanged module and its genuine overlaps.

Thus the correct reconstruction of the existing source-to-target map keeps both local factors and the overlap square for each target coefficient summand. The statement that the earlier fully target-framed jet marking limit is contractible is not contradicted. It concerns the jet inverse limit, not this punctured completed comparison.

## 8. Consequence for the native-source test

There is now a sufficient coefficient-level invariant rather than an endless sequence of insufficient local tests:

1. retain the ringed completed source, hence its whole intrinsic conductor resolution;
2. retain the source and the admissible polynomial maps on both punctured normalization sheets;
3. retain their full comparison on the punctured completed overlap, including both endpoint constants and all higher Cech intersections.

In this category the data reconstruct the coherent source, its exact endpoint sequence, and its maps. The analogous full-target condition must be imposed on the actual target arrow, not only its generic coefficient or residue signature.

A native physical comparison still has to produce these objects and bridges independently. Once it is typed into this coefficient category, its fourteen overlap constants can be compared with the computed r-vector, and the criterion of Section 4 decides framed coefficient equivalence. A source in another variance or degree placement must first supply the appropriate functor; the present criterion does not invent one.

The newly computed degree-three principal parts and the distinction between completed localization and finite jets are additional data for that comparison. Neither adds a carrier cell, cancels the global endpoint extension, or justifies a new physical pole.

## 9. Verification and provenance

Run:

```sh
python check_marici_formal_punctured_gluing_20260907.py \
  --output marici_formal_punctured_gluing_certificate_20260907.json
```

The standalone standard-library checker passes **292,331 exact assertions**. It checks 6,750 complete integral Cech/gluing mode comparisons, 3,456 exact framed-bridge mode sequences, the formal-shear transition equations, all fourteen residue classes and their labelled dihedral covariance, both triple-occurrence endpoint classes, and the full 215-state target census with differential compatibility.

The preceding `check_marici_conductor_jet_completion_20260907.py` was independently rerun at its default bounds. It passed **1,678,576 exact assertions**. Its replay hash and the input-note hashes appear in the new certificate. The new checker does not silently rerun a predecessor.

The all-series bridge classification and all-exponent cohomology formulas follow from the algebraic and gluing proofs above, not extrapolation from those tests. Formal module gluing is an existing theorem with its hypotheses explicitly checked here, not a newly discovered general theorem. There was no proof-assistant verification and no repository write.

## References

[M1] Stacks Project, *Formal glueing of module categories*, tag `05E5`, especially Lemmas 15.91.4 and 15.91.9, Proposition 15.91.16, and Remark 15.91.20. The flat-completion and punctured-module comparison reconstructs modules and their maps, preserving exact diagrams. `https://stacks.math.columbia.edu/tag/05E5`

[M2] Stacks Project, *Completion for Noetherian rings*, tag `0BNH`, Lemmas 10.97.1–10.97.2; flatness tag `00MB`. Completion agrees with tensor by the completed ring on finite modules, not arbitrary localization modules. `https://stacks.math.columbia.edu/tag/0BNH` and `https://stacks.math.columbia.edu/tag/00MB`

[M3] Stacks Project, *Local cohomology, Generalities*, tag `0DWQ`: the open-complement triangle and Cech realization. `https://stacks.math.columbia.edu/tag/0DWQ`

[M4] Stacks Project, *The Koszul complex*, tag `0621`: exterior signs and regular-coordinate complexes. The actual monomial-mode Cech calculation is supplied above and in the checker. `https://stacks.math.columbia.edu/tag/0621`

[M5] Stacks Project, *First cohomology and extensions*, tag `0B39`. `https://stacks.math.columbia.edu/tag/0B39`

Input constructions: `marici_conductor_jet_completion_20260907.md`, `marici_normalization_endpoint_extension_20260907.md`, and `marici_target_framed_conductor_tower_20260907.md`. Their distinction between the target-selected coefficient source and an independent native physical source remains in force.
