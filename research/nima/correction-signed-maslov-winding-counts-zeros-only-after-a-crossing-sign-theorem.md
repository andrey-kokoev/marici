# Correction: signed Maslov winding counts zeros only after a crossing-sign theorem

The previous winding criterion omitted a necessary orientation condition. The Riemann--von Mangoldt function counts zeros with nonnegative multiplicity. A Maslov index is a signed crossing count.

If the relative boundary lines cross forward and backward, the signed Maslov index can exhibit cancellations:
\[
\operatorname{Maslov}
=
N_{+}-N_{-},
\]
while the zero count is
\[
N=N_{+}+N_{-}
\]
after multiplicities are included.

Therefore the claim
\[
\operatorname{Maslov}=N
\]
requires every regular crossing to have the same sign, or a more general theorem identifying the algebraic divisor orientation with the chosen Maslov convention.

For a standard self-adjoint boundary triple in a spectral gap, monotonicity is available. The Weyl identity gives
\[
M'(x)
=
\gamma(x)^{*}\gamma(x)\ge0.
\]
For a constant self-adjoint boundary condition
\[
F(x)=\Theta-M(x),
\]
the crossing form on
\[
b\in\ker F(x_0)
\]
is
\[
\mathfrak q_{x_0}(b)
=
\langle b,F'(x_0)b\rangle
=
-\|\gamma(x_0)b\|^{2}.
\]
If \(\gamma(x_0)\) is injective on the kernel, the crossing form is strictly negative. Every crossing is regular and has the same orientation.

This yields three consequences:

1. the signed spectral flow equals the unsigned eigenvalue count;
2. the zero order equals kernel dimension at regular crossings;
3. tangential hostiles are excluded by a source norm.

The continuous-spectrum dark-line regime is harder. At a seam crossing,
\[
b(x)\in\ker \operatorname{Im}M_{+}(x),
\]
and the relevant derivative is the compressed reactive form
\[
\mathfrak q_{x_0}(b)
=
\left\langle
b,
\frac{d}{dx}
\left(
\Theta-\operatorname{Re}M_{+}(x)
\right)_{x=x_0}
b
\right\rangle,
\]
including the derivative induced by the moving dark line. Positivity of the bulk spectral measure does not automatically fix its sign.

Hence the winding audit must branch:

- Gap or compact-resolvent regime:
  use Weyl monotonicity directly.
- Embedded dark-state regime:
  derive a reduced crossing form after Feshbach projection onto \(\ker W(x)\).
- No sign theorem:
  use the argument principle or absolute local intersection multiplicities, not the signed Maslov index.

For the rank-two, rank-one-radiation model, let \(d(x)\) be a normalized dark vector. The reduced scalar reactive function is
\[
\rho(x)
=
\left\langle
d(x),
\left(
\Theta-\operatorname{Re}M_{+}(x)
\right)d(x)
\right\rangle.
\]
A simple zero requires
\[
\rho(x_0)=0,
\qquad
\rho'(x_0)\neq0.
\]
A one-sign crossing theorem requires
\[
\rho'(x_0)
\]
to have the same sign at every zero.

This derivative includes
\[
2\operatorname{Re}
\left\langle
d'(x),
(\Theta-\operatorname{Re}M_{+}(x))d(x)
\right\rangle,
\]
which vanishes at a crossing only if the full operator sends \(d(x_0)\) to zero, not merely if its expectation vanishes. The operator kernel condition must therefore be retained.

The next high-information theorem is:

> The source Green identity identifies the reduced crossing form with a positive state norm on every closed seam state.

That would recover monotone spectral flow even in the embedded regime.

The smallest hostile reproduces the correct number of unsigned intersections but alternates crossing signs. Its Maslov index remains bounded while \(N(T)\) grows.

A second hostile proves \(M'(x)\ge0\) off the continuous spectrum and applies it without justification to boundary values inside the spectrum.

A third hostile checks only \(\rho(x_0)=0\) as a scalar expectation while
\[
(\Theta-\operatorname{Re}M_{+}(x_0))d(x_0)\neq0.
\]

Thus the corrected asymptotic gate is:

\[
\text{Riemann--von Mangoldt count}
=
\begin{cases}
\text{signed Maslov index},&\text{after one-sign crossing proof},\\
\text{absolute intersection count},&\text{otherwise}.
\end{cases}
\]

The missing source calculation is now the crossing form, not merely the line winding.
