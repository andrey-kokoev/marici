# One Gaussian forcing atom completes as an entire-function jet connection

## Construction

Put

\[
y(x)=e^{2x},\qquad f(x)=2e^{-\pi y(x)},\qquad h_k(x)=y(x)^k f(x).
\]

The finite jet equations

\[
\partial_x h_k=2k h_k-2\pi h_{k+1}
\]

never close at finite grade. Package the full tower by its exponential generating function

\[
H_x(t)=\sum_{k\ge0}h_k(x)\frac{t^k}{k!}
      =f(x)e^{y(x)t}
      =2e^{y(x)(t-\pi)}.
\]

For every fixed `x`, this is an entire function of `t`. Use the Frechet carrier

\[
\mathcal E=\mathcal O(\mathbb C_t)
\]

with compact-open seminorms

\[
p_R(H)=\sup_{|t|\le R}|H(t)|,
\qquad R>0.
\]

## Connection

Summing the jet recurrence gives the exact transport equation

\[
\partial_xH_x=(2t-2\pi)\partial_tH_x.
\]

Thus the forcing connection is

\[
\nabla_x=\partial_x-(2t-2\pi)\partial_t.
\]

Differentiation and multiplication by `t` are continuous on
`O(C)` in the compact-open topology: for `R<R'`, Cauchy's estimate gives

\[
p_R(\partial_tH)\le \frac{1}{R'-R}p_{R'}(H),
\]

and

\[
p_R(tH)\le Rp_R(H).
\]

Therefore `(2t-2pi) partial_t` is a continuous linear operator on the
projective Frechet carrier, and `nabla_x H_x=0` exactly. Every finite jet is
recovered by the continuous evaluation

\[
h_k(x)=\partial_t^kH_x(0).
\]

## Provenance and limitations

The carrier and connection are derived directly from the single Gaussian atom
`f=2 exp(-pi e^(2x))`; no fitted coefficient or zero information is used. This
is the local model isolated in the variable-forcing audit, not the completed
theta forcing `Phi`, whose summands also contain the factor
`e^(x/2)(4X_n^2-6X_n)` with `X_n=pi n^2 e^(2x)`. The construction closes the
infinite jet transport of this atom only.

It does not yet prove that the Schur incidence, return, and recovery maps are
continuous on a common `x`-history tensor `O(C_t)` domain. It also does not
supply determinant-class control: differentiation on `O(C)` is continuous
between projective seminorms but is not a bounded operator on one fixed
Hilbert rung.

## Disposition

A Gaussian-atom jet carrier exists canonically as an entire-function Frechet
module, and that atom is a horizontal section of its continuous connection.
The next gate is a labelled direct-sum construction for every completed-theta
summand, including its polynomial prefactor, followed by normal convergence
and extension of the finite Schur block.
