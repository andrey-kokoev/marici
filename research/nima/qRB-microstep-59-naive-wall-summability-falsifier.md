# qRB microstep 59: naive wall summability fails

Under the theta scaling law

$$
\phi_n(u)=n^{-1/2}\phi_1(u+\log n),
$$

any translation-invariant wall norm gives

$$
\|\phi_n\|_{\rm wall}
=n^{-1/2}\|\phi_1\|_{\rm wall}.
$$

The sufficient absolute-summability test would then require

$$
\sum_{n\ge2}n^{-1/2}<\infty,
$$

which is false.

Therefore absolute summability of individual theta-cell wall norms is too strong and cannot be the mechanism for wall convergence. The correct route must use label-coupled cancellation, a stronger label weight, or a relative quotient that removes the common translated mode before taking the norm.

Status: naive wall-norm summability rejected; coupled relative assembly is confirmed as necessary.
