# Theta cubic modular seam rank one

Status: live bounded-transition successor.

## 1. Canonical chamber split

Fix the source-defined boundary

\[
 a=\frac12,
\qquad
 B=(0,a],\qquad F=(a,\infty).
\]

For the tilted law \(Q_t\), write

\[
 p_t=Q_t(B),\qquad q_t=Q_t(F)=1-p_t.
\]

Let

\[
 A_{X,t}=\mathbb E(R\mid X),\qquad
 M_{X,t}=\mathbb E(W\mid X),\qquad
 C_{X,t}=\operatorname{Cov}(R,W\mid X),
\]

for \(X=B,F\).  The global quadratic reserve is

\[
 C_t=\operatorname{Cov}_{Q_t}(R,W).
\]

## 2. Exact rank-one seam decomposition

The law of total covariance gives

\[
\boxed{
 C_t
 =p_tC_{B,t}+q_tC_{F,t}
 +p_tq_t
  (A_{F,t}-A_{B,t})
  (M_{F,t}-M_{B,t}).
}                                                       \tag{1}
\]

Since \(R=u^2\) and \(W\) are strictly increasing,

\[
 A_{F,t}>A_{B,t},\qquad M_{F,t}>M_{B,t}.
\]

Therefore the seam term

\[
\boxed{
 \mathcal R_t
 :=p_tq_t\Delta A_t\Delta M_t>0
}                                                       \tag{2}
\]

is a canonical positive completion channel.  Whether it repairs the cubic
readout must still be determined from its adjacent action.

It has rank one: it is the product of the jumps of the two sufficient
statistics across the binary chamber label.  No coefficient is fitted, and
the boundary is the same \(u=1/2\) at which the proved primitive/far
curvature arguments exchange authority.

## 3. Two-copy meaning

The same term is exactly the bounded--far block of the Andréief separation
energy.  If \(U_B\) and \(U_F\) are independent conditional source points,

\[
\begin{aligned}
 &p_tq_t\,
 \mathbb E[
 (R_F-R_B)(W_F-W_B)]\\
 &\qquad=
 p_tq_t\Delta A_t\Delta M_t
 +p_tq_t
 \bigl[
 \operatorname{Cov}_F(R,W)
 +\operatorname{Cov}_B(R,W)
 \bigr].
\end{aligned}                                           \tag{3}
\]

After the within-chamber contributions are assigned according to the law of
total covariance, the genuinely new cross information is precisely
\(\mathcal R_t\).

Thus the chamber cut does not create an uncontrolled continuum of mixed
defects.  It creates one binary between-class mode.

## 4. Exact adjacent evolution

Passing from \(Q_t\) to \(Q_{t+1}\) is \(R\)-size bias.  Hence

\[
 p_{t+1}=\frac{p_tA_{B,t}}{A_t},
\qquad
 q_{t+1}=\frac{q_tA_{F,t}}{A_t},
\qquad
 A_t=p_tA_{B,t}+q_tA_{F,t}.                            \tag{4}
\]

Within each chamber,

\[
 \mathbb E_{t+1}(G\mid X)
 =
 \frac{\mathbb E_t(RG\mid X)}{A_{X,t}}.                \tag{5}
\]

Therefore

\[
\boxed{
 \mathcal R_{t+1}
 =
 \frac{p_tq_tA_{B,t}A_{F,t}}{A_t^2}
 \Delta A_{t+1}\Delta M_{t+1}.
}                                                       \tag{6}
\]

Every factor is a one-chamber moment or a barycentre jump.  Equation (6) is
the exact size-bias transport law for the modular repair channel.

## 5. Correct proof architecture

The failed Prekopa route showed that the bounded--bounded product kernel
expands in the wrong logarithmic orientation at the seam.  Equation (1)
identifies the only source-fixed term capable of repairing that defect:

\[
\boxed{
\text{bounded internal reserve}
+
\text{far internal reserve}
+
\text{one positive modular seam mode}.
}                                                       \tag{7}
\]

The bounded cubic theorem should now be attacked as a rank-one secular
problem:

1. determine the cubic deficit produced by
   \(p_tC_{B,t}+q_tC_{F,t}\) alone;
2. prove that this internal part has at most one bad adjacent mode;
3. compute the exact contribution of \(\mathcal R_t\) and
   \(\mathcal R_{t+1}\) to the inverse lengths;
4. verify one scalar repair inequality, uniformly over the bounded tilt
   interval.

This is structurally parallel to the prime-two level-44 theorem.  The
analogy is earned: in both cases a canonical decomposition leaves one
unstable channel and one source-derived rank-one completion.

## 6. Sharp falsifier

The rank-one explanation fails if either:

\[
\text{the internal chamber system has two independent bad modes},
\]

or

\[
\text{its single defect exceeds the exact seam contribution } \mathcal R_t.
\]

No post-hoc movement of \(a=1/2\) is allowed.  The next calculation is to
write the adjacent inverse-length difference using (1) and (6), and isolate
the resulting scalar secular remainder.

## 7. Exact scalar secular remainder

Put

\[
 I_t=p_tC_{B,t}+q_tC_{F,t},
\qquad
 C_t=I_t+\mathcal R_t,
\qquad b=2t+1.
\]

The cubic gate is exactly

\[
 \left|
 \sqrt{\frac{b+2}{I_{t+1}+\mathcal R_{t+1}}}
 -
 \sqrt{\frac b{I_t+\mathcal R_t}}
 \right|\le1.                                          \tag{8}
\]

Multiplying by the positive product of the two reserves gives the scalar
secular condition

\[
\boxed{
 \Sigma_t:=
 C_tC_{t+1}
 -
 \left(
 \sqrt{(b+2)C_t}
 -
 \sqrt{bC_{t+1}}
 \right)^2
 \ge0.
}                                                       \tag{9}
\]

Substitution of \(C=I+\mathcal R\) makes (9) the exact one-channel test.
There is no matrix determinant left.

Positivity of \(\mathcal R_t\) alone does not determine the sign of its
effect.  If

\[
 d(X,Y)=\sqrt{\frac{b+2}{Y}}-\sqrt{\frac bX},
\]

then

\[
 \partial_Xd=\frac{\sqrt b}{2X^{3/2}}>0,
\qquad
 \partial_Yd=-\frac{\sqrt{b+2}}{2Y^{3/2}}<0.            \tag{10}
\]

Thus the two adjacent seam additions act in opposite directions on the
signed inverse-length displacement.  The channel earns the name “repair”
only if their source-fixed ratio moves \(d\) toward zero.

The exact orientation criterion along the seam ray

\[
 (X(s),Y(s))
 =(I_t+s\mathcal R_t,\,
   I_{t+1}+s\mathcal R_{t+1})
\]

is

\[
\boxed{
 d\,\frac{d d}{ds}\le0,
}                                                       \tag{11}
\]

where

\[
 \frac{dd}{ds}
 =
 \frac{\sqrt b\,\mathcal R_t}{2X^{3/2}}
 -
 \frac{\sqrt{b+2}\,\mathcal R_{t+1}}{2Y^{3/2}}.         \tag{12}
\]

Equations (11)--(12) are the proposed monotone rank-one mechanism and its
sharp local falsifier.  Failure of monotonicity would not by itself falsify
the endpoint gate (9); it would falsify only the claim that the seam repairs
the defect continuously as it is switched on.

When \(d>0\), contraction requires

\[
 \boxed{
 \frac{\mathcal R_{t+1}}{\mathcal R_t}
 \ge
 \sqrt{\frac b{b+2}}
 \left(\frac YX\right)^{3/2}.
 }                                                       \tag{13}
\]

When \(d<0\), the inequality reverses.  From (2) and (6), the left side is
the exact source ratio

\[
\boxed{
 \frac{\mathcal R_{t+1}}{\mathcal R_t}
 =
 \frac{A_{B,t}A_{F,t}}{A_t^2}
 \frac{\Delta A_{t+1}}{\Delta A_t}
 \frac{\Delta M_{t+1}}{\Delta M_t}.
}                                                       \tag{14}
\]

Thus the bounded transition has reduced to a comparison between:

- the canonical evolution of the two chamber probabilities and barycentre
  gaps, on the left of (13);
- the inverse-length ratio demanded by the internal defect, on the right.

This is the next source-derived inequality to attack.  It involves only
truncated one-chamber moments at the fixed modular boundary.

## 8. Truncated score integration exposes one seam current

Let

\[
 Z_{B,t}=\int_0^a u^{2t}\Phi(u)\,du,
 \qquad
 Z_{F,t}=\int_a^\infty u^{2t}\Phi(u)\,du,
 \qquad
 Z_t=Z_{B,t}+Z_{F,t},
\]

with \(a=1/2\) and \(b=2t+1\).  Since

\[
 RW\Phi=-u\Phi',
\]

integration by parts on the two chambers gives

\[
\begin{aligned}
 \int_0^a u^{2t+2}W\Phi\,du
 &=bZ_{B,t}-a^b\Phi(a),\\
 \int_a^\infty u^{2t+2}W\Phi\,du
 &=bZ_{F,t}+a^b\Phi(a).
\end{aligned}                                           \tag{15}
\]

Therefore

\[
\boxed{
 \mathbb E_B(RW)=b-j_{B,t},
 \qquad
 \mathbb E_F(RW)=b+j_{F,t},
}                                                       \tag{16}
\]

where

\[
 j_{B,t}=\frac{a^b\Phi(a)}{Z_{B,t}},
 \qquad
 j_{F,t}=\frac{a^b\Phi(a)}{Z_{F,t}}.                   \tag{17}
\]

The two apparent currents are one object.  Since
\(p_t=Z_{B,t}/Z_t\) and \(q_t=Z_{F,t}/Z_t\),

\[
\boxed{
 p_tj_{B,t}=q_tj_{F,t}
 =:\mathfrak s_t
 =\frac{a^b\Phi(a)}{Z_t}.
}                                                       \tag{18}
\]

Thus the internal channels carry equal and opposite boundary defects:

\[
 p_t(-j_{B,t})+q_t(+j_{F,t})=0.
\]

Only the completed source recovers the universal identity
\(\mathbb E(RW)=b\).  This is the exact finite modular sewing current.

## 9. Adjacent transport of the seam amplitude

Because

\[
 Z_{t+1}=A_tZ_t,
\]

the scalar current obeys

\[
\boxed{
 \mathfrak s_{t+1}
 =\frac{a^2}{A_t}\mathfrak s_t
 =\frac{1}{4A_t}\mathfrak s_t.
}                                                       \tag{19}
\]

No chamber probability or fitted coefficient remains in this evolution.
The boundary contributes the fixed geometric factor \(a^2=1/4\); the source
contributes the ordinary radial mean \(A_t\).

The lower score moment has the parallel formulas, valid for \(t\ge1\):

\[
\begin{aligned}
 \int_0^a u^{2t}W\Phi\,du
 &=(b-2)Z_{B,t-1}-a^{b-2}\Phi(a),\\
 \int_a^\infty u^{2t}W\Phi\,du
 &=(b-2)Z_{F,t-1}+a^{b-2}\Phi(a).
\end{aligned}                                           \tag{20}
\]

Its common weighted seam amplitude is

\[
 \frac{a^{b-2}\Phi(a)}{Z_t}
 =a^{-2}\mathfrak s_t
 =4\mathfrak s_t.                                      \tag{21}
\]

Equations (18)--(21) show that every truncated score defect is generated by
one scalar current and its fixed powers of the boundary coordinate.

## 10. Meaning for the rank-one ratio

The barycentre gap \(\Delta M_t\) in (14) is not an arbitrary difference of
conditional expectations.  Equation (20) decomposes it into:

1. a difference of the two truncated lower Mellin ratios;
2. the explicit positive boundary contribution
   \(a^{b-2}\Phi(a)(Z_{B,t}^{-1}+Z_{F,t}^{-1})\).

Similarly, the \(RW\) channel in each conditional covariance carries the
opposite currents in (16).  The seam strength ratio must therefore be
studied with these boundary terms retained together; separating them would
destroy their exact cancellation in the completed source.

The next scalar calculation is to substitute (20) into
\(\Delta M_{t+1}/\Delta M_t\) in (14).  This will decide whether the fixed
geometric evolution (19) supplies the orientation demanded by (13).

## 11. Boundary repair minus hostile Mellin drag

Define the conditional inverse-radius means

\[
 r_{B,t}=\frac{Z_{B,t-1}}{Z_{B,t}}
 =\mathbb E_B(R^{-1}),
\qquad
 r_{F,t}=\frac{Z_{F,t-1}}{Z_{F,t}}
 =\mathbb E_F(R^{-1}).                                 \tag{22}
\]

Because every bounded point has smaller \(R\) than every far point,

\[
 r_{B,t}>r_{F,t}.                                      \tag{23}
\]

Equation (20) gives

\[
\begin{aligned}
 \Delta M_t
 &=(b-2)(r_{F,t}-r_{B,t})\\
 &\quad+
 a^{b-2}\Phi(a)
 \left(\frac1{Z_{B,t}}+\frac1{Z_{F,t}}\right).
\end{aligned}                                           \tag{24}
\]

Using \(a^{-2}=4\) and (18),

\[
 a^{b-2}\Phi(a)
 \left(\frac1{Z_{B,t}}+\frac1{Z_{F,t}}\right)
 =
 \frac{4\mathfrak s_t}{p_tq_t}.
\]

Therefore

\[
\boxed{
 \Delta M_t
 =
 \frac{4\mathfrak s_t}{p_tq_t}
 -(b-2)(r_{B,t}-r_{F,t}).
}                                                       \tag{25}
\]

The two terms have opposite meanings:

- the truncated lower Mellin bulk is hostile; it orders the chamber score
  means in the wrong direction;
- the finite boundary current is the unique positive repair.

Since \(W\) is strictly increasing, \(\Delta M_t>0\).  Hence the exact seam
inequality

\[
\boxed{
 \frac{4\mathfrak s_t}{p_tq_t}
 >
 (b-2)(r_{B,t}-r_{F,t})
}                                                       \tag{26}
\]

is already forced by the completed source.  This is not generic positivity:
it states precisely that modular sewing overcomes the inverse-moment drag
created by cutting the source.

Multiplying (25) by \(p_tq_t\Delta A_t\) gives the rank-one channel itself:

\[
\boxed{
 \mathcal R_t
 =
 \Delta A_t
 \left[
 4\mathfrak s_t
 -
 p_tq_t(b-2)(r_{B,t}-r_{F,t})
 \right].
}                                                       \tag{27}
\]

Thus the candidate cubic repair is literally a positive boundary current
minus a typed hostile bulk term.  The remaining adjacent theorem must control
the reserve ratio of the bracket in (27), not merely the decay of
\(\mathfrak s_t\) alone.

## 12. Dimensionless seam reserve

Define

\[
 \chi_t
 =
 \frac{
 p_tq_t(b-2)(r_{B,t}-r_{F,t})
 }{4\mathfrak s_t}.                                    \tag{28}
\]

Equation (26) says exactly

\[
 \boxed{0<\chi_t<1.}                                   \tag{29}
\]

Then

\[
\boxed{
 \mathcal R_t
 =4\mathfrak s_t\Delta A_t(1-\chi_t).
}                                                       \tag{30}
\]

The scalar \(1-\chi_t\) is the genuine modular repair reserve.  It measures
how much boundary current remains after paying the hostile inverse-moment
drag.

Using (19), its adjacent evolution becomes

\[
\boxed{
 \frac{\mathcal R_{t+1}}{\mathcal R_t}
 =
 \frac1{4A_t}
 \frac{\Delta A_{t+1}}{\Delta A_t}
 \frac{1-\chi_{t+1}}{1-\chi_t}.
}                                                       \tag{31}
\]

This is substantially sharper than (14).  The chamber probabilities and
score gaps have disappeared into one bounded scalar \(\chi_t\).

The monotone rank-one criterion (13) is now a single comparison between the
source ratio in (31) and the inverse-length ratio demanded by the internal
system.  A near-critical bounded transition can occur only through
\(\chi_t\uparrow1\), where the hostile Mellin drag nearly exhausts the
modular boundary current.

That gives the next hard falsifier: if \(1-\chi_t\) collapses faster than its
adjacent geometric compensation in (31), the seam cannot repair the cubic
defect even though \(\Delta M_t\) remains positive.
