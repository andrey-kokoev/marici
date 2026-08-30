# Finite square boundary-anomaly trace forgets sewing

## Exact collapse

Let (W) be a finite-dimensional square invertible sewing map and define

\[
\mathcal A=Q_-W+WQ_+.
\]

Then

\[
W^{-1}\mathcal A
=
W^{-1}Q_-W+Q_+.
\]

Cyclicity of the finite trace gives

\[
\operatorname{Tr}(W^{-1}\mathcal A)
=
\operatorname{Tr}Q_-+operatorname{Tr}Q_+.
\]

The scalar determinant-line connection is independent of (W).

Therefore no finite square determinant jet of this form can detect the detailed
Fourier–Tate sewing. It sees only the sum of the two frame-generator traces.

## Consequences

If the two finite sector generators have opposite trace, the determinant-line
jet vanishes even when the full operator anomaly is nonzero.

If the full anomaly vanishes,

\[
Q_-W+WQ_+=0,
\]

then the sewing exactly intertwines the two generators with opposite sign. In
that case neither the operator anomaly nor its determinant trace supplies an
orientation current.

If the full anomaly is nonzero but traceless after multiplication by
(W^{-1}), it remains visible only as an operator-valued mixing channel. Scalar
determinant completion erases it.

## Where a scalar anomaly can survive

A sewing-dependent scalar contribution requires failure of at least one
finite-square hypothesis. The admissible possibilities are:

- (W) has kernel or cokernel and acts on a determinant line rather than as an
  invertible matrix;
- (Q_+) or (Q_-) is unbounded and domain transport contributes a boundary
  term;
- the relevant products are not trace class;
- a regularized trace has a nonzero cyclicity defect;
- cutoff completion leaves an endpoint current;
- a relative determinant retains primitive, square, seam, or archimedean
  boundary data.

These are not technical nuisances. They are the only places where the sewing
map can re-enter the scalar determinant connection.

## Archimedean confirmation

For the centered dilation generator

\[
D=x\partial_x+\frac12,
\]

Fourier reversal gives

\[
FD=-DF
\]

on Schwartz space. On a finite interval, Mellin integration produces

\[
\mathcal M(Df;s)
=
[x^sf(x)]_a^b
+
\left(\frac12-s\right)\mathcal M(f;s).
\]

The anomaly is entirely the endpoint evaluation. Ordinary Schwartz completion
kills it. Thus continuous archimedean bulk sewing supplies no residual scalar
orientation.

The surviving finite-Euler audit must retain primitive, prime-square, seam,
and continuation boundary coefficients explicitly.

## Revised determinant-frame residual

The naive scalar candidate

\[
\operatorname{Tr}(W^{-1}\mathcal A)
\]

must be decomposed into:

\[
\operatorname{Tr}Q_-+operatorname{Tr}Q_+
+
\operatorname{Def}_{\mathrm{cyc}}(W,Q_-,Q_+)
+
\operatorname{Ind}_{\partial}(W).
\]

Here the second term denotes an authorized regularized cyclicity defect and the
third denotes kernel, cokernel, domain, or endpoint contributions. In finite
square algebra both vanish.

Only the last two terms can carry sewing-dependent determinant information.
They must be constructed, not inferred from the completed scalar.

## Finite falsifier

For every proposed finite square realization, compute both

\[
\operatorname{Tr}(W^{-1}\mathcal A)
\]

and

\[
\operatorname{Tr}Q_-+operatorname{Tr}Q_+.
\]

Any claimed sewing-dependent scalar residual is false if these are equal, as
ordinary cyclicity requires.

If a nonzero difference is claimed, the proposal must identify the exact
failed hypothesis: noninvertibility, domain boundary, non-trace-class product,
regularized trace defect, or endpoint index. An untyped difference is rejected.

## Decisive boundary

The determinant route no longer seeks orientation in a finite square sewing
trace. The only live scalar mechanism is a source-derived boundary or index
anomaly that survives completion while ordinary continuous bulk cancellation
remains exact.
