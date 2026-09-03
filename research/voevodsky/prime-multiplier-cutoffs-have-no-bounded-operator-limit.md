# Prime-multiplier cutoffs have no bounded operator limit

## Question

Does the exact finite-cutoff linearization of the prime form converge as bounded multiplication operators on the heat-observer space?

## Claim boundary

No. The multiplier norms diverge already at frequency zero. This rejects bounded-operator convergence of the prime block alone, but does not reject a distributional quadratic-form limit or cancellation after joint completion with the gamma sector.

## Finite linearization

For fixed positive \(t,h\), let

\[
d\rho_{t,h}(u)
=
\frac1{2\pi}
e^{-tu^2}(1-e^{-hu^2})du
\]

and

\[
(V_hp)(u)=p(e^{-hu^2}).
\]

At cutoff \(N\), the prime form is

\[
Q_{P,N}(p)
=
\langle V_hp,M_{W_{P,N}}V_hp\rangle,
\]

where

\[
W_{P,N}(u)
=-
\sum_{2\leq n\leq N}
\frac{\Lambda(n)}{\sqrt n}
\cos(u\log n).
\]

This is linear in \(p\) before quadratic evaluation and introduces no cross-prime terms.

## Operator-norm hostile

At \(u=0\),

\[
W_{P,N}(0)
=-
\sum_{2\leq n\leq N}
\frac{\Lambda(n)}{\sqrt n}.
\]

All summands are nonnegative. The sum diverges, already by restricting to primes. Since \(W_{P,N}\) is continuous,

\[
\lVert M_{W_{P,N}}\rVert
=
\lVert W_{P,N}\rVert_{L^\infty(\rho_{t,h})}
\geq
|W_{P,N}(0)|,
\]

where essential supremum sees neighborhoods of zero even though the density of \(\rho_{t,h}\) vanishes at the point itself. Hence

\[
\sup_N
\lVert M_{W_{P,N}}\rVert
=
\infty.
\]

Uniform boundedness rules out convergence to a bounded operator on the full heat-observer Hilbert space.

## Meaning of the residual

The finite linear square-root factorization exists, but its prime multipliers leave every bounded operator ball. The residual is therefore not failure of linearity. It is failure of the prime block to complete independently.

The remaining possibilities are narrower:

1. the prime forms converge on a proper dense core as an unbounded closable form;
2. gamma and prime cutoffs must be combined before taking the limit;
3. a source-prescribed counterterm removes the frequency-zero divergence;
4. the relevant graph norm is stronger than the ambient heat-observer norm.

The first and third options require exact cutoff compatibility. Arbitrary subtraction of \(W_{P,N}(0)\) would change the form by a multiple of \(\lVert V_hp\rVert^2\) and is not source-authorized.

## Coherencer hierarchy

At finite cutoff, the indefinite multiplier \(M_{W_{P,N}}\) is the linear coherencer. Its norm-divergence is the next residual. A higher coherencer would have to specify a joint gamma--prime renormalization or a graph topology in which the residual is exact and the total form is lower bounded.

## Disposition

`linear_prime_form_factorization` passes at finite cutoff. `bounded_prime_operator_completion` fails. The live gate remains a jointly defined, closable, semibounded completed gamma-plus-prime form on a source-derived common domain.

## Verification

- `research/voevodsky/checkers/check_prime_multiplier_operator_growth.py`
- `research/voevodsky/results/prime_multiplier_operator_growth.json`
