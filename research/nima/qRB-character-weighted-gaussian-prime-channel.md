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

Therefore the prime contribution to the centered explicit formula is

$$
K_{\rm prime}(t,d)
=-\frac1{2\sqrt{\pi t}}
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 e^{-(\log n-d)^2/(4t)}.
$$

The endpoint term is

$$
K_{\rm endpoint}(t,d)=e^{t/4}\cosh(d/2).
$$

This calculation resolves the interface ambiguity: a character in the spectral variable becomes a translation of the Gaussian weight in the logarithmic prime coordinate. It is not obtained by inserting `d` into the shifted-real-Gaussian formula.

The gamma term is the corresponding weighted integral of `h_(t,d)` against the archimedean multiplier. Full equality with the relative linking block remains to be checked.
