# Speculative sweep of Gaitsgory–Rozenblyum DAG I–II

Date: 2026-09-08

Sources:

- `references/Derived algebraic geometry Vol1.pdf`, *A Study in Derived Algebraic Geometry, Volume I: Correspondences and Duality*;
- `references/Derived algebraic geometry Vol2.pdf`, *Volume II: Deformations, Lie Theory and Formal Geometry*.

This is a targeted applicability sweep, not a claim that the books prove the Marici comparison.

## Strongest finding: replace the naive symmetric dual by a formal vector prestack

Volume II, Chapter 7, Section 1.4 constructs, for **any** `F in IndCoh(X)`, a formal vector prestack

\[
\operatorname{Vect}_X(F)=\operatorname{Spec}^{\mathrm{inf}}(\operatorname{Sym}(F)),
\]

where `Sym(F)` is a cocommutative augmented coalgebra for the `!`-tensor structure on `IndCoh(X)`. Proposition 1.4.3 gives its mapping property in terms of distributions, and Corollary 1.4.4 identifies its tangent object with `F`.

This is a better fit for Marici than the provisional expression

\[
\operatorname{RSpec}_B\operatorname{Sym}_B((QD_k)^\vee).
\]

The latter requires a semi-free replacement and dualization of a nonperfect conductor-supported complex. The GR construction accepts the strict target itself as an IndCoh object and produces a formal moduli problem whose tangent object is canonically that complex. Thus the recommended formal object is

\[
\boxed{\mathfrak X_k=\operatorname{Vect}_{\operatorname{Spec}B}(D_k^{\operatorname{IndCoh}})}.
\]

This does not make it smooth, but it removes an avoidable dualization/perfectness assumption.

## Duality and singular support

Volume I develops `IndCoh`, its dualizing object, Serre duality, `!`-pullback, proper pushforward and correspondence formalism. This is precisely the categorical environment in which the nonsplit node dualizing complex and conductor support should live. The discussion in Volume I, Part III explicitly traces the functorial difficulty of `f!` back to Hartshorne's *Residues and Duality* and resolves functoriality through correspondences.

For Marici this suggests:

1. regard `omega`, `C`, and `D_k` as IndCoh objects on the derived node;
2. express the conductor inclusion and normalization correspondence using `!`-pullback/proper pushforward rather than an ad hoc scalar residue;
3. view the known sixfold residue as the local coordinate representative of an IndCoh duality counit.

This is structurally stronger than the Stacks-only formulation because it naturally accommodates derived singularities and nonperfect coherent objects.

## Square-zero extensions preserve a nonsplit dualizing extension

Volume II, Chapter 8, Section 6 studies `IndCoh` on square-zero extensions. Its stated conclusion is especially relevant: the dualizing sheaf of a square-zero extension is naturally an extension of the direct image of the defining ideal by the direct image of the original dualizing sheaf.

That is qualitatively the same behavior required by the two-layer conormal object and the nonsplit conductor channel. It supports retaining the extension

\[
0\to C\cdot v\to E_{\beta,k}\to C\cdot u\to0
\]

inside the dualizing/formal geometry rather than replacing it by two scalar lines. A future exact comparison should identify `E_beta,k` with the appropriate GR square-zero-extension dualizing triangle. The sweep did not locate a theorem making this identification automatically.

## Lie theory and the homological vector field

Volume II develops formal moduli problems, Lie algebras and Lie algebroids in `IndCoh`. This offers a more intrinsic replacement for saying only that a differential extends to a derivation of a symmetric algebra:

- the strict differential on `D_k` supplies the tangent-level homological operator;
- native outer operations should be encoded as Lie-algebroid actions on the formal vector prestack;
- chain homotopies should become coherent homotopies of these actions;
- reflection should be a morphism between the two marked formal moduli problems.

The books do not identify our operation bar complex with such a Lie algebroid; that remains a construction.

## Distributions are more promising than functions for the residue

The mapping property of `Vect_X(F)` is formulated using the augmented distribution coalgebra `Distr+`, not only ordinary functions. This is potentially the correct home for the sixfold conductor residue. The residue is already distributional/local-cohomological, whereas the naive augmentation on ordinary formal functions kills every Bruce product.

A speculative route is therefore:

\[
\operatorname{Distr}^+(\mathfrak X_k)
\longrightarrow \omega_{\operatorname{Spec}B}
\xrightarrow{R\Gamma_{\mathfrak m}}
R\Gamma_{\mathfrak m}(\omega_B)
\xrightarrow{\operatorname{Res}} C\Pi^{\otimes ?}.
\]

The first arrow would be a formal-fiber integration/counit in `IndCoh`. This is not yet constructed, but GR indicates that distributions and dualizing objects—not unrestricted polynomial functions—are the natural categorical inputs.

## What the books do not give for free

No direct occurrence of Berezin integration, Q-manifolds in Bruce's smooth sense, the Bruce derived associative product, or cyclic cohomology was found. In particular, the volumes do not automatically provide:

- a scalar-valued trace on the formal vector prestack;
- `Q`-invariance/divergence zero;
- an integration map for a nonproper formal fiber;
- the P24 one-cocycle;
- nontriviality of that cyclic class.

IndCoh proper pushforward is available when the relevant map is proper. The formal vector projection is not automatically proper. A support/pro-nilpotence condition or a distributional counit must replace naive integration over an affine even fiber.

## Revised next experiment

1. Promote the strict `B`-complex `D_k` to `IndCoh(Spec B)`.
2. Construct `X_k = Vect_{Spec B}(D_k)` via GR Volume II, Chapter 7, Section 1.4.
3. Model the conormal extension using Volume II, Chapter 8, Section 6 and compare its dualizing triangle with `E_beta,k`.
4. Construct the homological field and outer operations as a Lie-algebroid action.
5. Seek the trace first on `Distr+(X_k)` with conductor support, then pair it with the known sixfold residue.
6. Only after obtaining a `Q`-closed functional, transport Bruce's product/cyclic formulas to this distributional formal setting.

## Decision

The sweep finds a meaningful upgrade, not a finished trace. GR likely resolves the representability category and the nonperfect-dual problem: `D_k` canonically determines a formal vector prestack through IndCoh coalgebras. It also points to distributions as the proper carrier of the residue. The first genuinely new matrix still needed is the formal-fiber distribution counit/pushforward and its compatibility with the strict `Q` and outer-operation action.
