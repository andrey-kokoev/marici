# The two-port Pauli frame cancels endpoint cross-correlation under any common Green lift

## Result

Let a source-authorized common endpoint lift send the primitive-square plane into any Hilbert or reduced Green space. When the two normalized Euler Pauli ports are retained as separate outputs, their total lifted energy is independent of the off-diagonal endpoint correlation.

Only the two diagonal endpoint energies remain.

Thus mixed endpoint correlation cannot destroy the local arithmetic frame. Collapse can occur only if one endpoint lift loses norm, the lift leaks through a radical, or the two outputs are later merged by an untyped evaluator.

## Abstract endpoint lift

Let

\[
E_{12}=\mathbb C^2
\]

with ordered primitive-square basis. Let

\[
J:E_{12}\to\mathcal H_G
\]

be a common endpoint realization into a Hilbert space or a Green quotient after radical descent.

Its Gram matrix is

\[
A=J^*J
=
\begin{pmatrix}
a&z\\
\overline z&b
\end{pmatrix},
\]

where

\[
a=\|Je_1\|^2,
\qquad
b=\|Je_2\|^2.
\]

No assumption on the phase or magnitude of \(z\) is needed beyond \(A\ge0\).

## Pauli ports

Use the normalized strict Euler ports

\[
X=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\qquad
Y=
\begin{pmatrix}
0&i\\
-i&0
\end{pmatrix}.
\]

The lifted typed observer is

\[
\mathcal O_Jv
=
\begin{pmatrix}
JXv\\
JYv
\end{pmatrix}.
\]

Its frame operator is

\[
\mathcal O_J^*\mathcal O_J
=
XAX+YAY.
\]

## Exact cancellation identity

Direct multiplication gives

\[
XAX
=
\begin{pmatrix}
b&\overline z\\
z&a
\end{pmatrix},
\]

and

\[
YAY
=
\begin{pmatrix}
b&-\overline z\\
-z&a
\end{pmatrix}.
\]

Therefore

\[
XAX+YAY
=
2
\begin{pmatrix}
b&0\\
0&a
\end{pmatrix}.
\]

The complete endpoint cross-correlation \(z\) cancels.

Consequently,

\[
2\min(a,b)\|v\|^2
\le
\|\mathcal O_Jv\|^2
\le
2\max(a,b)\|v\|^2.
\]

The lower frame bound is

\[
\sqrt{2\min(a,b)}.
\]

## Interpretation

The Pauli pair swaps the two endpoint energies with opposite treatments of the off-diagonal polarization. Retaining both outputs performs an exact two-element twirl that removes cross-correlation.

This means the following endpoint defects do not affect the joint local lower bound:

- large real correlation;
- large imaginary reciprocal correlation;
- near-collinearity caused only by the off-diagonal Gram entry.

What matters is whether either endpoint has zero or collapsing norm in the reduced Green target.

This is stronger than a generic condition-number estimate.

## Radical gate

If the Green form is semidefinite, \(J\) must first land in the reduced support. The identity remains valid there.

The exact lower bound requires

\[
a>0,
\qquad
b>0.
\]

Thus the radical condition is endpointwise:

\[
Je_1\ne0,
\qquad
Je_2\ne0.
\]

A radical may identify the two endpoint images without destroying the typed two-port frame; even if \(Je_1=Je_2\ne0\), the formula still gives a positive lower bound. But killing either endpoint destroys one coordinate.

This does not authorize such identification categorically; it states only the observer-energy consequence.

## Separate lifts

Suppose the source constructs endpoint maps

\[
J_P:\mathbb C e_1\to\mathcal H_G,
\qquad
J_Q:\mathbb C e_2\to\mathcal H_G.
\]

Their direct assembly defines \(J\) by

\[
J(c_1,c_2)=J_Pc_1+J_Qc_2.
\]

Then

\[
a=\|J_P1\|^2,
\qquad
b=\|J_Q1\|^2,
\]

and the same identity applies. Hence no independent estimate of

\[
\langle J_P1,J_Q1\rangle
\]

is required for the typed arithmetic frame bound.

The off-diagonal pairing remains essential for the Green constructor and orientation, but not for this particular lower bound.

## Prime-uniform consequence

For prime-dependent lifts \(J_p\), if

\[
\|J_{P,p}1\|^2\ge m_P,
\qquad
\|J_{Q,p}1\|^2\ge m_Q
\]

uniformly after source normalization and radical reduction, then

\[
\|\mathcal O_{J_p}v\|^2
\ge
2\min(m_P,m_Q)\|v\|^2
\]

uniformly over primes and cutoffs.

No shear bound or endpoint angle enters this local arithmetic estimate.

## Mixed-output qualification

The identity relies on the direct-sum output norm

\[
\|JXv\|^2+\|JYv\|^2.
\]

If a terminal map combines the outputs,

\[
T(JXv,JYv)=JXv+JYv,
\]

cross cancellation can return. The global mixed-output angle margin remains necessary after such a terminal identification.

Thus this theorem removes correlation from endpoint loading, not from later evaluator mixing.

## Constructor frontier

This result does not construct the missing arithmetic-to-analytic endpoint lifts. It sharpens their required estimate.

The earliest Green-lift theorem no longer needs a lower angle bound between primitive and square endpoint images for arithmetic observability. It needs:

1. source-derived \(J_P,J_Q\);
2. radical descent;
3. positive endpoint norms;
4. uniform lower bounds in the source-normalized frame;
5. preservation of the two typed Pauli outputs.

The relative Green/Stokes identity and reciprocal orientation remain separate constructor obligations.
