# Completed-heat difference defines the joint Gaussian source form

## Question

Does the source-normalized completed heat kernel already define one quadratic form on every complex linear combination of Gaussian observers?

## Claim boundary

Yes algebraically. For fixed positive mesh \(h\), raw completed-heat differences define a Hermitian kernel on the Gaussian span and therefore one jointly regularized quadratic form. The raw form retains the endpoint rank-one term and is nonclosable in the order norm; the endpoint-corrected remainder kernel is the candidate for the common form. This constructs the primitive source quadratic map but does not prove closability of the corrected form, semiboundedness, or RH.

## Heat-coordinate convention

Use inverse-width coordinate \(a>0\) and the Gaussian label function

\[
F_a(\lambda)=e^{-a\lambda^2}.
\]

This is related to the width convention by

\[
a=\frac1{4\tau}.
\]

Products close under addition:

\[
F_a(\lambda)F_b(\lambda)
=
F_{a+b}(\lambda).
\]

The one-step difference factor is

\[
F_a(\lambda)F_b(\lambda)
(1-e^{-h\lambda^2})
=
F_{a+b}(\lambda)-F_{a+b+h}(\lambda).
\]

## Source kernel

Let \(H\) be the source-normalized completed heat kernel. Define

\[
K_h(a,b)
=
H(a+b)-H(a+b+h).
\]

For

\[
f=\sum_{j=1}^m c_jg_{a_j},
\]

define

\[
q_h(f)
=
\sum_{i,j=1}^m
\overline{c_i}c_jK_h(a_i,a_j).
\]

This uses one value of the already completed source kernel for each sum parameter. It does not split gamma and prime into separately divergent multiplier limits.

## Well-definedness on the algebraic span

Distinct Gaussian functions \(e^{-a_j\lambda^2}\) are linearly independent on an unbounded set of distinct labels. Indeed, order the \(a_j\); multiplying a vanishing combination by the slowest-decaying exponential and sending \(\lambda^2\) onward eliminates coefficients successively.

Therefore a finite Gaussian-span vector has a unique coefficient presentation. The formula for \(q_h\) is well defined.

Since \(H\) is real on positive arguments,

\[
K_h(a,b)
=
\overline{K_h(b,a)}.
\]

Hence \(q_h\) obeys homogeneity and the parallelogram identity. Its polarization is exactly \(K_h\).

## What has been constructed

The primitive

`jointly_regularized_source_quadratic_form_on_gaussian_span`

is inhabited by \(q_h\). Its regularization is joint because the completed \(H\) is evaluated only after gamma, prime, and endpoint normalization have been combined at source level.

This avoids the nonuniform prime-multiplier cutoff and its low-frequency divergence. It makes no claim that the resulting form is positive.

## Remaining residual

The first remaining gate is closability relative to the order Hilbert norm. One must exclude sequences \(f_n\) in the Gaussian span such that

\[
\lVert f_n\rVert_{\rm ord}
\longrightarrow0,
\qquad
q_h(f_n-f_m)
\longrightarrow0,
\]

but

\[
q_h(f_n)
\not\longrightarrow0.
\]

If the form is closable, semiboundedness is the next independent requirement. Positivity of all finite matrices \([K_h(a_i,a_j)]\) would imply semiboundedness with bound zero, but that is the RH-strength target rather than an input.

## Disposition

The source-quadratic-form blocker passes algebraically. `closable_semibounded_source_form` is now the first missing object. No source--Weil comparison or RH implication is asserted.

## Verification

- `research/voevodsky/checkers/check_completed_heat_gaussian_source_form.py`
- `research/voevodsky/results/completed_heat_gaussian_source_form.json`
