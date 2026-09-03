# Mellin-exponential Riesz family is total in the order completion

## Question

Do the bounded exponential evaluations in the logarithmic label jointly observe every vector in the source-derived order completion?

## Claim boundary

Yes. Their Riesz vectors have dense linear span in the Hilbert norm of the order completion. These are Mellin-semigroup probes \(e^{-t\lambda}\), not the completed-heat Gaussian probes \(e^{-\lambda^2/(4t)}\). This proves ordinary-norm density for the Mellin family, not graph-norm density for the missing completed gamma-plus-prime form.

## Laplace representation

Under the cumulative-sum isometry, a finite zero-sum packet \(c\) becomes

\[
g(u)=Jc(u)
=
\sqrt2
\sum_{\lambda_i>u}c_i.
\]

For

\[
L_t(c)
=
\sum_i c_i e^{-t\lambda_i},
\]

summation by parts gives

\[
L_t(c)
=
\frac{t}{\sqrt2}
\int_{\lambda_0}^{\infty}
g(u)e^{-tu}du.
\]

Both sides extend continuously to the order completion because \(e^{-tu}\) belongs to \(L^2\) for every \(t>0\).

## Totality

Suppose \(g\) is orthogonal to every Mellin-exponential Riesz vector. Then

\[
\int_{\lambda_0}^{\infty}
g(u)e^{-tu}du
=0
\]

for every \(t>0\). Uniqueness of the Laplace transform for locally integrable functions of exponential order implies

\[
g=0
\]

almost everywhere. Since \(g\) lies in the cumulative-sum realization of the order completion, the original vector is zero.

Therefore

\[
\overline{
\operatorname{span}
\{r_t:t>0\}
}^{\lVert\cdot\rVert_{\rm ord}}
=
\mathcal H_{\rm ord},
\]

where \(r_t\) is the Riesz vector representing \(L_t\).

## Finite-cutoff form

On adjacent-gap coordinates, the evaluation row is

\[
\left(
e^{-t\lambda_i}-e^{-t\lambda_{i+1}}
\right)_i.
\]

For a finite set of distinct labels, sufficiently many distinct positive heat parameters give full column rank. The checker verifies this on an exact symbolic fixture.

## Consequences

The order completion now has a jointly faithful heat observer family. Any bounded operator on \(\mathcal H_{\rm ord}\) is determined by its matrix elements on the span of these Riesz vectors.

This removes Hilbert-norm density from the blocker. It does not remove the decisive graph-domain problem: if the completed form is represented by an unbounded operator \(A\), one must prove that the heat-Riesz span is dense for

\[
\lVert f\rVert_A^2
=
\lVert f\rVert_{\rm ord}^2
+
\lVert Af\rVert_{\rm ord}^2
\]

or the corresponding closed-form norm.

Ordinary density does not imply graph density.

## Residual

The remaining sequence is now:

1. construct the source-regularized joint gamma-plus-prime form on the heat-Riesz span;
2. prove closability;
3. identify its closed domain;
4. prove the heat-Riesz span is a form core;
5. compare the closed form with the zero-side form.

Failure at step 2 would show that the dense observer family has incompatible limiting form values rather than inadequate observational resolution.

## Disposition

`heat_observer_hilbert_density` passes on the order completion. `gaussian_jet_form_core` remains open because no completed form operator or graph norm has yet been constructed.

## Verification

- `research/voevodsky/checkers/check_heat_riesz_totality.py`
- `research/voevodsky/results/heat_riesz_totality.json`
