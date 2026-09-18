# qRB microstep 129: heat-weighted endpoint sum

The Gaussian source naturally supplies a heat weight

$$
 w_{nm}(t)=e^{-t(n^2+m^2)},
\qquad t>0.
$$

Then the endpoint bound gives

$$
\sum_{n,m\ge1}|w_{nm}(t)e_{nm,b}|
\le
\frac12\sum_{n,m\ge1}
\frac{e^{-t(n^2+m^2)}}{\sqrt{n^2+m^2}}<\infty.
$$

This produces an absolutely summable endpoint pair observer at every positive heat scale. As `t` tends to zero, the bound is not uniform and the projective endpoint channel must be recovered separately.

Status: source-native heat-regularized endpoint assembly closed; zero-heat limit remains projective/relative.
