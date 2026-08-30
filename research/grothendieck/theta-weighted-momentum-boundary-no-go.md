# The theta Fourier-zero boundary does not make weighted momentum self-adjoint

Status: exact scalar first-order no-go; no RH claim

The faithful bilateral source suggests the Hilbert space

\[
 \mathcal H_\Phi=L^2(\mathbb R,\Phi(t)dt),             \tag{1}
\]

where the completed theta density is smooth, positive, and
superexponentially decreasing.  Every exponential `e_z(t)=e^{izt}` belongs
locally to the source calculus, and

\[
 X(z)=\int_{\mathbb R}\Phi(t)e^{izt}\,dt              \tag{2}
\]

is its scalar source readout.

It is tempting to impose `X(z)=0` as a nonlocal boundary condition on the
translation generator so that the Riemann zeros become eigenfrequencies.
This fails before any spectral estimate is needed.

## Weighted momentum has a bulk symmetry defect

On compactly supported smooth functions let

\[
 P_0=-i\partial_t.
\]

Integration by parts gives

\[
 \langle P_0f,g\rangle_\Phi-
 \langle f,P_0g\rangle_\Phi
 =i\int_{\mathbb R}f(t)\overline{g(t)}\Phi'(t)dt.     \tag{3}
\]

The defect is a bulk multiplication form, not an endpoint form and not a
finite-rank boundary channel.  Since `Phi` is nonconstant, no domain
condition involving only the scalar readout (2) can make (3) vanish for all
test functions in a dense domain.

## Symmetrization removes the desired eigenfunctions

The unique scalar imaginary drift that cancels (3) is

\[
 P_\Phi=-i\left(\partial_t+rac12\frac{\Phi'}\Phi\right),       \tag{4}
\]

up to addition of a real multiplication potential.  The unitary map

\[
 Uf=\sqrt\Phi\,f:
 \mathcal H_\Phi\longrightarrow L^2(\mathbb R,dt)    \tag{5}
\]

sends (4) to ordinary free momentum:

\[
 UP_\Phi U^{-1}=-i\partial_t.                         \tag{6}
\]

Its generalized eigenfunctions in the original representation are

\[
 \Phi(t)^{-1/2}e^{izt},                               \tag{7}
\]

not the exponentials whose theta-weighted readout is (2).  Moreover the
self-adjoint realization has continuous real spectrum.  It does not turn the
isolated Fourier zeros of `X` into normalizable eigenvalues.

## Nonlocal restriction does not repair the mismatch

Requiring

\[
 \int\Phi(t)f(t)dt=0                                  \tag{8}
\]

does select exponentials at the zeros of `X`, but those exponentials solve
the eigenvalue equation for the nonsymmetric operator `P_0`, not for the
symmetric operator `P_\Phi`.  On finite intervals, self-adjoint momentum
boundary conditions instead yield arithmetic frequency lattices; adding
(8) is an extra nonlocal constraint and does not create a self-adjoint
extension with the Xi spectrum.

Therefore

\[
 \boxed{
 \text{Fourier-readout zeros are not eigenvalues of the natural
 theta-weighted translation generator.}
 }                                                     \tag{9}
\]

## Consequence for the infinite Carrier

The moving tail space is still the correct faithful positive source object,
but its translation generator cannot be the missing Hilbert--Polya operator.
The divisor must arise through a genuinely relative boundary construction
whose Green form is nonlocal in the tail coordinate.  A scalar integral
constraint appended to weighted momentum is insufficient.

This no-go also explains the terminal singularity of finite tail
compressions: they attempt to turn a distributed bulk symmetry defect into a
finite endpoint condition.  The missing boundary quotient must retain that
distributed information rather than compressing it into `X` alone.
