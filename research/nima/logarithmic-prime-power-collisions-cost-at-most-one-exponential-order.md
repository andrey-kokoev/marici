# Logarithmic prime-power collisions cost at most one exponential order

## Question

Does the nonuniform spacing of the signed logarithmic prime-power displacements rule out continuous recovery in the projective exponential topology?

## Claim boundary

No by spacing alone. Distinct prime powers can approach in logarithmic coordinate, so no uniform separation or Hilbert interpolation bound exists. But the inverse gap grows at most exponentially in the displacement. The projective source contains every exponential order, so this geometric conditioning cost is admissible there. The unresolved estimate is deconvolution by the completed-theta atom, not displacement separation.

## Displacement set

Write every positive displacement as

\[
L_n=\log n,
\]

where \(n=p^k\) is a prime power. For two distinct prime powers \(m<n\),

\[
L_n-L_m=\log\frac nm
=\log\left(1+\frac{n-m}{m}\right).
\]

Since \(n-m\ge1\),

\[
L_n-L_m
\ge\log\left(1+\frac1m\right).
\]

Using \(\log(1+x)\ge x/(1+x)\) gives

\[
L_n-L_m\ge\frac1{m+1}\ge\frac1{n+1}.
\]

Therefore, for \(L_n\ge0\),

\[
\frac1{|L_n-L_m|}
\le n+1
=e^{L_n}+1
\le2e^{L_n}.
\]

The same estimate holds on the negative branch, and opposite signs are separated by at least \(2\log2\).

## Consequence for local interpolation

Any local coordinate extractor whose norm grows polynomially in the inverse nearest-neighbour gap incurs at most a finite exponential-order loss. For example, a first-order separation cost obeys

\[
\operatorname{cost}(L_n)
\le C e^{L_n}.
\]

Such a loss is continuous on the projective coefficient topology because

\[
q_\delta(e^Lc)
=q_{\delta+1}(c).
\]

Higher fixed powers of the inverse gap consume correspondingly higher but still finite exponential order. Thus clustering of logarithmic prime powers does not by itself obstruct a projective recovery map.

## Hilbert failure remains

There is no positive uniform gap. Consecutive primes have ratios tending to one, so logarithmic prime displacements approach each other. Translation differences then produce nearly dependent vectors in ordinary Hilbert history norms. Hence this estimate does not restore a uniform Hilbert frame bound.

## The remaining deconvolution gate

The common history is

\[
h=\Phi*\mu_c
\]

up to the fixed translation convention, and

\[
\widehat h=\widehat\Phi\,\widehat\mu_c.
\]

Spacing controls interpolation of \(\mu_c\) after that measure has been recovered. Quantitative recovery from \(h\) also requires a continuous division or parametrix for \(\widehat\Phi\) on the range of these exponential sums. Zeros or rapid smallness of \(\widehat\Phi\) can dominate the one-order spacing cost.

A valid proof may use a source-derived frequency window on which \(\widehat\Phi\) is bounded away from zero, together with an interpolation theorem for exponential sums restricted to that window. It may not choose a window after inspecting the coefficient packet or Xi zeros.

## Direction rescore

- Spacing obstruction in projective topology: eliminated.
- Exact spacing cost: completed, at most one exponential order for first-order separation.
- Uniform Hilbert interpolation: 0/10.
- Quantitative theta deconvolution plus exponential-sum interpolation: 9/10.
- Algebraic Fourier faithfulness: already completed.

## Disposition

The displacement geometry is compatible with projective recovery. The next depth-first gate is the theta deconvolution estimate: find a fixed source-authorized Fourier interval with a quantitative lower bound for \(|\widehat\Phi|\), then bound coefficient interpolation from the exponential sum on that interval. No RH conclusion is authorized.
