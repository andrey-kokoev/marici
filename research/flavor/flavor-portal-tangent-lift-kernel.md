# Portal tangent lift kernel

Work package: WP587  
Owner: marici.Figueiredo

## Known source-derived projection

The exact WP580 settings and the universal portal relations determine

\[
\kappa_t^2=1-r,
\qquad
\kappa_4=1+q.
\]

Therefore the tangent from the invariant setting coordinates \((r,q)\) into
the physical coupling pair \((\kappa_t^2,\kappa_4)\) is

\[
B=\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
\]

This projection has rank two and descends under the full weak-basis groupoid.
It is genuine source-derived coupling information.

## Nonunique lift

A completed event generator and detector depend on more coordinates than this
pair. With one representative omitted coordinate, every lift compatible with
the known projection has the form

\[
L_{a,b}=
\begin{pmatrix}
-1&0\\
0&1\\
a&b
\end{pmatrix}.
\]

Projection onto the first two rows gives \(B\) for every \((a,b)\). Thus
the known portal relations define an affine family of full generator tangents,
not a distinguished lift.

For the smallest detector row sensitive to both the quartic and omitted
coordinate,

\[
D=\begin{pmatrix}0&1&1\end{pmatrix},
\]

the \(q\)-response is \(1+b\). The completion \(b=0\) gives response one,
while \(b=-1\) cancels it exactly. Both have the same source-authorized
projection into \((\kappa_t^2,\kappa_4)\).

## Consequence

The portal coupling projection is faithful and rank two, but it does not
authorize a detector response whenever the detector is sensitive to the lift
kernel. This is the same obstruction exposed eventwise in WP586, now stated as
an exact factorization theorem.

The operation is neither a selector nor a rigidifier. No reference port is
added. The first unresolved arrow is the lift from the physical coupling pair
to the complete generator, width, and branching packet.

There are exactly two legitimate repairs:

1. derive every detector-sensitive omitted row from the admitted portal
   source; or
2. prove from a publication-bound detector model that its response annihilates
   the entire lift kernel.

Assuming omitted coordinates vanish is not a repair.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp587_portal_tangent_lift_kernel.py

The generated result is
research/flavor/results/wp587_portal_tangent_lift_kernel.json.
