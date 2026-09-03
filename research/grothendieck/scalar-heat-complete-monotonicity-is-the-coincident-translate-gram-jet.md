# Scalar heat complete monotonicity is the coincident-translate Gram jet

## Difference kernel

Remove the common positive factor from the translated-source Gram matrix and write

\[
K_\sigma(d)
=\left\langle\rho,e^{-2\sigma u^2}e^{-idu}\right\rangle,
\qquad d=a-b.
\]

Equivalently,

\[
K_\sigma(d)
=e^{-d^2/(8\sigma)}
\Theta\!\left(2\sigma,-\frac{id}{4\sigma}\right).
\]

The first two-translate PSD condition is

\[
|K_\sigma(d)|\le K_\sigma(0).
\]

## Coincident derivatives

Differentiation at `d=0` gives

\[
K_\sigma^{(2m)}(0)
=(-1)^m
\left\langle\rho,u^{2m}e^{-2\sigma u^2}\right\rangle.
\]

For the scalar heat slice

\[
\Theta(t,0)=\langle\rho,e^{-tu^2}\rangle,
\]

we also have

\[
\partial_t^m\Theta(t,0)
=(-1)^m
\left\langle\rho,u^{2m}e^{-tu^2}\right\rangle.
\]

Therefore

\[
K_\sigma^{(2m)}(0)
=
\left.\partial_t^m\Theta(t,0)\right|_{t=2\sigma}.
\]

In particular, local maximality of the difference kernel at the coincident translate requires

\[
K_\sigma''(0)=\partial_t\Theta(2\sigma,0)\le0.
\]

The full alternating scalar heat hierarchy is exactly the even coincident-translate jet required by positive definiteness.

## Meaning

This locates the scalar heat projection precisely. It is not faithful enough to prove separated-translate PSD, but it controls every confluent derivative at the Gram diagonal. Failure of complete monotonicity of `Theta(t,0)` produces an immediate local translate-Gram obstruction. Passage leaves all finite nonzero separations unresolved.

The source difference kernel therefore has a nested test order:

1. scalar heat complete monotonicity for coincident jets;
2. the rank-two bound `|K_sigma(d)|<=K_sigma(0)` for every separation;
3. higher finite Toeplitz matrices for all translate tuples;
4. Schwartz-density extension to the full Weil form.

## Disposition

Do not discard the scalar heat hierarchy as irrelevant, and do not promote it to full positivity. It is the exact local jet of the faithful source Gram kernel. The next nonlocal test is the separated rank-two difference inequality above.
