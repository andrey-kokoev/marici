# Prior-research clues after global iteration 30

Advisory search memo, not a new validated net iteration. No contracts, receipts, source pins, survivor counts or Hodge verdicts are changed. This search reviewed retained papers and local investigations; it is not an exhaustive or newly updated external literature survey.

## 1. Most concrete neglected constraint: use BOTH elliptic axes

The [actual principal-model construction](hodge-indecomposable-principal-model-v1.md), section 2, supplies elliptic subcurves of theta degrees **two and three**. The [latest tetragonal gate](hodge-equivariant-tetragonal-gate-v1.md) develops the degree-two axis. The degree-three axis was also used to reject scalar polarized models, but the reviewed notes do not develop its joint constraint on the remaining nonbielliptic tetragonal route.

Conditional deduction to develop and independently check: if P=Prym(C17/C9) is canonically polarized isomorphic to Y2, the degree-three axis has Jacobian theta degree six, since the Prym inclusion restricts Jacobian theta to twice the principal Prym polarization. The same norm-adjoint argument gives a degree-six map C17->Tminus, anti-invariant under the top involution up to translation. Quotienting by the elliptic reflection gives a degree-six map C9->P1 alongside the existing degree-four map. This is a second pencil, NOT a claim that gonality is six.

Their joint degree divides gcd(4,6)=2. Consequently the two elementary possibilities are:

- Joint degree one: a birational (4,6) image in P1 x P1, arithmetic genus 15, with total delta invariant 6 because its normalization has genus nine.
- Joint degree two: the normalized joint image has bidegree (2,3) and genus at most two. Genus zero or one would make C9 hyperelliptic or bielliptic, already excluded for this target. Thus this case requires a genus-two quotient of C9 of degree two.

This is a useful next classification calculation, not an exclusion of either case. Compatibility of both elliptic pullbacks, the free involution and the cyclic lift must still be imposed. Do not assume the sextic pencil is preserved by that involution, or that the deck generator preserves either chosen elliptic axis.

## 2. Exact canonical polarization is stronger than the original objective

The [stabilization reduction](hodge-split-eightfold-stabilization-v1.md) constructs algebraic forward/reverse correspondences. The [principal-model construction](hodge-indecomposable-principal-model-v1.md), sections 4-5, transports them to Y2 with the phase 48i and all four exceptional channels.

Thus failure of this particular canonical Prym polarization is not failure of every cycle route. Other principally polarized models, suitable unpolarized isogenies, and ramified/admissible constructions remain research directions. Any proposed isogeny must be actual and have a verified cycle transfer; elliptic theta degrees two and three cannot be transported unchanged across arbitrary isogenies. The 516 old unpolarized labels are necessary-condition data, not supplied isogenies.

## 3. Koike points directly to Schoen, but dominance cannot be copied

Retained primary paper: Kenji Koike, *Algebraicity of some Weil Hodge Classes*, Canadian Mathematical Bulletin 47 (2004), 566-572, DOI 10.4153/CMB-2004-055-x.

PDF page 1 credits Schoen's algebraic cycles on generalized Pryms. Its bibliography, PDF page 7, gives:

- C. Schoen, *Hodge classes on self-products of a variety with an automorphism*, Compositio Mathematica 65 (1988), 3-32.
- C. Schoen, *Addendum to Hodge classes on self-products of a variety with an automorphism*, Compositio Mathematica 114 (1998), 329-336.
- A. Beauville, *Varietes de Prym et Jacobiennes intermediaires*, Annales scientifiques de l'Ecole Normale Superieure 10 (1977), 309-391.

Next source task: inspect Schoen's construction and addendum for the precise dimension-eight cycle statement and its hypotheses, separately from the existence of a cover. The primary papers themselves were not retrieved in this search. Bibliography entries are leads, not proof imports; even bibliographic details should be checked against the originals.

Koike's retained theorem is about genus-four bottoms and sixfold Pryms. For genus-five bottoms the source dimension is 12 whereas the balanced Gaussian eightfold period domain has dimension 16. His dominance argument therefore cannot simply extend to the full eightfold domain. This does not prove avoidance by our particular special target.

## 4. Markman's higher-genus construction exists; deformation is the missing theorem

Retained Markman arXiv:2502.03415v2, PDF page 9, explicitly says Example 8.2.3 constructs higher-genus secant objects, but the semiregularity proof is special to genus three. See the [literature audit](hodge-literature-boundary-audit-v1.md) and [sixfold transplant rejection](hodge-secant-sheaf-transplant-v1.md).

A meaningful alternative project is genus-four semiregularity/deformation for the split eightfold construction. It is not licensed by the existing sixfold theorem. Changing the original sixfold's polarization or isogeny cannot repair its nonsplit norm class; stabilization changes dimension and avoids only that particular arithmetic mismatch.

## 5. Direct cycles on X remain a shorter positive criterion

The [middle Hodge kernel](hodge-middle-hodge-kernel-v1.md) and [reflexive reduction](hodge-reflexive-rank-reduction-v1.md) give concrete positive tests: a smooth threefold in X with nonzero exceptional projection, or suitable normalized third Chern data, would suffice. A pure effective Weil representative is neither required nor possible: an actual effective cycle needs a positive divisor background.

Do not keep searching divisor/graph/Poincare expressions: the all-power symmetry rejection already covers that library. A genuinely new sheaf, singularity cycle or geometric correspondence is required.

## 6. Theta and tetragonal literature: specific gaps, not existing solutions

Mumford, *Prym Varieties I*, section 7 (retained PDF page 20), gives an upper bound and an equality classification for smooth etale Pryms. It does not calculate the theta singularities of the explicit Y2 gluing. The previous bielliptic exclusion consequently leaves the necessary theta-dimension bound <=3, not an actual dimension.

A new source search should target tetragonal/bigonal Prym constructions (Recillas/Donagi), elliptic subvarieties of degree two in ppavs, and theta equations under finite isotropic gluing. No applicable theorem from those additional sources was verified here. In particular do not assert a universal theta lower bound from the degree-two axis.

## Search evidence and recommended order

Reviewed the retained Mumford section 7, Koike's introduction/bibliography and the earlier local proof notes. Ran `pnpm pdf:search` for `semiregularity` in the dedicated Markman index and `Schoen` in the dedicated Koike index. Their repository-wide stale-index warnings are not evidence of missing literature; the substantive scope above is supported by retained page text and prior source audits.

Recommended order:

1. Develop the joint tetragonal/sextic constraints from both actual axes.
2. Retrieve Schoen plus the addendum and verify the dimension-eight cycle mechanism.
3. Search tetragonal/bigonal transformations for alternative realizations or correspondences.
4. In parallel, investigate the actual gluing theta equations or a genuinely new direct sheaf/cycle on X.

None of these leads supplies a matched target cover, exceptional algebraic cycle, all-cycle obstruction or independent review.

## Shared `pnpm pdf:search` follow-up

Searched the current default shared index (45 PDFs; no freshness warning), not just the dedicated Hodge indexes:

    pnpm pdf:search -ListBooks
    pnpm pdf:search 'Prym|tetragon|Schoen|Recillas|Donagi|Weil type|Hodge conjecture' -Regex -Limit 30
    pnpm pdf:search 'semiregular|Atiyah class|Chern character|Hodge filtration' -Regex -Limit 20
    pnpm pdf:search 'Atiyah' -Book dag2 -Limit 12
    pnpm pdf:search 'algebraization|algebraisation|obstruction theory|deformation theory' -Regex -Book gaga

No direct Prym/Weil/tetragonal/Hodge-conjecture hits were returned; a separate `semiregular` search also returned none. This is a statement about the bounded shared corpus and text search, not the literature. Theta hits were largely automorphic theta correspondences or publisher names, not the target theta divisor.

Useful indirect machinery:

- **`dag2:p361` (printed p328), chapter 8 introduction, section 0.2.6:** describes the Atiyah-class obstruction/null-homotopy criterion for extending an ind-coherent object across a square-zero thickening, developed in section 6. **`dag2:p372`-`p373` (printed pp339-340)** introduces the Atiyah algebroid of a perfect complex. This provides an obstruction-theoretic framework for a supplied higher-genus secant object, but proves neither obstruction vanishing nor the required semiregularity/injectivity. It does not itself give an effective computation for our object.
- **`gaga:p4`:** Porta's proper derived GAGA comparison and Theorem 1.4 on algebraizability of a proper derived analytic space versus its classical truncation. For the existing projective X, the coherent-sheaf comparison supports an analytic-first construction followed by algebraization, if an actual coherent analytic sheaf is obtained. A formal deformation, a prescribed Chern character, or a rational Hodge class is not yet such a sheaf. Convergence/effectivity remains a separate gate.
- **`condensed-geometry:p139`, Propositions 15.1-15.2:** the refined Chern character from perfect complexes to Hochschild/Hodge cohomology is additive on cofiber sequences and agrees with the usual Chern character on vector bundles. Useful for organizing a genuine complex/correspondence and its exceptional component. No inverse or surjectivity onto rational Hodge classes is supplied.
- **`bott-chern:p28` (printed p76), equation (1.124):** alternating Chern forms of an acyclic hermitian complex are a double transgression. Useful for checking normalization, but changing metrics or adding Bott-Chern correction forms cannot manufacture a new de Rham Weil class: those corrections are exact at the relevant cohomological level.

The relevant pages were also freshly extracted from the PDFs with `pdftotext` and read; the shared normalized page text has character-encoding artifacts, so formulas should be checked in the rendered originals before implementation. Scratch page extracts are in `temp/hodge-pdf-search-clues/`.

Bottom line: the shared corpus supports the sheaf-deformation/algebraization route, not a direct solution of the remaining cover problem. The specialized Schoen/Donagi/Recillas and elliptic-theta sources still need retrieval and hypothesis checking. No validated net changes follow from this follow-up search.
