# The Mixed Green Kernel Is Cauchy Character Covariance

## The phase-bearing realization

Let \(T\) have the centered Cauchy law of scale \(1/2\):

\[
d\mu_C(t)=\frac{dt}{2\pi(t^2+1/4)}.
\]

Its characteristic function is

\[
\mathbb E(e^{iuT})=e^{-|u|/2}.
\]

For each positive frequency \(x\), define the unitary Mellin character

\[
X_x(T)=e^{-iTx}.
\]

Then

\[
\mathbb E(X_x)=e^{-x/2}
\]

and

\[
\mathbb E(X_x\overline{X_y})=e^{-|x-y|/2}.
\]

Therefore

\[
\operatorname{Cov}(X_x,X_y)
=e^{-|x-y|/2}-e^{-(x+y)/2}.
\]

This is exactly the mixed Cauchy defect and the Dirichlet Green kernel from
Entries 3929 and 3931.

## Canonical global codiagonal

For a finite frequency packet \(c=(c_j)\), put

\[
F_c(T)=\sum_jc_jX_{x_j}(T).
\]

The missing global synthesis map is simply Cauchy expectation:

\[
M(c)=\mathbb E(F_c)=\sum_jc_je^{-x_j/2}.
\]

Centering before observation gives

\[
F_c^\circ=F_c-\mathbb E(F_c),
\]

and its norm is

\[
\|F_c^\circ\|_{L^2(\mu_C)}^2
=\sum_{j,k}\overline{c_j}
K(x_j,x_k)c_k.
\]

Thus the phase-bearing codiagonal required by Entry 3932 is not an additional
fitted map.  It is the orthogonal projection onto the constant Cauchy mode,
and the Green state is its orthogonal complement.

At prime frequencies,

\[
X_p(T)=p^{-iT},
\qquad
\mathbb E(X_p)=p^{-1/2}.
\]

The cross-prime coefficient follows without choosing a phase by hand:

\[
\operatorname{Cov}(X_p,X_q)
=\sqrt{\frac{\min(p,q)}{\max(p,q)}}
-\frac1{\sqrt{pq}}.
\]

The endpoint orientation is fixed by the sign in the centered variable
\(X_p-p^{-1/2}\).

## Three equivalent presentations

The same object now has three exact presentations:

1. multiplicativity defect of the Cauchy characteristic function across
   opposite Mellin sectors;
2. Dirichlet Green kernel of \(-d^2/dx^2+1/4\) on the half-line;
3. covariance kernel of unitary Mellin characters under the Cauchy observer.

The equivalence rotates the problem from a boundary-value calculation into a
Hilbert-space projection.  The seam image is the constant mode, and seam
retention means retaining the mean before passing to centered fluctuations.

This also supplies the source-authorized operation order:

1. retain labelled Mellin characters;
2. synthesize them in \(L^2(\mu_C)\);
3. project onto the constant mode and its orthogonal complement;
4. take norms only afterward.

## Scope boundary

This theorem derives the global codiagonal for the universal Cauchy observer,
not yet for the completed theta--Tate source.  It explains every linear and
quadratic term in the mixed Green kernel, but the BSY observable contains
\(\log|\zeta|\), which is nonlinear and requires Euler exponentiation,
regularization, and analytic completion.

Accordingly, the remaining obstruction has moved.  It is no longer the
existence or phase of the global seam codiagonal.  It is whether the nonlinear
Euler logarithm and theta--Tate completion descend through this centering
projection with exactly the BSY relative term.

## Next gate

Apply the centering projection to the finite Euler logarithm

\[
L_X(T)=\sum_{p\le X}\sum_{k\ge1}
\frac{p^{-k/2}X_p(T)^k}{k}.
\]

Its formal mean is

\[
\mathbb E(L_X)
=\sum_{p\le X}\sum_{k\ge1}\frac1{k p^k}.
\]

This is exactly the divergent Mertens channel plus the convergent square and
higher channels already isolated in Entry 3924.  The next calculation must
center \(L_X\) before exponentiation and compare that order with centering the
completed Euler product.  Their residual is a concrete candidate for the BSY
renormalization anomaly.
