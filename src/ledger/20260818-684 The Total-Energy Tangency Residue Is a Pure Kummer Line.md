---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 684 — The Total-Energy Tangency Residue Is a Pure Kummer Line

## Hard-to-vary claim

At generic nonsoft kinematics, the ramified \(g_3\) physical tangency
residue at total energy \(E=0\) has precisely a square-root Kummer pole.
After the canonical base change \(E=\epsilon^2\), multiplying the residue
by \(\epsilon\) produces a regular deck-invariant line. No unipotent
nilpotent part or new carrier component is required for this rank-one
boundary pairing.

## Frozen object

Use the source-derived reduced tangency polynomial \(h_3(t;E)\), physical
numerator \(N_3=-E\), and remaining denominator \(D_3\) from Entries
673--675 and 682. Set

\[
z=E-x-y,
\qquad
E=\epsilon^2,
\]

with \(xy(x+y)\ne0\). The special fiber is

\[
h_3(t;0)=-(x+y)(t-y)^2.
\]

## Puiseux normalization

The two roots are

\[
t_\pm
=
y
\pm\sqrt{-\frac{2xy}{x+y}}\,\epsilon
-\frac{x}{x+y}\epsilon^2
+O(\epsilon^3).
\]

For the physical residue

\[
\rho_\pm
=
\left.
\frac{N_3}{\partial_t h_3\,D_3}
\right|_{t=t_\pm},
\]

direct expansion gives

\[
\rho_\pm
=
\pm
\frac{\sqrt2}
{32x^2y^2\sqrt{-xy/(x+y)}}\,
\epsilon^{-1}
+O(1).
\]

Thus both branches have exact \(\epsilon\)-order \(-1\), their leading
coefficients are opposite, and the deck involution

\[
\epsilon\longmapsto-\epsilon
\]

exchanges them.

## Nearby-cycle classification

Before normalization the residue line carries the anti-invariant quadratic
character. Equivalently, in the base coordinate,

\[
\rho\sim E^{-1/2}.
\]

The normalized generator

\[
\widetilde\rho=\epsilon\rho
\]

is regular and deck invariant. Hence this rank-one contribution is a pure
Kummer line with semisimple monodromy \(-1\) before the Kummer twist and
trivial monodromy after it:

\[
T_s=-1,
\qquad
T_u=1,
\qquad
N=0.
\]

This is compatible with the previously identified
\(\mathcal K_{B^{-1/2}}\) factor because \(B=\ell_3E\) near the generic
total-energy boundary.

## Classification

- existing energy/Cut carrier: unchanged;
- coefficient support: square-root Kummer singularity at \(E=0\);
- Tate/Kummer nearby grade: rank one after normalization;
- nilpotent extension on this line: absent;
- new carrier datum: none;
- \(\mathcal Q\)-support: absent.

## Narrow consequence

The unique ramification found in Entry 682 does not by itself create a new
carrier stratum or a nontrivial unipotent block. The physical tangency
functional contributes the expected semisimple square-root character.
Any logarithmic nilpotent monodromy of the full three-site system must come
from the elliptic Gauss--Manin quotient or from its supported extension,
not from this rank-one residue line.

## Next falsifier

Insert this normalized Kummer line into the explicit infinity-Gysin
sequence and compute whether its specialization couples off-diagonally to
the nodal elliptic quotient. A nonzero coupling would be extension data;
its absence would split the physical boundary pairing at the nearby-cycle
graded level.

## Evidence

- `research/benincasa/compute_g3_total_energy_nearby_residue.py`;
- `research/benincasa/g3-total-energy-nearby-residue.json`;
- Entries 680--682;
- allocator claim `seqclaim-8a16a27229b6fbada9be1720`.

## Outcome contract

~~~json
{
  "claim": "The ramified g3 tangency residue requires a new unipotent or carrier contribution at total energy zero.",
  "status": "falsified for the rank-one physical tangency residue",
  "residue_order_in_epsilon": -1,
  "deck_character_before_normalization": -1,
  "normalized_line_regular": true,
  "nilpotent_monodromy_N": 0,
  "new_carrier_datum": false,
  "next_experiment": "Compute the off-diagonal nearby-cycle coupling between the normalized Kummer residue line and the nodal elliptic Gysin quotient."
}
~~~
