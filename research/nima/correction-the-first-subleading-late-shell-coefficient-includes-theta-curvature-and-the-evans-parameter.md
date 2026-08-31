# Correction: the first subleading late-shell coefficient includes theta curvature and the Evans parameter

## Question

Is the previously stated relative correction \(-1/(2\Lambda)\) for the combined
reciprocal/linking response valid for the completed theta forcing?

## Claim boundary

No. That coefficient retained the leading ordinary overlap but omitted the
first curvature correction in the Evans endpoint integral and the explicit
Evans parameter. For the completed theta tail, \(\Lambda'/\Lambda^2\) is itself
of relative order \(1/\Lambda\), so it contributes at the same order. The
correct zeroth-jet benchmark is derived below. Higher jets require a separate
curvature-aware expansion.

## Completed-tail rates

Let

\[
 \Lambda(a)=-\frac{\Phi'(a)}{\Phi(a)}.
\]

First-label dominance gives

\[
 \Lambda(a)=2\pi e^{2a}-\frac92+O(e^{-2a}),
\]

and

\[
 \Lambda'(a)=4\pi e^{2a}+O(e^{-2a}).
\]

Hence

\[
 \varepsilon(a)
 :=\frac{\Lambda'(a)}{\Lambda(a)^2}
 =\frac{2}{\Lambda(a)}+O(\Lambda(a)^{-2}).
\]

The slow-variation ratio tends to zero, but not fast enough to be omitted from
the first relative correction.

## Evans endpoint expansion

For fixed \(z\) in a compact set,

\[
 u_z(a)
 =-\int_0^\infty e^{-zs}\Phi(a+s)\,ds.
\]

Endpoint Laplace expansion gives

\[
 u_z(a)
 =-\frac{\Phi(a)}{\Lambda(a)}
 \left[
 1-\frac{z}{\Lambda(a)}
 -\frac{\Lambda'(a)}{\Lambda(a)^2}
 +O(\Lambda(a)^{-2})
 \right].
\]

Using \(\varepsilon=2/\Lambda+O(\Lambda^{-2})\), the lower-end contribution to
the endpoint shell is

\[
 I^{({\rm end})}(z)
 =\frac{\Phi(a)^2}{\Lambda(a)}
 \left[
 1-\frac{z+2}{\Lambda(a)}
 +O(\Lambda(a)^{-2})
 \right].
\]

The upper endpoint is superexponentially smaller on a late consecutive-prime
shell.

## Ordinary overlap expansion

Set \(s=y/\Lambda(a)\). Then

\[
 \frac{\Phi(a+s)^2}{\Phi(a)^2}
 =e^{-2y}
 \left[1-\varepsilon(a)y^2+O(\Lambda(a)^{-2})\right],
\]

and the variation of \(1/\Lambda(a+s)\), together with the Evans endpoint
correction, contributes

\[
 1-\frac{z}{\Lambda(a)}
 -\varepsilon(a)(1+y+y^2).
\]

Using

\[
 \int_0^\infty e^{-2y}\,dy=\frac12,
 \quad
 \int_0^\infty ye^{-2y}\,dy=\frac14,
 \quad
 \int_0^\infty y^2e^{-2y}\,dy=\frac14,
\]

one obtains

\[
 I^{(0)}(z)
 =-\frac{\Phi(a)^2}{2\Lambda(a)^2}
 \left[
 1-\frac{z+4}{\Lambda(a)}
 +O(\Lambda(a)^{-2})
 \right].
\]

Only its leading term affects the combined shell through relative order
\(1/\Lambda\).

## Correct zeroth-jet benchmark

Adding the ordinary and endpoint terms gives

\[
 I^{(0)}(z)+I^{({\rm end})}(z)
 =\frac{\Phi(a)^2}{\Lambda(a)}
 \left[
 1-\frac{z+5/2}{\Lambda(a)}
 +O(\Lambda(a)^{-2})
 \right].
\]

Therefore candidate one requires

\[
 I^{({\rm recip})}(z)+I^{({\rm link})}(z)
 =-\frac{\Phi(a)^2}{\Lambda(a)}
 \left[
 1-\frac{z+5/2}{\Lambda(a)}
 +O(\Lambda(a)^{-2})
 \right]
\]

under the frozen unit port coefficients.

## Correction to the previous hostile

`the-reciprocal-linking-shell-must-match-a-two-term-asymptotic-not-only-the-leading-endpoint-flux.md`

stated the relative coefficient \(-1/2\) without the \(z\) and theta-curvature
terms. That coefficient must not be used for candidate-one rejection or SCC
mutation.

The leading endpoint dominance and the necessity of a subleading bulk
correction remain valid.

## Multiplicity warning

Differentiating the corrected expansion introduces derivatives of the explicit
\(z\) term as well as the factorial endpoint hierarchy. A jet-order-independent
relative coefficient is therefore not established. Each fixed jet must be
recomputed from the curvature-aware endpoint expansion or, preferably, from an
entire source identity.

## Disposition

The late-shell hostile survives but its first subleading coefficient is
corrected to \(-(z+5/2)\) inside the combined zeroth-jet bracket. The previously
reported universal \(-1/2\) coefficient is retracted. Exact reciprocal/linking
comparison remains open. No RH conclusion is authorized.
