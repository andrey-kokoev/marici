# Source Dyson normalization supplies the Cut Kraus trace balance

For each labelled production channel, Entry 1616 fixes

\[
C_r=-i(H_r-S_r).
\]

The source exponential simultaneously supplies the second-order no-production
coefficient.  In Kraus language,

\[
K_0
=
I-igH_{\rm coh}
-\frac{g^2}{2}
\left(H_{\rm coh}^2+\sum_r C_r^\dagger C_r\right)
+O(g^3),
\]

and

\[
K_r=gC_r+O(g^2).
\]

Consequently,

\[
K_0^\dagger K_0+sum_rK_r^\dagger K_r
=I+O(g^3).
\]

At order \(g^2\), the virtual/no-production trace coefficient is

\[
-\sum_rC_r^\dagger C_r,
\]

and the labelled Cut coefficient is the opposite positive term.  Their sum
vanishes without fitting an anti-Hermitian correction.

Channelwise, endpoint sewing gives

\[
|H-S|^2
=|H|^2-2\operatorname{Re}(H\bar S)+|S|^2,
\]

so the algebraic coefficients are \((1,-2,1)\) in the norm expansion.  The
unsigned location multiplicities remain \((1,2,1)\); the mixed minus sign is
carried by the source amplitude, while the occurrence-resolved four cells
retain their Hermitian pairing.

The finite checker verifies the complex endpoint identity and trace balance.
The result is perturbative through second order; it does not construct the
complete finite-time CPTP channel at all interaction orders.
