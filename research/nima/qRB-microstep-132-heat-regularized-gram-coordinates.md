# qRB microstep 132: heat-regularized Gram coordinates

For a finite translate set `a_1,...,a_r`, define the heat-regularized Gram coordinates by applying the source target to the midpoint probes:

$$
G_t(a_i,a_j)
=e^{-t(a_i-a_j)^2/4}
\Theta\left(t,\frac{a_i+a_j}{2}\right).
$$

At every `t>0`, these are finite source coordinates. The projective zero-heat object is the compatible coordinatewise limit when it exists.

This connects the heat-weighted endpoint family to the spectral observer without asserting positive semidefiniteness of the limiting matrices.

Status: finite heat-regularized Gram coordinates defined; positivity and zero-heat matrix convergence remain separate gates.
