# qRB character target: all translation derivatives

For the centered character probe, the prime Gaussian factor is

$$
 e^{-(x-d)^2/(4t)},
 \qquad x=\log n.
$$

Its `m`-th derivative is

$$
\partial_d^m e^{-(x-d)^2/(4t)}
=(2\sqrt t)^{-m}H_m\left(\frac{x-d}{2\sqrt t}\right)e^{-(x-d)^2/(4t)},
$$

where `H_m` is the physicists' Hermite polynomial.

Therefore all translation jets of the prime channel are explicit weighted Hermite moments. Endpoint and gamma jets are obtained by differentiating `cosh(d/2)` and `cos(du)` respectively.

This gives a finite algorithm for every jet order and preserves the endpoint–gamma–prime coupling. Odd jets isolate the prime-sensitive asymmetry at the origin; even jets mix all channels.

Status: all-order Gaussian translation-jet interface closed formally; comparison with the relative linking block remains the source-compatibility gate.
