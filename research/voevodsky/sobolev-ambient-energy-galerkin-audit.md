# Sobolev ambient energy and Galerkin control

## Question

Does the fixed-support Sobolev factorization provide a noncircular energy and quantitative finite-mode control for local Weil operators?

## Claim boundary

This packet verifies the factorization consequences and exact tail-rate formula conditional on the source norm \(\lVert B_{L,r}\rVert\). It does not supply the missing source constants or prove positivity.

## Ambient factorization

For fixed support window \((-L,L)\) and \(0<r<s\), the source construction gives

\[
A_{L,s}=J_{s,r}^{*}B_{L,r}J_{s,r},
\]

where \(B_{L,r}\) is bounded and \(J_{s,r}:H_0^s\to H_0^r\) is compact. This construction is independent of RH and therefore supplies an admissible local ambient norm.

For the first-\(M\)-mode sine projection \(P_M\),

\[
\lVert J_{s,r}(I-P_M)\rVert
\le
\left[1+\left(\frac{\pi(M+1)}{2L}\right)^2\right]^{-(s-r)/2}.
\]

Hence

\[
\lVert A_{L,s}-P_MA_{L,s}P_M\rVert
\le
2\lVert B_{L,r}\rVert
\left[1+\left(\frac{\pi(M+1)}{2L}\right)^2\right]^{-(s-r)/2}
\]

under the declared compression convention, with a smaller quadratic correction available from the full expansion.

For \(r=1/2\), \(s=1\), the bound decays as \(M^{-1/2}\). The checker verifies strict decrease symbolically and records exact expressions at selected cutoffs.

## What the bound certifies

Norm convergence gives a one-sided falsifier. If a finite compression has a negative eigenvalue whose magnitude exceeds the tail bound, the full operator has negative spectrum. Positive finite compressions do not prove full positivity because the extended compression has zero on its complement.

The checker exhibits a hostile diagonal operator whose first \(M\) modes are positive while an unresolved tail mode is negative within the norm error. Compactness alone therefore supplies falsification, not verification.

## Remaining source constants

An executable local certificate still requires:

1. fixed Fourier and Sobolev normalization;
2. explicit endpoint, digamma, and prime-term bounds for \(\lVert B_{L,r}\rVert\);
3. interval enclosures for the Galerkin matrix;
4. endpoint-representer augmentation;
5. a signed-tail or Schur argument for positivity.

## Disposition

The fixed-support Sobolev construction is a noncircular local energy and supplies uniform finite-mode approximation rates once \(\lVert B_{L,r}\rVert\) is sourced. It repairs the ambient-energy problem locally but does not yield global support-window coercivity or RH-bearing positivity.

## Verification

- `research/voevodsky/checkers/check_sobolev_ambient_energy_galerkin.py`
- `research/voevodsky/results/sobolev_ambient_energy_galerkin.json`
- `research/grothendieck/sobolev-gap-gives-computable-galerkin-tail-rates-for-local-weil-operators.md`
