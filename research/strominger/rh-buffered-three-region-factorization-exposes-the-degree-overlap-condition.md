# Buffered three-region factorization exposes the degree-overlap condition

## Question

Can two overlap cuts remove the sharp local--far interface singularity while preserving all particles?

Choose rescaled cuts

\[
z_-=X^{\beta/8},
\qquad
z_+=X^{3\beta/8},
\]

both inside the Laguerre overlap \(z=o(X^{\beta/2})\), and define regions \(A,C,B\) separated by these cuts. Andréief's integral splits exactly over occupancies \(k+\ell+m=n\) with coefficient

\[
\frac1{k!\ell!m!}.
\]

Each sector retains all three internal Vandermonde factors and all three pairwise cross factors. Transition particles are not discarded.

For \(x\in A\), \(y\in B\),

\[
0\leq\frac{x}{y}\leq r_X:=\frac{z_-}{z_+}=X^{-\beta/4}.
\]

Expanding only the separated \(A\)--\(B\) interaction gives, for sufficiently large \(X\),

\[
\left|2\log(1-x/y)+2x/y\right|
\leq2(x/y)^2.
\]

With \(km\leq n^2/4\) cross pairs, the accumulated remainder is bounded by

\[
\frac12 n^2X^{-\beta/2}.
\]

Hence this expansion is asymptotically small under

\[
n=o(X^{\beta/4}).
\]

For \(\beta=1/4\), this is \(n=o(X^{1/16})\).

## Disposition

Construct the exact buffered factorization and its degree-overlap condition. The condition is too restrictive to assume silently. The next leaf is `transition-occupancy-bound`: determine whether ensemble concentration reduces the effective number of separated cross pairs or whether a nonperturbative interface treatment is required.

## Claim boundary

Only the separated \(A\)--\(B\) cross term is expanded. Interactions involving \(C\) remain exact. No occupancy concentration or determinant asymptotic is proved.
