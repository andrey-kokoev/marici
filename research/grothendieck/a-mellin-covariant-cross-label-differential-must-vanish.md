# A Mellin-covariant cross-label differential must vanish

## The proposed repair

Ledger 3825 identified a possible missing constructor: a parity-changing
differential between distinct integer-label divisor complexes, producing
Möbius cancellation before scalar aggregation.

The first compatibility test is Mellin covariance.

Let the label Hamiltonian be

\[
H e_n=(\log n)e_n.
\]

The spectrum is simple on the integer-label basis because `log n=log m`
implies `n=m`.

## Exact no-go theorem

Let `d` be a linear operator on the algebraic finite-support label module. If

\[
[H,d]=0,
\]

then `d` preserves every one-dimensional eigenspace of `H`. Hence

\[
d e_n=c_ne_n.
\]

If the label line `e_n` has one fixed parity and `d` is parity-changing, then
`c_n=0` for every `n`. Therefore

\[
d=0.
\]

More generally, if each integer label carries an internal divisor complex,
a commuting differential may act inside one `n`-fiber but cannot connect
distinct labels. Such internal maps reproduce the already known Möbius Euler
characteristic and provide no cross-label analytic cancellation.

## Consequence

The proposed cross-label differential cannot simultaneously be:

- nonzero between distinct integer labels;
- parity-changing;
- strictly commuting with native Mellin transport.

Any viable cross-label operation must carry the energy mismatch

\[
\log m-\log n=\log(m/n).
\]

It therefore needs an additional scale reservoir, a connection term, or a
covariance law with nonzero weight rather than ordinary commutation.

For prime attachment `n -> np`, the mismatch is exactly `log p`. This makes
the moving seam and prime-scale currents natural candidates for the missing
reservoir: they already carry the translation length `log p`. But they must
enter as typed energy-bearing arrows, not as flat comparisons among paths.

## Fermionic partition-function caution

Squarefree integers can be represented as finite prime subsets, and

\[
\prod_p(1-p^{-s})
\]

is the fermionic graded partition function. The alternating sign is fermion
parity. This does not make the product a supersymmetric index. A differential
pairing even and odd states at equal energy is absent because adjoining a
prime changes the energy by `log p`.

Calling the Euler product a supertrace is correct algebraically in its
convergence domain; calling its continuation an index protected by a
commuting differential is not.

## Revised constructor target

Seek a weighted differential `d_p` satisfying a covariance relation such as

\[
[H,d_p]=(\log p)d_p
\]

for prime attachment, together with a compensating seam or reservoir action
of weight `-log p`. Only the combined operator could have total Mellin weight
zero and participate in a completion-stable complex.

The acceptance gates are:

1. derive both weighted arrows from source constructors;
2. prove the total differential squares to zero;
3. prove its contraction respects the boundary-bearing completion;
4. recover the Möbius inverse as a shadow, not as an input;
5. reject a Blaschke-modified hostile at the complex level.

## Scope

This closes the naive Mellin-commuting cross-label differential. It does not
exclude an energy-bearing bicomplex or connection, construct the compensating
reservoir, continue the inverse, or prove RH.
