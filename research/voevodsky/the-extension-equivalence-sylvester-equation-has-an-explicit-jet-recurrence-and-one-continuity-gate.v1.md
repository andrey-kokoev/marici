# The extension-equivalence Sylvester equation has an explicit jet recurrence and one continuity gate

## Question

Can a bounded triangular correction compare the radial augmented extension with the conservative extension despite the native mismatch between \(B^\dagger\) and \(\pi_0\)?

## Claim boundary

Let the radial extension be \(A_{\mathrm{aug}}=\begin{pmatrix}\lambda&-\pi_0\\0&S\end{pmatrix}\), let the conservative upper extension be \(C_{\mathrm{cons}}=\begin{pmatrix}A_0&-B^\dagger\\0&D_0\end{pmatrix}\), and seek a triangular comparison \(F=\begin{pmatrix}q&X\\0&h\end{pmatrix}\).

The equation \(C_{\mathrm{cons}}F=FA_{\mathrm{aug}}\) is equivalent to \(A_0q=q\lambda\), \(D_0h=hS\), and \(A_0X-XS=B^\dagger h-q\pi_0\).

On one shell where the Euler comparison identifies \(A_0\) with scalar multiplication by \(\lambda\), put \(R=B^\dagger h-q\pi_0\). Write a continuous candidate row as \(X(a)=\sum_{j\ge0}x_ja_j\) and the residual row as \(R(a)=\sum_{j\ge0}r_ja_j\). Since \(S(a_0,a_1,\ldots)=(a_1,a_2,\ldots)\), coefficient comparison in \(\lambda X-XS=R\) gives \(\lambda x_0=r_0\) and \(\lambda x_j-x_{j-1}=r_j\) for \(j\ge1\).

For \(\lambda\neq0\), the unique forward recurrence is \(x_j=\sum_{m=0}^jr_m\lambda^{-(j-m+1)}\). This formula gives the only triangular correction compatible with the chosen forward jet ordering.

The native equality \(B^\dagger h=q\pi_0\) corresponds to \(R=0\) and produces \(X=0\). A nonzero residual can therefore be absorbed by a nonzero triangular comparison exactly when the coefficient sequence \((x_j)\) defines a continuous functional on the declared projective boundary-jet space.

At \(\lambda=0\), solvability requires \(r_0=0\), followed by \(x_{j-1}=-r_j\); the free terminal behavior must be fixed by the topology or an additional boundary condition. For \(\lambda\neq0\), continuity may fail when the factors \(|\lambda|^{-j}\) outgrow the dual weights of the jet space.

If \(q\) and \(h\) are bounded graph isomorphisms and the row \(X\) is continuous, then \(F\) is a bounded triangular isomorphism with \(F^{-1}=\begin{pmatrix}q^{-1}&-q^{-1}Xh^{-1}\\0&h^{-1}\end{pmatrix}\).

## Disposition

The algebraic Sylvester problem is solved by an explicit jet recurrence. The remaining analytic gate is continuity of that row in the actual boundary-jet topology, together with construction of the history comparison \(h\) needed to determine the residual coefficients \(r_j\). The prior native-adjoint mismatch selects a nonzero correction rather than rejecting extension equivalence.
