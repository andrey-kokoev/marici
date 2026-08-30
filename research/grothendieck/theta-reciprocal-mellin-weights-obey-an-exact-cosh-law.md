# Theta reciprocal Mellin weights obey an exact cosh law

## Source decomposition

For a nonzero (f\in L^2(0,\infty)), retain the complete moving-cut tail and
seam energies

\[
 T(q)=\int_q^\infty |f(v)|^2\,dv,
 \qquad
 S(q)=\int_0^q |f(v)|^2\,dv.
\]

Packet 201 proves the source identity

\[
 T(q)+S(q)=\|f\|_2^2.
\]

Write the centered Mellin parameter as (z=\delta+i\tau). The two reciprocal
valuation orientations assign opposite hyperbolic weights to the same typed
tail and seam components:

\[
 E_\delta^+(q)=e^{-2\delta q}T(q)+e^{2\delta q}S(q),
\]

\[
 E_\delta^-(q)=e^{2\delta q}T(q)+e^{-2\delta q}S(q).
\]

Neither orientation is discarded or reconstructed from the other.

## Exact reciprocal sum

Adding before scalar projection gives

\[
 E_\delta^+(q)+E_\delta^-(q)
 =2\cosh(2\delta q)\bigl(T(q)+S(q)\bigr).
\]

Hence the full reciprocal energy obeys the source-independent law

\[
 E_\delta^{\mathrm{full}}(q)
 =2\cosh(2\delta q)\|f\|_2^2.
\]

Its derivative is

\[
 {d\over dq}E_\delta^{\mathrm{full}}(q)
 =4\delta\sinh(2\delta q)\|f\|_2^2.
\]

The pointwise moving-boundary terms (\pm|f(q)|^2) cancel exactly. What
remains is not an uncontrolled endpoint defect: it is the universal
hyperbolic distortion imposed by the reciprocal Mellin pair.

## Consequence

For nonzero (f), the full reciprocal trajectory is bounded on the entire
half-line precisely when

\[
 \delta=0.
\]

When (\delta=0), it is the constant trajectory

\[
 E_0^{\mathrm{full}}(q)=2\|f\|_2^2.
\]

When (\delta\ne0), it grows like (e^{2|\delta|q}). Thus one orientation may
appear to lose a state into the completion, but its reciprocal partner records
the compensating growth. The complete two-orientation object has no bounded
nonzero off-seam trajectory.

This is the first exact realization of the proposed geometric intuition:
the two half-planes are reciprocal shadows of two sectors, and only their
common seam supports lossless joint transport.

## Remaining bridge

This does not prove RH. The missing theorem must derive from the completed
theta/Tate construction that a zero of the scalar section supplies a nonzero
full reciprocal tail--seam state satisfying the required bounded endpoint
domain. Without that zero-to-state and domain bridge, boundedness may not be
imposed merely because it confines zeros to the desired seam.

The next hostile test is therefore categorical rather than numerical:

1. derive the reciprocal pair from the same labelled source packet;
2. derive its endpoint domain before inspecting the scalar transform;
3. prove that scalar nullity places the full pair in that domain; and
4. test whether a hostile symmetric divisor can satisfy the same lift.

## Falsifier

The cosh law fails if reciprocal Mellin transport does not act by the stated
opposite weights on the two retained orientations, if the two orientations do
not share the same complete moving-cut decomposition, or if source-authorized
sewing introduces a further typed bulk component. The RH route fails even if
the cosh law holds when scalar nullity does not imply membership in the bounded
full-state endpoint domain.

## Scope

This proves an exact source-level bounded-trajectory obstruction for the full
reciprocal Mellin transport. It does not prove the zero-to-state bridge,
endpoint-domain authority, determinant correspondence, or RH.
