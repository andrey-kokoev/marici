# Euler-domain Mellin modes are total in the polarized Xi jet boundary

Sequence claim: \`seqclaim-de6abc770ec47b55ba625d6e\` (1408).

Epistemic-graph event: 1458.

## Source modes

For \`Im(z)>1/2\`, take the one-sided logarithmic Mellin mode

\`g_z(u)=i exp(i z u) 1_(u>=0)\`.

With the Fourier convention of Ledger 1396,

\`G_z(lambda)=1/(lambda-z)\`.

Its normalized jet at a zero \`lambda\` is

\`G_z^(k)(lambda)/k!
 =(-1)^k/(lambda-z)^(k+1)\`.

Thus the half-line source produces the Cauchy jet vector

\`v_z(lambda,k)=(-1)^k/(lambda-z)^(k+1)\`,

for every \`0<=k<m_lambda\).

## Membership

In the polarized jet norm of Ledger 1407,

\`||v_z||^2
 =sum_lambda m_lambda
  sum_(k=0)^(m_lambda-1)|lambda-z|^(-2k-2)\`.

Away from finitely many spectral points, \`|lambda-z|>2\), and the inner sum
is bounded by a fixed multiple of \`|lambda|^(-2)\). The canonical-product
convergence (equivalently the Riemann--von Mangoldt bound) gives

\`sum_lambda m_lambda/|lambda|^2<infinity\`.

Hence every Euler-domain source mode defines a vector in the full
multiplicity-sensitive jet boundary.

## Totality theorem

Let \`a=(a_(lambda,k))\` be orthogonal to \`v_z\` for every
\`Im(z)>1/2\). Then

\`F_a(z)=sum_lambda m_lambda
         sum_(k=0)^(m_lambda-1)
         conjugate(a_(lambda,k))(-1)^k
         /(lambda-z)^(k+1)\`

vanishes on that open domain. Cauchy--Schwarz with the preceding norm estimate
gives normal convergence on compact subsets away from the zero divisor, so
\`F_a\` is meromorphic with poles only at the Xi zeros.

The identity theorem makes \`F_a\` identically zero on the complement of its
poles. At each \`lambda\`, its complete principal part is

\`m_lambda sum_k conjugate(a_(lambda,k))(-1)^k
              /(lambda-z)^(k+1)\`.

Every principal-part coefficient must vanish, hence every
\`a_(lambda,k)=0\`. Therefore

\`closure span{v_z:Im(z)>1/2}=H_J\`.

## Consequences

The extra jet lines introduced by the associated-graded quotient are not
spectrally detached decorations. The original one-sided Mellin family reaches
them through derivatives of its Cauchy transform, and its open Euler domain is
already total.

Conditional on RH, the source map therefore extends uniquely and onto the
positive polarized jet boundary. Together with Ledger 1407 this yields a
Mellin-dilation boundary operator with:

- discrete real spectrum;
- full Xi zero multiplicities;
- compact resolvent and Hilbert--Schmidt inverse; and
- \`det_2(I-zA^(-1))=Xi(z)/Xi(0)\`.

No numerical zero list enters the construction. The sole analytic condition
left for self-adjointness is the reality of the quotient spectrum, exactly RH.

## Non-RH falsifier

If a nonreal Xi zero exists, its jet principal part is still detected by the
same total Cauchy family, but the corresponding diagonal eigenvalue is
nonreal. Thus source totality cannot hide or quotient away an RH violation:
the operator is then discrete and normal after square-sum completion, but not
self-adjoint.

## Scope

Conditional totality and self-adjoint determinant theorem for the analytic
Mellin/source-ideal-saturated jet boundary. This does not prove RH and does
not construct the separate physical coefficient--Betti relative-chain
pushforward.
