# Xi multiplicities require amplification beyond the scalar Weyl model

Sequence claim: \`seqclaim-240242b4940547529851d1fb\` (1401).

Epistemic-graph event: 1447.

## Defect found

Ledger 1382 correctly proves

\`RH iff M_Xi=-Xi'/Xi is Nevanlinna\`,

but it compressed two different realizations into one sentence. If

\`M_Xi(z)=sum_lambda m_lambda/(lambda-z)\`

under RH, the scalar Herglotz measure is

\`mu=sum_lambda m_lambda delta_lambda\`.

The Hilbert space \`L^2(mu)\` has one dimension at each *distinct* atom,
regardless of its mass. Multiplication by \`lambda\` therefore has each
distinct eigenvalue once. The mass \`m_lambda\` is the squared norm of the
boundary vector component, not the dimension of the eigenspace. Its Fredholm
determinant consequently counts each distinct zero once and need not equal Xi
when a zero is multiple.

## Exact repair

The source-defined meromorphic function contains the missing integer:

\`m_lambda=-Res_(z=lambda) M_Xi(z)\`.

Define the multiplicity-amplified Hilbert space and operator

\`H_mult = direct_sum_lambda C^(m_lambda)\`,

\`A_mult|C^(m_lambda) = lambda I_(m_lambda)\`.

Choose in each fiber a vector of squared norm \`m_lambda\`; its scalar resolvent
matrix element recovers the same \`M_Xi\` (up to the usual affine Herglotz term).
Different choices are unitarily equivalent. Thus Xi determines this amplified
operator up to unitary equivalence without a supplied numerical zero list.
Under RH it is self-adjoint, has compact resolvent, and

\`det_2(I-z A_mult^(-1))=Xi(z)/Xi(0)\`.

The scalar Weyl function does not make the amplification minimal or cyclic:
the \`m_lambda-1\` directions orthogonal to the boundary vector are invisible to
that scalar boundary channel. The repaired determinant construction is an
abstract multiplicity amplification derived from pole residues, not the
minimal scalar Herglotz realization by itself.

## Entire-function quotient obstruction

The same distinction appears in the CCM quotient. Near a zero \`lambda\` of
multiplicity \`m\`, the principal-ideal quotient has local algebra

\`O_lambda/(z-lambda)^m\`.

Multiplication by \`z\` is \`lambda I+N\`, where \`N\` is a nonzero nilpotent
Jordan operator when \`m>1\`. No positive Hilbert inner product can make this
operator self-adjoint: a self-adjoint nilpotent operator is zero. Passing to
the radical quotient removes \`N\` but also forgets multiplicity, so its
determinant contains the zero only once.

Therefore the literal principal-ideal quotient is Hilbert-self-adjoint only
if all Xi zeros are simple. RH alone does not imply that statement. Without
simplicity, a self-adjoint determinant model must semisimplify the quotient
and restore the residue multiplicities as fiber dimensions.

## Smallest hostile test

Replace Xi locally by \`F(z)=(z-lambda)^2\`. Then

\`-F'/F=-2/(z-lambda)\`.

The scalar Herglotz space has one atom of mass two and hence a one-dimensional
multiplication operator; its determinant has one factor \`(1-z/lambda)\`. The
principal-ideal quotient has the two-dimensional Jordan block

\`[[lambda,1],[0,lambda]]\`,

which is not self-adjoint in any positive metric. The amplified semisimple
operator \`lambda I_2\` is self-adjoint and has the required squared determinant
factor. These three objects have to remain distinct.

## Consequence

The conditional existence theorem survives after repair: theta-derived Xi,
RH positivity, and residue amplification give a self-adjoint
compact-resolvent operator with the correct determinant. What remains
unproved is still the requested source boundary: the Mellin/Weil quotient must
itself supply the semisimplification and multiplicity fibers rather than have
them attached by abstract inverse spectral reconstruction.

## Scope

This repairs the multiplicity logic of Ledger 1382. It neither assumes nor
proves simplicity of the zeta zeros and does not prove RH.
