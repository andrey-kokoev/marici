# Control-theory map for the framed theta two-port system

## Status

Typed dictionary and route-selection audit. The theta/Tate construction is
currently a noncollocated source-to-endpoint transfer channel built over a
selfadjoint transport carrier. RH is therefore typed as confinement of
transmission zeros, not stability of carrier poles and not rank loss of the
unframed full Weyl matrix.

This packet identifies which parts of classical control theory apply, which
ones address a different divisor, and which source-specific laws would be
strong enough to matter.

## State-space typing

At a finite source-authorized cutoff, take

\[
A=A^*,
\qquad
B=b_0,
\qquad
C=b_f^*,
\qquad
D=0.
\]

The state equation and readout are

\[
\dot x=Ax+Bu,
\qquad
y=Cx,
\]

after the appropriate spectral or time convention is fixed. The transfer
function is

\[
F(z)
=
C(A-zI)^{-1}B
=
b_f^*(A-zI)^{-1}b_0.
\]

Here \(b_0\) injects through the endpoint port and \(b_f^*\) reads through the
theta-source port. The ordering is part of the system type.

## Control dictionary

| Theta/Tate object | Control-theory object | Exact caution |
|---|---|---|
| Selfadjoint logarithmic transport | Internal state generator | Its spectrum gives carrier poles, not theta zeros |
| Endpoint distribution \(b_0\) | Input actuator | It may be rigged or unbounded after completion |
| Theta source \(b_f\) | Output sensor after adjunction | It is not the same port as the actuator |
| Theta scalar \(F\) | SISO cross transfer | Its zeros are transmission cancellations |
| Reciprocal sheet | Adjoint or time-reversed channel | The source must derive the port exchange |
| Functional equation | Reciprocity constraint | Reciprocity does not imply minimum phase |
| Critical seam | Lossless symmetry interface | Losslessness does not exclude transmission zeros |
| Bordered pencil \(L_{\mathfrak f}\) | Rosenbrock system pencil | It preserves the correct zero divisor |
| Full Weyl matrix \(W\) | Multiport impedance or scattering object | Its determinant has a different divisor |
| Seam history | Independent boundary state | It cannot be reconstructed boundedly from the tail |
| Primitive and square currents | Singular boundary or renormalization channels | Their exact port incidence is not yet constructed |
| Restricted-product limit | Infinite-dimensional system completion | Finite minimality and passivity need not survive |

## Poles and zeros must not be conflated

Carrier poles are controlled by

\[
\det(A-zI)=0.
\]

Theta transmission zeros are controlled by

\[
F(z)=0.
\]

Equivalently, away from carrier poles, they are rank losses of

\[
L_{\mathfrak f}(z)
=
\begin{pmatrix}
0&C\\
B&A-zI
\end{pmatrix}.
\]

A selfadjoint internal generator can have real spectrum while its
noncollocated transfer has zeros away from the real spectral axis. This is a
standard structural possibility, not a completion defect.

## Controllability and observability

Finite controllability asks whether

\[
\operatorname{span}
\left\{
B,AB,A^2B,\ldots
\right\}
=
\mathcal X.
\]

Finite observability asks whether

\[
CA^kx=0
\]

for every \(k\geq0\) forces \(x=0\).

Together they remove redundant internal states and pole-zero cancellations.
They do not constrain the remaining transmission zeros to the seam. Minimal
hostile Blaschke realizations already prove this.

## Collocation is the missing easy theorem

If the output were the adjoint of the input under a source-derived positive
metric,

\[
C=B^*,
\]

then the transfer would be an impedance-type diagonal resolvent pairing. Its
imaginary part would inherit a fixed sign in a resolvent half-plane, yielding
Herglotz or positive-real geometry.

But the current theta system has

\[
B=b_0,
\qquad
C=b_f^*,
\qquad
b_0\ne b_f.
\]

Earlier source audits also rule out a bounded local metric that simply
identifies the two ports. Treating the system as collocated changes the
observable.

## Passivity and losslessness

The full two-port system can be passive or lossless while one cross channel has
nonminimum-phase zeros. Energy conservation constrains the complete scattering
matrix, not every individual transfer entry.

Therefore full-port passivity does not imply cross-channel zero confinement.
In mathematical symbols, the invalid implication is

\[
Q_W\geq0
\nRightarrow
F(z)\ne0
\]

in either open sector.

## Reciprocity

The completed functional equation supplies a reciprocal comparison between
the two analytic sectors. In control language this resembles a relation
between a system and an adjoint or reversed system.

Reciprocal systems can still have paired nonminimum-phase zeros. A hostile zero
can be accompanied by its reflected partner without violating reciprocity.
Thus reciprocal symmetry explains the pairing law, not confinement to the
fixed seam.

## Minimum phase

The direct control-theoretic translation of the RH target is a source-relative
minimum-phase theorem for the flagged transfer channel after centering the
critical seam.

This terminology is diagnostic, not explanatory. Declaring the theta channel
minimum phase would restate the desired zero-free sector. The programme needs
a stronger source operation from which minimum phase follows.

Potential sufficient mechanisms include:

- source-derived port collocation in an indefinite or rigged metric;
- sign-regular or totally positive impulse response;
- a variation-diminishing source kernel;
- a port-Hamiltonian boundary law with a definitizable transmission pencil;
- or an arithmetic incidence relation forcing every open-sector zero state to
  pair with a forbidden boundary charge.

Each must be tested against hostile reciprocal factors.

## Infinite-dimensional gates

At completion, \(b_0\) and the primitive current need not be bounded Hilbert
ports. The correct setting may be a regular linear system on a nuclear rigging.
The required gates are:

1. admissibility of the input operator;
2. admissibility of the output operator;
3. closability of the source-to-boundary relation;
4. a well-defined transfer on a common resolvent domain;
5. preservation of the ordered port flag;
6. convergence of the bordered determinant or relative transmission section;
7. no hidden zero state entering through completion at infinity.

Finite state-space algebra alone cannot certify these properties.

## Exact RH typing

After shifting the critical seam to the imaginary axis, the current control
statement is:

> The completed, reciprocal, noncollocated theta transmission channel has no
> invariant transmission zeros in either open sector.

This is not implied by internal selfadjointness. It is a special property of
the ordered actuator-sensor pair and their arithmetic completion.

## Decisive finite programme

Before another conceptual rotation, compute at the smallest actual theta
compression:

1. the controllability rank of \((A_X,b_{0,X})\);
2. the observability rank of \((b_{f,X}^*,A_X)\);
3. the bordered-pencil transmission zeros;
4. the full Weyl determinant zeros;
5. the first mismatch between the two divisors;
6. every fixed Hermitian signature matrix \(J_X\) satisfying framed-pencil
   symmetry;
7. whether any such \(J_X\) is source-derived and stable under prime
   transport.

The first cross zero with invertible full Weyl matrix proves that unframed
control positivity is irrelevant to that zero. The absence of a source-derived
framed metric closes the direct selfadjoint-control route.

## Conclusion

Control theory maps cleanly, but it changes the RH diagnosis. The problem is
not stabilization of an unstable plant. The internal carrier is already
selfadjoint. The problem is confinement of transmission zeros of a
noncollocated, reciprocal, infinite-dimensional channel. Generic control
theory permits the hostile zeros. Only a source-derived law governing the
ordered endpoint/source port pair can exclude them.
