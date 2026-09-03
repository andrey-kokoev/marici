# Correction: unrestricted scalar prime resonance cost is attained at zero

## Question

Does the fixed-support scalar residual require global interval optimization as stated?

## Claim boundary

This packet audits the residual exactly as defined in the source packet. It does not analyze the support-window operator or a high-frequency-restricted residual.

## Exact maximum

Let

\[
S_L(\xi)=
\sum_{\log n\le2L}
\frac{\Lambda(n)}{\sqrt n}
\cos(\xi\log n)
\]

and

\[
F_L(\xi)=S_L(\xi)-\log(1+\xi),
\qquad \xi\ge0.
\]

Every coefficient is nonnegative, so

\[
S_L(\xi)\le
M_L:=
\sum_{\log n\le2L}
\frac{\Lambda(n)}{\sqrt n}.
\]

Since \(\log(1+\xi)\ge0\),

\[
F_L(\xi)\le M_L.
\]

At \(\xi=0\), every cosine equals one and the logarithm vanishes. Therefore

\[
F_L(0)=M_L
\]

and the sharp unrestricted constant is exactly

\[
C_L^*=M_L.
\]

No branch-and-bound is required for the residual as written.

## Nontrivial replacement

The finite optimization becomes nontrivial only after changing the domain or target, for example

\[
C_L^*(\xi_0)
=
\max_{\xi\ge\xi_0}F_L(\xi),
\qquad \xi_0>0,
\]

or after incorporating the interval overlap/boundary operator rather than the translation-invariant scalar symbol. For the restricted problem,

\[
F_L(\xi)
\le M_L-\log(1+\xi_0)
\]

for all \(\xi\ge\xi_0\), and finite interval certification remains applicable.

## Disposition

The source packet's existence theorem is correct but its proposed global optimization is unnecessary for the stated unrestricted scalar residual. The exact constant \(M_L\) is generally too crude to close positivity. The next meaningful computation must specify a positive high-frequency threshold or use the actual interval operator.

## Verification

- `research/voevodsky/checkers/check_prime_resonance_zero_frequency_correction.py`
- `research/voevodsky/results/prime_resonance_zero_frequency_correction.json`
- `research/grothendieck/prime-resonance-cost-is-a-finite-global-optimization-at-fixed-support.md`
