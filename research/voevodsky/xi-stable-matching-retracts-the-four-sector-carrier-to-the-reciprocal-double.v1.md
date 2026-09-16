# Xi stable matching retracts the four-sector carrier to the reciprocal double

## Carrier

Use the ordered basis \((L,z),(R,z),(L,-z),(R,-z)\) of \(B_{\mathrm{fb}}\cong\mathbb C^4\).

Let \(B_{\mathrm{rec}}\cong\mathbb C^2\) have basis \((z,-z)\).

Define the normalized stable-plus inclusion

\[
\iota_+
=
\frac{1}{\sqrt{2}}
\begin{pmatrix}
1&0\\
1&0\\
0&1\\
0&1
\end{pmatrix}.
\]

Its adjoint is

\[
\pi_+
=
\iota_+^*
=
\frac{1}{\sqrt{2}}
\begin{pmatrix}
1&1&0&0\\
0&0&1&1
\end{pmatrix}.
\]

They satisfy \(\pi_+\iota_+=I_{B_{\mathrm{rec}}}\).

The orthogonal stable-plus projector is

\[
P_+
=
\iota_+\pi_+
=
\frac12
\begin{pmatrix}
1&1&0&0\\
1&1&0&0\\
0&0&1&1\\
0&0&1&1
\end{pmatrix}.
\]

## Evans matching

The stable mismatch operator is

\[
D_{\mathrm{Ev}}
=
\begin{pmatrix}
1&-1&0&0\\
0&0&1&-1
\end{pmatrix}.
\]

Direct multiplication gives

\[
\ker D_{\mathrm{Ev}}
=
\operatorname{ran}\iota_+
=
\operatorname{ran}P_+.
\]

For the reciprocal pair of stable histories, the exact Evans identity is

\[
D_{\mathrm{Ev}}\mathcal O_{\mathrm{fb}}u(z)
=
\begin{pmatrix}
\tau(z)\\
\tau(-z)
\end{pmatrix}.
\]

Hence simultaneous reciprocal Evans matching places the four-sector endpoint state in \(\operatorname{ran}\iota_+\).

The reduced reciprocal state is \(b_{\mathrm{rec}}=\pi_+\mathcal O_{\mathrm{fb}}u\), and reconstruction is exact through \(\mathcal O_{\mathrm{fb}}u=\iota_+b_{\mathrm{rec}}\).

## Reciprocal naturality

Let

\[
r_g
=
\begin{pmatrix}
0&g^{-1}\\
g&0
\end{pmatrix},
\qquad
z_{\mathrm{rec}}
=
\begin{pmatrix}
1&0\\0&-1
\end{pmatrix}.
\]

The four-sector reciprocal operators satisfy

\[
R_g\iota_+
=
\iota_+r_g,
\qquad
Z_{\mathrm{rec}}\iota_+
=
\iota_+z_{\mathrm{rec}}.
\]

Therefore reciprocal exchange and its quarter-turn descend strictly to \(B_{\mathrm{rec}}\).

## Stable Clifford variance

Stable exchange satisfies \(S_{\mathrm{st}}\iota_+=\iota_+\).

Stable Green sign sends the stable-plus line to the stable-minus line.

The stable quarter-turn \(F_{\mathrm{st}}=J_{\mathrm{st}}S_{\mathrm{st}}\) also sends stable-plus states to stable-minus states.

Consequently \(J_{\mathrm{st}}\), \(F_{\mathrm{st}}\), and \(U_{\mathrm{kin}}=F_{\mathrm{st}}F_{\mathrm{rec}}\) do not descend as endomorphisms of the reduced matched carrier.

They remain transverse maps between matching and mismatch chiralities.

The positive crossing survives because \(J_{\mathrm{st}}F_{\mathrm{st}}=S_{\mathrm{st}}\), whose restriction to the matched carrier is the identity.

## Disposition

Xi matching gives a canonical normalized retract from four stable-reciprocal endpoint sectors to the reciprocal double.

The reduction preserves reciprocal Tate transport, reciprocal quarter-turn structure, endpoint norms, and the positive stable crossing.

The reduction retains the stable-minus space as the transverse defect carrier measured by the Evans section.

A full feedback reduction must therefore use the decomposition \(B_{\mathrm{fb}}=B_+\oplus B_-\) rather than discard \(B_-\), because the stable Clifford operators exchange the two chiralities.
