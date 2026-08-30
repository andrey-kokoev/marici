# Twisted exchange leaves mixed angular invariants

Work package: WP599  
Owner: marici.Figueiredo

## Directed audit

Nima proposed the quarter-twisted exchange

\[
T(\phi,\psi)=\left(Q\psi,Q^{-1}\phi\right),
\qquad Q=R_{\pi/4}.
\]

On the separate quartic anisotropy characters, this forces opposite signs.
Nima's finite group census then correctly finds no CP-odd stabilizer among the
sixteen opposite-parity axis-and-diagonal vacua. The remaining hostile is
whether those vacua are extrema of the complete renormalizable invariant
potential.

## Complete mixed-quartic census

Enumerate all nine real monomials of bidegree \((2,2)\) in
\(\phi=(x,y)\) and \(\psi=(u,v)\). Imposing the common quarter rotation,
bare CP and \(T\) leaves a two-dimensional invariant space. An exact basis is

\[
J_s=(uy+vx)^2,
\qquad
J_c=(ux-vy)^2.
\]

On unit-radius angular representatives these become

\[
J_s=\sin^2(\alpha+\beta),
\qquad
J_c=\cos^2(\alpha+\beta).
\]

Their sum is radial, but their difference is angular. The declared symmetry
does not force equal coefficients, because each basis element is separately
invariant.

## Exact obstruction

Add the allowed term \(\zeta J_c\). At the representative selected by the
truncated anisotropy packet,
\((\alpha,\beta)=(0,\pi/4)\), its angular gradient is

\[
\nabla(\zeta J_c)=
\begin{pmatrix}-\zeta\\-\zeta\end{pmatrix}.
\]

The unit-coefficient witness is therefore \((-1,-1)\). The checker also
tests all sixteen opposite-parity axis-and-diagonal vacua; every one has a
nonzero gradient under this allowed invariant.

The twisted exchange solves the binary sign and generalized-CP stabilizer
problem only on a truncated potential. It does not yet define a closed
hard-to-vary source architecture. Deleting the mixed angular combination or
equating its two coefficients requires an additional constructor.

## Surviving source and instrument gates

A progressive successor must derive microscopic sequestering, locality or a
non-abelian product-selection rule that removes the nonradial combination of
\(J_s\) and \(J_c\). WP598 shows that ordinary abelian phase charges cannot
do this for Hermitian overlaps.

Even after that repair, the architecture requires a portal descending to a
CP-odd coordinate on `physical16` and a calibrated scalar or threshold record
testing the same protecting interaction. No such joined instrument is present.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp599_twisted_exchange_mixed_invariant_obstruction.py

The generated result is
research/flavor/results/wp599_twisted_exchange_mixed_invariant_obstruction.json.
