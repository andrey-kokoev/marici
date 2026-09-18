# Correction: the actual prime-cell comparison has no free even alpha

## Error corrected

The abstract two-output notation

\[
T_p=\operatorname{diag}(\alpha_p,\lambda_p)
\]

was reused in the recent Green-mate audit as though \(\alpha_p\) remained missing. Later source state explicitly supersedes that interpretation.

The completed theta columns are fixed:

\[
Q_p^{\rm lin}e_1=w_\theta=\binom{1/2}{1/2},
\qquad
Q_p^{\rm lin}e_2=j_\theta=\binom{1/4}{-1/4}.
\]

Therefore

\[
Q_p^{\rm lin}
=
\begin{pmatrix}1/2&1/4\\1/2&-1/4\end{pmatrix}
\]

is uniquely determined and invertible. There is no adjustable even scalar.

## Correct residual

The local theorem is parameter-free:

\[
\Delta_p
=G_p^{\rm St}-(Q_p^{\rm lin})^*H_p^\theta Q_p^{\rm lin}.
\]

With the correct antiunitary variance and common quarter-turn covariance, this residual reduces to

\[
\Delta_p
=a_p\begin{pmatrix}1&0\\0&1/4\end{pmatrix}
+b_p\begin{pmatrix}0&i\\-i&0\end{pmatrix}.
\]

The two tests are:

\[
a_p=(\Delta_p)_{11}=0,
\qquad
b_p=-i(\Delta_p)_{12}=0.
\]

These are measured residual coordinates, not normalization parameters available for fitting.

## Status of the inputs

The repository contains:

- explicit Stieltjes window formulas and typed attachments;
- the fixed linear map \(Q_p^{\rm lin}\);
- a complete analytic theta candidate, including the bounded skew linking block;
- a candidate common source plane.

What remains absent is an authoritative frozen packet exposing the complete two matrices on that common plane, with all attachments and variance conventions, so that \(a_p\) and \(b_p\) can be evaluated independently.

## Revised next action

Do not search for or choose \(\alpha_p\). Instead:

1. freeze the independently constructed \(G_p^{\rm St}\) and \(H_p^\theta\) matrices in the source basis \((e_1,e_2)\);
2. verify their common form domain and the antiunitary reflection convention;
3. compute \(\Delta_p\);
4. report the two parameter-free coordinates \((a_p,b_p)\).

Any choice of a scale made after inspecting \(\Delta_p\) would alter the source problem.

## Claim boundary

This removes a fictitious degree of freedom. It does not establish that either residual coordinate vanishes.
