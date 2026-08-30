# The Fourier–Tate cocycle is meromorphically trivial but may have no admissible global frame

## Question

What global obstruction remains after the Fourier–Tate jet shear has been
shown locally removable by a source-frame change?

## Reflection cocycle

Let (X) carry the involution

\[
\iota(s)=1-s
\]

and let a nonzero meromorphic transition satisfy

\[
\gamma(s)\gamma(\iota s)=1.
\]

A frame (b) changes it to

\[
\gamma_b(s)=\frac{b(s)}{b(\iota s)}\gamma(s).
\]

Trivialization asks for

\[
\frac{b(s)}{b(\iota s)}=\gamma(s)^{-1}.
\]

This is a (C_2) one-cocycle equation.

## Meromorphic category

At the level of the meromorphic function field, Hilbert theorem 90 gives

\[
H^1(C_2,\mathcal M(X)^\times)=0
\]

under the usual field-extension hypotheses. Therefore every such
meromorphic reflection cocycle is a meromorphic coboundary.

This does not provide an admissible source frame. The trivializing (b) may
have zeros, poles, uncontrolled growth, or incompatible Real structure.

## Fixed-point sign

At a holomorphic fixed point (s_0=\iota(s_0)), the cocycle law gives

\[
\gamma(s_0)^2=1.
\]

Hence

\[
\gamma(s_0)=\pm1.
\]

For a nowhere-zero finite frame,

\[
\frac{b(s_0)}{b(s_0)}=1.
\]

Thus a fixed-point value (-1) cannot be removed by a nowhere-vanishing
holomorphic gauge.

It can be removed meromorphically only by allowing a singular frame. The
elementary model

\[
b(s)=s-s_0
\]

satisfies

\[
\frac{b(s)}{b(\iota s)}=-1
\]

when reflection reverses the local coordinate. The price is a zero at the
fixed point.

## Half-log monodromy

The local frame

\[
b=e^{-\frac12\log\gamma}
\]

requires a single-valued half-logarithm. Around a closed loop, an odd winding
of (gamma) changes the half-log frame by a sign. Therefore odd winding
obstructs this nonsingular global construction even when meromorphic Hilbert
90 triviality holds.

The invariant is the equivariant line or torsor class together with its
allowed singularity and growth structure, not the local connection
coefficient.

## Admissible-frame hierarchy

The following notions must remain distinct:

1. meromorphic coboundary;
2. holomorphic coboundary;
3. nowhere-vanishing holomorphic coboundary;
4. Real-compatible coboundary;
5. source-normalization-preserving coboundary;
6. bounded invertible coboundary on the completed carrier.

Each implication goes from the stronger condition to the weaker one. None of
the converses is automatic.

## Completion gate

Even a nowhere-zero holomorphic (b) may fail to define a bounded invertible
multiplier on the constructor-generated completion. The operational gate is

\[
\lVert b f\rVert_{\rm comp}
\asymp
\lVert f\rVert_{\rm comp}
\]

with cutoff-independent constants, together with the same condition for
(b^{-1}).

Without it, gauge triviality at finite cutoff does not descend to the
completed source carrier.

## Theta consequence

The arithmetic finite-prime Fourier–Tate line can be perfectly coherent and
meromorphically trivial while the canonically normalized completed frame
remains nontrivial. The remaining audit must therefore record:

- the divisor of the global transition;
- fixed-point signs;
- logarithmic winding;
- Real compatibility;
- source-unit normalization;
- multiplier bounds in the completed topology.

Only after these are frozen does the connection shear acquire invariant
meaning.

## Relation to crossed experimental controls

Aspect's optical factorial repair has the same algebraic shape. Observing
only the confounded combinations (A+D) does not distinguish associator and
hardware phase. Crossing logical constructors with physical paths produces
(A+D) and (A-D), a two-character inversion.

Here the analogous separation is between the reflection cocycle and the
chosen source frame. A single normalized scalar cannot identify both without
an independent frame intervention or a canonical source unit.

## Falsifier certificate

    {
      "code": "meromorphic_triviality_mistaken_for_admissible_frame",
      "hilbert_90_trivial": true,
      "nowhere_zero_holomorphic_frame": "unproved",
      "real_compatible": "unproved",
      "completion_bounded_inverse": "unproved",
      "fixed_point_sign_or_monodromy_may_obstruct": true
    }

## Disposition

The Fourier–Tate reflection cocycle is meromorphically trivial, but the
research-bearing question is existence of a nonsingular, Real-compatible,
source-normalized, completion-bounded global frame. Fixed-point sign,
monodromy, divisor, and operator bounds are the exact obstruction classes.

## Claim boundary

This packet invokes Hilbert theorem 90 only at the meromorphic function-field
level. It does not establish the analytic hypotheses for a particular global
theta domain, compute its equivariant Picard class, or prove existence or
nonexistence of the required completed frame.
