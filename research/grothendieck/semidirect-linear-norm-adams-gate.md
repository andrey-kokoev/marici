# Semidirect linear-norm Adams gate

## Theorem

Let `K` be a finite vector space, let a cyclic quotient act through an
automorphism `A`, and form `G=K semidirect <A>`.  On the fiber over `h`, the
`n`-th power map has linear part

`S_{h,n}=I+A^h+A^(2h)+...+A^((n-1)h)`.

Consequently, coefficient fiber sum and basis-level fiber lift commute with
the `n`-th power operation on that fiber exactly when `S_{h,n}` is invertible.
This makes Ledger 1260's twisted norm explicit for split extensions with
elementary-abelian kernel.

## Odd-index hostile test

Take `K=F_2^2` and

`A=[[0,1],[1,1]]`,

which has order three and no nonzero fixed vector.  The resulting semidirect
product is `A4`, with quotient `A4 -> C3` and kernel `(C2)^2`.  At the odd
index `n=3`,

`S_{1,3}=I+A+A^2=0`.

Thus every point of a nonidentity quotient fiber has the same cube.  The
power map is not fiberwise bijective, even though `gcd(3,exp K)=1` and the
index is odd.

The direct-product control `(C2)^2 x C3 -> C3` has trivial action, so
`S_{1,3}=3I=I` over `F_2` and passes.

## Consequence

The statement "odd Adams indices survive a 2-primary branch kernel" is valid
for the abelian deck system of Ledger 1258 but cannot be exported to a
nonabelian monodromy extension.  There the quotient action and its geometric
sum, not parity alone, decide survival.

## Scope and falsifier

This is algebra on finite split extensions, not a physical relative-chain
pushforward.  It is falsified if exhaustive fiber enumeration disagrees with
the rank of `S_{h,n}`, if `A4 -> C3` passes at `n=3`, or if the direct-product
control fails there.

