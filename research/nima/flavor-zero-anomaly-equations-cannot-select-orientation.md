# Flavor Zero-Anomaly Equations Cannot Select Orientation

## Result

Anomaly cancellation equations set to zero cannot select the orientation of a
charge line when charge reflection acts on the full anomaly domain.

This remains true even if the anomaly polynomial contains the centered cubic
moment missing from WP616. A reflection-odd polynomial changes sign, but its
zero set does not.

## Odd anomaly functional

Let \(F(q)\) be odd under charge reflection:

\[
F(-q)=-F(q).
\]

Then

\[
F(q)=0
\]

if and only if

\[
F(-q)=0.
\]

The cancellation locus contains both reflected sheets or neither. It cannot
orient them.

The centered cubic

\[
m_3(q)=\sum_i(q_i-\bar q)^3
\]

is an exact example. For \((3,2,0)\),

\[
m_3=-\frac{20}{9},
\]

while reflection gives \(20/9\). Neither satisfies \(m_3=0\), and replacing
the target by zero would not choose between them.

## Even equations also fail

An equation depending only on

\[
m_3^2
\]

or another reflection-even quantity admits both sheets whenever it admits one.
Thus taking an absolute value or squared anomaly does not repair orientation.

## What would select a sheet

A nonzero signed condition

\[
m_3(q)=r,
\qquad
r\ne0,
\]

selects one sheet for a fixed \(r\). But \(r\) is now an oriented source datum.
Choosing \(r=-20/9\) after inspecting the target is circular.

The covariant construction is relational. Introduce an independently derived
oriented reference sector carrying \(r\), and compare

\[
m_3(q)=r.
\]

Under simultaneous reflection,

\[
(m_3,r)
\longmapsto
(-m_3,-r),
\]

so the relation is preserved. The comparison fixes relative orientation, not
an absolute sign.

## WP616 consequence

WP616 is even more restrictive. In the frozen minimal spectrum, the complete
local anomaly family collapses to the uncentered first moment

\[
\sum_i(3q_i+\ell_i).
\]

It constrains an origin-sensitive direction but contains neither centered
quadratic nor centered cubic quark data. It therefore does not select charge
gaps or orientation.

Adding a cubic anomaly term would not automatically solve this. If its role is
only cancellation at zero, the reflection no-go still applies.

## Observer architecture

The source stages are now:

1. hierarchy distances determine the affine charge family;
2. linear anomaly data may constrain the origin;
3. a relative signed observer compares charge orientation with an independently
   oriented reference sector;
4. the charge lattice constrains admissible lifts;
5. a physical width or resonance experiment criticizes the selected
   architecture;
6. preparation dynamics remain responsible for Wilson coefficients and CP.

The third item cannot be replaced by more zero-valued anomaly equations.

## Finite falsifiers

Any anomaly-based orientation proposal fails if:

- every equation is imposed at zero and the full domain is closed under charge
  reflection;
- the proposed signed polynomial enters only through an even function;
- its nonzero target was chosen after inspecting the desired charge vector;
- the reference sector is reflected simultaneously and no independent frame
  distinguishes the two configurations.

## Status

This closes homogeneous anomaly cancellation as a standalone Flavor
orientation mechanism. The live route is relational: identify a separately
derived representation or sector whose orientation can be compared with the
quark charge cubic, then test that joint architecture with the WP616 physical
width probe.
