# 2096 — Simultaneous Gaussian Zero Modes Force a Labelled Multi-Rees Lens

## Hostile question

Entry 2095 showed that one vanishing symplectic frequency has a canonical
first boundary coefficient after multiplication by the intrinsic normal
\(\lambda=\sqrt{\det h}\).  Test whether a single determinant normal remains
faithful when two labelled frequencies vanish independently.

## Frozen source

In the labelled ordering \((q_1,p_1,q_2,p_2)\), take two uncoupled positive
quadratic blocks

\[
h_i=\operatorname{diag}(\lambda_i^2/\alpha_i,\alpha_i),
\qquad i=1,2.
\]

Their pure source-selected covariance is

\[
V
=
\operatorname{diag}
\left(
\frac{\alpha_1}{2\lambda_1},
\frac{\lambda_1}{2\alpha_1},
\frac{\alpha_2}{2\lambda_2},
\frac{\lambda_2}{2\alpha_2}
\right).
\]

The scalar determinant normal of the complete source is

\[
\sqrt{\det h}=\lambda_1\lambda_2.
\]

## Scalar-normal failure

Multiplication by the total normal gives

\[
(\lambda_1\lambda_2)V
=
\operatorname{diag}
\left(
\frac{\alpha_1\lambda_2}{2},
\frac{\lambda_1^2\lambda_2}{2\alpha_1},
\frac{\alpha_2\lambda_1}{2},
\frac{\lambda_1\lambda_2^2}{2\alpha_2}
\right).
\]

At the simultaneous corner \((\lambda_1,\lambda_2)=(0,0)\), this grade is
zero.  It erases both nonzero rank-one boundary coefficients.  Recovering
either coefficient by division then depends on a chosen approach ratio
\(\lambda_1/\lambda_2\).

Therefore

\[
\boxed{
\sqrt{\det h}\text{ is an intrinsic scalar, but it is not a faithful
normal coordinate at the codimension-two zero-mode corner.}
}
\]

## Occurrence-resolved grades

Retain the two labelled normals separately.  Then

\[
\lim_{\lambda_1\to0}\lambda_1V_1
=
\begin{pmatrix}\alpha_1/2&0\\0&0\end{pmatrix},
\qquad
\lim_{\lambda_2\to0}\lambda_2V_2
=
\begin{pmatrix}\alpha_2/2&0\\0&0\end{pmatrix}.
\]

These coefficients survive independently of the relative rate at which the
two frequencies vanish.

## Narrow result

\[
\boxed{
\text{simultaneous labelled zero modes force a multi-Rees coefficient
object over the existing support intersection.}
}
\]

The new necessity is not another Carrier cell.  The Carrier already knows the
two labelled zero-frequency occurrences and their intersection.  What fails
is the unlabelled scalar projection of their normal cone.

This is a direct finite model of the broader Marici rule:

\[
\text{coarse invariant normal}
\not\Rightarrow
\text{faithful resolved normal geometry}.
\]

## Next falsifier

Turn on a source-derived coupling between the two modes.  Test whether the
labelled normal pair transforms covariantly under symplectic mixing and
whether its multi-Rees boundary coefficients glue without selecting a
preferred normal frame.  Failure of gluing would expose missing coefficient
descent data; it would justify new Carrier structure only if the frozen
zero-mode incidence itself failed to carry the transition.

## Durable evidence

- `research/benincasa/checkers/two_mode_gaussian_multi_rees_lens.py`
- `research/benincasa/checkers/results/two-mode-gaussian-multi-rees-lens.json`
- Ledger allocation: `seqclaim-865d11eee884be6b927e9494`

