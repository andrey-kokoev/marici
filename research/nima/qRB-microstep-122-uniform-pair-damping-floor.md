# qRB microstep 122: uniform pair damping floor

For positive integer labels `n,m`,

$$
\frac{n^2m^2}{n^2+m^2}\ge\frac12,
$$

because `n,m >= 1` and `n^2+m^2 <= 2n^2m^2`. Hence

$$
\kappa_{nm}
=2\pi\frac{n^2m^2}{n^2+m^2}
\ge\pi.
$$

Every ordered pair response therefore has at least the common Gaussian damping

$$
 e^{-\pi t^2/2}.
$$

This gives a label-uniform Laplace convergence envelope, provided the forcing amplitudes have a compatible uniform growth bound. It is stronger than pairwise existence and is the first useful estimate for summing the pair-response family.

Status: uniform damping floor proved; uniform forcing-amplitude and pair-to-wall summability remain open.
