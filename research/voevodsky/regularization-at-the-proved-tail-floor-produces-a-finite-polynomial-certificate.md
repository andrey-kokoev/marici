# Trace-derived coercivity yields a finite continuum positivity certificate

## Question

Does a degree-159 regularized tail map retain positivity under the coercivity bound actually supplied by the concentration trace argument?

## Claim boundary

Yes for the cutoff-250 first-prime form. Directed Arb evaluation certifies the concentration matrix, cutoff-form matrix, exact decimal span, projected residual Gram including its analytic Legendre tail, and final \(LDL^*\) positivity. This does not assert positivity for other support windows or an RH implication.

## Correct a posteriori bound

For trial map \(Y\),

\[
F-BC^{-1}B^*=J-R^*C^{-1}R,
\qquad R=B^*-CY.
\]

With

\[
\rho=\operatorname{Tr}(T)-\operatorname{Tr}(PTP),
\]

the concentration argument gives

\[
C\geq\alpha Q,
\qquad
\alpha=\frac{1-130\rho}{40}.
\]

The canonical run finds

\[
\rho\approx0.00619401302875,
\quad
\alpha\approx0.00486945765657,
\quad
\alpha^{-1}\approx205.361678964.
\]

Hence the tested lower form is

\[
J-\alpha^{-1}R^*R.
\]

## Selected finite candidate

The canonical \(700\)-point, 220-node-per-half-panel run selects a hard cutoff \(0.002\), retaining 36 numerical tail modes. After degree-159 truncation and orthogonality restoration,

\[
\|Y\|\approx10.1978366917,
\qquad
\|R\|\approx0.00887898151260,
\]

and

\[
\lambda_{\min}(J)\approx0.01799018237361,
\]

\[
\lambda_{\min}(J-\alpha^{-1}R^*R)
\approx0.01781853729388.
\]

The omitted tail-map Legendre coefficient tail has norm about \(4.54\times10^{-10}\). The projected residual itself is substantially more compressible: its Legendre tails after degrees 159 and 299 are approximately \(3.81\times10^{-13}\) and \(2.99\times10^{-13}\). The exported artifact now includes all 700 residual coefficient rows so that a rigorous analytic tail estimate can replace the numerical truncation. All three registered resolutions give the same lower margin to the displayed precision. The 280-node run labels cutoff \(0.01\), but it retains the same effective spectral set and produces the same form; the exported canonical candidate uses \(0.002\).

## Finite algebra checks

The exact-decimal-span checker proves an interval \(LDL^*\) minimum Gram pivot above \(0.999999999999988\). Exact algebraic tail orthogonalization has no cross-Gram failures and changes the exported tail matrix by at most \(6.0\times10^{-13}\) in maximum row-sum norm.

The concentration trace interval scout keeps the trace residual below \(1/130\) for assumed entry radii through \(2\times10^{-6}\). Its frequency quadrature remainder is attached, but floating-center roundoff remains to be replaced by directed interval evaluation before this becomes a continuum certificate.

## Interval sensitivity budget

An Arb \(LDL^*\) sweep varies the 25-by-25 candidate-form entries, all first-160 residual coefficients, and the inverse floor independently. With inverse-floor radius \(1\) and analytic tail \(4.36\times10^{-13}\), every tested pair through

\[
|\Delta J_{ij}|\leq10^{-4},
\qquad
|\Delta R_{nj}|\leq10^{-5}
\]

remains positive. Candidate-form radius \(3\times10^{-4}\) fails for every tested residual radius, while residual radius \(10^{-4}\) fails throughout the passing candidate-form range. The sufficient certification targets are therefore \(10^{-4}\) for each candidate-form entry and \(10^{-5}\) for each residual coefficient.

## Disposition

The corrected trace-derived certificate passes. Directed 192-bit Arb Gauss evaluation encloses every cutoff-form entry with maximum radius \(4.09\times10^{-21}\), far below the \(10^{-8}\) target. It independently certifies

\[
\rho=0.0061940130287439028\ldots,
\qquad
\alpha=0.0048694576565823159\ldots,
\]

and propagates the resulting inverse floor through the exact-span projected residual. Final interval \(LDL^*\) completes all 25 pivots with minimum pivot lower bound \(0.2428851171\). Therefore the cutoff-250 first-prime continuum form is positive. The omitted multiplier outside the cutoff is nonnegative, so the corresponding uncut form is positive on this support window. Positivity for other windows and any RH implication remain outside scope.

## Verification

- `research/voevodsky/checkers/run_regularized_polynomial_certificate_pipeline.py`
- `research/voevodsky/results/regularized_polynomial_scout.json`
- `research/voevodsky/results/regularized_polynomial_coefficients.json`
- `research/voevodsky/results/interval_polynomial_coefficients.json`
- `research/voevodsky/results/interval_exact_span_trace.json`
- `research/voevodsky/results/regularized_polynomial_pipeline.json`
- `research/voevodsky/checkers/check_arb_cutoff_form_legendre_matrix.py`
- `research/voevodsky/results/arb_cutoff_form_legendre_matrix.json`
- `research/voevodsky/checkers/check_interval_exterior_multiplier_nonnegative.py`
- `research/voevodsky/results/interval_exterior_multiplier_nonnegative.json`
- epistemic graph event `ep_c22157b9-64df-4c85-be8d-7e806fd27afc`
