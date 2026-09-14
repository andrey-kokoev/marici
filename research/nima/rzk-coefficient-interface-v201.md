# v201: canonical three-channel supported detector target

The actual endpoint/Q restriction already provides the correct three-channel object

`B = Q direct-sum Vplus[1] direct-sum Vminus[1]`

and chain map

`rho=(pi,kappa_plus,kappa_minus): E -> B`.

Its differential is `(d_Q,-d_V,-d_V)`, and the source checker verifies `d_B rho=rho d_E`. Thus the three detector domains required by module 209 need not be invented: they are the generic Q quotient and the two shifted endpoint connectors. In the target Cech realization, radial coefficients are `X_a/u_a`, with `u_a^-1` available only on states where that normal is present and uncircled.

This does not yet produce scalar detectors. They require three functionals on `Q`, `Vplus[1]`, and `Vminus[1]`, respectively, and their values on the selected physical Gysin class. The canonical connecting class beta is not that class: it satisfies `rho(beta)=0`, while its primitive satisfies `rho(s)=(theta,0,0)`.

Consequently beta cannot be used to fit the desired amplitude coordinates. The next executable detector task is to locate the selected supported W class in E and compute all three components of rho(W) before choosing scalar evaluations.
