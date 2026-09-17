# qRB character target: fourth translation derivative

At `d=0`, the fourth derivative receives all three channel contributions.

The endpoint term is

$$
\partial_d^4K_{\rm endpoint}(t,0)=\frac1{16}e^{t/4}.
$$

The gamma term is

$$
\partial_d^4K_{\rm gamma}(t,0)
=\frac1{4\pi}\int u^4e^{-tu^2}\operatorname{Re}\psi(1/4+iu/2)\,du
-\frac{3\log\pi}{16t^2\sqrt{\pi t}}.
$$

The prime term is

$$
\partial_d^4K_{\rm prime}(t,0)
=-\frac1{2\sqrt{\pi t}}
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 e^{-(\log n)^2/(4t)}
\left(
\frac{(\log n)^4}{16t^4}
-\frac{3(\log n)^2}{4t^3}
+\frac3{4t^2}
\right).
$$

This is the first derivative order where endpoint, gamma, and prime channels all enter simultaneously and can test full normalization coupling.
