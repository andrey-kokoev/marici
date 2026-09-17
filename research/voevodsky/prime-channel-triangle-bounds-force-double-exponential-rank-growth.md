# Prime-channel triangle bounds force double-exponential rank growth

For support radius `L`, the autocorrelation reaches prime powers
`n<=X=e^(2L)`. The triangle-bound prime budget is

\[
C_{\rm pr}(L)=\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}.
\]

Partial summation with the prime number theorem `psi(x)~x` gives

\[
\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}
=\frac{\psi(X)}{\sqrt X}
 +\frac12\int_1^X\frac{\psi(t)}{t^{3/2}}dt
\sim 2\sqrt X=2e^L.
\]

The coercive threshold has the form

\[
M(L)\asymp L\exp(2C_{\rm pr}(L)),
\]

apart from lower-order archimedean and boundary constants. Consequently

\[
\log M(L)\sim4e^L,
\qquad
M(L)=\exp((4+o(1))e^L).
\]

Thus treating every prime-power translation by its separate operator norm
cannot provide a practical or uniform `L->infinity` continuation. This is a
structural obstruction, not merely a poor constant at `L=0.55`.

Any viable support-limit argument must retain cancellation in the signed
prime kernel (or invoke an equivalent global arithmetic theorem). Increasing
finite rank while continuing to use the prime-channel triangle inequality
cannot close the form-core gate.
