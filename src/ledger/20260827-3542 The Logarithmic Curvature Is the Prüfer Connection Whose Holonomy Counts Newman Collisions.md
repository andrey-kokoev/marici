# The Logarithmic Curvature Is the Prüfer Connection Whose Holonomy Counts Newman Collisions

For the native collision section

\[
G(\lambda,x)=H_\lambda(x)+iH_x(\lambda,x),
\]

the phase connection \(\omega=d\arg G\) has components

\[
\omega_x=\frac{HH_{xx}-H_x^2}{H^2+H_x^2},
\qquad
\omega_\lambda=\frac{H_xH_{xx}-HH_{xxx}}{H^2+H_x^2}.
\]

Thus the recurring logarithmic curvature and derivative Wronskian are the two
components of one Prüfer connection. It is flat away from collisions and has
quantized negative curvature at every generic collision. Its four-edge
holonomy equals minus the collision count.

Pointwise curvature positivity is therefore stronger than needed. The actual
RH target is zero complete holonomy on the nonnegative Newman strip, with the
height-wall infinity ports retained.

Research packet:
`research/grothendieck/the-logarithmic-curvature-is-the-prufer-connection-whose-holonomy-counts-newman-collisions.md`

Checker:
`research/grothendieck/checkers/check_newman_prufer_connection_curvature_identity.py`

The dependency-free checker passes 16/16 gates.