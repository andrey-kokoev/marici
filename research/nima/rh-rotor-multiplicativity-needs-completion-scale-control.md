# Rotor multiplicativity needs completion-scale control

## Even Clifford typing

The even subalgebra of the Euclidean plane is

\[
\operatorname{Cl}^+(2,0)
=
\{a+Ib:I^2=-1\},
\]

so it is naturally the complex plane. Every nonzero element has the form

\[
z=\rho e^{I\theta},
\qquad
\rho>0.
\]

The unit factor is a rotor and \(\rho\) is its conformal scale.

For finite products, nonzero conformal rotors remain nonzero:

\[
\lVert z_1z_2\rVert
=
\lVert z_1\rVert
\lVert z_2\rVert.
\]

If the completed theta section were a finite geometric product of
source-derived invertible factors, zero exclusion would be immediate.

## Addition does not preserve invertibility

The theta and Mellin presentations also contain linear superposition. Two
nonzero rotors can cancel:

\[
R+(-R)=0.
\]

Therefore rewriting a scalar section as a sum or projection of rotor-valued
states supplies no nonvanishing theorem. A source-derived multiplicative
factorization is required.

## Infinite products add a second failure

Finite multiplicativity is still insufficient under completion. Consider the
positive conformal factors

\[
z_n=1-\frac1n,
\qquad
n\ge2.
\]

Every factor and every finite product is invertible, but

\[
\prod_{n=2}^{N}z_n
=
\frac1N
\longrightarrow0.
\]

Thus a sequence of finite rotor–dilation products can collapse to the zero
endomorphism at infinity. The lost datum is a lower bound on accumulated
scale, not phase coherence.

The reciprocal companion factors \(z_n^{-1}\) produce the opposite behavior.
Their paired product is exactly one at every cutoff while one sector collapses
and the other diverges. Joint reciprocal normalization can therefore hide
sectorwise loss of invertibility.

## RH consequence

The Euler chamber avoids this problem because its local product is absolutely
convergent and nonzero. Extending rotor multiplicativity into either critical
half-plane requires more than analytic continuation and more than finite
source-factor invertibility. It requires the renormalized relative products to
converge in the group of invertible even Clifford elements rather than merely
in its closure containing zero.

Equivalently, on every compact subset of an open half-plane, the completed
source transport needs a cutoff-uniform lower bound on its conformal scale.
That is the rotor form of the reduced-minimum-modulus or completion-stable
invertibility gate.

## Relation to the actual section

The hostile multiplier test is easy because its inserted factor visibly exits
the invertible group at its own zeros. The actual source problem is harder:
all finite source factors may be invertible while their renormalized completed
mate loses scale at infinity.

Demanding nonzero completed scale without deriving it from the source merely
restates zero exclusion. A valid rotor proof must identify an independent
conservation or normalization law that bounds the accumulated scale before
the scalar divisor is inspected.

## Finite falsifiers

Reject a proposed rotor proof when:

1. the section is formed by addition or projection rather than multiplication;
2. only finite-cutoff factor invertibility is shown;
3. reciprocal pairing keeps the joint product finite while permitting one
   sector to collapse;
4. the lower scale bound is defined using the completed section itself.

## DPC verdict

The rotor formulation sharpens the RH completion problem but does not solve
it. The missing theorem is source-derived scale conservation for the completed
relative rotor product in each open half-plane. Without that law, finite
invertibility and reciprocal coherence permit collapse at infinity.

## Verification

`check_rh_rotor_completion_scale.py` verifies finite Clifford norm
multiplicativity, exact additive rotor cancellation, the telescoping nonzero
product collapsing to zero, and reciprocal paired normalization hiding
sectorwise collapse.
