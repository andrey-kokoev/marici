# Final gate audit: rank compression does not close global Weil positivity

## Closed technical subgates

- Directed rank-160 two-prime compression at `L=0.55` is positive.
- The gamma comparison has directed upper constant `2.6947343671`.
- The finite-interval logarithmic image decomposition has an explicit boundary
  budget `pi/sqrt(3)+log(2)-3/8` under the recorded Fourier normalization.
- Prime-power event bookkeeping and coercive-tail thresholds are explicit.
- The prime-channel triangle strategy has proved asymptotic rank cost
  `M(L)=exp((4+o(1))exp(L))`.

## Gates not closed

1. The rank-160 Legendre block is not nested with the Dirichlet high-mode
   projection. It does not certify the first 51,677 Dirichlet modes and their
   endpoint couplings at `L=0.55`.
2. No certified finite-dimensional calculation covers that coupled space.
3. Across increasing support, separate prime-channel norm bounds lose the
   signed arithmetic cancellation and force double-exponential rank growth.
4. No uniform form-core convergence theorem with a positive lower margin has
   been established.
5. Consequently global Weil positivity has not been proved.
6. The transfer to a global Loewner/co-defect inequality cannot be invoked,
   because its positivity hypothesis is absent.

## Logical endpoint

Global Weil positivity for all compactly supported tests is a standard
formulation equivalent to the Riemann hypothesis. The current artifacts are
finite-window certificates and comparison bounds; promoting them to all
supports without a new cancellation theorem would amount to supplying the
missing RH-level argument.

The present norm-subtraction/compression branch is exhausted: increasing rank
or adding prime channels under the same triangle inequality cannot close the
support limit. A nonredundant continuation requires a new theorem preserving
signed cancellation in the full prime kernel, not another parameter increase.
