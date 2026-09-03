# Imaginary-character Weil continuation closes termwise

## Substitution

In the materialized shifted-Gaussian formula substitute

\[
t=2\sigma,
\qquad
\xi=-\frac{id}{4\sigma},
\qquad d=a-b,
\]

and multiply by the Gram prefactor

\[
4\pi\sigma e^{-d^2/(8\sigma)}.
\]

## Endpoint term

The shifted endpoint is

\[
e^{t/4-t\xi^2}\cos(t\xi).
\]

After substitution and multiplication by the exponential Gram factor, its nonconstant part becomes

\[
e^{\sigma/2}\cosh(d/2).
\]

This agrees with direct evaluation of the character-weighted centered Gaussian at the two polar points `u=+/- i/2`.

## Prime term

For `L=log n`, the continued damping is

\[
e^{-(L^2+d^2)/(8\sigma)}
\cosh\!\left(\frac{dL}{4\sigma}\right)
=
\frac12\left[
 e^{-(L-d)^2/(8\sigma)}
+e^{-(L+d)^2/(8\sigma)}
\right].
\]

Thus the imaginary-character continuation produces the expected pair of source-translation Gaussian weights at the prime displacements `+/- log n`. Absolute convergence holds for every fixed positive `sigma` and finite `d` because quadratic Gaussian decay in `L` dominates the von Mangoldt growth.

## Gamma term

The same completed square gives

\[
e^{-d^2/(8\sigma)}
 e^{-2\sigma(u+i d/(4\sigma))^2}
=
 e^{-2\sigma u^2-idu}.
\]

Hence the continued digamma integral is exactly the character-weighted centered Gaussian pairing, without a contour displacement. Its integrand remains absolutely integrable because the Gaussian dominates the logarithmic vertical growth of the digamma factor.

## Conclusion

Endpoint, gamma, and prime sectors all match the Fourier-transformed source-translation probe with `t=2 sigma`. The interface therefore closes termwise under the already fixed explicit-formula convention. The Gram matrix is

\[
G_{ij}=4\pi\sigma e^{-(a_i-a_j)^2/(8\sigma)}
\Theta\!\left(2\sigma,-\frac{i(a_i-a_j)}{4\sigma}\right).
\]

Hermitian symmetry follows by exchanging `i,j`, which conjugates the character.

## Disposition

The Fourier comparison and convergence gates are closed. The sole remaining statement for this fixed-width dense Gaussian family is PSD of every finite difference-kernel matrix above. That statement is equivalent, after the established density extension, to positivity of the completed Weil form and hence remains RH-strength.
