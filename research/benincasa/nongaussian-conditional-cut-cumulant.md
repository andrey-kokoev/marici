# Non-Gaussian conditional Cut sewing requires the fourth cumulant

Let \(X,Y\in\{\pm1\}\) have the correlated distribution

\[
\Pr(X=x,Y=y)=\frac{1+rxy}{4},
\qquad |r|\le1.
\]

Then

\[
\mathbb E[X^2]=\mathbb E[Y^2]=1,
\qquad
\mathbb E[XY]=r,
\qquad
\mathbb E[X^2Y^2]=1.
\]

Gaussian Wick closure would predict

\[
1+2r^2.
\]

The exact connected fourth cumulant is

\[
\boxed{\kappa_{22}=-2r^2,}
\]

which restores the physical fourth moment:

\[
1+2r^2+\kappa_{22}=1.
\]

Exact conditional pushforward remains associative because \(Y^2=1\) pointwise:

\[
\mathbb E\!\left[X^2\mathbb E(Y^2\mid X)\right]=1,
\]

and similarly in the opposite order.

Thus non-Gaussianity does not obstruct nested Cut associativity when the full joint coefficient state is retained. It invalidates Gaussian closure: covariance and pairings alone omit the fourth-cumulant correction. A cumulant-truncated coefficient object is therefore filtered and must declare its retained grade.
