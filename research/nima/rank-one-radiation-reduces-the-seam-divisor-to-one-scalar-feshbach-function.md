# Rank-one radiation reduces the seam divisor to one scalar Feshbach function

The rank-two boundary model admits an exact reduction once the radiation form has rank one.

Let
\[
A(x)
=
\Theta-M_{+}(x)
=
F(x)-iW(x),
\]
where
\[
F(x)=\Theta-\operatorname{Re}M_{+}(x)
\]
is self-adjoint and
\[
W(x)=\operatorname{Im}M_{+}(x)\ge0
\]
has rank one.

Choose an orthonormal frame
\[
(d(x),r(x))
\]
with
\[
d(x)\in\ker W(x),
\qquad
W(x)r(x)=w(x)r(x),
\qquad
w(x)>0.
\]

In this frame,
\[
A(x)
=
\begin{pmatrix}
a(x)&b(x)\\
\overline{b(x)}&c(x)-iw(x)
\end{pmatrix},
\]
where
\[
a=\langle d,Fd\rangle,
\qquad
b=\langle d,Fr\rangle,
\qquad
c=\langle r,Fr\rangle.
\]

The radiative block
\[
c(x)-iw(x)
\]
is always invertible because its imaginary part is strictly negative. Therefore the full Evans determinant factors:
\[
\det A(x)
=
\bigl(c(x)-iw(x)\bigr)\,\mathcal E(x),
\]
where the reduced Feshbach function is
\[
\mathcal E(x)
=
a(x)
-
\frac{|b(x)|^{2}}{c(x)-iw(x)}.
\]

Since the radiative factor is zero-free, the complete seam divisor belongs to the scalar function \(\mathcal E\).

Its imaginary part is
\[
\operatorname{Im}\mathcal E(x)
=
-
\frac{|b(x)|^{2}w(x)}
{c(x)^{2}+w(x)^{2}}
\le0.
\]
Hence
\[
\mathcal E(x)=0
\]
forces
\[
b(x)=0
\]
and then
\[
a(x)=0.
\]

This recovers the two independent closed-state conditions automatically:

- \(b=0\): the reactive operator preserves the dark line, so no radiative component is generated;
- \(a=0\): the reactive phase on the dark line matches the boundary condition.

Thus a scalar expectation \(a=0\) alone is insufficient. The mixed dark-to-radiative coupling \(b\) must vanish as well.

At a true zero \(x_0\),
\[
F(x_0)d(x_0)=0.
\]
Because \(b(x_0)=0\), differentiating the Schur complement yields
\[
\mathcal E'(x_0)
=
\left\langle
d(x_0),
F'(x_0)d(x_0)
\right\rangle.
\]
The derivatives of the moving frame and of the quadratic correction disappear at the exact operator kernel.

Therefore the crossing-sign theorem has one scalar target:
\[
\left\langle
d(x_0),
F'(x_0)d(x_0)
\right\rangle
\]
must be nonzero, and preferably have a fixed sign at every zero.

This is a strong contraction of the multiplicity problem. For a simple zero,
\[
\mathcal E(x_0)=0,
\qquad
\mathcal E'(x_0)\neq0.
\]
For higher multiplicity, the order of \(\mathcal E\) is the Evans multiplicity because the radiative factor never vanishes.

The formula also identifies the mixed-cancellation margin away from seam zeros:
\[
\frac{|b|^{2}w}{c^{2}+w^{2}}
\]
is the strictly dissipative penalty for coupling the dark candidate into the radiative channel. It prevents an approximate dark phase match from becoming a true closed state.

Completion requires uniform control of the denominator:
\[
w(x)\ge w_0>0
\]
on compact seam intervals away from thresholds, together with bounded \(c(x)\). If \(w\to0\), the radiative elimination becomes singular and the rank-one model changes type.

The smallest hostile solves only
\[
a(x_0)=0
\]
while \(b(x_0)\neq0\). It finds a scalar dark expectation zero, but the state leaks radiation and the full Evans determinant remains nonzero.

A second hostile has \(a=b=0\) but
\[
\langle d,F'd\rangle=0.
\]
Kernel dimension one does not imply a simple zero.

A third hostile lets \(w(x_X)\to0\) with cutoff, so finite Feshbach reductions exist but no uniform radiative quotient survives completion.

The next source calculation is now explicit: in the wall/disagreement boundary frame, compute the four scalars
\[
a(x),\quad b(x),\quad c(x),\quad w(x).
\]
The completed RH divisor, if this regime is correct, is the scalar Feshbach function \(\mathcal E(x)\).
