# Smooth logarithmic IMS estimate from the digamma Lévy representation

Put

\[
q(u)=\frac12\left(\Re\psi\left(\frac14+\frac{iu}{2}\right)-\log\pi\right),
\qquad q_0=q(0).
\]

The digamma integral gives the exact representation

\[
q(u)=q_0+\frac12\int_0^\infty
 \frac{e^{-t/4}}{1-e^{-t}}
 \left(1-\cos\frac{ut}{2}\right)dt.
\]

Consequently, with `T_h f(x)=f(x-h)`, Plancherel gives

\[
\langle f,q(D)f\rangle
=q_0\|f\|^2+\frac14\int_0^\infty w(t)
 \|f-T_{t/2}f\|^2dt,
\quad w(t)=\frac{e^{-t/4}}{1-e^{-t}}.
\]

Let `chi_j` be a finite real nonnegative smooth partition with
`sum_j chi_j^2=1`, and set

\[
K=\sum_j\|\chi_j'\|_\infty^2.
\]

Expanding the translated differences shows

\[
\sum_j\|\chi_jf-T_h(\chi_jf)\|^2-
\|f-T_hf\|^2
=
\Re\int\overline{f(x)}f(x-h)
 \sum_j(\chi_j(x)-\chi_j(x-h))^2dx.
\]

Since

\[
\sum_j(\chi_j(x)-\chi_j(x-h))^2
\le \min(4,K h^2),
\]

Cauchy--Schwarz and translation invariance imply the two-sided IMS estimate

\[
\left|\sum_j\langle\chi_jf,q(D)\chi_jf\rangle
-\langle f,q(D)f\rangle\right|
\le C_{\rm IMS}(K)\|f\|^2,
\]

where

\[
C_{\rm IMS}(K)=\frac14\int_0^\infty
 \frac{e^{-t/4}}{1-e^{-t}}
 \min\left(4,\frac{Kt^2}{4}\right)dt<\infty.
\]


This proves the required smooth logarithmic IMS estimate with an explicit
one-dimensional constant. It also identifies the next optimization problem:
choose the edge transition profile and width so that its logarithmic
coercivity exceeds `C_IMS(K)` together with arithmetic cross terms.
