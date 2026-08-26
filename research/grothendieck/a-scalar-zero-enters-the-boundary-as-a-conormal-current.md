# A scalar zero enters the boundary as a conormal current

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: exact source-adapter theorem

## The missing crossing

The scalar readout and the zero-to-boundary relation are different adapters.
For a completed scalar section (F), the source-native Clark sheets are

\[
H_+=F+iaF',
\qquad
H_-=F-iaF'.
\]

Their symmetric and antisymmetric channels are

\[
T=H_++H_-=2F,
\qquad
C=H_+-H_-=2iaF'.
\]

At a scalar zero, (T=0), but generally (C\ne0). Thus the zero does not
remain silent. It enters the boundary object through the conormal derivative
of its divisor.

For a simple zero,

\[
F(s_0)=0,
\qquad
F'(s_0)\ne0,
\]

the conormal current (C(s_0)) is nonzero. This is exactly the transverse
current demanded by the corrected zero-confinement programme.

## Source covariance

Let a nonvanishing source block multiply the section by (g). Then

\[
(gF)'=g'F+gF'.
\]

On the divisor (F=0), the inhomogeneous term disappears and

\[
C(gF)=gC(F).
\]

Therefore the conormal current transforms in the scalar source line, while its
quadratic energy transforms in the determinant-line square. This matches the
finite jet coherencer derived in ledger 3035.

The construction is not a post-hoc derivative of a numerical zero. Clark
differentiation is defined before imposing (F=0), and restriction to the
divisor produces the conormal adapter.

## Reciprocal typing

In the centered coordinate, reciprocal reflection sends an even completed
section to itself and its derivative to its negative. Hence

\[
C(-z)=-C(z).
\]

The linear conormal current retains which reciprocal side supplied it. But the
quadratic currents

\[
C^2,
\qquad
|C|^2
\]

are reciprocal-even. Squaring restores positivity while erasing the side
orientation needed to distinguish the two open sectors.

At a simple zero the Clark Wronskian becomes

\[
W_a=2ia\bigl(FF''-(F')^2\bigr)
=-2ia(F')^2.
\]

This is nonzero, but it is again quadratic in the conormal derivative.

## What is now explained

A zero is not a disappearance of the full source state. It is a rank transfer:

1. the grade-zero value channel vanishes;
2. the reciprocal-odd conormal channel becomes the first surviving boundary
   datum;
3. the positive Clark energy records its magnitude;
4. a further oriented global law is required to relate that current to
   horizontal displacement from the seam.

This identifies the precise input to a Sommerfeld-type identity. Its natural
shape is

\[
2\operatorname{Re}(z)\,E(C)
=J_{\mathrm{total}}(\infty)-J_{\mathrm{total}}(0),
\]

where (E(C)>0) for a simple zero and the completed source boundary conditions
must force the right side to vanish.

## Real obstacle

The local adapter is universal for analytic sections and therefore does not by
itself reject hostile multipliers. The RH-bearing theorem is exactly the
global boundary cancellation of this source-derived conormal current. A norm
identity without the oriented linear current cannot distinguish the two
half-planes.

For a multiple zero, the first conormal current vanishes and the first nonzero
higher normal jet must replace it. No simplicity assumption is authorized.

## Verification

The exact checker verifies the symmetric/antisymmetric decomposition,
restriction to the divisor, multiplication covariance, simple-zero Wronskian,
reciprocal oddness of the linear current, and reciprocal evenness after
squaring.
