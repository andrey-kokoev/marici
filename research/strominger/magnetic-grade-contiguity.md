# Pole-depth transport closes on three adjacent grades

Introduce the exponential grade-generating function of the source paths:

\[
\mathcal C_a(t,x)
=\sum_{g\ge0}C_{g,a}(x)\frac{t^g}{g!}.
\]

The rising-factorial definition sums exactly:

\[
\boxed{
\mathcal C_a(t,x)=(1+t)^{-a}(1-xt)^{a-4}.
}
\]

Consequently, shifting pole depth by two gives

\[
\mathcal C_{a+2}(t,x)
=\left(\frac{1-xt}{1+t}\right)^2\mathcal C_a(t,x).
\]

After clearing the denominator and extracting the coefficient of `t^g/g!`,
one obtains the exact contiguous law

\[
\begin{aligned}
C_{g,a+2}+2gC_{g-1,a+2}+g(g-1)C_{g-2,a+2}
={}&C_{g,a}-2gxC_{g-1,a}\\
&+g(g-1)x^2C_{g-2,a}.
\end{aligned}
\]

This is the finite source transport sought in the determinant programme.  It
has intrinsic order two and closes on the adjacent grades `g,g-1,g-2`.
Attempts to close `a -> a+2` using only differential transforms within one
fixed grade fail from grade four onward because they discard these required
lower-grade states.

The square

\[
\left(\frac{1-xt}{1+t}\right)^2
\]

is also conceptually revealing: pole depth advances by transporting two copies
of the same reflection character.  The rising factorial determinant factors
are exterior characters of this bigraded transport.

The next derivation should apply the magnetic Euler operator

\[
x(1+x)\partial_x+m+(m-g)x
\]

to this three-grade recurrence, while shifting the branch exponent `m` with
`a`.  That produces a fixed local elimination identity for the actual magnetic
columns and should yield the observed parity transfer multipliers without a
growing determinant calculation.

The checker verifies the formal generating function through grade 30 and the
contiguous recurrence through grade 20, with explicit order-one and
one-memory falsifiers.
