# Tail certificates are complete only off the positivity boundary

## Question

Does a shrinking arithmetic tail bound eventually decide every finite observer positivity question?

## Spectral enclosure

For a fixed observer packet `I`, let

\[
\delta_{I,N}=|I|\varepsilon_N,
\qquad
\|G_I-G_{I,N}\|_{\rm op}\le\delta_{I,N},
\qquad
\delta_{I,N}\to0.
\]

Then

\[
\lambda_{\min}(G_I)
\in
[
\lambda_{\min}(G_{I,N})-\delta_{I,N},
\lambda_{\min}(G_{I,N})+\delta_{I,N}
].
\]

If the full minimum eigenvalue is strictly positive or strictly negative, some finite cutoff eventually determines its sign. This follows directly from convergence of the enclosure width to zero.

## Boundary obstruction

If

\[
\lambda_{\min}(G_I)=0,
\]

no nonzero tail enclosure can certify semidefiniteness. Every finite interval may straddle zero. Shrinking numerical or analytic error bounds therefore do not provide a complete decision procedure for membership in the closed positive cone.

This is structural rather than a weakness of the elementary prime estimate. Any approximation-only method has the same boundary problem.

## Required boundary certificate

A semidefinite boundary claim needs an exact source-derived null relation. For a coefficient vector `c`, require both

\[
G_Ic=0
\]

through completed source identities and

\[
x^*G_Ix\ge0
\quad\text{on }c^\perp.
\]

Equivalently, a coherent Gram factorization may exhibit `c` in the kernel of the global defect operator. Approximate small eigenvalues alone do not establish this relation.

## Four-valued disposition

A finite meta-observer should return one of:

1. `positive_definite`: lower enclosure endpoint is positive;
2. `negative`: upper enclosure endpoint is negative;
3. `positive_semidefinite_boundary`: exact null relation plus positivity on the quotient;
4. `unresolved`: none of the preceding certificates exists.

The third state must not be inferred as the limit of repeated unresolved computations.

## Relevance to the infinite cone

The positive observer cone is closed, and RH-strength positivity includes its boundary. Hence an architecture based only on strict eigenvalue margins proves at most positivity on the cone interior. Closure requires exact identities or a global contraction/factorization that remains meaningful when the defect operator has a kernel.

## Disposition

Retain log-Gaussian tail margins for interior and exterior decisions. Add an exact-nullspace certificate lane for boundary points. The global source contraction remains the only uniform constructor covering all three decided cases without assuming a spectral gap.
