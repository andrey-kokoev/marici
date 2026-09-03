# Moving prime thresholds rule out termwise infinitesimal positivity

## Question

Can the infinitesimal source form be factored globally by assigning every differentiated prime-power heat term an independently nonnegative square weight?

## Claim boundary

The derivative of each standard prime heat atom changes sign at an explicit scale, ruling out such a global termwise factor. The exact explicit-formula normalization still needs source attachment. Collective factors remain possible.

## Prime heat atom

Let

\[
L=\log n
\]

and consider the standard heat atom

\[
f_L(t)
=t^{-1/2}
\exp\left(-\frac{L^2}{4t}\right).
\]

Direct differentiation gives

\[
f_L'(t)
=
f_L(t)
\frac{L^2-2t}{4t^2}.
\]

All factors except \(L^2-2t\) are positive. Therefore the differentiated channel changes sign exactly at

\[
t_n=\frac{(\log n)^2}{2}.
\]

## First threshold

For \(n=2\),

\[
t_2
=
\frac{(\log2)^2}{2}
\approx0.2402265069591007.
\]

Below this scale the \(n=2\) differentiated atom has one sign; above it, the opposite sign. Every later prime power has its own larger threshold.

Thus no global source factor may assign a fixed nonnegative square coefficient to each differentiated prime-power channel independently.

## Current small-scale region

The current numerical boxes satisfy

\[
t\leq0.08<t_2.
\]

Hence all prime-power scalar derivative weights for \(n\geq2\) have the same positive sign there. The observed rank-two difficulty in this region is not caused by an individual prime channel crossing its scalar threshold.

It arises from moment correlations and the combined archimedean--prime form.

## Global consequence

As \(t\) increases, prime channels cross one after another. A valid all-scale factor must encode this moving boundary through one of:

- collective cancellation among prime powers;
- interaction with the archimedean term;
- a nonlocal transform changing the feature basis;
- a scale-dependent indefinite decomposition whose final compression is positive.

It cannot be a direct sum of permanently positive differentiated-prime features.

## Relation to local certification

Small-box certification can exploit the uniform scalar sign below \(t_2\), but that proof architecture cannot be extrapolated globally. Any theorem using termwise prime positivity must stop at the first threshold unless a new collective identity takes over.

This provides a typed stopping boundary rather than a numerical warning.

## Disposition

The global termwise-prime Dirichlet factor is falsified. Collective source positivity remains untested. The next candidate must state how it transports through every threshold \(t_n\), not only how it works in the initial small-\(t\) chamber.

## Verification

- `research/voevodsky/moving-prime-threshold-no-go-v1.json`
- `research/voevodsky/checkers/check_moving_prime_threshold_no_go.py`
- `research/voevodsky/results/moving_prime_threshold_no_go.json`
