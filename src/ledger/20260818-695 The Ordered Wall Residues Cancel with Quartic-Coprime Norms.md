---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 695 — The Ordered Wall Residues Cancel with Quartic-Coprime Norms

## Hard-to-vary claim

Entry 694 proves that the physical wall mapping-cone representative has
zero Čech degree-one component. The individual ordered iterated residues
are nevertheless nonzero. Their exact values cancel solely by the
orientation reversal of the two wall orders, and every numerator,
denominator, and surface-sheet norm entering those values is coprime to
\(\mathcal Q\).

## Frozen form

Use

\[
\omega_{\rm phys}
=
\frac{da\wedge db}
{wq_{g_1}q_{g_2}q_{g_3}}
\left(\frac1{q_{g_{23}}}+\frac1{q_{g_{31}}}\right),
\]

with

\[
q_{g_1}=b-y-z,quad
q_{g_2}=a-x-z,quad
q_{g_3}=a+b+z,
\]

\[
q_{g_{23}}=b-x,qquad
q_{g_{31}}=a-y.
\]

No tubular primitive or absolute lift is used.

## Exact ordered residues

For the order \((g_i,g_j)\), use the Jacobian of
\((q_{g_i},q_{g_j})\) against \((a,b)\). The three independent values
are

\[
\operatorname{Res}_{g_2}\operatorname{Res}_{g_1}\omega_{\rm phys}
=
\frac{2z}
{(x-y-z)(x-y+z)(x+y+3z)}\frac1w,
\]

\[
\operatorname{Res}_{g_3}\operatorname{Res}_{g_1}\omega_{\rm phys}
=
-\frac{E}
{2(y+z)(x-y-z)(x+y+3z)}\frac1w,
\]

\[
\operatorname{Res}_{g_3}\operatorname{Res}_{g_2}\omega_{\rm phys}
=
-\frac{E}
{2(x+z)(x-y+z)(x+y+3z)}\frac1w.
\]

Reversing each order reverses the Jacobian and therefore the sign:

\[
\operatorname{Res}_{g_i}\operatorname{Res}_{g_j}
=
-\operatorname{Res}_{g_j}\operatorname{Res}_{g_i}.
\]

Hence all three Čech components vanish exactly:

\[
\boxed{
\delta_{\check C}\rho_W=(0,0,0).
}
\]

This independently verifies the closure asserted in Entry 694 and records
the nonzero values that cancel.

## Sheet norms

At the three pair intersections, the surface values factor respectively as

\[
(x-y-z)^2(x-y+z)^2E^2,
\]

\[
(y+z)^2(x-y-z)^2(x+y-z)^2,
\]

\[
(x+z)^2(x-y+z)^2(x+y-z)^2.
\]

Squaring each ordered residue and dividing by the corresponding surface
value gives its two-sheet norm. Exact polynomial gcd tests show that every
factor in all three norms is coprime to \(\mathcal Q\).

Thus the cancellation does not hide opposite quartic poles:

\[
\boxed{
\mathcal Q
\text{ is absent from both the Čech sum and the individual ordered
residue norms.}
}
\]

## Consequence

The static localization representative is now audited at both Čech
degrees:

- degree zero: conductor support \(R_1R_2E^2\), quartic-coprime;
- degree one: exactly zero, with individually quartic-coprime ordered
  terms.

Any surviving \(\mathcal Q\)-dependence must therefore enter through
Gauss--Manin transport or a higher homotopy of the localization extension,
not its static Čech representative.

## Classification

- mapping-cone representative: closed;
- pairwise transition: zero by oriented cancellation;
- hidden quartic pole in cancelling terms: absent;
- new carrier datum: none;
- remaining \(\mathcal Q\)-home: transported extension data only.

## Next falsifier

Differentiate the complete degree-zero wall cocycle in the total-energy
direction, compute the induced ordered pair terms before cancellation, and
reduce by mapping-cone homotopies. Test whether differentiation preserves
the zero degree-one component or produces a nontrivial transported
extension class.

## Evidence

- `research/benincasa/compute_physical_wall_cech_transitions.py`;
- `research/benincasa/physical-wall-cech-transitions.json`;
- Entries 693--694;
- allocator claim `seqclaim-0fdcfdc2c23635ff76a256c4`.

## Outcome contract

~~~json
{
  "claim": "The vanishing Cech transition may conceal cancelling ordered residues with quartic poles.",
  "status": "falsified",
  "ordered_pair_residues_nonzero": true,
  "reverse_order_sign": -1,
  "cech_degree_one_component_zero": true,
  "ordered_residue_norms_Q_coprime": true,
  "new_carrier_datum": false,
  "next_experiment": "Differentiate the mapping-cone cocycle and test transported Cech closure modulo canonical homotopies."
}
~~~
