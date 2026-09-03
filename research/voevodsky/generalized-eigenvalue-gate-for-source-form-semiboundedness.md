# Generalized-eigenvalue gate for source-form semiboundedness

## Question

How can semiboundedness of the completed-heat source form be tested using only finite Gaussian observer packets while retaining the required global quantifier?

## Claim boundary

Uniform semiboundedness is equivalent to a uniform lower bound on all finite generalized eigenvalues of the source kernel relative to the order Gram kernel. This gives an exact finite-packet criterion but does not evaluate it for the completed heat kernel.

## Two Gram matrices

For a finite parameter set

\[
F=\{a_1,\ldots,a_m\},
\]

let

\[
G_F
=
[\langle g_{a_i},g_{a_j}\rangle_{\rm ord}]_{i,j}
\]

and

\[
K_F
=
[H(a_i+a_j)-H(a_i+a_j+h)]_{i,j}.
\]

Gaussian independence and positivity of the order norm make \(G_F\) positive definite.

For

\[
f=\sum_i c_i g_{a_i},
\]

one has

\[
\lVert f\rVert_{\rm ord}^2
=
c^*G_Fc,
\qquad
q_h(f)=c^*K_Fc.
\]

## Exact criterion

Let \(\lambda_{\min}(K_F,G_F)\) be the smallest generalized eigenvalue. The least lower-bound correction required on packet \(F\) is

\[
C_F
=
\max\{0,-\lambda_{\min}(K_F,G_F)\}.
\]

The algebraic source form is semibounded on the full Gaussian span precisely when

\[
\sup_F C_F
<\infty,
\]

where the supremum ranges over every finite parameter set.

Equivalently, there exists one \(C\) such that

\[
K_F+CG_F
\succeq0
\]

for every \(F\).

## Quantifier distinction

The statement

\[
\text{for every }F\text{ there exists }C_F
\]

is automatic in finite dimension. It does not imply

\[
\text{there exists }C\text{ for every }F.
\]

The second quantifier order is the semiboundedness theorem required for completion.

Positivity corresponding to the RH-strength cone is the stronger special case

\[
C=0.
\]

A finite negative eigenvalue does not by itself refute semiboundedness; divergence of the required constants across packets does.

## Relation to closability

A uniform lower bound allows the shift

\[
q_{h,C}(f)
=
q_h(f)+C\lVert f\rVert_{\rm ord}^2
\]

to become positive. It does not make that positive form closable automatically. The base-null/form-Cauchy test must still be applied to the shifted kernel

\[
K_F+CG_F.
\]

Thus semiboundedness and closability remain distinct gates.

## Disposition

The finite observer contract for `closable_semibounded_source_form` is now complete:

1. compute generalized lower constants \(C_F\);
2. prove they admit one global bound;
3. apply the null-sequence closability test after shifting;
4. close the form.

The first missing evidence is a source-authorized evaluator or analytic estimate for the completed values \(H(a_i+a_j)-H(a_i+a_j+h)\) strong enough to control \(C_F\) uniformly. Finite samples alone cannot establish the global quantifier.

## Verification

- `research/voevodsky/checkers/check_source_form_semiboundedness_gate.py`
- `research/voevodsky/results/source_form_semiboundedness_gate.json`
