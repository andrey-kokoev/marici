---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2146 — The Soft and Triangle Contact Restrictions Split the Cayley--Menger Cover

## Hard-to-vary claim

The two existing support components excluded from Entry 2145 do not supply
the half-Kummer normal character at their generic contact intersections.
Instead, the restricted Cayley--Menger polynomial becomes a perfect square.

## Soft contact intersection

For the component contact with focal separation \(p_2\), impose

\[
p_2=0,
\qquad
E=0.
\]

The exact restricted polynomial is

\[
\boxed{
K|_{q,;p_2=E=0}
=-2a^2(p_1-p_3)^2.
}
\]

Away from the deeper coordinate locus \(p_1=p_3\), the double cover splits
into two rational sheets. The residue has an ordinary logarithmic pole in
\(a\), not a new square-root character in the contact normal.

## Triangle contact intersection

Parametrize a generic component of the triangle wall by

\[
p_1=r^2,
\qquad
p_2=s^2,
\qquad
p_3=(r+s)^2,
\]

and impose the contact condition \(E=2s\). Exact substitution gives

\[
\boxed{
K|_{q,;\Lambda=0,;E=2s}
=-2s^2
\left(C+2ar-a^2-r^2\right)^2.
}
\]

For \(s\ne0\), this cover likewise splits. Any sign attached to choosing
\(s=\sqrt{p_2}\) is the already resolved momentum-polarity sheet; it is not
a half-Kummer character in \(\nu_2=p_2-E^2/4\).

## Consequence

The generic contact, soft-contact, and triangle-contact routes now agree:

\[
\boxed{
\text{none supplies the }(-1,-1)\text{ normal character required by Entry
2144.}
}
\]

On the supported strata the reason is stronger than generic unipotence: the
branch cover itself splits after restriction.

## Scope

The conclusion remains generic along each support component. It does not
classify the deeper intersections

\[
p_2=E=0, p_1=p_3,
\]

or

\[
s=0, C+2ar-a^2-r^2=0.
\]

Those are existing coordinate-soft/triangle corners, not new carrier
divisors.

## Evidence

- Entry 2136 and Entries 2143--2145;
- exact assertions in
  `research/benincasa/marici-gm/src/bin/three_site_deletion_landau.rs`;
- allocator claim `seqclaim-506710ecf17f5d0d6f3ad026`.

## Next falsifier

Resolve the two displayed deeper corners and compute the normalized cover and
residue inertia. Accept a bridge to the lower Kummer line only if a labelled
half-character survives normalization and is compatible with the physical
sheet orientation.
