# The Hadamard wall--jump frame is the exact metric comparison from adelic boundary observers to the theta endpoint port

## Two canonical frames

In the observer frame

\[
e_{\mathrm{ev}}=\epsilon,
\qquad
e_{\mathrm{mass}}=\mu,
\]

Fourier sewing acts by the exchange matrix

\[
B=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

Define the normalized wall and jump observers by

\[
e_{\mathrm{wall}}
=
\frac{\epsilon+\mu}{\sqrt2},
\qquad
e_{\mathrm{jump}}
=
\frac{\epsilon-\mu}{\sqrt2}.
\]

The change of frame is the Hadamard matrix

\[
H=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix},
\qquad
H^*=H^{-1}=H.
\]

It diagonalizes Fourier exchange:

\[
HBH
=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

Thus the theta wall--jump grading is not an additional fitted decomposition.
It is the spectral decomposition of the source constant--delta exchange.

## Metric compatibility

The source endpoint metric in the two-coordinate normalization is

\[
G_\theta=2I.
\]

Therefore

\[
H^*G_\theta H=G_\theta.
\]

The observer-to-wall--jump comparison is exactly unitary, with no condition
loss and no cutoff-dependent normalization. It preserves both the absolute
endpoint scale and the reciprocal parity labels.

This is a comparison of external boundary ports. It does not promote the wall
coordinates to dynamic bulk states.

## Identification of the two retained coordinates

The even coordinate is the tensor-unit wall direction. The odd coordinate is
the oriented jump direction already used by the local theta-to-window
compression.

In the normalized odd line, the prior local comparison has

\[
K_pj_\theta=d_p.
\]

Hence the composite

\[
\operatorname{span}\{\epsilon_p,\mu_p\}
\xrightarrow{\,H\,}
\operatorname{span}\{e_{\mathrm{wall},p},e_{\mathrm{jump},p}\}
\xrightarrow{\,I\oplus K_p\,}
E_{\theta,p}\oplus E_{\mathrm{win},p}
\]

retains the even unit coordinate and sends the odd Fourier character to the
analytic window jump.

The second arrow is a graph attachment, not an isometry. Its correct positive
form is

\[
G_{\Gamma,p}
=
G_{\theta,p}
+
K_p^*G_{\mathrm{win},p}K_p.
\]

Therefore the exact Hadamard comparison supplies the lower margin, while the
window term is a positive trace-class shadow.

## Global restricted-product comparison

At every unramified finite place, the observer vacuum is

\[
(\epsilon_p,\mu_p)=(1,1).
\]

Under \(H\), it lies entirely in the even wall line:

\[
H(1,1)^T=(\sqrt2,0)^T.
\]

Thus the odd jump coordinate is a genuine finite excitation of the
Fourier-fixed restricted-product vacuum. On the cylinder domain, the
restricted tensor product of the local Hadamard maps is well typed and
isometric.

The archimedean even and odd Tate observer lines supply the analogous signed
reflection frame at infinity. Consequently the complete boundary cylinder
admits a Fourier-diagonal wall--jump frame before determinant or scalar
readout.

## Cutoff and completion behavior

Finite-place truncation projections commute with the frame change because
\(H\) acts independently inside each retained prime label. They also commute
with the wall projection and the jump projection.

Since \(H\) is unitary and \(K=\bigoplus_pK_p\) is trace class in the established
theta-to-window direction, the completed comparison has:

- an exact even retract;
- an exact odd theta coordinate;
- a compact analytic jump shadow;
- zero boundary radical;
- and the same endpoint coercivity constant as the source metric.

No finite-Euler Poisson operator is used. The truncations are projections of
an already constructed adelic boundary cylinder.

## Remaining constructor gate

The local and global boundary comparison is now explicit. What remains is not
a missing map between constant--delta and wall--jump coordinates.

The remaining question is whether every admitted arithmetic constructor
preserves the Fourier-saturated boundary pro-Gram in which this Hadamard frame
is orthogonal. Equivalently, for each constructor \(A\), one needs a
cutoff-compatible bound

\[
c_AQ_{\mathrm{sat}}
\le
A^*Q_{\mathrm{sat}}A
\le
C_AQ_{\mathrm{sat}}
\]

on its typed domain, with composite bounds controlled over the admitted
constructor words.

The first relevant constructor is Adams grade transport. Its action must
preserve prime labels, map the wall line to the authorized wall line, and map
the jump line through the already constructed odd compression without
switching reciprocal character.

## Hostiles

1. Use the unnormalized sum and difference frame without tracking its factor
   of \(\sqrt2\). Reciprocal characters are correct but the source metric
   scale changes.
2. Identify evaluation alone with the wall coordinate. Fourier then mixes it
   with mass, so the proposed retract is not sewing invariant.
3. Treat the odd window jump as the whole odd coordinate. Its norm decays with
   \(p\) and completion loses the lower margin.
4. Promote the external wall port to a bulk dynamic state. This contradicts
   the source five-cell typing.
5. Verify only scalar functional equation agreement. The Hadamard orientation
   and split endpoint metric can still be lost.

## Verdict

The metric-compatible comparison from the adelic constant--delta observer
plane to the theta wall--jump endpoint port is the normalized Hadamard
transform. It is exact, Fourier-equivariant, and completion-stable.

Together with the positive graph attachment \(I\oplus K\), it closes the
boundary comparison arrow. The earliest remaining gate is constructor
stability of the Fourier-saturated boundary pro-Gram, beginning with Adams
grade transport.
