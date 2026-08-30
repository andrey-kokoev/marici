# The final forcing obstruction is the odd transform of source autocorrelation

## Correct antidiagonal zero-state

For the completed real half-line source \(f\), define

\[
H_+(q,z)
=
\int_q^\infty f(v)e^{z(v-q)}\,dv,
\]

and

\[
H_-(q,z)
=
\int_q^\infty f(v)e^{-z(v-q)}\,dv.
\]

The completed scalar section is

\[
X(z)=H_+(0,z)+H_-(0,z).
\]

Therefore a zero imposes the antidiagonal interface condition

\[
H_-(0,z)=-H_+(0,z),
\]

not separate vanishing of the two tails.

The flux

\[
J=|H_+|^2-|H_-|^2
\]

vanishes at the interface and at infinity, while

\[
N=|H_+|^2+|H_-|^2
\]

is strictly positive for every nonzero state.

## Exact remaining forcing term

The doubled Green identity reduces every zero-state to

\[
2\Re(z)\int_0^\infty N(q,z)\,dq
=
-2I_f(z),
\]

where

\[
I_f(z)
=
\int_0^\infty
f(q)\Re\left(H_+(q,z)-H_-(q,z)\right)\,dq.
\]

Thus all RH-bearing content is now in \(I_f\).

## Autocorrelation reduction

Define the one-sided source autocorrelation

\[
K_f(r)
=
\int_0^\infty f(q)f(q+r)\,dq,
\qquad
r\ge0.
\]

Changing variables \(v=q+r\) gives the exact complex forcing function

\[
C_f(z)
=
\int_0^\infty
f(q)\left(H_+(q,z)-H_-(q,z)\right)\,dq
=
2\int_0^\infty K_f(r)\sinh(zr)\,dr.
\]

The Green obstruction is

\[
I_f(z)=\Re C_f(z).
\]

Hence the final obstruction is the odd Laplace transform of a positive
autocorrelation kernel.

## Immediate orientation and its limit

If \(z=x\) is real and \(x>0\), then

\[
K_f(r)\ge0
\]

and

\[
\sinh(xr)>0
\]

for \(r>0\). Therefore

\[
C_f(x)>0
\]

for every nontrivial positive source with nonzero correlation away from the
origin.

The Green identity then forbids a real zero with \(x>0\). Reciprocal symmetry
gives the opposite side.

At nonzero spectral height, however,

\[
\Re\sinh((x+it)r)
=
\sinh(xr)\cos(tr).
\]

The cosine oscillation destroys the sign. Positivity of the source
autocorrelation alone cannot confine complex zeros.

## Product decomposition

Let

\[
F(z)=\int_0^\infty f(v)e^{zv}\,dv.
\]

Then \(X(z)=F(z)+F(-z)\), while

\[
F(z)F(-z)
=
2\int_0^\infty K_f(r)\cosh(zr)\,dr.
\]

The scalar section sees the even autocorrelation transform. The forcing
obstruction is its odd ordered companion.

A zero of \(X\) constrains the sum \(F(z)+F(-z)\), but does not determine the
odd ordering transform \(C_f(z)\). This is why the antidiagonal boundary
condition kills flux without killing forcing.

## Smallest hostile witness

Take the positive two-shell source

\[
f=a\delta_1+b\delta_2,
\qquad
a,b>0.
\]

Its off-diagonal autocorrelation is concentrated at separation \(1\), so

\[
C_f(z)=2ab\sinh z.
\]

Choose

\[
z=y+i\pi,
\qquad
y\ne0,
\]

and

\[
b=a\frac{\cosh y}{\cosh 2y}.
\]

Then

\[
X(z)=0,
\]

but

\[
C_f(z)=-2ab\sinh y\ne0.
\]

Smooth narrow positive bumps preserve the counterexample after a small
parameter adjustment.

Therefore no conservation theorem based only on positivity, rapid decay,
reciprocal doubling, and the antidiagonal boundary condition can eliminate
the forcing term.

## Exact source discriminator required

The theta source must contribute an additional identity acting on
\(K_f\) or its odd transform. Candidate origins are:

- the global Fourier–Poisson correspondence;
- labelled prime-exclusion recursion;
- the square cumulant and connected determinant packet;
- the archimedean line incidence;
- a source-derived differential equation for the autocorrelation.

The required law must fail for the two-shell hostile before its zero is
inspected.

## Finite and symbolic falsifier

For any proposed modular current \(J_{\mathrm{mod}}\), compute

\[
R_f(z)
=
C_f(z)-\partial J_{\mathrm{mod}}(z)
\]

on a source-authorized core. Test first on:

1. one shell, where the odd correlation vanishes;
2. two shells, where \(C_f(z)=2ab\sinh z\);
3. three labelled shells, where distinct separations test interference;
4. the actual theta source.

If the proposed law cancels every positive two-shell source, it is universal
and cannot distinguish theta. If it fails on theta, the route closes. If it
holds only through a labelled theta recursion, that recursion is the desired
source-specific mechanism.

## Disposition

The final conservation DPC no longer has a vague forcing term. Its obstruction
is a canonical quadratic source object:

\[
C_f(z)
=
2\int_0^\infty K_f(r)\sinh(zr)\,dr.
\]

RH-strength progress now requires a theta-specific law converting this odd
autocorrelation transform into completed boundary flux. Every preceding gate
is already solved or separately typed.
