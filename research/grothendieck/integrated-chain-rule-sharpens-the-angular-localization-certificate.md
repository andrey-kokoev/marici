# Integrated chain rule sharpens the angular localization certificate

## Problem

The directed angular-window certificate `104.4253919` uses pointwise derivative suprema before integration. The resulting localization constant pushes the positive Dirichlet tail to an impractical exponential mode scale.

## Integrated estimate

Let

`rho(t)=sin(c s(t))`, with `c=pi/2`.

Then

`rho'''=c cos(cs)s'''-3c^2 sin(cs)s's''-c^3 cos(cs)(s')^3`.

Using only `|sin|,|cos|<=1` gives

`||rho'''||_1`

`<=c||s'''||_1+3c^2 integral |s's''|+c^3 integral (s')^3`.

For the septic profile,

`s'(t)=140 t^3(1-t)^3`,

which is nonnegative and increases to its unique maximum at `t=1/2`, then decreases. Hence

`integral_0^1 |s's''| dt = s'(1/2)^2 = 1225/256`.

The cubic integral is an exact beta integral:

`integral_0^1 (s')^3 dt`

`=140^3 integral_0^1 t^9(1-t)^9 dt`

`=137200/46189`.

Voevodsky's exact septic calculation gives

`||s'''||_1=336 sqrt(5)/25`.

Therefore

`||rho'''||_1`

`<= (pi/2)(336 sqrt(5)/25)`

`+3(pi/2)^2(1225/256)`

`+(pi/2)^3(137200/46189)`

`approximately 94.14010123`.

The cosine-complement window obeys the same bound.

## Normalized cover constant

For two windows, two transitions, and angular overlap `h_theta=pi`, Aspect's estimate yields

`C_loc^quad <= (pi/6)*4*pi^(-2)*94.14010123`

`approximately 19.97714994`.

This is a fully analytic upper bound conditional only on the already checked septic identities. It is about five times smaller than `104.4253919`, though still above the non-directed scout `9.84825790`.

## Consequence

The improvement reduces but does not remove the exponential low-block problem: any argument subtracting the entire localization constant from a logarithmic Dirichlet floor still requires modes on the scale of `exp(C_loc)` before adding the other bounded remainders.

## Disposition

Pointwise-sup chain-rule certification is superseded by the integrated bound `19.97714994`. Further improvement requires directed sign decomposition of `rho'''` or a localization-free comparison; enlarging the arithmetic matrix remains premature.
