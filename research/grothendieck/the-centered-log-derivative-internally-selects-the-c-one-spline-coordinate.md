# The centered log derivative internally selects the c=1 spline coordinate

## Question

Can the canonical spline scale be fixed without treating dilation covariance itself as source authority?

## Centered Euler coordinate

Set

\[
s=\frac12+z.
\]

In the Euler half-plane, the Dirichlet-series part of the completed logarithmic derivative is

\[
-\sum_{n\ge2}\Lambda(n)n^{-s}
=-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}e^{-z\log n}.
\]

Therefore the Laplace coordinate dual to the centered variable `z` is exactly

\[
x=\log n.
\]

If the stored spline profile is the logarithmic test `phi(x)`, the prime cell must evaluate `phi(log n)`. Evaluating `phi(log n/2)` would instead replace the source coordinate by a dilation.

## Gamma coordinate

The completed gamma factor contributes

\[
\frac12\psi\!\left(\frac14+\frac z2\right)-\frac12\log\pi.
\]

Using

\[
\psi(a)= -\gamma+\int_0^\infty
\frac{e^{-x}-e^{-ax}}{1-e^{-x}}\,dx
\]

in its regularized form, the argument `a=1/4+z/2` produces the same logarithmic variable after the even-test pairing combines the two centered directions. The resulting repository archimedean cell has the form

\[
-(\gamma+\log\pi)\phi(0)
+
\int_0^\infty
\frac{\phi(0)e^{-x}-\phi(x)e^{-x/4}}{1-e^{-x}}\,dx.
\]

The profile is `phi(x)`, not `phi(x/2)`. Introducing `phi(x/2)` changes the test to `D_{1/2}phi` and simultaneously requires prime samples at `phi(log n/2)`.

## Internal normalization result

Relative to the declared centered spectral coordinate `z=s-1/2` and the Euler identity `n^{-s}=n^{-1/2}e^{-z log n}`, the repository convention selects `c=1` internally. This is not a claim that dilation by another `c` is invalid; it says that every cell must then be dilated together.

The exact consistency chain is

\[
s-\frac12=z
\longmapsto e^{-z\log n}
\longmapsto x=\log n
\longmapsto \phi(x).
\]

This chain rules out the mixed implementation `P(D_1 phi)+A(D_{1/2}phi)` independently of numerical behavior.

## Hostile checks

A repaired implementation must fail each of these mutations:

1. keep prime samples at `phi(log n)` while replacing the gamma profile by `phi(x/2)`;
2. use the gamma substitution `u=x/2` without changing both its Jacobian and exponential parameter;
3. dilate prime and gamma cells but leave endpoint or pole characters undilated;
4. reverse the completed prime sign.

## Claim boundary

This derivation fixes the repository's internal coordinate once `s=1/2+z` and the displayed completed logarithmic derivative are admitted. It does not supply bibliographic provenance for that completed explicit formula, directed numerical enclosures, positivity of any translate Gram family, or global Weil positivity.

## Disposition

Use `c=1` for the repaired spline certificate. The remaining source-provenance task is narrower than scale selection: attach a published theorem to the already fixed completed explicit formula. The next executable numerical task is directed enclosure of the `c=1` archimedean moments with the four hostile mutations above retained.
