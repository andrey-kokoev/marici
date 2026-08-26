# Theta transform is a two-port cross-transfer, not yet a Weyl determinant

## Bounded question

In the adjoint-closed two-port system, is the completed theta transform a cross
transfer entry or the determinant of the full Weyl matrix?

## Self-adjoint transport carrier

On the full logarithmic line, let

\[
A=-i\partial_q
\]

with its standard self-adjoint domain. Use two rigged ports:

\[
b_0=\delta_0,
\qquad
b_f=f.
\]

Here (b_0) is the boundary port and (b_f) is the completed theta-source
port. Their adjoints are endpoint evaluation and source pairing, respectively.

For a spectral parameter in a causal resolvent half-plane, the kernel of
\((A-z)^{-1}\) is one-sided. Consequently

\[
\langle b_f,(A-z)^{-1}b_0\rangle
\]

is, up to the fixed Fourier convention and a nowhere-zero scalar, the
one-sided Fourier--Laplace transform of (f). This is the theta scalar entering
the Evans construction.

Thus the source-derived scalar is naturally a cross-transfer entry between two
different ports.

## Full Weyl matrix

Let

\[
B=\begin{pmatrix}b_f&b_0\end{pmatrix}.
\]

The two-port Weyl matrix has the form

\[
W(z)=A_{\partial}(z)-B^*(A-z)^{-1}B.
\]

Its resolvent contribution contains four entries:

\[
\begin{pmatrix}
\langle b_f,R_zb_f\rangle&\langle b_f,R_zb_0\rangle\\
\langle b_0,R_zb_f\rangle&\langle b_0,R_zb_0\rangle
\end{pmatrix}.
\]

The theta transform occupies an off-diagonal entry. The determinant also uses
both diagonal self-energies and the reciprocal cross entry:

\[
\det W=W_{ff}W_{00}-W_{f0}W_{0f}.
\]

No currently derived source identity reduces this determinant to (W_{f0})
up to a nowhere-zero unit.

## Transmission zeros are not eigenvalues

A zero of (W_{f0}) means destructive transmission cancellation between the
source and boundary ports. It does not imply that (W) is singular, that the
internal self-adjoint operator has an eigenvalue, or that a full exterior
section vanishes.

This explains the persistent bridge failure. The scalar readout records a
relationship between distinct ports; Hilbert--Pólya requires a characteristic
section of one self-adjoint spectral problem.

## Exact exteriorization gate

To promote the theta scalar to a determinant, the source must prove one of the
following before zero inspection:

1. a rank or Plücker relation making the cross minor equal to \(\det W\) times a
   zero-free unit;
2. vanishing or fixed normalization of the diagonal minors;
3. a larger exterior-power section whose canonical coordinate is the theta
   cross transfer;
4. a boundary relation reducing the two-port system to one Lagrangian channel
   without losing sheet data.

Absent such a theorem, replacing the cross entry by \(\det W\) changes the
divisor.

## Sheet and winding consequence

Any determinant-to-section unit must be constructed separately on the two
reciprocal sheets. Their winding and parity classes must be retained before
taking the Ubersector product. Global cancellation of winding does not
authorize sheetwise square roots.

## Scope

This packet gives a self-adjoint two-port realization of the theta scalar as a
cross resolvent transfer and proves that it is not presently the Weyl
determinant. It does not rule out a source-derived exteriorization identity or
prove RH.
