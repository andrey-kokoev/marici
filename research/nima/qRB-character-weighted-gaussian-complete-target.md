# qRB character-weighted Gaussian: complete target

For the centered character-weighted probe

$$
h_{t,d}(u)=e^{-tu^2}e^{-idu},
$$

the real completed source target is

$$
\Theta(t,d)=K_{\rm endpoint}(t,d)+K_{\rm gamma}(t,d)+K_{\rm prime}(t,d).
$$

The three channels are

$$
K_{\rm endpoint}(t,d)=e^{t/4}\cosh(d/2),
$$

$$
K_{\rm gamma}(t,d)
=-\frac{\log\pi}{4\sqrt{\pi t}}e^{-d^2/(4t)}
+\frac1{4\pi}\int_{\mathbb R}e^{-tu^2}\cos(du)\operatorname{Re}\psi(1/4+iu/2)\,du,
$$

and

$$
K_{\rm prime}(t,d)
=-\frac1{4\sqrt{\pi t}}
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\left[
 e^{-(\log n-d)^2/(4t)}+
 e^{-(\log n+d)^2/(4t)}
\right].
$$

This real-character formula is superseded for the translate-Gram interface. Use the exact imaginary-continuation formula from `source-translate-weil-gram-is-imaginary-character-continuation-of-theta.md` instead.
