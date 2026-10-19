# Theorem audit: the control correspondence is algebraic by the retained fourfold theorem

## Fresh task and evidence boundary

Execute split-fourfold-correspondence-theorem-audit for the actual control C times A and gamma from the preceding turn. Freshly read the retained primary paper and survey statement, rather than inferring coverage from a title or an abstract. This is an applicability audit of imported results, not independent verification of their proofs or a new literature-completeness claim.

The retained source snapshot is research/voevodsky/inputs/hodge-literature-v1/sources.json, observed 2026-10-15. This turn rereads and hash-checks that snapshot's two relevant PDFs and extracted pages. It does not claim a fresh network download or verify whether later versions exist.

Reproduction search this turn:

    pnpm pdf:search 'Corollary 1.6.1' -IndexDirectory temp/hodge-literature-index-v1 -Book '*2502*'

The search returns PDF page9. Its index warning compares the separate custom collection against the shared reference collection, so the audit does not use index freshness as proof: it independently checks the retained PDF and page hashes.

## Actual theorem statements

Primary paper: Eyal Markman, Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds, arXiv:2502.03415v2, PDF page9.

    Corollary 1.6.1. The Hodge conjecture holds for abelian fourfolds.

The adjacent proof explicitly states that the Hodge-Weil classes are algebraic for EVERY abelian fourfold of Weil type, for all imaginary quadratic number fields and all discriminants. It then treats nonsimple fourfolds and explicitly discusses A=B times E, where B is a simple abelian threefold and E is an elliptic curve. Thus this is not a generic-only or simple-only statement accidentally applied to a decomposable control.

The same page's Theorem 1.5.1 concerns polarized abelian SIXFOLDS of Weil type with discriminant -1. That theorem alone must not be relabeled a fourfold theorem; the paper explicitly supplies the fourfold corollary and its reduction.

Cross-check: Markman, Secant sheaves and Weil classes on abelian varieties, arXiv:2509.23403v2, PDF page3, Theorem 1.2 states:

    The Weil classes for abelian fourfolds of Weil type and abelian sixfolds
    of split Weil type with complex multiplication by a quadratic imaginary
    number field K are algebraic.

The survey is corroborating scope, not a substitute for reading the primary paper's corollary. It also records earlier split-fourfold results; none needs to be invoked separately here.

Sources:
- https://arxiv.org/pdf/2502.03415v2, PDF page9; retained PDF SHA256 8155aa33870069b8381efe9a53adf091ce28a6a518311d768e0248abb2e675ba.
- https://arxiv.org/pdf/2509.23403v2, PDF page3; retained PDF SHA256 3151aee3307548da8f89b7b8d396db6e6c6fb6753cf76d152ad4b52b944252f5.

## Hypothesis-by-hypothesis match

| Requirement or possible scope issue | Actual control |
| --- | --- |
| Smooth projective abelian fourfold | C is a projective CM elliptic curve and A the polarized active abelian threefold; their product has dimension4 |
| Imaginary quadratic K | Q(i), with the conjugate action on C and the native action on A |
| Balanced Weil signature | (2,2), computed from those actions |
| Polarization and Hermitian discriminant | Product polarization, native matrix diag(-1,1,1,-1), determinant+1 and an explicit maximal isotropic two-plane |
| Rational Hodge class and codimension | gamma=f external p-e external q in H^4(C times A,Q), type(2,2), codimension2 |
| Membership in the actual Weil subspace | gamma=-Im(conjugate(omega) external Omega_A), a rational determinant component |
| Generic versus special/decomposable | Primary corollary is for all abelian fourfolds; its proof explicitly includes the threefold-times-elliptic case |
| Whole Weil space versus one unspecified component | The theorem states algebraicity of the Weil classes, and the corollary covers all rational Hodge classes; both determinant components are covered |

No further principal-polarization, simplicity or generic-period restriction is present in the quoted corollary. Thus no specialization theorem needs to be silently added to apply it to this control.

## Scoped conclusion

Accepting the cited primary result as imported mathematics, there exists

    Gamma_alg in CH^2(C times A)_Q with cl(Gamma_alg)=gamma.

Likewise the other rational determinant component has an algebraic representative. This supplies a theorem-backed algebraic correspondence whose action on H^1(C) is the previously calculated map e to p and f to q. It is not merely an isomorphism of Hodge structures anymore: existence of a cycle realizing the tensor follows from the imported theorem.

No equations, effective representative, canonical choice or relative cycle over the parameter family are produced by this audit. The finite checker verifies source integrity, statement presence and the already supplied hypothesis data; it does not verify Markman's proof. The result is therefore recorded as imported-theorem-backed existence, not an explicit cycle construction or a new proof of Hodge.

## Boundary with the original fixed sixfold

The control fourfold is split, dimension4, with Hermitian determinant+1. The original selected X is a nonsplit dimension6 Weil variety with determinant-3. Neither the quoted sixfold split theorem nor the fourfold corollary establishes algebraicity of its alpha. The genericity and all-cycle necessity gates for that original source remain unchanged.

This audit positively resolves the correspondence-existence question on the control, not the original conjecture objective. It also reinforces why the prior degree-six divisor exclusion must not be promoted to a nonalgebraicity conclusion.

## Next executable construction

Use Gamma_alg and its CM transforms together with the inactive factor's actual divisor classes to construct codimension-three rational cycle classes on A times B. Type the pullback maps and products and compute whether their classes are exactly K1,K2, including the signs from reversing the C/A factor order. This turns the theorem-backed correspondence into a concrete composition of licensed algebraic operations and tests the previously non-divisor-generated control classes. No transport to the original fixed X is licensed by this composition alone.
