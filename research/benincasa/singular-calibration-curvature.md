# Singular calibration curvature

Let

\[
F_\varepsilon=\operatorname{diag}(1,\varepsilon),
\qquad
A_\varepsilon=F_\varepsilon^{-1}AF_\varepsilon.
\]

Then

\[
A_\varepsilon=
\begin{pmatrix}
a_{11}&\varepsilon a_{12}\\
\varepsilon^{-1}a_{21}&a_{22}
\end{pmatrix}.
\]

For a regular calibration \(B\), the mixed curvature acting on \(H\) is

\[
K_\varepsilon=[[A_\varepsilon,B],H].
\]

The forced parabolic factor \(\varepsilon\) makes it regular. Its supported
residue is

\[
\left.\varepsilon K_\varepsilon\right|_{\varepsilon=0}
=
\left[
\left[
\begin{pmatrix}0&0\\a_{21}&0\end{pmatrix},
B\right],H\right].
\]

This residue can be nonzero. It is the negative-grade coefficient curvature
retained by the source frame valuation, not a new carrier incidence.
