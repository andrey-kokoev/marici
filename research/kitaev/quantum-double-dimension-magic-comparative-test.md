# Quantum dimension predicts typed quarter spectra in four finite doubles so far

Owner: `marici.Kitaev`

Ledger: Entries 2471--2474  
Graph: `ev-000000003389-98d2469d-5dac-434c-aedf-68d33cd3f28e`,
`ev-000000003391-792b3e78-aa0b-4e95-8559-d4027dc683dd`,
`ev-000000003394-992c0ebf-9307-4415-ba1b-fd0e2aab3957`,
`ev-000000003397-cb1e0507-58c3-40a3-ab6c-e2e6ba278785`

Status: DPC-QW falsified by a typed nonvacuum product-double counterexample
in $D(S_4\times D_4)$. Earlier single-group confirmations remain valid data,
not a universal law.

## Sharpened Deutsch--Popper conjecture

For a finite group (G), let (x) be a nonvacuum simple object of (D(G))
whose Wilson character row

\[
  \lambda_x(a)=S_{xa}/S_{0a}
\]

is real and integral. Define the quarter evolution

\[
  U_x=\exp(2\pi iW_x/4).
\]

**DPC-QW.** Within a fixed quantum double, the eigenvalue-multiplicity
spectrum of (U_x) depends only on the quantum dimension (d_x).

The vacuum is excluded: (W_0=I) is distinguished by its unit role even when
other invertible sectors also have dimension one. Non-Hermitian Wilson rows
are excluded because exponentiating the raw oriented loop is not a unitary
Hamiltonian operation.

## First hostile comparison: (D(D_4))

The checker constructs all 22 simples directly from conjugacy classes and
centralizer irreducible characters, then derives the exact modular (S)
matrix. Symmetry, unitarity, and recovery of all quantum dimensions pass.
Every Wilson character eigenvalue is integral.

The naive vacuum-inclusive conjecture fails: the vacuum and the other seven
dimension-one sectors have different spectra. But the corrected nonvacuum
claim survives:

- all seven nonvacuum dimension-one sectors share one quarter spectrum;
- all fourteen dimension-two sectors share one quarter spectrum.

There are zero nonvacuum counterexamples.

## Second hostile comparison: (D(A_4))

The checker independently constructs the 14-sector modular matrix. This case
contains the important comparison between a dimension-three pure electric
charge and four dimension-three double-transposition flux sectors.

Eight oriented Wilson rows have complex eigenvalues and are rejected by the
Hamiltonian typing gate. On the six real integral rows, the vacuum and all
five dimension-three sectors remain. The pure charge and all four flux
sectors have exactly the same quarter spectrum. Again there are zero typed
nonvacuum counterexamples.

## Meta-level status

The (D(S_3)) result is no longer an isolated coincidence: DPC-QW survives
two independently generated non-Abelian quantum doubles, including a
same-dimension charge--flux comparison.

## Predeclared prediction: (D(S_4))

Before constructing the 21-sector modular matrix, the risky prediction was
fixed: zero typed nonvacuum equal-dimension counterexamples. The checker then
derived all five conjugacy sectors and their centralizer characters. Every
Wilson row is real and integral; modular symmetry, unitarity, and all quantum
dimensions pass. The prediction survives with zero counterexamples across
dimensions (1,2,3,6,8). In particular, each of the six dimension-three,
nine dimension-six, and three dimension-eight sectors has the unique quarter
spectrum for its dimension.

DPC-QW has therefore survived (D(S_3)), (D(D_4)), (D(A_4)), and
(D(S_4)). This is strong corroboration, not an explanation or proof.
Quantum dimension is only the vacuum entry of a Wilson character row; no
theorem yet forces it to determine the whole residue histogram.

## Modulus four is essential

The stronger modulus-independent statement fails inside (D(S_4)). There
are eight pairs of equal-dimensional nonvacuum sectors with different raw
integer fusion spectra. The first compares two dimension-six sectors:

\[
\begin{aligned}
2{:}uv00 &: \{-6{:}1,-2{:}4,0{:}11,2{:}4,6{:}1\},\\
22{:}two &: \{-2{:}6,0{:}11,2{:}1,6{:}3\}.
\end{aligned}
\]

They become identical modulo four: eleven zero residues and ten residues
equal to two. Exhausting moduli (2\) through (12\), the equal-dimension law
survives only modulo (2) and modulo (4); each of
(3,5,6,7,8,9,10,11,12) retains all eight counterexamples.

Thus DPC-QW is not a shadow of equality of fusion spectra. It is specifically
a 2-primary congruence phenomenon. Modulus two records mostly parity;
modulus four is the first nontrivial surviving refinement and is also exactly
the modulus selected by the controlled quarter-phase compiler. Explaining
that coincidence is now the central theorem target.

A proper explanation must derive the histogram collapse from finite-group
character orthogonality, fusion-ring constraints, or another invariant. The
next falsification targets are groups with several inequivalent nonvacuum
conjugacy/centralizer constructions at the same dimension and real integral
Wilson rows, such as suitable order-16 groups or (S_4).

## Falsifiers and boundaries

DPC-QW fails upon finding two typed nonvacuum rows in the same (D(G)) with
equal quantum dimension but different mod-four eigenvalue multiplicities.
Complex rows must first be paired with their duals or otherwise converted to
a declared Hermitian observable; silently reducing complex eigenvalues modulo
four is forbidden. Cross-group equality is not claimed.

## Decisive product-double falsifier

The direct-product theorem gives

\[
  D(G\times H)\simeq D(G)\boxtimes D(H).
\]

Simple dimensions and Wilson eigenvalues multiply, so mod-four spectral
multiplicities tensor-convolve. In $D(S_4\times D_4)$ choose typed nonvacuum
factor sectors with dimensions

\[
  3\times2=6,
  \qquad
  6\times1=6.
\]

The two product sectors have equal dimension but different spectra:

\[
\begin{aligned}
(3,2)&:\{0{:}282,2{:}180\},\\
(6,1)&:\{0{:}242,2{:}220\}.
\end{aligned}
\]

Therefore dimension does not determine Wilson quarter spectrum even on the
typed nonvacuum domain. The four earlier groups lacked a competing
multiplicative factorization severe enough to expose the missing information.
The replacement explanation is compositional: the full Wilson character row
retains tensor-factor construction through multiplicative convolution, while
quantum dimension remembers only the product of factor dimensions.

## Artifacts

- `checkers/check_d4_quantum_double_dimension_magic_conjecture.py`
- `results/d4-quantum-double-dimension-magic-conjecture.json`
- `checkers/check_a4_quantum_double_dimension_magic_conjecture.py`
- `results/a4-quantum-double-dimension-magic-conjecture.json`
- `checkers/check_s4_quantum_double_dpc_qw.py`
- `results/s4-quantum-double-dpc-qw.json`
- `checkers/check_product_double_dpc_qw_counterexample.py`
- `results/product-double-dpc-qw-counterexample.json`
