# Arithmetic sampling supplies the exact shear that removes the Clark Jordan coupling

Status: exact gauge reduction; positivity after sampling and reflection remains open

Nima's Clark-differentiated tail features obey

\[
 G_q=-sG-f,
 \qquad
 H_q=-sH+aG-f,
 \qquad s=\frac12+iz,                                 \tag{1}
\]

with `f(q)=e^(-q/2)phi(q)>0`.  The homogeneous part has one nonzero Jordan
coupling `aG`.

## Exact scale-dependent shear

Define

\[
 \boxed{K(q,z)=H(q,z)-aq\,G(q,z).}                    \tag{2}
\]

Differentiating and using (1) gives

\[
 \begin{aligned}
 K_q
 &=H_q-aG-aqG_q\\
 &=-sH+aG-f-aG+aq(sG+f)\\
 &=-sK+(aq-1)f.
 \end{aligned}
\]

Hence

\[
 \boxed{K_q=-sK+(aq-1)f.}                            \tag{3}
\]

The Jordan coupling has vanished.  Its price is not a new continuum defect,
but the single source-fixed sign transition in the forcing at `q=1/a`.

No constant change of metric can perform this reduction because the required
shear depends on the scale coordinate.  The transformation matrix is

\[
 \binom GK=
 \begin{pmatrix}1&0\\-aq&1\end{pmatrix}
 \binom GH.                                           \tag{4}
\]

It is regular on every finite scale interval and has determinant one.

## Sampling turns the shear into the arithmetic repair

At the physical scale samples `q=log n`, equation (2) becomes

\[
 \boxed{
 H(\log n,z)
 =K(\log n,z)+a\log n\,G(\log n,z).
 }                                                     \tag{5}
\]

The second term is exactly the logarithmic repair cocycle derived from

\[
 [M_a,S_n]=a\log n\,S_n.                              \tag{6}
\]

Meanwhile, direct substitution in the tail integral shows that `K(log n,z)`
is the scale transport of the primitive signed fold with no displacement
repair.  Thus (5) identifies the Jordan decomposition with the arithmetic
one:

\[
 \boxed{
 \text{Clark feature}
 =\text{transported primitive fold}
 +\text{positive logarithmic repair}.
 }                                                     \tag{7}
\]

The match is exact and explains why the coefficient `log n` appears in both
real-space fold displacement and scale-flow Jordan theory.

## The sheared Green identity has positive bulk

Put

\[
 g_a(q)=(aq-1)f(q).
\]

Although `g_a` changes sign, equation (3) has the scalar forced-flow form
`K_q=-sK+g_a`.  Integrating the derivative of
`K(q,z)overline{K(q,w)}` gives

\[
 \boxed{
 \begin{aligned}
 i(\bar w-z)\int_0^\infty K_z\overline{K_w}\,dq
 ={}&\int_0^\infty(K_z-g_a)
 \overline{(K_w-g_a)}\,dq\\
 &-\int_0^\infty g_a(q)^2dq
 -K(0,z)\overline{K(0,w)}.
 \end{aligned}
 }                                                     \tag{8}
\]

Thus the sheared chart contains no indefinite continuum pair.  It has a
positive bulk and two rank-one lines, exactly like the undifferentiated tail
flow.

Spectral independence alone does **not** make the line `int g_a^2` cancel.
Clark reflection reverses the fold orientation `a -> -a`, so

\[
 g_a=(aq-1)f,
 \qquad
 g_{-a}=(-aq-1)f.                                    \tag{9}
\]

Therefore the reflected difference is

\[
 \boxed{
 \int_0^\infty(g_a^2-g_{-a}^2)dq
 =-4a\int_0^\infty qf(q)^2dq\ne0.
 }                                                     \tag{10}
\]

The surviving quantity

\[
 M_1=\int_0^\infty q e^{-q}\phi(q)^2dq>0             \tag{11}
\]

is a source-fixed, sheet-odd first-moment line.  It may cancel in a genuinely
bilateral Green identity if the oriented scale coordinate is sewn by
`q -> -q`, but that cancellation is not present in the one-sided tail chart
and must not be assumed.

At the seam,

\[
 K(0,z)=H(0,z),                                       \tag{12}
\]

so the seam is the same primitive Clark feature already identified before
shearing.  The `U_+/-` indefinite continuum split is a coordinate
presentation of the Jordan flow, but the sheared presentation retains two
source-fixed defect lines: the primitive seam and `M_1`.

## Relation to the continuum signature

Nima's diagonal channels

\[
 U_\pm=(H\pm G)/\sqrt2
\]

become

\[
 U_+=\frac{K+(aq+1)G}{\sqrt2},
 \qquad
 U_-=\frac{K+(aq-1)G}{\sqrt2}.                       \tag{13}
\]

Therefore the negative `U_+` channel is not an unrelated continuum sector.
It is a fixed polarization of the primitive feature `K` and the arithmetic
repair carrier `qG`.  Sampling at `q=log n` supplies precisely the shear
coefficient needed to distinguish them.

## What remains

Equation (3) does not prove positivity.  Its forcing `(aq-1)f` is signed, and
the hostile-source theorem shows that one fold alone is insufficient.
Instead, (5) says exactly what arithmetic sewing must accomplish: the sampled
positive term `a log(n)G` must repair the transported `K` channel after all
labels and the reflected chamber are assembled.

The next admissible identity should be written in the sheared variables and
have the form

\[
 \text{de Branges current}
 =\text{positive }G\text{-bulk}
 +\sum_n\text{sampled shear loss}
 -\text{one }K\text{-seam form}
 -\text{one sheet-odd moment line}.                  \tag{14}
\]

The mechanism is falsified if the exact sampling formula leaves a third
independent negative polarization beyond the seam and sheet-odd moment.  It
succeeds only if arithmetic/bilateral sewing accounts canonically for both
of those declared defects.
