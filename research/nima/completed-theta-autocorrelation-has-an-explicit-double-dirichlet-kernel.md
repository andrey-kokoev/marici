# Completed theta autocorrelation has an explicit double Dirichlet kernel

Use the completed theta forcing

$$
\Phi(u)=\sum_{n\ge1}
\left(
4\pi^2n^4e^{9u/2}
-6\pi n^2e^{5u/2}
\right)e^{-\pi n^2e^{2u}}.
$$

For the whole-line autocorrelation

$$
A_\Phi(t)=\int_{\mathbb R}\Phi(u)\Phi(u+t)\,du,
$$

set

$$
D_{n,m}(t)=n^2+m^2e^{2t}.
$$

At a finite theta-label cutoff, termwise integration is valid. The unrestricted interchange is not absolutely convergent and is retracted by `correction-the-theta-autocorrelation-double-series-is-only-a-finite-cutoff-identity.md`. With `y=e^(2u)` and `du=dy/(2y)`, the elementary gamma integral gives

$$
\begin{aligned}
A_\Phi(t)
=\sum_{n,m\ge1}\Bigg[&
8\pi^4n^4m^4e^{9t/2}
\frac{\Gamma(9/2)}{\bigl(\pi D_{n,m}(t)\bigr)^{9/2}}\\
&-12\pi^3
\left(n^4m^2e^{5t/2}+n^2m^4e^{9t/2}\right)
\frac{\Gamma(7/2)}{\bigl(\pi D_{n,m}(t)\bigr)^{7/2}}\\
&+18\pi^2n^2m^2e^{5t/2}
\frac{\Gamma(5/2)}{\bigl(\pi D_{n,m}(t)\bigr)^{5/2}}
\Bigg].
\end{aligned}
$$

This is an explicit finite-cutoff source-labelled two-index kernel before prime factorization. Substitution into

$$
\langle\Phi,G_z\rangle=-\int_0^\infty e^{-zt}A_\Phi(t)\,dt
$$

gives a fully explicit double Dirichlet integral for the forcing reservoir.

The remaining arithmetic comparison can now be performed by writing `n` and `m` in prime-power labels and sorting the double sum into primitive, square, connected, seam, and archimedean components. The presence of `D_(n,m)=n^2+m^2e^(2t)` shows that the decomposition is genuinely relational; it is not a termwise Euler product in either index alone.

Status: finite-cutoff theta autocorrelation evaluated explicitly; completion requires scaling-ray renormalization before prime-grade sorting.
