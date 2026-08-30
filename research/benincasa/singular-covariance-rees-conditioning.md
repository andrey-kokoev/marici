# Singular Gaussian conditioning requires a covariance-Rees direction

Consider

\[
\Sigma(t)=
\begin{pmatrix}
a&t\gamma\\
t\gamma&t^2\beta
\end{pmatrix},
\qquad \beta>0.
\]

For (t\ne0), conditioning the first variable on the second gives

\[
\Sigma_{A\mid B}=a-\frac{\gamma^2}{\beta}.
\]

All such families specialize to the same ordinary covariance

\[
\begin{pmatrix}a&0\\0&0\end{pmatrix},
\]

but retain different finite values of

\[
\lambda=\frac{c^2}{b}=\frac{\gamma^2}{\beta}.
\]

Positivity imposes (0\le\lambda\le a); it does not choose one value. If the
cross covariance decays faster, (c=t^2\gamma), then (lambda\to0).

Thus ordinary pullback to the singular covariance stratum loses the conditional
limit. The appropriate object is a weighted/Rees coefficient boundary carrying
(c^2/b). This refines the covariance coefficient space and does not by itself
add a Cut incidence to the common carrier.

