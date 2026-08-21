# Finite-monodromy exponent Adams spectrum

## Theorem

Let a finite group `H` act faithfully on `K=F_p^r`, and form
`G=K semidirect H -> H`.  The `n`-th power map preserves every coefficient
fiber-sum and basis-level fiber-lift square if and only if

`gcd(n,p*exp(H))=1`.

For `h in H`, the power map on the fiber over `h` has linear part

`S_{h,n}=I+rho(h)+...+rho(h)^(n-1)`.

If `p` divides `n`, the identity fiber fails.  If another prime divides both
`n` and `exp(H)`, Cauchy's theorem supplies an element of that prime order;
faithfulness makes its action nontrivial, and a corresponding root-of-unity
eigenvalue kills the geometric sum.  Conversely, coprimality with
`p*exp(H)` makes every scalar geometric sum nonzero; Jordan corrections do
not affect its determinant.

The quotient need not be abelian.  In that case the power map is only a
basis-level linear operation on the group algebra, not a ring Adams
endomorphism; the theorem concerns the Mackey correspondence square alone.

## Exact controls

- the faithful reflection representation `S3 -> GL(2,F5)`, with exponent 6;
- the faithful diagonal representation `V4 -> GL(2,F3)`, with exponent 2.

Through index 24, their global survivor spectra are exactly the indices
coprime to 30 and 6, respectively.

## Scope and falsifier

The kernel is elementary abelian and the action faithful, but the quotient is
arbitrary finite.  No physical chain pushforward is supplied.  Any exact
fiber result disagreeing with the exponent criterion falsifies the theorem.

