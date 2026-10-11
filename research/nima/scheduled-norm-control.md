# Actual scheduled norm controls

Implementation: `agda/TickScheduledNormControl.agda`.
Fresh verification: `results/scheduled-norm-control.json`.

## Implemented and checked

For each canonical cosine/sine representative `y`, multiplication uses the sample depth `suc(d+d)+suc(n)`, where `d` is that representative's canonical dyadic radius exponent. The extra `suc(n)` comes from Cauchy addition. The two exponents are independent; this is not a common-depth substitution.

`actual-norm-sample` proves definitionally that the actual norm representative is the sum of squares of those two samples.

The actual samples now have instantiated uniform magnitude bounds: take `M` as the sum of their canonical dyadic radii. Both samples are bounded by `M` for every output depth, and `M` is nonnegative.

`SampleControl x k n` specifies two rational controls `c,s`, their common amplitude bound, approximation error `epsilon`, finite norm defect `delta`, and the budget `4*M*epsilon+delta <= precision k`. `sample-control-bound` applies the checked rational perturbation theorem at the actual operational samples.

`controls-to-scheduled-norm` proves that eventually having these controls at every requested precision gives metric equivalence of the actual norm representative to constant one. It uses propositional-truncation mapping, not an unproved global selection of thresholds.

## Common Taylor controls now constructed

`agda/TickCommonTaylorControls.agda` chooses the common rational input at the maximum of the two actual input depths, and the common Taylor term index at the maximum of their series cutoffs. Both controls are explicit partial sums at that same rational input.

Agda proves input-refinement and tail-extension bounds, combines them into actual-sample-to-control errors, and derives amplitude bounds for the controls. Each error is at most `precision(n)` at actual output depth `n`, so these comparisons vanish with a concrete rate. Fresh closure passed: `results/common-taylor-controls.json`.

The common index counts trigonometric terms: cosine has degree `2N`, sine degree `2N+1`. The earlier equal-total-degree Python test must not be mistaken for a kernel proof of this exact pair.

## All-order algebraic cancellation now checked

`agda/TickTrigCoefficientCancellation.agda` proves, over any commutative ring, that the recursively defined Leibniz derivative coefficients of the cosine/sine norm have constant coefficient one and every positive coefficient zero. It also proves that truncating the two derivative sequences preserves these cancellations through their common retained degree, even with different cutoffs. This is an all-order kernel proof, not sampled coefficient testing.

Fresh receipt: `results/trig-coefficient-cancellation.json`. The module deliberately uses unnormalized derivative sequences; it does not yet identify its Leibniz product with the factorial-normalized operational partial-sum product.

## Operational term normalization now checked

`agda/TickTrigTaylorNormalization.agda` proves for every rational `q` and natural `n`:

- `cosineTerm q n = cosineDerivative(2n) * exponentialTerm q (2n)`;
- `sineTerm q n = sineDerivative(2n+1) * exponentialTerm q (2n+1)`;
- the corresponding equalities for the actual finite partial sums.

Here `exponentialTerm` is the existing recursively factorial-normalized operational term, not a new assumed coefficient. The proof uses the actual two-reciprocal term recurrences. Fresh verification: `results/trig-taylor-normalization.json`.

## Finite product expansion now checked

`agda/TickTaylorProductExpansion.agda` proves finite-sum multiplication, interchange of the two finite summation orders, and expansion of the squared norm as a rectangular double sum. `operational-norm-expansion` instantiates this at the actual normalized sine/cosine partial sums for every rational input and cutoff. No infinite rearrangement or convergence assumption is used.

Fresh receipt: `results/taylor-product-expansion.json`. This is the rectangular-expansion part of the product bridge, not yet its identification with the Leibniz derivative convolution. The cosine and sine summands have different total-degree offsets, so equal rectangular indices must not be canceled directly.

## Exact degree regrouping now checked

`agda/TickTaylorDegreeRegrouping.agda` proves that a bounded rectangular weighted sum equals its sum over total-degree contributions. It instantiates this for the operational norm with cosine-square degree `2i+2j`, sine-square degree `2i+2j+2`, and maximum degree `4N+2`. The original normalized weights are preserved exactly; the different parity offsets are not conflated.

Fresh receipt: `results/taylor-degree-regrouping.json`.

## Binomial weights implemented; fresh verification pending

`agda/TickTaylorBinomialWeights.agda` reuses `AbsoluteTaylorSeriesMultiplication.reciprocal-factorial-split` to prove

`exponentialTerm q i * exponentialTerm q j = choose(i+j,i) * exponentialTerm q (i+j)`.

It lifts this identity to the actual cosine/sine products and to every grouped degree contribution. Cached-dependency Agda checking passes (`results/taylor-binomial-weights-cached.json`); fresh closure timed out at 300 seconds (`results/taylor-binomial-weights.json`). This is not recorded as fresh verification.

The existing `AbsoluteTaylorSeriesMultiplication.agda` also contains finite triangular residual and tail-majorant machinery. The next tail work should instantiate those results rather than duplicate them.

## Still missing

No inhabitant of `EventualSampleControls` has yet been constructed. The remaining coefficient-sum target is

`degreeContribution q N k = truncatedNorm (2N) (2N+1) k * exponentialTerm q k`.

The individual factorial/binomial weight identity is now implemented. What remains is identifying the parity-filtered finite binomial **sum** with the recursive Leibniz derivative (and completing fresh verification). This connects the actual degree contributions to the proved cancellation. The high-degree residual estimate and combined precision budget remain afterward. The existing Python coefficient checks and paper series proof do not fill those fields.

Consequently **ScheduledNormBound remains uninstantiated**. This step connects the existing estimate to actual shifted representatives and supplies their amplitude bounds; it is not a complete phase-unitarity proof. The metric-equivalence target has the same norm representative expression as `TickPhaseNormTransfer`.
