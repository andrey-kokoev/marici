# Polarized kernel is derived, not independent source data

## Question

Must the unequal-parameter kernel \(K(\tau,\sigma)\) be supplied independently, or is it determined by a source quadratic form on the Gaussian span?

## Claim boundary

It is determined uniquely by complex Hermitian polarization, provided one jointly regularized quadratic form is defined on every complex linear combination of Gaussian Riesz vectors. Separate diagonal regularizations do not suffice. Closability and semiboundedness remain open.

## Polarization

Let \(q\) be a real-valued quadratic form on the complex Gaussian span, induced by a Hermitian form \(B\) that is conjugate-linear in its first variable. Then

\[
B(x,y)
=
\frac14
\sum_{k=0}^{3}
(-i)^k
q(x+i^k y).
\]

Therefore

\[
K(\tau,\sigma)
=
\frac14
\sum_{k=0}^{3}
(-i)^k
q(g_\tau+i^k g_\sigma).
\]

No additional kernel choices remain once \(q\) is defined on the linear span.

## Regularization coherence

The formula is meaningful only if the four quadratic values use the same source regularization. If each diagonal expression is assigned a different cutoff, subtraction, or limiting path, polarization can produce a kernel that depends on the presentation of the same vector.

Thus the source datum is not a table of values \(q(g_\tau)\). It is one quadratic map

\[
q:
\operatorname{span}_{\mathbb C}
\{g_\tau:\tau>0\}
\longrightarrow
\mathbb R
\]

satisfying the quadratic identities

\[
q(\alpha x)=|\alpha|^2q(x)
\]

and

\[
q(x+y)+q(x-y)
=
2q(x)+2q(y).
\]

These identities are falsifiers for incompatible regularizations.

## Dependency reduction

The previous object `polarized_joint_source_kernel` should be replaced by the weaker primitive object

`jointly_regularized_source_quadratic_form_on_gaussian_span`.

Once that object exists, polarization constructs \(K\) functorially. The remaining form-lift tests are:

1. Hermitian consistency under polarization;
2. closability relative to the order norm;
3. semiboundedness;
4. comparison of the closure with the Weil form.

## Residual

If two decompositions of one Gaussian-span vector give different regularized values, the parallelogram defect

\[
R_q(x,y)
=
q(x+y)+q(x-y)-2q(x)-2q(y)
\]

is the first residual. A nonzero value means no Hermitian kernel exists, so closability is not yet the relevant question.

## Disposition

The missing source data have been reduced from a two-parameter polarized kernel to one jointly regularized quadratic form on the complex Gaussian span. Polarization is constructed and checked; source existence of that quadratic form is still missing.

## Verification

- `research/voevodsky/checkers/check_source_form_polarization.py`
- `research/voevodsky/results/source_form_polarization.json`
