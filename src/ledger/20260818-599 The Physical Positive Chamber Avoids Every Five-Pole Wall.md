---
authors:
  - marici.Nima
date: 2026-08-18
---
# 599 — The Physical Positive Chamber Avoids Every Five-Pole Wall

## Hard-to-vary claim

The primary physical contour does not meet any denominator wall in either
rank-thirty-five five-pole family.  Consequently its geometric boundary is
the Cayley--Menger boundary, not the conductor boundary of the cohomological
localization complex.

## Source-defined chamber

The primary source defines the loop contour by non-negativity of the
Cayley--Menger simplex and all of its faces.  In particular,

\[
X_1,X_2,X_3>0,
\qquad
y_{12},y_{23},y_{31}\ge0.
\]

The relevant connected-subgraph denominators are

\[
\begin{aligned}
q_{g_1}&=X_1+y_{12}+y_{31},\\
q_{g_2}&=X_2+y_{12}+y_{23},\\
q_{g_3}&=X_3+y_{23}+y_{31},\\
q_{G_{12}}&=X_1+X_2+X_3+y_{12},\\
q_{g_{23}}&=X_2+X_3+y_{12}+y_{31},\\
q_{g_{31}}&=X_3+X_1+y_{12}+y_{23}.
\end{aligned}
\]

Every coefficient is nonnegative and every form contains a strictly
positive site energy.  Hence

\[
q>0
\]

for every denominator occurring in either physical five-pole summand.

## Chain consequence

Let \(W\) be the union of these denominator walls and let \(\Gamma\) be the
physical real integration chain.  Then

\[
\boxed{\Gamma\cap W=\varnothing.}
\]

The physical period is therefore a well-defined pairing with the relative
cohomology class on \(S_E\setminus W\), but the boundary of \(\Gamma\) does
not run along \(W\) or its conductor.  Its boundary is instead selected by
the vanishing faces of the Cayley--Menger measure.

Thus the contour prescription does not supply the missing
conductor-to-infinity nullhomotopy isolated in Entry 597.  The conductor
boundary is a boundary of the **coefficient object**, not a geometric
boundary component of the primary real chain.

## Interpretation

This separates two notions that had remained close:

\[
\text{physical semialgebraic chain boundary}
\ne
\text{localization boundary of the meromorphic form}.
\]

The Bunch--Davies prescription fixes the physical period, but no
source-derived operation presently turns that period functional into a
canonical elliptic projection of the relative coefficient class.

## Updated frontier

The next admissible construction is the relative period pairing itself:
retain the rank-twenty wall complex, pair its bulk term with \(\Gamma\), and
test whether integration by parts produces a canonical chain homotopy on
the Cayley--Menger faces.  A wall-supported homotopy is now excluded.

## Evidence

- `temp/arxiv-2408.16386-source/sections/cosmologicalintegrals.tex`, lines
  78--104;
- `temp/arxiv-2408.16386-source/sections/applications.tex`, lines 202--256;
- `research/benincasa/physical_positive_chamber_q_wall_gate.py`;
- Entries 596--597.

## Outcome contract

~~~json
{
  "claim": "The primary physical integration chain acquires a boundary component on one of the five-pole denominator walls.",
  "status": "falsified_in_physical_positive_chamber",
  "five_pole_families_checked": 2,
  "denominator_forms_checked": 6,
  "physical_contour_intersects_q_wall_divisor": false,
  "chain_boundary_type": "Cayley-Menger faces",
  "localization_boundary_type": "coefficient-object conductor",
  "next_experiment": "Construct the relative period pairing and audit the integration-by-parts homotopy on Cayley-Menger faces."
}
~~~
