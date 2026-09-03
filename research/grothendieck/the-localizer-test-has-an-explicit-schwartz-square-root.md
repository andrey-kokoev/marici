# The localizer test has an explicit Schwartz square root

## Question

Is the Gaussian localizer test merely pointwise nonnegative, or does it belong to the convolution-square class of the classical Weil criterion?

## Smooth spectral factor

For `h>0`, define on the real spectral axis

\[
q_h(u)
=u\left(\frac{1-e^{-hu^2}}{u^2}\right)^{1/2},
\]

with the quotient extended at zero by the value `h`. The factor in parentheses is positive, even, and smooth on the real line. Hence `q_h` is a smooth odd function and

\[
|q_h(u)|^2=1-e^{-hu^2}.
\]

For a polynomial `p_c`, put

\[
G_{t,h,c}(u)
=e^{-tu^2/2}q_h(u)p_c(e^{-hu^2}).
\]

Gaussian decay makes `G_(t,h,c)` a Schwartz function. Its squared modulus is exactly

\[
|G_{t,h,c}(u)|^2
=e^{-tu^2}(1-e^{-hu^2})
|p_c(e^{-hu^2})|^2.
\]

## Convolution-square realization

Let `g_(t,h,c)` be the inverse Fourier transform of `G_(t,h,c)`. Then `g` is Schwartz and

\[
\widehat{g*g^*}(u)=|G_{t,h,c}(u)|^2.
\]

Therefore the sampled heat localizer form is an actual Weil convolution square:

\[
Q_{t,h}(c)=W(g_{t,h,c}*g_{t,h,c}^*),
\]

with the Fourier convention fixed by the completed heat explicit formula.

This supplies the missing source map

\[
(t,h,c)\longmapsto g_{t,h,c}
\]

before positivity. It does not use GNS or a positive moment measure.

## Mesh behavior

The factor obeys the exact refinement identity

\[
1-e^{-(h_1+h_2)u^2}
=(1-e^{-h_1u^2})
+e^{-h_1u^2}(1-e^{-h_2u^2}).
\]

Thus squared localizer tests split additively under mesh composition. At the amplitude level this is an orthogonal two-channel dilation, not a scalar multiplicative identity for `q_h`.

Any proposed source factorization should preserve this two-channel refinement rather than choose unrelated square roots at each mesh.

## Boundary

The exact Fourier normalization and admissible Weil test algebra must be checked against the repository's completed explicit-formula convention. This construction proves membership in the Schwartz convolution-square class; it does not prove the Weil form is positive on that class.

## Disposition

Use `G_(t,h,c)` as the canonical pre-positivity embedding of sampled localizer packets into the Weil criterion. This replaces the abstract phrase “Gaussian-square family” by an explicit source map and a testable mesh-refinement law.