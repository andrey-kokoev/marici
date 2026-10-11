# Understanding the unit-circle gap

This is a read-only review of the mathematical route and the inspected library interfaces, not a new proof receipt. No conjecture outcome or completion claim is changed.

## 1. The actual theorem

For the **existing operational** completion functions, the desired theorem is

`completionCosine x * completionCosine x + completionSine x * completionSine x = 1`.

The functions are independently scheduled Taylor constructions. Their names do not supply the usual trigonometric identities. Conversely, `ScheduledNormBound` is not an additional scientific conjecture: it is this identity expressed as metric equivalence of particular representatives.

`TickPhaseNormTransfer.norm-representative-class` identifies the quotient class of the scheduled norm representative with the completion-valued norm. `MetricCompletionEffectiveness.quotientPathToMetric` takes equality of quotient classes back to metric equivalence. Thus a completion-level proof could recover `ScheduledNormBound`; proving that bound by our current moving-sample route is not mandatory.

## 2. What the existing exponential proof actually does

The decisive interfaces were traced through these files:

1. `AbsoluteTaylorSeriesMultiplication.agda`:
   - `reciprocal-factorial-split` proves the all-degree factorial/binomial relation.
   - `exponential-coefficient-convolution` proves the exponential coefficient identity.
   - `finite-residual-is-upper-rows` identifies the rectangular-minus-triangular error.
   - `finite-triangular-residual-sharp-magnitude-bound` is generic in the two term sequences.
   - `scaledPrecisionTriangularResidualMagnitudeBound` bounds that residual using geometric majorants.
   - `absorbedFiniteProductDifferenceMagnitudeBound` converts it to a requested precision.
   - `ExponentialGlobalMajorant` and its construction handle the finite early terms as well as the contracting tail.
2. `CanonicalRationalExponentialMultiplication.agda` packages the rational case. `AutomaticRationalExponentialMultiplication.preferredExponentialMajorant` actually constructs its global majorant for each rational input, and `rationalExponentialMultiplication` assembles the theorem.
3. `ExponentialRationalApproximation.agda` approximates completion inputs by **fixed rational inputs**, using a bounded modulus.
4. `SynchronizedExponentialApproximation.agda` chooses a common rational approximation precision.
5. `ExponentialProductEventualApproximation.agda` controls products of the resulting approximate values.
6. `CompletedExponentialMultiplication.agda` composes those comparisons, the rational theorem, and raw/bounded-product transport.

This separates finite algebra, fixed-input convergence, and completion transport. Our recent route entangled all three.

## 3. The missing mathematical content

The library already supplies a generic product/residual estimate. What I have not found is the trigonometric **coefficient identity connected to the operational series**.

For fixed rational `q`, use dense degree-indexed sequences

`a_k = cosineDerivative(k) * exponentialTerm(q,k)`

`b_k = sineDerivative(k) * exponentialTerm(q,k)`.

The opposite-parity derivatives vanish. Consequently these dense sums reproduce the operational trigonometric partial sums at appropriate cutoffs; that parity/cutoff identification still needs a checked bridge.

The crucial finite identity, using the existing library interface, is

`cauchyProductCoefficient a a k + cauchyProductCoefficient b b k = 1 if k=0, else 0`.

Equivalently: `sum_(j=0)^k (a_j*a_(k-j) + b_j*b_(k-j)) = 1 if k=0, else 0`.

We have the derivative-model cancellation and the individual binomial normalization identities. We do **not** yet have a checked identification of the finite binomial sum with that recursive derivative model. That is a specific finite-algebra theorem, not a mysterious convergence failure.

Once it holds, the two finite norm products differ from one by the sum of **two generic triangular residuals**. The existing residual theorem should then be instantiated, rather than replaced with another custom norm-tail proof. This applicability still requires the majorant hypotheses and cutoff bridges to be supplied.

## 4. Why fixed rational inputs are a cleaner boundary

For a fixed rational `q`, an absolute exponential majorant can be chosen once. The derivative coefficients have magnitude at most one, so the dense trigonometric terms can be dominated by a positive exponential majorant at a rational radius bounding `|q|`. Bounds on those coefficients, domination, and alignment with the operational sums are proof obligations, not established here.

In the direct route, the common rational input changes with output depth. A majorant that exists separately for each rational input does not automatically give a uniform bound along that moving sequence. Our control-amplitude bounds do not, by themselves, discharge this coefficient-tail uniformity obligation.

The rational-first route avoids making the finite identity carry this extra uniformity burden. It would then require completion approximation lemmas for sine and cosine analogous to the exponential ones. `OperationalCosineMetric.agda`, `OperationalSineMetric.agda` and their uniform comparison modules provide ingredients, but I did not find ready-made sine/cosine versions of `BoundedExponentialModulus` and `ExponentialRationalApproximation`. Transfer is therefore work, not a free consequence of saying 'by continuity'. Metric-respecting descent alone is not that quantitative continuity theorem.

## 5. Alternatives and why none is a free shortcut

- **Our direct scheduled route:** can reuse the newly proved actual-sample comparisons, but still needs coefficient identification, residual estimates uniform on the chosen input bound, and the final budget.
- **Rational identity, then completion transfer:** follows the existing multiplication architecture and isolates the algebraic problem. It needs bounded sine/cosine approximation wrappers and schedule alignment. This is the clearest route to investigate next, not a measured optimum.
- **Complex exponential inverse law:** mathematically elegant, but the operational complex exponential is assembled as `exp(real)*(cos(imag),sin(imag))`. `ComplexExponentialAssembly.agda` supplies components and zero laws, not a multiplication theorem. Appealing to `exp(i*x)*exp(-i*x)=1` would presently assume new work which may contain the same trigonometric identity.
- **ODE uniqueness or trigonometric addition formulas:** valid mathematical approaches, but I found no ready-to-use theorem for these operational completion functions. Introducing differentiation/uniqueness now could be a larger detour.

## 6. What remains useful, and what duplicated infrastructure

Useful source-specific work includes the phase component reduction, operational trig term normalization, the actual scheduled sample identities, and the common-input comparison bounds. The derivative cancellation proof is useful if its finite-sum interpretation is established.

The new finite-sum product and interchange modules substantially overlap existing `finiteSumAdd`, `finiteDoubleSumSwap`, and rectangular/triangular decomposition machinery. Our degree regrouping handles explicit trig parity offsets, but it should not become a second general multiplication library. I should have discovered and compared the existing machinery before adding those files. They are retained as checked artifacts, not treated as a reason to keep following that route.

Fresh-check timeouts are a separate verification problem. Cached checks do not replace fresh closure, and a timeout is not evidence against the identity. The cause of the expensive fresh checks has not been diagnosed here.

## 7. Relation to the larger conjecture

Unit norm is a necessary certificate for the **declared relative spectral realization**. It does not establish that bare Tick determines the complex carrier, exponential phase, time scale or return convention. The original source-derived-lift question remains distinct. Completing this analytic identity would validate the chosen interpretation, not supply a new selection principle or an observable law.

## 8. What would count as the next meaningful result

The fixed-rational coefficient identity is stated in section 3. Before more code, trace its remaining parity bridge and finite binomial-sum lemma against the library's existing definitions. Compare the existing derivative proof with a direct binomial proof; do not choose solely because one route already has more of our files. The majorant/residual step should reuse the generic interfaces listed in section 2.

A meaningful next certificate is the **fixed-rational unit-circle theorem together with its operational-series identification**, not another increasing count of auxiliary net checks. This is a research boundary, not a promised one-turn completion or a deadline. If the inspected interfaces do not fit, record why before creating another abstraction.
