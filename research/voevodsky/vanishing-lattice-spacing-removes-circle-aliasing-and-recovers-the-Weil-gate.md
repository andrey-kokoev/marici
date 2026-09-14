# Vanishing lattice spacing removes circle aliasing and recovers the Weil gate

## Theorem

Fix \(\sigma>0\) and let

\[

ho_\sigma=e^{-2\sigma u^2}\rho.
\]

Assume this Gaussian-damped distribution admits tail-continuous periodization. Let \(h_j>0\) tend to zero. If the circle pushforward of \(\rho_\sigma\) under

\[
u\longmapsto e^{-ih_ju}
\]

is positive for every \(j\), then \(\rho_\sigma\) is positive on the real line.

## Proof

Let \(\phi\) be a nonnegative compactly supported smooth real-line test. For sufficiently small \(h\), its periodization at period \(2\pi/h\) is

\[
P_h\phi(u)
=
\sum_{k\in\mathbb Z}
\phi\left(u+\frac{2\pi k}{h}\right).
\]

This is the pullback of a nonnegative smooth circle test. Positivity of the circle pushforward gives

\[
\langle\rho_\sigma,P_h\phi\rangle
\geq0.
\]

As \(h\) tends to zero, every nonzero translated copy of \(\phi\) escapes to infinity. Gaussian damping and the assumed tail continuity give

\[
\langle\rho_\sigma,P_h\phi\rangle
\longrightarrow
\langle\rho_\sigma,\phi\rangle.
\]

Therefore \(\rho_\sigma\) is nonnegative on every nonnegative compactly supported smooth test and is a positive distribution.

Conversely, a positive real-line distribution has positive pushforward at every spacing.

## RH consequence

Circle positivity at spacing \(h_j\) is equivalent to positivity of every equally spaced Toeplitz rank at that spacing. Hence, at one fixed Gaussian width, the following condition recovers the full real-line positivity target:

> For a sequence \(h_j\to0\), every finite equally spaced source Toeplitz matrix at every spacing \(h_j\) is positive semidefinite.

Because the Gaussian weight is strictly positive, local division removes it. With the standard Weil criterion and exact source normalization, this condition is equivalent to RH.

## One-spacing hostile

A fixed spacing is insufficient. The signed measure

\[
2\delta_0-
\delta_{2\pi/h}
\]

pushes forward to the positive circle measure \(\delta_1\), because its two atoms alias. Smaller generic spacings separate the negative atom and expose the failure.

## Scope

Tail-continuous periodization is an analytic hypothesis that must be checked for the completed source distribution. Gaussian damping makes it natural, but it is not replaced by the finite atomic checker.

## Verification

```text
python research/voevodsky/checkers/check_vanishing_spacing_dealiases_circle_positivity.py
```

Artifacts:

- `research/voevodsky/checkers/check_vanishing_spacing_dealiases_circle_positivity.py`
- `research/voevodsky/results/vanishing_spacing_dealiases_circle_positivity.json`
