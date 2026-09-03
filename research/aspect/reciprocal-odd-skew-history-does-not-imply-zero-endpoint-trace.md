# Reciprocal-odd skew history does not imply zero endpoint trace

## Question

Does the source-native candidate

\[
T_{\rm hist}=\frac{H_+-H_+^*}{2}
\]

belong automatically to the recovery-dark vertical auxiliary bundle because it is anti-Hermitian and reciprocal odd?

## Exact countermodel

On \(H=\mathbb R^2\), take reciprocal reflection and skew operator

\[
U=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
K=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]

Then

\[
K^*=-K,
\qquad
UKU=-K.
\]

Thus \(K\) has exactly the abstract skew-adjoint and reciprocal-odd properties required of the history difference. Let endpoint recovery be

\[
T=\begin{pmatrix}1&0\end{pmatrix}.
\]

Then

\[
TK=\begin{pmatrix}0&1\end{pmatrix}\ne0.
\]

Therefore reciprocal oddness and skew-adjointness do not place the image of \(K\) in \(\ker T\).

## Structural distinction

The identities

\[
K^*=-K,
\qquad
UKU=-K
\]

control metric parity and reciprocal character. The zero-trace law

\[
TJ_{\rm aux}=0
\]

controls compatibility with the endpoint quotient. Neither class of identities implies the other.

A source-native tail/PV constructor based on \(T_{\rm hist}\) must therefore include a separate endpoint cancellation. The canonical conditional correction is

\[
J_{\rm aux}=(I-P_{\min}T)T_{\rm hist}J_{\rm source},
\]

but this is physical only if the subtraction is part of the source constructor before representation.

## Covariance gate

To preserve reciprocal parity after regularization, the projection must intertwine the reflection:

\[
U(I-P_{\min}T)=(I-P_{\min}T)U.
\]

Sufficient typed identities are equivariance of endpoint recovery and harmonic lift:

\[
TU=U_ET,
\qquad
UP_{\min}=P_{\min}U_E.
\]

The same commutation requirement applies to prime-label projections.

## Disposition

Reject automatic recovery-darkness of the skew history candidate. The next executable construction is the reciprocal- and label-equivariant zero-trace projection, followed by a source proof that this projection occurs before Green representation rather than as a fitted correction.
