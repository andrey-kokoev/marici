# Every odd central log jet of the finite-prime transition diverges

## Question

Is the divergent first logarithmic derivative the only obstruction to a
cutoff-uniform Fourier–Tate jet frame, or does the divergence persist through
the full reflection-odd jet tower?

## Exact local expansion

Put

\[
s=1/2+u,
\qquad
r_p=p^{-1/2},
\qquad
L_p=\log p.
\]

Then

\[
\gamma_p(1/2+u)
=
\frac{1-r_pe^{-L_pu}}{1-r_pe^{L_pu}}.
\]

For (u) in a sufficiently small local disk,

\[
\log\gamma_p(1/2+u)
=
2\sum_{k\ge1}
\frac{r_p^k}{k}\sinh(kL_pu).
\]

The logarithm is odd in (u), as required by reflection inversion.

## All central derivatives

Every even central logarithmic derivative vanishes:

\[
\partial_u^{2m}\log\gamma_p(1/2)=0.
\]

For every (m\ge0), the odd derivative is

\[
\partial_u^{2m+1}\log\gamma_p(1/2)
=
2L_p^{2m+1}
\sum_{k\ge1}k^{2m}p^{-k/2}.
\]

Every summand is positive.

For the finite product,

\[
a_{2m+1,X}
:=
\partial_u^{2m+1}\log\gamma_X(1/2)
\]

equals

\[
2\sum_{p\le X}L_p^{2m+1}
\sum_{k\ge1}k^{2m}p^{-k/2}.
\]

## Divergence theorem

Keeping only the (k=1) term gives

\[
a_{2m+1,X}
\ge
2\sum_{p\le X}
\frac{(\log p)^{2m+1}}{\sqrt p}.
\]

For sufficiently large (p), the summand dominates (1/p). Euler's
divergence of the prime harmonic series therefore implies

\[
a_{2m+1,X}\longrightarrow+\infty
\]

for every (m\ge0).

Thus every odd central log jet diverges, while every even one vanishes
identically.

## Finite-order normal form

To cancel the logarithmic jets through order (2M+1), the unique odd Taylor
counterterm through that order is

\[
\log\rho_{X,M}(u)
=
-\sum_{m=0}^{M}
\frac{a_{2m+1,X}}{(2m+1)!}u^{2m+1}.
\]

Exponentiation preserves reflection inversion:

\[
\rho_{X,M}(-u)=\rho_{X,M}(u)^{-1}.
\]

This cancels the central log jets only through the declared finite order.

## Infinite-jet consequence

No finite polynomial counterterm controls the complete Hardy or Clark jet
tower. A full analytic completion requires an infinite reflection-odd
renormalization whose coefficients, radius, cutoff bonding, and multiplier
bounds are all source-derived.

This is not merely a large constant problem. Each higher odd rung introduces
a new divergent connection coefficient.

The result explains why a scalar completion may exist while every finite jet
order requires additional normalization data. Scalar closure and
constructor-jet closure are genuinely different towers.

## Source-authority boundary

The Taylor subtraction above is the unique formal cancellation at a fixed
order, but it is not a construction of the completed Tate normalization.

A valid infinite tower must establish:

1. one analytic odd generating function rather than unrelated fitted jets;
2. compatibility with the finite-prime valuation grading;
3. the archimedean and polar source terms;
4. cutoff cocycle coherence;
5. convergence on a nonzero domain;
6. bounded action on every downstream graph topology;
7. direct qualification on target currents, not only on the normalization
   monitor.

## Relation to reset qualification

Aspect's acquisition hostiles separate monitor decay from target reset and
block balance from drift confounding. The parallel here is exact: cancellation
of the first monitored jet does not certify higher target jets, and a quiet
normalization residual does not certify the Green or arithmetic outputs.

Every retained target family needs its own qualification under the completed
odd normalization.

## Falsifier certificate

    {
      "code": "finite_order_prime_jet_renormalization_incomplete",
      "even_log_jets": 0,
      "odd_log_jets_diverge": "all orders",
      "highest_cancelled_order": "2M+1",
      "next_uncancelled_order": "2M+3",
      "infinite_source_odd_generator_required": true
    }

## Disposition

Every odd central logarithmic jet of the unrenormalized finite-prime
Fourier–Tate transition diverges positively. The completed constructor needs
an infinite source-derived reflection-odd normalization tower; first-order or
finite-order repair cannot close the full jet carrier.

## Claim boundary

This theorem concerns central Taylor jets of the naive finite-prime product.
It does not show that the globally completed Tate transition lacks a
convergent odd normalization, nor does it determine the correct analytic
generator or its completion topology.
