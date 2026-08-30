# Additive prime-edge budget: Lean packet

Source: `research/grothendieck/additive-prime-edge-budget-theorem.md`.

Formal object: for a finite index type `ι`, real edge coefficients
`coefficient : ι → ℝ`, and Boolean Walsh polarity `polarity : ι → Bool`,
`additiveEdgeEigenvalue` is

\[
1+\sum_i \varepsilon_i r_i,
\qquad \varepsilon_i\in\{1,-1\}.
\]

`additiveEdgeSpectrum_nonnegative_iff` proves that every such eigenvalue is
nonnegative precisely when

\[
\sum_i |r_i|\le 1.
\]

The proof constructs the coefficient-opposite polarity, whose eigenvalue is
`1 - ∑ i, |coefficient i|`, and proves the converse termwise from
`-|r_i| ≤ ε_i r_i`.

`twoEdge_individual_bounds_do_not_glue` is the finite hostile model: two
coefficients equal to `3/5` each satisfy the individual contraction bound, but
the all-negative Walsh eigenvalue is negative.

Typing boundary: `ι` is an arbitrary finite type and coefficients are real.
The module formalizes the finite diagonal spectrum and its exact positivity
criterion. It does not formalize the Fourier diagonalization of a convolution
matrix, the completed Weil form, a prime-indexed infinite sum, or any
archimedean/endpoint compensation. Consequently it supplies no Weil-positivity
or Riemann-hypothesis conclusion.

Verification boundary: Nima's active no-build instruction forbids Lean and
project compilation. This increment was checked only by bounded static scans
and remains outside `MariciFormal.lean` pending authorized elaboration.
