# Oscillatory gamma-tail moments admit directed integration-by-parts recurrences

Set `omega=2L` and, for `k>=2`,

\[
C_k(R)=\int_R^\infty u^{-k}\cos(\omega u)du,
\qquad
S_k(R)=\int_R^\infty u^{-k}\sin(\omega u)du.
\]

Integration by parts gives

\[
C_k=-\frac{R^{-k}\sin(\omega R)}\omega+rac{k}{\omega}S_{k+1},
\]

\[
S_k=\frac{R^{-k}\cos(\omega R)}\omega-rac{k}{\omega}C_{k+1}.
\]

For the logarithmic leading term, define

\[
C_k^{\log}=\int_R^\infty\log\frac{u}{2\pi}
 u^{-k}\cos(\omega u)du,
\]

and similarly `S_k^log`. Then

\[
C_k^{\log}
=-\frac{R^{-k}\log(R/(2\pi))\sin(\omega R)}\omega
+\frac{k}{\omega}S_{k+1}^{\log}
-\frac1\omega S_{k+1},
\]

\[
S_k^{\log}
=\frac{R^{-k}\log(R/(2\pi))\cos(\omega R)}\omega
-\frac{k}{\omega}C_{k+1}^{\log}
+\frac1\omega C_{k+1}.
\]

After `d` recurrence steps, the residual is bounded directly by

\[
|C_m|,|S_m|\le\frac{R^{1-m}}{m-1},
\]

\[
|C_m^{\log}|,|S_m^{\log}|
\le R^{1-m}
\left(
\frac{\log(R/(2\pi))}{m-1}+rac1{(m-1)^2}
\right)
\]

when `R>=2*pi`. Every correction term `c_j u^{-j}` from the digamma expansion
uses the plain recurrence at index `k+j`.

These equations enclose all 317 oscillatory moments in the order-79 tail
manifest using endpoint sine/cosine balls plus explicit residual radii.
