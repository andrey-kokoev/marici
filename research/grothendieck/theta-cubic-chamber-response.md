# Theta cubic chamber response

Status: live successor to theta-cubic-seam-plucker-flow.md.

## 1. Response theorem

For \(X=B,F\), let

\[
 A_X=\mathbb E_XR,\qquad
 \mathscr V_X=\frac{\operatorname{Var}_X(R)}{A_X}.
\]

Adjacent size bias changes the conditional radial mean by exactly
\(\mathscr V_X\).  Therefore

\[
 \Delta A_{t+1}-\Delta A_t
 =\mathscr V_{F,t}-\mathscr V_{B,t}.                    \tag{1}
\]

The strong sufficient theorem for convex chamber odds is

\[
 \boxed{\mathscr V_{F,t}\ge\mathscr V_{B,t}.}           \tag{2}
\]

## 2. Universal bounded-chamber ceiling

On \(B\), the variable \(R\) satisfies

\[
 0<R\le a^2.
\]

Bhatia--Davis therefore gives

\[
 \operatorname{Var}_B(R)
 \le A_B(a^2-A_B).
\]

Hence

\[
 \boxed{
 \mathscr V_B\le a^2-A_B.
}                                                       \tag{3}
\]

This is sharp for a two-endpoint law, precisely the hostile geometry that
made the separator-only conjecture fail.

## 3. Boundary-corrected far Stein identity

Let \(f_{F,t}\) be the normalized conditional density on \(F=[a,\infty)\),
and put

\[
 \sigma_t(u)=\partial_u\log f_{F,t}(u)
 =\frac{2t}{u}-V'(u).
\]

Its boundary density is

\[
 h_{F,t}=f_{F,t}(a)
 =\frac{a^{2t}\Phi(a)}{Z_{F,t}}
 =\frac{j_{F,t}}a.                                     \tag{4}
\]

Integration by parts gives

\[
 \mathbb E_F\sigma_t=-h_{F,t},                         \tag{5}
\]

and

\[
\boxed{
 \operatorname{Cov}_F(R,\sigma_t)
 =
 (A_F-a^2)h_{F,t}-2\mathbb E_Fu.
}                                                       \tag{6}
\]

Define

\[
 \mathcal I_{F,t}
 =\operatorname{Var}_F(\sigma_t).
\]

Cauchy--Schwarz gives the boundary-corrected Cramer--Rao floor

\[
\boxed{
 \operatorname{Var}_F(R)
 \ge
 \frac{
 \left[
 2\mathbb E_Fu-(A_F-a^2)h_{F,t}
 \right]^2
 }{
 \mathcal I_{F,t}
 }.
}                                                       \tag{7}
\]

The boundary term cannot be omitted.  It is the same modular seam hazard
that repaired the truncated score gap.

## 4. Scalar sufficient theorem

Combining (3) and (7), condition (2) follows from

\[
\boxed{
 \frac{
 \left[
 2\mathbb E_Fu-(A_F-a^2)h_{F,t}
 \right]^2
 }{
 A_F\mathcal I_{F,t}
 }
 \ge a^2-A_B.
}                                                       \tag{8}
\]

Every quantity in (8) is a one-chamber expectation or the fixed boundary
hazard.  No two-copy integral remains.

If (8) holds, then

\[
 \Delta A_{t+1}\ge\Delta A_t,
\]

which is stronger than the exact compensated condition required for
increasing odds increments.

## 5. Exact compensated fallback

Failure of (8) does not falsify the seam mechanism.  The true requirement is

\[
 \frac{\Delta A_{t+1}}{\Delta A_t}
 \ge\frac{A_{B,t+1}}{A_{F,t}},
                                                        \tag{9}
\]

whose right side is below one.  Thus the far response may lose to the
bounded response by a controlled amount.

The hostile test order is:

1. test the strong scalar inequality (8) analytically from theta curvature;
2. if it fails, retain the signed deficit
   \(\mathscr V_B-\mathscr V_F\);
3. compare that deficit with the exact separator allowance in (9);
4. do not alter the chamber boundary.

The next calculation is to express \(\mathcal I_{F,t}\) through the effective
curvature and boundary score, producing a fully source-explicit inequality.

## 6. Exact far Fisher denominator

Since

\[
 (\sigma_tf_{F,t})'
 =(\sigma_t'+\sigma_t^2)f_{F,t},
\]

integration over \([a,\infty)\) gives

\[
 -\sigma_t(a)h_{F,t}
 =
 \mathbb E_F\sigma_t'
 +\mathbb E_F\sigma_t^2.
\]

Using \(\mathbb E_F\sigma_t=-h_{F,t}\), we obtain

\[
\boxed{
 \mathcal I_{F,t}
 =
 \mathbb E_F\left[
 V''(u)+\frac{2t}{u^2}
 \right]
 -
 \left(\frac{2t}{a}-V'(a)\right)h_{F,t}
 -h_{F,t}^2.
}                                                       \tag{10}
\]

Thus (8) is now entirely explicit in:

- the far mean of the already-controlled effective curvature;
- the far first radial and square-root moments;
- the fixed seam values \(\Phi(a)\) and \(V'(a)\);
- the truncated partition \(Z_{F,t}\).

The two negative boundary terms in (10) are not defects in Fisher
information.  They remove the artificial information created by conditioning
the source at the seam.  Discarding them would enlarge the denominator,
weaken the Cramer--Rao floor, and erase the same repair current that appears
in the numerator of (8).

The strong chamber-response theorem has therefore reduced to one explicit
inequality with no latent differential or correspondence objects.

## 7. Source-sharp bounded ceiling

The bounded conditional density is proportional to

\[
 e^{-\mathcal V_t(u)},
 \qquad
 \mathcal V_t(u)=V(u)-2t\log u,
\]

on the convex interval \((0,a]\).  Its curvature is

\[
 \mathcal V_t''(u)
 =V''(u)+\frac{2t}{u^2}>0.
\]

The one-dimensional Brascamp--Lieb inequality on the truncated convex
domain gives

\[
\operatorname{Var}_B(R)
\le
\mathbb E_B
\left[
\frac{4u^2}{V''(u)+2t/u^2}
\right].
\]

Writing

\[
\mathcal K_t(u)=u^2V''(u)+2t,
\]

we obtain the source-sharp response ceiling

\[
\boxed{
\mathscr V_{B,t}
\le
\frac4{A_{B,t}}
\mathbb E_{B,t}
\left[
\frac{R^2}{\mathcal K_t}
\right].
}                                                       \tag{11}
\]

Because the completed source satisfies \(V''>10\),

\[
\boxed{
\mathscr V_{B,t}
\le
\frac4{A_{B,t}}
\mathbb E_{B,t}
\left[
\frac{R^2}{2t+10R}
\right].
}                                                       \tag{12}
\]

This retains the radial location of the bounded mass and is generally much
sharper than the endpoint-only Bhatia--Davis ceiling.

## 8. Both chamber responses use the same curvature

The far Fisher denominator (10) can be written

\[
\mathcal I_{F,t}
=
\mathbb E_{F,t}\left(\frac{\mathcal K_t}{R}\right)
-\sigma_t(a)h_{F,t}-h_{F,t}^2.                         \tag{13}
\]

Therefore the strong response ordering follows from

\[
\boxed{
\frac{
\left[
2\mathbb E_Fu-(A_F-a^2)h_F
\right]^2
}{
A_F
\left[
\mathbb E_F(\mathcal K_t/R)
-\sigma_t(a)h_F-h_F^2
\right]
}
\ge
\frac4{A_B}
\mathbb E_B(R^2/\mathcal K_t).
}                                                       \tag{14}
\]

This is the cross-chamber analogue of the global curvature corridor:

- the bounded wall uses the reciprocal curvature average
  \(\mathbb E_B(R^2/\mathcal K_t)\);
- the far wall uses the direct curvature average
  \(\mathbb E_F(\mathcal K_t/R)\);
- the modular boundary hazard corrects both the Stein numerator and Fisher
  denominator.

The two chambers are now compared through one completed-source field
\(\mathcal K_t\), not unrelated variance estimates.

## 9. Boundary hazard is an earned improvement

If the seam terms were discarded, the far lower bound would use

\[
\frac{4(\mathbb E_Fu)^2}
{A_F\mathbb E_F(\mathcal K_t/R)}.
\]

The true conditional expression instead replaces

\[
2\mathbb E_Fu
\longmapsto
2\mathbb E_Fu-(A_F-a^2)h_F,
\]

and

\[
\mathbb E_F(\mathcal K_t/R)
\longmapsto
\mathbb E_F(\mathcal K_t/R)-\sigma_t(a)h_F-h_F^2.
\]

The numerator correction weakens the floor, while the denominator correction
strengthens it.  Their competition is source-fixed.  Hence the seam cannot
be called beneficial merely because it lowers the Fisher denominator; its
net effect is the scalar hazard ratio

\[
\boxed{
\mathfrak H_t
=
\frac{
\left[
1-\dfrac{(A_F-a^2)h_F}{2\mathbb E_Fu}
\right]^2
}{
1-\dfrac{\sigma_t(a)h_F+h_F^2}
{\mathbb E_F(\mathcal K_t/R)}
}.
}                                                       \tag{15}
\]

Values \(\mathfrak H_t>1\) mean that conditioning at the modular seam
improves the far Cramer floor relative to the unconditioned form;
\(\mathfrak H_t<1\) means it weakens it.

This is the next hostile scalar to classify before attempting the full
cross-chamber inequality (14).

## 10. The Fisher correction is the hazard slope

Let

\[
 \mathfrak h_t(u)
 =
 \frac{f_t(u)}{\int_u^\infty f_t(v)\,dv}
\]

be the survival hazard of the unnormalized far density
\(f_t(u)=u^{2t}\Phi(u)\).  At the seam,

\[
 \mathfrak h_t(a)=h_{F,t}.
\]

Direct differentiation gives

\[
\boxed{
 \mathfrak h_t'(a)
 =
 h_{F,t}\bigl[\sigma_t(a)+h_{F,t}\bigr]
 =
 \sigma_t(a)h_{F,t}+h_{F,t}^2.
}                                                       \tag{16}
\]

The tilted theta density is log-concave, so its survival law has increasing
hazard.  Therefore

\[
 \boxed{\mathfrak h_t'(a)\ge0.}                         \tag{17}
\]

The conditional Fisher denominator is exactly

\[
\boxed{
 \mathcal I_{F,t}
 =
 \mathbb E_F(\mathcal K_t/R)-\mathfrak h_t'(a).
}                                                       \tag{18}
\]

Thus the denominator correction is always earned: conditioning removes the
positive hazard slope created at the seam.

## 11. Exact criterion for net seam improvement

Define

\[
 \alpha_t
 =
 \frac{(A_F-a^2)h_F}{2\mathbb E_Fu},
\qquad
 \beta_t
 =
 \frac{\mathfrak h_t'(a)}
      {\mathbb E_F(\mathcal K_t/R)}.                    \tag{19}
\]

Then

\[
 \mathfrak H_t=\frac{(1-\alpha_t)^2}{1-\beta_t}.
\]

Assuming the Stein numerator retains its natural sign
\(0\le\alpha_t\le1\), the seam improves the far floor exactly when

\[
\boxed{
 \beta_t\ge2\alpha_t-\alpha_t^2.
}                                                       \tag{20}
\]

This is a curvature-versus-hazard theorem:

- \(\alpha_t\) is the fraction of radial Stein transport consumed by the
  boundary displacement;
- \(\beta_t\) is the fraction of far Fisher curvature removed as artificial
  boundary information.

The seam helps only when the removed Fisher fraction dominates the quadratic
cost of the lost Stein numerator.

## 12. Canonical boundary-mode split

The boundary score is

\[
 \sigma_t(a)=\frac{2t}{a}-V'(a).
\]

It changes sign at the source-defined real tilt

\[
\boxed{
 t_\partial=\frac{aV'(a)}2.
}                                                       \tag{21}
\]

For \(t<t_\partial\), the far conditional density is already decreasing at
the seam.  For \(t>t_\partial\), it initially rises toward an interior mode.
This is the canonical split of the bounded transition range; it is fixed by
the source and cannot be moved to fit the cubic gate.

Since

\[
 \mathfrak h_t'(a)=h_F[\sigma_t(a)+h_F],
\]

the hazard repair changes character across \(t_\partial\):

- below it, increasing hazard requires the nonlinear term \(h_F\) to overcome
  a negative boundary score;
- above it, both terms reinforce the Fisher correction.

The next proof should treat these two source-defined regimes separately,
while retaining the single scalar criterion (20).

## 13. Both hazard coordinates lie in the unit interval

The far score derivative is

\[
 \sigma_t'(u)
 =-V''(u)-\frac{2t}{u^2}<0.
\]

Thus \(\sigma_t\) is strictly decreasing, while \(R=u^2\) is strictly
increasing.  Their covariance is strictly negative:

\[
 \operatorname{Cov}_F(R,\sigma_t)<0.
\]

Using (6),

\[
 (A_F-a^2)h_F-2\mathbb E_Fu<0,
\]

and therefore

\[
\boxed{0<\alpha_t<1.}                                  \tag{22}
\]

Similarly, (18) and positivity of the conditional score variance give

\[
 0\le\mathfrak h_t'(a)
 <\mathbb E_F(\mathcal K_t/R),
\]

so

\[
\boxed{0\le\beta_t<1.}                                 \tag{23}
\]

Hence the net seam factor

\[
 \mathfrak H_t=\frac{(1-\alpha_t)^2}{1-\beta_t}
\]

is parametrized by a canonical point \((\alpha_t,\beta_t)\) in the unit
square.  The improvement boundary

\[
 \beta=2\alpha-\alpha^2
\]

is the parabola separating beneficial from detrimental conditioning.

This supplies a compact phase portrait for the strong chamber-response
route.  The next analytic move is to derive the theta trajectory
\(t\mapsto(\alpha_t,\beta_t)\) from the exact boundary current and determine
on which side of that parabola it lies in the two regimes split by
\(t_\partial\).

## 14. Exact discrete hazard dynamics

The far boundary hazard evolves under adjacent size bias without remainder:

\[
\boxed{
 \frac{h_{F,t+1}}{h_{F,t}}
 =\frac{a^2}{A_{F,t}}<1.
}                                                       \tag{24}
\]

Thus the boundary density decays monotonically with tilt.  At the same time,

\[
\boxed{
 \sigma_{t+1}(a)=\sigma_t(a)+\frac2a.
}                                                       \tag{25}
\]

So adjacent transport moves the two ingredients of the hazard slope in
opposite ways:

- the boundary score increases by the fixed source-independent increment
  \(2/a\);
- the boundary hazard decreases by the exact radial factor
  \(a^2/A_{F,t}\).

Consequently

\[
 \mathfrak h_{t+1}'(a)
 =
 \frac{a^2h_{F,t}}{A_{F,t}}
 \left[
 \sigma_t(a)+\frac2a
 +\frac{a^2h_{F,t}}{A_{F,t}}
 \right].                                              \tag{26}
\]

Equations (24)--(26) give a closed discrete evolution for the boundary part
of \(\beta_t\).  The only remaining moving denominator is the far effective
curvature mean, which evolves by ordinary \(R\)-size bias.

This makes the next comparison sharply finite-dimensional: track one hazard,
one boundary score, and one far curvature mean across the source-defined
transition.  No new two-copy object is required.
