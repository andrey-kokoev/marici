# G4 must separate the triangular divisor compiler from the conservative Green pencil

## Two tasks previously conflated

G4 contains two distinct comparison problems:

1. compile the theta Xi section together with a zero-free arithmetic
   complement into one determinant-line object;
2. map the Xi residue to a state in a conservative maximal-isotropic Green
   pencil.

The first is naturally triangular and non-self-adjoint. The second is a
Green-domain chain-map problem. A strict same-sign passive three-port pencil
cannot perform both tasks at once.

## Triangular divisor compiler

The theta side is the canonical Koszul complex

\[
K_\tau:
\mathcal L_\theta\xrightarrow{\tau}\mathcal O.
\]

Let \(Q_U\) be a holomorphically invertible arithmetic complement. Then the
stabilized triangular complex

\[
C_{\rm div}(s)
=
\begin{pmatrix}
\tau(s)&A(s)\\
0&Q_U(s)
\end{pmatrix}
\]

has determinant section

\[
\operatorname{Det}C_{\rm div}
=
\operatorname{Det}Q_U\,\tau.
\]

A bounded triangular elimination removes \(A\) using \(Q_U^{-1}\), so the
local cokernel module is

\[
\mathcal O/(\tau)
\]

and Xi multiplicity is preserved exactly.

This construction is valid only when \(A\) is a source-derived chain arrow and
the determinant line of \(Q_U\) has the required Euler/anomaly descent. It is
not an RH proof: the Xi section is already the differential of \(K_\tau\).

## Conservative Green pencil

A maximal-isotropic spectral realization instead needs a chain map

\[
(i,w):K_\tau\to C_{\rm FP},
\qquad
C_{\rm FP}i=w\tau,
\]

with an invertible complement and a holomorphically contractible mapping cone.
At \(\tau=0\), this sends the determinant-line residue to a nonzero Green-domain
state.

This is stronger than determinant stabilization. It cannot be replaced by
placing \(K_\tau\) as an explicit diagonal block, because that merely rewrites
the known scalar section.

## Same-sign obstruction

For the symmetric three-port characteristic

\[
M_{\theta U}
=C^\dagger R_+C+
\begin{pmatrix}0&0\\0&D_U\end{pmatrix},
\]

same-sign passivity with strict \(\operatorname{Im}D_U\) forces every seam
kernel to have arithmetic coordinate zero. Hence arithmetic Schur feedback
cannot manufacture the Xi divisor.

The triangular divisor compiler avoids this obstruction because it is not a
self-adjoint passive kernel pencil. Conversely, it supplies no conservative
Green state without the separate chain map.

## Correct constructor order

The admissible order is:

1. construct \(K_\tau\) from the theta determinant line;
2. construct and descend the zero-free arithmetic complement \(Q_U\);
3. form the triangular determinant compiler and verify its typed elimination;
4. independently construct \(C_{\rm FP}\) and maximal-isotropic domains;
5. build \((i,w)\) and prove \(C_{\rm FP}i=w\tau\);
6. prove the mapping-cone complement is contractible with uniform completed
   bounds.

Only steps 5--6 promote the known divisor into an independent Green-domain
state theorem.

## Consequence for the dressed scalar

The scalar Schur expression \(F_\theta\) should not be required simultaneously
to be:

- the theta Koszul differential by construction;
- an arithmetic-feedback-generated zero set;
- and the characteristic of a strict same-sign conservative pencil.

Those requirements are incompatible unless the bare theta Weyl section
already has the Xi divisor and the arithmetic mixed covector vanishes there.
In that case arithmetic dressing contributes only a zero-free determinant
unit.

## Disposition

The zero-free Cayley complement remains eligible for determinant stabilization
and complement control. The symmetric same-sign three-port pencil is not an
arithmetic generator of Xi zeros. The decisive open G4 object is again the
source chain map from \(K_\tau\) to the maximal-isotropic Green pencil, not a
further Schur rearrangement. No RH conclusion is authorized.
