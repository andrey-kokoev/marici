# The Critical Half-Density Is the Return Amplitude of a Unitary-Dilated Prime Loop

## Closed prime circles have the wrong repetition amplitude

The closed circle of circumference $L_p=\log p$ gives the correct return times
and primitive weight, but every traversal has modulus one. In the centered
coordinate

$$
s=\frac12+z,
$$

the local Euler factor is

$$
(1-p^{-1/2}e^{-zL_p})^{-1}.
$$

Its $k$-fold return carries amplitude

$$
p^{-k/2}.
$$

A fixed spectral functional on an isolated closed circle produces a periodic
distribution, so it cannot assign geometrically decaying amplitudes to
successive periods. A time-dependent regularization could do so but would
violate source authority and Nima's fixed-functional gate.

## Canonical contraction and unitary dilation

Set

$$
r_p=p^{-1/2}.
$$

Regard one traversal of the prime loop as the scalar contraction $T_p=r_p$ on
its internal return channel. By the Sz.-Nagy dilation theorem it has a
canonical minimal unitary dilation $U_p$ with fixed embedding $J_p$ such that

$$
J_p^*U_p^kJ_p=r_p^k,
\qquad k\ge0.
$$

An explicit model uses multiplication by $e^{i\theta}$ on
$L^2(S^1,d\mu_{r_p})$, where

$$
d\mu_r(\theta)
=\frac{1-r^2}{|e^{i\theta}-r|^2}\frac{d\theta}{2\pi}.
$$

For the fixed vector $\Omega=1$,

$$
\langle\Omega,U_p^k\Omega\rangle=r_p^k
$$

for $k\ge0$. The functional

$$
\tau_p(B)=\langle\Omega,B\Omega\rangle
$$

is linear, positive, independent of return time, and adjoint compatible. All
attenuation comes from repeated unitary dynamics followed by the same fixed
internal-channel observation.

Suspending one application of $U_p$ over the geometric delay $L_p$ gives the
positive-return distribution

$$
W_p(t)
=(\log p)\sum_{k\ge1}p^{-k/2}\delta(t-k\log p).
$$

Summing primes yields the centered von Mangoldt current

$$
W_{\mathbb P}(t)
=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\delta(t-\log n).
$$

This is the exact arithmetic distribution appearing after centering on the
critical half-density.

## Transfer and determinant

The fixed-channel return transfer is

$$
\sum_{k\ge0}r_p^ke^{-zkL_p}
=\frac1{1-p^{-1/2}e^{-zL_p}}
=\frac1{1-p^{-(1/2+z)}}.
$$

Thus the centered Euler factor is the transfer function of the unitary-dilated
prime loop. Its logarithmic derivative is the Laplace transform of $W_p$.

The half-offset has acquired an operator meaning:

> The critical factor $p^{-1/2}$ is the internal return amplitude of the
> minimal unitary dilation, equivalently the square root of the local escape
> probability normalization.

It is not inserted as an external spectral shift.

## Fixed-functional audit

The construction passes the local gates:

- the dilation generator is self-adjoint;
- $\tau_p$ is one fixed functional on its functional calculus;
- $\tau_p$ is independent of $t$, $z$, and cutoff;
- adjoints send positive to negative returns through complex conjugation;
- the $k=1$, $k=2$, and $k\ge3$ currents are the first, second, and remaining
  return depths of the same dilation;
- finite prime sums are compatible under direct-sum inclusion.

## Remaining global obstruction

The local dilations add an environment channel for every prime. Their direct
sum still has the wrong global spectral content and severe completion
multiplicity. A valid RH operator must perform an adelic global coupling that:

1. identifies the source-derived combination of all defect channels;
2. introduces the continuum and archimedean reference evolution;
3. produces a fixed global functional rather than a cutoff-dependent trace;
4. retains the centered return distribution above;
5. cancels the elementary local dilation spectra in the relative trace;
6. yields framed Xi as the normalized relative determinant;
7. leaves one self-adjoint global spectrum.

The immediate falsifier is implementability. If the tensor or restricted sum
of the local dilation vacua fails the exact infinite-product criterion without
a source-derived reference change, then the half-density construction remains
local and cannot be promoted to the global trace formula.
