# Random Euler products cross half density but erase Weil polarization

## Positive random carrier

Let \(X_p\) be independent Haar-uniform variables on the unit circle. The random Euler logarithm

\[
\sum_p\sum_{k\ge1}
\frac{X_p^k}{k p^{k\sigma}}
\]

has square-summable primitive coefficients whenever

\[
\sum_p p^{-2\sigma}<\infty,
\]

hence for \(\sigma>1/2\). This allows almost-sure or probabilistic random Euler-product constructions substantially left of the deterministic absolute-convergence line \(\sigma>1\).

At the critical boundary, cutoff fields are log-correlated and—after subtracting divergent variance and exponentiating—lead to Gaussian multiplicative-chaos constructions. The probability literature therefore supplies genuine positive measures where the unrandomized compound-Poisson jump measure from the previous packet diverges.

Relevant external lineages include Bohr--Jessen value distributions, random Euler products, Selberg-type central-limit models, and the Saksman--Webb zeta multiplicative-chaos programme. The indexed local PDF corpus contains none of this literature; web metadata search was intermittently unavailable, but the theorem architecture is standard and no claim of a Weil factorization was located.

## Exact cross-prime mismatch

Randomization changes the observer. For distinct primes and independent Haar phases,

\[
\mathbb E\left|aX_p+bX_q\right|^2
=|a|^2+|b|^2,
\]

because

\[
\mathbb E(X_p\overline{X_q})=0.
\]

The deterministic character selected by the Weil observer has

\[
X_p=e^{-i\xi\log p},
\qquad
X_q=e^{-i\xi\log q},
\]

and therefore

\[
\left|
a e^{-i\xi\log p}+b e^{-i\xi\log q}
\right|^2
=|a|^2+|b|^2
+2\operatorname{Re}
\left(a\overline b e^{-i\xi(\log p-\log q)}\right).
\]

The cross-prime polarization is not noise. It changes sign with \(\xi\) and is part of the terminal composite Gaussian square.

For \(a=1/2,b=1/3\), independent phase averaging gives \(13/36\). Deterministic aligned phases give \(25/36\), while opposed phases give \(1/36\). The erased cross term has magnitude \(1/3\).

## Why Bohr--Jessen averaging does not repair this

Kronecker--Bohr equidistribution identifies long averages over the vertical parameter with Haar averages on every finite prime torus. It does not identify a fixed character value with that average.

Thus random Euler measures can represent:

- vertical value distributions;
- averaged moments;
- prime-diagonal covariance;
- typical or almost-sure cutoff behavior.

They cannot directly represent:

- the pointwise shifted-Gaussian kernel at each \(\xi\);
- its cross-prime phase polarization;
- universal rung-four positivity for every deterministic composite primitive.

A concentration theorem is also insufficient: universal positivity concerns worst-case characters, and prime phases can align adversarially on any finite set.

## Critical multiplicative chaos boundary

Variance renormalization at \(\sigma=1/2\) removes a scalar diagonal divergence. It does not restore the erased off-diagonal deterministic phase matrix. Multiplicative chaos is positive because it exponentiates a randomized real field relative to a reference measure; the completed Weil observer is a signed deterministic linear functional with endpoint and gamma cancellation.

Any proposed crossing must therefore condition or disintegrate the random carrier back to every deterministic character while preserving positivity. Point-mass conditioning on one infinite phase configuration is singular with respect to Haar product measure and has no uniform positive-density bound.

## Disposition

Random Euler products solve a different positivity problem. They bypass absolute convergence through probabilistic orthogonality, precisely the operation forbidden by the coupled terminal scalar observer. They provide useful diagonal majorants and typical-value controls, but not the missing form-preserving map on composite Gaussian primitives.

## Verification

```text
python research/voevodsky/checkers/check_random_Euler_carrier_erases_deterministic_cross_prime_polarization.py
```

Artifacts:

- `research/voevodsky/checkers/check_random_Euler_carrier_erases_deterministic_cross_prime_polarization.py`
- `research/voevodsky/results/random_Euler_carrier_erases_deterministic_cross_prime_polarization.json`
