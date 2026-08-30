# Theta no finite antiderivative tower closes the mixed seam residual

## Residual recursion

Use the centered symmetric/antisymmetric state

\[
 x=\begin{pmatrix}m\\d\end{pmatrix},
\]

whose homogeneous evolution is

\[
 x'=A_zx+bF,
 \qquad
 A_z=
 \begin{pmatrix}
 -i\tau&-\delta\\
 -\delta&-i\tau
 \end{pmatrix}.
\]

Packet 198 shows that retaining the first primitive antiderivative

\[
 H_1'=F
\]

converts the forcing defect into a nonzero bilinear residual of the form

\[
 R_1=2\operatorname{Re}(H_1 r_1x)
\]

for an explicit row \(r_1\).

## Attempted finite repair

Introduce successive source antiderivatives

\[
 H_{j+1}'=H_j.
\]

To cancel \(R_j=2\operatorname{Re}(H_jr_jx)\), the corresponding local
current must contain

\[
 K_{j+1}=2\operatorname{Re}(H_{j+1}r_jx).
\]

Differentiation produces the desired term and a new one:

\[
 K_{j+1}'
 =2\operatorname{Re}(H_jr_jx)
 +2\operatorname{Re}(H_{j+1}r_jA_zx)
 +2\operatorname{Re}(H_{j+1}r_jbF).
\]

The second term is another mixed residual at level \(j+1\), with row

\[
 r_{j+1}=r_jA_z.
\]

## Nontermination off the seam origin

The determinant of the homogeneous flow matrix is

\[
 \det A_z=-(\delta^2+\tau^2)=-|z|^2.
\]

Hence \(A_z\) is invertible whenever \(z\ne0\). If a finite tower terminated
at level \(n\), its last nonzero residual row would have to satisfy

\[
 r_nA_z=0.
\]

Invertibility forces \(r_n=0\), and backward recursion then forces every
preceding row to vanish, contradicting the nonzero residual from packet 198.

Therefore no finite tower of source antiderivatives and local bilinear
currents can close the mixed forcing residual at any \(z\ne0\).

## Meaning

Primitive and square boundary coordinates may remain necessary typed
channels, but they cannot constitute the entire seam state when used merely
as the first two antiderivatives of a generic theta forcing. Closure requires
one of two genuinely stronger structures:

1. the complete infinite-dimensional shift orbit of the theta source; or
2. an independent finite-dimensional source equation that closes the forcing
   hierarchy.

The second option is unavailable for the exact theta tail: its translate span
is not finite-dimensional and it satisfies no nontrivial constant-coefficient
finite-order differential equation.

This connects the Green residual directly to the earlier seam-germ theorem.
The infinite shift state is not excess presentation; it is forced by
nontermination of the local boundary-current recursion.

## Falsifier

The no-go is defeated by an explicit finite source state whose closed
dynamics include \(F\) and whose bilinear current cancels packet 198's
residual without importing the scalar detector. Merely truncating the
antiderivative hierarchy or cancelling only after endpoint integration does
not qualify.

## Scope

This theorem applies to finite local currents built from a finite
antiderivative tower of the generic forcing. It does not exclude a
nonlocal current, an infinite shift-space current, or a distinct
finite-dimensional theta identity with independently derived dynamics.
