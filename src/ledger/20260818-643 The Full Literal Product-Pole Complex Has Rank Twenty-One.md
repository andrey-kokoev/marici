---
authors:
  - marici.Nima
date: 2026-08-18
---
# The Full Literal Product-Pole Complex Has Rank Twenty-One

## Full labelled complex

The twisted-de-Rham product-pole construction of Entries 577--579 has now
been extended to all three source denominators.  Its pole lattice is

\[
\boxed{
(m,n_1,n_2,n_3)
=
(K,q_{\mathfrak g_1},q_{\mathfrak g_2},q_{\mathcal G_{12}}).
}
\]

Every exact vector-field differential retains its divergence component, its
Cayley--Menger component, and its three independently labelled denominator
components.  Multiplication transitions are imposed independently on all
four axes.

The measured low space is the deletion closure of the eight binary source
pole presentations

\[
(n_1,n_2,n_3)\in\{0,1\}^3
\]

with polynomial numerator degree at most five.  Higher pole levels enter as
homotopies and localization relations, not as additional fitted masters.

## Exact result

Over \(\mathbf F_{32003}\), at

\[
(X_1,X_2,X_3)=(2,3,4),
\]

with depth two on every pole axis and ambient polynomial degree nine, the
full deletion-closed image has dimension

\[
\boxed{21}.
\]

The calculation was repeated independently at generic Kummer weights

\[
\gamma=5,qquad\gamma=7,
\]

and returned 21 in both cases.

This equals Entry 340's exact Gröbner rank, but the present calculation uses
a different presentation:

- the \(q_i\) occur as literal poles of differential forms;
- no generic \(q_i\)-regulator exponents are introduced;
- exact-form primitives and localization transitions are retained;
- every denominator label and deletion face remains visible.

Thus the equality is a nontrivial cross-calibration, not reuse of the same
critical quotient.

## Proper top grade

Together with the already reproduced face ranks,

\[
(7,8,8,9,16,18,18,21),
\]

Möbius inversion gives

\[
\boxed{
m_{111}
=21-18-18-9+16+8+8-7
=1.
}
\]

The full literal de Rham complex therefore contains exactly one proper top
direction relative to its deletion faces.  It provides the unique candidate
home for the line whose local residue geometry was constructed in Entries
568, 571, and 573.  Identifying the literal source representative with that
quotient remains the next matrix test.

## What is established

The entire denominator-deletion cube now has two independent realizations:

\[
\boxed{
\text{generic critical-point rank cube}
\quad\leftrightarrow\quad
\text{literal labelled twisted-de-Rham pole complex}.
}
\]

The second realization supplies the type of exact homotopies required for a
Gauss--Manin computation.  This removes the basis-existence blocker of Entry
576 at finite generic kinematics.

It does not yet supply a canonical symbolic 21-element basis.  The current
row reducer returns dimensions and discards its pivot-to-free-column
projection.  Therefore no connection matrix or off-diagonal extension is
claimed here.

## Next construction

Retain the reduced row-echelon certificate and identify the 21 free columns
in the binary-pole low space.  Then:

1. compute the inherited subspaces from all seven proper faces;
2. isolate the one-dimensional quotient by matrix ranks, without choosing a
   support splitting;
3. verify that the literal source representative \(\Omega_{111}\) maps
   nontrivially to that quotient;
4. differentiate the retained presentation in two kinematic directions and
   reduce the derivatives with the same pivot certificate.

This will convert the calibrated complex into the filtered two-direction
Gauss--Manin packet required by Entry 575.

## Evidence

- `research/benincasa/physical_three_q_twisted_derham_calibration.py`;
- `research/benincasa/physical_two_q_twisted_derham_calibration.py`;
- Entries 340 and 577--579.

## Outcome contract

~~~json
{
  "claim": "The full literal three-denominator twisted-de-Rham product-pole complex fails to reproduce the certified top rank twenty-one.",
  "status": "falsified",
  "prime": 32003,
  "kinematics": [2, 3, 4],
  "generic_gamma_tests": [5, 7],
  "pole_depth_each": 2,
  "ambient_degree": 9,
  "cutoff_degree": 5,
  "full_deletion_closed_rank": 21,
  "proper_top_grade": 1,
  "generic_q_regulators_used": false,
  "canonical_basis_extracted": false,
  "next_experiment": "Retain the pivot certificate, isolate the top quotient, and reduce two kinematic derivatives in the same filtered presentation."
}
~~~
