# The endpoint face is the unbounded desmoothing of the source-adjoint face

## Hankel history correspondence

For a real half-line source (f), let

\[
(mathsf H_f\varphi)(q)
=\int_0^\infty f(q+a)\varphi(a)\,da.
\]

The physical Evans face is endpoint evaluation

\[
E_0y=y(0),
\]

while the canonical adjoint face is

\[
B_f^*y=\langle f,y\rangle.
\]

## Exact source–endpoint incidence

In the rigged half-line space,

\[
\mathsf H_f\delta_0=f.
\]

Self-adjointness of the real Hankel kernel therefore gives, on its natural
test domain,

\[
B_f^*y
=\langle\mathsf H_f\delta_0,y\rangle
=\langle\delta_0,\mathsf H_fy\rangle
=E_0\mathsf H_fy.
\]

Thus the two boundary covectors are not unrelated:

\[
B_f^*=E_0\mathsf H_f.
\]

The adjoint/source observer is the physical endpoint observer after one extra
history smoothing.

## The inverse comparison

On the range of (mathsf H_f), recovering the physical face requires

\[
E_0=B_f^*\mathsf H_f^{-1},
\]

where the inverse is interpreted on the quotient by the kernel if necessary.
Equivalently, the endpoint distribution is the desmoothed source:

\[
\delta_0=\mathsf H_f^{-1}f.
\]

For the theta source, (mathsf H_f) is Hilbert–Schmidt and therefore compact.
It has infinite rank. Indeed, a finite-rank Hankel translation kernel forces
the translate span of (f) to be finite-dimensional, so (f) is an
exponential polynomial and satisfies a constant-coefficient differential
equation. A nonzero exponential polynomial cannot have the theta tail's
superexponential decay. Therefore the compact Hankel operator has singular
values tending to zero, its inverse on the range is unbounded, and its
infinite-dimensional range is not closed.

Hence there is no bounded completion-stable desmoothing on the ambient Hilbert
space.

## Evans versus curvature

For the character state (e_z),

\[
F(z)=E_0\mathsf H_fe_z
\]

is the physical one-point transform. The canonical adjoint return is

\[
B_f^*\mathsf H_fe_z
=E_0\mathsf H_f^2e_z,
\]

which is the two-point autocorrelation/curvature face.

The two expressions differ by one full Hankel smoothing. Positivity and
self-adjointness naturally control the second iterate, while the xi divisor
belongs to the first.

## Completion obstruction

Any proof transferring positivity from the adjoint face to the endpoint face
must control the unbounded inverse (mathsf H_f^{-1}) on the
source-authorized character/history orbit. A bounded Schur complement or
ordinary Hilbert metric cannot perform this transfer.

The exact hostile sequence is any normalized singular-vector sequence
(arphi_n) with singular values (sigma_n\to0):

\[
\|\mathsf H_f\varphi_n\|=\sigma_n\to0,
\qquad
\|\varphi_n\|=1.
\]

Desmoothing amplifies these nearly invisible history states by
(sigma_n^{-1}). A viable theta theorem must prove that the completed
zero-state orbit avoids this escaping sector or retain the endpoint
distribution as an independent boundary channel.

## DPC

The completed theta/Tate constructor supplies a rigged comparison between the
direct and reciprocal endpoint/source-adjoint faces. Beyond controlling the
unbounded Hankel desmoothing, its cross-chart boundary law forces off-seam
endpoint nullity to be impossible. Packet 3992 explains why orbitwise
desmoothing control alone is insufficient.

The falsifier is a source-admissible character packet approaching the small
singular-value sector while all declared boundary currents remain bounded.
