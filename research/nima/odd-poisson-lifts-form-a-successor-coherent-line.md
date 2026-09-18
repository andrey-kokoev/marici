# Odd Poisson lifts form a successor-coherent line

For every `L>0`, let

$$
d_L(x)=\frac1{\sqrt2}
\frac{\sinh(x/2)}{\sinh(L/2)}
$$

be the normalized odd harmonic lift on `[-L,L]`. Let

$$
\mathcal P_L^{\rm odd}=\mathbb C d_L.
$$

For two lengths `L,M>0`, define the successor map on the odd harmonic line by analytic restriction/extension followed by endpoint renormalization:

$$
S_{L\to M}f(x)
=rac{\sinh(L/2)}{\sinh(M/2)}f(x),
\qquad f\in\mathcal P_L^{\rm odd},
$$

where the unique harmonic analytic continuation is understood when the target interval is larger.

Then

$$
S_{L\to M}d_L=d_M.
$$

For any `L,M,N>0`,

$$
S_{M\to N}S_{L\to M}=S_{L\to N},
\qquad
S_{L\to L}=I.
$$

Thus the odd Poisson lifts form a flat one-dimensional successor system. Every successor preserves the normalized endpoint vector and intertwines the shifted-Laplacian equation because all fibers lie in `ker(partial_x^2-1/4)`.

The energy changes with the fiber metric:

$$
\|d_L\|_{G_P}^2
=\frac{\sinh L-L}{2\sinh^2(L/2)}<1.
$$

Therefore the transport is metric-compatible when each harmonic line is assigned its source-pulled endpoint normalization; it is not an isometry for the unrescaled ambient `L2` graph norms across different interval lengths.

This closes successor coherence for the rank-one odd Poisson/Douglas vector. It does not give a uniform strict margin as `L->infinity`, where the leverage approaches one.

Status: successor-natural odd Poisson line constructed with exact cocycle; completion transversality at the limiting semidefinite boundary remains open.
