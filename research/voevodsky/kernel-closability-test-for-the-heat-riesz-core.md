# Kernel closability test for the heat-Riesz core

## Question

What exact finite-data-compatible test decides whether a source-defined form on the dense heat-Riesz span extends to a closed form on the order completion?

## Claim boundary

Closability is equivalent to exclusion of one typed null-sequence residual. Positivity of every finite kernel matrix does not imply closability. This packet defines the test but does not evaluate the Marici completed source kernel because its joint gamma-plus-prime values have not been supplied on the heat-Riesz span.

## Two kernels

Let \(r_t\in\mathcal H_{\rm ord}\) represent the heat functional \(L_t\). The base kernel is

\[
G(s,t)
=
\langle r_s,r_t\rangle_{\rm ord}.
\]

Suppose the completed source form defines a Hermitian kernel

\[
K(s,t)
=
q(r_s,r_t).
\]

Because the \(r_t\) are total, \(K\) determines \(q\) on their algebraic span.

## Sequential criterion

The form is closable precisely when every sequence

\[
f_n
=
\sum_j c_{n,j}r_{t_{n,j}}
\]

satisfying

\[
\lVert f_n\rVert_G
\longrightarrow0
\]

and

\[
q(f_n-f_m)
\longrightarrow0
\]

also satisfies

\[
q(f_n)
\longrightarrow0.
\]

In kernel coordinates these quantities are finite Gram contractions:

\[
\lVert f_n\rVert_G^2
=
c_n^*G_n c_n,
\qquad
q(f_n)
=
c_n^*K_n c_n.
\]

Thus a failed completion has an explicit residual: a base-null, form-Cauchy sequence whose form value survives.

## Positivity is insufficient

On finite-support sequences, let

\[
L(x)=
\sum_{j\geq1}jx_j,
\qquad
q(x)=|L(x)|^2.
\]

Every finite kernel matrix

\[
K_{ij}=ij
\]

is positive semidefinite. But with

\[
x_n=
\frac1n e_n,
\]

one has

\[
\lVert x_n\rVert^2=
\frac1{n^2}
\longrightarrow0,
\]

while

\[
q(x_n)=1,
\qquad
q(x_n-x_m)=0.
\]

Hence the positive form is not closable.

## Application contract

To test the Marici form, the source side must provide exact polarized values

\[
K(s,t)
=
Q_{\Gamma+P}(r_s,r_t)
\]

with a declared regularization shared across all finite linear combinations. Diagonal values alone are insufficient: closability depends on \(K(s,t)\) for unequal parameters.

A computational hostile should then search generalized Gram directions with small \(G\)-norm and stable nonzero \(K\)-value across increasing parameter sets. Such a sequence is a mathematical obstruction only after the kernel entries themselves are source-certified.

## Higher-coherence interpretation

Finite positivity concerns each matrix \(K_n\). Closability concerns compatibility of those matrices with the base topology under refinement. The null-sequence residual is therefore the first higher coherence condition not visible in any isolated finite observer.

## Disposition

The exact acceptance and falsification test for `common_closed_form_domain` is now fixed. The first missing typed object is the polarized, jointly regularized source kernel \(K(s,t)\), not another diagonal positivity table.

## Verification

- `research/voevodsky/checkers/check_heat_kernel_closability_witness.py`
- `research/voevodsky/results/heat_kernel_closability_witness.json`
