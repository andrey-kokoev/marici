# Uniform Consumer Compilation Needs a Bounded Decoder

Let (R_N) be the selected observation ports and (L_N) the declared
consumer at cutoff (N). Exact factorization is governed by

\[
\ker R_N\subseteq\ker L_N.
\]

Completion-stable factorization requires more: there must be one constant
(C), independent of cutoff, such that

\[
L_N^*L_N\le C^2R_N^*R_N.
\]

Equivalently,

\[
\|L_Nv\|\le C\|R_Nv\|
\]

for every admitted state. When the kernel condition holds, the sharp squared
constant is

\[
C_N^2=
\lambda_{\max}
\left(
(R_N^*R_N)^{\dagger/2}
L_N^*L_N
(R_N^*R_N)^{\dagger/2}
\right)
\]

on the supported quotient. Uniform compilation is exactly

\[
\sup_N C_N<\infty.
\]

## Exact pointwise-but-nonuniform family

Let

\[
R_N=
\begin{pmatrix}
1&0\\
1&1/N
\end{pmatrix},
\qquad
L_N=I_2.
\]

Every (R_N) is invertible, so the consumer is reconstructed exactly at
every finite cutoff. But

\[
Q_N=R_N^*R_N
=
\begin{pmatrix}
2&1/N\\
1/N&1/N^2
\end{pmatrix}.
\]

Its smaller eigenvalue satisfies

\[
N^2\lambda_{\min}(Q_N)\longrightarrow\frac12.
\]

Hence the sharp squared decoder cost grows as

\[
C_N^2\sim2N^2.
\]

The state (v=(0,1)^T) is the approximate hidden direction:

\[
\|L_Nv\|=1,
\qquad
\|R_Nv\|=1/N.
\]

Finite injectivity has not survived metrically.

## Minimal seam augmentation

Adjoin the independent row

\[
s=(0,1).
\]

The augmented observation Gramian is

\[
Q_N^{\mathrm{full}}
=
R_N^*R_N+s^*s
=
\begin{pmatrix}
2&1/N\\
1/N&1+1/N^2
\end{pmatrix}.
\]

For every (N\ge1),

\[
Q_N^{\mathrm{full}}-\frac12I>0,
\]

because its leading minor is (3/2) and its determinant is

\[
\frac34+\frac{1}{2N^2}>0.
\]

Therefore

\[
Q_N^{\mathrm{full}}\ge\frac12I,
\qquad
C_N^{\mathrm{full}}\le\sqrt2.
\]

One transverse row repairs the approximate kernel uniformly. It is minimal in
rank because the collapsing family has one asymptotically hidden direction.

## Compiler verdicts

The finite compiler must return one of three distinct statuses:

- kernel failure: some consumer direction is exactly invisible;
- pointwise factorization without uniform stability: every cutoff decodes,
  but (C_N\to\infty);
- uniform factorization: one fixed authorized port family has bounded
  domination constants.

An additional row suggested by the singular vector is only an algebraic
repair signature. Source authority must independently provide that row. If it
is a seam current, the source must prove its typing and continuity.

## Falsifiers

- Equating invertibility at every cutoff with a continuous completed inverse.
- Reporting only rank while omitting the smallest singular value.
- Allowing the repair row to depend on (N) without a fixed constructor.
- Adding the approximate singular vector as a port without source authority.
- Proving a lower bound in a cutoff-dependent norm.
- Calling a bounded decoder a proof of physical actuator accessibility.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to price the gap between exact consumer factorization and
completion-stable compilation.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. A two-row finite family gives exact decoding with quadratic cost
escape, while one authorized transverse row restores a uniform bound.
