# The fixed-prime homotopy survives graph completion

## Completion question

Ledger 3831 proved finite flatness of the prime-seam bicomplex. Could an
infinite-prime completion nevertheless destroy the contraction and create a
new cohomology class carrying the Hardy inner divisor?

For the natural graph completion, the answer is no.

## Algebraic homotopy

Let `d` be the finite-support prime-seam differential and fix one prime `p`.
Its half-line homotopy `h_p` satisfies on the algebraic core

\[
dh_p+h_pd=1-E_p,
\]

where

\[
E_p=(i_pc_p)\otimes P_{[0,\log p)}
\]

is the explicit moving-window projection. Both `h_p` and `E_p` are bounded on
the ambient Fock--half-line Hilbert space.

## Graph-norm estimate

For every core vector `x`, the homotopy identity gives

\[
\|dh_px\|
\leq
(1+\|E_p\|)\|x\|+\|h_p\|\|dx\|.
\]

Together with

\[
\|h_px\|\leq\|h_p\|\|x\|,
\]

this proves that `h_p` is bounded for the graph norm of `d`. Therefore it
extends continuously to the graph closure of `d`, and the homotopy identity
survives there:

\[
\overline d\,h_p+h_p\overline d=1-E_p.
\]

No cutoff-dependent inverse norm appears.

## Consequence

Infinite-prime graph completion cannot manufacture cohomology away from the
already explicit boundary projection `E_p`. On the kernel of `E_p`, the
completed complex remains contractible. Any completed class must be supported
in the finite moving-window boundary sector already visible at one prime.

Thus this particular complex cannot generate a hidden Blaschke divisor merely
because infinitely many primes are admitted. Its completion is too coherent:
the fixed-prime contraction remains uniformly available.

## Where the RH information is not

The Euler product

\[
\prod_p(1-p^{-s})
\]

may still fail to be trace class or summable outside its Euler domain. That is
a property of the graded partition-function shadow, not a failure of
exactness of this graph complex. Conflating trace divergence with emergent
cohomology would be another typing error.

The current prime-seam bicomplex therefore explains the moving-window
boundary and Möbius parity but does not protect the stable inverse.

## Surviving modifications

To obtain a nontrivial completion class, a future construction must invalidate
at least one premise of the fixed-prime homotopy theorem through independently
derived structure. Possibilities include:

- reciprocal or archimedean sewing that does not preserve `h_p`;
- a domain on which the right-shift homotopy is not graph bounded;
- prime-dependent noncommutative coefficients whose cross terms do not cancel;
- a relative determinant completion carrying an anomaly outside the graph
  complex.

Each option has a direct falsifier: apply `h_p`, compute its graph norm and
commutator with the new constructor, and reject any claimed anomaly when the
homotopy still extends.

## Scope

This closes spontaneous cohomology under the natural graph completion of the
prime-seam bicomplex. It does not analyze a separately justified reciprocal or
archimedean domain, regularized supertrace anomalies, stable inversion, or RH.
