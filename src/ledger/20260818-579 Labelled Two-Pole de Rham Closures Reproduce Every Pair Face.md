---
authors:
  - marici.Nima
date: 2026-08-18
---
# Labelled Two-Pole de Rham Closures Reproduce Every Pair Face

## Product-pole construction

The admitted literal twisted-de-Rham reducer has been extended from one
source denominator to two independently labelled denominators.  For a pair
\((q_1,q_2)\), pole presentations are indexed by

\[
(m,n_1,n_2).
\]

The exact differential of a polynomial vector-field primitive is

\[
\boxed{
\frac{\operatorname{div}V}{K^m q_1^{n_1}q_2^{n_2}}
+(\gamma-m)
\frac{V(K)}{K^{m+1}q_1^{n_1}q_2^{n_2}}
-\sum_{i=1}^2n_i
\frac{V(q_i)}{K^m q_i^{n_i+1}\prod_{j\ne i}q_j^{n_j}}.
}
\]

The implementation retains independent multiplication transitions along
all three pole axes.  Hence it preserves the source labels and the deletion
faces rather than replacing the pair by its product.

## Exact pair ranks

Over \(\mathbf F_{32003}\) at

\[
(X_1,X_2,X_3)=(2,3,4),
\]

with pole depth two on every axis and ambient degree ten, the binary-pole
deletion closures are

\[
\boxed{
\begin{array}{c|c}
\text{labelled pair}&\text{closed dimension}\\
\hline
(q_{\mathfrak g_1},q_{\mathfrak g_2})&9\\
(q_{\mathfrak g_1},q_{\mathcal G_{12}})&18\\
(q_{\mathfrak g_2},q_{\mathcal G_{12}})&18
\end{array}
}
\]

These exactly reproduce the pair entries of Entry 340's independently
certified deletion cube.

All three values are unchanged when the generic Kummer weight is changed
from \(\gamma=5\) to \(\gamma=7\).  The lower pair and one representative
mixed pair also remain unchanged at ambient degree twelve.  The equality of
the two mixed ranks is computed independently; it is not imposed by a
symmetry quotient.

## Associated-grade consequence

Combining the zero and single-pole closures from Entry 578 gives

\[
9-8-8+7=0
\]

for the proper lower-pair grade, and

\[
18-16-8+7=1
\]

for each mixed \(q_{\mathcal G_{12}}\)-lower grade.  Thus the literal
de Rham presentation reproduces not only the closed ranks but also the
pairwise support filtration

\[
\boxed{m_{011}=0,\qquad m_{101}=m_{110}=1.}
\]

This is important for the extension problem: the lower pair supplies no new
proper class, whereas each mixed face carries exactly one line through which
the proper top class can descend.

## Frontier

Every proper face of the three-denominator cube is now reproduced by a
literal, labelled twisted-de-Rham complex with exact homotopies.  The next
calculation is the full four-axis pole lattice

\[
(K,q_{\mathfrak g_1},q_{\mathfrak g_2},q_{\mathcal G_{12}}),
\]

whose binary-pole closure must have dimension \(21\).  If it does, its
row-reduction data provide an explicit finite presentation from which the
proper top generator and its two mixed-face residue images can be extracted.

## Evidence

- `research/benincasa/physical_two_q_twisted_derham_calibration.py`;
- Entries 340, 577, and 578.

## Outcome contract

~~~json
{
  "claim": "The literal labelled two-denominator twisted-de-Rham complexes fail to reproduce the pair faces of the certified deletion cube.",
  "status": "falsified",
  "prime": 32003,
  "kinematics": [2, 3, 4],
  "generic_gamma_tests": [5, 7],
  "closed_pair_ranks": {
    "q_g1_q_g2": 9,
    "q_g1_q_G12": 18,
    "q_g2_q_G12": 18
  },
  "proper_pair_grades": {
    "q_g1_q_g2": 0,
    "q_g1_q_G12": 1,
    "q_g2_q_G12": 1
  },
  "pole_depth_each": 2,
  "generic_q_regulators_used": false,
  "next_experiment": "Construct the full three-denominator product-pole complex and reproduce deletion-closed rank 21."
}
~~~
