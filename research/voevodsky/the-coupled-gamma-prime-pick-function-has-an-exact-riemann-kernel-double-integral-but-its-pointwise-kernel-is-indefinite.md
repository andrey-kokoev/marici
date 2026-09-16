# The coupled gamma--prime Pick function has an exact Riemann-kernel double integral, but its pointwise kernel is indefinite

## Objective

Derive an integral representation that couples the gamma and prime terms before taking imaginary parts.

The completed logarithmic derivative does admit such a representation through Riemann's positive theta kernel. After clearing the quotient, the Pick imaginary part becomes one explicit double integral. The resulting pointwise kernel is not sign definite, so this derivation does not by itself prove the Pick inequality. It identifies the exact cancellation that a successful estimate must control.

## Endpoint-reduced logarithmic derivative

Let

\[
z
=
s-
\frac12,
\qquad

t
=
z^2.
\]

Define

\[
\Xi(z)
=
\xi
\left(
\frac12+z
\right).
\]

Then \(\Xi\) is even in \(z\). The completed logarithmic derivative satisfies

\[
\frac{
\xi'(s)
}
{
\xi(s)
}
=
\frac1s
+
\frac1{s-1}
-
\frac12
\log\pi
+
\frac12
\psi(s/2)
+
\frac{
\zeta'(s)
}
{
\zeta(s)
}.
\]

Since

\[
\frac{
4s(s-1)
}
{
2s-1
}
\left(
\frac1s
+
\frac1{s-1}
\right)
=4,
\]

the endpoint-reduced Pick inequality is equivalent to

\[
\operatorname{Im}
\left[
\frac{
4s(s-1)
}
{
2s-1
}
\frac{
\xi'(s)
}
{
\xi(s)
}
\right]
\ge0,
\]

because the removed constant four is real.

In centered coordinates, define

\[
F(t)
=
\frac{
4z^2-1
}
{
2z
}
\frac{
\Xi'(z)
}
{
\Xi(z)
}.
\]

This agrees with the endpoint-reduced gamma--prime Pick function on the chosen square-root sheet.

## Riemann theta kernel

Use the standard positive Riemann kernel \(\Phi(u)\), normalized so that

\[
\Xi(z)
=
\int_0^\infty
\Phi(u)
\cosh(zu)
\,du.
\]

The precise rescaling of \(u\) depends on the convention for \(\Xi\); all formulas below transform covariantly under that rescaling.

The classical theta-series expression gives

\[
\Phi(u)
>0
\qquad
(u>0),
\]

and rapid superexponential decay as \(u\to\infty\).

Differentiation under the integral gives

\[
\Xi'(z)
=
\int_0^\infty
u
\Phi(u)
\sinh(zu)
\,du.
\]

Set

\[
D(z)
=
\int_0^\infty
\Phi(v)
\cosh(zv)
\,dv,
\]

\[
N(z)
=
\int_0^\infty
u
\Phi(u)
\sinh(zu)
\,du,
\]

and

\[
c(z)
=
\frac{
4z^2-1
}
{
2z
}.
\]

Then

\[
\boxed{
F(z^2)
=

c(z)
\frac{
N(z)
}
{
D(z)
}.
}
\]

This is already a fully coupled gamma--prime representation: the Euler and archimedean pieces have recombined into the single positive theta kernel \(\Phi\).

## Double-integral imaginary part

Away from zeros of \(D(z)=\Xi(z)\),

\[
\operatorname{Im}
F(z^2)
=
\frac{
\operatorname{Im}
\left[

c(z)
N(z)
\overline{D(z)}
\right]
}
{
|D(z)|^2
}.
\]

Substituting the two integrals gives

\[
\boxed{
\operatorname{Im}
F(z^2)
=
\frac1{
|D(z)|^2
}
\int_0^\infty
\int_0^\infty
\Phi(u)
\Phi(v)
\mathcal K_z(u,v)
\,du\,dv,
}
\]

where

\[
\boxed{
\mathcal K_z(u,v)
=
\operatorname{Im}
\left[

c(z)

u
\sinh(zu)
\cosh(
\overline z
v)
\right].
}
\]

This is the desired coupled integral before any sectorwise sign estimate.

## Real-variable expansion

Write

\[
z
=
x+iy.
\]

Then

\[
\sinh(zu)
=
\sinh(xu)
\cos(yu)
+
i
\cosh(xu)
\sin(yu),
\]

and

\[
\cosh(
\overline z
v)
=
\cosh(xv)
\cos(yv)
-
i
\sinh(xv)
\sin(yv).
\]

Write

\[
c(z)
=

a(x,y)
+
i
b(x,y).
\]

A direct multiplication yields

\[
\begin{aligned}
\mathcal K_z(u,v)
=u\{&
a(x,y)
[
\cosh(xu)\cosh(xv)\sin(yu)\cos(yv)\\
&\qquad-
\sinh(xu)\sinh(xv)\cos(yu)\sin(yv)
]\\
&+
b(x,y)
[
\sinh(xu)\cosh(xv)\cos(yu)\cos(yv)\\
&\qquad+
\cosh(xu)\sinh(xv)\sin(yu)\sin(yv)
]
\}.
\end{aligned}
\]

with equivalent shorter trigonometric rearrangements available. The unsymmetrized display is less important than the structural fact that both sine and cosine oscillations occur.

A safer computational form is to retain

\[
\mathcal K_z(u,v)
=
\operatorname{Im}
[

c(z)

u
\sinh(zu)
\cosh(
\overline z
v)
].
\]

## Symmetrized kernel

Since the measure

\[
\Phi(u)
\Phi(v)
\,du\,dv
\]

is symmetric, one may replace \(\mathcal K_z\) by

\[
\mathcal K_z^{sym}(u,v)
=
\frac12
\left[
\mathcal K_z(u,v)
+
\mathcal K_z(v,u)
\right].
\]

Then

\[
\operatorname{Im}
F(z^2)
=
\frac1{
|D(z)|^2
}
\iint
\Phi(u)
\Phi(v)
\mathcal K_z^{sym}(u,v)
\,du\,dv.
\]

This form exposes pairwise cancellation and is the natural candidate for integration-by-parts or total-positivity arguments.

## Pointwise sign obstruction

The kernel contains factors

\[
\sin(yu),
\qquad
\cos(yu),
\qquad
\sin(yv),
\qquad
\cos(yv).
\]

For every nonzero \(y\), these change sign as \(u\) and \(v\) vary. The positive weight \(\Phi(u)\Phi(v)\) does not remove that pointwise oscillation.

Therefore

\[
\mathcal K_z^{sym}(u,v)
\]

is not pointwise nonnegative on the full quadrant in general.

The coupled theta representation consequently does not produce a direct positive-measure proof by inspection.

## Small-imaginary expansion

For \(y\) small,

\[
\operatorname{Im}
F((x+iy)^2)
=

y
\partial_x
F(x^2)
+
O(y^3)
\]

with the precise Jacobian determined by the \(t=z^2\) chart.

Equivalently, the boundary Pick sign reduces to monotonicity of the real Loewner function. In the theta quotient this derivative contains the covariance-type expression

\[
\frac{
N'(x)D(x)
-
N(x)D'(x)
}
{
D(x)^2
}

after differentiating the prefactor as well.

The numerator is a symmetrized double integral. Its sign is the rank-two Loewner/Turán gate already identified in the Hankel formulation.

Thus even the boundary linearization retains a nontrivial coupled determinant rather than becoming a one-body positive integral.

## A possible integration-by-parts route

The theta kernel \(\Phi\) is built from derivatives of the Jacobi theta function and satisfies strong decay at both ends after the standard logarithmic change of variables.

A viable proof would need an identity of the form

\[
\iint
\Phi(u)
\Phi(v)
\mathcal K_z^{sym}(u,v)
\,du\,dv
=
\iint
W_z(u,v)
|G_z(u)-G_z(v)|^2
\,du\,dv
\]

with

\[
W_z(u,v)
\ge0.
\]

No such identity follows from the raw quotient representation. Deriving it would be genuinely new positive structure rather than a reformulation of the Pick target.

## Rotor interpretation

If \(D(z)=\Xi(z)\) has a forbidden zero, the quotient has a pole. In the Loewner kernel, its residue produces the finite-rank hostile model-space direction.

The denominator

\[
|D(z)|^2
\]

in the coupled integral makes this explicit: theta-kernel positivity alone cannot control the sign across a forbidden pole. Any successful square-difference identity would simultaneously exclude such poles.

## Practical use

The double-integral formula is useful for:

1. stable numerical evaluation away from zeros;
2. deriving boundary asymptotics without separately truncating primes;
3. testing candidate symmetrizations or integration-by-parts identities;
4. locating which \((u,v)\) regions dominate a near-zero Pick margin;
5. constructing interval enclosures using the rapidly decaying theta kernel.

It is less useful for direct pointwise positivity because the kernel oscillates.

## Scope boundary

The derivation assumes the standard positive Riemann theta-kernel representation and a fixed normalization of its argument. Publication use must align the factors of two in \(u\), \(z\), and the definition of \(\Xi\).

The formula is valid away from zeros of \(\Xi\). Near a zero, one must use a pole-aware enclosure or multiply through by \(|D(z)|^2\).

## Disposition

The coupled integral exists and is exact:

\[
\boxed{
|\Xi(z)|^2
\operatorname{Im}
F(z^2)
=
\iint
\Phi(u)
\Phi(v)
\operatorname{Im}
\left[
\frac{
4z^2-1
}
{
2z
}

u
\sinh(zu)
\cosh(
\overline z
v)
\right]
\,du\,dv.
}
\]

It couples gamma and primes through one positive theta weight, but its oscillatory two-body kernel is indefinite. The next nonredundant question is whether theta identities convert the symmetrized integral into a positive square-difference form.
