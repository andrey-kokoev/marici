# Mellin regularization is the prime-compatible completion of the ratio kernel

The source-ordered ratio sum is conditionally cancelled and cannot be regrouped directly by gcd or prime grade. Introduce the multiplicative regulator

$$
A_{\Phi,\varepsilon}(t)
=e^{t/2}
\sum_{n,m\ge1}
\frac{\kappa(me^t/n)}{n^{1+\varepsilon}m^{\varepsilon}}.
$$

For `Re(epsilon)` sufficiently large this is absolutely convergent, so one may:

1. group `(n,m)` by common gcd;
2. factor labels into prime powers;
3. separate primitive, square, and connected grades;
4. apply reciprocal exchange without changing the value.

Along `(n,m)=(da,db)`, the dilation factor is

$$
\sum_{d\ge1}d^{-1-2\varepsilon}
=\zeta(1+2\varepsilon).
$$

Thus the common scaling anomaly is isolated as the standard zeta pole

$$
\zeta(1+2\varepsilon)
=\frac1{2\varepsilon}+\gamma+O(\varepsilon).
$$

This reproduces the finite-cutoff logarithm and Euler constant in a multiplicative, prime-compatible frame.

The completed autocorrelation should be defined by meromorphic continuation and finite part:

$$
A_\Phi^{\rm ren}(t)
=\operatorname{FP}_{\varepsilon=0}A_{\Phi,\varepsilon}(t).
$$

The zero-mass identity for `kappa` is the expected cancellation mechanism for the aggregate residue after summing primitive ratio classes. This cancellation must be proved in the regulated arithmetic topology; it cannot be inferred by exchanging divergent sums.

Because `n^{-epsilon}` and `m^{-epsilon}` factor over prime powers, this regulator is compatible with the common logarithmic operator and determinant-line grading. It supplies a precise bridge between source-ordered Euler–Maclaurin completion and primitive/square/connected current decomposition.

Required comparison theorem:

$$
\operatorname{FP}_{\varepsilon=0}A_{\Phi,\varepsilon}(t)
=A_\Phi(t)
$$

in the completed source distribution space, together with equality of the Laurent coefficients to the seam and archimedean anomaly currents.

Status: canonical prime-compatible regulator identified; meromorphic continuation and comparison with the original theta autocorrelation remain open.
