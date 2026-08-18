---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 668 — The Physical Wall-Conductor Support Is Coprime to the Quartic

## Hard-to-vary claim

The algebraic quartic \(\mathcal Q\) is absent from the diagonal support of
the canonical physical shared-wall cocycle. It divides neither an individual
normalized-wall conductor resultant nor their total product.

## Frozen source data

Entry 594 derived the three exact conductor resultants of the nonzero wall
components \(\rho_1,\rho_2,\rho_3\):

\[
\begin{aligned}
R_1={}&-x^3+x^2y+3x^2z+xy^2+2xyz+xz^2\\
&-y^3-y^2z+yz^2+z^3,\\
R_2={}&x^3-x^2y+x^2z-xy^2-2xyz-xz^2\\
&+y^3-3y^2z-yz^2-z^3,\\
R_3={}&E^2.
\end{aligned}
\]

Entry 648 assembles those components into the closed source-derived cocycle

\[
\rho_{\rm phys}=(\rho_1,\rho_2,\rho_3;0).
\]

No fitted wall, projector, or absolute \(\mathcal T_7\) coordinate is used.

## Exact support test

Using

\[
\mathcal Q
=
4AB-(A+B-E^2)^2
=
-16x^2y^2-8xyE^2+8(x+y)E^3-5E^4,
\]

exact polynomial gcd calculations over \(\mathbb Q[x,y,z]\) give

\[
\gcd(\mathcal Q,R_1)
=
\gcd(\mathcal Q,R_2)
=
\gcd(\mathcal Q,R_3)
=
1.
\]

Consequently,

\[
\boxed{
\gcd(\mathcal Q,R_1R_2R_3)=1.
}
\]

The full wall-conductor support has degree eight; it contains two cubic
components and the total-energy component \(E^2\), but no
\(\mathcal Q\)-component.

## Interpretation

This is a support statement, not a full connection calculation. It excludes

\[
\mathcal Q
=
\text{rank loss or diagonal singular support of }
\rho_{\rm phys}
\]

on the normalized wall/conductor complex.

It does not exclude \(\mathcal Q\) from

- the supported Gysin map \(i_{W!}\);
- the commutator between parameter transport and localization boundary;
- an off-diagonal extension between the wall complex and the algebraic
  kernel.

Thus Entries 667 and 668 jointly remove both source-visible scalar divisors:
neither the unsplit numerator-zero collision nor the canonical wall
conductor support generates \(\mathcal Q\).

## Classification

\[
\boxed{
\mathcal Q
\text{ is not existing wall/conductor carrier support.}
}
\]

No new carrier datum is indicated. If \(\mathcal Q\) belongs to the physical
relative object, its remaining typed home is secondary comparison or
extension data.

## Next falsifier

Construct the minimal labelled residue--Čech bicomplex required by Entry
666 and first reproduce

\[
\operatorname{Res}(\Omega_{\rm phys})=\rho_{\rm phys}.
\]

Then compute the connection-residue commutator. The decisive test is whether
\(\mathcal Q\) appears only in that secondary map while remaining absent
from the diagonal bulk and wall supports.

## Evidence

- \`research/benincasa/check_physical_wall_conductor_q_support.py\`;
- \`research/benincasa/physical-wall-conductor-q-support.json\`;
- Entries 594, 648, 666, and 667.

## Outcome contract

~~~json
{
  "claim": "Q is a component of the normalized physical wall-conductor support.",
  "status": "falsified",
  "wall_component_degrees": [3, 3, 2],
  "individual_gcds_with_Q": [1, 1, 1],
  "total_support_gcd_with_Q": 1,
  "new_carrier_datum": false,
  "surviving_home": "supported Gysin commutator or off-diagonal extension",
  "next_experiment": "Construct the labelled residue-Cech bicomplex and test its connection-residue commutator."
}
~~~
