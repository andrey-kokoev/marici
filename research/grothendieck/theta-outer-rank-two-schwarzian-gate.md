# Outer rank-two Loewner positivity is a Schwarzian curvature theorem

## Rank-two determinant

Let \(H\in C^3(J)\) be real with \(H'>0\) on an interval \(J\). Its
two-point Loewner matrix is

\[
\begin{pmatrix}
H'(x)&\dfrac{H(y)-H(x)}{y-x}\\[6pt]
\dfrac{H(y)-H(x)}{y-x}&H'(y)
\end{pmatrix}.
\]

Rank-two positivity is exactly

\[
\boxed{
\left(\frac{H(y)-H(x)}{y-x}\right)^2
\le H'(x)H'(y).
}
\]

For the theta current, the full-source theorem already proves
\(H'(x)>0\) on \(J=(1/4,\infty)\). Thus only this coupled determinant remains.

## Concave length-density theorem

Define

\[
p(x)=\frac1{\sqrt{H'(x)}}.
\]

If \(p\) is concave and positive, then for \(x<y\) and
\(t\in[x,y]\),

\[
p(t)\ge
\frac{y-t}{y-x}p(x)+\frac{t-x}{y-x}p(y).
\]

Therefore

\[
\begin{aligned}
H(y)-H(x)
&=\int_x^y\frac{dt}{p(t)^2}\\
&\le
\int_x^y
\frac{dt}{
\left(
\frac{y-t}{y-x}p(x)+\frac{t-x}{y-x}p(y)
\right)^2}\\
&=\frac{y-x}{p(x)p(y)}\\
&=(y-x)\sqrt{H'(x)H'(y)}.
\end{aligned}
\]

Hence

\[
\boxed{
p''\le0
\quad\Longrightarrow\quad
\text{every rank-two Loewner matrix is positive semidefinite}.
}
\]

Conversely, taking the confluent limit of the two-point determinant gives the
same differential condition. Thus, under the stated smoothness and strict
monotonicity, rank-two Loewner positivity on an interval is equivalent to
concavity of \(p\).

## Schwarzian form

Direct differentiation gives

\[
p''=
\frac{3H''^2-2H'H'''}{4H'^{5/2}}.
\]

Therefore the curvature condition is

\[
\boxed{
2H'H'''-3H''^2\ge0.
}
\]

Equivalently, the Schwarzian derivative satisfies

\[
\boxed{
\mathcal S(H)
=\frac{H'''}{H'}
-\frac32\left(\frac{H''}{H'}\right)^2
\ge0.
}
\]

The first coupled Loewner theorem is therefore exactly a nonnegative
Schwarzian theorem for the source-derived angular-current function.

## Why this is useful

The matrix problem has become a local scalar differential inequality. Unlike
pointwise positivity of \(H'\), it controls how rapidly the Loewner metric
\(H'(x)dx^2\) may change. The quantity \(p=H'^{-1/2}\) is its reciprocal
length density; concavity prevents a secant from outrunning the geometric mean
of its endpoint slopes.

For the completed theta source, derivatives of \(H\) can be written using the
tilted moments of

\[
q_x(u)=\partial_x\log\cosh(\sqrt x\,u).
\]

Thus the next analytic target is no longer an arbitrary two-point inequality:
derive \(\mathcal S(H)\ge0\) from moment/cumulant inequalities of the complete
positive source law \(\nu_x\) for every \(x>1/4\).

## Exact cumulant closure

Let

\[
\ell(x)=\log C(x),
\qquad
q^{[j]}_x(u)=\partial_x^j q_x(u),
\]

and write \(\kappa_x(\cdots)\) for joint cumulants under \(\nu_x\). Standard
exponential-family differentiation gives

\[
\ell' =\mathbb E q,
\]

\[
\ell''=\mathbb E q^{[1]}+\kappa(q,q),
\]

\[
\ell'''=
\mathbb E q^{[2]}
+3\kappa(q,q^{[1]})
+\kappa(q,q,q),
\]

and

\[
\begin{aligned}
\ell''''={}&
\mathbb E q^{[3]}
+4\kappa(q,q^{[2]})
+3\kappa(q^{[1]},q^{[1]})\\
&+6\kappa(q,q,q^{[1]})
+\kappa(q,q,q,q).
\end{aligned}
\]

Since \(H=(x-c)\ell'\),

\[
H'=\ell'+(x-c)\ell'',
\]

\[
H''=2\ell''+(x-c)\ell''',
\]

and

\[
H'''=3\ell'''+(x-c)\ell''''.
\]

Therefore the complete rank-two outer theorem is the single finite source
inequality

\[
\boxed{
2\bigl(\ell'+(x-c)\ell''\bigr)
\bigl(3\ell'''+(x-c)\ell''''\bigr)
-3\bigl(2\ell''+(x-c)\ell'''\bigr)^2
\ge0,
}
\]

with the four derivatives expanded by the displayed theta cumulants. No
derivative beyond the fourth log-cumulant occurs.

## Boundaries

- This is a rank-two theorem only. Higher Loewner ranks impose higher
  differential and separated-point conditions.
- Generic positive even source measures can violate the Schwarzian sign; the
  special theta structure is still essential.
- A numerical positive Schwarzian scan is reconnaissance, not proof.

The sharp falsifier is one \(x>1/4\) with

\[
2H'(x)H'''(x)-3H''(x)^2<0.
\]

## First outer reconnaissance

Direct completed-theta quadrature, differentiating the transform kernel
analytically through fourth order, finds positive Schwarzian numerator at

\[
x=0.251,0.26,0.3,0.5,1,2,5,10,30,100,300.
\]

The numerator decreases from approximately \(2.33\times10^{-8}\) near the
threshold to \(7.44\times10^{-10}\) at \(x=300\), but remains positive.
Independent 4,000- and 8,000-step Simpson evaluations agree far below every
displayed margin. The weakest sampled regime is the large positive ray, not
the source threshold.

This is non-certified reconnaissance and proves no interval.

Artifacts:

- checkers/theta_outer_schwarzian_scan.py
- results/theta-outer-schwarzian-scan.json

## Compact bridge via numerator monotonicity

The far-ray theorem now proves \(\mathcal N(H)>0\) for \(x\ge400\).  A fifth
source jet reveals a sharper candidate for the remaining compact interval.
Since

\[
\mathcal N(H)=2H'H'''-3(H'')^2,
\]

its derivative has the cancellation

\[
\boxed{
\mathcal N'(H)=2H'H''''-4H''H'''.
}
\]

Direct fixed-contour theta quadrature finds this quantity strictly negative
at every tested point from \(x=0.251\) through \(x=400\).  Representative
values are approximately

\[
\mathcal N'(0.251)=-4.76\times10^{-10},\qquad
\mathcal N'(100)=-5.98\times10^{-11},\qquad
\mathcal N'(400)=-2.21\times10^{-12}.
\]

Thus the preferred compact theorem is

\[
\boxed{
2H'(x)H''''(x)-4H''(x)H'''(x)<0
\qquad(1/4<x\le400).
}
\]

If proved, \(\mathcal N(H)\) is decreasing on the entire compact bridge, so

\[
\mathcal N(H)(x)\ge\mathcal N(H)(400)>0.
\]

This would join directly to the analytic far-ray theorem and establish the
global rank-two Schwarzian inequality without separately certifying the sign
of \(\mathcal N\) on a mesh.

The statement remains source-derived and finite: writing
\(\ell=\log C\),

\[
H''''=4\ell''''+(x-1/4)\ell''''',

so only the first five log-cumulants of the fixed theta source occur.  The
sharp falsifier is one point in \((1/4,400]\) where

\[
H'H''''-2H''H'''\ge0.
\]

The extended checker evaluates the fifth transform jet analytically and
records both \(\mathcal N\) and \(\mathcal N'\).  Its scan is reconnaissance,
not an interval proof.

### Generic-source falsifier

The monotonic bridge is not a consequence of positivity or evenness alone.
For the smallest hostile family

\[
\mu=\delta_0+\frac w2(\delta_a+\delta_{-a}),
\qquad
C_\mu(x)=1+w\cosh(a\sqrt x),
\]

a scan of 432 parameter triples finds 19 violations of
\(\mathcal N'(H)<0\).  More sharply, monotonicity can fail while the rank-two
numerator itself remains positive.  At

\[
(x,a,w)=(2,4,0.1)
\]

one obtains approximately

\[
\mathcal N(H)=0.16028>0,
\qquad
\mathcal N'(H)=0.13110>0.
\]

Therefore the proposed bridge is a sufficient theta-specific mechanism, not
a reformulation of rank-two positivity and not a generic positive-transform
theorem.  Any proof must spend genuine source information: modular sewing,
the consecutive labelled theta mixture, or a variation-diminishing property
stronger than measure positivity.  Failure of the monotonic bridge would not
by itself falsify global rank-two positivity.

Artifacts:

- checkers/theta_compact_monotonicity_two_atom_falsifier.py
- results/theta-compact-monotonicity-two-atom-falsifier.json

### First theta-specific separator: strong source log-concavity

The completed folded theta density itself, not merely the precursor, has the
form

\[
\Phi(u)=\sum_{n\ge1}T_n(u),
\quad
T_n(u)=2a_n e^{5u/2}(2a_ne^{2u}-3)e^{-a_ne^{2u}},
\quad a_n=\pi n^2,
\]

for \(u\ge0\).  Every summand is positive.  For the dominant first label,
put \(y=2\pi e^{2u}\).  Direct differentiation gives the exact identity

\[
\boxed{
(\log T_1)''(u)
=-2y-\frac{12y}{(y-3)^2}<0.
}
\]

Thus the one-label source is strongly log-concave, with its weakest curvature
at the seam.  The remaining theta labels are already tiny there:

\[
\frac{\sum_{n\ge2}T_n(0)}{T_1(0)}approx2.1761\times10^{-3},
\]

and the ratio decays superexponentially, reaching approximately
\(2.37\times10^{-4}\) at \(u=0.1\) and
\(3.73\times10^{-6}\) at \(u=0.25\).  Direct log-sum evaluation finds

\[
(\log\Phi)''(u)<0\qquad(0\le u\le4),
\]

with the least-negative sampled value, about \(-18.73\), at \(u=0\).
This makes a tail-domination proof of strict log-concavity plausible: the
first-label curvature has order-one slack precisely where the relative tail
is largest, and the slack grows where the tail disappears.

This property cleanly excludes the atomic hostile examples, but it has not
yet been shown to imply \(\mathcal N'(H)<0\).  The next hostile question is
therefore exact: does strong even log-concavity suffice for the five-cumulant
inequality, or is a still more theta-specific labelled order required?

That hostile question has a negative answer.  Consider the smooth even
densities

\[
e^{-V(u)},
\qquad
V(u)=\frac{u^2}{2}+\varepsilon(1-\cos bu),
\qquad \varepsilon b^2<1.
\]

They are rigorously strongly log-concave because
\(V''(u)\ge1-\varepsilon b^2>0\).  Nevertheless a 112-case scan finds 57
violations of \(\mathcal N'(H)\le0\).  For example, at

\[
x=0.251,\quad b=1,\quad \varepsilon b^2=0.9,
\]

the source remains strongly log-concave while

\[
\mathcal N(H)\approx1.7903\times10^{-3}>0,
\qquad
\mathcal N'(H)\approx2.8314\times10^{-4}>0.
\]

Hence even strong log-concavity is not the missing theorem.  The falsifier
localizes the absent information: its convex potential has oscillating
curvature, while the theta source is sewn at \(u=0\) and its sampled potential
curvature \(- (\log\Phi)''\) increases away from that seam.  The next viable
property is therefore a coupled one:

\[
\boxed{
\text{modular seam compatibility plus outward-increasing source curvature.}
}
\]

Neither clause should be silently discarded: generic strong convexity has
just failed, while seam identities alone do not control the fifth tilted
cumulant.

The conjunction is nevertheless still insufficient in that generic form.
The smooth even polynomial potentials

\[
V(u)=\frac{u^2}{2}+\lambda u^4+\mu u^6,
\qquad \lambda,\mu\ge0,
\]

are sewn evenly at the origin, strongly convex, and have

\[
V'''(u)=24\lambda u+120\mu u^3\ge0
\qquad(u\ge0).
\]

Among 98 hostile cases, 12 violate \(\mathcal N'(H)\le0\).  The logical
separation persists even where rank-two positivity itself holds: for

\[
x=10,qquad \lambda=10^{-3},qquad \mu=10^{-4},
\]

the scan gives

\[
\mathcal N(H)\approx6.3716\times10^{-5}>0,
\qquad
\mathcal N'(H)\approx1.0666\times10^{-5}>0.
\]

Therefore “seam plus increasing curvature” is falsified as a universal
explanation.  Its survival for \(\Phi\) remains useful phenomenology, but the
proof must now spend the discrete modular theta-label relation itself, or
abandon monotonicity and certify \(\mathcal N>0\) directly.

### Hidden alternating hierarchy

Direct compact-source reconnaissance reveals more structure than the single
monotonicity sign.  Across 65 logarithmically spaced points on
\(0.251\le x\le400\), it finds

\[
\mathcal N>0,
\qquad \mathcal N'<0,
\qquad \mathcal N''>0,
\qquad \mathcal N'''<0.
\]

The local sign length \(\mathcal N/|\mathcal N'|\) stays between approximately
\(48.99\) and \(183.68\), so compact positivity is not numerically grazing
zero.  Differentiation also produces unexpected cancellations:

\[
\mathcal N''
=2H'H^{(5)}-2H''H^{(4)}-4(H''')^2,
\]

\[
\boxed{
\mathcal N'''
=2H'H^{(6)}-10H'''H^{(4)}.
}
\]

This suggests the stronger theta-specific conjecture

\[
\boxed{
(-1)^k\mathcal N^{(k)}(x)\ge0
\qquad(k\ge0,\ x>1/4),
}
\]

so that the Schwarzian numerator itself would be completely monotone.  By
Bernstein's theorem it would then be a Laplace transform of a positive
measure, making rank-two positivity immediate.  This is reconnaissance, not
a theorem, and the hostile examples above show that it cannot follow from
generic log-concavity or increasing curvature.

The full hierarchy is unnecessary for the immediate compact result.  It is
enough to certify

\[
\mathcal N''>0\quad(1/4<x\le400),
\qquad
\mathcal N'(400)<0,
\qquad
\mathcal N(400)>0.
\]

Then \(\mathcal N'\) increases but remains negative, while \(\mathcal N\)
decreases to its positive endpoint value.  This is now the preferred finite
fallback alongside the more explanatory complete-monotonicity conjecture.

The conjecture survives its first moment-theoretic falsifier.  Exact kernel
jets through order ten were used to compute

\[
m_k(x)=(-1)^k\mathcal N^{(k)}(x),\qquad 0\le k\le6,
\]

at \(x=0.251,1,10,100,400\).  All \(m_k\) are positive.  Moreover the first
Stieltjes conditions

\[
\det(m_{i+j})_{0\le i,j\le1}>0,
\qquad
\det(m_{i+j+1})_{0\le i,j\le1}>0,
\qquad
\det(m_{i+j})_{0\le i,j\le2}>0
\]

hold at every tested scale.  The normalized two-by-two determinant margins
are not small: the unshifted ratios lie between approximately \(0.216\) and
\(0.270\), and the shifted ratios between \(0.168\) and \(0.209\).  Doubling
the source-quadrature resolution changes the signed derivative candidates by
at most about \(5.1\times10^{-10}\) relatively at the most difficult sampled
point.

This does not prove a Stieltjes moment sequence or complete monotonicity.  It
does change the preferred explanatory attack: seek an explicit positive
measure \(\sigma\), derived from the labelled theta source, for which

\[
\boxed{
\mathcal N(x)=\int_0^\infty e^{-(x-1/4)t}\,d\sigma(t).
}
\]

Any proposed representation must reproduce the displayed Hankel moments and
the exact two-copy Schwarzian numerator; fitting a positive exponential sum
to sampled values is not evidence of source derivation.

### Conditional-spread reduction of the Bernstein measure

There is an exact route to such a representation.  Suppose first that
\(f=H'\) is completely monotone and let its Bernstein measure be \(\mu\):

\[
f(x)=\int_0^\infty e^{-(x-1/4)t}\,d\mu(t).
\]

Then

\[
\begin{aligned}
\mathcal N(x)
&=2f(x)f''(x)-3f'(x)^2\\
&=\iint e^{-(x-1/4)(t+u)}
\bigl(t^2+u^2-3tu\bigr)\,d\mu(t)d\mu(u).
\end{aligned}
\]

Push this signed two-copy measure forward by the faithful sum coordinate
\(v=t+u\).  On each fiber, exchange symmetry gives
\(\mathbb E[t\mid v]=v/2\), while

\[
\boxed{
t^2+u^2-3tu
=5\left(t-\frac v2\right)^2-\frac{v^2}{4}.
}
\]

Consequently the pushed measure is positive precisely when the conditional
spread satisfies

\[
\boxed{
\operatorname{Var}(t\mid t+u=v)
\ge\frac{v^2}{20}
}

for the relevant convolution fibers, interpreted measure-theoretically when
\(\mu\) is not absolutely continuous.  This is the source-normalized
imbalance theorem hidden inside the Schwarzian numerator: balanced pairs
carry negative weight, and sufficiently off-diagonal pairs dominate them.

The reduction preserves the earlier durable rule.  Positivity is asserted
after pushforward to the faithful sum coordinate \(v\), not inferred from a
coarser scalar sample.  A sharp falsifier is one fiber whose conditional
variance is below \(v^2/20\).

The prerequisite is itself supported by hostile reconnaissance.  At
\(x=0.251,1,10,100,400\), the available derivatives of \(H'\) alternate in
sign and its ordinary and shifted Stieltjes Hankel determinants through order
three are positive.  This is not yet a proof that \(H'\) is completely
monotone.  The next two exact tasks are therefore:

1. derive the Bernstein measure \(\mu\) of \(H'\) from the fixed labelled
   theta/arithmetic source; and
2. prove or finitely falsify the conditional-spread bound on its convolution
   fibers.

Artifacts:

- checkers/theta_completed_source_log_concavity.py
- results/theta-completed-source-log-concavity.json
- checkers/theta_compact_monotonicity_strong_log_concavity_falsifier.py
- results/theta-compact-monotonicity-strong-log-concavity-falsifier.json

## Arithmetic meaning of the same threshold

With

\[
x=(s-1/2)^2,
\]

the source center satisfies

\[
x=1/4\quad\Longleftrightarrow\quad s=1
\]

on the positive branch. Moreover

\[
H(x)=\frac{s(s-1)}{2s-1}\frac{\xi'(s)}{\xi(s)}.
\]

Thus the same boundary marks:

1. the null-mode exponent of \(1/4-\partial_u^2\);
2. the convergence wall of the precursor probability law;
3. cancellation of the completed-zeta pole; and
4. entry into the absolutely convergent Euler-product region \(s>1\).

This supplies a new proof strategy for the outer Schwarzian theorem. Split
the exact logarithmic derivative for \(s>1\) into endpoint, gamma, and
absolutely convergent prime-power terms, differentiate with respect to
\(x=(s-1/2)^2\), and prove the nonlinear Schwarzian combination directly.
Because the Schwarzian is nonlinear, the three sectors cannot be declared
positive separately; their coupled bounds must retain the completion terms.

The leading completed-gamma term has now been differentiated exactly. Its
Schwarzian numerator is
\((3L^2+4L-2)/(256x^3)\), positive beyond approximately \(x=85.7\).
This supplies the far-ray mechanism and leaves explicit derivative remainder
bounds plus a compact interval. See
`theta-outer-schwarzian-asymptotic-mechanism.md`.
