# The raw Stieltjes endpoint plane has no finite radical but loses area at large primes

## Endpoint plane

For \(0<s<t\), consider the two window vectors

\[
W_s,
\qquad
W_t
\]

in \(L^2(\nu)\), where

\[
d\nu(q)=\rho(q)dq,
\qquad
\rho(q)=e^{-\pi q^2}>0.
\]

At prime \(p\),

\[
s=L=\log p,
\qquad
t=2L.
\]

## Finite linear independence

The window has the convolution form

\[
W_t(q)
=
-\int_{q-t}^{q+t}\rho(x)\,dx
=
-(\rho*\mathbf1_{[-t,t]})(q).
\]

Taking the ordinary Fourier transform gives

\[
\widehat W_t(\xi)
=
-\widehat\rho(\xi)
\frac{2\sin(t\xi)}{\xi}.
\]

The Gaussian transform \(\widehat\rho\) never vanishes.

Suppose

\[
W_s=cW_t.
\]

Then

\[
\sin(s\xi)=c\sin(t\xi)
\]

for every \(\xi\). Comparing the linear Taylor terms gives

\[
c=\frac{s}{t}.
\]

Comparing the cubic terms then gives

\[
s^2=t^2.
\]

For positive \(s,t\), this forces \(s=t\), a contradiction.

Therefore \(W_L\) and \(W_{2L}\) are linearly independent for every finite
prime.

## Finite radical descent

Since \(\rho>0\) everywhere, the Stieltjes GNS radical is zero on actual
functions. Linear independence implies the endpoint Gram

\[
G_p^{\mathrm{win}}
=
\begin{pmatrix}
\langle W_L,W_L\rangle_\nu&
\langle W_L,W_{2L}\rangle_\nu\\
\langle W_{2L},W_L\rangle_\nu&
\langle W_{2L},W_{2L}\rangle_\nu
\end{pmatrix}
\]

is strictly positive definite for every finite \(p\).

Thus the primitive-square endpoint cell has no finite Stieltjes radical.

## Large-prime limit

For each fixed \(q\),

\[
W_t(q)\to-1
\qquad
(t\to\infty).
\]

Also \(|W_t(q)|\le1\). Dominated convergence in \(L^2(\nu)\) gives

\[
W_t\to-\mathbf1.
\]

Hence, as \(p\to\infty\),

\[
W_L\to-\mathbf1,
\qquad
W_{2L}\to-\mathbf1,
\]

and

\[
G_p^{\mathrm{win}}
\longrightarrow
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}.
\]

Consequently,

\[
\det G_p^{\mathrm{win}}\to0.
\]

The disagreement energy also collapses:

\[
\|W_{2L}-W_L\|_\nu^2\to0.
\]

## Interpretation

The raw endpoint plane is two-dimensional at every finite prime, but its two
vectors become asymptotically parallel. Therefore:

- finite radical descent passes;
- no prime-uniform lower endpoint-area bound exists;
- the primitive-square difference becomes an asymptotically soft direction.

This is exactly the finite-positive-versus-completion-uniform distinction.

## Consequence for the Adams cell

A local endpoint-loading theorem cannot demand

\[
\inf_p\det G_p^{\mathrm{win}}>0
\]

in the raw Stieltjes frame. That statement is false.

There are only three legitimate repairs:

1. retain the prime-dependent endpoint metric without requiring local uniform
   inversion;
2. renormalize the disagreement direction by a source-derived scale;
3. prove that Euler-weighted global assembly suppresses the soft direction
   before inversion is used.

A fitted normalization by
\(\|W_{2L}-W_L\|_\nu^{-1}\) is not source-authorized automatically.

## Interaction with summability

The primitive-square mixed coefficient decays as \(p^{-3/2}\), and the exact
translation defect grows only logarithmically. Therefore the global mixed
operator can converge even while the local endpoint area tends to zero.

Bounded synthesis and uniform local invertibility are distinct requirements.

## Theta-history side

If \(M_\Phi<1\), the shifted theta-history blocks have a uniform positive
lower bound. Hence any quadratic comparison that is uniformly bi-bounded
from the raw Stieltjes endpoint plane to the theta graph is impossible: one
side loses a singular value and the other does not.

The comparison must be either:

- nonuniform in the raw frame;
- defined after an authorized disagreement renormalization;
- or a noninvertible incidence whose soft direction is intentionally
  compressed.

## Hostile

Verify positive determinant for every finite prime and infer a uniform
endpoint-loading margin. The matrices converge to rank one, so the inferred
margin is false.

## Frontier

Radical descent is closed finitely, but completion exposes a genuine
asymptotic endpoint-area obstruction:

\[
\det G_p^{\mathrm{win}}\to0.
\]

The next source theorem must decide whether this soft disagreement direction
is renormalized, compressed, or harmless after Euler-weighted global
assembly.
