# The truncation exponent grid separates off-diagonal and diagonal rates

## Question

Does the degree-four through degree-eight grid support one common relative-decay exponent for both Jacobi coefficients?

Log--log least-squares fits across \(q=3,12,48\) give off-diagonal slopes

\[
-3.0203,\quad-3.0156,\quad-3.0124,
\]

while diagonal slopes are

\[
-2.7252,\quad-2.7217,\quad-2.7194.
\]

The \(n^3\)-rescaled off-diagonal values vary by at most \(1.43\%\) within each tested tail start. The same rescaling does not stabilize the diagonal sequence.

## Disposition

Reject the earlier common-\(n^{-3}\) diagnostic. Retain separate conjectures: an off-diagonal \(n^{-3}\) rate and an unresolved diagonal rate whose finite fitted exponent is near \(2.72\). Both observed exponents exceed one, so either fitted behavior would be summable, but neither is proved.

The next leaf is `diagonal-truncation-exponent`: discriminate whether the diagonal rate approaches \(8/3\), \(11/4\), \(3\), or another value using a longer precision-controlled grid or source asymptotics.

## Claim boundary

Short-window regression does not identify an exact exponent. The values are finite diagnostics and cannot support cocycle perturbation bounds without uniform residual estimates.
