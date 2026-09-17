# qRB microstep 121: pair Laplace convergence

The explicit solution contains the Gaussian damping factor

$$
 e^{-\kappa_{nm}t^2/2},
 \qquad
\kappa_{nm}=2\pi\frac{n^2m^2}{n^2+m^2}>0.
$$

If the forced term has at most exponential growth after integrating against the damping factor, then `rho_nm` is integrable against every exponential Laplace weight on the admissible half-plane. In particular,

$$
R_{nm}(z)=\int_0^\infty e^{-zt}\rho_{nm}(t)\,dt
$$

is holomorphic there, and differentiation in `z` is justified by dominated convergence.

This closes analytic existence of the pair Laplace readout under the stated growth condition. It does not identify that readout with the scalar wall port.

Status: pair Laplace convergence conditionally closed; wall-coordinate identification remains open.
