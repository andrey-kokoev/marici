# Erratum: the central sheet collapses the four pyramid fibers pairwise

## Correction

The conclusion in `the_reflected_physical_vertex_has_zero_valg_boundary_residue.md` was too strong. Its central-fiber residue computation is correct, but it cannot select the generic transverse pyramid route.

## Collision under E=0

The four global split-fiber values are

\[
q_1=y+z,
\quad q_2=-(y+z),
\quad q_3=2x+y+z,
\quad q_4=-(2x+y+z).
\]

On the central specialization

\[
E=x+y+z=0,
\qquad z=-x-y,
\]

they become

\[
(q_1,q_2,q_3,q_4)=(-x,x,x,-x).
\]

Hence

\[
q_1=q_4,
\qquad q_2=q_3.
\]

The four distinct generic fibers collapse to only two central walls. The central-sheet representative

\[
\varphi_{v_{\rm alg}}
=
\frac{x^2y^2(x^2-y^2+2a^2-2b^2)}
{xa^2+yb^2-xy(x+y)}\,da\wedge db
\]

therefore cannot distinguish \(d_1\) from \(d_4\), or \(d_2\) from \(d_3\).

## What survives

The calculations

\[
\operatorname{Res}_{b=-x}\varphi_{v_{\rm alg}}=0,
\qquad
\operatorname{Res}_{b=x}\varphi_{v_{\rm alg}}=0
\]

remain valid on the central fiber. They show that the two *collapsed wall supports* are \(v_{\rm alg}\)-null under ordinary boundary residue.

They do **not** show that the generic orbit-odd lattice direction \(\alpha_{13}+\alpha_{14}\) is null, nor that \(\alpha_{13}-\alpha_{14}\) is selected. The latter statements require first-order specialization data separating the colliding fibers.

## Missing comparison reinterpreted

The missing coherence comparison must retain the normal direction to \(E=0\). Writing

\[
z=-x-y+E,
\]

the four locations are

\[
q_1=-x+E,
\quad q_2=x-E,
\quad q_3=x+E,
\quad q_4=-x-E.
\]

Thus the two collisions separate to first order with opposite velocities:

\[
q_3-q_2=2E,
\qquad
q_1-q_4=2E.
\]

The desired route information lives in these first normal jets and is erased by setting \(E=0\) before taking the comparison.

## Next executable calculation

Use a first-order \(E\)-lift of the \(v_{\rm alg}\) representative and compute the antisymmetric collision residues

\[
\frac{1}{2E}
\bigl(
\operatorname{Res}_{q=x+E}
-
\operatorname{Res}_{q=x-E}
\bigr),
\]

and similarly at \(q=-x\). This is the minimal calculation capable of distinguishing the four vertices and identifying the transverse route.

Verification:

- `research/voevodsky/checkers/check_central_pyramid_pair_collision.py`
- `research/voevodsky/results/central_pyramid_pair_collision.json`
