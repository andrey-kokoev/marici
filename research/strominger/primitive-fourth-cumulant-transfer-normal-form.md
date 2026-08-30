# Primitive fourth cumulant as an adjacent-bias transfer inequality

Status: exact normalization and proof target; the invariant-region theorem is
open.

## Moment potential

Fix the moving wall \(a\) and define

\[
Z(q)=\int_0^\infty R^qF(a+R)\,dR,
\qquad
\psi(q)=\log Z(q).
\]

Under the residual-power law \(Q_q\), the logarithmic residual
\(H=\log R\) has cumulants

\[
\mathbb E_qH=\psi'(q),\qquad
\operatorname{Var}_qH=\psi''(q),\qquad
\operatorname{cum}_{3,q}(H)=\psi'''(q).
\]

Inverse-residual bias is exactly the adjacent law \(Q_{q-1}\).  Put

\[
d=\psi'(q)-\psi'(q-1),
\]

\[
B=\psi''(q-1)-\psi''(q),
\]

and

\[
C=\psi'''(q)-\psi'''(q-1).
\]

The observed theta branch has \(d,B,C>0\).  Differentiation gives the exact
transfer relations

\[
d'=-B,\qquad B'=-C.
\]

Thus the fourth-cumulant obstruction is a curvature law for one adjacent-bias
step, not an independent four-moment coincidence.

## Dimensionless defect coordinates

Define

\[
A=1-qd,\qquad
b=\frac{B}{d^2},\qquad
c=\frac{C}{d^3}.
\]

The exponential residual law is the memoryless reference:

\[
A=0,\qquad b=1,\qquad c=2.
\]

Grothendieck's exact score elimination says that negativity of the mixed
fourth cumulant is equivalent to

\[
qC<3AB+d^2(2+A).
\]

Since \(qd=1-A\), this becomes the dimensionless transfer inequality

\[
(1-A)c<2+A+3Ab.
\]

The exponential law lies exactly on its boundary.  The theta theorem asks
whether the explicit superexponential carrier remains on the strict repair
side of this boundary for \(4\le q\le10\) and every admitted wall.

## Flow identities

The first two normalized coordinates obey

\[
A'
=d\bigl((1-A)b-1\bigr),
\]

and

\[
b'
=d(2b^2-c).
\]

Consequently the desired inequality can be rewritten as an upper barrier on
the normalized skew transport:

\[
c<
\frac{2+A+3Ab}{1-A},
\qquad 0\le A<1.
\]

This is the correct transfer-system target.  A proof may proceed by finding a
source-derived forward-invariant region in the \((A,b,c)\) state space.  It
must not assume the desired fourth cumulant sign when establishing that
region.

## Why this normalization matters

The three raw terms have different dimensions and nearly cancel near the
far-wall exponential regime.  Dividing by \(d^2\) separates:

- \(A\): failure of normalized memorylessness;
- \(b\): variance response relative to the squared adjacent mean gap;
- \(c\): skew response relative to the cubed adjacent mean gap.

The theorem is therefore a stability statement around the universal
memoryless fixed point.  The two repair channels are encoded by \(A\) and
\(b\); failure occurs when the normalized skew transport \(c\) crosses their
barrier.

## Proof routes

Three routes remain source-faithful:

1. derive a Stein-kernel bound for the explicit carrier that places
   \((A,b,c)\) inside an invariant cone;
2. use the closed-form carrier score to obtain a comparison principle for the
   adjacent laws \(Q_q,Q_{q-1}\);
3. prove the barrier only after the exact cubic B-spline averaging required
   by the flux, which is weaker than pointwise control.

Generic log-concavity is insufficient.  It supplies \(A\ge0\) but does not
control \(b\) or \(c\) sharply enough.

## Falsifiers

The pointwise transfer conjecture fails at the first \((a,q)\) for which

\[
(1-A)c\ge2+A+3Ab.
\]

Pointwise failure does not falsify the flux theorem.  The exact flux uses a
cubic B-spline average in \(q\), so the averaged transfer residual must be
tested separately.

The invariant-region strategy fails if a theta trajectory exits every
source-derived proposed cone while the averaged flux remains positive.  That
would prove that local state-space orientation is stronger than the actual
theorem and force a genuinely nonlocal-in-\(q\) proof.

## Floating-point reconnaissance

A composite-Simpson sweep over

\[
1.500001\le c_{\rm wall}\le200,
\qquad
4\le q\le10
\]

on a quarter-step \(q\)-grid finds \(d,B,C,A>0\) and a positive normalized
margin at every sampled point.  The minimum occurs at the far-wall boundary
\(q=4,c_{\rm wall}=200\), where the refined margin is approximately

\[
2.91435\times10^{-5}.
\]

The exact scaled-carrier expansion confirms cancellation through order
\(c_{\rm wall}^{-2}\).  For every integer \(4\le q\le10\), the first
nonzero term is

\[
\mathfrak m(q,c_{\rm wall})
=
\frac{4q^3}{c_{\rm wall}^3}
+O(c_{\rm wall}^{-4}).
\]

### Exact carrier and its characteristic wall

Writing \(t=c_{\rm wall}^{-1}\), the scaled carrier used by the formal
calculation resums exactly:

\[
W_t(x)=
\left(e^{xt}-\frac{3t}{2}\right)e^{5xt/4}
\exp\left(-\frac{e^{xt}-1-xt}{t}\right).
\]

This formula explains the lower wall \(c_{\rm wall}=3/2\).  The only
sign-bearing factor is \(e^{xt}-3t/2\).  It is strictly positive for every
\(x\ge0\) precisely when \(t<2/3\), or \(c_{\rm wall}>3/2\).  At equality it
first vanishes at \(x=0\).  For \(t>2/3\), the zero

\[
x_*=\frac{\log(3t/2)}{t}
\]

lies inside the integration domain.  Thus \(3/2\) is a characteristic wall
of the source carrier, not a fitted numerical cutoff.

The same identity supplies a uniform real-axis envelope.  Since
\(e^{xt}-1-xt\ge0\),

\[
0<W_t(x)\le e^{9xt/4}.
\]

On the proposed far-wall patch \(c_{\rm wall}\ge60\), one has \(t\le1/60\),
the first factor retains the margin \(1-3t/2\ge39/40\), and the gamma
integrand decays at least as \(e^{-77x/80}\).  Uniformly for
\(4\le q\le10\), the \(q\)-derivatives through order three are dominated by

\[
(x^4+x^{10})(1+|\log x|^3)e^{-77x/80}.
\]

This licenses differentiation under the integral and supplies the
dominated-convergence part of a Watson argument.  It does not yet control
the sixth-order remainder in \(t\); that is now the sole missing far-wall
estimate.

There is a more useful exact normalization.  Set

\[
y=\frac{e^{xt}-1}{t},
\qquad
x=h_t(y):=\frac{\log(1+ty)}{t}.
\]

The moving exponential and the Jacobian then cancel, giving

\[
Z_t(q)=
\int_0^\infty e^{-y}
\left(1+t\left(y-\frac32\right)\right)
(1+ty)^{1/4}h_t(y)^q\,dy.
\]

This is the decisive remainder coordinate.  The reference measure
\(e^{-y}dy\) no longer depends on \(t\); all deformation is carried by an
affine factor, a quarter-power, and the logarithmic coordinate \(h_t\).
Moreover \(0<h_t(y)\le y\) for \(t,y>0\).  The characteristic wall is now
visibly the loss of positivity of \(1+t(y-3/2)\) at \(y=0\), while the tail
remains controlled by the fixed exponential measure.  A proof of the
sixth-order remainder should therefore differentiate this transformed
integrand, not the original moving-exponential presentation.

The logarithmic coordinate already has the required alternating remainder
structure:

\[
\frac{h_t(y)}{y}
=
\int_0^1\frac{ds}{1+tys}.
\]

Consequently, for every \(n\ge0\),

\[
0\le
(-1)^n\partial_t^n\left(\frac{h_t(y)}{y}\right)
=
n!y^n\int_0^1\frac{s^n\,ds}{(1+tys)^{n+1}}
\le
\frac{n!}{n+1}y^n.
\]

Thus the coordinate deformation is completely monotone and its Taylor
remainder is bounded by the first omitted term.  For integer \(q\),
\((h_t(y)/y)^q\) is a product of \(q\) such resolvent averages, so it retains
complete monotonicity.  The unresolved orientation problem is now confined
to its product with the affine factor and \((1+ty)^{1/4}\), followed by the
logarithm and adjacent-grade differences defining the margin.

### Hostile remainder localization

High-precision quadrature in the fixed-measure coordinate tested

\[
q\in\{4,4.5,\ldots,10\},
\qquad
c_{\rm wall}\in\{60,75,100,150,200\}.
\]

Every sampled remainder after order five is negative, as predicted by the
order-six orientation, and every absolute remainder lies inside the proved
reserve.  The largest normalized consumption occurs at the near corner
\((q,c_{\rm wall})=(10,60)\):

\[
\frac{|\mathcal R_6|}{5q^3/(2c_{\rm wall}^3)}
=
0.394496196326513\ldots.
\]

Thus the sampled patch retains more than sixty percent of the available
reserve.  More importantly, the hostile maximum lies at the corner of the
parameter rectangle.  Every sampled step is strictly increasing in \(q\) and
in \(t=c_{\rm wall}^{-1}\); the smallest observed positive steps are
\(4.2165\times10^{-4}\) and \(1.3487\times10^{-3}\), respectively.  This
points to a smaller analytic target: prove those two monotonicities.  Such a
theorem would reduce the entire far-wall patch \(4\le q\le10\),
\(c_{\rm wall}\ge60\) to a single certified corner bound.  The quadrature is
not interval arithmetic, so neither monotonicity nor the corner bound is yet
a proof.

Over the rational function field in \(q\), the first coefficients factor as

\[
\mathfrak m(q,c_{\rm wall})
=
\frac{4q^3}{c_{\rm wall}^3}
-\frac{q^3(92q-53)}{4c_{\rm wall}^4}
+\frac{q^3(1520q^2-776q+297)}{16c_{\rm wall}^5}
+O(c_{\rm wall}^{-6}).
\]

Thus the value \(256\) is not isolated numerology.  It is the first member
of the exact cubic-grade law \(4q^3\).  Exact propagation over the rational
function field, followed by an independent polynomial-identity check, shows
that every coefficient from orders three through eight has a common \(q^3\)
factor.  This is evidence for a three-step transport multiplicity behind the
fourth-cumulant gate, rather than a coincidence confined to the leading
term.  A uniform remainder estimate is still required for the full far-wall
theorem.

The displayed three-term bracket is itself strictly positive for every
\(c_{\rm wall}>0\) and \(q\ge4\).  As a quadratic in
\(c_{\rm wall}^{-1}\), its discriminant has numerator

\[
-15856q^2+2664q-1943.
\]

This polynomial is negative at \(q=4\) and strictly decreasing thereafter,
while the quadratic leading coefficient

\[
1520q^2-776q+297
\]

is positive and increasing.  Thus the known \(c_{\rm wall}^{-3}\),
\(c_{\rm wall}^{-4}\), and \(c_{\rm wall}^{-5}\) terms cannot cancel to a
negative value anywhere in the admissible grade range.  All remaining
far-wall sign risk lies in the exact remainder.

The same quadratic calculation yields the uniform quantitative reserve

\[
\mathfrak m_{\le5}(q,c_{\rm wall})
\ge
\frac{5q^3}{2c_{\rm wall}^3},
\qquad q\ge4,\quad c_{\rm wall}>0.
\]

After minimizing in \(c_{\rm wall}^{-1}\), the difference from the
\(5/2\) bound has numerator

\[
656q^2+5096q-1027,
\]

which is positive and increasing from \(q=4\).  Therefore the far-wall proof
does not require a sharp asymptotic remainder.  It is enough to prove

\[
|\mathcal R_6(q,c_{\rm wall})|
<
\frac{5q^3}{2c_{\rm wall}^3}
\]

uniformly on the declared far-wall region.

Exact expansion through \(c_{\rm wall}^{-12}\) alternates in sign for every
real \(q\ge4\), not only at the tested integer grades.  After removing \(q^3\),
orienting by \((-1)^{n-3}\) at order \(n\), and writing the quotient in powers
of \(q-4\), every coefficient is strictly positive through order twelve.  The
raw quotient polynomials have mixed signs, so this shifted positive cone is
the relevant invariant.  The coefficient ratios increase with grade: the
initial ratio is about \(19.7\) at \(q=4\) and \(54.2\) at \(q=10\).  This
suggests a uniform far-wall threshold near \(c_{\rm wall}=60\), but it does
not establish convergence.  Because the series arises from a Laplace
endpoint expansion, the admissible proof target is an alternating
Watson-type remainder estimate after the scaled-carrier change of variables.

The later coefficients admit a sharper finite dominance theorem.  Let
\(B_n(q)=(-1)^{n-3}a_n(q)/q^3\).  Exact Bernstein conversion on
\(4\le q\le10\) proves

\[
0<B_{n+1}(q)<37B_n(q),
\qquad 6\le n\le11.
\]

Therefore, on \(t\le1/60\), the known tail terms from orders six through
twelve contract successively by less than \(37/60\).  This does not control
the infinite tail, but it replaces sampled ratio evidence by an exact
finite-interval polynomial certificate and identifies \(37/60\) as the
natural candidate contraction constant.

The sampled margin decreases monotonically as the wall moves outward, but it
is not monotone in \(q\).  Its minimizing grade changes with the wall:

- near \(c_{\rm wall}=1.5\), the sampled minimum lies at \(q=10\);
- near \(c_{\rm wall}=1.70\), it lies internally around \(q=8.6\);
- near \(c_{\rm wall}=1.75\), it lies internally around \(q=6.8\);
- from approximately \(c_{\rm wall}=1.8\) outward, it lies at \(q=4\).

This rules out a global reduction to the lowest grade.  It also reveals a
benign crossover: the near-wall and interior-grade margins are large, while
the only small reserve occurs in the already factorized far-wall
\(q=4\) corner.  A regional proof should therefore overlap a coarse
near-wall estimate, an intermediate compact certificate, and the far-wall
Watson bound.

## Relation to the incidence programme

This transfer law does not construct the global Tate seam maps or a
determinant--kernel bridge.  It attacks the strongest current source-specific
orientation theorem after the operator-incidence routes have been reduced to
scalar projection boundaries.  Success would explain the first cubic
coherence gate, not by itself prove RH.

## Bounded evidence

The deterministic checker
research/strominger/checkers/primitive_fourth_cumulant_transfer_checks.py
verifies:

- exact equivalence of the raw and normalized margins on rational fixtures;
- both normalized flow identities;
- the exponential boundary point for every integer \(4\le q\le10\);
- explicit open status of the theta invariant-region theorem.

Its result is
research/strominger/results/primitive_fourth_cumulant_transfer_checks.json.
The checker certifies the algebraic reduction only.

The separate reconnaissance checker
research/strominger/checkers/primitive_fourth_cumulant_transfer_recon.py
produces
research/strominger/results/primitive_fourth_cumulant_transfer_recon.json.
It is explicitly typed as floating-point falsification evidence, not an
interval certificate.

The exact formal-series checker
research/strominger/checkers/primitive_fourth_cumulant_far_wall_series.py
produces
research/strominger/results/primitive_fourth_cumulant_far_wall_series.json.
It verifies the order-three onset, the common \(q^3\) factor through order
twelve, continuous-\(q\) sign alternation on \(q\ge4\), and the exact
order-six-to-twelve ratio bound on \(4\le q\le10\), while declaring uniform
remainder control open.

The exact carrier-envelope checker
research/strominger/checkers/primitive_fourth_cumulant_carrier_envelope.py
produces
research/strominger/results/primitive_fourth_cumulant_carrier_envelope.json.
It verifies the characteristic wall, the positive-factor reserve, and the
uniform far-wall decay constants while keeping the Taylor-remainder gate
open.

The high-precision hostile remainder checker
research/strominger/checkers/primitive_fourth_cumulant_remainder_recon.py
produces
research/strominger/results/primitive_fourth_cumulant_remainder_recon.json.
It requires mpmath, evaluates the transformed fixed-measure integral at
60 decimal digits, and records the signed reserve consumption without
promoting the samples to an interval certificate.
