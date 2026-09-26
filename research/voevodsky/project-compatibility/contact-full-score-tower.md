# The existing complete score tower does not remove contact-infinity suppression

## Prior-source search

Freshly read ledger2174,2218,2230,2231. Entry2231 already supplies all labelled mixed covariance responses via Boolean zeta inversion. Entry2174 supplies the actual contact-normal route pair (8C,-8C), from a grade-two deletion sector and the fully deleted sector. Entry2218 warns that raw mixed correlators also contain backgrounds. We therefore test the frozen contact-normal channel, not an arbitrarily chosen raw observable or a full physical period.

The question is whether the already admitted complete tower supplies a bounded alternative to first-score extraction at contact infinity.

## Source polynomial and complete response vector

Label the absent edge i and the other two edges j,k. The source-normal packet has covariance-multiplier polynomial

    F(g)=8 C g_j g_k (1-g_i).

Here C is independent of the covariance multipliers in the generic source chart. For every subset T of the three edges, define the distinct mixed logarithmic response at g=1. Then

    M_T = -8 C if i belongs to T, and0 otherwise.

The empty response vanishes by destructive interference. Four of the eight complete-tower entries are nonzero. Boolean Mobius inversion exactly recovers the two route values, but both reconstructed values still vanish with C. No bounded fixed inverse transform removes that common scalar factor.

## Actual Gaussian norm on the complete tower

Use the independent real-mode scores from ledger2214. For T nonempty, let S_T be the product of S_e over e in T. Include S_empty=1. Independence and centering give the L2 Gram matrix

    E(S_T S_U)=0 for T!=U,
    E(S_T^2)=2^(-|T|).

This is an L2 Gram matrix of mixed tests, not automatically a Fisher matrix for a new statistical model. The constant test is included with L2 norm1, not variance1.

The squared dual norm of the full response is therefore

    sum_T 2^|T| M_T^2
      =64 C^2 * 2(1+2)^2
      =1152 C^2.

The first detecting score alone gives128 C^2. The complete tower improves the response norm by a finite factor3, not by a factor that cancels C. For any uniformly L2-bounded linear combination of these tests, Cauchy–Schwarz forces the response to vanish with C.

For this single declared channel, the minimum squared norm of a test in the complete tower normalized to response1 is1/(1152 C^2). This follows by the Riesz representation and equality in Cauchy–Schwarz. It is nine times smaller than the first-score test cost, but still divergent. It does not assert minimum cost among all physical observables or amongst multiparameter estimators.

Along the previously tested source path, C=t^3. Full response norm squared is1152 t^6; minimum extracting-test norm squared is1/(1152 t^6).

## What this settles, and what it does not

The prior complete tower is a genuine extension of the port family and a successful exact tomography result. It is not a bounded alternative to the first-score channel at this infinity face. Exact reconstruction of shrinking route values must not be confused with uniform recovery of their normalized coefficients.

This is a bounded search and a scoped obstruction: all eight labelled covariance-response slots of this three-edge contact-normal packet have been tested. It does not exclude an independently sourced non-covariance observable, an orthogonal component of the full physical observable, or a different physical preparation. The contact-normal projection itself still requires its source admissibility and continuity conditions; no raw-background subtraction is inferred.

Next inspect whether the source fixes the full contact observable in Gaussian L2, rather than only these response moments. That decides whether the suppression is merely a finite-port limitation or extends to all bounded tests of the specified observable. Do not infer the stronger result from tomography labels alone.

## Verification

`uv run --with sympy python research/voevodsky/project-compatibility/check_contact_full_score_tower.py` differentiates the source polynomial in every labelled subset, verifies Mobius recovery, computes the mixed-test dual norm and checks three rational infinity samples. Owner artifacts remain unchanged.
