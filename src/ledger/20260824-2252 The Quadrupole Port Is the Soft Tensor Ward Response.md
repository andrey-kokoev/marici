# 2252 — The Quadrupole Port Is the Soft Tensor Ward Response

## Hard-to-vary claim

Entry 2251's traceless-metric susceptibility has a canonical wavefunctional
instrument type: it is the zero-momentum soft-tensor Ward response.  This
identifies an existing physical coefficient port, but does not by itself prove
that a chosen late-time experiment measures it.

## Functional typing

For a wavefunctional \(\Psi[g,\varphi]\), define its boundary stress response
by

\[
\delta_h\log\Psi
=
\frac12\int d^dx\,h_{ij}(x)\,\mathcal T^{ij}(x).
\]

Take a spatially constant traceless shear.  In momentum space its two real
polarizations are

\[
e_+=
\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
e_\times=
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

For \(p=k(\cos\theta,\sin\theta)\),

\[
e_+^{ij}p_ip_j=k^2\cos2\theta,
\qquad
e_\times^{ij}p_ip_j=k^2\sin2\theta.
\]

These are exactly Entry 2251's two quadrupole score directions.  Equivalently,
they are the two polarization components of the soft tensor insertion acting
on the radial Gaussian kernel.

## Equilateral faithfulness

Appending the isotropic scalar score gives the same scaled evaluation matrix

\[
\begin{pmatrix}
2&2&0\\
2&-1&-1\\
2&-1&1
\end{pmatrix},
\qquad \det=-12.
\]

Hence the scalar port plus the two soft-tensor polarization ports separate the
three homogeneous labelled occurrences.

## Type boundary

Established:

\[
\boxed{
\text{quadrupole Gaussian score}
=
\text{traceless boundary-metric / soft-tensor Ward response}.
}
\]

Not established:

- that the strict zero-momentum tensor mode is an independent observable;
- that a specified detector can access both polarizations;
- that the squeezed physical limit has nonzero transfer after gauge and
  constraint reduction.

The next falsifier is therefore the finite-soft-momentum transfer map from the
two Ward ports to an admitted late-time tensor-scalar readout.  A rank loss
there would be physical readout loss, not Carrier loss.

## Verification

`research/benincasa/checkers/soft_tensor_quadrupole_port.rs` verifies the two
polarization contractions, reversal parity, and equilateral rank.
