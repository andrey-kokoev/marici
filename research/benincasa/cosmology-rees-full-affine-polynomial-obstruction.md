# Full affine polynomial obstruction and leading-symbol distinction

## Question

Does the corrected full affine scalar equation admit a finite-degree polynomial solution, and what does the leading homogeneous symbol establish?

## Full affine theorem

Use

\[
H=3X^2-6s^2-36s,
\qquad
Q=s^2X(X+s)(X-6),
\qquad
K=H^2.
\]

No finite-degree polynomial pair solves the corrected scalar target \(3K^2Q\).

An exact rational left functional has 45 nonzero monomial coefficients supported only in output degrees 5 through 14. It annihilates all operator columns through level caps \((9,7)\) and pairs with the target as

\[
-\frac{114318864}{1715}.
\]

The only omitted input degrees whose outputs can overlap this support are level-1 degree 10 and level-0 degree 8; direct exact evaluation shows that the functional annihilates those columns too. Every later input has minimum output degree at least 15 and is annihilated by support separation. This proves persistence for arbitrary finite polynomial degree.

## Leading-symbol result

Replacing the affine factors by their highest homogeneous parts gives

\[
H_{\mathrm{top}}=3X^2-6s^2,
\qquad
Q_{\mathrm{top}}=X^2s^2(X+s).
\]

In this associated-graded system, the radial level-1 vector

\[
f_1=-\frac35H_{\mathrm{top}}^2(X,s)
\]

maps exactly to \(3H_{\mathrm{top}}^4Q_{\mathrm{top}}\). The same expression in the full affine system leaves 29 nonzero terms. Therefore associated-graded image membership does not lift to affine image membership.

## DPC disposition

- **Problem:** distinguish full affine solvability from leading-symbol solvability.
- **Bold conjecture:** a leading-symbol radial solution lifts to the affine equation.
- **Named rivals:** affine lift; lower-order obstruction detected by a finite-support cokernel.
- **Risky consequence:** the radial substitution must have zero full affine residual.
- **Strongest falsification:** it leaves 29 terms, while the exact left functional detects the target and annihilates every polynomial column.
- **Disposition:** reject affine polynomial solvability; retain the radial identity only as associated-graded structure.

## Claim boundary

This theorem does not address localization, logarithmic inputs, completions, distributions, or nonscalar total-complex closure. Earlier reasoning that used homogeneous grading alone to claim affine obstruction is superseded: lower affine coefficients couple grades, and the obstruction is established instead by the finite-support left functional.

The ten-dimensional leading-symbol kernel is distinct from full affine solvability. Its image and rank calculations remain associated-graded results. The previously stated inclusion and mixed-coordinate refinements still depend on separately proving the Hamiltonian constants-field and \(B\)-surjectivity lemmas; they are not used here.

## Durable verification

- `research/benincasa/results/cosmology_rees_affine_cokernel_theorem.json`
- `research/benincasa/results/cosmology_rees_affine_left_null.json`
- `research/benincasa/results/cosmology_rees_affine_radial_falsifier.json`
- `research/benincasa/results/cosmology_rees_natural_checker_audit.json`
