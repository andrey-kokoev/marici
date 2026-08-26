# A sheet quarter-turn converts doubled theta transport into its cofactor

Owner: `marici.Nima`

## Starting transport

For the centered spectral coordinate \(z=s-1/2\), write

\[
U_z(q)=
\begin{pmatrix}
u&0\\
0&v
\end{pmatrix},
\qquad
u=e^{-zq},
\qquad
v=e^{\overline zq}.
\]

The determinant phase is

\[
\delta_z(q)=uv=e^{(\overline z-z)q},
\qquad
|\delta_z(q)|=1.
\]

Let the oriented quarter-turn in sheet space be

\[
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\qquad
J^2=-I.
\]

## Rotate both the source and target frames

Direct multiplication gives

\[
J U_z(q)J^{-1}
=
\begin{pmatrix}
v&0\\
0&u
\end{pmatrix}
=
\operatorname{adj}U_z(q).
\]

Thus, in the native rank-two doubled system, the cofactor operator is not an
unrelated extra observable. It is the transport seen after a quarter-turn of
both sheet frames. Equivalently,

\[
J U_z(q)J^{-1}=U_{-\overline z}(q).
\]

The quarter-turn implements the reciprocal-conjugate reflection of the
centered spectral parameter.

Because

\[
\operatorname{adj}U_z(q)
=
\delta_z(q)U_z(q)^{-1},
\]

and \(|\delta_z(q)|=1\), its norm is

\[
\|\operatorname{adj}U_z(q)\|
=
\|U_z(q)^{-1}\|
=
e^{|\operatorname{Re}z|q}.
\]

The cofactor growth is therefore the rotated view of the contracting
direction.

## Rotate only once

Define the transport-dressed quarter-turn

\[
Q_z(q)=J U_z(q).
\]

Then

\[
Q_z(q)^2
=
-\delta_z(q)I.
\]

Choose either local square root of the nonvanishing determinant phase and set

\[
\widetilde Q_z(q)=\delta_z(q)^{-1/2}Q_z(q).
\]

It follows that

\[
\widetilde Q_z(q)^2=-I.
\]

Hence the doubled flow carries a locally normalized algebraic complex
structure at every spectral point. This alone does not select the critical
line.

## Metric compatibility selects the seam

Left multiplication by \(J\) and multiplication by a unit phase do not change
singular values. Therefore

\[
\widetilde Q_z(q)^*\widetilde Q_z(q)
=
U_z(q)^*U_z(q)
=
\begin{pmatrix}
e^{-2aq}&0\\
0&e^{2aq}
\end{pmatrix},
\qquad
a=\operatorname{Re}z.
\]

Consequently, the following are equivalent:

1. \(a=0\);
2. \(\widetilde Q_z(q)\) is unitary for every \(q\ge0\);
3. the algebraic quarter-turn is compatible with the source Hermitian metric;
4. reciprocal-conjugate rotation preserves lengths in both sheet directions.

The critical seam is therefore not where a complex structure first exists.
It is where the source-derived complex structure, reciprocal transport, and
metric become mutually compatible.

## Rotation census

There are three distinct rotations, and they must not be conflated.

### Common phase rotation

Multiplication by \(e^{i\theta}I\) commutes with \(U_z(q)\). It changes no
singular value and supplies no orientation or positivity.

### Sheet quarter-turn

The operator \(J\) exchanges complementary reciprocal directions, produces
the cofactor under conjugation, and implements \(z\mapsto-\overline z\). This
rotation is internal to the doubled source architecture.

### Spectral-plane or flow-time quarter-turn

The substitutions \(z\mapsto iz\) or \(q\mapsto iq\) rotate which coordinate
controls growth, but they do not preserve the Mellin half-line, its endpoint
domain, or the theta source without an additional analytic-continuation
constructor. They are useful hostile transformations, not currently
source-authorized symmetries.

## Consequence for the RH route

The rotation supplies an exact geometric interpretation of the cofactor
channel, but it does not yet control the forced system. The remaining theorem
must show that endpoint, primitive, square, seam, and archimedean forcing
preserve the metric-compatible rotated structure only on the seam, or that
off-seam forcing cannot satisfy both endpoint conditions.

A finite falsifier is any source-authorized forcing block whose rotated Green
current has a nonzero bulk residual not proportional to

\[
\operatorname{Re}z.
\]

Such a residual would show that the homogeneous quarter-turn does not extend
to the complete arithmetic boundary system.
