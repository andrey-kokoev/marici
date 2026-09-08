# Physical source comparison \(a:J\to T[1]\)

## Scope

This constructs the source comparison on the **physical six-point derived-pullback
complex** \(J\) of Marici Entry 436, and lifts it canonically to the
normalization-conductor resolution \(T[1]\) **in the derived category**.

It does not choose a noncanonical \(B\)-linear section of the normalization
quotient.

## 1. Physical source \(J\)

Use the homological complex

\[
J_3\longrightarrow J_2\longrightarrow J_1\longrightarrow J_0
\]

with matrices

\[
d_3=
\begin{pmatrix}
0\\1\\1\\1
\end{pmatrix},
\]

\[
d_2=
\begin{pmatrix}
1&0&0&0\\
1&0&0&0\\
0&1&0&-1\\
0&-1&1&0\\
0&0&-1&1
\end{pmatrix},
\qquad
d_1=
\begin{pmatrix}
1&-1&-1&-1&-1
\end{pmatrix}.
\]

The primitive physical cycle is

\[
z=(1,0,1,0,0)^T\in J_1.
\]

## 2. Canonical conductor coefficient map

Let \(C_{\rm cond}\) denote the conductor coefficient line. Define

\[
a_C:J\longrightarrow C_{\rm cond}[1]
\]

by zero in every degree except degree one, where

\[
a_{C,1}
=
\begin{pmatrix}
0&0&1&1&1
\end{pmatrix}.
\]

Thus \(a_C\) is the road augmentation.

The chain equation is

\[
a_{C,1}d_2=0.
\]

Moreover,

\[
a_C(z)=1.
\]

The first two coordinates of \(J_1\) are the endpoint coordinates, so

\[
a_C|_{\rm endpoint}=0.
\]

This is the unique integral degree-one chain map with zero endpoint
coordinates and \(a_C(z)=1\).

Indeed, write

\[
w=(0,0,r_1,r_2,r_3).
\]

The equation \(wd_2=0\) forces

\[
r_1=r_2=r_3.
\]

The condition \(wz=1\) then forces

\[
r_1=r_2=r_3=1.
\]

Hence

\[
\boxed{
a_C=(0,0,1,1,1).
}
\]

This matches the already established physical road augmentation \(+1\).

## 3. Lift to the normalization-conductor resolution

Let

\[
0\longrightarrow B
\xrightarrow{\nu}
B_+\oplus B_-
\xrightarrow{\epsilon_+-\epsilon_-}
C_{\rm cond}
\longrightarrow0
\]

be the normalization-conductor exact sequence, and define

\[
T=
[B\xrightarrow{\nu}B_+\oplus B_-].
\]

There is a canonical quasi-isomorphism

\[
\rho:T\longrightarrow C_{\rm cond}
\]

induced in degree zero by \(\epsilon_+-\epsilon_-\).

Therefore \(\rho[1]\) is invertible in the derived category, and the physical
source comparison is

\[
\boxed{
a
=
\rho[1]^{-1}\circ a_C:
J\longrightarrow T[1].
}
\]

Equivalently, it is represented by the roof

\[
\boxed{
J
\xrightarrow{\,a_C\,}
C_{\rm cond}[1]
\xleftarrow[\sim]{\,\rho[1]\,}
T[1].
}
\]

This is the correct integral construction: it uses the normalization exact
sequence itself and does not choose either sheet as a global \(B\)-linear
section.

## 4. Physical normalization

The map has the required primitive normalization

\[
a_*([z])=1\in H_1(T[1])\cong C_{\rm cond}.
\]

The physical \(Q\)-roof has independently established coefficient \(+1\), so
the source comparison preserves the chosen primitive orientation at the
coefficient level.

The endpoint coordinates are killed strictly by \(a_C\).  The three road
coordinates enter only through their oriented augmentation.

Under physical reflection the road orientation and the conductor polarity
line are both odd; their product is even.  Thus the comparison has the same
loaded reflection parity as the physical line.

## 5. Uniqueness

Among integral chain maps

\[
J\to C_{\rm cond}[1]
\]

which

1. vanish on the two endpoint coordinates, and
2. send the primitive physical cycle \(z\) to \(+1\),

\(a_C\) is unique strictly, not merely up to homotopy.

Since \(\rho:T\to C_{\rm cond}\) is a fixed quasi-isomorphism, the corresponding
derived morphism

\[
a:J\to T[1]
\]

is unique.

## 6. What this does and does not solve

The missing source comparison is therefore constructed:

\[
\boxed{
a:J\to T[1].
}
\]

For the kernel-derived conductor homotopy

\[
k_\nu:T[1]\to V
\]

one may now form

\[
H_{\rm cond}^{\nu}=k_\nu a.
\]

The next test is not existence of \(a\).  It is whether the ordinary primitive
appearing in

\[
H_{\rm cond}^{\nu}-e_\nu h_{\rm Morse}
\]

is admissible in the fully framed physical mapping fibre.

A separate comparison is still required if one wants to identify the
seven-triangle corrected Morse complex itself, before the physical
derived-pullback construction, with this \(J\) chain model.
