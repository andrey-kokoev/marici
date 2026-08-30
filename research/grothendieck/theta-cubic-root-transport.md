# Theta cubic root transport

Author: `marici.Grothendieck`

## Purpose

This packet asks whether the cubic Jensen gate reduces to interlacing of the
already-hyperbolic quadratic Jensen polynomials. The answer is precise:
ordinary interlacing is automatic and too weak. The cubic datum is the
oriented height of a cubic primitive at its two quadratic critical points.

## Intrinsic quadratic roots

Let `b_t` be the Gaussian-normalized moment sequence and put

\[
Q_t(X)=b_{t-1}+2b_tX+b_{t+1}X^2,
\qquad
D_t=b_t^2-b_{t-1}b_{t+1}>0.
\]

Under

\[
Y=X\sqrt{\frac{b_{t+1}}{b_{t-1}}},
\qquad
a_t=\frac{b_t}{\sqrt{b_{t-1}b_{t+1}}}=\cosh\theta_t>1,
\]

the normalized polynomial is `1+2a_tY+Y^2`, with roots

\[
\boxed{Y_{t,-}=-e^{\theta_t},\qquad Y_{t,+}=-e^{-\theta_t}.}
\]

Every quadratic carrier is therefore a reciprocal root pair centered on the
fixed point `-1` of inversion.

## Coercivity length as eccentricity

The quadratic deficit and cubic length are

\[
u_t=1-\frac{b_{t-1}b_{t+1}}{b_t^2}=\tanh^2\theta_t,
\qquad
\boxed{L_t=u_t^{-1/2}=\coth\theta_t.}
\]

Thus the exact cubic Jensen condition is

\[
\boxed{|\coth\theta_{t+1}-\coth\theta_t|\le1.}
\]

It says that one insertion of the radial statistic changes reciprocal-pair
eccentricity by at most one unit.

## Ordinary interlacing is too weak

For `0<theta<psi`, the intrinsic roots obey

\[
-e^\psi<-e^\theta<-e^{-\theta}<-e^{-\psi}.
\]

The root intervals are nested, so they possess a common linear interlacer for
every positive pair `theta,psi`. Yet taking `theta` arbitrarily small makes
`|coth(psi)-coth(theta)|` arbitrarily large. Consequently

\[
\boxed{\text{quadratic real-rootedness plus common interlacing}
\not\Rightarrow\text{cubic hyperbolicity}.}
\]

This exact falsifier rules out any proof that forgets relative normalization
and the cubic integration constant.

## The missing datum is a critical value

For

\[
J_r^{(3)}(X)=b_r+3b_{r+1}X+3b_{r+2}X^2+b_{r+3}X^3,
\]

one has

\[
(J_r^{(3)})'(X)=3Q_{r+2}(X).
\]

Quadratic positivity supplies two distinct negative critical points. A real
cubic with positive leading coefficient has three real roots precisely when
its left critical value is nonnegative and its right critical value is
nonpositive. Hence the faithful condition is

\[
\boxed{
J_r^{(3)}(x_{r,-})J_r^{(3)}(x_{r,+})\le0,
\qquad Q_{r+2}(x_{r,\pm})=0,
}
\]

with orientation fixed by the leading coefficient. The coefficient `b_r` is
the integration constant invisible to the derivative quadratic. Root
locations alone therefore cannot close the theorem.

The discriminant identity makes the equivalence algebraically exact:

\[
\operatorname{disc}(J_r^{(3)})
=-27b_{r+3}^2
 J_r^{(3)}(x_{r,-})J_r^{(3)}(x_{r,+}).
\]

Thus no sign information has been lost in passing from the discriminant to
the two critical values.

## Canonical critical-area interval

Since `J_r^{(3)}(0)=b_r` and `(J_r^{(3)})'=3Q_{r+2}`, define

\[
A_{r,\pm}=3\int_{x_{r,\pm}}^0Q_{r+2}(s)\,ds.
\]

Then

\[
J_r^{(3)}(x_{r,\pm})=b_r-A_{r,\pm}.
\]

The quadratic is negative between its roots and positive to their right, so

\[
A_{r,+}-A_{r,-}
=-3\int_{x_{r,-}}^{x_{r,+}}Q_{r+2}(s)\,ds>0.
\]

Consequently cubic hyperbolicity is exactly the scalar interval condition

\[
\boxed{A_{r,-}\le b_r\le A_{r,+}.}
\]

This is stronger conceptually than the discriminant formula. The derivative
quadratic constructs a canonical admissible interval; the preceding moment
must be centered inside it. The interval width is automatic from quadratic
hyperbolicity. The entire new burden at degree three is the position of one
source-derived scalar within that interval.

It also gives a local falsifier with no root census: either

\[
b_r<A_{r,-}
\qquad\text{or}\qquad
b_r>A_{r,+}.
\]

Each failure identifies which critical lobe has the wrong orientation.

## The three-halves law is the lobe area

Write locally

\[
Q(X)=C+2BX+AX^2,
\qquad D=B^2-AC>0,
\]

where `(A,B,C)=(b_{r+3},b_{r+2},b_{r+1})`. Direct evaluation at

\[
x_\pm=\frac{-B\pm\sqrt D}{A}
\]

gives

\[
A_\pm
=\frac{-2B^3+3ABC\pm2D^{3/2}}{A^2}.
\]

Hence the exact cubic condition is

\[
\boxed{
\left|
b_r-\frac{-2b_{r+2}^3+3b_{r+3}b_{r+2}b_{r+1}}
{b_{r+3}^2}
\right|
\le
\frac{2(b_{r+2}^2-b_{r+3}b_{r+1})^{3/2}}
{b_{r+3}^2}.
}
\]

The center is the derivative-determined centering prediction. The radius is
exactly the area reserve of the negative quadratic lobe:

\[
\frac{A_+-A_-}{2}=\frac{2D^{3/2}}{A^2}.
\]

This identifies the recurrent exponent `3/2` geometrically. As the quadratic
pair approaches collision, its horizontal scale is `sqrt(D)` and its depth
is `D`; their product is `D^(3/2)`. The cubic theorem asks the source's
centering error to vanish at least as rapidly as that collapsing lobe area.

Therefore the near-Gaussian difficulty is not merely that quadratic
coercivity becomes small. The admissible interval collapses cubically in the
root-separation scale. This is the local rigidity that killed generic
higher-order perturbations while allowing the quartic tangent direction.

## Source-derived target

The next theorem must transport a *pointed quadratic* `(Q_{r+2},b_r)`, not
merely the unordered roots. Equivalently it must explain why the
source-weighted area accumulated between the two critical points straddles
zero.

A faithful attack is:

1. express both endpoints `A_{r,-},A_{r,+}` through the positive two-copy
   companion measure;
2. pull those integrals through the positive two-copy companion measure;
3. seek one source-derived orientation pairing of the two lobes;
4. reject any pairing that chooses its base point after seeing the answer.

## Scope

The root coordinate and interlacing no-go are exact. This packet does not
prove critical-value orientation for the completed theta source and does not
prove RH.
