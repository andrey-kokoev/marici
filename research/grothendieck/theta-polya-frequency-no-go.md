# The Riemann theta kernel cannot be Pólya-frequency of infinite order

Epistemic-graph event: 1427.

## Tempting but incorrect route

Ledger 1386 shows that positivity of the theta density is too weak to imply
the Stieltjes property of its logarithmic transform. A natural strengthening
would be to conjecture that the translation kernel \`Phi(x-y)\` is totally
positive of all orders, equivalently that \`Phi\` is a Pólya-frequency
function of infinite order.

Schoenberg's classification rules this out.

## Schoenberg reciprocal-transform theorem

If an integrable function \`f\` is Pólya-frequency of infinite order, its
bilateral Laplace transform

\`L_f(s)=integral_R exp(-s u)f(u)du\`

equals \`1/Psi(s)\` on a strip containing the imaginary axis, where \`Psi\`
is an entire Laguerre--Pólya function. Conversely, such reciprocals generate
the Pólya-frequency class.

For the even Riemann theta kernel, the bilateral transform is, up to the fixed
normalization and sign convention,

\`L_Phi(s)=Xi(i s)\`.

Because \`Phi\` decreases super-exponentially, \`L_Phi\` is entire, not merely
strip-holomorphic.

## Entire-reciprocal contradiction

Assume \`Phi\` were Pólya-frequency of infinite order. On the Schoenberg strip,

\`Xi(i s) Psi(s)=1\`.

Both factors on the left are entire, so the identity theorem extends this
equality to all \`s in C\`. It follows that both \`Xi(i s)\` and \`Psi(s)\`
are zero-free.

But completed \`xi\` has nontrivial zeros; indeed infinitely many critical-line
zeros are known unconditionally. Hence \`Xi(i s)\` has zeros in the complex
\`s\`-plane. Contradiction.

Therefore

\`Phi is not PF_infinity\`.

This conclusion is unconditional and does not depend on RH.

## Consequence for the positivity program

The desired positivity cannot be a variation-diminishing property of the
original theta convolution kernel. That route would erase all transform
zeros, including the zeros we need to realize spectrally.

The correct location remains the nonlinear logarithmic resolvent

\`R_Xi(x)=d/dx log Xi(i sqrt(x))\`.

Under RH this is Stieltjes even though \`Phi\` is not Pólya-frequency. Thus
the source boundary must create positivity after logarithmic differentiation
and squared-variable passage, not before Fourier/Mellin transformation.

This also sharpens the categorical requirement: the missing operation is not
an ordinary positive convolution, reflection, or compression functor. It must
behave like a connected/logarithmic or primitive extraction turning the theta
partition function into its positive spectral resolvent.

## Scope

This falsifies full translation-kernel total positivity for the Riemann theta
kernel. It does not exclude weaker finite-order total positivity or positivity
of the derived Pick/Stieltjes kernels.

Primary references:

- I. J. Schoenberg,
  [On Totally Positive Functions, Laplace Integrals and Entire Functions of
  the Laguerre–Pólya–Schur Type](https://pmc.ncbi.nlm.nih.gov/articles/PMC1078971/).
- Belton, Guillot, Khare, and Putinar,
  [Totally positive kernels, Pólya frequency functions, and their
  transforms](https://arxiv.org/abs/2006.16213).
