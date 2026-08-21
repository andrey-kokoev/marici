# The intrinsic-prime diagonal operator realizes the Euler product

Epistemic-graph event: 1391.

## Global operator family

Let `P` be the intrinsic prime locus of the conditional initial semiring and
form the explicitly analytic Hilbert realization

`H_P=ell^2(P)`.

On its natural domain define the positive diagonal operator

`N e_p=p e_p`.

For complex `s`, functional calculus gives

`N^(-s)e_p=p^(-s)e_p`.

If `Re(s)=sigma>1`, then

`sum_p |p^(-s)|=sum_p p^(-sigma)<infinity`,

so `N^(-s)` is trace class.  Its Fredholm determinant is exactly

`det(1-N^(-s))=product_p(1-p^(-s))=zeta(s)^(-1)`.

The logarithmic derivative is the prime-power trace formula

`d/ds log det(1-N^(-s))`

`=sum_(p,k>=1) (log p)p^(-ks)=-zeta'(s)/zeta(s)`.

Thus the intrinsic primes admit a genuine noncircular global operator family
whose determinant realizes the Euler product in its convergent domain.

## Trace-class boundary

The trace norm diverges for `Re(s)<=1`.  Therefore the same Fredholm
determinant construction does not cross the line where continuation becomes
necessary.

This is structurally unavoidable for this family.  At a nontrivial zero of
`zeta`, `zeta(s)^(-1)` has a pole, whereas a Fredholm determinant of a
holomorphic trace-class family is holomorphic.  Consequently no holomorphic
trace-class continuation of `N^(-s)` can retain the identity
`det(1-N^(-s))=zeta(s)^(-1)` through a zeta zero.

## Spectrum audit

The spectrum of `N` is the set of intrinsic prime values, and the spectrum of
`log N` is `{log p}`.  Neither is the set of imaginary parts of zeta zeros.
The zeros occur as singularities of the analytically continued determinant,
not as eigenvalues of this prime-diagonal operator.

The Hilbert completion and complex functional calculus are archimedean input,
while the basis index and eigenvalue classes come from the conditional
intrinsic-prime semiring.

## Scope

This constructs the global Euler determinant only for `Re(s)>1`.  It does not
provide a Hilbert--Polya operator, analytic continuation of the determinant,
or a physical Carrier realization.
