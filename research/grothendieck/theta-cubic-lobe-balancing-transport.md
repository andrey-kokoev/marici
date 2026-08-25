# Theta cubic lobe-balancing transport

Author: `marici.Grothendieck`

## Objective

Derive or sharply falsify a source-derived lobe-balancing explanation of the
unique exceptional cubic Jensen interface `t=3 -> 4` for the completed theta
source. This packet begins with the exact reduction of the two lobe areas to
the fixed positive bilinear companion.

## 1. Index audit

The Gaussian-normalized moments are

\[
b_t=\frac{Z_t}{\Gamma(t+1/2)}.
\]

For

\[
J_r^{(3)}(X)=b_r+3b_{r+1}X+3b_{r+2}X^2+b_{r+3}X^3,
\]

the two quadratic deficits are centered at `t=r+1` and `t=r+2`. Therefore
the exceptional interface `t=3 -> 4` is `r=2`:

\[
J_2^{(3)}(X)=b_2+3b_3X+3b_4X^2+b_5X^3.
\]

Its integration constant is `b_2`, while

\[
(J_2^{(3)})'(X)=3(b_3+2b_4X+b_5X^2)
\]

contains `b_3,b_4,b_5`. Any formulation calling `b_3` the integration
constant has an off-by-one error. The phrase "centering error of `b_3`" is
retained only if it means the first coefficient of the derivative quadratic,
not the scalar positioned inside the lobe interval.

## 2. Exact lobe interval

Put

\[
D_4=b_4^2-b_3b_5>0.
\]

The critical-area calculation gives the permitted interval

\[
\left|
b_2-\frac{b_4^3-3b_4D_4}{b_5^2}
\right|
\le\frac{2D_4^{3/2}}{b_5^2}.
\]

Equivalently, define the unnormalized centering error

\[
\boxed{
E_{34}:=b_2b_5^2-b_4^3+3b_4D_4.
}
\]

Then the exceptional cubic theorem is exactly

\[
\boxed{|E_{34}|\le2D_4^{3/2}.}
\]

The right side is not an estimated reserve. It is exactly half the area
between the two critical-lobe endpoint values after clearing `b_5^2`.

## 3. Bilinear companion substitution

The fixed positive companion satisfies

\[
C_t=\frac{K_t}{Z_t^2},
\qquad
D_t=b_t^2\frac{C_t}{2t+1}.
\]

Consequently

\[
\boxed{
D_t=\frac{K_t}{(2t+1)\Gamma(t+1/2)^2}.
}
\]

At `t=4`, writing `G=Gamma(9/2)`,

\[
b_2=\frac{35Z_2}{4G},
\qquad
b_4=\frac{Z_4}{G},
\qquad
b_5=\frac{2Z_5}{9G},
\qquad
D_4=\frac{K_4}{9G^2}.
\]

Substitution yields

\[
E_{34}=\frac1{G^3}
\left(
\frac{35}{81}Z_2Z_5^2-Z_4^3+\frac13Z_4K_4
\right),
\]

and

\[
2D_4^{3/2}=\frac{2K_4^{3/2}}{27G^3}.
\]

The common gamma carrier cancels. Hence the exceptional cubic gate is the
single exact companion inequality

\[
\boxed{
\left|
35Z_2Z_5^2-81Z_4^3+27Z_4K_4
\right|
\le6K_4^{3/2}.
}
\]

This completes the first two intended moves:

1. the two critical-lobe areas have been expressed through the positive
   bilinear companion;
2. the centering error has been isolated with the correct index and with no
   Gaussian normalization left.

## 4. Structural reading

Define

\[
\mathcal E_{34}=35Z_2Z_5^2-81Z_4^3+27Z_4K_4.
\]

The source has reduced to two fixed moment systems:

\[
Z_t=\int_0^\infty u^{2t}\Phi(u)\,du,
\qquad
K_t=\int_0^\infty p^{2t}k(p)\,dp,
\quad k(p)>0.
\]

The theorem is not positivity of `mathcal E_34`; either sign is allowed. It
is domination of a cubic centering error by the `3/2` power of one positive
two-copy moment. Therefore a termwise-positive label expansion is not the
right target. The faithful target is an oriented pairing whose total signed
mass lies inside the two-sided companion budget.

## 5. Next exact question

Expand `mathcal E_34` by completed theta labels before choosing signs. The
terms `Z_2 Z_5^2` and `Z_4^3` are three-copy packets; `Z_4K_4` is also
three-copy because `K_4` is bilinear. The next object is therefore a single
three-label kernel, not an unrelated mixture of one- and two-copy estimates.

The required comparison with `K_4^(3/2)` cannot be labelwise until the latter
is given a faithful three-copy realization. Any arbitrary independent-copy
square root would insert a measure not derived from the source. The next move
must either construct a canonical geometric-mean coupling from the companion
or prove that no such label-preserving coupling exists.

## 6. Symmetric three-label expansion of the centering error

Define the one-label moments and two-label companion moments

\[
z_t(n)=\int_0^\infty u^{2t}\phi_n(u)\,du,
\qquad
\kappa_t(m,n)=\int_0^\infty p^{2t}k_{m,n}(p)\,dp.
\]

Thus

\[
Z_t=\sum_nz_t(n),
\qquad
K_t=\sum_{m,n}\kappa_t(m,n).
\]

Although the completed `K_t` is positive, individual `kappa_t(m,n)` need
not be. The exact symmetric ordered three-label kernel is

\[
\begin{aligned}
e(i,j,k)={}&
\frac{35}{3}\sum_{\rm cyc}z_2(i)z_5(j)z_5(k)
-81z_4(i)z_4(j)z_4(k)\\
&+9\sum_{\rm cyc}z_4(i)\kappa_4(j,k).
\end{aligned}
\]

It satisfies

\[
\boxed{\mathcal E_{34}=\sum_{i,j,k\ge1}e(i,j,k).}
\]

This is the faithful label expansion of the signed centering error. Modular
partners must be regrouped before inspecting the sign of `e(i,j,k)` because
neither `phi_n` nor `kappa_4(m,n)` is separately a completed physical source.

## 7. The minimal faithful lift is six-copy

The term `K_4^(3/2)` is homogeneous of source degree three but is not a
polynomial label packet. Choosing labelwise square roots of the signed matrix
`kappa_4(m,n)` is neither canonical nor generally real. Therefore the
three-label comparison

\[
|\mathcal E_{34}|\le6K_4^{3/2}
\]

does not admit a faithful termwise expansion merely from bilinearity.

Because `K_4>0`, it is exactly equivalent to

\[
\boxed{
36K_4^3-\mathcal E_{34}^2\ge0.
}
\]

Both terms are now honest degree-six source packets. The right term is the
square of the symmetric three-label kernel; the left term is the product of
three completed bilinear companions. Thus six labels are the smallest
canonical algebraic lift supplied by the existing source operations.

This is not an unwanted growth of complexity. It is a typing theorem:

\[
\boxed{
\text{three-copy signed readout}
\quad\text{versus}\quad
\text{six-copy polynomial positivity certificate}.
}
\]

Any proposed three-label involution must provide additional source structure
equivalent to a canonical square root of the companion. Without it, the
six-copy lift is compulsory.

## 8. Prime-route quotient and seam audit

The prime-route score cocycle is

\[
J_a(u)=\frac{u+a}{u}.
\]

On the open chamber it is the coboundary `h(u+a)/h(u)` for `h(u)=u`; after
the gauge `uD_0=partial_u`, translation commutes with the score. Hence it has
no bulk curvature capable of orienting the lobe kernel.

The gauge fails only at `u=0`, producing the known rank-one seam covector in
each companion index. But completed modular evenness gives

\[
\sum_n\phi_n'(0)=\Phi'(0)=0,
\]

and contraction with the physical all-label vector annihilates that seam
covector. Consequently the completed physical scalar has

\[
\boxed{
\text{prime-route bulk class}=0,
\qquad
\text{physical seam residue}=0.
}
\]

This sharply falsifies a planned mechanism: no surviving modular-seam scalar
is available to repair `mathcal E_34`. Prime routes remain useful for faithful
coefficient reconstruction, but not for the missing physical orientation.
The lobe theorem, if true, must be a property of the regular completed bulk.

## 9. Revised transport target

The remaining alternatives are now narrow:

1. construct a canonical positive square-root feature of the completed
   companion, thereby earning a three-copy lobe involution; or
2. work directly with the six-copy polynomial
   `36 K_4^3-mathcal E_34^2` and seek a completed reflection pairing there.

The second route is source-complete with no extra choices. It is therefore
the default unless the first route is derived rather than postulated.

## 10. Canonical quadratic-lobe involution

Before lifting to six copies, there is one unavoidable involution on the
critical polynomial itself. For

\[
Q(X)=C+2BX+AX^2,
\]

reflection about its vertex is

\[
\boxed{R(X)=-\frac{2B}{A}-X.}
\]

It has

\[
R'(X)=-1,
\qquad
|R'(X)|=1,
\qquad
Q(R(X))=Q(X),
\qquad
R(x_-)=x_+.
\]

Thus its Jacobian magnitude and density ratio are both exactly one. It
reverses orientation and pairs the entire negative interval between the two
critical points without loss. No inequality is required for the lobe bulk.

However the cubic primitive is based at `X=0`, and

\[
\boxed{R(0)=-\frac{2B}{A}\ne0.}
\]

For the exceptional derivative quadratic this is

\[
R(0)=-\frac{2b_4}{b_5}.
\]

Therefore the unique canonical lobe involution does not preserve the
source-fixed base point. It proves equality of the reflected negative-lobe
bulk but leaves an endpoint interval between `0` and `-2B/A`. That endpoint
displacement is precisely where the centering prediction

\[
\frac{B^3-3BD}{A^2}
\]

enters. In other words,

\[
\boxed{
\text{lobe reflection closes the bulk automatically;}
\quad
\text{cubic hyperbolicity is the unpaired endpoint current.}
}
\]

This is a sharp analytic falsifier of the naive lobe-pairing proposal. No
involution determined solely by the quadratic can prove the theorem, because
such an involution cannot see the primitive constant `b_2`. A successful
source transport must supply an additional pointed endpoint law.

## 11. Modular reflection after moment reduction

The completed theta source is even under `u -> -u`. All moments entering
`Z_2,Z_4,Z_5` and `K_4` are even radial moments. Hence modular reflection has
already been contracted out in the scalar companion inequality: on these
variables it acts trivially, with unit Jacobian and unit density ratio.

It follows that modular reflection cannot repair the displaced polynomial
base point after the even-moment quotient. To use reflection nontrivially one
would have to retain the two prequotient half-charts and their endpoint
incidence. But the seam audit above shows that their physical boundary
residues cancel. Therefore any remaining orientation must descend from a
regular bulk identity, not from a hidden seam correction.

The surviving hard object is now the pointed endpoint current, equivalently
the six-copy scalar

\[
36K_4^3-\mathcal E_{34}^2.
\]

## 12. Diagonal theta labels are not coherently oriented

On the positive chart an individual theta label has the form

\[
\phi_n(u)=e^{u/2}(4x_n^2-6x_n)e^{-x_n},
\qquad
x_n=\pi n^2e^{2u}.
\]

Let `s_n=partial_u log(phi_n)`. At the modular seam,

\[
s_n(0)
=\frac92+\frac{6}{2\pi n^2-3}-2\pi n^2.
\]

Since `2x-3>0` for `x=pi n^2`, its sign is the sign of

\[
\boxed{-8x^2+30x-15.}
\]

The larger root is

\[
x_*=\frac{15+\sqrt{105}}8.
\]

One has `pi<x_*<4pi`. Therefore

\[
\boxed{s_1(0)>0,\qquad s_n(0)<0\quad(n\ge2).}
\]

For the diagonal polarized companion,

\[
\mathscr B_{n,n}(u,v)
=\frac{\phi_n(u)\phi_n'(v)}v
-\frac{\phi_n'(u)\phi_n(v)}u,
\]

the leading residue as `v -> 0+` has the sign of `s_n(0)`. Hence the
primitive diagonal label has the opposite seam orientation from every
higher diagonal label.

This provides the requested diagonal classification at the strongest local
level:

\[
\boxed{
\text{diagonal label pairs are not individually or uniformly oriented.}
}
\]

Cross-label completion is not a small correction; it is forced already by
the first boundary germ. Since the completed physical seam residue is zero,
these opposite diagonal residues must be cancelled by cross-label packets
before any bulk sign can be inspected.

More generally, for an ordered cross-label pair `(m,n)`,

\[
\mathscr B_{m,n}(u,v)
=\frac{\phi_m(u)\phi_n'(0)}v+O(1)
\qquad(v\downarrow0).
\]

Because `phi_m(u)>0` on the positive chart, the boundary classification is
complete:

\[
\begin{array}{c|c}
\text{second label}&\text{residue orientation}\\
\hline
n=1&\text{positive}\\
n\ge2&\text{negative}.
\end{array}
\]

As a coefficient matrix the residue factors as the outer product

\[
a_m(u)b_n,
\qquad
a_m(u)=\phi_m(u),
\qquad
b_n=\phi_n'(0).
\]

It therefore has rank one. Restricting the second coefficient channel to
the canonical seam hyperplane `ker(b^*)` removes every diagonal and
cross-label residue simultaneously. This is the exact cross-label boundary
classification: one positive column, infinitely many negative columns, and
one rank-one completed defect—not independently positive blocks.

It follows that a proof based on positivity of each `(n,n)` block is
impossible. The smallest admissible sign unit is a seam-closed modular label
packet, and its regular bulk contribution must then be tested in the
six-copy polynomial lift.

## 13. Unpointed lobe-transport no-go theorem

Fix any quadratic `Q` with two distinct real roots and let `P_0` be one cubic
primitive satisfying `P_0'=3Q`. Every other cubic primitive is

\[
P_c=P_0+c.
\]

All members of this family have exactly the same:

- critical points and quadratic lobes;
- vertex reflection and its Jacobian;
- bulk density ratio;
- quadratic discriminant and companion reserve.

But their critical values are translated by `c`. If the two critical values
of `P_0` are `h_->h_+`, then `P_c` is hyperbolic precisely for

\[
-h_-\le c\le-h_+.
\]

Choosing `c` inside and outside this nonempty bounded interval produces two
cubics with identical unpointed lobe data and opposite hyperbolicity status.
Therefore:

\[
\boxed{
\textbf{No-go theorem.}\quad
\text{No transport functor of the derivative quadratic alone can imply
cubic hyperbolicity.}
}
\]

The theorem covers transports built from root locations, lobe areas,
ordinary or signed interlacing, the vertex involution, its Jacobian, or any
other invariant unchanged by adding a constant to the primitive.

For theta, the missing point is exactly the source-selected value `b_2`.
Thus the proposed lobe-balancing route has been sharply falsified in its
unpointed form. Its only viable refinement is a pointed endpoint-current
theorem proving

\[
|\mathcal E_{34}|\le6K_4^{3/2},
\]

or equivalently the six-copy positivity

\[
36K_4^3-\mathcal E_{34}^2\ge0.
\]

This residual inequality is the smallest scalar obstruction left by the
audit. It is not supplied by lobe geometry, prime-route shear, modular seam
residue, diagonal-label positivity, or ordinary interlacing.

## 14. Disposition

The intended lobe-transport mechanism is finitely and analytically
falsified, rather than repaired after failure:

1. its canonical involution pairs the bulk but moves the base point;
2. the moved endpoint is precisely the datum deciding hyperbolicity;
3. prime-route bulk shear is a coboundary;
4. completed modular sewing annihilates the physical seam residue;
5. individual diagonal label packets have incompatible seam orientations;
6. all cross-label boundary defects form one rank-one seam packet;
7. the faithful remaining certificate is the regular six-copy endpoint
   current above.

This does not disprove the exceptional theta inequality. It proves that the
proposed lobe-balancing explanation cannot establish it unless enlarged by
the pointed source endpoint, in which case the work is exactly the residual
six-copy inequality rather than a lobe-only transport theorem.

## Scope

All identities above are exact. No numerical positivity or zero data enter.
The companion inequality has not yet been proved for theta, and RH is not
proved.
