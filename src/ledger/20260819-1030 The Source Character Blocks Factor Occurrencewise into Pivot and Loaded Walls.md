# 1030 — The Source Character Blocks Factor Occurrencewise into Pivot and Loaded Walls

## Exact source presentation

Entry 1029 notes that Entry 943 exported only its maximal minor. The durable
checker now exports the two source rows on both the \(X=+1\) and \(X=-1\)
sheets, together with the character supports

\[
\{0,2\},\quad\{1\},\quad\{3\},\quad\{4,5\}.
\]

On each two-dimensional support, the two sheet rows have the form

\[
\begin{pmatrix}
b_i&b_j\\
-b_i&b_j
\end{pmatrix}.
\]

The fixed character-row transformation diagonalizes this matrix. Its
determinant is \(2\), so the construction is invertible over
\(\mathbb Q\) but retains Entry 943's integral two-primary caveat.

## Six occurrencewise products

Up to declared Laurent units and occurrence permutation, the rational source
presentation becomes diagonal with entries \(p_iq_i\):

\[
\begin{array}{c|c}
p_i&q_i\\ \hline
(A_3B_{34})^2-1&(ZA_2B_{24})^2-1\\
A_3^2-1&(ZA_2B_{24})^2-1\\
(A_2B_{24})^2-1&(A_3B_{34})^2-Z^2\\
A_2^2-1&(A_3B_{34})^2-Z^2\\
A_3^2-1&(ZA_2)^2-1\\
A_2^2-1&A_3^2-Z^2.
\end{array}
\]

The \(p_i\) are exactly the six unshifted/pivot factors missing from
Entry 1028's determinant. The \(q_i\) have multiplicities

\[
(1,2,1,2)
\]

on the four loaded composite walls.

## Comparison with the loaded boundary complex

Entry 968 proves that the absolute chamber skeleton of \(C\) is unimodular
under all allowed orientation and endpoint gauges. Therefore

\[
\mathcal P_{\rm load}
\simeq
\left[
R^6\xrightarrow{\operatorname{diag}(q_i)}R^6
\right]
\]

up to an integral target gauge and occurrence permutation.

Consequently, over the rational Laurent ring,

\[
\boxed{
\mathcal P_{\rm load}
\simeq
\operatorname{Sat}_{(p_i)}(\mathcal P_{\rm src})
}
\]

where the saturation is performed occurrencewise using the independently
labelled Cartier factors \(p_i\). This is not an ordinary quotient or a
postulated splitting; it is the diagonal source presentation after removing
the labelled existing-wall factor in each occurrence.

## Narrow conclusion

\[
\boxed{
\text{the loaded boundary complex is the rational occurrencewise Cartier
grade of the frozen source character presentation.}
}
\]

This upgrades Entry 1029's determinant evidence to an explicit presentation
calculation. It supports the shared carrier/calculus thesis: the transition
from the full source lattice to the loaded corner object uses existing
Cartier walls and changes the coefficient layer.

The result is not yet integral. The two character transforms have determinant
\(2\), and the pre-existing order-four projector issue remains unresolved.

## Next falsifier

Construct the saturation without rational character projectors in the native
six-occurrence orbit lattice. Compute its Smith data and compare it with the
integral loaded-path presentation. The decisive outcomes are:

- equality: the Cartier grade exists integrally;
- a finite two-primary cokernel: the rational grade survives with an
  arithmetic coefficient defect;
- a free cokernel: the proposed source-to-loaded Cartier operation fails.

## Durable evidence

- extended checker:
  'research/benincasa/marici-gm/src/bin/string_six_point_cartier_sheet_transition.rs';
- extended packet:
  'research/benincasa/string-six-point-cartier-sheet-transition.json';
- result packet:
  'research/benincasa/string-six-point-source-occurrence-products.json';
- verified command:
  'cargo run --quiet --bin string_six_point_cartier_sheet_transition';
- allocator claim:
  'seqclaim-34027b38a845dc9f88b2a718'.
- epistemic event:
  'ev-000000000649-a1dd745e-f47d-481f-944f-4328e8695bc3'.
