# 1721 — Independent Coherent Inputs Descend by Labelled Density-Kernel Tensor Product

## Cut falsifier

Entry 1720 derives the full Hermitian component density kernel for coherent
Gaussian input.  For two independent labelled inputs, freeze

\[
\rho^{XY}_{(j,k),(j',k')}
=\rho^X_{jj'}\rho^Y_{kk'}.
\]

No equal-displacement occurrences are identified.

## Exact descent

The partial trace is

\[
\boxed{
\operatorname{Tr}_Y(\rho^X\otimes\rho^Y)
=\operatorname{Tr}(\rho^Y)\rho^X.
}
\]

For normalized \(\rho^Y\), this recovers \(\rho^X\) exactly.  Likewise, for
labelled transition kernels \(A,B\),

\[
\operatorname{Tr}
\bigl((\rho^X\otimes\rho^Y)(A\otimes B)\bigr)
=
\operatorname{Tr}(\rho^XA)\operatorname{Tr}(\rho^YB).
\]

## Narrow result

Independent coherent inputs close under the ordinary labelled tensor product
of component density kernels.  The relevant interchange is the canonical
bosonic tensor symmetry.  Entry 1719's generic commutator is not activated by
this source construction.

The enlargement remains coefficient-theoretic; no new Cut carrier stratum or
braiding cell is required.

## Durable artifacts

- `research/benincasa/checkers/coherent_density_kernel_cut.rs`
- `research/benincasa/results/coherent-density-kernel-cut.json`
- `research/benincasa/coherent-density-kernel-cut.md`

## Next falsifier

Admit entangled, non-product component kernels.  Test whether the complete
joint density kernel and ordinary partial trace suffice, including rank loss
and conditioning on a zero-probability measurement outcome, or whether the
singular quantum instrument introduces a new Rees coefficient direction.
