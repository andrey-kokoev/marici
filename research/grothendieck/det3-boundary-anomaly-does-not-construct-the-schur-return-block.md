# The det3 boundary anomaly does not construct the Schur return block

## Question

Can the exact order-three prime boundary factor be used directly as the
missing scalar block of the reciprocal Evans colligation?

## Two different categorical levels

For a finite cutoff, the reciprocal colligation would have the form

\[
L_X(z)=
\begin{pmatrix}
A_X(z)&B_X(z)\\
B_X(z)^*&C_X(z)
\end{pmatrix},
\qquad
S_X(z)=C_X(z)-B_X(z)^*A_X(z)^{-1}B_X(z).
\]

The endpoint Evans pencil independently constructs a scalar section
\(F_X(z)\).  The missing comparison cell is

\[
S_X(z)=u_X(z)F_X(z),
\]

with \(u_X\) nowhere zero and every block of \(L_X\) derived before this
comparison.

The recent prime calculation constructs something different.  The factor

\[
D_3(q)=(1+q)e^{-q+q^2/2}
\]

and its shared-corner anomaly live in a determinant line.  They determine how
finite prime-transfer determinants compose.  They do not, by themselves,
provide an arrow from the boundary line into the bulk state, its adjoint, or a
scalar return incidence.

Thus the tempting assignment \(C_X=D_{3,X}\), or any logarithmic derivative
of it, is ill-typed unless a separate source correspondence lifts the
determinant-line datum to the colligation.

## Exact finite nonuniqueness

Determinant data cannot reconstruct a reciprocal block system.  Even after
fixing the bulk scalar \(A=2\), the symmetric matrices

\[
L_0=
\begin{pmatrix}
2&0\\
0&3/2
\end{pmatrix},
\qquad
L_1=
\begin{pmatrix}
2&1\\
1&2
\end{pmatrix}
\]

have the same determinant, namely \(3\), but different return blocks and
different feedback decompositions:

\[
(B_0,C_0)=(0,3/2),
\qquad
(B_1,C_1)=(1,2).
\]

Their Schur complements agree only because the changed return block exactly
compensates the changed feedback:

\[
C_0-B_0^2/A=C_1-B_1^2/A=3/2.
\]

This is the smallest witness for the forgotten special-linear fiber.  A
determinant section records the reduced scalar after elimination; it does not
say which incidence and return channels produced it.

If \(A_X\), \(B_X\), and the determinant of the full colligation were all
independently available, then \(C_X\) could be recovered in this scalar
finite-dimensional case.  That stronger premise is exactly what we do not
have: det3 currently normalizes the prime-transfer determinant, not the
determinant of a source-derived reciprocal Evans colligation.

## Multi-tower interpretation

The input tower supplies the source and forward incidence.  The output tower
supplies the endpoint Evans section.  The control tower asks for the adjoint
return and a conserved Green form.  The det3 anomaly belongs to the fourth,
cross-tower coherence tower: it tells us how determinant readouts compose
across overlapping prime additions.

What is still missing is a rung above that coherence datum: a lift from the
determinant-line comparison back to an operator-level reciprocal
colligation.  This is not another scalar comparison channel.  It is a
source-derived refinement whose image under the determinant functor is the
known det3 cocycle and whose Schur image is the independently known Evans
section.

The required diagram is therefore constrained from two sides:

\[
\text{operator colligation}
\longrightarrow
\begin{cases}
\text{det3 prime-composition cocycle},\\
\text{endpoint Evans section}.
\end{cases}
\]

Neither scalar shadow can reconstruct the common source object alone.

## Consequence

The det3 discovery remains essential: it gives a necessary coherence law for
any candidate colligation and proves that shared prime corners cannot be
discarded.  But it does not fill the Schur return block.

The next admissible construction must derive \(B_X\) and \(C_X\) from the
same labelled boundary correspondence, then pass two independent tests:

1. its determinant-line composition reproduces the det3 anomaly and its
   boundary cancellation;
2. its Schur complement reproduces the endpoint Evans section up to a
   source-derived nowhere-zero unit.

A candidate satisfying only one test is not the missing common refinement.

## Falsifier

At the first finite prime cutoff, reject a proposed lift if any of the
following occurs:

- the return block is defined from \(F_X\) or from its zeros;
- the determinant composition misses the shared-corner anomaly;
- two source-authorized lifts have the same determinant data but different
  Schur sections without an explicit gauge equivalence;
- the Schur section and endpoint Evans section have different divisors;
- the comparison unit fails to be nowhere zero or cutoff-natural.

## Scope

This proves a typing and reconstruction no-go.  It does not prove that a
source-derived lift is impossible, construct the lift, establish
Schur--Evans agreement, or prove RH.
