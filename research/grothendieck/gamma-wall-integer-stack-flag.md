# The Integer Gamma-Wall Stack Has a Canonical Oriented Flag

## Bounded question

What is the full linear carrier when the Pearson transfer is retained through
integer exponent grade $m$?

This packet constructs the carrier and its exterior-algebra orientation. It
does not extend the result to noninteger exponent depth or prove the cubic
response theorem.

## Graded state

For each integer $0\le k\le m$, retain the tail pair

\[
V_{j,k}=
\begin{pmatrix}
I_{j+1,k}\\
I_{j,k}
\end{pmatrix}.
\]

Adjoin the wall current $W_j$. The complete state is

\[
X_j^{(m)}=
\left(
V_{j,0},V_{j,1},\ldots,V_{j,m},W_j
\right).
\]

Its dimension is

\[
2(m+1)+1=2m+3.
\]

## Block transfer

Let

\[
A_j=
\begin{pmatrix}
j+19/4 & -(3/2)(j+5/4)\\
1 & 0
\end{pmatrix}
\]

and

\[
C_k=
\begin{pmatrix}
k & -3k/2\\
0 & 0
\end{pmatrix}.
\]

The Pearson recurrence gives

\[
V_{j+1,0}=A_jV_{j,0}+\begin{pmatrix}W_j\\0\end{pmatrix},
\]

\[
V_{j+1,k}=A_jV_{j,k}+C_kV_{j,k-1},
\qquad 1\le k\le m,
\]

and

\[
W_{j+1}=cW_j.
\]

The complete matrix is block lower-bidiagonal in exponent grade, with one
wall-to-grade-zero shear. No higher exponent feeds a lower exponent.

## Canonical invariant coflag

For $0\le r\le m$, define $G_r$ as the span of tail grades $r$ through $m$.
Then

\[
G_m\subset G_{m-1}\subset\cdots\subset G_0
\subset X^{(m)}
\]

is preserved by every transfer step. The full tail space is $G_0$. The wall
direction is not itself invariant, because it shears into grade zero. Instead,
the quotient $X^{(m)}/G_0$ is the one-dimensional wall channel and is acted
on by multiplication by $c$.

On the associated graded object, every tail-grade quotient is acted on by
$A_j$, while the final full-over-tail quotient carries the wall scaling.
The unit wall-to-grade-zero entry is the extension class joining that quotient
to the tail flag.

The coflag is source-derived. It records that lower exponent grades can feed
higher grades, while no higher grade feeds a lower one. The direction of the
flag is part of the theorem; reversing it erases the actual transport
incidence.

## Exterior-algebra orientation

The diagonal block determinant is

\[
\det A_j=\frac32\left(j+\frac54\right)>0.
\]

Therefore the complete determinant is

\[
\det M_j^{(m)}
=c\left[
\frac32\left(j+\frac54\right)
\right]^{m+1}>0.
\]

The top exterior blade of every invariant tail suffix keeps positive
orientation. The full blade does as well. The lower-grade couplings and wall
shear change representatives but cannot annihilate these blades at a finite
transfer step.

This statement uses only the exterior algebra of the transfer module. It does
not yet equip the module with a quadratic form or Clifford multiplication.
Consequently it proves preservation of oriented volume and nonannihilation,
not preservation of lengths, angles, causal type, or a Clifford-positive
cone.

## The source-derived dimension 21

At exponent grade $m=9$, the complete carrier has dimension

\[
2(9+1)+1=21.
\]

This is a legitimate rank-21 matrix system: ten tail two-planes plus one wall
direction. The number has no demonstrated relation to rank-21 systems in
other sectors. Such a relation would require a source-derived comparison map
preserving the flag and transfer, not merely equal dimension.

## Physical compression

At integer grade $m$, the primitive boundary readout is

\[
r(m)=m\frac{I_{0,m-1}}{I_{0,m}}.
\]

It compresses two adjacent flag stages to one scalar. Since the full transfer
is invertible and orientation-preserving, a failure of this scalar coordinate
cannot be identified with loss of the complete graded state.

## Remaining boundary

Continuous exponent response requires noninteger $q$. Repeated shifts then
terminate in the independent strip $-1<q\le0$, not in the single wall line
$q=0$. The integer flag theorem therefore supplies the exact finite model,
but the cubic theorem needs a continuous base-strip module and its
order-three exponent jet.

## Verification

The checker
`research/grothendieck/checkers/gamma_wall_integer_stack.py` constructs every
matrix for $0\le m\le10$ using exact arithmetic. It verifies the dimension,
determinant, invariant flag, wall shear, and the grade-nine dimension 21. A
deliberately reversed diagonal sign must reverse the determinant orientation.
