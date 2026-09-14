# Gaussian damping makes tempered Weil periodization tail-continuous

## Theorem

Let \(T\) be a tempered distribution and let \(\sigma>0\). Then

\[
T_\sigma=e^{-\sigma u^2}T
\]

admits pairing with smooth periodic functions having bounded derivatives through the finite order required by \(T\). Moreover, for every compactly supported smooth \(\phi\),

\[
\left\langle
T_\sigma,
\sum_{k\in\mathbb Z}
\phi\left(u+\frac{2\pi k}{h}\right)
\right\rangle
\longrightarrow
\langle T_\sigma,\phi\rangle
\]

as \(h\) tends to zero.

## Proof

Continuity of a tempered distribution is controlled by finitely many Schwartz seminorms. Differentiating the product of the Gaussian with a translated compact test produces a Gaussian times a polynomial, multiplied by a bounded derivative of the test.

For the nonzero alias indexed by \(k\), its support lies at distance comparable to

\[
\frac{2\pi|k|}{h}
\]

from the origin. Every relevant seminorm is therefore bounded by a term of the form

\[
C(1+|k|/h)^m
\exp\left(-c\sigma k^2/h^2\right).
\]

The sum over nonzero \(k\) converges and tends to zero as \(h\) tends to zero. This proves both existence of the periodic pairing and tail-continuous de-aliasing.

## Consequence for the Weil gate

The completed spectral distribution has polynomial zero-counting growth and is tempered. After multiplication by the fixed positive Gaussian used in the Toeplitz kernel, the tail-continuity hypothesis in the vanishing-spacing theorem is automatic.

Thus the conditional statement sharpens to:

> Assuming the standard source identification with the tempered completed Weil distribution, positivity of every equally spaced Toeplitz rank along any spacing sequence tending to zero is equivalent to positivity of the real-line Weil distribution.

With the standard Weil criterion, this is equivalent to RH.

## Scope

The theorem controls de-aliasing. It does not prove positivity of any circle pushforward. That remains the arithmetic sign problem.

## Verification

```text
python research/voevodsky/checkers/check_gaussian_damping_periodization_tail.py
```

The checker audits polynomial-growth orders through ten and observes Gaussian domination as spacing decreases.

Artifacts:

- `research/voevodsky/checkers/check_gaussian_damping_periodization_tail.py`
- `research/voevodsky/results/gaussian_damping_periodization_tail.json`
