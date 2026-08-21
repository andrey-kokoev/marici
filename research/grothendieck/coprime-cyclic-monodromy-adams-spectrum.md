# Coprime cyclic-monodromy Adams spectrum

## Classification

Let `K=F_p^r`, let `A in GL(K)` have finite order `m` with `gcd(p,m)=1`,
and form the faithful split extension `G=K semidirect C_m`.  For the quotient
`q:G -> C_m`, the `n`-th power operation commutes with coefficient fiber sum
and basis-level fiber lift on every quotient fiber if and only if

`gcd(n,p*m)=1`.

Indeed, on fiber `h` the twisted norm is the geometric sum

`S_{h,n}=I+A^h+...+A^((n-1)h)`.

Because the action order is prime to `p`, `A` is semisimple after extending
scalars.  On an eigenvalue `lambda` of `A^h`, the norm eigenvalue is
`1+lambda+...+lambda^(n-1)`.  It vanishes when `lambda != 1` and
`lambda^n=1`, or when `lambda=1` and `p` divides `n`.  Requiring nonvanishing
for every fiber gives exactly coprimality with both `p` and the faithful
action order `m`.

## A4 spectrum

For `A4=(C2)^2 semidirect C3 -> C3`, the globally compatible indices are
exactly those coprime to six.  Ledger 1263's hostile index `n=3` is the first
odd failure; even indices already fail on the identity fiber.

## Exact controls

The checker exhausts:

- `(C2)^2 semidirect C3` with its irreducible order-three action;
- `C3 semidirect C2` with inversion;
- `C5 semidirect C4` with multiplication by two.

For indices `1..24`, direct fiber enumeration agrees with `gcd(n,p*m)=1` in
all three families.

## Scope and falsifier

The theorem requires an elementary-abelian kernel, a cyclic faithful action,
and action order prime to the kernel characteristic.  It is an algebraic
correspondence result, not a physical chain transfer.  Any enumerated index
whose global compatibility disagrees with `gcd(n,p*m)=1` falsifies it.

