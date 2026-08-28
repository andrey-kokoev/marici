# Local det3 control does not globalize without cross-prime overlap decay

## Local regularity is insufficient

Let \(T_p\) be the relative-transfer factor for a prime block. The
third-Schatten condition

\[
\sum_p\lVert T_p\rVert_3^3<\infty
\]

controls the direct-sum third regularized determinant.

Ordered products also produce pairwise coherence cells

\[
\alpha_3(T_p,T_q).
\]

Their absolute summability depends on mixed products such as

\[
\operatorname{Tr}(T_p^2T_q),
\qquad
\operatorname{Tr}(T_pT_q^2),
\qquad
\operatorname{Tr}((T_pT_q)^2).
\]

Individual Schatten norms do not determine these overlaps.

## Exact aligned hostile

Let \(P\) be one rank-one projection and put

\[
T_n=\frac1nP.
\]

The local third-Schatten budget converges:

\[
\sum_n\lVert T_n\rVert_3^3
=
\sum_n\frac1{n^3}<\infty.
\]

All factors occupy the same boundary direction. Their pair anomaly is

\[
\alpha_3(T_m,T_n)
=
-\frac1{m^2n}
-\frac1{mn^2}
+\frac1{2m^2n^2}.
\]

The absolute double sum diverges because it contains the harmonic cross term

\[
\sum_{m<n}\frac1{m^2n}.
\]

Thus every local regularized determinant can exist while the global route
coherencer fails to be summable.

## Orthogonal comparison

Now place the same singular values on mutually orthogonal rank-one
projections:

\[
T_n=\frac1nP_n,
\qquad
P_mP_n=0
\]

for \(m\neq n\). Every cross anomaly vanishes.

The aligned and orthogonal families have identical local operator-ideal data.
Only their cross-block incidence differs. Globalization therefore requires a
source-derived overlap law.

## Exact gate

A sufficient absolute coherence condition is

\[
\sum_{p<q}
\left(
|\operatorname{Tr}(T_p^2T_q)|
+|\operatorname{Tr}(T_pT_q^2)|
+\frac12|\operatorname{Tr}((T_pT_q)^2)|
\right)
<\infty.
\]

The theta–Euler programme must compute these terms from the common seam-shell
incidence. Treating prime blocks as orthogonal by declaration would erase the
shared source geometry.

The relevant source object is a cross-prime overlap kernel, not another
one-prime norm:

\[
\mathcal K(p,q)
=
\bigl(
\operatorname{Tr}(T_p^2T_q),
\operatorname{Tr}(T_pT_q^2),
\operatorname{Tr}((T_pT_q)^2)
\bigr).
\]

## DPC verdict

Resolved:

- local third-Schatten control does not imply global anomaly summability;
- overlap geometry is independent of local singular-value data;
- an exact cross-prime summability gate;
- aligned and orthogonal finite falsifiers.

Withheld:

- the actual theta cross-prime kernel;
- its decay in \(|\log p-\log q|\);
- restricted-product convergence of the coherence cells;
- archimedean and zero-state bridges.

The next source calculation is the overlap of two labelled seam-shell
realizations before scalar aggregation.

## Verification

The checker `check_cross_prime_anomaly_summability.py` verifies finite local
third-grade budgets, growing aligned anomaly sums, and identically zero
orthogonal cross anomalies.
