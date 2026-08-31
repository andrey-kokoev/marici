# Reciprocal-determinant \(\rho\) no-go: WP1090

## Question

Can the reciprocal Krylov determinant \(1/D(x)\) serve as the missing
weight-\((-3)\) reference \(\rho\)?

## Exact weight check

For the WP1086 witness \(\lambda=(2,3,5)\) and \(x=(1,1,1)\),

\[
D(x)=\det[x,Ax,A^2x]=6.
\]

Under ray scaling \(x\mapsto 2x\),

\[
D(2x)=8D(x)=48,
\qquad
\frac1{D(2x)}=\frac1{48}=\frac{1}{2^3}\frac1{D(x)}.
\]

Thus \(1/D(x)\) has ray-phase weight \(-3\) on the cyclic domain where
\(D(x)\neq0\).

## Boundary of the loophole

The relation

\[
D(x)\frac1{D(x)}=1
\]

is tautological. It does not identify an independent source-authorized section
of a weight-\((-3)\) line.

The reciprocal is also singular on every noncyclic ray. For the eigenline
\(x=(1,0,0)\), the determinant vanishes, so \(1/D\) is undefined. It therefore
cannot be a global nonsingular reference over rays.

## Classification

Negative gate. The reciprocal determinant is a tautological meromorphic
inverse, not an independent source-authorized \(\rho\). It supplies no source
coorientation, temporal scope, comparison node, or global section.

The remaining gate is an independent source-authorized weight-\((-3)\) section
with a stated line bundle, descent law, temporal scope, and comparison node.

Checker: `research/flavor/checkers/wp1090_reciprocal_determinant_rho_no_go.py`

Result: `results/wp1090_reciprocal_determinant_rho_no_go.json`
