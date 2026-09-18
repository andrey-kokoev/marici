# qRB character-weighted Gaussian: prime channel

Use the Fourier convention

$$
\widehat h(x)=\int_{\mathbb R}h(u)e^{ixu}\,du.
$$

For

$$
 h_{t,d}(u)=e^{-tu^2}e^{-idu},
$$

one obtains

$$
\widehat h_{t,d}(x)
=\sqrt{\frac\pi t}\,e^{-(x-d)^2/(4t)}.
$$

For the real character probe, Fourier transformation symmetrizes the two shifts. Therefore the prime contribution is

$$
K_{\rm prime}(t,d)
=-\frac1{4\sqrt{\pi t}}
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\left[
 e^{-(\log n-d)^2/(4t)}
+
 e^{-(\log n+d)^2/(4t)}
\right].
$$

The endpoint term is

$$
K_{\rm endpoint}(t,d)=e^{t/4}\cosh(d/2).
$$

This direct real-character formula is superseded for translate-Gram purposes. Use the exact imaginary-continuation source interface, which fixes the contour and gauge simultaneously.

The gamma term is the corresponding weighted integral of `h_(t,d)` against the archimedean multiplier. Full equality with the relative linking block remains to be checked.
