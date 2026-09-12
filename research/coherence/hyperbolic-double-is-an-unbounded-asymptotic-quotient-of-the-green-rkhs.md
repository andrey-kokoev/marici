# The hyperbolic double is an unbounded asymptotic quotient of the Green RKHS

## Kernel packet

Let

\[
k_x(s)=e^{-|s-x|}
\]

and consider a finite Green packet

\[
f(s)=\sum_i u_i k_{x_i}(s).
\]

At the two ends of the line,

\[
k_x(s)=e^x e^{-s}\quad(s>x),
\]

and

\[
k_x(s)=e^{-x}e^s\quad(s<x).
\]

Therefore the asymptotic boundary amplitudes are

\[
q_+(f)=\lim_{s\to+\infty}e^sf(s)=\sum_i u_i e^{x_i},
\]

\[
q_-(f)=\lim_{s\to-\infty}e^{-s}f(s)=\sum_i u_i e^{-x_i}.
\]

For multiplicative coordinates \(y_i=e^{x_i}\), these are exactly the previously derived residual charges

\[
q_+=\sum_i u_i y_i,
\qquad
q_-=\sum_i u_i/y_i.
\]

Thus the finite residual retyping map is the two-ended asymptotic observation

\[
\mathcal O_\infty f=(q_-(f),q_+(f)).
\]

## Exact discarded kernel

On finite kernel packets,

\[
\ker\mathcal O_\infty
=
\left\{
\sum_i u_i k_{x_i}:
\sum_i u_i e^{x_i}=0,
\quad
\sum_i u_i e^{-x_i}=0
\right\}.
\]

These are precisely the contextual distinctions invisible to the two-ended protocol. Quotienting by this kernel leaves the stationary hyperbolic double.

## Continuity obstruction

The observation is not bounded on the full Green RKHS \(H^1(\mathbb R)\). Every kernel section has constant norm,

\[
\|k_x\|_{H^1}=\|k_0\|_{H^1},
\]

while

\[
q_+(k_x)=e^x,
\qquad
q_-(k_x)=e^{-x}.
\]

Letting \(x\to+\infty\) or \(x\to-\infty\) gives an immediate boundedness contradiction.

Therefore no continuous map

\[
H^1(\mathbb R)\to\mathbb C^2
\]

extends these two asymptotic charges.

## Correct domain

The two-dimensional quotient exists algebraically on finite packets and continuously on a stronger exponentially controlled test domain. For example, require coefficient seminorms controlling

\[
\sum_i|u_i|e^{\delta|x_i|}
\]

for sufficiently large \(\delta\). Then both \(q_+\) and \(q_-\) are continuous covectors.

This recovers the projective exponential source rigging:

\[
\mathcal A_{\exp}
\subset H^1(\mathbb R)
\subset\mathcal A_{\exp}'.
\]

The hyperbolic double is a boundary-dual readout of \(\mathcal A_{\exp}\), not a bounded Hilbert quotient of the complete RKHS.

## Consequence

The infinite and finite realizations now fit without contradiction:

```text
H1 Green RKHS
  retains every signed context continuously

exponential test domain
  admits the unbounded two-ended asymptotic observation

C2 hyperbolic double
  retains only incoming/outgoing asymptotic charges
```

The exact information loss is the two-moment kernel displayed above. Any use of the finite double must declare this stronger domain and quotient explicitly.
