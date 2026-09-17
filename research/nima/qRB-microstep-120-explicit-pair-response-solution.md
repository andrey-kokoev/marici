# qRB microstep 120: explicit pair-response solution

The first-order pair equation

$$
(\partial_t+\kappa_{nm}t)\rho_{nm}(t)=F_{nm}(t),
\qquad
\rho_{nm}(0)=r_{nm},
$$

has the exact solution

$$
\rho_{nm}(t)
=e^{-\kappa_{nm}t^2/2}
\left[
 r_{nm}+
 \int_0^t e^{\kappa_{nm}s^2/2}F_{nm}(s)\,ds
\right].
$$

This explicitly separates the shell initial value from the forced response. It also shows that the pair-dependent damping coefficient cannot be dropped when defining the wall interface.

The Laplace readout is therefore a well-defined integral on any domain where the displayed solution has sufficient decay. The remaining comparison is to express this readout through the declared wall coordinates and verify the source-fixed endpoint subtraction.

Status: pair response explicitly solved; wall-coordinate realization remains open.
