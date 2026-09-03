# Prime cutoff and observer rank are opposite truncation axes

## Question

On which finite stages may one demand positivity or contractivity?

## Two noninterchangeable indices

Let `N` denote an arithmetic source cutoff and `I` a finite observer packet.

The cutoff `N` approximates the entries of the completed kernel:

\[
K_{N,\sigma}(a-b)\longrightarrow K_\sigma(a-b).
\]

The packet `I` restricts the full kernel to a finite Gram matrix:

\[
G_I=(K_\sigma(a_i-a_j))_{i,j\in I}.
\]

These operations have different logical roles. Source cutoff is a convergence device. Observer restriction is a positivity test.

## Invalid strengthened demand

It is not legitimate to require

\[
G_{I,N}\ge0
\]

for every arithmetic cutoff `N`. Completion identities and cross-sector cancellation apply to the full source. A partial endpoint--gamma--prime sum may be indefinite even when its limit is positive. Requiring a contraction `C_N` at each arithmetic cutoff is therefore stronger than RH and can reject the intended completed object.

Nor does convergence of indefinite `G_(I,N)` to `G_I` prove that `G_I` is positive.

## Correct order of limits

At fixed Gaussian width:

1. form the full labelled prime feature rows by completing the absolutely convergent log-Gaussian direct sums;
2. combine them with the endpoint and gamma rows to obtain global `A` and `B`;
3. restrict the probe domain to each finite observer packet `I`;
4. demand

\[
\|Bf\|\le\|Af\|
\qquad(f\in V_I).
\]

The observer packets form the inverse positivity system. Arithmetic cutoffs require source-convergence residuals and common-normalization checks, not positivity certificates.

## Mixed finite computations

A finite computation uses both indices and must report a tail error. If

\[
G_I=G_{I,N}+R_{I,N},
\]

then a numerical lower bound for `G_(I,N)` is meaningful only together with an operator bound on `R_(I,N)`. A negative partial eigenvalue is not a refutation unless it dominates the certified tail; a positive partial eigenvalue is not evidence for the full matrix unless the tail is smaller than its margin.

## Revised meta-observer table

- Prime support refinement: covariant source convergence; check entry residuals and tail bounds.
- Completion refinement: verify endpoint, gamma, and prime terms use one convention.
- Observer-rank refinement: contravariant principal-submatrix restriction; require positivity.
- Heat-order and translate refinement: compare the full completed source, not independently regularized cutoffs.

## Disposition

Withdraw any requirement that arithmetic-cutoff contractions be individually contractive or form a positive inverse system. The global source contraction, if it exists, is restricted by observer packets. Prime cutoffs approximate its matrix entries and must carry rigorous tail bounds.
