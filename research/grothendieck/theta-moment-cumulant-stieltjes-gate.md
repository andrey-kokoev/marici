# Theta positivity does not imply the xi Stieltjes property

Epistemic-graph event: 1426.

## Normalize the theta kernel

Let

\`B(y)=Xi(i y)=integral_0^infinity Phi(u) cosh(yu) du\`

and normalize the positive measure

\`d nu(u)=Phi(u)du/B(0)\`.

Write its even moments as

\`m_(2n)=integral u^(2n)d nu(u)\`.

Then

\`F(x)=B(sqrt(x))/B(0)
=sum_(n>=0) m_(2n)x^n/(2n)!\`

has positive Taylor coefficients, and the Stieltjes candidate of Ledger 1385
is

\`R_Xi(x)=F'(x)/F(x)\`.

## First exact cumulant gates

Expanding the logarithmic derivative gives

\`R_Xi(0)=m_2/2\`,

\`R_Xi'(0)=(m_4-3m_2^2)/12\`,

and

\`R_Xi''(0)
=(m_6-15m_2m_4+30m_2^3)/120\`.

Complete monotonicity therefore begins with

\`m_4<=3m_2^2\`

and

\`m_6-15m_2m_4+30m_2^3>=0\`.

The first inequality says that the normalized theta density has kurtosis at
most three. The higher inequalities are alternating even log-cumulant
conditions, not ordinary moment positivity.

## Positive density is insufficient

Consider the positive even probability measure

\`nu_epsilon=(1-epsilon)delta_0
+(epsilon/2)(delta_L+delta_(-L))\`.

It has \`m_2=epsilon L^2\` and \`m_4=epsilon L^4\). The first Stieltjes
condition becomes \`epsilon>=1/3\`. Thus every \`0<epsilon<1/3\` is a positive
even-kernel counterexample. Narrow symmetric smooth approximations preserve
the strict violation.

Therefore positivity, evenness, rapid decay, and an entire cosh transform do
not yield the desired Stieltjes measure. A proof for the Riemann theta kernel
must use stronger source structure such as total positivity or a sufficiently
strong log-concavity/variation-diminishing theorem.

## Exploratory theta values

A direct 80-digit differentiation of the completed theta function at the
origin gives

\`m_2 approximately 0.04620998623083794\`,
\`m_4 approximately 0.00596001729093946\`,
\`m_6 approximately 0.00120553389214916\`.

The first two nontrivial signed residuals are positive:

\`3m_2^2-m_4 approximately 4.46071191423236e-4\`,

\`m_6-15m_2m_4+30m_2^3
 approximately 3.46017435362336e-5\`.

The first six coefficients of \`R_Xi(x)\` alternate with positive signed
magnitudes in the same diagnostic. These finite numerical checks validate the
expansion and find no low-order falsifier; they do not prove complete
monotonicity or the Stieltjes property.

## Constructive consequence

The desired positive spectral measure cannot be taken to be the theta density
\`Phi(u)du\` itself. It is a nonlinear logarithmic-cumulant transform of that
density. The missing boundary functor must explain why this nonlinear
transform is positive and atomic. Merely applying the Fourier, Mellin,
reflection, or compression operations already tested does not do so.

## Scope

This derives exact low-order source inequalities and proves a general
positivity insufficiency theorem. It neither falsifies the Riemann theta
kernel nor proves its full Stieltjes hierarchy.
