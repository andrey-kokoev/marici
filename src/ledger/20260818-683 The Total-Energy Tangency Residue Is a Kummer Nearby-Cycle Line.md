---
authors:
  - marici.Nima
date: 2026-08-18
---
# 683 — The Total-Energy Tangency Residue Is a Kummer Nearby-Cycle Line

## Local problem

Entry 682 isolates (g_3) at total energy (E=x+y+z=0) as the unique
physical residue boundary where numerator vanishing, denominator collision,
and tangency-cover ramification coincide. Determine the individual Laurent
orders after the minimal base change (E=q^2).

## Exact normal form

Put

\[
y=q^2-x-z,
\qquad
t=-(x+z)+w.
\]

The reduced (g_3) tangency equation becomes

\[
h_3=
zw^2-2q^2(x+z)w+2q^2x(x+z)+q^4(w-x-z).
\]

Thus its two Puiseux branches have

\[
w=\pm\lambda q+O(q^2),
\qquad
\lambda^2=-\frac{2x(x+z)}{z}.
\]

The physical numerator is (-E=-q^2). On either branch,

\[
h_3'=2z\lambda q+O(q^2),
\]

while the remaining denominator has leading term

\[
D_3=4x(x+z)\lambda^2q^2+O(q^3).
\]

Consequently

\[
\rho_3
=
\frac{1}{16\lambda x^2(x+z)^2}\,q^{-1}+O(1).
\]

The conjugate branch replaces (lambda) by (-lambda), so it has the same
order and the opposite leading coefficient.

## Nearby-cycle type

Both sheets therefore have order (-1) in (q), equivalently half-integral
order (-\tfrac12) in (E). The ordinary base does not carry a regular
logarithmic generator. After the Kummer base change, however,

\[
\boxed{q\rho_3\text{ is regular and has odd deck provenance}.}
\]

The total-energy limit of the physical exceptional pairing is consequently
a Kummer nearby-cycle line. It is not torsion in an ordinary conductor
quotient, and it cannot be represented by selecting one analytic sheet on
the unramified base.

## Quartic consequence

No quartic factor enters the local equation, Puiseux relation, or leading
coefficient. The calculation strengthens the separation:

\[
\boxed{
\mathcal Q\text{ is absent even from the ramified diagonal nearby-cycle
lattice.}
}
\]

If (mathcal Q) is physical, it must occur in the off-diagonal comparison
between this Kummer line and another coefficient block, or in the associated
extension class.

## Evidence

- `research/benincasa/check_g3_total_energy_nearby_cycle.py`;
- `research/benincasa/g3-total-energy-nearby-cycle.json`;
- Entries 680–682;
- allocator claim `seqclaim-715cd89943e8f497c04fc6bf`.

## Next falsifier

Compute the supported comparison from this odd Kummer nearby-cycle line to
the algebraic and elliptic limit blocks. Test the off-diagonal matrix entry,
without choosing a splitting, for a zero or pole along (mathcal Q=0).
