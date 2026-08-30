# Theta Separation Density Is Not Convex at the Origin

## Global separation pushforward

The two-sector Krein form can be pushed forward from source coordinates (u,v) to their separation. For (D\ge0), define

\[
\rho_y(D)
=2\int_0^\infty
\Phi(v+D)\Phi(v)
\sinh(y(2v+D))\,dv.
\]

Then the global orientation is the cosine transform

\[
J(x,y)=2\int_0^\infty \rho_y(D)\cos(xD)\,dD,
\]

up to the fixed normalization convention already used for the Krein form.

This is the correct global object after local two-point positivity fails. Negative local packets are allowed; only their completed separation distribution matters.

## Natural Pólya certificate

A tempting sufficient theorem is that (\rho_y) is positive, decreasing, convex, and decays to zero. Classical cosine-transform criteria would then orient (J) without requiring pointwise positivity of every pair.

The source itself rejects this shortcut. Write

\[
a(u)=e^{yu}\Phi(u),
\qquad
b(u)=e^{-yu}\Phi(u).
\]

Then (\rho_y) is the difference of their half-line autocorrelations. Direct differentiation and integration by parts give

\[
\rho_y''(0+)
=2\int_0^\infty
\sinh(2yu)
\left(y^2\Phi(u)^2-\Phi'(u)^2\right)du.
\]

Thus origin convexity is not automatic from source positivity. It is a weighted competition between vertical mass and dilation-decay energy.

Put

\[
k(u)=-\frac{\Phi'(u)}{\Phi(u)}.
\]

The already proved source inequality

\[
-u(\log\Phi)''(u)+(\log\Phi)'(u)>0
\]

implies

\[
k'(u)>\frac{k(u)}u>0.
\]

Hence (k) increases strictly from zero and crosses each (y>0) exactly once. The curvature density has one canonical sign transition: positive where (k<y), negative where (k>y).

More strongly, integration by parts with (W=\Phi^2) gives the exact identity

\[
\rho_y''(0+)
=-y\Phi(0)^2
-\int_0^\infty
\sinh(2yu)k'(u)\Phi(u)^2\,du
<0.
\]

Therefore concavity at the origin holds for every (y>0), without numerical input.

As a numerical replay, direct quadrature at (y=0.2) gives

\[
\rho_y''(0+)\approx-0.33695.
\]

The separation density is concave, not convex, immediately to the right of the origin.

## Meaning

The first global repair is therefore not ordinary variation diminution of one scalar separation density. Both the local acute-cone route and the simplest global convex-density route fail at the same near-diagonal source region.

The surviving opportunity is more structured:

1. split off the concave near-diagonal cap as a typed seam current;
2. prove convexity or another positive-transform property only for the remaining tail;
3. show reciprocal modular sewing repairs the cap exactly;
4. or replace scalar convexity with a matrix-valued total-positivity statement retaining label and boundary channels.

The curvature identity points directly at the needed repair term: it must account for the region where (\Phi'(u)^2<y^2\Phi(u)^2). That region is the global shadow of the local logarithmic-slope corridor found in the preceding packet.

## Scope

Both curvature formulas and the strict negative sign are exact consequences of the proved theta source inequality. The numerical checker is only a replay of the analytic theorem.

The result does not bear directly on RH. It rejects one natural global sufficient mechanism and exposes the exact source-energy term that any modular repair must absorb.
