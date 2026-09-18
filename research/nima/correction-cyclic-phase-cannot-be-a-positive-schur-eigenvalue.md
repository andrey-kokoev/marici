# Correction: cyclic phase cannot be a positive Schur eigenvalue

On the critical seam

$$
s=\frac12+it,
$$

the cyclic Adams-two factor is

$$
p^{-2s}=p^{-1}e^{-2it\log p},
$$

which is nonreal for generic `t`.

A positive conservative Schur return in the Hermitian lane is self-adjoint and nonnegative. Every eigenvalue on that lane is real and nonnegative. Therefore the literal equation

$$
R_{\rm cons}w_\theta=p^{-2s}w_\theta
$$

cannot hold generically.

The cyclic trace and conservative energy belong to different variances:

- analytic/determinant lane: the holomorphic phase `p^(-2s)`;
- Hermitian Green lane: the energy covariance
  $$
  |p^{-2s}|=p^{-2\operatorname{Re}s}.
  $$

The valid comparison must retain the phase in the Tate/determinant line and compare only its Hermitian modulus with the positive return, or use a two-lane pairing whose analytic transpose readout is `p^(-2s)` and Hermitian quadratic readout is `p^(-2 Re s)`.

Thus the correct positive seam equation is of the form

$$
R_{\rm cons}^{\rm Herm}w_\theta
=p^{-2\operatorname{Re}s}w_\theta,
$$

while the line transition separately records `p^(-2it log p)`. Identifying these two equations as one scalar operator identity would erase the determinant-line phase.

This retracts the literal complex-eigenvalue target in the preceding Schur-return notes. Quarter-turn covariance still transfers the Hermitian modulus equation from the even to the odd line.

Status: variance mismatch corrected; remaining gate is a two-lane conservative/cyclic comparison preserving both positive modulus and analytic phase.
