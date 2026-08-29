# The complete endpoint pushforward is exactly faithful on the reciprocal incidence plane

## Endpoint trace map

For a relative history \(f\), write

\[
t_-(f)=f(-\infty),
\qquad
t_+(f)=f(+\infty).
\]

The complete endpoint pushforward is the Hadamard change of coordinates

\[
\Phi_{\partial}f
=
\begin{pmatrix}
w(f)\\
j(f)
\end{pmatrix}
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
-1&1
\end{pmatrix}
\begin{pmatrix}
t_-(f)\\
t_+(f)
\end{pmatrix}.
\]

Here:

- \(w\) is the constant-wall coordinate;
- \(j\) is the oriented-jump coordinate.

The matrix is unitary. Hence the complete pushforward is exactly faithful on the two-dimensional endpoint system and preserves its endpoint norm.

## Reflection character

Reciprocal reflection exchanges the two endpoint traces. Therefore

\[
w(Rf)=w(f),
\qquad
j(Rf)=-j(f).
\]

The pushforward diagonalizes the reciprocal involution instead of erasing it.

For Volterra histories of a source \(g\) with mass \(m_g\),

\[
\Phi_{\partial}(Sg)
=
\begin{pmatrix}
m_g/\sqrt2\\
0
\end{pmatrix},
\]

while

\[
\Phi_{\partial}(Tg)
=
\begin{pmatrix}
0\\
m_g/\sqrt2
\end{pmatrix}.
\]

Thus the even and odd history channels land in distinct output ports with identical normalization.

## Scalar Euler loss

The scalar Euler readout is only the first projection

\[
\Phi_{\mathrm{Euler}}f=w(f).
\]

Its kernel contains the full oriented-jump line:

\[
\ker\Phi_{\mathrm{Euler}}
\cap
\mathcal V_{\mathrm{inc}}
=
\mathbb C j.
\]

Therefore scalar prime pushforward is necessarily nonfaithful on the reciprocal incidence plane. This is not a numerical accident; it is a rank-one quotient of a rank-two source boundary.

## Minimal source repair

No invented observer is required. The odd port \(j\) is already the oriented endpoint difference supplied by the relative Stokes boundary. Retaining

\[
(w,j)
\]

is the minimal complete pushforward. Any other faithful pair is related to it by an invertible source-authorized change of endpoint frame.

Under the endpoint metric transported by Mellin half-density, the corresponding weighted Hadamard map remains an isometry between typed fibers.

## Primewise assembly

Apply \(\Phi_{\partial}\) inside each valuation label before any label aggregation:

\[
\bigoplus_{p,k}
P_{p,k}\mathcal H_{\mathrm{rel},p,k}
\longrightarrow
\bigoplus_{p,k}
P_{p,k}(\mathbb C w\oplus\mathbb C j).
\]

This preserves prime diagonality and reciprocal character. Summing scalar Euler coefficients may occur only after the odd ports have either been retained or linked by a proved source identity.

## Consequence

The prime-pushforward kernel theorem is closed on the endpoint incidence subspace:

\[
\ker\Phi_{\partial}
\cap
\mathcal V_{\mathrm{inc}}
=
\{0\}.
\]

The next gate is the linking theorem: prove that the retained jump port \(j_{p,k}\) maps with the correct normalization to the Euler-ratio or Wronskian odd coordinate used by the Adams Schur cell.
