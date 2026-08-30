# Connected Euler tail is divisor-neutral but coherence-bearing

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: exact reciprocal transition identity and global-current obstruction

## Residual sections on two charts

Let

\[
 z=s-\frac12
\]

and define the reciprocal primitive loops

\[
 L_+(z)e_p=p^{-1/2-z}e_p,
 \qquad
 L_-(z)e_p=p^{-1/2+z}e_p.
\]

Their determinant-three units are

\[
 u_+(z)=\det_3(I-L_+(z)),
 \qquad
 u_-(z)=\det_3(I-L_-(z)).
\]

The carrier-normalized theta sections are

\[
 R_+(z)=\Xi(z)u_+(z),
 \qquad
 R_-(z)=\Xi(z)u_-(z),
\]

where (\Xi(z)\) abbreviates the centered completed section.  Each residual
section has exactly the divisor of (\Xi\) on its chart.

## Exact transition

On the overlap (\lvert\Re z\rvert<1/6\), the ratio is the unit

\[
 g_3(z)=\frac{R_+(z)}{R_-(z)}
 =\frac{u_+(z)}{u_-(z)}.
\]

Using the regularized logarithms gives

\[
 \log g_3(z)
 =2\sum_p\sum_{k\ge3}
 \frac{p^{-k/2}}k\sinh(kz\log p).
\]

The series converges normally on compact subsets of the overlap.  Its
connection is

\[
 \partial_z\log g_3(z)
 =2\sum_p\sum_{k\ge3}
 (\log p)p^{-k/2}\cosh(kz\log p).
\]

Consequently

\[
 \partial_z\log R_+(z)
 -\partial_z\log R_-(z)
 =\partial_z\log g_3(z).
\]

This identity holds away from the common zeros, and extends as an identity of
meromorphic connections because the equal divisor poles cancel in the
difference.

## Correction to the three-channel reduction

Multiplication by (u_+\) or (u_-\) removes every (k\ge3\) term from the
local Euler-chamber logarithm without moving the divisor.  But the connected
tail has not disappeared globally.  It is exactly the transition connection
between the two reciprocal low-current presentations.

Thus the connected tail has two different roles:

- it is divisor-neutral because its determinant is a unit;
- it is coherence-bearing because its connection glues the reciprocal
  residual packets.

The archimedean, primitive, and square coordinates therefore do not form an
ordinary global direct-sum current.  They form a chartwise affine packet
twisted by the determinant-three carrier.

## Consequence for a Green identity

A proposed global residual current built only from

\[
 B_\infty,\qquad \tau_1,\qquad \tau_2
\]

will differ between the reciprocal charts by

\[
 \partial_z\log g_3(z).
\]

Unless that term is retained as a declared carrier connection, the current
is not globally typed.  Agreement after scalar summation would hide a genuine
transition anomaly.

Conversely, subtracting the local carrier connections gives

\[
 \partial_z\log R_\pm-partial_z\log u_\pm
 =\partial_z\log\Xi.
\]

This is globally covariant but contains the original divisor poles and has no
new zero-confining force.  Carrier covariance alone therefore cannot be the
missing conservation theorem.

## Symmetric gauge does not solve orientation

One may multiply (\Xi\) by a symmetric nowhere-zero function constructed
from (u_+u_-\).  This distributes the transition connection evenly between
the two charts.  It is a valid gauge choice, but it moves no zero and creates
no sign law.  The obstruction is not failure to choose a convenient frame.

## Falsifier

For any claimed reciprocal Green or connection identity on the low-current
packet, compute the chart difference.  If the residual is

\[
 2\sum_p\sum_{k\ge3}
 (\log p)p^{-k/2}\cosh(kz\log p),
\]

then the connected carrier was silently discarded.  If the residual vanishes
only after replacing it by (\Xi'/\Xi\), the construction is covariant but
tautological.

## Result

The determinant-three quotient gives a sharp local divisor normal form, not a
standalone global three-current theory.  The connected tail is harmless to
zeros but indispensable to reciprocal coherence.  The remaining theorem must
couple the low boundary currents to this carrier connection and derive an
independent global conservation law for the distinguished theta section.
