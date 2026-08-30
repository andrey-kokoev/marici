# The reciprocal tail plane has an empty positive symplectic cone

## Complete two-dimensional classifier

For the centered reciprocal tail symbol

\[
A_1=
\begin{pmatrix}
-1&0\\
0&1
\end{pmatrix},
\]

classify every skew-Hermitian symplectic form on the real two-dimensional tail plane.

Up to a nonzero real scalar, every such form is

\[
\Omega_\omega
=
\omega
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\qquad
\omega\neq0.
\]

The induced canonical Hamiltonian candidate is

\[
H_\omega
=
\Omega_\omega A_1
=
\omega
\begin{pmatrix}
0&-1\\
-1&0
\end{pmatrix}.
\]

It is Hermitian, and its eigenvalues are

\[
\lambda_\pm=\pm|\omega|.
\]

Therefore

\[
H_\omega\not\ge0
\qquad
\text{for every nondegenerate }\Omega_\omega.
\]

The admissible cone of nondegenerate symplectic forms producing a positive semidefinite Hamiltonian is empty.

## Meaning

This removes the remaining coordinate ambiguity on the reciprocal tail plane. The previous indefinite result was not an artifact of choosing the standard \(J\). Every possible nondegenerate skew form in dimension two gives the same mixed signature.

Reciprocal doubling is necessary because it restores trace zero and Hamiltonian spectral pairing, but it is still insufficient for a Hilbert-positive canonical realization.

## Minimal enlargement theorem

A positive canonical model must use a larger source module. The wall, square, and archimedean channels cannot be attached only after constructing a tail-plane Hamiltonian; they must participate in the symplectic form and spectral coefficient before reduction.

Let the enlarged spectral symbol and skew form be

\[
\mathcal A_1=
\begin{pmatrix}
A_1&B\\
C&D
\end{pmatrix},
\qquad
\Omega=
\begin{pmatrix}
\Omega_{tt}&\Omega_{ta}\\
\Omega_{at}&\Omega_{aa}
\end{pmatrix}.
\]

The relevant condition is positivity of the full product

\[
\mathcal H=\Omega\mathcal A_1\ge0,
\]

not positivity of \(\Omega_{tt}A_1\) followed by a later endpoint correction. Off-diagonal source incidence may change the effective signature only at this enlarged level.

## Rank warning

Adding a spectrally inert positive coordinate does not automatically help. If the added channel contributes only to \(A_0\) and not to \(\mathcal A_1\), the positive spectral Hamiltonian may retain the tail obstruction. The source audit must determine which wall or archimedean channels actually carry centered spectral weight.

Thus the next inventory needs, for each added channel:

- its coefficient in \(\mathcal A_1\);
- its pairing in \(\Omega\);
- its boundary trace;
- its reciprocal character;
- whether it is reachable from the theta forcing.

## Decisive finite test

Build the smallest enlarged source cell and solve the joint linear matrix system

\[
\Omega^*=-\Omega,
\qquad
\Omega\mathcal A_1=(\Omega\mathcal A_1)^*\ge0,
\qquad
\mathcal A_0^*\Omega+\Omega\mathcal A_0=0,
\]

with boundary isotropy. Report the full solution cone. Since the two-dimensional cone is empty, any successful ray must visibly use an added source channel. This makes the authority contribution of wall and archimedean completion mechanically testable.
