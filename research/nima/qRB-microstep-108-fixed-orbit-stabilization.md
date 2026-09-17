# qRB microstep 108: fixed-orbit stabilization

The source record constructs one bounded `J_link` on the completed response orbit `H_orb`. On that fixed carrier, `G_link` is one bounded operator, so a nonzero scalar stabilization exists:

$$
0<\lambda<\|G_{\rm link}\|^{-1}.
$$

The uniform-lambda problem arises only if one insists on a family of distinct regulator-dependent linking operators before passing to the completed orbit.

Thus the fixed-orbit relative construction does not need a regulator-uniform norm estimate for `J_link`. The remaining regulator issue concerns convergence of finite presentations to that fixed operator.

Status: fixed-orbit stabilization available conditionally on the constructed bounded `J_link`; pre-completion presentation convergence remains separate.
