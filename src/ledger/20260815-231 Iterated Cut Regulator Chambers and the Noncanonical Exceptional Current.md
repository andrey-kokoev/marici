---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# Iterated Cut Regulator Chambers and the Noncanonical Exceptional Current

## Record

Status: the printed positive energy-regulator conditions do not select a
unique boundary-value current after the ordered
\(q_{\mathcal G_{12}}\) residue. Four regulator chambers give three
different exceptional currents. The full occurrence-level physical boundary
map therefore remains underdetermined by the published source.

No denominator, carrier stratum, support summand, regulator hierarchy,
projector, or normalization is added.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

\[
\boxed{
\text{the published Bunch--Davies negative-imaginary prescription uniquely
determines the lower-occurrence current after the ordered Cut residue.}
}
\]

The finite falsifier was two positive energy-regulator assignments satisfying
the printed conditions that induce different currents on the same frozen
exceptional locus.

## Frozen primary prescription

Albayrak--Benincasa--Duaso Pueyo, arXiv:2305.19686v2,
equations (4.18)--(4.20), derives

\[
X_s\longmapsto X_s-i\epsilon_{X_s},
\qquad
y_e\longmapsto y_e-i\epsilon_{y_e},
\]

with positive regulator data obtained as linear combinations of the
positive contour regulators. The source describes a class of prescriptions;
it does not identify all energy regulators with one scalar. Equation (4.17)
also explicitly notes that a reduced spurious pole can have ambiguous
\(i\epsilon\) sign.

This corrects the stronger wording “common displacement” used in some
earlier Marici packets. What is source-derived is common negativity, not
equality of regulator magnitudes.

## Ordered residue

Write

\[
X_i\mapsto X_i-i\xi_i,
\qquad
y_{ij}\mapsto y_{ij}-i\eta_{ij},
\qquad
\xi_i,\eta_{ij}>0.
\]

At the \(q_{\mathcal G_{12}}=0\) pole one substitutes
\(y_{12}=-E\). The two lower denominators become

\[
q_{\mathfrak g_{31}}
=a-X_2+i(\xi_2-\eta_{23})
=A+i\alpha,
\]

\[
q_{\mathfrak g_{23}}
=b-X_1+i(\xi_1-\eta_{31})
=B+i\beta,
\]

where

\[
\alpha=\xi_2-\eta_{23},
\qquad
\beta=\xi_1-\eta_{31}.
\]

Positivity of the four energy regulators does not determine either
difference. All four nonzero sign chambers

\[
(\operatorname{sgn}\alpha,\operatorname{sgn}\beta)
\in\{(--),(-+),(+-),(++)\}
\]

occur among assignments satisfying the printed energy-level sign
conditions. This does not yet prove that the unexpanded graph-level map from
contour regulators reaches all four chambers.

## Exceptional boundary currents

Entry 230 gives \(B=-A\) on the exceptional divisor. Using

\[
\frac1{x+i0\,s}
=
\operatorname{PV}\frac1x-i\pi s\,\delta(x),
\qquad s\in\{\pm1\},
\]

one obtains

\[
\frac1{A+i0s_\alpha}
+
\frac1{-A+i0s_\beta}
=
-i\pi(s_\alpha+s_\beta)\delta(A).
\]

Thus, in units of \(i\pi\delta(A)\), the four chambers give

\[
\begin{array}{c|cccc}
(s_\alpha,s_\beta)&--&-+&+-&++\\
\hline
\text{coefficient}&2&0&0&-2.
\end{array}
\]

The equal-regulator specialization
\(\xi_1=\xi_2=\eta_{23}=\eta_{31}\) lands exactly on
\(\alpha=\beta=0\). It selects no side of either reduced pole and hence
does not repair the ambiguity.

## Noncommuting limits

If the regulators are removed before taking the weighted nearby grade,
entry 230 gives cancellation of the \(\tau^{-2}\) term and the rational
\(\tau^{-1}\) coefficient \(-n/r^2\).

If the boundary value is taken first, the \(\tau^{-2}\) grade can instead
contain

\[
2i\pi\delta(r),\qquad 0,qquad -2i\pi\delta(r),
\]

depending on the regulator chamber. Therefore

\[
\boxed{
\lim_{\tau\to0}\lim_{\epsilon\to0}
\ne
\lim_{\epsilon\to0}\lim_{\tau\to0}
}
\]

without additional source-defined transport data.

## Verdict

The uniqueness conjecture is falsified:

\[
\boxed{
\text{the published source does not canonically determine the iterated
lower-occurrence boundary map after the Cut residue.}
}
\]

This is a coefficient/chain-level underdetermination, not a failure of the
shared carrier. Every possible current is supported on the already frozen
intersection \(r=0\) of the two marked lower divisors.

Entry 321 remains valid after occurrence forgetting, and entry 230 remains
valid as the regulator-free rational weighted identity. Neither determines
the missing iterated boundary-value functor.

## Classification

- existing carrier: both lower marked divisors, their intersection
  \(r=0\), and the weighted exceptional chart;
- coefficient/chain datum: regulator-chamber-dependent delta current;
- source insufficiency: no ordered regulator hierarchy or simultaneous
  residue prescription for this four-pole corner is printed;
- elliptic Gauss--Manin data: no new component;
- genuinely new carrier datum: none.

## Exact evidence

- primary source arXiv:2305.19686v2, equations (4.17)--(4.20), pages 22--23;
- `research/benincasa/check_iterated_cut_regulator_chambers.rs`;
- `research/benincasa/iterated-cut-regulator-chambers.json`;
- exhaustive positive-integer chamber census;
- warnings-denied optimized Rust compilation and execution.

## Next finite falsifier

Consult the upstream primary construction for an explicit graph-level map
from positive contour regulators \(\epsilon_{\hat a}\) to the triangle
energy regulators

\[
(\xi_1,\xi_2,\xi_3,\eta_{12},\eta_{23},\eta_{31}).
\]

Push that cone through the ordered \(q_{\mathcal G_{ij}}\) residue.

- If its image lies in one chamber, the source geometry canonically selects
  the corresponding current and cyclic sewing can be tested.
- If it intersects multiple chambers, the nonuniqueness is intrinsic to the
  published class and the full physical occurrence lift requires an
  additional chain-level choice.
- Only if the selected current requires support outside the frozen marked
  intersection is a new carrier datum justified.

## Outcome contract

~~~json
{
  "claim": "The published negative-imaginary prescription uniquely determines the iterated lower-occurrence current.",
  "status": "falsified at the published energy-regulator level",
  "induced_regulators": {
    "q_g31": "epsilon_X2-epsilon_y23",
    "q_g23": "epsilon_X1-epsilon_y31"
  },
  "realized_chambers": ["--", "-+", "+-", "++"],
  "current_coefficients_in_i_pi_delta_units": [2, 0, 0, -2],
  "equal_regulator_diagonal_selects_side": false,
  "new_carrier_incidence": false,
  "next_experiment": "Derive the explicit graph-level contour-to-energy regulator cone and test its image chambers."
}
~~~
