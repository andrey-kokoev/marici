# Strict theta monotonicity follows from a two-line Gaussian tail bound

## Result

For the completed theta kernel

\[
\Phi(u)
=
\sum_{n\ge1}
e^{u/2}e^{-x_n}(4x_n^2-6x_n),
\qquad
x_n=\pi n^2e^{2u},
\]

one has

\[
\Phi'(u)<0
\qquad(u>0).
\]

The only non-termwise interval identified previously can be closed by a coarse rational estimate with a large margin.

## Derivative reduction

Let

\[
Q(y)=8y^2-30y+15
\]

and put

\[
x=\pi e^{2u}.
\]

Then

\[
Phi'(u)
=
-e^{u/2}D(x),
\]

where

\[
D(x)
=
\sum_{nge1}
G(n^2x),
\qquad
G(y)=yQ(y)e^{-y}.
\]

Evenness of \(\Phi\) gives

\[
D(\pi)=0.
\]

For

\[
\pi<xle r_+
=
\frac{15+\sqrt{105}}8,
\]

it is enough to prove \(D'(x)>0\).

Differentiate:

\[
D'(x)
=
\sum_{nge1}
n^2e^{-n^2x}P(n^2x),
\]

with

\[
P(y)
=
-8y^3+54y^2-75y+15.
\]

## Positive first-label bound

The interval satisfies

\[
3<\pi<x<r_+<\frac{16}{5}.
\]

Moreover,

\[
P'(y)=-24y^2+108y-75>0
\]

on \([3,16/5]\). Hence

\[
P(x)>P(3)=60.
\]

Using

\[
e^{16/5}<25,
\]

the first label obeys

\[
e^{-x}P(x)
>
\frac{60}{25}
=
\frac{12}{5}.
\]

## Complete tail bound

For \(n\ge2\),

\[
y=n^2x>12.
\]

On \([12,\infty)\), \(P(y)<0\), and

\[
-P(y)
=
8y^3-54y^2+75y-15
<
8y^3.
\]

Therefore

\[
\left|
\sum_{n\ge2}
n^2e^{-n^2x}P(n^2x)
\right|
<
8x^3
\sum_{n\ge2}
n^8e^{-n^2x}.
\]

Since \(x>3\) and \(x<16/5\),

\[
8x^3
\sum_{n\ge2}
n^8e^{-n^2x}
<
8\left(\frac{16}{5}\right)^3
\sum_{n\ge2}n^8e^{-3n^2}.
\]

The elementary exponential-series bounds

\[
e^{12}>160000,
\qquad
e^{27}>10^{11}
\]

and the ratio estimate for \(n\ge3\) give

\[
\sum_{n\ge2}n^8e^{-3n^2}
<
\frac1{600}.
\]

Thus the full negative tail has magnitude less than

\[
\frac{32768}{75000}
<
\frac{11}{25}.
\]

## Strict departure from the seam

Combining the two estimates,

\[
D'(x)
>
\frac{12}{5}
-
\frac{11}{25}
=
\frac{49}{25}
>0
\]

throughout \((\pi,r_+]\).

Since \(D(\pi)=0\),

\[
D(x)>0
\qquad
(\pi<x\le r_+).
\]

For \(x>r_+\), every \(Q(n^2x)\) is positive, so \(D(x)>0\) termwise. Consequently,

\[
D(x)>0
\qquad(x>\pi),
\]

and therefore

\[
\Phi'(u)<0
\qquad(u>0).
\]

## Authority and convergence

The theta series and all differentiated series above converge normally on compact subsets of \([0,\infty)\), because polynomial factors in \(n^2e^{2u}\) are dominated by the Gaussian

\[
e^{-\pi n^2e^{2u}}.
\]

Termwise application of \(\partial_u^2-1/4\), the additional derivative, and the rearranged tail estimates are therefore valid.

The identity \(D(\pi)=0\) is not numerical. It follows from the source modular relation

\[
\Phi(-u)=\Phi(u).
\]

## One-sided transfer consequence

Because \(\Phi\) is nonnegative, integrable, and now strictly decreasing on the positive half-line, its Laplace transfer

\[
m_\Phi(z)
=
\int_0^\infty\Phi(u)e^{-zu}\,du
\]

satisfies

\[
\operatorname{Re}(z,m_\Phi(z))>0
\qquad
(\operatorname{Re}z>0).
\]

Hence

\[
m_\Phi(z)\ne0
\qquad
(\operatorname{Re}z>0).
\]

The causal theta propagation therefore has no open-sector Blaschke zeros. Any completed zero must arise after reciprocal sewing or boundary-value combination.

## Remaining outer-factor qualification

Strict monotonicity closes the zero-free half-plane gate. Full outerness still requires the Hardy logarithmic-integrability statement and exclusion of a singular or delay factor in the exact weighted class.

The source already supplies the relevant evidence:

- rapid theta decay gives analytic continuation across finite boundary arcs;
- \(\Phi(0)>0\) gives
  \[
  m_\Phi(x)\sim\Phi(0)/x,
  ]
  excluding a positive delay.

The remaining step is to write these facts as a canonical Hardy-factor theorem in the declared half-plane rigging.

## Verification target

A checker need only certify the rational inequalities used above:

\[
r_+<16/5,
\quad
P'|_{[3,16/5]}>0,
\quad
e^{16/5}<25,
\quad
e^{12}>160000,
\quad
e^{27}>10^{11},
\]

and the geometric ratio bound for the \(n\ge3\) tail. No floating-point theta summation is required.
