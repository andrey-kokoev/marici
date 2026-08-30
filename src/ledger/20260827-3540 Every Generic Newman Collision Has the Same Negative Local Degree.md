# Every Generic Newman Collision Has the Same Negative Local Degree

For the coupled collision map

\[
\mathcal F(\lambda,x)=
(H_\lambda(x),\partial_xH_\lambda(x)),
\]

the Newman equation gives, at every generic collision,

\[
\det D\mathcal F=-(H_{xx})^2<0.
\]

Thus every collision has local Brouwer degree \(-1\). Multiple generic
collisions cannot cancel in the global boundary winding.

On any bounded heat-time/height rectangle whose boundary is collision-free,
the negative winding of \(H+iH_x\) exactly counts the collisions inside. This
replaces a two-dimensional interior search by one four-edge boundary
observable. The remaining gates are deriving that boundary phase from theta
and proving compatibility of the integer degrees under height exhaustion.

Research packet:
`research/grothendieck/every-generic-newman-collision-has-the-same-negative-local-degree.md`

Checker:
`research/grothendieck/checkers/check_newman_collision_map_uniform_local_degree.py`

The dependency-free checker passes 38/38 gates.
