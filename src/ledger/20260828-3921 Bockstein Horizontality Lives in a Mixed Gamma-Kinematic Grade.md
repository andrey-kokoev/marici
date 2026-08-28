# 3921 — Bockstein Horizontality Lives in a Mixed Gamma-Kinematic Grade

## Typing question

Entry 3916 constructs the conductor specialization cone fiberwise. To make its rank-three cohomology a coefficient local system, the exact boundary line must be preserved by Gauss–Manin transport.

The boundary constructor is already a first normal derivative in the source exponent:

\[
\beta=\partial_\gamma d_{\rm exact}.
\]

Therefore its variation in a kinematic direction \(X\) is not contained in either first jet separately. It belongs to the mixed grade

\[
\epsilon_\gamma\epsilon_X.
\]

## Frozen source test

For every integration-by-parts generator in the complete five-mark presentation, compare the two source routes

\[
\partial_X\partial_\gamma d_{\rm exact}
\qquad\text{and}\qquad
\partial_\gamma\partial_X d_{\rm exact}.
\]

The gamma derivative selects the \(\partial K\) coefficient. The kinematic derivative is the exact source five-point stencil, valid because the frozen coefficients have bounded polynomial degree. Marked-denominator terms have no gamma dependence and therefore contribute zero to the mixed cell.

No quotient reduction or fitted connection is used in this test.

## Result

At primes \(32009\) and \(32003\), both kinematic directions \(x,y\) contain \(480\) mixed generator instances. Across all \(960\) instances:

\[
\partial_X\partial_\gamma d_{\rm exact}
=
\partial_\gamma\partial_X d_{\rm exact}.
\]

There are zero failures. The mixed coefficient packet is nonzero in both directions, with support count \(1200\) per direction.

## Narrow conclusion

The frozen source already contains the coherence type required for Bockstein horizontality. The missing object is not another Carrier stratum or an added connection cell; it is the reduction of the existing mixed gamma/kinematic grade through the physical quotient and conductor target.

This establishes generator-level mixed flatness only. It does not prove that the induced rank-one boundary subbundle is horizontal after quotient reduction.

## Correction to the frontier

Testing horizontality from the ordinary rank-26 connection and the gamma-Bockstein as two independent first-order packets would be mistyped. The required computation is a bidual reduction over

\[
\mathbb F_p[\epsilon_\gamma,\epsilon_X]/
(\epsilon_\gamma^2,\epsilon_X^2),
\]

retaining the mixed product \(\epsilon_\gamma\epsilon_X\).

## Next falsifier

Perform that bidual quotient reduction. Extract the covariant derivative of the Bockstein line and compare it with the independently derived root-cover/weighted-sheet connection. The line is horizontal only if the projected mixed defect vanishes modulo the line in both kinematic directions.

## Rejected shortcut

A five-point audit recomputed the complete dual-gamma quotient at nearby source points and normalized the resulting Bockstein line in each normal-form frame. In both (x) and (y), the free-coordinate support changes across the stencil.

Therefore the sampled fiberwise vectors do not inhabit one canonical frame. Their apparent projective derivatives are not connection invariants and cannot decide horizontality. This rejects the tempting shortcut of differentiating independently reduced fibers and strengthens the requirement for one simultaneous bidual reduction.

## Bidual arithmetic contract

The required coefficient ring has now been implemented in the ordered basis

\[
(1,\epsilon_\gamma,\epsilon_X,\epsilon_\gamma\epsilon_X).
\]

Its multiplication and unit inversion, including the quadratic mixed correction in the inverse, pass deterministic tests at primes (32009) and (32003). The frozen integration-by-parts coefficient lifts with mixed component exactly (partial_X\partial_fK), nonzero in both directions. Thus the arithmetic and source-coefficient contracts for the simultaneous reducer are fixed; quotient elimination and projected-line extraction remain.

## Artifacts

- `research/benincasa/checkers/check_rank26_gamma_kinematic_mixed_generator.py`
- `research/benincasa/results/rank26-gamma-kinematic-mixed-generator.json`
- `research/benincasa/results/rank26-gamma-kinematic-mixed-generator-p32003.json`
- `research/benincasa/checkers/check_rank26_bockstein_projective_variation.py`
- `research/benincasa/results/rank26-bockstein-projective-variation.json`
- `research/benincasa/checkers/check_rank26_bidual_coefficient_ring.py`
- `research/benincasa/results/rank26-bidual-coefficient-ring.json`
- `research/benincasa/results/rank26-bidual-coefficient-ring-p32003.json`

Ledger sequence claim: `seqclaim-7563cb8d20ef79a8488f6cef`.
