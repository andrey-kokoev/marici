# The Cayley--Schur characteristic factors into the inverse Euler block and one coupled numerator

## Finite cutoff

Let \(S_X(z)\) be the finite prime-delay direct sum and let

\[
\Theta_X(z)
=i(I+S_X(z))(I-S_X(z))^{-1}.
\]

Let the history Weyl return on the same source space be

\[
M_{H,X}(z)
=B_X^\dagger(A_X-z)^{-1}B_X.
\]

The source Schur characteristic is

\[
M_{U,X}(z)=\Theta_X(z)+M_{H,X}(z),
\]

with the sign adjusted if the opposite Green convention is used.

## Exact right factorization

Right multiplication by \(I-S_X\) gives

\[
M_{U,X}(I-S_X)
=
i(I+S_X)+M_{H,X}(I-S_X).
\]

Define the coupled numerator

\[
N_X(z)
=
i(I+S_X(z))
+M_{H,X}(z)(I-S_X(z)).
\]

Then

\[
M_{U,X}(z)
=N_X(z)(I-S_X(z))^{-1}.
\]

No commutativity between \(S_X\) and \(M_{H,X}\) is required because the
factorization order is retained.

## Determinant identity

At finite cutoff,

\[
\det M_{U,X}(z)
=
\det N_X(z)
\det(I-S_X(z))^{-1}.
\]

Since

\[
S_p(z)=p^{-s},
\]

one has

\[
\det(I-S_X(z))^{-1}
=
\zeta_X(s).
\]

Therefore

\[
\det M_{U,X}(z)
=
\det N_X(z)\zeta_X(s).
\]

This places the Euler factor in the denominator with the correct variance,
without assigning parity after determinant evaluation.

## Kernel identity

Because \(I-S_X\) is invertible in the strict Schur chart,

\[
\ker M_{U,X}(z)
=
(I-S_X(z))\ker N_X(z)
\]

with the evident ordered isomorphism.  Thus every characteristic collision is
carried by the coupled numerator \(N_X\), not by a local prime-loop resonance.

## Prime-power filtration

The inverse Euler block has the exact finite expansion

\[
\det(I-S_X)^{-1}
=
\exp\left(
\operatorname{Tr}S_X+
\frac12\operatorname{Tr}S_X^2
\right)
\det_3(I-S_X)^{-1}.
\]

Hence primitive, square, and connected grades remain attached to one ordered
factor.  The numerator \(N_X\) must not duplicate those low-grade cumulants.

## Completed determinant-line target

After adding the source archimedean and endpoint line, G4 reduces to proving a
completed identity of the form

\[
\det_{\rm rel}N(z)
=E(z)B_\infty(s),
\]

if the numerator is a unit, or more generally

\[
\det_{\rm rel}M_U(z)
=E(z)\xi(s).
\]

The first form would make the coupled numerator divisor-free and leave the Xi
divisor in the completed Euler/theta section.  The second permits the numerator
to carry the boundary divisor.  These alternatives cannot be identified
without a source comparison.

## Passivity consequence and limit

On each open half-plane, compatible strict signs of \(\Theta\) and \(M_H\)
make \(M_U\), hence \(N\), invertible.  This gives the desired off-seam
orientation for the completed characteristic if cutoff convergence and
minimality hold.

At finite cutoff, all factors are nonzero in the strict Schur chart.  Any
nontrivial divisor can arise only in the completed boundary limit.  Uniform
inverse bounds are therefore essential to distinguish a genuine seam divisor
from spectral pollution.

## G4 consequence

The arithmetic Cayley law and history Weyl return now assemble into one exact
finite characteristic with correct inverse Euler variance:

\[
\det M_{U,X}=\zeta_X\det N_X.
\]

The remaining calculation is no longer an unspecified closed-loop
determinant.  It is the completed determinant-line identification and
compact-local inverse control of the single coupled numerator \(N_X\).  No RH
conclusion is authorized.
