# The canonical Xi jet pairing is Krein, not Hilbert

Sequence claim: \`seqclaim-55af5867d14169fbaceabed7\` (1405).

Epistemic-graph event: 1455.

## Canonical local pairing

The local Xi quotient

\`A_lambda=O_lambda/(Xi)\`

is a one-variable Artinian Gorenstein algebra. It has the source-canonical
Grothendieck residue pairing

\`B_lambda([f],[g])=Res_(z=lambda)
                   f(z) conjugate(g(conjugate z)) dz/Xi(z)\`.

When \`lambda\` is real, conjugation preserves the local algebra. The pairing
is nondegenerate and multiplication by the real spectral coordinate is
self-adjoint with respect to it:

\`B_lambda(zf,g)=B_lambda(f,zg)\`.

Thus the principal-ideal quotient already carries a canonical
multiplicity-sensitive boundary form. It is the correct algebraic explanation
for why its Jordan multiplication is symmetric in an indefinite geometry.

## Positivity obstruction

Write locally \`Xi(z)=u(z)t^m\`, with \`t=z-lambda\` and \`u(lambda)!=0\`.
After an invertible triangular change of jet basis, the residue matrix is
congruent to the anti-diagonal form on

\`1,t,...,t^(m-1)\`.

If \`m>1\`, the nonzero socle vector \`t^(m-1)\` is isotropic:

\`B_lambda(t^(m-1),t^(m-1))=0\`.

A positive-definite Hermitian form has no nonzero isotropic vector. Since the
residue form is nondegenerate, it is necessarily indefinite whenever the zero
is multiple. No scalar rescaling repairs this.

For the smallest case \`Xi_local=t^2\`, the basis \`(1,t)\` gives

\`B=[[0,1],[1,0]]\`,

with one positive and one negative direction. Multiplication by
\`z=lambda+t\` is the Jordan matrix

\`T=[[lambda,0],[1,lambda]]\`

in the column convention and satisfies \`B T=T^* B\`. It is Krein-self-adjoint
but cannot be Hilbert-self-adjoint.

## Three incompatible source structures

At a multiple zero the available constructions now separate exactly:

1. The scalar Weil form is positive under RH but has local rank one, so it
   loses determinant multiplicity.
2. The Grothendieck residue form is nondegenerate on all \`m\` jet directions
   and makes the Jordan operator symmetric, but it is indefinite.
3. The associated-graded square-sum form is positive and
   multiplicity-preserving after RH, but its orthogonalization is not induced
   by either canonical source form.

Therefore a positive multiplicity-sensitive Mellin boundary cannot be
obtained merely by choosing between the Weil and residue pairings. It requires
additional source polarization data that both kills the nilpotent extension
and converts the residue Krein form into a positive form on the graded pieces.

## Simple-zero branch

When \`m=1\`, the local residue form is a nonzero scalar. Its sign is not
automatically positive, but a one-dimensional polarization can flip it. The
Weil form already supplies the positive weight one. Hence the residue/Weil
rank conflict disappears under simplicity; only global RH positivity remains.

## Falsifier

Any proposed canonical positive jet pairing derived solely by multiplying the
local residue form by a nonzero scalar fails on \`C[t]/(t^2)\`: the vector
\`t\` remains nonzero and isotropic. Any proposal that instead quotients the
isotropic direction reduces the local rank to one and loses the squared
determinant factor.

## Scope

This is a local algebraic no-go for the unpolarized residue pairing. It does
not rule out extra source-derived Hodge/polarization data or the possibility
that all Xi zeros are simple.
