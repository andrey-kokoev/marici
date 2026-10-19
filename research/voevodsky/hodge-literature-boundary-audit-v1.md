# Hodge iteration 3: dated literature boundary and a nonsplit shortlist

## Disposition

`literature-boundary-audit` is completed as a **source-specific audit**, not a certification of the cited proofs or an exhaustive theorem about the state of the literature. Four documents were retrieved on 2026-10-15 UTC. Their PDFs, nine searched pages, URLs and SHA-256 hashes are retained in `research/voevodsky/inputs/hodge-literature-v1/sources.json`.

The important correction to the initial search intuition is that abelian fourfolds of Weil type are no longer a suitable unresolved rational target in these sources. Markman's 2026 survey reports algebraicity of their Weil classes for all imaginary quadratic fields and all discriminants, and deduces Hodge for abelian varieties of dimension at most five. The sixfold theorem covers **Weil classes in the split case**, not every Hodge class on every sixfold.

The primary family to investigate is therefore nonsplit Weil-type abelian sixfolds, codimension three. This is a shortlist, not a selected variety/class, and not evidence of nonalgebraicity. A split eightfold family is a reserve. Both statuses mean **unresolved in the reviewed sources**; a bounded search cannot certify global absence of subsequent results.

## How the sources were searched

The operator-requested `pnpm pdf:search` was used. The shared reference index returned no matches for `Hodge conjecture` or `Weil type`; it is not evidence of literature absence. A separate index of the four downloaded PDFs was then built with `references/build-pdf-search-index.ps1` and UTF-8 native output, without modifying the shared reference collection.

Examples:

    pnpm pdf:search 'Theorem 1.2' -IndexDirectory temp/hodge-literature-index-v1 -Book '*2509*'
    pnpm pdf:search 'semiregularity is special' -IndexDirectory temp/hodge-literature-index-v1 -Book '*2502*'
    pnpm pdf:search 'discriminant' -IndexDirectory temp/hodge-literature-index-v1 -Book '*2609*'
    pnpm pdf:search 'integrally' -IndexDirectory temp/hodge-literature-index-v1 -Book '*deligne*'

The search script's stale-index warning compares the custom manifest with PDFs in `references/`, not this separate input set. The custom index had just been built from the four retained PDFs; their own hashes and selected page texts are verified offline. It is reproducible from those PDFs, not a required untracked proof input. A broad arXiv query is retained as a search observation only; it contains irrelevant Lang-Weil results and is not a completeness certificate.

## Source boundaries

1. **Pierre Deligne, official Clay Hodge problem description**, PDF p2, https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf. The target is rational linear combinations of algebraic cycle classes on nonsingular projective complex varieties. The same page derives the divisor case from the exponential sequence and explains Atiyah-Hirzebruch integral failures. Those failures do not refute the rational conjecture. The exposition is historical; its other statements of what was unknown are not silently promoted to current status.
2. **Eyal Markman, Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds**, arXiv:2502.03415v2, PDF p9, https://arxiv.org/pdf/2502.03415v2. Theorem 1.5.1 gives algebraicity of Weil classes on sixfolds of discriminant -1 for any imaginary quadratic field. Corollary 1.6.1 deduces Hodge for abelian fourfolds. The extension to higher-genus constructions is stated, but its semiregularity proof is special to genus three.
3. **Eyal Markman, Secant sheaves and Weil classes on abelian varieties**, arXiv:2509.23403v2, updated 2026-02-11, PDF p3, https://arxiv.org/pdf/2509.23403v2. Theorem 1.2 reports the fourfold and split-sixfold Weil results. Corollary 1.3 states Hodge for all abelian varieties of dimension at most five. These are imported reported results, not the output of our finite checker.
4. **Patrick Brosnan, Discriminants of Hermitian forms, maximal degenerations and Kontsevich's tropical approach to the Hodge conjecture**, arXiv:2609.14169v1, 2026-09-12, https://arxiv.org/pdf/2609.14169v1. PDF pp3-5 describe the Weil condition, moduli and discriminant. Proposition 4, p4, gives maximal degeneration => half-dimensional K-isotropic subspace => split discriminant. Its conclusion p8 agrees.

**Source anomaly retained:** Brosnan p2 says sixfolds of discriminant -1 cannot have maximal degeneration. This contradicts his abstract, Proposition 4 and conclusion: the excluded sixfold discriminants are those **not equal to** -1. We do not use that introductory sentence as a theorem. The relevant determinant necessity also has the elementary proof below. Nor do we upgrade introductory shorthand about sixfold Hodge to a theorem about all their Hodge classes: Markman's stated result concerns the Weil classes.

## Known cases and exclusions

- Codimension one is covered by Lefschetz (1,1). Codimension d-1 follows rationally by hard Lefschetz: alpha=L^(d-2) beta with beta of type (1,1); products of the associated divisor with hyperplanes are algebraic. Together with the endpoints, this handles complex dimension at most three.
- The reported abelian dimension <=5 result is **not** a theorem for arbitrary smooth projective fourfolds or fivefolds.
- Q4's two plane families and primitive A-B remain algebraic non-divisor controls. The six middle coordinate surfaces on (P1)^4 remain positive controls. Primitivity and failure of divisor generation do not establish nonalgebraicity.
- All integral failures, torsion-only detectors, singular or nonprojective examples remain outside this rational target.
- Split sixfold Weil classes are excluded as proposed nonalgebraic candidates, while additional Hodge classes on special sixfolds require their own status review.

## Shortlist with explicit conventions

Use the **unnormalized** discriminant det(h) in Q*/Nm(K*), so a split form on K^(2n) has discriminant (-1)^n. This is not a sign-free integer invariant.

### Primary: nonsplit sixfolds

Set K=Q(i) and take the Hermitian diagonal

    h=<1,1,1,-1,-1,-3> on K^6.

It has signature (3,3) and determinant -3. The associated polarized Weil-type period family has complex dimension 9, by the standard unitary-family construction described in Brosnan p4. Its fibers are smooth projective abelian sixfolds. This specifies a family; no period/member or alpha is selected here.

Its determinant Weil subspace is

    W_K = wedge_K^6 H^1(A,Q),    dim_Q W_K=2,

viewed inside H^6(A,Q). Over C its two determinant lines have type (3,3), because the two K-eigenspaces each have three holomorphic and three antiholomorphic directions. A coordinate expression in a fixed rational marking is

    U = wedge_(j=1..6) (dx_j+i dy_j),
    R=Re U, I=Im U.

Each rational generator has 32 signed terms; they are independent. The checker verifies the pullback character of the endomorphism 1+i:

    (1+i)*R=8I,    (1+i)*I=-8R.

These formulas specify the determinant subspace without defining it as an unknown quotient by algebraic cycles. They do not prove that R or I is nonalgebraic, and are not a selection of an actual class on an actual chosen member.

### Reserve: split eightfolds

Take K=Q(i), h=<1,1,1,1,-1,-1,-1,-1>, dimension eight and codimension four. The discriminant is +1 and the determinant subspace has dimension two and type (4,4). The cited sixfold semiregularity proof does not automatically cover this case. This reserve is not declared globally open merely because one theorem fails to cover it; it requires renewed status checking before selection.

## Why -3 is genuinely nonsplit

The ratio (-3)/(-1)=3 is not a norm from Q(i). If a^2+b^2=3 with rational a,b, clear denominators to obtain a primitive integer solution A^2+B^2=3C^2. Modulo three the only way two squares sum to zero is that both are zero. Thus 3 divides A and B; the equation then forces 3 to divide C, contradicting primitivity. The checker verifies the finite residue lemma; the general rational conclusion uses this written descent proof, not a bounded search.

If an n-dimensional K-isotropic subspace exists in a nondegenerate Hermitian space of dimension 2n, extend its basis to obtain a Gram matrix

    [[0,B],[B*,C]],     det(h)=(-1)^n Nm(det B).

Hence its discriminant is the split class. The checker verifies the determinant sign on a nontrivial rational example and a split positive control. Our six-dimensional form has an explicit isotropic two-plane spanned by e1+e4,e2+e5, but the norm argument excludes an isotropic three-plane; its K-Witt index is two.

For a maximal toric degeneration of abelian sixfolds preserving K, the image of logarithmic monodromy is a K-stable isotropic subspace: weight-one N^2=0 and polarization compatibility give E(Nv,Nw)=0, and K-stability gives Hermitian isotropy. Maximal rank would mean K-dimension three, impossible here. Consequently its rational monodromy rank is at most four, not six. This uses the imported weight-one degeneration facts; no degeneration or all-cycle obstruction is constructed by the checker.

**No maximal degeneration is not no algebraic cycle.** It excludes a specific full-rank tropical method, not algebraicity of the Weil classes.

## Special-point hostile: the same discriminant can have algebraic Weil classes

On the lattice Z[i]^6 choose E=Im(h), and let J act by i on the first three coordinates and -i on the last three. The checker verifies J^2=-1, commutation with K, polarization compatibility and positive definiteness of E J. This is a product of elliptic curves, not an unresolved generic member.

Write u_j=dx_j+i dy_j. At this point u1,u2,u3 are holomorphic and u4,u5,u6 antiholomorphic. Each

    b_j = u_j wedge u_(j+3) = r_j+i s_j, j=1,2,3,

has rational real and imaginary parts of type (1,1). By Lefschetz (1,1), r_j and s_j are divisor classes. Since

    U = -b1 b2 b3,

both R and I are rational polynomials in these divisor classes and hence algebraic. The checker verifies the J-invariance and full exterior-product identity. This explicit control prevents turning a nonsplit discriminant, or its degeneration restriction, into a putative universal nonalgebraicity detector.

## Next gate and verification

The next ready node is `candidate-variety-and-class`: bind a rigorously constructed marked member or generic member and an independently specified rational Hodge class, then retain every obstruction/descent/rational-survival/all-cycle gate. Renew the family-specific literature check at binding time. The general witnessed-identity conjecture remains a methodological reference, not a proof import.

    python research/voevodsky/checkers/check_hodge_literature_boundary_audit.py

Ten checks verify the source snapshot/quotes and exact lattice/exterior controls. The necessity and norm arguments are written proofs using the declared imported standard facts. No Hodge proof, counterexample, specific target or exhaustive literature verdict is claimed.
