# Reciprocity reduces the conservative boundary extension to one scalar

Rescale the endpoint coordinate so that the active colocation metric is the normalized swap

$$
J_{\rm col}=
\begin{pmatrix}0&0&1\\0&I_M&0\\1&0&0\end{pmatrix}.
$$

The conservative extension then has the form

$$
\widetilde A(x,y)=
\begin{pmatrix}
d&r^*&x\\
r&D_M&r\\
y&r^*&d
\end{pmatrix},
\qquad x,y\in\mathbb R.
$$

Let reciprocal exchange swap the normalized forcing direction and endpoint coordinate while fixing the common history complement:

$$
R=
\begin{pmatrix}0&0&1\\0&I_M&0\\1&0&0\end{pmatrix}.
$$

Direct conjugation gives

$$
R\widetilde A(x,y)R=\widetilde A(y,x).
$$

Therefore strict reciprocal invariance

$$
R\widetilde A R=\widetilde A
$$

holds exactly when

$$
x=y.
$$

The conservative reciprocal family is consequently

$$
\widetilde A_t=
\begin{pmatrix}
d&r^*&t\\
r&D_M&r\\
t&r^*&d
\end{pmatrix},
\qquad t\in\mathbb R.
$$

Reciprocity removes one scalar freedom but cannot select `t`. The remaining scalar is a boundary self-coupling. It must be fixed by a source boundary law or by requiring equality of the bordered transfer with the transverse Xi transfer. Setting `t=0` is a minimal convention, not yet a source theorem.

Status: conservative and reciprocal extension reduced to one real boundary parameter; Xi-transfer comparison remains the normalization gate.
