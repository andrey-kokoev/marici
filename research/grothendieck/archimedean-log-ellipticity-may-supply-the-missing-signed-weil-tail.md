# Archimedean log-ellipticity may supply the missing signed Weil tail

## Question

Can the high-mode complement of a fixed-support Weil operator be proved nonnegative, rather than merely small in norm?

## Principal-symbol comparison

On a fixed logarithmic support window, the completed source form has three analytic orders:

1. the archimedean multiplier satisfies
   `Re psi(1/4+iu/2)=log|u|+O(1)` and is eventually positive;
2. the prime contribution is a finite sum of bounded translation pairings, hence order zero with explicit norm `C_prime(L)`;
3. the endpoint contribution is finite rank.

Therefore the archimedean sector is logarithmically elliptic relative to the bounded prime sector. In an ideal frequency-diagonal model, every mode above

`log|u| > C_prime(L)+C_gamma`

has positive total quadratic energy, apart from the finite-rank endpoint correction.

## Exact periodic fixture

On a circle, Fourier modes diagonalize the archimedean multiplier and each translation. For mode `n`, the prime contribution is a bounded trigonometric sum whose absolute value is at most the sum of the absolute prime coefficients. Hence

`q(n) >= log|n|-C_gamma-C_prime(L)`.

All sufficiently large modes are positive. In that fixture, positivity of the full operator reduces to a finite matrix after the threshold.

## Interval obstruction

The actual core is compactly supported on an interval, not periodic. Dirichlet sine projection does not strictly localize the zero-extended Fourier transform, and multiplication by the support cutoff creates boundary/commutator errors. Consequently the periodic inequality is not yet a theorem for `H_0^s((-L,L))`.

The required analytic result is a logarithmic Gårding estimate on the high Dirichlet subspace:

`Gamma_L(f,f) >= [c log M-C_L] ||f||_2^2`

for `f` orthogonal to the first `M` modes, with explicit `c>0` and `C_L`. Combining it with

`|P_L(f,f)| <= C_prime(L)||f||_2^2`

would make the tail block nonnegative once `c log M>=C_L+C_prime(L)`. Endpoint representers can be included in the finite trial space, eliminating their pure-tail block.

## Off-diagonal gate

Tail-block positivity alone is insufficient if the finite/tail off-diagonal block is nonzero. The final certificate needs either:

- a Schur estimate against a strictly positive finite block;
- a trial space invariant under the source operator;
- or an exact completion of squares pairing the off-diagonal terms with tail reserve.

Because the compact operator has eigenvalues accumulating at zero, the finite block may itself have very small positive pivots. The Schur budget must be certified rather than inferred from high-frequency positivity.

## Why this is nonredundant

Unsigned compactness could only certify negative spectrum. Log-ellipticity is sign-sensitive and can, in principle, prove that no negative eigenvalue lies beyond a computable mode threshold. It moves the positivity problem back to finitely many modes for each fixed support `L`, provided the interval Gårding and off-diagonal estimates are proved.

## Global limitation

The prime norm `C_prime(L)` grows with the support window because more prime powers enter. The threshold may therefore diverge rapidly with `L`. Even a successful theorem for every fixed `L` does not reduce RH to one finite computation; it creates a countable family of finite-but-growing certification problems unless a uniform arithmetic pattern is found.

## Disposition

The missing signed tail has a plausible source: eventual positivity of the archimedean logarithmic symbol dominating bounded fixed-support prime translations. The next exact theorem is an explicit high-Dirichlet-mode logarithmic Gårding inequality with boundary constants.
