# Inertia ghost traces produce exact dynamical Euler factors

Epistemic-graph event: 1383.

## Determinant theorem

Let `(X,sigma)` be a finite inertia object and let `V_X=Q[X]` be its
permutation representation.  The ghost coordinate is exactly a trace:

`w_r(X,sigma)=|Fix(sigma^r)|=Tr(sigma^r | V_X)`.

The formal determinant identity gives

`Z_(X,sigma)(u)`

`=exp(sum_(r>=1) w_r u^r/r)`

`=det(1-u sigma | V_X)^(-1)`.

If the cycle lengths of `sigma` are `ell_1,...,ell_c`, then

`Z_(X,sigma)(u)=product_j (1-u^ell_j)^(-1)`.

This is a canonical rational dynamical Euler factor derived from the inertia
object; no eigenvalue choices or regularization are required.

## Compatibility with power Frobenius

Powering an `ell`-cycle by `n` splits it into `gcd(ell,n)` cycles of length
`ell/gcd(ell,n)`.  Therefore

`Z_(F_n(X,sigma))(u)`

`=product_j (1-u^(ell_j/gcd(ell_j,n)))^(-gcd(ell_j,n))`.

This agrees with the ghost shift `w_r(F_n)=w_(rn)` and is compatible with
`F_mF_n=F_(mn)`.

The smallest hostile prime control is a `p`-cycle:

`Z_sigma(u)=(1-u^p)^(-1)`,

while

`Z_(F_p sigma)(u)=(1-u)^(-p)`.

The determinant is nontrivial and the prime power operation acts
nontrivially on it.

## Arithmetic audit

This completes the determinant/Euler-factor gate only at the level of finite
dynamics.  It is not yet an arithmetic local factor:

- no source rule canonically assigns an inertia cycle to each intrinsic
  prime;
- the variable `u` has no derived identification with `p^(-s)`;
- cycle multiplicities are permutation fixed-point counts, not counts of
  rational points of a derived finite-field fiber; and
- the `D4_ab` labelled rig remains physically unauthorized.

Thus the result is a genuine construction, not the zeta Euler product.  Its
sharp next gate is a prime-to-inertia attachment functor derived from the
Carrier rather than chosen by cycle length.

## Scope

No geometric Frobenius, finite-field fiber, archimedean factor, analytic
continuation, or global zero spectrum is claimed.
