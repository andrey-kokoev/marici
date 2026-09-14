# The total-energy cusp is a global double-conic surface degeneration

Write the total energy as

\[
E=x+y+z,
\qquad z=E-x-y,
\]

and form the complete homogenized Cayley--Menger branch quartic \(G_E(a,b,h)\). At \(E=0\), it factors globally:

\[
G_0(a,b,h)=Q(a,b,h)^2,
\]

where

\[
Q=-xa^2-yb^2+xy(x+y)h^2.
\]

Consequently the central degree-two del Pezzo fiber is reducible:

\[
S_0=S_+\cup S_-,
\qquad
S_\pm:\ W=\pm Q.
\]

The two components meet along the conic

\[
\mathcal C:\ Q=0.
\]

The paired infinity nodes are merely the intersection of this global conductor with \(h=0\). Indeed, setting \(a=t,b=1,h=0\) gives

\[
Q=-(xt^2+y),
\]

recovering the previously known doubled infinity quartic.

The first smoothing term also factors completely:

\[
\left.\frac{\partial G_E}{\partial E}\right|_{E=0}
=-2(x+y)(hy-a)(hy+a)(hx-b)(hx+b).
\]

It vanishes at four labelled points of the conductor:

\[
\left(\frac ah,\frac bh\right)
=(y,x),(y,-x),(-y,x),(-y,-x).
\]

All four satisfy \(Q=0\). These are the global special points where the first-order smoothing of the normal crossing fails. They replace the earlier abstract four-label picture with concrete points on one conductor conic.

For positive \(x,y\), the physical Cayley--Menger quadrant \(a,b\ge0\) singles out

\[
p_{++}=(y,x).
\]

The other three points belong to sign-reflected sheets/chambers. This does not yet determine the integral extension, but it provides a canonical physical marking that was absent from the root-permutation analysis.

The geometry to resolve is now explicit: locally near a generic conductor point, \((W-Q)(W+Q)=E\cdot\text{unit}\); at the four labelled points the unit vanishes and a second blow-up is required. Computing the specialization boundary map through those four resolved local models should produce the saturation class directly.

Certificate:

- `research/voevodsky/checkers/global_total_energy_surface_degeneration.py`;
- `research/voevodsky/results/global_total_energy_surface_degeneration.json`.
