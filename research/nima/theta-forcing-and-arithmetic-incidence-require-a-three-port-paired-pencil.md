# Theta forcing and arithmetic incidence require a three-port paired pencil

> **Current reduction.** Source-order reread fixes \(D_\theta=0\) and the
> primitive direct cross block to zero. The authoritative history-eliminated
> form is in
> `the-three-port-schur-reduction-is-one-dressed-theta-weyl-scalar-over-a-coercive-arithmetic-complement.md`.
> Any residual formulas below containing an independent \(R\) describe a
> rejected enlargement, not the minimal source pencil.

## Type correction

The theta forcing column and the arithmetic seam incidence have different
source spaces:

\[
V:\mathbb C_\theta\to H,
\qquad
Vc=c\Phi,
\]

\[
B:U_{\rm ar}\to H.
\]

The scalar theta source coordinate is not an all-prime arithmetic coefficient
vector.  Requiring an arithmetic state \(x\) with

\[
Bx=\Phi
\]

conflates these ports and fails on the retained seam topology.

## Three-port carrier

The minimal paired carrier is

\[
H\oplus\mathbb C_\theta\oplus U_{\rm ar}.
\]

The source-authorized minimal paired block is

\[
\mathcal P_3(z)
=
\begin{pmatrix}
A-z&-V&-B\\
V^*&0&0\\
B^\dagger&0&D_U(z)
\end{pmatrix}.
\]

The theta diagonal is zero because its source coordinate is constant. No
direct arithmetic--theta block is present: \(V^\dagger B\) is a downstream
Gram compression, not a primitive dynamic arrow. The displayed
off-diagonal history pairs are skew-adjoint in the direct-sum metric.

## Green cancellation

For a state \((u,c,x)\), the real parts of the three off-diagonal pairings
cancel:

\[
-V\leftrightarrow V^*,
\qquad
-B\leftrightarrow B^\dagger,
\qquad
R\leftrightarrow -R^*.
\]

Hence the total Green identity contains only:

- the displacement term from \(A-z\);
- the Hermitian parts of \(D_\theta\) and \(D_U\);
- endpoint flux.

No forcing pairing remains when the full three-port system is used.

## Evans-state promotion

The analytic Evans construction supplies \(u_z\) and the normalized theta
source coordinate \(c=1\), satisfying

\[
(A-z)u_z=V1.
\]

The first row of the three-port pencil instead requires

\[
(A-z)u_z=V1+Bx_z.
\]

Therefore promotion of this unchanged Evans state already imposes

\[
Bx_z=0.
\]

The remaining source equations are

\[
V^*u_z+D_\theta(z)+Rx_z=0,
\]

\[
B^\dagger u_z-R^*+D_U(z)x_z=0.
\]

## Vector residual

For the unchanged Evans history define

\[
\mathcal R_3(z;x)
=
\begin{pmatrix}
Bx\\
V^*u_z+D_\theta(z)+Rx\\
B^\dagger u_z-R^*+D_U(z)x
\end{pmatrix}.
\]

It promotes precisely when a source-authorized \(x_z\) makes all three
components vanish. If \(B\) is injective on the reduced arithmetic carrier,
the first component forces \(x_z=0\), so the reservoir cannot repair the
adjoint equation through \(R x_z\).

A nonzero arithmetic state requires a modified history

\[
u_{z,x}=(A-z)^{-1}(V1+Bx),
\]
## Schur elimination

Let

\[
R_H(z)=(A-z)^{-1}.
\]

Eliminating the history coordinate from the full three-port pencil gives the
two-port source characteristic

\[
M_{\theta U}(z)
=
\begin{pmatrix}
D_\theta+V^*R_HV & R+V^*R_HB\\
-R^*+B^\dagger R_HV & D_U+B^\dagger R_HB
\end{pmatrix},
\]

with signs changed coherently if the opposite resolvent convention is used.
This is the correct Schur object for a nonzero arithmetic state.

The scalar Evans mismatch belongs initially to the \(R_HV\) history. The
additional blocks \(R_HB\) change both its seam trace and its source return.
Therefore identifying

\[
\det_{\rm rel}M_{\theta U}(z)
\]

with the Xi section requires a source theorem; it does not follow from the
analytic Evans identity.

## Determinant architecture

The three-port architecture correctly separates theta forcing from arithmetic
incidence and cancels all Green cross terms. It also exposes a new coupled
divisor rather than preserving the Xi divisor automatically.

For the unchanged Evans state, injectivity of \(B\) forces the arithmetic
coordinate to vanish. For a nonzero arithmetic coordinate, the history and
its seam mismatch change. These alternatives cannot be merged by terminal
scalarization.

## Remaining constructor

The new data are

\[
R:U_{\rm ar}\to\mathbb C_\theta,
\qquad
D_\theta(z),
\qquad
D_U(z),
\]

plus a determinant-line comparison between the full source Schur matrix
\(M_{\theta U}\) and the theta Xi dual section. They must be derived from the
primitive, square, connected, seam, endpoint, and archimedean packet.
Defining them to force the determinant equality would be circular.

## Disposition

The correct paired architecture has three distinct ports, but it does not yet
promote the unchanged Evans state. It replaces the impossible equation
\(Bx=\Phi\) by the sharper alternative: either \(x=0\) on an injective
incidence, or the arithmetic state modifies the history and its divisor. G4
remains open at the three-port Schur/Xi comparison. No RH conclusion is
authorized.
