# Modular cyclic-monodromy Adams spectrum

## Strengthened theorem

Let `K=F_p^r`, let `A in GL(K)` have arbitrary finite order `m`, and form the
faithful split extension `G=K semidirect C_m`.  No coprimality assumption on
`p` and `m` is needed.  The `n`-th power operation commutes with coefficient
fiber sum and basis-level fiber lift on every quotient fiber exactly when

`gcd(n,p*m)=1`.

On fiber `h`, the twisted norm remains

`S_{h,n}=I+A^h+...+A^((n-1)h)`.

Over an algebraic closure, its determinant is the product of the scalar
geometric sums on the eigenvalues of `A^h`; nilpotent Jordan corrections do
not change this determinant.  If `p` divides `n`, the identity fiber already
fails.  If a prime other than `p` divides both `n` and the action order, a
quotient fiber exposes an eigenvalue of that prime order and its geometric
sum vanishes.  Conversely, coprimality with `p*m` prevents both mechanisms.

## Modular controls

Two genuinely nonsemisimple actions test the removed hypothesis:

- `F_2^2 semidirect C2`, with unipotent matrix `[[1,1],[0,1]]`;
- `F_3^2 semidirect C3`, with the same Jordan form in characteristic three.

For indices `1..24`, exhaustive fiber enumeration gives precisely the odd
indices in the first family and precisely the indices prime to three in the
second.  Both agree with `gcd(n,p*m)=1`.

## Scope and falsifier

The kernel remains elementary abelian and the quotient cyclic; only the
coprime-action restriction is removed.  This is an algebraic correspondence
theorem and does not create a physical chain transfer.  Any modular family or
index whose fiberwise result disagrees with the gcd criterion falsifies it.

