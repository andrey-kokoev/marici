# 2095 — The Source Normal Canonically Renormalizes the Gaussian Zero-Mode Lens

## Question

Entry 2094 found that a Gaussian zero mode selects only an
infinite-squeezing boundary ray and that its raw affine covariance depends on
the regulator coordinate.  Test whether this ambiguity survives when the
normal parameter is derived from the quadratic source itself.

## Frozen family

Let

\[
h_{\lambda,\alpha}
=
\begin{pmatrix}
\lambda^2/\alpha&0\\
0&\alpha
\end{pmatrix},
\qquad
\lambda=\sqrt{\det h}>0,
\qquad
\alpha>0.
\]

The positive-source rule of Entry 2091 gives

\[
V_{\lambda,\alpha}
=
\frac{\sqrt{\det h}}2h^{-1}
=
\begin{pmatrix}
\alpha/(2\lambda)&0\\
0&\lambda/(2\alpha)
\end{pmatrix}.
\]

The covariance diverges as \(\lambda\to0\), while remaining pure:

\[
\det V_{\lambda,\alpha}=\frac14.
\]

## Source-normalized grade

Multiply by the intrinsic source normal rather than an external regulator
coordinate:

\[
\lambda V_{\lambda,\alpha}
=
\begin{pmatrix}
\alpha/2&0\\
0&\lambda^2/(2\alpha)
\end{pmatrix}.
\]

Therefore

\[
\boxed{
\operatorname{gr}^{(1)}_{\lambda}V
=
\lim_{\lambda\to0}\lambda V
=
\begin{pmatrix}\alpha_0/2&0\\0&0\end{pmatrix}.
}
\]

This limit is unchanged by a reparameterization
\(\epsilon\mapsto c\epsilon\), because
\(\lambda=\sqrt{\det h}\) transforms with the source itself.  The surviving
factor \(\alpha_0\) is not regulator freedom: it is the nonzero quadratic
source stiffness at the boundary.

## Narrow result

Entry 2094's affine ambiguity belongs to the unnormalized divergent
representative.  The first Rees grade defined by the source normal is
canonical relative to the surviving source form:

\[
\boxed{
\text{zero-mode boundary lens}
=
\operatorname{gr}^{(1)}_{\sqrt{\det h}}V.
}
\]

Thus the correct architecture is sharper than a merely projective boundary:

\[
\text{existing zero-frequency support}
+\text{source-normal Rees filtration}
\longrightarrow
\text{canonical boundary coefficient}.
\]

No new Carrier incidence and no independent infrared normalization primitive
are required in this one-mode test.

## Limitation and next falsifier

This uses a simple corank-one quadratic source with a nonzero complementary
stiffness.  At higher corank, \(\sqrt{\det h}\) vanishes at higher order and
need not distinguish labelled soft directions.  The next hostile test is a
two-mode source with two independently vanishing symplectic frequencies.  It
must retain the labelled normal cone and test whether one scalar determinant
normal suffices or a multi-Rees coefficient object is forced.

## Durable evidence

- `research/benincasa/checkers/zero_mode_gaussian_rees_lens.py`
- `research/benincasa/checkers/results/zero-mode-gaussian-rees-lens.json`
- Ledger allocation: `seqclaim-028623999343d28fd62fe54f`

