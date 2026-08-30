# The prime-two one-label constructor packet has four explicit Gaussian grades

## Exact local defect

Let

\[
f_j(x)=x^je^{-\pi x^2},
\qquad
L=\log2.
\]

The exact positive-ray translation defect is

\[
\mathcal R_2
=
U_L
\left[
-2L(A+1)D+L^2D^2
\right].
\]

On the Gaussian seed,

\[
(A+1)Df_0
=
-4\pi f_1+4\pi^2f_3,
\]

and

\[
D^2f_0
=
-2\pi f_0+4\pi^2f_2.
\]

Therefore

\[
\mathcal R_2f_0
=
U_L
\left[
-2\pi L^2f_0
+
8\pi Lf_1
+
4\pi^2L^2f_2
-
8\pi^2Lf_3
\right].
\]

This is the first fully evaluated local constructor packet.

## Numerical coefficient column

In the ordered basis

\[
(f_0,f_1,f_2,f_3),
\]

the pretranslation coefficient column is approximately

\[
\begin{pmatrix}
-3.018775317841\\
17.420688722429\\
18.967524722735\\
-54.728707710857
\end{pmatrix}.
\]

The exact values, rather than the decimal approximations, remain
authoritative.

## Even and odd decomposition

The reciprocal-even part is

\[
E_2
=
-2\pi L^2f_0
+
4\pi^2L^2f_2,
\]

while the reciprocal-odd part is

\[
O_2
=
8\pi Lf_1
-
8\pi^2Lf_3.
\]

Thus

\[
\mathcal R_2f_0
=
U_L(E_2+O_2).
\]

For the opposite translation ray, the odd part reverses sign and the even
part remains:

\[
\mathcal R_2^-f_0
=
U_{-L}(E_2-O_2).
\]

This gives the exact two-ray reciprocal packet before endpoint projection.

## One-label half-density image

At theta label \(n\),

\[
(\mathcal M_nf_j)(u)
=
n^{j+1/2}
e^{(j+1/2)u}
e^{-\pi n^2e^{2u}}.
\]

Hence the pretranslation polynomial packet maps to

\[
\begin{aligned}
\Psi_{2,n}(u)
={}&
-2\pi L^2
n^{1/2}e^{u/2}
e^{-\pi n^2e^{2u}}
\\
&+
8\pi L
n^{3/2}e^{3u/2}
e^{-\pi n^2e^{2u}}
\\
&+
4\pi^2L^2
n^{5/2}e^{5u/2}
e^{-\pi n^2e^{2u}}
\\
&-
8\pi^2L
n^{7/2}e^{7u/2}
e^{-\pi n^2e^{2u}}.
\end{aligned}
\]

At the first label \(n=1\), this is a four-grade
half-density Gaussian packet with exponents

\[
\frac12,
\quad
\frac32,
\quad
\frac52,
\quad
\frac72.
\]

## Consequence for finite truncations

The exact prime-two defect does not land in the earlier three-grade
completion packet. Finite translation adds the fourth grade through the odd
\(f_3\) component, while the even \(D^2\) correction supplies \(f_0\) and
\(f_2\).

Any first-prime checker restricted to three grades necessarily discards a
source term.

## Ordered-port action

The odd Wronskian port satisfies

\[
j_\theta\Omega=A.
\]

Since

\[
O_2=L\Omega f_0,
\]

with \(\Omega=-2(A+1)D\), one gets

\[
j_\theta O_2
=
LAf_0
=
-2\pi Lf_2.
\]

The even packet \(E_2\) remains a separate second-order channel.

## Exact first-prime comparison target

The constructor-identification theorem at \(p=2\) must compare the raw
window boundary

\[
d_2=W_{2L}-W_L
\]

with the completed image of the two-ray packet

\[
U_L(E_2+O_2)
\oplus
U_{-L}(E_2-O_2),
\]

after:

1. moving-center ray sewing;
2. half-density transport;
3. theta label summation;
4. Wronskian odd resolution;
5. tail convolution;
6. relative Green quotient.

## New falsifier

A three-grade implementation can match the wall, first odd response, and one
even completion coefficient while omitting the \(f_3\) term. It will pass
the prior truncated observer but fail the exact finite-translation identity.

## Frontier

The first-prime source side is no longer schematic. It is the explicit
four-grade packet above.

The next calculation is the moving-cut sewing of its two translated rays and
the comparison of the resulting relative boundary with \(d_2\).
