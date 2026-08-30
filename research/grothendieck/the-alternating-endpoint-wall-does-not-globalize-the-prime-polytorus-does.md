# The Alternating Endpoint Wall Does Not Globalize; the Prime Polytorus Does

## Status

This is a scope correction to the reciprocal-quartic interval theorem. That
theorem remains exact on one equally spaced valuation chain. Its endpoint
`w=-1`, however, is not a global theta/Tate boundary point once distinct prime
labels are retained.

## Why the endpoint is only chart-local

For a single prime `p`, the spectral character is

\[
w_p=p^{-z}.
\]

On the critical seam `Re(z)=0`, write `z=it`. The alternating endpoint of this
one-prime chart is reached when

\[
p^{-it}=-1,
\qquad
t\log p=(2k+1)\pi.
\]

Two distinct primes cannot reach that endpoint at the same spectral height.
Indeed, common antiphase for distinct primes `p` and `q` would imply

\[
(2k+1)\log q=(2\ell+1)\log p,
\]

and hence

\[
q^{2k+1}=p^{2\ell+1},
\]

contradicting unique factorization. Thus `P(-1)>=0` is a legitimate wall for a
single prime-power chain, but it cannot be the global theta wall.

## The source-native global geometry

Retain one coordinate for every prime:

\[
w_p=p^{-z}.
\]

An integer label `n` then determines the valuation monomial

\[
w^{v(n)}=\prod_p w_p^{v_p(n)}.
\]

Multiplication of integer labels becomes multiplication of monomials because
`v_p(mn)=v_p(m)+v_p(n)`. The three spectral regions become:

- `Re(z)>0`: every `|w_p|<1`, the prime polydisk;
- `Re(z)=0`: every `|w_p|=1`, the prime polytorus;
- `Re(z)<0`: every `|w_p|>1`, the reciprocal exterior.

The half-plane split is therefore the diagonal shadow of an infinite
multivariable inside/boundary/outside geometry. The seam is not one endpoint;
it is the whole prime polytorus.

## Corrected theorem-shaped target

Let `F_X((w_p)_{p in X})` be a finite, source-derived prime-labelled
generating object. A sufficient global mechanism would have two parts:

1. `F_X` is nonzero whenever `|w_p|<1` for every `p in X`.
2. Reciprocal completion transports this stability to the simultaneous
   exterior chamber.

Then the diagonal spectral embedding `w_p=p^{-z}` is zero-free away from the
unit-polytorus seam. A compatible cutoff limit could yield the corresponding
statement for the completed source.

This is a target, not a theorem about `Xi`. In particular, simultaneous
inversion of all prime coordinates may preserve mixed invariants. Separate
one-prime quotient coordinates do not automatically describe the global
invariant ring.

## Hostile tests

Coefficient positivity is insufficient. Already

\[
F(u,v)=1+4uv
\]

has positive coefficients and stable coordinate-axis restrictions
`F(u,0)=F(0,v)=1`, yet it vanishes at `u=v=i/2` inside the bidisk. Hence even
perfect one-prime tests can miss a mixed-prime zero.

The source theorem must therefore constrain mixed-prime incidence. This makes
the labelled interaction port structurally necessary: it is not auxiliary
bookkeeping added after one-variable stability.

## Explanation gained

The failed globalization identifies what the earlier reduction was hiding.
The reciprocal quartic compressed several independent valuation axes into one
scale coordinate. Undoing that compression rotates the problem from a Jacobi
interval to a Lee--Yang-type prime polydisk. The next useful question is not
whether every one-prime alternating wall is positive, but which theta/Tate
constructor restricts all mixed-prime monomials strongly enough to produce
multivariate stability.

## Falsifier

The proposed route fails at the first finite prime set `X` for which the exact
source-derived `F_X` has a zero with every `|w_p|<1`. It also fails if its
claimed stability follows only after erasing mixed-prime labels or choosing a
one-variable diagonal before proving the multivariate statement.
