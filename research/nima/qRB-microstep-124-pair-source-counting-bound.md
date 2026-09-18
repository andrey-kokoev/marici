# qRB microstep 124: pair-source counting bound

For a shell bounded away from the endpoint, `a >= a_0 > 0`, the pair source amplitudes obey Gaussian decay of the form

$$
|g_{nm}(a)|
\le e^{-\pi(n^2+m^2)a_0^2}.
$$

Consequently

$$
\sum_{n,m\ge1}|g_{nm}(a)|
\le
\left(\sum_{n\ge1}e^{-\pi n^2a_0^2}\right)^2
<\infty.
$$

Together with `0 < alpha_nm < 1` and the uniform damping floor, this gives absolute pair summability on every shell separated from zero.

The endpoint limit `a_0 downarrow 0` is not covered: theta counting then becomes nonuniform and must be handled by the separately typed endpoint graph.

Status: pair summability closed away from the endpoint; endpoint-uniform summability remains open.
