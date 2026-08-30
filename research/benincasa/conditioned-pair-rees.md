# Conditional mixed-pair observable on the Gaussian Rees boundary

For centered jointly Gaussian `X,Y,R`, write

\[
b=\operatorname{Var}(R),
\qquad
c_X=\operatorname{Cov}(X,R),
\qquad
c_Y=\operatorname{Cov}(Y,R).
\]

At `b>0`, Gaussian conditioning gives

\[
\mathbb E[XY\mid R=r]
=A_{XY}+\frac{c_Xc_Y}{b}
\left(\frac{r^2}{b}-1\right).
\]

Use the weighted exceptional coordinates

\[
r=\sqrt b\,s,
\qquad
\xi=\frac{c_Xc_Y}{b}.
\]

Then

\[
\mathbb E[XY\mid s]=A_{XY}+\xi(s^2-1).
\]

The Gaussian average over `s` returns `A_XY`, but pointwise conditional
specialization retains `xi`.  Thus forgetting support erases a genuine
exceptional coefficient even though the unconditional pair observable is
polynomial and regular.
