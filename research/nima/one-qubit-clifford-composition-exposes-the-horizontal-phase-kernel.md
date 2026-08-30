# One-qubit Clifford composition exposes the horizontal phase kernel

## Generators

Use the Pauli section

\[
P(a,b)=X^aZ^b
\]

and the one-qubit Clifford generators

\[
H
=
\frac{1}{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix},
\qquad
S
=
\begin{pmatrix}
1&0\\
0&i
\end{pmatrix}.
\]

Their additive actions on Pauli labels are

\[
h(a,b)=(b,a),
\qquad
s(a,b)=(a,a+b).
\]

## Generator coherence cells

Hadamard transport satisfies

\[
HP(v)H^*
=
\beta_H(v)P(hv),
\qquad
\beta_H(a,b)=(-1)^{ab}.
\]

Phase-gate transport satisfies

\[
SP(v)S^*
=
\beta_S(v)P(sv),
\qquad
\beta_S(a,b)=i^a.
\]

The Sum actions \(h\) and \(s\) are linear. The Product cells
\(\beta_H\) and \(\beta_S\) are the corrections required to lift those label
actions to exact Endo conjugation.

## Composition law

For horizontal transports \(G\) and \(K\), suppose

\[
GP(v)G^*=\beta_G(v)P(gv),
\qquad
KP(v)K^*=\beta_K(v)P(kv).
\]

Then

\[
(GK)P(v)(GK)^*
=
\beta_K(v)\beta_G(kv)P(gkv).
\]

Therefore the composite cell is

\[
\beta_{GK}(v)
=
\beta_K(v)\beta_G(kv).
\]

This is the horizontal composition coherence required by the double-functor
packet. Checking generator squares independently is insufficient unless their
cells obey this law.

## Finite relations

The Clifford generators obey

\[
H^2=I,
\qquad
S^4=I,
\qquad
(HS)^3=e^{i\pi/4}I.
\]

On Pauli labels,

\[
h^2=I,
\qquad
s^4=I,
\qquad
(hs)^3=I.
\]

The accumulated vertical conjugation cells around all three relations are
trivial because conjugation by a scalar unitary acts trivially on every Pauli
operator.

Thus every Pauli-intervention square identifies the Clifford route only modulo
its horizontal scalar phase.

## Exact kernel

The adjoint action

\[
\operatorname{Ad}:U(2)\longrightarrow
\operatorname{Aut}(\operatorname{End}(\mathbf C^2))
\]

has kernel

\[
\ker\operatorname{Ad}=U(1)I.
\]

Consequently, complete operator conjugation data cannot distinguish

\[
(HS)^3
\]

from \(I\), although the unitary routes differ by \(e^{i\pi/4}\).

This is not a defect when global unitary phase is declared gauge. It becomes a
real kernel when a larger intervention context makes the phase relative.

## Controlled transport

For an uncontrolled unitary \(U\), the replacement

\[
U\longmapsto e^{i\theta}U
\]

has no effect on conjugation of the isolated target.

For a controlled operation,

\[
|0\rangle\langle0|\otimes I
+
|1\rangle\langle1|\otimes U,
\]

the same replacement changes the relative branch phase. The horizontal
\(U(1)\) fiber then becomes observable by interference with the control
branch.

Therefore:

- Pauli conjugation is faithful on projective Clifford transport;
- a controlled reference port is required for unitary-phase faithfulness;
- physical availability of that controlled lift remains an implementation
  question.

## Three-layer lesson

The previous Hadamard square closed vertical transport through Sum, Product,
and Endo. Horizontal route composition introduces another quotient:

\[
U(2)\longrightarrow PU(2).
\]

The full double-functor audit must therefore declare whether horizontal scalar
phases are gauge or operative. Vertical faithfulness does not decide that
typing.

## Failure signatures

1. Check \(H\) and \(S\) squares separately but violate
   \(\beta_{GK}(v)=\beta_K(v)\beta_G(kv)\): generator covariance does not
   compose.
2. Infer \(H^2=I\) only from label action: the label quotient cannot certify
   the unitary phase.
3. Identify \((HS)^3\) with \(I\) in a controlled context: a relative phase
   error remains.
4. Demand a controlled reference when global phase is declared gauge:
   the interface is over-specified.
5. Declare global phase gauge and later admit controlled-\(U\) without
   retyping the quotient.

## Explanatory status

This is the first finite higher-coherence test of the double-functor proposal.
It shows that exact vertical intervention covariance can coexist with a
horizontal central kernel. Whether that kernel is harmless gauge or missing
information is determined by the admitted control context, not by the
conjugation algebra alone.
