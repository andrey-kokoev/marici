# 2094 — A Gaussian Zero Mode Selects Only a Projective Boundary Lens

## Frozen test

For one canonical mode use

\[
\Omega=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad
h_0=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
\]

Ask whether the source-selection rule of Entry 2091 still determines a finite
positive pure stationary covariance when the quadratic source acquires a zero
frequency.  No new Carrier incidence or fitted infrared normalization is
admitted.

## Exact obstruction

Write

\[
V=\begin{pmatrix}x&z\\z&y\end{pmatrix},
\qquad A_0=\Omega h_0.
\]

The stationarity equation

\[
A_0V+VA_0^T=0
\]

has components

\[
\begin{pmatrix}2z&y\\y&0\end{pmatrix}=0.
\]

Hence \(z=y=0\), so \(\det V=0\).  This is incompatible with the
one-mode purity condition

\[
\det V=\frac14.
\]

Therefore the semidefinite source selects no finite positive pure stationary
covariance.

## Regulated family

Use the declared positive regulator

\[
h_{\epsilon,c}=\operatorname{diag}((c\epsilon)^2,1),
\qquad c>0,
\]

without identifying different values of \(c\).  Entry 2091's source rule gives

\[
V_{\epsilon,c}
=
\begin{pmatrix}
\dfrac1{2c\epsilon}&0\\[2mm]
0&\dfrac{c\epsilon}{2}
\end{pmatrix},
\qquad
\det V_{\epsilon,c}=\frac14.
\]

As \(\epsilon\to0^+\), every fixed \(c\) approaches the same projective
boundary ray

\[
[V_{qq}:V_{pp}]=[1:0],
\]

but the affine normalization depends on \(c\).  The source at zero frequency
therefore determines an infinite-squeezing direction, not a normalized finite
state.

## Narrow result

\[
\boxed{
\text{Positive quadratic source selects a unique interior Gaussian lens,}
\quad
\text{whereas a zero mode selects only its projective boundary direction.}
}
\]

The zero-mode failure is supported on the already existing zero-frequency/soft
locus.  It requires a boundary coefficient/readout object and independent
infrared source data for affine normalization.  It does not justify a new
Carrier stratum.

This sharpens the source-indexed interface architecture:

\[
\text{Carrier}
+\text{positive source}
\longrightarrow
\text{unique interior lens},
\]

while

\[
\text{Carrier}
+\text{degenerate source}
\longrightarrow
\text{projective boundary lens}
+\text{normalization obligation}.
\]

## Next falsifier

Freeze one physical infrared prescription—finite volume, positive mass, or an
independently derived cosmological boundary condition—and test whether its
zero-mode limit canonically fixes the affine normalization.  If two admissible
source-derived prescriptions reach the same projective ray with inequivalent
normalizations, only the projective boundary object is intrinsic.

## Durable evidence

- `research/benincasa/checkers/zero_mode_gaussian_source_lens.py`
- `research/benincasa/checkers/results/zero-mode-gaussian-source-lens.json`
- Ledger allocation: `seqclaim-8d8f298ff9b327435082cd4c`

