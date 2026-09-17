# A finite dangerous-eigenspace residual replaces the full cross norm

Let `P` be the rank-1000 Legendre projection and suppose the infinite tail
satisfies `QAQ >= delta Q`. Diagonalize the certified finite block `PAP` and
split its range into a dangerous eigenspace `D` and a safe eigenspace `S`.
For a normalized finite eigenvector `v` with eigenvalue `lambda`, completing
the square against the tail gives the sufficient bound

\[
\lambda-\frac{\|QAv\|^2}{\delta}>0.
\]

For a multidimensional dangerous space, replace the scalar residual by the
small matrix `R_D^*(QAQ)^{-1}R_D`, bounded above by `R_D^*R_D/delta`. The safe
space can use its much larger spectral gap and a coarser residual estimate.

At `L=0.55`, the concentration-sharpened Legendre estimate gives, above degree
999,

\[
\delta_{1000}=
\frac12\log\left(1+\frac{\sqrt{1000\cdot1001}}{0.55}\right)
-3.5526025323746278.
\]

Thus the first finite eigenvalue only requires residual norm below
`sqrt(lambda_1 delta_1000)`, while the second permits the much larger
`sqrt(lambda_2 delta_1000)`. This is the correct quantitative target because
the full cross norm is dominated by harmless high finite directions.
