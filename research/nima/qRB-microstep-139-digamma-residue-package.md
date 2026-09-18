# qRB microstep 139: digamma residue package

When the continuation crosses `u=i/2`, the gamma integral acquires the residue of the pole of

$$
\psi(1/4+iu/2).
$$

The corrected continued gamma channel must therefore be written as

$$
K_{\rm gamma}^{\rm cont}
=K_{\rm gamma}^{\rm shifted}
+K_{\rm residue}^{(0)},
$$

and each further crossing adds the corresponding pole residue. The same residue bookkeeping must be combined with the endpoint term so that the completed source identity remains contour-independent.

The first safe strip is `|d|<2 sigma`; continuation beyond it is piecewise analytic, with jumps represented by explicit finite boundary corrections at each crossed pole.

Status: residue package identified structurally; explicit coefficients and signs remain to be calculated.
