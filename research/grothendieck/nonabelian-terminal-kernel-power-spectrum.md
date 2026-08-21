# Nonabelian terminal-kernel power spectrum

## Theorem

For an arbitrary finite group `K`, consider the terminal quotient `q:K->1`.
The `n`-th power correspondence commutes with coefficient fiber sum and
basis-level fiber lift if and only if

`gcd(n,exp(K))=1`.

There is only one fiber, so compatibility says exactly that `x -> x^n` is a
permutation of `K`.  If `n` is coprime to `exp(K)`, choose `a` with
`a*n=1 mod exp(K)`; then `x -> x^a` is its inverse.  Conversely, if a prime
`p` divides both `n` and `exp(K)`, Cauchy's theorem supplies an element of
order `p`, which has the same `n`-th power as the identity.

No commutativity of `K` is used.

## Exact controls

The checker exhausts the power maps of `S3` (exponent six) and the quaternion
group `Q8` (exponent four) for indices `1..24`.  Their survivor spectra are
exactly the indices coprime to six and the odd indices, respectively.

## Scope and falsifier

This proves the nonabelian-kernel theorem only for the terminal quotient.
General nontrivial quotient fibers still involve genuinely twisted word maps.
The operation is basis-linear, not generally a group-ring endomorphism, and
no physical chain transfer is supplied.  Any power permutation disagreeing
with the exponent criterion falsifies the theorem.

