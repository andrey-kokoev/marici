# The bilateral Green form has an explicit parity graph, but its local positive polarization excludes physical exponential states

## Parity blocks

Let

\[
P_e=
\frac12(I+R),
\qquad
P_o=
\frac12(I-R).
\]

Then

\[
\widehat{\mathcal H}_\Phi
=
\mathcal H_e
\oplus
\mathcal H_o.
\]

Both differentiation and multiplication by the odd function

\[
q=
\frac{W'}W
\]

reverse parity. Therefore

\[
A=
\begin{pmatrix}
0&A_{eo}\\
A_{oe}&0
\end{pmatrix},
\qquad
M_q=
\begin{pmatrix}
0&Q_{eo}\\
Q_{oe}&0
\end{pmatrix}.
\]

The bilateral Green form contains only even--odd cross terms:

\[
2\operatorname{Re}
\langle Af,f\rangle
=
2\operatorname{Re}
\langle Q_{oe}f_e,f_o\rangle.
\]

This is the spin-two or oriented component in parity coordinates.

## Polar decomposition of the Green multiplier

For the completed theta weight, \(W\) decreases with \(|u|\). Hence

\[
q(u)>0
\quad(u<0),
\qquad
q(u)<0
\quad(u>0).
\]

Write

\[
M_q=J_qM_{|q|},
\]

where

\[
J_q=
\operatorname{sgn}(q)
=-
\operatorname{sgn}(u).
\]

The operator \(J_q\) is a self-adjoint unitary that exchanges even and odd parity. It gives the canonical local Krein polarization of the Green form.

## Positive and negative graphs

The positive spectral subspace of \(M_q\) consists of functions supported on the negative half-line. In parity coordinates it is the graph

\[
f_o
=-
\operatorname{sgn}(u)f_e.
\]

The negative spectral subspace, supported on the positive half-line, is the opposite graph

\[
f_o
=+
\operatorname{sgn}(u)f_e.
\]

Thus the local maximal positive graph is completely explicit.

## Failure of physical-state admission

A physical exponential state

\[
e_s(u)=e^{-su}
\]

is nonzero on both half-lines. It lies in neither local spectral graph.

Its parity components are

\[
(e_s)_e=
\cosh(su),
\qquad
(e_s)_o=
-
\sinh(su).
\]

The graph relation between these components is

\[
(e_s)_o
=-
\tanh(su)
(e_s)_e.
\]

The multiplier \(-\tanh(su)\) depends on the spectral parameter. Therefore no fixed local parity multiplier admits every physical exponential section.

## Consequence

The bilateral dilation solves reciprocal implementation but not positive-state admission. The canonical positive spectral subspace of the local Green multiplier discards half of each physical state.

A successful polarization must be nonlocal. It must mix the parity sectors through an operator \(T\) satisfying

\[
f_o=Tf_e
\]

for the completed physical state family while making

\[
2\operatorname{Re}
\langle Q_{oe}f_e,Tf_e\rangle
\ge0.
\]

Pointwise multiplication cannot provide such a universal \(T\), because the required multiplier on exponential sections is \(-\tanh(su)\).

## Control interpretation

The local sign decomposition is the open-loop energy-direction split. Physical Xi states are closed-loop states crossing both incoming and outgoing regions. Their admission requires a dynamic controller, not static local feedback.

In Hardy language, this dynamic graph is the graph of a Toeplitz or Hankel operator determined by the boundary transfer function. Its contractivity is again the substantive positive-real condition.

## Disposition

The parity block structure and local maximal positive graph are now explicit. They prove that the remaining bilateral constructor must be nonlocal; neither half-line support projection nor a fixed parity multiplier can contain the physical exponential family.
