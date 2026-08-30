# Theta transported incidence loop is nonzero off and on the seam

## Bounded question

Does composing the opposite incidence arrows through explicit reciprocal
sewing produce a critical-seam discriminator?

## Typed transported loop

Let the direct and dual carriers be

\[
X_+=Y_+\oplus F_+,
\qquad
X_-=Y_-\oplus F_-.
\]

The two source-derived arrows are

\[
p_+:F_+\longrightarrow Y_+,
\qquad
q_-:Y_-\longrightarrow F_-.
\]

Choose only explicit sewing identifications

\[
U_Y:Y_+\longrightarrow Y_-,
\qquad
V_F:F_+\longrightarrow F_-.
\]

Transporting the dual arrow back to the direct carrier gives

\[
\widetilde q_+=V_F^{-1}q_-U_Y,
\]

and the closed endpoint loop is

\[
\kappa_+=p_+V_F^{-1}q_-U_Y:Y_+\longrightarrow Y_+.
\]

This formula keeps the sewing frame visible. Writing down
\(p_+q_-\) without the two comparison maps is ill-typed.

## Rank-one theorem

For the scalar theta tail, both endpoint and forcing fibers have rank one.
Hence, whenever the two sewing maps are invertible,

\[
\kappa_+=0
\quad\Longleftrightarrow\quad
p_+=0\ \lor\ q_-=0.
\]

The source tail has

\[
p_s(q)=-f(q)e^{sq}.
\]

In the adjoint source frame,

\[
q_s(q)=\overline{p_s(q)}.
\]

Thus at every interior point where \(f(q)\ne0\), the transported loop is
nonzero for every invertible sewing. On the unitary seam, choosing the common
native frame gives

\[
\kappa_s(q)=|p_s(q)|^2>0.
\]

Away from the seam, an invertible Tate comparison changes this scalar by a
nonzero transition factor. It cannot create or remove its zero set.

## Consequence

Closing the two directional arrows is source-faithful, but not
critical-line-selective. It detects whether the local source forcing is
present. It does not detect a zero of the completed scalar transform and does
not distinguish the seam from either open sector.

This is the same structural warning encountered for the completed endpoint
shear: an invertible full transport remains regular at scalar transmission
zeros. Here the closed local incidence loop remains nonzero there as well.

## Higher-rank pressure point

Kitaev's orthogonality hostile becomes relevant only after the forcing port is
enlarged. For rank greater than one, nonzero \(p_+\) and \(q_-\) do not imply
nonzero \(\kappa_+\), because the transported image of \(q_-\) may lie in
\(\ker p_+\).

The scalar tail therefore cannot supply the desired selection law by itself.
Any seam-sensitive mechanism must live in a larger labelled forcing module,
where the relative orientation of the two incidence subspaces is meaningful.

## Smallest rank-two hostile

Take one-dimensional endpoint fibers and a two-dimensional forcing fiber. In
a common orthonormal frame, let

\[
P=\begin{pmatrix}1&0\end{pmatrix},
\qquad
Q=\binom10.
\]

Both arrows are nonzero, and without forcing-space transport their loop is
one. Now use the unitary forcing comparison

\[
V=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\qquad
U_Y=1.
\]

Then

\[
PV^{-1}QU_Y=0.
\]

Thus even unitary sewing, nonzero arrows, equal ranks, and an adjoint relation
before sewing do not protect the transported loop. The obstruction is the
principal angle between the transported dual image and the direct observed
line.

For one-dimensional endpoint fibers the exact invariant is

\[
\tau_s=
\frac{|P_sV_F^{-1}Q_sU_Y|}
{\|P_s\|\,\|V_F^{-1}Q_sU_Y\|}.
\]

It lies between zero and one whenever the forcing metric is positive. The
rank-two hostile has \(\tau_s=0\). Any genuine source theorem must therefore
control this normalized incidence angle, not just ranks, norms, unitarity, or
the existence of both arrows.

## Completion hostile

Although the pointwise loop is nonzero, theta decay gives

\[
|\kappa_s(q)|\longrightarrow0
\]

along the far tail in the native unitary frame. Consequently pointwise
nonvanishing does not imply a uniform completed lower bound. An accumulated
loop Gramian can remain positive for each fixed state while losing closed
range under completion.

## Revised target

The next source-native object is not the scalar loop. It is the labelled
transported incidence form

\[
K_s(q)=P_s(q)V_F(s,q)^{-1}Q_s(q)U_Y(s,q),
\]

before arithmetic aggregation. The decisive question is whether Fourier--Tate
sewing forces its image away from the kernel of \(P_s\) in both open sectors,
with the primitive, square, and archimedean ports retained.

The sharp finite observable is the smallest normalized principal-angle
reserve of this pairing. A vanishing reserve gives an exact destructive
incidence despite individually faithful direct and dual ports. A positive
cutoff reserve is only reconnaissance until its behavior under restricted
product completion is controlled.

## Falsifier and scope

A proposed scalar-loop confinement theorem is falsified by any invertible
sewing for which the loop remains nonzero on both sides of the seam; the
rank-one theorem shows this is the generic source situation. A proposed
higher-rank theorem is falsified by a labelled state in

\[
\operatorname{Ran}(V_F^{-1}Q_sU_Y)\cap\ker P_s.
\]

This packet proves that rank-one transported closure has no RH-selective
content and gives the smallest rank-two unitary orthogonality hostile. It does
not construct the labelled forcing module, prove transverse incidence there,
close the global boundary current, or prove RH.
