# The first analytic two-prime bad-set cover exposes a million-dimensional Schur gate

At `L=0.55` and `delta=1/40`, use the proved lower bound

\[
g(u)=\frac{\Re\psi(1/4+iu/2)-\log\pi}{4\pi}
\ge\frac{\log(u/2)-3/2-\log\pi}{4\pi}.
\]

Write `c_p=log(p)/sqrt(p)`. If

\[
g(u)-c_2\cos(u\log2)-c_3\cos(u\log3)<\delta,
\]

then necessarily

\[
c_2\cos(u\log2)>g_{\rm lower}(u)-\delta-c_3.
\]

Partitioning into complete periods of the `2`-phase and using the left-endpoint
lower bound produces an explicit cover of the bad set. Floating evaluation of
this analytic cover gives

\[
|\Omega_{L,\delta}|\le 1.7356\times10^7
\]

before directed rounding, and therefore a concentration trace bound around

\[
\frac{L}{\pi}|\Omega_{L,\delta}|
\le3.04\times10^6.
\]

The constants can be promoted to directed bounds, but doing so would not make
the resulting dense Schur certificate useful. Joint `2`--`3` phase cells can
shrink the cover, yet the direct grid scout already finds bad-set measure
about `4431` inside radius only `10000`; the growth is not solely an artifact
of the one-phase relaxation.

Thus the first-prime 25-dimensional certificate does not scale naively across
the next source threshold. A viable continuation needs a structured sparse
or block certificate exploiting the quasiperiodic phase cells, not one basis
vector per time-frequency concentration degree.
