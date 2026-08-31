# The late-prime-shell autocorrelation is superexponentially dominated by the first completed-theta label pair

## Question

Does the exact ordered-pair expansion simplify on late consecutive-prime
shells in a source-controlled way?

## Claim boundary

Yes. On shells whose lower endpoint \(a\) tends to infinity, the \((1,1)\)
completed-theta pair dominates every other ordered label pair by a factor
superexponentially small in \(e^{2a}\), locally uniformly in the separation
coordinate. This reduces the late-shell hostile to one explicit
incomplete-gamma kernel. It does not prove exact cancellation at finite shells.

## Label tail

For

\[
 \Phi_n(u)
 =e^{u/2}
 \left(2\pi^2n^4e^{4u}-3\pi n^2e^{2u}\right)
 e^{-\pi n^2e^{2u}},
\]

the exponential ratio against the first label is

\[
 \exp\!\left[-\pi(n^2-1)e^{2u}\right].
\]

The polynomial prefactor grows only polynomially in \(n\) and \(e^u\).
Therefore, for \(u\ge a\) and \(n\ge2\),

\[
 \frac{|\Phi_n(u)|}{|\Phi_1(u)|}
 \le P_n(e^u)
 e^{-3\pi e^{2a}},
\]

away from the finite transition region where the first-label polynomial
changes sign. Every late prime shell lies beyond that region.

## Ordered-pair suppression

For separation \(t\ge0\), the pair exponential is

\[
 \exp\!\left[
 -\pi\left(n^2+m^2e^{2t}\right)e^{2u}
 \right].
\]

Relative to \((1,1)\), every pair \((n,m)\ne(1,1)\) contains

\[
 \exp\!\left[
 -\pi\left((n^2-1)+(m^2-1)e^{2t}\right)e^{2u}
 \right].
\]

At least one integer difference is at least three. Hence on \(u\ge a\), every
nonfirst pair has a superexponential penalty. Polynomial label factors and the
theta sum do not compensate for it.

For each compact separation interval \(0\le t\le T\),

\[
 \rho_{a,b}(t)
 =d_1^2\rho_{11}^{[a,b]}(t)
 \left(1+O_T(e^{-3\pi e^{2a}}\,P_T(e^a))\right),
\]

where \(P_T\) denotes a fixed polynomial bound and \(d_1\) is the
source-normalized first theta coefficient.

## Large-separation tail

For \(t>T\), even the first pair contains

\[
 e^{-\pi e^{2(u+t)}}.
\]

Thus its separation tail is double-exponentially small. The nonfirst pairs
have at least the same tail decay. Splitting the Laplace integral at fixed
\(T\), then increasing \(T\), transports first-pair dominance to the ordinary
shell transform uniformly for \(z\) in compact sets.

## First-pair kernel

For \((n,m)=(1,1)\),

\[
 A=\pi,
 \qquad
 C=\pi e^{2t},
 \qquad
 \lambda=\pi(1+e^{2t}).
\]

The exact density is the previously constructed three-term
incomplete-gamma expression with these coefficients and endpoints
\(e^{2a},e^{2b}\).

Consequently

\[
 I_{a,b}^{(0)}(z)
 =-d_1^2\int_0^\infty
 e^{-zt}\rho_{11}^{[a,b]}(t)\,dt
 +\text{superexponentially smaller label tail}.
\]

## Relation to endpoint asymptotics

The first completed label also controls

\[
 \Lambda(a)=-\frac{\Phi'(a)}{\Phi(a)}
 \sim2\pi e^{2a}.
\]

Thus the earlier two-term late-shell hierarchy is source-consistent with the
first-pair kernel rather than with the retracted additive-Gaussian model.

## Hostile use

Any proposed reciprocal/linking response whose first-label-pair density has
the wrong leading or first subleading coefficient fails candidate one on all
sufficiently late prime shells. Higher labels cannot repair that mismatch,
because their combined contribution is superexponentially smaller.

## Disposition

Late-shell candidate one reduces asymptotically to the exact \((1,1)\)
incomplete-gamma density. This supplies a corrected source-specific hostile for
reciprocal/linking proposals. Exact finite-shell and multiplicity cancellation
remain open. No RH conclusion is authorized.
