# qRB microstep 137: imaginary-continuation component check

Set `t=2 sigma` and `xi=-i d/(4 sigma)`. The source translate-Gram gauge is

$$
 e^{-d^2/(8\sigma)}\Theta(2\sigma,\xi).
$$

For the shifted-Gaussian endpoint term,

$$
 e^{-d^2/(8\sigma)}e^{t/4-t\xi^2}\cos(t\xi)
=e^{\sigma/2}\cosh(d/2).
$$

For each prime-power displacement `L=log n`, the shifted prime factor becomes

$$
 e^{-d^2/(8\sigma)}e^{-L^2/(8\sigma)}\cosh\left(\frac{dL}{4\sigma}\right)
=\frac12\left[e^{-(L-d)^2/(8\sigma)}+e^{-(L+d)^2/(8\sigma)}\right].
$$

Thus the imaginary continuation reproduces the symmetric real-character prime factor, while simultaneously fixing the endpoint gauge.

Status: endpoint and prime component normalization verified algebraically; the digamma contour continuation remains the only component-level check.
