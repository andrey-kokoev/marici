# Common scaling-ray renormalization of theta autocorrelation

At finite label cutoff `N`, group the double sum by

$$
(n,m)=(da,db),
\qquad (a,b)=1.
$$

For fixed coprime `(a,b)`, put

$$
r_{a,b}(t)=\frac ba e^t
$$

and let `kappa(r)` be the universal ratio profile. Since the summand is

$$
\frac{e^{t/2}}{da}\kappa(r_{a,b}(t)),
$$

the ray contribution is

$$
\frac{e^{t/2}}a\kappa(r_{a,b}(t))
H_{\lfloor N/\max(a,b)\rfloor},
$$

where `H_M` is the harmonic number.

Using

$$
H_M=\log M+\gamma+o(1),
$$

the divergent part is

$$
\frac{e^{t/2}}a\kappa(r_{a,b}(t))\log N.
$$

After subtracting this common cutoff divergence, the raywise finite part is

$$
\frac{e^{t/2}}a\kappa(r_{a,b}(t))
\left(\gamma-\log\max(a,b)\right).
$$

Thus the scaling divergence and its finite normalization are explicit. Euler's constant appears from the common dilation multiplicity, while `log max(a,b)` records the primitive coprime-ray scale.

This is a raywise renormalization only. It does not prove convergence of the subsequent sum over coprime pairs `(a,b)`. That sum must still be controlled in the source projective topology and matched with seam and archimedean countercurrents.

The calculation supplies a concrete candidate for the primitive anomaly line in the two-height forcing reservoir: it is the coefficient of `log N` under common label dilation. Any completed current decomposition must subtract the same coefficient and retain the displayed finite part.

Status: common scaling-ray divergence and finite part computed exactly; coprime-ray completion and source counterterm identification remain open.
