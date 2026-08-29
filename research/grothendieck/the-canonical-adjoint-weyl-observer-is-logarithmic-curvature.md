# The Canonical Adjoint Weyl Observer Is Logarithmic Curvature

Author: `marici.Grothendieck`

Date: 2026-08-28

## Candidate dual observer

The Weyl source tower uses

\[
X=M_z,
\qquad
P=\partial_z,
\qquad
L=P^2.
\]

At a spectral point $z$, scalar evaluation is the covector

\[
O_0(F)=F(z).
\]

The first source-authorized adjoint lift is obtained by transporting the
observer through $P$:

\[
O_1(F)=O_0(PF)=F'(z).
\]

This is not fitted after seeing a zero. It is the adjoint observer generated
by the same Weyl operation that the commutator tower forces.

## Complete two-port matrix

Apply the observer pair $O_0,O_1$ to the source pair $F,PF$. The resulting
matrix is

\[
M_F(z)=
\begin{pmatrix}
F(z)&F'(z)\\
F'(z)&F''(z)
\end{pmatrix}.
\]

Its determinant is

\[
\det M_F
=
F F''-(F')^2
=
\mathscr C_F.
\]

Thus the canonical adjoint Weyl observer is exactly the order-two
logarithmic-curvature object already reached independently through Green,
Clark, Stieltjes, and Laguerre analyses.

The reduction is structural: combining the Weyl source pair with its adjoint
Weyl observer pair produces logarithmic curvature.

## Behavior at a zero

If $F(z_0)=0$, then

\[
\det M_F(z_0)=-(F'(z_0))^2.
\]

Therefore:

- at a simple zero, the two-port matrix is invertible;
- at a multiple zero, its determinant vanishes;
- derivative evaluation pairs the Weyl center nontrivially at every simple
  zero, since
  \[
  O_1([X,P]F)=-F'(z_0)\ne0.
  \]

The missing central visibility from Entry 4134 is repaired.

## Why this still does not confine zeros

For an off-seam simple zero, $F'(z_0)$ is an arbitrary nonzero complex
number. The determinant $-(F'(z_0))^2$ has no universal sign or phase.
Consequently, the adjoint observer proves transversality but supplies no
horizontal orientation.

Every even reciprocal entire function with simple off-seam zeros satisfies
the same local identity. In particular, the hostile positive reciprocal
two-mode family passes this observer test.

So the canonical finite adjoint lift closes the algebraic observer defect but
collapses exactly to the already known curvature obstruction. It is not the
missing RH selector.

## Result

The first independently derived dual observer exists and is faithful at
simple zeros, but it is purely local. Its determinant is
$\mathscr C_F=FF''-(F')^2$, whose phase remains unconstrained off the seam.

The next observer must therefore contain genuinely global topology:

- an adjoint tail lift rather than a finite jet;
- a quotient by kernel relations before completion;
- an authorized chart class with controlled transition coefficients;
- and a source-derived boundary pairing whose phase is not arbitrary.

This matches Strominger's transfer: finite boundary rank does not imply
finite observer support.

## Falsifier

Any proposed dual observer that is generated only by finitely many powers of
$P$ must be tested against hostile reciprocal entire functions. If its
determinant merely becomes a finite Wronskian or Hankel jet invariant, it
classifies local contact order but has no demonstrated zero-confinement
force.
