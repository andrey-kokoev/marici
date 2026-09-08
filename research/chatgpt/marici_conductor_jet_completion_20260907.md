# Higher conductor jets, faithful transport, and the global endpoint obstruction

Date: 2026-09-07  
Lane: Branch B — derived coefficient sources and globally framed transport  
Baseline: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result and scope

The previous conductor marking space detected only linear occurrence tails of a globally framed shear. This note constructs all occurrence-conductor neighborhoods, their actual transition maps, and the induced action of the same global polynomial transport group.

The new conclusions are:

1. The order-m neighborhood detects occurrence terms through degree m+1. Its exact invisible subgroup consists of occurrence tails of order at least m+2. The action on the entire compatible tower is faithful.
2. Every finite neighborhood still has nonzero higher homotopy groups in arbitrarily high dimensions. However, every successive transition is zero on those positive homotopy groups. The compatible inverse-limit marking space is discrete.
3. This discreteness does not make the completed coefficient module perfect. Its derived conductor fibre still recovers the original infinite Tor groups. Keeping the ringed module is strictly different from retaining only its underlying marking space.
4. Polynomial transport and formal transport must not be identified. The first derived inverse limit of the decreasing invisible groups records compatible formal transformations that are not single global polynomial transformations.
5. Even the whole compatible formal conductor diagram fails to determine the global endpoint extension. All its thickenings lie inside the existing central chart, where the actual residue extension splits. Its nonzero gluing class on the seven-chart open remains unchanged.

These statements concern the already specified coefficient source S14(r). They are not a new geometric support operation, not a change in Rees variables, and not an identification with the native physical normalization/PC correspondence. Both endpoint channels and all twelve other channels are retained. No extra physical inverse is admitted. The generic *coefficient* quotient used here is not silently identified with the seven-state physical Q complex.

## 1. Fixed rings, fixed source, and two independent degrees

Use the existing positive and negative occurrence labels

\[
S_+=\{13,15,35\},\qquad S_-=\{02,04,24\},\qquad L=\{03,14,25\}.
\]

In words: the two triples label occurrence sheets; the third triple labels independent long parameters. None of these is a new carrier.

Retain

\[
\mathcal C=\mathbb Z[t_s,X_l,u_l\mid s\in S_+\cup S_-,\ l\in L],
\quad \tau_+=\prod_{p\in S_+}t_p,
\quad \tau_-=\prod_{m\in S_-}t_m,
\quad T=\tau_+\tau_-.
\]

In words: the spectator ring contains all short Rees parameters and the independent long occurrence and normal parameters. Set

\[
\mathcal C_\pm=\mathcal C[\tau_\pm^{-1}],\qquad C=\mathcal C[T^{-1}].
\]

In words: these are the existing sheet rings and central-chart ring, not new global physical localizations.

On the central chart write

\[
B=C[x_1,x_2,x_3,y_1,y_2,y_3]/(x_i y_j),
\quad I_+=(x_1,x_2,x_3),\quad I_-=(y_1,y_2,y_3),\quad I=I_+\oplus I_-.
\]

In words: x and y are the two ordered occurrence triples. The ideal being thickened is I, not an ideal of the Rees t parameters. The previous normalization equations give an actual central-chart isomorphism

\[
S(r)|_{D(T)}\cong B\oplus I_+^{\oplus7}\oplus I_-^{\oplus7}.
\]

In words: subtract the fourteen actual residue coefficients times the generic coefficient. This is a B-linear triangular change on D(T); it is not a global splitting on V.

For m at least zero define

\[
B_m=B/I^{m+1},\qquad K_m=B_m\otimes_B^L S(r)|_{D(T)}.
\]

In words: m is occurrence-conductor thickness. Homological degree in K-m is an independent index. The maps from m+1 to m are induced by the actual quotient homomorphisms. This is not a Postnikov tower: increasing m does not simply add a homotopy dimension.

The central generic projection gives

\[
\mathscr X_m=\operatorname{hofib}_{1}\!\left(
\operatorname{Map}_{D(C)}(C,K_m)\longrightarrow (B_m)_{\mathrm{disc}}
\right).
\]

In words: the entire B-m-valued generic coefficient is fixed to one. Only fixing its constant term would define a different, larger marking problem. Nonnegative homological complexes give the stated spaces through Dold–Kan [M1].

## 2. The ideal fibre keeps one more occurrence order

The degree-zero derived tensor calculation is

\[
H_0(B_m\otimes_B^L I_\sigma)
=I_\sigma/I^{m+1}I_\sigma
=I_\sigma/I_\sigma^{m+2}.
\]

In words: the channel retains branch monomials of degrees one through m+1. Mixed-sheet products vanish, so the denominator is precisely the stated branch-ideal power.

This is not the image ideal inside B-m. For instance, at m=1,

\[
[x_1^2]_{B_1}=0,
\qquad
[x_1^2]_{I_+/I_+^3}\ne0.
\]

In words: the quadratic scalar vanishes in the thickened ring, but the corresponding ideal-module class does not.

An explicit ideal-resolution representative is

\[
x_1[x_1]\in B_1\otimes_B Q_{+,0}.
\]

In words: its coefficient is linear, its labelled generator contributes the second occurrence order, and its augmentation is the nonzero ideal class x-one squared. The checker proves it is not a boundary using the integral homology projector below.

The normalized marking components therefore form

\[
\pi_0(\mathscr X_m)
\cong
(I_+/I_+^{m+2})^{\oplus7}\oplus
(I_-/I_-^{m+2})^{\oplus7}.
\]

In words: these are free C-modules of total rank fourteen times the number of nonconstant monomials of degree at most m+1 in three variables. All channel grading and endpoint labels remain available.

## 3. An explicit homology projector at every thickness

Use the preceding all-degree conductor resolution. Its words are alternating nonempty exterior blocks, with differential acting on the first block. Let Q-sigma be the unaugmented ideal resolution: its degree-i basis consists of words of total length i+1 ending on sheet sigma. The differential of singleton words is zero in this unaugmented complex; its separate augmentation sends [i] to X-i.

For a nonconstant coefficient monomial M, the integral contraction h selects the least occurrence in the union of the coefficient support and the first block on the same sheet. When that least label is not already in the block, h moves one copy of it from the coefficient to the block, with the exterior insertion sign. Otherwise h is zero. For constant coefficients h is zero. It is C-linear, not B-linear. All divided monomials remove an already present factor, so no localization is involved.

For the untruncated ideal resolution let epsilon denote its augmentation and let s choose the least-divisor representative of a branch monomial. Then

\[
dh+hd=1-s\epsilon,\qquad h^2=0.
\]

In words: this is the previous integral contraction, now used without destroying the ideal's degree-zero augmentation.

Reduce coefficients modulo I to the power m+1 and denote the differential by d-m. Define

\[
E_m=1-d_mh-hd_m.
\]

In words: use exactly the existing contraction; it lowers coefficient order and therefore is defined on each truncated complex. For every degree,

\[
E_m^2=E_m,\qquad d_mE_m=0,\qquad E_md_m=0.
\]

In words: this is an actual chain retraction onto a zero-differential integral direct summand. It identifies all homology, including its integral coefficient structure.

Its description is particularly simple. In degree zero it is s-epsilon. In positive homological degree, it is zero on coefficient monomials of degree less than m. On the top allowed coefficient degree m it is

\[
E_m(v)=h\,d(v),
\]

where the d on the right is computed before coefficient truncation. In words: the boundary that would have occupied the next coefficient order is contracted back into the top slice.

Proof: the untruncated contraction is the identity in positive degree. Below the top coefficient slice the reduction does not alter either term. On the top slice d-m of v is zero, but d-m of h(v) equals the full d of h(v), because h lowers coefficient degree. The original contraction identity then yields the formula. The projector equations follow either from these formulas and d-squared equal to zero, or from h-squared equal to zero and h d-m h equal to h. In degree zero d h is unchanged by truncation, giving s-epsilon.

This establishes an all-order, all-homological-degree result. The image of each finite integer projector is a direct summand of a finite free abelian group, hence free. Base change to C therefore gives free C-homology, with no hidden integer torsion. The checker constructs the same projectors on all recorded basis columns and independently performs integral unit-pivot reductions on complete small homogeneous differential blocks.

## 4. Exact ranks and the transition maps

Let b-i be the ideal-resolution ranks. They are determined by

\[
\sum_{i\ge0}b_i z^i
=\frac{3+3z+z^2}{1-3z-3z^2-z^3},
\qquad (b_0,b_1,b_2,b_3)=(3,12,46,177).
\]

In words: these are ranks for one labelled branch-ideal channel. Define

\[
h_0=1,\qquad h_k=2\binom{k+2}{2}\quad(k\ge1).
\]

In words: h-k counts coefficient monomials of degree k in the two-sheet occurrence ring.

For i at least one,

\[
r_{m,i}:=\operatorname{rank}_C H_i(B_m\otimes_B^L I_\sigma)
=\sum_{j=0}^{m}(-1)^j h_{m-j}b_{i+j}.
\]

In words: count top-slice generators and subtract the exact images supplied by the untruncated linear resolution. The alternating sum terminates because coefficient degree cannot be negative.

Equivalently,

\[
r_{m,i}
=b_i\binom{m+2}{2}
+(3b_i-b_{i+1})\binom{m+1}{2}
+b_{i-1}\binom{m}{2}.
\]

In words: for fixed i the rank is a quadratic polynomial in m. The recurrence for the b-i gives this equality from the coefficient generating series. The coefficients of m-squared and m in twice this expression are positive: their initial values are respectively 5,19,73 and 23,87,335, and both obey the same positive third-order recurrence. Hence every r-m-i is positive.

For all fourteen channels the ranks are:

| Occurrence thickness m | Rank of marking components | Rank of pi-1 | Rank of pi-2 | Rank of pi-3 |
|---:|---:|---:|---:|---:|
| 0 | 42 | 168 | 644 | 2478 |
| 1 | 126 | 364 | 1386 | 5334 |
| 2 | 266 | 630 | 2394 | 9212 |
| 3 | 476 | 966 | 3668 | 14112 |
| 4 | 770 | 1372 | 5208 | 20034 |

The most important new calculation is not these larger ranks. It is the transition:

\[
t_m:K_{m+1}\longrightarrow K_m,\qquad H_i(t_m)=0\quad(i\ge1).
\]

In words: the target homology group is not zero; the induced homomorphism is zero.

Proof: every homology class at thickness m+1 has a projector representative with coefficient degree m+1. Reducing to B-m kills that representative term by term. The chain map itself is not zero, and individual contraction homotopies need not commute strictly with reduction. Only the asserted induced maps are zero. Degree-zero transition maps are the usual surjective truncations of branch polynomials.

## 5. Recover all polynomial transports, without dividing factorials

Keep precisely the prior globally framed group

\[
G=I_+[\tau_+^{-1}]^{\oplus7}\oplus I_-[\tau_-^{-1}]^{\oplus7}.
\]

In words: its elements are global polynomial occurrence tails, allowing only each sheet's already admitted normal denominators. This discrete additive group consists of automorphisms of one fixed global extension, fixing its quotient and kernel pointwise.

The central free-resolution lift of a shear f sends the generic degree-zero generator to itself plus the least-divisor lift of f in the ideal channels. It fixes all other columns. These shears compose by addition and have inverse obtained by negating f. On the normalized fibre the action is translation by that cycle.

At thickness m, its component action is

\[
v\longmapsto v+[f]_{I_\sigma/I_\sigma^{m+2}}.
\]

In words: it retains all branch Taylor coefficients through occurrence degree m+1. The projector of Section 3 fixes those chosen translation cycles; the positive-homology summand is unchanged by the action in this labelled model.

The exact kernel is

\[
G_{m+2}
=(I_+^{m+2})[\tau_+^{-1}]^{\oplus7}
\oplus (I_-^{m+2})[\tau_-^{-1}]^{\oplus7},
\qquad \bigcap_{m\ge0}G_{m+2}=0.
\]

In words: a nonzero polynomial transport is detected at a finite conductor order. A monomial of degree d is first detected at m=d-1. In particular x-one squared, invisible on the original conductor fibre, is detected at the first thickening by the ideal class from Section 2.

The intersection statement follows coefficientwise from separatedness of polynomial degree; it does not assume that every global morphism of arbitrary sheaves can be detected on a conductor. It applies to the explicitly classified shear group G.

For an integral derivative notation, use branchwise Hasse coefficients:

\[
f(X+Z)=\sum_\alpha \partial^{[\alpha]}f(X)Z^\alpha,
\qquad
\partial^{[\alpha]}f(0)=[X^\alpha]f.
\]

In words: the coefficient is extracted before any factorial division. These are the familiar divided polynomial derivatives [M2], taken on each normalization branch separately. Translation in all six variables need not preserve the singular relation x-i y-j equal to zero, so no such translation or derivation on the whole singular ring is asserted.

For example over characteristic p,

\[
\partial^{[p]}(x^p)(0)=1,\qquad
\frac{d^p}{dx^p}(x^p)=0.
\]

In words: the divided coefficient still detects the transport while the iterated ordinary derivative loses it. This introduces no new arithmetic derivative of primes and no prime torsion. The identities are valid integrally before coefficient reduction; the checker includes characteristics two, three, five, and seven.

Least-divisor chain representatives depend on the ordered labels beyond first order. Their images on the intrinsic ideal fibre do not. For each dihedral relabelling the difference of the two representatives has zero augmentation, and its explicit comparison homotopy is h applied to that difference. This is checked before and after thickening. Functorial derived tensor preserves the underlying relabelling action; no independently reconstructed spatial dihedral comparison is claimed here.

## 6. Finite action groupoids and their complete limit

For a fixed globally framed source let

\[
\mathcal Y_m=\mathscr X_m//G.
\]

In words: take the homotopy quotient by the same discrete global polynomial transport group at every thickness. Only the coefficient neighborhood changes.

There are binomial(m+4,3) minus one monomials in each channel's component module. Put

\[
N_m=7\left(\binom{m+4}{3}-1\right).
\]

In words: N-m is the number of coordinates per occurrence sheet, retaining the seven channel labels. Then

\[
\pi_0(\mathcal Y_m)
\cong(C/\mathcal C_+)^{N_m}\oplus(C/\mathcal C_-)^{N_m}.
\]

In words: global transport removes exactly the coefficients regular on that normalization sheet. These are additive quotients, not quotient rings or generally C-modules.

At a chosen component and basepoint, the chain-level translation model gives

\[
\pi_1(\mathcal Y_m)\cong C^{14r_{m,1}}\oplus G_{m+2},
\qquad
\pi_i(\mathcal Y_m)\cong C^{14r_{m,i}}\quad(i\ge2).
\]

In words: the invisible global shears are stabilizer loops. The indicated product splitting uses the labelled central model and the actual translation cycles. Triviality on homology alone would not have proved such a product.

For the compatible inverse limit, Sections 3–4 show that all positive-degree homology systems have zero successive maps, and the degree-zero system is surjective. Their first derived inverse limits vanish. The derived-limit cohomology sequence therefore gives

\[
R\!\varprojlim_m K_m\simeq\widehat S(r),
\qquad H_i(\widehat S(r))=0\quad(i\ne0).
\]

In words: this is ordinary occurrence-adic completion of the finite coefficient module, concentrated in degree zero. The conclusion also follows from the Noetherian derived-completion theorem [M3], but the explicit zero-transition calculation proves more about this particular tower.

Let

\[
\widehat I_{+,C}=(x_1,x_2,x_3)C[[x_1,x_2,x_3]],
\qquad
\widehat I_{-,C}=(y_1,y_2,y_3)C[[y_1,y_2,y_3]],
\]

\[
\widehat M_C=\widehat I_{+,C}^{\oplus7}\oplus\widehat I_{-,C}^{\oplus7}.
\]

In words: retain formal occurrence series with their labelled channel coefficients in the central ring. Normalizing the completed generic coefficient to one yields

\[
\varprojlim_m\mathscr X_m\simeq(\widehat M_C)_{\mathrm{disc}}.
\]

In words: the compatible complete marking space has no positive homotopy groups, despite the unbounded groups at every finite stage. It is not the same object as the original conductor fibre.

For the quotient, all transition maps lie over the identity of BG. Limits of these action fibrations retain the same base and the inverse-limit fibre; equivalently this is the limit of the equivariant spaces followed by their associated fibration. Thus

\[
\varprojlim_m\mathcal Y_m\simeq\widehat M_C//G
\simeq(\widehat M_C/G)_{\mathrm{disc}}.
\]

In words: G acts faithfully by translations on the completed markings. The action is free, so there are no remaining stabilizer loops. G has not been replaced by its formal completion.

### What the completed marking space does not assert

The completed B-module is still nonperfect. Completing the finite-coefficient free resolution is exact over the Noetherian ring and gives a free resolution over the completed ring. Derived restriction to its conductor gives

\[
C\otimes_{\widehat B}^{L}\widehat S(r)
\simeq C\otimes_B^L S(r).
\]

In words: all original infinite Tor groups return. Discreteness of the underlying completed marking space does not erase this derived module structure. The ringed completed object can recover its derived jets; its underlying C-valued marking groupoid cannot stand in for that object. No physical source is replaced by a discrete module in this argument.

## 7. The first derived inverse limit measures formal, nonglobal transport

There is a separate inverse-limit effect in the decreasing stabilizer groups. Let

\[
\widehat G=
\bigl((x_1,x_2,x_3)\mathcal C_+[[x_1,x_2,x_3]]\bigr)^{\oplus7}
\oplus
\bigl((y_1,y_2,y_3)\mathcal C_-[[y_1,y_2,y_3]]\bigr)^{\oplus7}.
\]

In words: this is completion of the actual polynomial group in occurrence order; it is not an admitted enlargement of it. The short exact sequence of towers with constant middle term G yields

\[
R^1\!\varprojlim_m G_{m+2}\cong\widehat G/G.
\]

In words: coherent finite polynomial transformations can fail to come from one polynomial transformation. The derived-limit exact sequence [M4] computes exactly their difference.

An explicit example is

\[
f_m=x_1+x_1^2+\cdots+x_1^{m+1}.
\]

In words: every finite jet is an allowed positive-sheet polynomial. Consecutive choices differ by an invisible term of the preceding stage. No single polynomial has all these coefficients. The limiting formal series is not promoted to a global physical transport.

Indeed its completed marking is in the zero orbit at each finite thickness, but it is not in the G-orbit of zero at infinite thickness. Hence

\[
0\longrightarrow\widehat G/G
\longrightarrow\pi_0(\varprojlim_m\mathcal Y_m)
\longrightarrow\varprojlim_m\pi_0(\mathcal Y_m)
\longrightarrow0.
\]

In words: taking components first loses the formal-versus-polynomial distinction. The exact sequence can also be read coefficientwise: arbitrary formal series modulo polynomials map to formal series of opposite-normal coefficient cosets, with the displayed kernel.

This is not the original endpoint Ext class and is not integer torsion. It is a completion obstruction to finding one member of the specified polynomial transport group.

## 8. Every formal neighborhood is still blind to the global endpoint attachment

The seven-chart open is

\[
V=\operatorname{Spec}\mathcal B\setminus V(T,\tau_+I_+,\tau_-I_-).
\]

In words: the same test open as in the previous calculations is retained. On any occurrence chart an occurrence in I is invertible. Therefore

\[
(\mathcal O_V/I^{m+1})|_{D(\tau_+X_p)}=0,
\qquad
(\mathcal O_V/I^{m+1})|_{D(\tau_-X_q)}=0.
\]

In words: every conductor neighborhood, including its derived restriction of S(r), is supported in D(T). The vanishing follows by localization at a nilpotent element; it is not a new deletion of target states.

On D(T), all fourteen residue coefficients belong to C. The same triangular change works at every order and in the formal limit:

\[
(b,z_j)\longmapsto(b,z_j-r_jb).
\]

In words: it fixes the generic quotient and every kernel channel, and changes the actual residue extension to the split local model. All reductions of this single map agree. Consequently any two global sources S(r) and S(r-prime) have equivalent complete derived formal conductor diagrams under those frames.

Nevertheless the original global extension components remain

\[
(C/\mathcal C_+)^{7}\oplus(C/\mathcal C_-)^{7}.
\]

In words: a globally defined branch coordinate change may shift a residue only by a conductor value regular on its own full sheet. This is the previous normalization and first-cohomology calculation; extension classes are classified by first cohomology [M5].

For the two actual endpoint entries,

\[
r_+=\frac{U_L}{\tau_-},\qquad r_-=\frac{U_L}{\tau_+},
\qquad U_L=u_{03}u_{14}u_{25},
\]

\[
[r_+]_{C/\mathcal C_+}\ne0,
\qquad
[r_-]_{C/\mathcal C_-}\ne0.
\]

In words: each has an opposite-sheet denominator unavailable globally. The independent long-normal numerator cannot cancel that pole. Removing the endpoint attachments therefore changes the global framed extension component, although no formal conductor neighborhood detects that change.

The conclusion is sharper than a ranks-only warning: even the entire compatible, ringed derived conductor tower with its actual global-polynomial action fails to classify the global source. The comparison after completion is B-linear and fixes the channels; it is not merely an equality of homotopy-group dimensions.

Faithfulness on *automorphisms of one fixed source* is compatible with failure to distinguish *different global sources*. These are different tests. Neither licenses deletion of an endpoint or identifies the coefficient source with the native physical kernel.

## 9. Classify a global source together with a formal conductor frame

There is a useful exact presentation of the remaining global-to-formal comparison. The globally framed extension groupoid is presented by residue objects r in C to the fourteenth power and arrows from

\[
F=\mathcal C_+[x_1,x_2,x_3]^{7}\oplus
\mathcal C_-[y_1,y_2,y_3]^{7}.
\]

In words: a branch polynomial shifts its residue by its constant term. The stabilizer is the positive-tail subgroup G.

The formally completed extension groupoid has only one extension component, with automorphism group hat-M-C. In the fixed central trivializations a global arrow f acts on the formal frame by its positive part f minus f-at-zero. This follows by composing the actual triangular normalization maps, not by identifying their signatures.

The homotopy fibre over a fixed formal split model is discrete and has components

\[
\bigoplus_{\sigma\in\{+,-\}}
\left(C[[X_\sigma]]/\mathcal C_\sigma[X_\sigma]\right)^{7}.
\]

In words: a global extension with a chosen compatible formal frame is classified by a full formal branch series modulo a globally regular polynomial. The quotients are additive. To verify this directly, combine the residue constant and the positive formal frame into one formal series; a global arrow changes it by exactly f. The only arrow fixing both constant and every positive coefficient is zero, so all stabilizers vanish.

Constant-term projection gives the exact sequence

\[
0\longrightarrow\widehat M_C/G
\longrightarrow
\bigoplus_\sigma
\left(C[[X_\sigma]]/\mathcal C_\sigma[X_\sigma]\right)^7
\longrightarrow
\bigoplus_\sigma(C/\mathcal C_\sigma)^7
\longrightarrow0.
\]

In words: the left term measures the formal marking/frame freedom for one fixed source; the right term measures the actual global extension, including the endpoints. This separates rather than conflates the two obstructions.

## 10. Verification, provenance, and limits

Run:

```sh
python check_marici_conductor_jet_completion_20260907.py \
  --output marici_conductor_jet_completion_certificate_20260907.json
```

The default run passes **1,678,576 exact assertions**. It checks all occurrence thicknesses zero through four, both occurrence sheets, and homological degrees zero through four. It verifies square-zero differentials, the explicit integral projectors, their homology supports, their integral traces/ranks, and the zero maps on positive homology under every successive tested reduction. It independently checks complete small integral differential blocks with unit pivots.

The action audit retains every one of the fourteen channel labels, including the two endpoints. It checks exact action kernels on polynomial monomials beyond the tested thickness, strict additive composition, inverse identities, and all reduction maps. It also checks branchwise Hasse identities, factorial-failure controls in positive characteristic, and explicit syzygy homotopies for the six dihedral relabellings. It does not claim that pairwise tests alone geometrize all native dihedral coherence.

The formal and global assertions have algebraic proofs in Sections 6–9. Finite formal-series prefixes are only tests of those formulas, not a proof that every limit has been enumerated. Likewise the Laurent-domain audit checks coefficient patterns; global nonvanishing follows from the normalization-ring divisibility argument, not from a finite table.

The predecessor `check_marici_conductor_yoneda_and_global_frames_20260907.py` was independently rerun with its default settings, passing 3,164,764 exact assertions. The new checker records that replay's hash when the replay file is present; it does not rerun it internally. The new script's hash, the predecessor note's hash, the detailed per-family counts, and the finite bounds are in the new certificate.

No proof assistant was run, no repository was changed, and no physical or analytic equality is inferred. The mathematical constructions are reproducible over the retained integral spectator ring. Completion is a diagnostic object, not an additional physical admissibility rule.

## References and input artifacts

[M1] Stacks Project, *Dold–Kan*, tag 019D. `https://stacks.math.columbia.edu/tag/019D`

[M2] Official mathlib documentation, *Polynomial.HasseDeriv*: integral coefficient formula, composition, and product law. `https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/HasseDeriv.html`

[M3] Stacks Project, *Derived completion for Noetherian rings*, tag 0BKH; especially Lemma 15.96.4, tag 0A06, and the finite-module consequence in tag 0EEU. `https://stacks.math.columbia.edu/tag/0BKH` and `https://stacks.math.columbia.edu/tag/0A06`

[M4] Stacks Project, *Rlim of abelian groups*, tag 07KV: the derived-limit exact sequence and inverse-limit cohomology formula. `https://stacks.math.columbia.edu/tag/07KV`

[M5] Stacks Project, *First cohomology and extensions*, tag 0B39. `https://stacks.math.columbia.edu/tag/0B39`

Project inputs: `marici_conductor_yoneda_and_global_frames_20260907.md`, `marici_intrinsic_conductor_resolution_20260907.md`, and the complete fourteen-residue normalization source from the preceding Branch B constructions. This note extends those specified coefficient objects. It neither replaces nor assumes an independently constructed Branch A or Branch C support-changing map.
