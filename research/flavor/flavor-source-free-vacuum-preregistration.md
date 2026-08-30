# Source-free two-adjoint vacuum preregistration (WP437)

## Purpose

WP436 shows that WP128's positive-mass potential selects the symmetric origin
unless Yukawa-dependent linear sources import the desired vacuum. WP437 freezes
the smallest source-free symmetry-breaking successor before solving it or
comparing it with flavor data.

This packet is a preregistration, not a vacuum result.

## Frozen symmetry grammar

The two Hermitian traceless diagonal-(SU(3)_F) adjoints (A,D) obey:

- gauge conjugation covariance;
- exchange symmetry (A\leftrightarrow D);
- independent sign flips (A\mapsto-A) and (D\mapsto-D);
- power-counting renormalizability;
- no external Yukawa, texture, CKM, or detector source.

The sign flips exclude all cubic invariants. Exchange symmetry identifies the
two quadratic coefficients. The frozen potential is

$$
V_{437}=
-\frac{m^2}{2}\left(\operatorname{Tr}A^2+\operatorname{Tr}D^2\right)
+rho\left(\operatorname{Tr}A^2+\operatorname{Tr}D^2\right)^2
-lambda\lVert[A,D]\rVert_F^2,
$$

with the coefficient domain

$$
m^2>0,
\qquad
lambda>0,
\qquad
rho>\frac{lambda}{2}.
$$

The negative quadratic triggers spontaneous breaking; the strict quartic
margin makes the potential coercive. No coefficient is assigned a numerical
value in this packet.

## Frozen vacuum acceptance

The successor may claim a viable vacuum shape only if it proves all of:

1. a nonzero global minimum exists;
2. the complete minimum is stable modulo gauge zero modes;
3. (A,D) do not commute;
4. the diagonal-(SU(3)_F) gauge-mass Gram has rank eight;
5. the result is obtained for an open coefficient domain rather than a single
   fitted point;
6. no measured Yukawa or CKM coordinate enters the solution.

Even success would select only a normalized vacuum class. The radial scale is
proportional to (m/\sqrt{rho,lambda}), so (g_Ff/v) remains a separate source
gate.

## Frozen falsifiers

- the global minimum is the origin;
- every global minimum commutes;
- a non-gauge Hessian direction is negative or flat;
- the gauge-mass rank is below eight;
- full rank occurs only after adding a target-dependent invariant;
- the potential is unbounded on a matrix ray;
- the conclusion uses a numerical coefficient chosen after inspecting flavor.

## No-outcome boundary

WP437 contains no stationary solution, Hessian spectrum, vacuum matrices,
gauge-mass rank, CKM value, or comparison with `physical16`. The successor must
import the frozen JSON unchanged.

Run `uv run --with sympy python
research/flavor/checkers/wp437_source_free_vacuum_preregistration.py` to
regenerate the JSON packet.
