# The tail constructor forces a four-component Fourier boundary cell

## Question

Does the source-tail operation used by the doubled Green system act inside
the Fourier-stable Gaussian rigging, or does it force another boundary
component?

## The Gaussian witness

Use the self-Fourier Gaussian

\[
\phi(q)=e^{-\pi q^2}
\]

and its right tail

\[
H(q)=\int_q^\infty \phi(v)\,dv
=\frac12\operatorname{erfc}(\sqrt\pi q).
\]

Then

\[
H'(q)=-\phi(q),
\qquad
H(+\infty)=0,
\qquad
H(-\infty)=1.
\]

Thus \(H\) is not in any Gaussian Gelfand–Shilov step. The tail constructor
leaves the bulk rigging even on its canonical vacuum.

## Exact Fourier boundary decomposition

With Fourier convention

\[
\widehat f(\xi)=\int_{\mathbb R}f(q)e^{-2\pi i q\xi}\,dq,
\]

differentiation gives, away from the origin,

\[
2\pi i\xi\widehat H(\xi)=-e^{-\pi\xi^2}.
\]

The reflection identity

\[
H(q)+H(-q)=1
\]

fixes the missing distribution at the origin. Therefore

\[
\widehat H
=
\frac12\delta_0
+
\frac{i}{2\pi}
\operatorname{pv}\left(\frac{e^{-\pi\xi^2}}{\xi}\right).
\]

The tail does not merely add one scalar endpoint. Its Fourier-stable closure
exposes four separately typed pieces:

1. the Gaussian bulk \(\phi\);
2. the one-sided asymptotic carrier \(H\);
3. the Fourier boundary atom \(\delta_0\);
4. the odd principal-value comparison port.

The derivative relates the first two, Fourier transport relates the second
to the last two, and reflection recombines the two tail orientations into
the constant carrier. None of these arrows permits deleting a component.

## Categorical meaning

The Gaussian rigging is a valid bulk object but is not closed under the
source-tail constructor. The minimal repair is not a stronger Gaussian norm.
It is an extension object whose quotient records the asymptotic carrier and
whose Fourier image records both an atomic boundary and an odd comparison
distribution.

This identifies the previously suspected fourth wall. The full moment port
sees the analytic bulk germ, whereas tail incidence creates a boundary
extension class. Fourier saturation of that extension produces two more
comparison coordinates rather than returning to the bulk.

The construction is archimedean and source-native: it follows already from
the theta Gaussian, the tail differential equation, reflection, and Fourier
transport. No zero data or positivity hypothesis enters.

## Consequence for the adelic topology

The combined source cannot be only

\[
\mathcal G\widehat\otimes\mathcal B_{\mathrm{arith}}.
\]

Its archimedean factor must be replaced by a boundary-bearing extension
containing the four components above. Primitive and prime-square currents
must then be tested against that extension, not merely against the Gaussian
bulk. In particular, a scalar endpoint correction or a single Hilbert graph
norm would erase the delta/principal-value distinction.

## Falsifier

Any proposed Fourier-stable domain for the tail constructor fails if it
contains \(\phi\) but omits one of the following consequences:

- the nonzero left asymptote of \(H\);
- the half-delta term in \(\widehat H\);
- the odd principal-value term;
- the reflection relation reconstructing the constant carrier.

## Linear-closure correction

The four items above describe the nonconstant tail decomposition, but they do
not by themselves form a linear Fourier-stable object. Reflection gives

\[
H(q)+H(-q)=1,
\]

and Fourier transform exchanges the newly explicit constant with
\(\delta_0\). Hence a linear closure must retain the constant carrier as a
fifth component. The corrected minimal linear cell is derived in
`the-linear-fourier-tail-cell-has-five-components.md`.

## Result

The first constructor-continuity gate does not close inside the Gaussian
rigging. It first exposes four nonconstant roles, while linear Fourier and
reflection closure forces a fifth constant carrier. Primitive and
prime-square incidence must be tested on that corrected boundary cell.
