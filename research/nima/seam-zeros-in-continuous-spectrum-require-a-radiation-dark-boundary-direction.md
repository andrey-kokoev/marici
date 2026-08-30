# Seam zeros in continuous spectrum require a radiation-dark boundary direction

The continuous-spectrum interpretation has a stringent compatibility condition.

Let \(M(z)\) be the Weyl function of the reference self-adjoint transport system, and let the closed boundary condition be self-adjoint:
\[
\Theta=\Theta^{*}.
\]
Suppose nontangential boundary values exist at a real seam point \(x\):
\[
M_{+}(x)
=
\lim_{\varepsilon\downarrow0}M(x+i\varepsilon).
\]
The imaginary part
\[
W(x)=\operatorname{Im}M_{+}(x)\ge0
\]
is the boundary spectral-density or radiation form.

If a seam state satisfies
\[
(\Theta-M_{+}(x))b=0,
\]
then taking imaginary parts gives
\[
\langle b,W(x)b\rangle=0.
\]
Since \(W(x)\ge0\),
\[
W(x)^{1/2}b=0.
\]

Therefore every real zero lying inside the absolutely continuous spectrum must occupy a boundary direction dark to the open radiation channels.

This creates a sharp trichotomy:

1. Spectral gap:
   \(W(x)=0\) because \(x\) lies outside the essential spectrum. Ordinary discrete eigenvalues are possible.
2. Threshold or singular point:
   the limiting absorption law degenerates.
3. Embedded state:
   \(W(x)\neq0\) but has a nontrivial kernel containing the resonant boundary vector.

If \(W(x)\) is strictly positive definite on the complete boundary space, then no self-adjoint boundary condition can produce an embedded eigenvalue at \(x\).

This interacts nontrivially with the earlier observability programme. Uniform boundary observability was required only on compact off-seam sets. It cannot remain strictly positive through every seam zero in the continuous-spectrum regime. The intended zero is precisely a controlled loss of radiation observability on the seam.

Thus the correct margins are asymmetric:

- off seam:
  strict Schur defect or positive Weyl imaginary part excludes collisions;
- on seam:
  a rank loss in the radiation form is permitted and must be matched by conservative sewing;
- transverse directions:
  remain observable so the zero has finite multiplicity.

For a rank-two boundary space, a simple seam zero should ideally satisfy
\[
\dim\ker W(x_0)=1,
\]
\[
\ker(\Theta-\operatorname{Re}M_{+}(x_0))
=
\ker W(x_0),
\]
and a nonzero crossing derivative on this common line.

This is a bound-state-in-continuum mechanism: destructive interference cancels all outgoing radiation in one arithmetic boundary combination while the internal state remains nonzero.

The five-margin taxonomy must therefore be read carefully. The mixed-cancellation margin must not forbid the intended seam cancellation. It forbids cancellation on compact off-seam sectors. On the seam, the zero mechanism requires a source-authorized cancellation at the radiation output.

The immediate source test is to compute the rank of
\[
W(x)
=
\operatorname{Im}G_{+}(x)
\]
for the theta-tail return. Possible outcomes:

- full rank almost everywhere: the self-adjoint embedded-zero route is closed;
- rank one with an arithmetic kernel line: a viable seam crossing channel exists;
- identically zero: the boundary return is lossless and the model is effectively discrete at the boundary;
- undefined boundary value: limiting absorption remains the prior gate.

The smallest hostile claims both:

\[
W(x)\ge\varepsilon I
\]
uniformly through the seam, and
\[
(\Theta-M_{+}(x_0))b=0
\]
for a nonzero \(b\). These are algebraically incompatible.

A second hostile finds a kernel of \(W(x)\) for every real \(x\). That supplies too many dark states and makes the zero set depend entirely on a fitted real boundary relation.

This yields a source-specific target:

> The doubled theta-wall system has a one-dimensional radiation-dark boundary line only at the completed arithmetic phase-matching points, while its orthogonal boundary direction remains radiative.

If proven independently of \(\xi\), this would explain zeta zeros as discrete dark-state crossings inside a continuous seam spectrum. If not, the programme must seek hidden compactification or a different relative spectral event.
