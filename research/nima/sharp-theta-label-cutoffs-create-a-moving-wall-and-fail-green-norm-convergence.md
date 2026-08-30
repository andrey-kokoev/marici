# Sharp theta-label cutoffs create a moving wall and do not converge in the Green norm

## Finite label packet

Let

\[
\Psi_{p,N}(u)
=
\sum_{n=1}^{N}
\sum_{j=0}^{3}
c_{j,p}
n^{r_j}e^{r_ju}
e^{-\pi n^2e^{2u}},
\qquad
r_j=j+\frac12.
\]

For each fixed \(N\), this is a smooth \(L^2\) function. On every compact
\(u\)-interval it converges with all derivatives to the infinite theta packet
as \(N\to\infty\).

That local convergence does not imply convergence in the global Green norm.

## Moving-wall scaling

Set

\[
u=v-\log N,
\qquad
n=Ny.
\]

Then one summand becomes

\[
n^{r_j}e^{r_ju}e^{-\pi n^2e^{2u}}
=
y^{r_j}e^{r_jv}e^{-\pi y^2e^{2v}}.
\]

The Riemann-sum limit therefore gives

\[
N^{-1}\Psi_{p,N}(v-\log N)
\longrightarrow
F_p(v),
\]

locally uniformly in \(v\), where

\[
F_p(v)
=
\sum_{j=0}^{3}
c_{j,p}e^{r_jv}
\int_0^1
y^{r_j}e^{-\pi y^2e^{2v}}\,dy.
\]

The profile \(F_p\) is not identically zero. As \(v\to-\infty\), its slowest
term is

\[
\frac{c_{0,p}}{3/2}e^{v/2},
\]

and \(c_{0,p}=-2\pi(\log p)^2\ne0\).

Thus the finite label packet contains a transition layer of amplitude
proportional to \(N\), centered at

\[
u\sim-\log N.
\]

## Norm consequence

Choose a bounded interval \(I\) on which \(F_p\) is nonzero. Then

\[
\int_{I-\log N}
|\Psi_{p,N}(u)|^2\,du
\sim
N^2
\int_I|F_p(v)|^2\,dv.
\]

Hence

\[
\|\Psi_{p,N}\|_{L^2}
\]

grows at least linearly in \(N\). In particular, sharp label truncations are
not Cauchy in the Hilbert or quarter-gap Green norm.

The bounded resolvent

\[
\mathcal C^{-1}
\]

cannot repair this failure: boundedness transports convergence when it exists,
but does not manufacture convergence of a moving wall.

## Why the limiting wall subtraction is insufficient

The infinite packet has the asymptotic wall

\[
\rho_pe^{-u}.
\]

No finite sharp cutoff has that stationary wall at \(u=-\infty\); each finite
sum instead has a wall transition moving left with \(N\). Therefore
subtracting one fixed representative

\[
\rho_p\chi_-(u)e^{-u}
\]

from every finite cutoff does not produce a Green-Cauchy sequence.

The finite-cutoff subtraction must track the moving profile, or the source
must use an Abel/Poisson summation in which the wall is present as an
independently typed coefficient component at every regularization stage.

## Constructor requirement

A valid theta-completion theorem must supply renormalized packets

\[
\Psi_{p,N}^{\mathrm{ren}}
=
\Psi_{p,N}-W_{p,N}^{\mathrm{wall}}
\]

such that:

1. \(W_{p,N}^{\mathrm{wall}}\) is source-derived;
2. its moving-scale profile agrees with \(F_p\);
3. its completed coefficient tends to \(\rho_p\);
4. \(\Psi_{p,N}^{\mathrm{ren}}\) is Cauchy in the graph norm of
   \(\mathcal C\);
5. the construction intertwines the labelwise connection and reciprocal
   sewing.

This is the exact remaining wall-synthesis gate.

## Consequence

Local \(C^\infty\) label synthesis and existence of a bounded Green inverse
are both true, but they do not compose under sharp cutoffs. The obstruction is
a nonuniform wall escaping to the negative Mellin end.

The first Adams edge therefore needs a source-authorized renormalized
theta-synthesis map before the quarter-gap resolvent can be interchanged with
completion.

## Hostile

Verify convergence only on every fixed compact interval. The moving layer
eventually leaves each such interval, so all compact tests pass while the
global Green norm diverges like \(N\).
