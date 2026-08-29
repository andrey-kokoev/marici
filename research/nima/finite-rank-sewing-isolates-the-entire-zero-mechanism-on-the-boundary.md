# Finite-rank sewing isolates the entire zero mechanism on the boundary

The zero-free Euler carrier and the finite boundary pencil now fit through an exact relative-determinant identity.

Let \(S(z)\) be the prime-diagonal Schur operator, so
\[
\|S(z)\|<1
\]
in the right off-seam sector. Let the source sewing be represented by finite boundary maps
\[
U(z):\mathcal B\to\mathcal H_{\mathcal P},
\qquad
V(z)^{*}:\mathcal H_{\mathcal P}\to\mathcal B,
\]
and a boundary coupling \(C(z)\) on the finite-dimensional space \(\mathcal B\). Define the completed operator
\[
\widetilde S(z)
=
S(z)+U(z)C(z)V(z)^{*}.
\]

Since \(I-S(z)\) is invertible,
\[
I-\widetilde S
=
(I-S)
\left[
I-(I-S)^{-1}UCV^{*}
\right].
\]
The kernel equation reduces exactly to the boundary:
\[
(I-\widetilde S)f=0
\]
if and only if there exists \(b\neq0\) satisfying
\[
\left[I-C(z)G(z)\right]b=0,
\]
where
\[
G(z)
=
V(z)^{*}(I-S(z))^{-1}U(z).
\]

Thus the finite Birman--Schwinger operator is
\[
K_{\partial}(z)=C(z)G(z),
\]
and every zero arises from
\[
1\in\sigma(K_{\partial}(z)).
\]
The prime-diagonal bulk remains invertible throughout.

The relative determinant makes the same statement without requiring \(S\) to be trace class:
\[
\det_{\mathrm{rel}}
\left(
(I-\widetilde S)(I-S)^{-1}
\right)
=
\det_{\mathcal B}\left(I-CG\right).
\]
Because the perturbation is finite rank, the relative determinant is ordinary and finite-dimensional even when the bulk is only Hilbert--Schmidt.

This is the exact location of the zero divisor:
\[
\text{zero-free Euler carrier}
\times
\text{finite sewing determinant}.
\]
Any regularized bulk determinant contributes only a nowhere-zero factor in the open sector.

The resolvent expansion
\[
(I-S)^{-1}
=
\sum_{k\ge0}S^{k}
\]
shows how Euler prime powers enter the boundary Green function \(G(z)\). The arithmetic data are not lost; they are resummed inside the propagation between boundary incidence maps. The zero occurs only when the returned boundary amplitude closes coherently through \(C\).

This identifies the source responsibilities precisely:

1. \(S(z)\): prime-diagonal passive propagation.
2. \(U(z)\): primitive/wall injection into prime fibers.
3. \(V(z)^{*}\): tail, endpoint, or archimedean observation.
4. \(C(z)\): reciprocal sewing and boundary constitutive law.
5. \(G(z)\): propagated return through all prime powers.
6. \(I-CG\): finite spectral defect.

The construction is source-authorized only if \(U,V,C\) are independently derived. Given any target scalar function, a fitted rank-one perturbation can manufacture its zeros.

Completion requires:

- \(U\) and \(V^{*}\) bounded in the declared rigged topology;
- \(G(z)\) finite and analytic on compact off-seam sets;
- cutoff convergence of
  \[
  V_X^{*}(I-S_X)^{-1}U_X;
  \]
- preservation of reciprocal orientation;
- minimality of the boundary realization;
- identification of
  \[
  \det(I-CG)
  \]
  with \(\xi(\tfrac12-iz)\) up to a nowhere-zero source factor.

This finite-rank identity also reconciles the Weyl and scattering pictures. The return \(G(z)\) is the scattering-side Weyl function; the constitutive relation \(C(z)^{-1}\), where defined, is the arithmetic boundary relation. Indeed,
\[
I-CG
=
C\left(C^{-1}-G\right),
\]
so the collision is equivalently
\[
\det\left(C^{-1}-G\right)=0.
\]

The smallest hostile chooses unbounded \(U_X\) and vanishing \(V_X^{*}\) whose product \(G_X\) converges. The finite determinant looks correct, but the source realization loses completion stability through cancellation.

A second hostile fits \(C(z)\) directly from \(\xi\). It produces perfect spectral identification while moving the entire theorem into an unauthorized boundary coefficient.

The next concrete calculation should therefore freeze the source incidence maps \(U\) and \(V\) from the primitive wall and endpoint ports, then compute the first \(2\times2\) return matrix
\[
G_X(z)=V_X^{*}(I-S_X(z))^{-1}U_X.
\]
This is the earliest finite object capable of carrying the completed zero mechanism.
