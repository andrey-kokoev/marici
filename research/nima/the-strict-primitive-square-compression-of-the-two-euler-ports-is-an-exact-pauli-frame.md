# The strict primitive-square compression of the two Euler ports is an exact Pauli frame

## Result

Compressing the normalized central Euler current and its first jet to the strict primitive-square boundary plane gives exactly the two Pauli off-diagonal matrices.

Their joint frame operator is

\[
2I.
\]

Thus the strict two-grade Adams boundary has a perfect arithmetic observer frame, independent of the prime. Higher Euler grades do not contaminate this compression; they remain in the connected tail channel.

## Boundary plane

On the bilateral valuation chain, let

\[
Ue_j=e_{j+1}.
\]

The strict primitive-square plane is

\[
E_{12}
=
\operatorname{span}\{e_1,e_2\}.
\]

Let \(P_{12}\) be its orthogonal projector.

For every \(k\ge2\),

\[
P_{12}U^{\pm k}P_{12}=0.
\]

Only the adjacent shift \(k=1\) has a nonzero compression.

## Central current compression

With

\[
a=p^{-1/2},
\]

the self-adjoint central current is

\[
Q_p
=
-i\sum_{k\ge1}
\frac{a^k}{k}
\left(
U^k-U^{-k}
\right).
\]

Therefore

\[
P_{12}Q_pP_{12}
=
-ia
P_{12}(U-U^{-1})P_{12}.
\]

In the ordered basis \((e_1,e_2)\),

\[
\frac1aP_{12}Q_pP_{12}
=
\begin{pmatrix}
0&i\\
-i&0
\end{pmatrix}.
\]

This is a fixed Pauli matrix up to the frozen sign convention. Reversing the boundary orientation changes its sign.

## First-jet compression

The first central jet is

\[
D_p
=
(\log p)
\sum_{k\ge1}
a^k
\left(
U^k+U^{-k}
\right).
\]

Hence

\[
P_{12}D_pP_{12}
=
a(\log p)
P_{12}(U+U^{-1})P_{12}.
\]

In the same basis,

\[
\frac1{a\log p}P_{12}D_pP_{12}
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

This is the complementary Pauli matrix.

The two normalizations are precisely the primitive Euler amplitude and its logarithmic position derivative.

## Exact frame

Write

\[
Y=
\frac1aP_{12}Q_pP_{12},
\qquad
X=
\frac1{a\log p}P_{12}D_pP_{12}.
\]

Then

\[
X^*=X,
\qquad
Y^*=Y,
\]

\[
X^2=I,
\qquad
Y^2=I,
\]

and

\[
XY+YX=0.
\]

For every \(v\in E_{12}\),

\[
\|Xv\|^2+\|Yv\|^2
=
2\|v\|^2.
\]

Thus the joint observer

\[
\mathcal O_{12}v
=
\begin{pmatrix}
Xv\\
Yv
\end{pmatrix}
\]

has exact lower and upper frame bound

\[
\sqrt2.
\]

This bound is independent of \(p\), cutoff, and the theta-sampling coefficient.

## Granularity theorem

The all-grade Euler current decomposes under the strict compression as

\[
P_{12}\mathcal J_pP_{12}
=
P_{12}\mathcal J_{p,1}P_{12}.
\]

Every grade \(k\ge2\) shift leaves the two-dimensional plane before returning. In particular, the square scalar cumulant is not represented as an internal \(e_1\leftrightarrow e_2\) shift of length two. It belongs to the endpoint label/loading and connected external history, not to this adjacent incidence matrix.

This clarifies the typing:

- primitive and square are the two endpoint objects;
- the grade-one shift is their incidence arrow;
- higher shifts are external tail paths;
- Euler coefficients remain endpoint/edge loadings.

Compressing the all-grade operator therefore does not silently import the connected tail into the \(2\times2\) frame.

## Radical behavior

The Pauli pair has no common kernel:

\[
\ker X\cap\ker Y=\{0\}.
\]

Hence no nonzero strict boundary vector is lost before Green quotienting.

If the later Green form has a radical, descent of both ports requires that radical to be zero on this strict plane or be routed into a separately retained wall channel. Quotienting any nonzero vector of \(E_{12}\) would destroy the exact frame and must be source-authorized.

## Mixed-output warning

The exact bound uses the typed direct-sum observer

\[
v\mapsto(Xv,Yv).
\]

It does not apply to an untyped scalar sum

\[
Xv+Yv.
\]

A shared terminal evaluator can create cancellation between the two separately perfect outputs. Therefore the two arithmetic ports must remain separate until the global mixed-margin or output-angle condition is proved.

This is the finite local instance of the earlier mixed-cancellation margin.

## Constructor consequence

The first strict Adams boundary now has an explicit source-native arithmetic normal form:

\[
\text{primitive-square plane}
\xrightarrow{(X,Y)}
E_{12}\oplus E_{12},
\]

with exact frame operator

\[
X^*X+Y^*Y=2I.
\]

The compact theta incidence may be attached downstream as an additional comparison port without affecting this essential frame.

## Next gate

The next theorem is the Green loading comparison:

> Prove that the source endpoint lifts carry this Pauli frame into the enlarged primitive-square Green cell with bounded triangular realization and without collapsing the two typed outputs at the common evaluator.

This reduces the arithmetic part of endpoint loading to a fixed \(2\times2\) model.
