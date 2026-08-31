# The exact Evans history lies in the whole-line maximal-isotropic domain without a limiting-absorption limit

## Question

Does the two-sided Evans history require a limiting-absorption theorem merely
to define its seam state and endpoint Green flux?

## Claim boundary

No. Theta superexponential decay and the exact Evans mismatch put every Xi-zero
history, and every parameter-root vector below its local multiplicity, directly
in the whole-line first-order graph domain. This closes the history-block domain
and flux statement. It does not solve the arithmetic adjoint equation, construct
the full conservative Green-kernel state, or prove seam confinement.

## Source class

Let \(\Phi\) be the completed theta forcing. The required source property is

\[
 e^{a|q|}(1+|q|)^N\Phi(q)\in L^1(\mathbb R)\cap L^2(\mathbb R)
\]

for every finite \(a>0\) and integer \(N\ge0\). This is the
superexponential theta estimate already used to make

\[
 \tau(z)=\int_{\mathbb R}e^{-zr}\Phi(r)\,dr
\]

entire.

Define

\[
 u_-(q;z)=e^{zq}\int_{-\infty}^{q}e^{-zr}\Phi(r)\,dr,
\]

\[
 u_+(q;z)=-e^{zq}\int_q^{\infty}e^{-zr}\Phi(r)\,dr.
\]

Their difference at every \(q\), not only at the seam, is

\[
 u_-(q;z)-u_+(q;z)=e^{zq}\tau(z).
\]

## Global zero history

If \(\tau(z_0)=0\), the two formulas agree for every \(q\). Write their common
value as \(u_{z_0}\). It has both tail representations

\[
 u_{z_0}(q)
 =e^{z_0q}\int_{-\infty}^{q}e^{-z_0r}\Phi(r)\,dr
 =-e^{z_0q}\int_q^{\infty}e^{-z_0r}\Phi(r)\,dr.
\]

Use the first representation as \(q\to-\infty\) and the second as
\(q\to+\infty\). For any \(A>|\operatorname{Re}z_0|\), the source estimate
gives constants \(C_A,c_A>0\) such that

\[
 |u_{z_0}(q)|\le C_Ae^{-c_A|q|}
\]

outside a compact interval. Hence

\[
 u_{z_0}\in L^1(\mathbb R)\cap L^2(\mathbb R).
\]

The forced equation holds without a seam delta:

\[
 (\partial_q-z_0)u_{z_0}=\Phi.
\]

Since the right side and \(u_{z_0}\) are in \(L^2\),

\[
 u_{z_0}\in H^1(\mathbb R).
\]

This conclusion holds for every zero of \(\tau\), regardless of its real part.
It therefore supplies domain membership but no zero-location theorem.

## Split-line maximal-isotropic domain

For the punctured-line first-order operator, take boundary values

\[
 \gamma u=(u(0^-),u(0^+)).
\]

The seam Green form is

\[
 \omega(\gamma u,\gamma v)
 =u(0^-)\overline{v(0^-)}-u(0^+)\overline{v(0^+)}.
\]

The continuity relation

\[
 \Lambda_{\rm cont}=\{(c,c):c\in\mathbb C\}
\]

is isotropic. It is one-dimensional in the two-dimensional nondegenerate
boundary space, so it is maximal isotropic. Its operator domain is exactly

\[
 \{(u_-,u_+)\in H^1(( -\infty,0))\oplus H^1((0,\infty)):
 u_-(0)=u_+(0)\}=H^1(\mathbb R).
\]

Therefore \(u_{z_0}\) lies in the source-selected maximal-isotropic seam
domain. Its endpoint values vanish, and integration by parts has no endpoint
or seam remainder.

This is a statement about the history coordinate \(q\), not about physical
time.

## Parameter-root vectors and local length

Differentiate the exact identity

\[
 u_-(q;z)-u_+(q;z)=e^{zq}\tau(z).
\]

For \(j\ge0\),

\[
 \partial_z^j(u_--u_+)
 =e^{zq}\sum_{k=0}^j {j\choose k}q^{j-k}\tau^{(k)}(z).
\]

Suppose \(z_0\) is a zero of order \(m\). Then for every \(0\le j<m\),

\[
 \partial_z^j u_-(q;z_0)=\partial_z^j u_+(q;z_0)
\]

for every \(q\). Differentiating either tail formula introduces only powers of
\(q-r\). Superexponential source decay absorbs every such power, so

\[
 \partial_z^j u(\cdot;z_0)\in H^1(\mathbb R),
 \qquad 0\le j<m.
\]

At order \(m\), the mismatch is

\[
 e^{z_0q}\tau^{(m)}(z_0)\ne0.
\]

Thus the first \(m\) parameter-root vectors belong to the same
maximal-isotropic history domain, and the next derivative detects the local
vanishing order. This proves domain-level local-length preservation for the
triangular Evans complex.

It does not prove local-length preservation after promotion into the
conservative arithmetic--Green complex.

## Why limiting absorption is unnecessary here

A limiting-absorption argument is needed when a seam state is defined only as a
boundary value of a resolvent. The Evans history is instead given by convergent
source integrals. At a zero, the exact mismatch identity converts the two
one-ended formulas into one global \(H^1\) vector. No limit
\(z\to z_0\) from a half-plane is used.

Accordingly the prior open SCC slot should be refined into two nodes:

1. `evans_history_maximal_isotropic_domain`, now constructed;
2. `conservative_green_seam_domain_and_state`, still open.

The second still requires all extra Green ports, the arithmetic lower equation,
and the adjoint residual

\[
 B_\Sigma^\dagger u_z=0.
\]

## Disposition

The seam rigging problem is closed for the explicit triangular Evans history,
including its parameter-root vectors. The remaining rigging problem belongs to
the conservative Green promotion, not to the existence or boundary regularity
of the Evans state. No RH conclusion is authorized.
