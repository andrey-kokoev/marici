# Global recurrence transfer reduces to an ell-two product cocycle

## Question

What exact recurrence estimate would preserve one polynomial state across the entire shifted Weibull tail?

Let \(P_n^{(X)}\) be orthonormal for the normalized shifted measure

\[
d\nu_X(y)=e^{-2a[(X+y)^\beta-X^\beta]}\,dy,
\qquad y\geq0.
\]

Its Jacobi recurrence is

\[
yP_n^{(X)}(y)=a_{n+1}^{(X)}P_{n+1}^{(X)}(y)
+b_n^{(X)}P_n^{(X)}(y)
+a_n^{(X)}P_{n-1}^{(X)}(y).
\]

At the endpoint \(y=0\), define

\[
u_n^{(X)}=
\begin{pmatrix}P_n^{(X)}(0)\\P_{n-1}^{(X)}(0)\end{pmatrix}.
\]

Then

\[
u_{n+1}^{(X)}=T_n^{(X)}u_n^{(X)},
\qquad
T_n^{(X)}=
\begin{pmatrix}
-b_n^{(X)}/a_{n+1}^{(X)}&-a_n^{(X)}/a_{n+1}^{(X)}\\
1&0
\end{pmatrix}.
\]

The endpoint kernel is finite exactly when

\[
\sum_{n\geq0}|P_n^{(X)}(0)|^2<\infty.
\]

Thus global recurrence transfer does preserve polynomial coherence, but the required quantitative theorem is an ell-two bound on the first coordinate of the product cocycle

\[
T_{n-1}^{(X)}\cdots T_0^{(X)}u_0^{(X)}.
\]

## Artifact audit

The gamma comparator bounds individual moments. It does not provide Loewner-stable inverse Hankel bounds, hence it does not bound the Jacobi coefficients uniformly in \(n\). Finite Christoffel computations provide partial sums of the desired series from below. Neither artifact controls the infinite cocycle tail.

## Disposition

Resolve the structural recurrence reduction, but defer quantitative recurrence transfer. The next executable leaf is `jacobi-coefficient-asymptotics`: derive two-sided large-degree bounds for \(a_n^{(X)}\) and \(b_n^{(X)}\), uniform enough in the moving start \(X\) to test cocycle contraction.

## Claim boundary

No contraction follows merely from norms or eigenvalues of individual transfer matrices; noncommuting products and the selected initial vector matter. This packet defines the missing estimate and does not claim it.
