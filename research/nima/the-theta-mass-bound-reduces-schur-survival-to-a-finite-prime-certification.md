# The theta-mass bound reduces Schur survival to a finite-prime certification

## Explicit reciprocal resolvent

In the frozen completed-theta normalization,

\[
M_\Phi
=
\xi\!\left(\frac12\right)
\approx0.497120778.
\]

For

\[
D_{p,\pm}
=
\frac12(I\pm iH_\Phi)^*(I\pm iH_\Phi),
\]

the normal-convolution estimate gives

\[
D_{p,\pm}
\ge
\frac{(1-M_\Phi)^2}{2}I
\]

and hence

\[
\|D_{p,\pm}^{-1}\|
\le
\frac{2}{(1-M_\Phi)^2}.
\]

This bound is uniform in prime and reciprocal sheet once constructor
identification places the same normalized theta history in every labelled
fiber.

## Loading estimate

With

\[
d_p=W_{2\log p}-W_{\log p}
\]

and

\[
q_{p,\pm}
=
\langle d_p,D_{p,\pm}^{-1}d_p\rangle,
\]

one obtains

\[
q_{p,\pm}
\le
\frac{2}{(1-M_\Phi)^2}
\|d_p\|_\nu^2.
\]

The Wronskian rank-one survival condition

\[
q_{p,\pm}<16a_p
\]

therefore follows from

\[
\|d_p\|_\nu^2
<
8(1-M_\Phi)^2a_p.
\]

Numerically,

\[
8(1-M_\Phi)^2
\approx2.022.
\]

Thus the sufficient right-hand side is approximately \(2.022a_p\).

## Automatic large-prime regime

The endpoint energy satisfies

\[
a_p=\|W_{\log p}\|_\nu^2\longrightarrow1,
\]

while

\[
\|d_p\|_\nu^2
\le
C^2(\log p)^{-1}
\exp\left(
-\frac\pi4(\log p)^2
\right).
\]

Therefore the loading inequality holds automatically for all sufficiently
large primes, with a rapidly growing margin.

The Schur-survival audit is consequently finite:

1. derive a certified tail threshold \(P_0\) from the Gaussian estimate;
2. evaluate rigorous upper bounds for \(\|d_p\|_\nu^2\) for
   \(p<P_0\);
3. evaluate rigorous lower bounds for \(a_p\);
4. verify
   \[
   \|d_p\|_\nu^2
   <
   8(1-M_\Phi)^2a_p
   ]
   on that finite list.

No infinite-prime optimization remains.

## Integral formulas

The finite quantities are explicit Gaussian integrals. With

\[
W_L(q)
=
-\int_{q-L}^{q+L}e^{-\pi x^2}\,dx,
\qquad
d\nu(q)=e^{-\pi q^2}\,dq,
\]

one has

\[
a_p
=
\int_{\mathbb R}
|W_L(q)|^2e^{-\pi q^2}\,dq,
\]

and

\[
\|d_p\|_\nu^2
=
\int_{\mathbb R}
|W_{2L}(q)-W_L(q)|^2
e^{-\pi q^2}\,dq,
\qquad
L=\log p.
\]

Certified interval quadrature with explicit Gaussian tail bounds can decide
the finite inequalities without fitting any constructor parameter.

## Exact-symbol improvement

The mass estimate is not the sharp resolvent. Under Fourier transform,

\[
D_\pm^{-1}
\longleftrightarrow
\frac{2}{|1\pm im(\xi)|^2}.
\]

If the transformed incidence \(\widehat d_p\) is available, then

\[
q_{p,\pm}
=
2\int_{\mathbb R}
\frac{|\widehat d_p(\xi)|^2}
{|1\pm im(\xi)|^2}
\,d\xi.
\]

This exact integral may certify a small prime even when the uniform
theta-mass bound fails. It also records the difference between reciprocal
sheets.

## Authority order

The finite numerical certificate remains downstream of two source theorems:

- \(J_{\mathrm{src}}e_p=d_p\) in the common relative Green quotient;
- the shifted auxiliary block is exactly the normalized theta-history square.

Numerical smallness cannot establish either identification.

## Minimal hostiles

1. Verify the finite inequalities using the wrong theta normalization.
2. Replace rigorous lower bounds for \(a_p\) by sampled values.
3. Use the mass bound on a prime-scaled history without including its
   amplitude.
4. Prove eventual Gaussian decay but omit the explicit finite threshold.
5. Pass both norm bounds while reversing the reciprocal linking orientation.

## Verdict

Conditional on the two remaining constructor identifications, local
Wronskian Schur survival is no longer an infinite analytic problem. The exact
theta mass and super-Gaussian disagreement decay reduce it to certified
quadrature for finitely many small primes.

This is the first point at which the remaining local coercivity margin has a
fully explicit finite verification programme.
