# Bordered-pencil coefficient comparison

## Formal target

For a finite carrier index `ι`, the formal pencil uses the port/carrier sum
`Unit ⊕ ι`. Its constant block is

\[
L_0=\begin{pmatrix}0&c^*\\b&A\end{pmatrix},
\]

and its spectral coefficient is the carrier projection

\[
P=\begin{pmatrix}0&0\\0&I\end{pmatrix}.
\]

The metric is initially arbitrary for the projection-commutation theorem and
is then represented as

\[
J=\begin{pmatrix}\alpha&0\\0&K\end{pmatrix}.
\]

## Grothendieck theta cross-transfer mapping

Grothendieck's finite compression uses `A` for the Hermitian theta carrier,
`b` for the forcing port `b₀`, and `c` for the observation port `b_f`. The Lean
object `borderedPencil A b c λ` is his canonical bordered exteriorization on a
real spectral parameter. `borderedPencil_isHermitian_iff_ports_equal` proves
the exact obstruction stated in
`theta-cross-transfer-has-a-bordered-determinant-not-a-self-adjoint-pencil.md`:
the pencil is Hermitian precisely when `b₀ = b_f`.

This theorem does not identify the two ports, replace the bordered determinant
by the full two-port Weyl determinant, or assert a Hilbert realization. It
therefore preserves Grothendieck's distinction between divisor-faithful
exteriorization and self-adjoint authority. The later block-metric theorems
address possible Krein symmetrizers; they do not retroactively make the
ordinary bordered pencil Hermitian.

The coefficient comparison is split into three typed results:

- `affine_coefficients_eq` separates constant and linear coefficients;
- `carrierProjection_commutation_forces_blockDiagonal` proves that the
  spectral coefficient forces the off-diagonal metric blocks to vanish;
- `borderedConstant_symmetrizer_coefficients` extracts
  \(AK=KA\), \(Kb=\alpha c\), and the adjoint row equation.
- `adjointPortEquation` derives the row equation from \(Kb=\alpha c\) using
  Hermiticity of `K` and reality of `α`.
- `borderedConstant_selfadjoint_of_coefficients` proves the converse, and
  `borderedConstant_symmetrizer_iff` packages the exact finite criterion.
- `blockMetric_commutes_carrierProjection` supplies the spectral-coefficient
  identity automatically for a block metric.
- `borderedPencil_selfadjoint_of_coefficients` reconstructs
  \(L(\lambda)^*J=JL(\lambda)\) for every real `λ`. The real-parameter type is
  essential because conjugate-linearity would alter a complex coefficient.
- `borderedPencil_symmetrizer_forces_blockDiagonal` starts from the actual
  full-pencil equation for an arbitrary constant metric `J`, performs the
  affine coefficient comparison, and concludes both block diagonality and the
  constant symmetrizer equation.
- `blockMetric_mulVec_injective_iff` supplies the missing nondegeneracy
  interface: the block action is injective exactly when `alpha` is nonzero and
  the carrier action `K *ᵥ -` is injective. The auxiliary `portLift` and
  `carrierLift` witnesses keep the two failure modes visibly independent.
- `blockMetric_mulVec_eq_zero_iff` gives the stronger pointwise kernel
  decomposition: a block vector lies in the metric kernel exactly when its
  boundary coordinate solves `alpha * z = 0` and its carrier coordinates lie
  in the kernel of `K`.
- `zeroBoundaryWeight_blockMetric_not_injective` and
  `carrierKernelWitness_blockMetric_not_injective` expose those two failures
  as reusable hostile constructors: neither a good carrier block nor a
  nonzero boundary scalar can repair degeneracy in the other block.

## Assumptions

The carrier is finite (`Fintype ι`) with decidable equality. Matrices and port
vectors have complex coefficients. The carrier matrix `A` and carrier metric
`K` are Hermitian. The boundary weight `α` is real. Invertibility and
nondegeneracy are not needed for coefficient extraction and are therefore not
assumed. For the displayed block form, `blockMetric_mulVec_injective_iff`
states the exact additional assumptions needed for nondegeneracy: nonzero
boundary weight and injective carrier action.

The simple-spectrum conclusion is deliberately coordinate-local:
`real_ratio_of_real_weights` proves that a scalar equation
\(k b=\alpha c\), with real `k`, nonzero real `α`, forces `c` to be a real
multiple of `b`. A separate spectral theorem is needed to derive diagonal
real weights from simple spectrum and Hermitian commutation.

`support_matches_of_nonzero_real_weights` proves \(b=0\iff c=0\) when both
weights are nonzero. At a nonzero port coordinate,
`port_ratio_eq_real_weight_ratio` proves the exact formula
\(c/b=k/\alpha\). `support_mismatch_forbids_nonzero_real_weights` packages the
corresponding finite falsifier.
`nonreal_port_ratio_forbids_real_weights` packages the complementary
falsifier: one nonzero imaginary part of \(c/b\) rules out all real diagonal
weights with nonzero boundary scale.
`zero_one_support_mismatch_fixture` and `one_I_nonreal_ratio_fixture`
instantiate the two obstructions with the minimal coordinate pairs
\((b,c)=(0,1)\) and \((b,c)=(1,i)\).

## Hostile example

The singleton-carrier construction separates algebraic symmetrization from
metric nondegeneracy. `singularSymmetrizerHostile_selfadjoint` proves that the
full real pencil with `A = 0`, `b = c = 0`, `alpha = 1`, and `K = 0` satisfies
the coefficient-level selfadjointness equation. At the same time,
`singularMetricKernelVector_ne_zero` and
`singularBlockMetric_kills_kernelVector` exhibit a nonzero vector killed by the
block metric, and `singularBlockMetric_mulVec_not_injective` proves that its
matrix action is not injective. Thus the coefficient equations do not imply
invertibility or nondegeneracy; either property must enter through an
independent assumption before the block form can be treated as a genuine
Krein metric. The kernel proof now instantiates
`blockMetric_mulVec_eq_zero_iff`, so the concrete hostile also checks the shared
boundary/carrier decomposition rather than duplicating its coordinate proof.

`hostileKreinOperator` is

\[
H=\begin{pmatrix}0&1\\-1&0\end{pmatrix}
\]

and `hostileKreinMetric` is \(J=\operatorname{diag}(1,-1)\). The file states
and proves \(H^*J=JH\), together with explicit eigenvectors for eigenvalues
\(i\) and \(-i\). Thus indefinite selfadjointness supplies conjugate symmetry,
not real-spectrum confinement.

## Verification status

Per Nima's explicit instruction, no Lean compilation or project build was run
for this increment. The file is intentionally not imported by
`MariciFormal.lean` until it receives a targeted elaboration check.

## Missing interfaces

- A reusable theorem that a Hermitian matrix commuting with a simple-spectrum
  Hermitian matrix is diagonal with real diagonal entries.
- A library-level bridge from finite matrix-action injectivity to the preferred
  typed definition of a nondegenerate Krein inner product.
- Source authority identifying a particular `K`; solving the equations does
  not make a fitted metric source-derived.
