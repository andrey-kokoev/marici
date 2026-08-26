# A Fredholm Determinant Detects Kernels, Not Uniform Coercivity or Sheet

For a trace-class operator \(K\) on a Hilbert space, the Fredholm determinant

\[
\det(I-K)
\]

is defined and satisfies

\[
\det(I-K)=0
\quad\Longleftrightarrow\quad
I-K\text{ is not invertible}.
\]

For a trace-norm analytic family, the determinant is analytic and its zeros
encode algebraic multiplicity. This supplies a valid scalar kernel detector
once trace-class topology and equality with the desired scalar section are
proved.

It supplies neither a uniform inverse bound nor the source type of the kernel.

## Nonzero determinant does not give uniform coercivity

At cutoff \(N\), let

\[
A_N=\operatorname{diag}(N^{-1},1,\ldots,1).
\]

Every determinant is nonzero, but

\[
\det A_N=N^{-1},
\qquad
\|A_N^{-1}\|=N.
\]

Thus pointwise determinant nonvanishing is exactly another finite-stage
certificate that can lose strict invertibility at completion.

Determinant magnitude is not a coercivity proxy in the other direction
either. For \(B_N=\frac12I_N\),

\[
\det B_N=2^{-N}\to0,
\qquad
\|B_N^{-1}\|=2.
\]

The scalar product collapses solely because the dimension grows, while the
operator remains uniformly invertible. Even a constant determinant can hide
bad conditioning: \(\operatorname{diag}(N,N^{-1})\) has determinant one and
inverse norm \(N\).

## The determinant forgets the kernel sheet

Let the sheet involution be \(S=\operatorname{diag}(1,-1)\), and define

\[
A_+(s)=\operatorname{diag}(1-s,1),
\qquad
A_-(s)=\operatorname{diag}(1,1-s).
\]

Both have the identical determinant \(1-s\). At \(s=1\), however, the first
kernel is even and the second is odd. Hence the scalar determinant detects
that an obstruction exists but cannot reconstruct its boundary character,
seam action, or operator-valued lift.

## Typed hierarchy

The completed theta/Tate bridge must distinguish:

1. **Determinant authority:** the correlation defect is trace class (or an
   authorized regularized determinant is defined).
2. **Scalar identification:** that determinant equals the completed scalar
   Tate section up to a proved zero-free normalization.
3. **Kernel typing:** operator-valued source data identify which sheet and
   boundary channel carry the kernel.
4. **Uniform coercivity:** a lower singular-value estimate rules out
   completion escape.

The first two can identify the zero set. They do not imply the third or
fourth.

## Falsifiers

- Finite determinants are multiplied across growing cutoffs without
  trace-norm convergence or regularization.
- Pointwise nonzero determinants are reported as a uniform inverse bound.
- Determinant magnitude is treated as a smallest-singular-value estimate.
- Equal scalar determinants are used to identify operator lifts or sheet
  characters.
- A zero-free normalization factor is assumed rather than derived.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to type exactly what a Fredholm determinant can transport
from the operator problem into a scalar section.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Kernel existence, kernel character, determinant amplitude, and uniform
coercivity are now separated by exact hostile families.
