# qRB microstep 119: pair Laplace equation

For the pair response satisfying

$$
(\partial_t+\kappa_{nm}t)\rho_{nm}=F_{nm},
\qquad
\kappa_{nm}=2\pi\frac{n^2m^2}{n^2+m^2},
$$

and initial value `rho_nm(0)`, define

$$
R_{nm}(z)=\int_0^\infty e^{-zt}\rho_{nm}(t)\,dt.
$$

Integration by parts gives the exact Laplace-side equation

$$
 zR_{nm}(z)-\rho_{nm}(0)-\kappa_{nm}\partial_zR_{nm}(z)
=\int_0^\infty e^{-zt}F_{nm}(t)\,dt.
$$

Thus the pair-to-wall comparison is not a simple multiplier identity: the pair-dependent coefficient becomes a `z`-derivative on the Laplace side. Any scalar wall port must reproduce this differential response or explicitly quotient it.

Status: exact Laplace equation derived; matching it to the existing wall linking functional remains open.
