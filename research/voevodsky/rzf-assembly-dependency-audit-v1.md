# RZF assembly dependency audit v1

## Question

Which exact interface prevents the current canonical Dirichlet construction from yielding a checked value function?

## Claim boundary

The inspected domain is `RationalRightHalfPlanePoint`: rational complex coordinates with real part above one, not the full complex completion half-plane. The conjecture was that the existing components fill the evaluator without another mathematical premise. Rivals: missing primitives, missing convergence control, or a hidden completed implementation.

`CanonicalNegativePowerKernel.agda` constructs the exponential-of-negative-product expression and its quotient comparison. `CanonicalDirichletRegularPartialSum.agda` supplies its finite sum. `CanonicalDirichletTriangularApproximation.agda` supplies approximation, self-comparison error, and cofinality. Self-comparison is not a tail estimate.

The risky assembly probe is `agda/CanonicalZetaAssemblyBoundary.agda`: all evaluator fields are filled, except `cauchyDifference` is explicitly supplied as an argument. Agda checks this conditional constructor. This does not inhabit its premise, identify the logarithm analytically, or implement RZF.

## Disposition

For this assembly the explicit residual is `CanonicalDirichletCauchyBoundary`: for each rational half-plane point s, a `TriangularDifferenceCertificate (canonicalDirichletTriangularApproximation s)`. Its `differenceBound` must compare every pair of rational stage approximants within `precision m + precision n`; see `TriangularComplexSeriesCompletion.agda`.

The current truncation is `dyadicReciprocalIndex (suc stage)`, independent of s. Next test: can it satisfy the dyadic difference budget near real part one? Cofinality alone supplies no rate. No counterexample has yet been proved. A failed schedule requires a source-derived point-dependent replacement with a proved tail budget, not a weakened certificate.

Verification: Agda 2.8.0.1, Cubical 0.9, successful check of `CanonicalZetaAssemblyBoundary.agda` using `--transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9`. Safe Cubical source flags retained; authorized PowerShell fallback used. No aggregate rerun or new negative control. New module and packet remain uncommitted.

No repository-wide absence claim: a broad search result failed with `output_ref_length_mismatch`; bounded source reads established this constructor instead. The natural-zeta and critical-strip source audits remain outside this result. Continuation and zero properties are separate later objectives; the abstract predicates in `ConstructiveZetaInterfaces.agda` do not prove them.
