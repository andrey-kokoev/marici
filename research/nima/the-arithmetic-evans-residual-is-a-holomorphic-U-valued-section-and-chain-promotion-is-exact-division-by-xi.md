# The arithmetic Evans residual is a holomorphic U-valued section and chain promotion is exact division by Xi

## Question

Once all residual ports are continuously rigged, what is the exact analytic
condition for promotion of the triangular Evans complex into the conservative
three-port complex with multiplicity?

## Claim boundary

The arithmetic residual is a holomorphic \(U_{\rm ar}\)-valued section on the
split wall graph. A divisor-preserving chain promotion exists locally exactly
when that section is divisible by the Xi section. At a zero of order \(m\),
this is equivalent to vanishing of the first \(m\) residual jets. This theorem
identifies the obligation; it does not prove any jet vanishes.

## Holomorphic split history

For every \(z\in\mathbb C\), define the split Evans vector

\[
 \widehat u(z)
 =\bigl(u_-(\cdot;z)|_{(-\infty,0]},
         u_+(\cdot;z)|_{[0,\infty)}\bigr).
\]

Each component is given by a superexponentially convergent source integral.
On every compact parameter set, differentiation under the integral is
permitted to every order. Powers of \(q-r\) introduced by parameter
differentiation are absorbed by theta decay.

Therefore

\[
 z\longmapsto\widehat u(z)
\]

is entire with values in

\[
 H^1(( -\infty,0))\oplus H^1((0,\infty)).
\]

Its wall mismatch is

\[
 \gamma_-\widehat u(z)-\gamma_+\widehat u(z)=\tau(z).
\]

Retaining that mismatch as the wall coordinate makes \(\widehat u\) an entire
section of the split wall graph even away from the Xi divisor. At a zero of
\(\tau\), it descends to the whole-line domain \(H^1(\mathbb R)\).

## Holomorphic arithmetic residual

Let the complete centered incidence adjoint, including its ordinary,
derivative, wall, reciprocal, and ordered-linking ports, be

\[
 \mathcal B^\dagger_G:
 \mathcal H_{G,\rm wall}^{\rm split}\longrightarrow U_{\rm ar}.
\]

The preceding port estimates prove this map bounded on the declared graph.
Define

\[
 r_U(z)=\mathcal B^\dagger_G\widehat u(z).
\]

A bounded linear map sends Banach-valued holomorphic sections to holomorphic
sections. Hence

\[
 r_U:\mathbb C\to U_{\rm ar}
\]

is entire. Compact-local bounds follow from the corresponding split-history
graph bounds.

If a final source comparison alters a port normalization, it changes
\(\mathcal B^\dagger_G\) and this statement must be rechecked. No fitted
comparison is included.

## Local vector-valued division theorem

Let \(z_0\) be a zero of \(\tau\) of order \(m\). Write

\[
 \tau(z)=(z-z_0)^m a(z),
 \qquad a(z_0)\ne0.
\]

For a holomorphic Banach-valued function \(r_U\), the following are equivalent
on a neighborhood of \(z_0\):

1. there is a holomorphic \(h_U\) such that
   \[
   r_U(z)=\tau(z)h_U(z);
   \]
2. \(r_U\) vanishes to order at least \(m\);
3. its first \(m\) jets vanish:
   \[
   r_U^{(j)}(z_0)=0,
   \qquad 0\le j<m.
   \]

To prove the nontrivial direction, expand \(r_U\) in its norm-convergent local
power series. Vanishing of the coefficients below degree \(m\) permits
factorization by \((z-z_0)^m\); multiplication by the scalar unit
\(a(z)^{-1}\) gives \(h_U\). No coordinatewise choice or Riesz identification
is involved.

## Chain interpretation

The triangular Evans complex has wall differential \(\tau\). The conservative
three-port image has the additional arithmetic row \(r_U\). A local chain map
that preserves the Xi module length requires a holomorphic homotopy coefficient
\(h_U\) satisfying

\[
 r_U=\tau h_U.
\]

Thus pointwise cancellation

\[
 r_U(z_0)=0
\]

is sufficient only for a simple zero. For multiplicity \(m>1\), every jet
through order \(m-1\) is required.

This is the precise distinction between kernel inclusion and local-module
length preservation.

## Prime-shell form of every jet

Because the arithmetic source coordinates retain the prime labels, each jet
condition is equivalent to the complete shell family

\[
 \partial_z^j\mathcal S_{p,q}(z_0)=0,
 \qquad 0\le j<m,
\]

for consecutive primes, together with the limiting common-mode condition.
Each shell derivative includes all five declared Green ports.

A single scalar Evans mismatch, a single shell, or only the zeroth residual
cannot establish the divisibility theorem.

## Global division

If the jet conditions hold at every Xi zero with its full multiplicity, define

\[
 h_U(z)=\frac{r_U(z)}{\tau(z)}
\]

away from the divisor. The local division theorem makes every apparent pole
removable. The local extensions agree automatically because they equal the
same quotient on each punctured overlap. Hence they patch uniquely to an
entire \(U\)-valued section on \(\mathbb C\).

Thus global holomorphic division requires no additional overlap cocycle. A
separate growth class, determinant-line trivialization, or invertible-unit
estimate may still be required by the completed Fredholm comparison, but not
by existence of the entire quotient itself.

## Disposition

Rigging turns the G4 promotion problem into exact vector-valued analytic
division:

\[
 r_U\in\tau\,\mathcal O(U_{\rm ar}).
\]

The complete residual-jet family is the remaining local multiplicity gate.
No source identity currently proves it, and no RH conclusion is authorized.
