# The scalar Weil boundary has the squarefree Xi determinant

Sequence claim: \`seqclaim-d524480297f27f30b3dd6e54\` (1403).

Epistemic-graph event: 1451.

## Scalar Weil completion under RH

Assume RH so that the Weil form is positive. On the spectral side it is

\`W(g*g*)=sum_lambda m_lambda |G(lambda)|^2\`,

where \`lambda\` ranges over the distinct real Xi zeros and \`m_lambda\` is
their order. Its Hilbert completion is

\`H_W=L^2(sum_lambda m_lambda delta_lambda)\`.

An atom remains one-dimensional regardless of its mass. The multiplication
operator \`A_W G(lambda)=lambda G(lambda)\` therefore has each distinct
eigenvalue exactly once. The constant function is cyclic, so this is also a
special case of the general theorem that a cyclic self-adjoint operator has
simple point spectrum.

## Determinant theorem

The symmetric modified determinant of this scalar Weil operator is

\`D_W(z)=product_(lambda>0, distinct)(1-z^2/lambda^2)\`.

By contrast,

\`Xi(z)/Xi(0)
 =product_(lambda>0, distinct)
  (1-z^2/lambda^2)^(m_lambda)\`.

Hence

\`D_W=Xi/Xi(0)\`

if and only if every Xi zero is simple. With no simplicity assumption,
\`D_W\` is the squarefree spectral product, and the missing factor is

\`product_(lambda>0)(1-z^2/lambda^2)^(m_lambda-1)\`.

The atom weights affect the distinguished boundary vector and Weyl residues,
but Fredholm determinants count Hilbert-space dimension. They cannot repair
this discrepancy.

## Consequence for the source boundary

The scalar Weil radical quotient cannot by itself meet both requirements

1. remain the Hilbert completion of the explicit-formula evaluation pairing;
2. have determinant equal to Xi with its full zero divisor;

unless zeta-zero simplicity is added.

Ledger 1402's jet associated graded supplies the correct dimensions, but its
extra graded lines lie outside the scalar Weil quotient. A full solution must
therefore prove one of two genuinely stronger statements:

- **simplicity branch:** all Xi zeros are real and simple, after which the
  scalar Weil/Pick boundary has the correct determinant; or
- **jet branch:** the Mellin source has a canonical vector-valued or
  derivative-enhanced boundary pairing whose local rank is \`m_lambda\`.

RH alone selects reality but does not choose between these branches.

## Smallest falsifier

For a double zero \`lambda\`, the local Weil form is the one-dimensional norm

\`2|G(lambda)|^2\`.

Its local determinant factor is \`1-z/lambda\`. Xi requires
\`(1-z/lambda)^2\`. No change of the positive scalar weight two changes the
dimension or determinant exponent. This is the minimal hostile model.

## Scope

This is conditional on Weil positivity/RH only for the Hilbert interpretation.
The rank and determinant comparison is algebraic. It does not assert that a
multiple zeta zero exists and does not disprove a vector-valued source
boundary.
