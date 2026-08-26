# The paired theta Fourier minor is a metaplectic area, not a positive order minor

## Status

Exact two-label/two-frequency calculation. Reciprocal pairing of the Fourier
minor produces a nonnegative scalar square, but that square erases the
orientation needed for variation diminution. The unsquared minor is controlled
by the symplectic area of the sampling rectangle and changes sign after phase
wrapping. A metaplectic or Maslov-type lift retains the missing half-angle and
crossing count.

This identifies the correct carrier for transported order. It does not yet
prove that theta/Tate source data supplies the lift or that the lift excludes
off-seam transmission zeros.

## Exact Fourier rectangle

Take

\[
q_1<q_2,
\qquad
\xi_1<\xi_2,
\]

and define the Fourier minor

\[
\Delta
=
e^{-i(\xi_1q_1+\xi_2q_2)}
-
e^{-i(\xi_2q_1+\xi_1q_2)}.
\]

Introduce the phase-space area

\[
\mathcal A
=
(\xi_2-\xi_1)(q_2-q_1)
>0
\]

and the center phase

\[
\mathcal C
=
\frac{(\xi_1+\xi_2)(q_1+q_2)}{2}.
\]

Then

\[
\Delta
=
-2i
e^{-i\mathcal C}
\sin\left(\frac{\mathcal A}{2}\right).
\]

The order data from the radial minor has become a phase-space area and a
half-angle.

## What reciprocal pairing retains

The conjugate sector carries \(\overline\Delta\). Their scalar product is

\[
\Delta\overline\Delta
=
4
\sin^2\left(\frac{\mathcal A}{2}\right)
\geq0.
\]

This is a valid positive Gram quantity. But it is unchanged when

\[
\sin\left(\frac{\mathcal A}{2}\right)
\]

changes sign. The paired scalar therefore forgets the orientation that
distinguished one sign-transition order from its reversal.

Reciprocal doubling repairs positivity by type erasure unless the unsquared
phase relation is retained.

## Centered oriented minor

If the center phase is fixed by the source frame, define

\[
\widetilde\Delta
=
i e^{i\mathcal C}\Delta.
\]

Then

\[
\widetilde\Delta
=
2\sin\left(\frac{\mathcal A}{2}\right).
\]

For the first phase-space cell,

\[
0<\mathcal A<2\pi,
\]

the orientation is positive. It vanishes when

\[
\mathcal A=2\pi n
\]

and flips sign after crossing an odd such boundary.

Thus local variation diminution survives below one phase-wrapping threshold,
but no global fixed sign survives arbitrary spectral separation.

## Metaplectic meaning

The half-angle

\[
\frac{\mathcal A}{2}
\]

is the signature of a double-cover phenomenon. A full \(2\pi\) phase-space
loop changes the sign of the lifted orientation even though the scalar unitary
phase returns to the same point.

The correct transported datum is therefore not only a point of \(U(1)\). It is
a lifted phase together with an integer crossing grade. In geometric language,
this is metaplectic or Maslov-type data.

The positive square sees only the projection of that lift.

## Relation to the rotation programme

The earlier Lagrangian and unitary turns already produced Maslov and spectral-
flow indices for full-port rank crossings. The ordered-port correction requires
the same idea at the level of the framed transmission minor.

The two-polarization object must therefore retain

\[
\left(
\Delta_{\rm L},
\Delta_{\rm F},
\widetilde\Delta_{\rm F},
m,
\mathfrak f
\right),
\]

where \(m\) records phase-wrapping crossings and \(\mathfrak f\) is the ordered
endpoint/source flag.

Without \(m\), reciprocal pairing returns only the orientationless Gram
square.

## Aliasing interpretation

The zero condition

\[
\mathcal A=2\pi n
\]

means the two Fourier sampling paths become linearly dependent. This is a
phase-space aliasing event. The sign flip after the event records how the
oriented two-plane passes through degeneracy.

Therefore the transported order law cannot be a global statement that no
minor vanishes. It must specify how each degeneracy is crossed and how the
crossing grade contributes to the framed boundary current.

## Source-derived gate

The metaplectic lift is explanatory only if theta/Tate data constructs:

1. the center phase convention;
2. the continuous lift along prime and cutoff transport;
3. the crossing grade at each aliasing surface;
4. the reciprocal relation between the two lifted sectors;
5. the incidence of primitive, square, seam, and archimedean currents with the
   accumulated grade;
6. completion stability of the lifted phase.

Choosing branches after inspecting the theta divisor would be circular.

## Hostile tests

The route fails if:

- a source-compatible phase multiplier changes the lift while preserving the
  paired Gram square;
- different cutoff paths accumulate different crossing grades;
- the center phase depends on an untyped coordinate origin;
- the primitive and square counterterms repair the scalar determinant but not
  the lifted framed minor;
- or the lifted orientation has no implication for the ordered spectral
  signature of the endpoint/source channel.

The minimal hostile is multiplication of one sector by a unit phase that
preserves \(|\Delta|^2\) but reverses or shifts the lifted orientation.

## Connection to the completion anomaly

At finite cutoff, a continuous phase lift can always be chosen along one path.
Global arithmetic descent requires path-independent lifts across prime
transport squares and controlled accumulation at infinity.

The primitive and square Tate currents are natural candidates for the first
two phase counterterms. The trace-class tail can carry the convergent residual
determinant. This interpretation must be derived by matching exact finite Euler
cutoffs; it cannot be assigned by analogy.

## Decisive conclusion

Reciprocal sewing does not restore radial order as scalar positivity. It turns
the order minor into a symplectic-area phase whose square is positive and whose
orientation lives on a metaplectic lift. The next finite calculation is whether
the actual labelled two-sector theta sewing supplies a path-independent lifted
minor with boundary-current accounting. If not, the variation-diminishing
bridge closes.
