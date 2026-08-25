# Theta cubic hazard phase

Status: live successor to theta-cubic-chamber-response.md.

## 1. Phase coordinates

For the far conditional law on \([a,\infty)\), put

\[
 m_t=\mathbb E_Fu,\qquad
 A_t=\mathbb E_FR,\qquad
 h_t=f_{F,t}(a),
\]

\[
 E_t=
 \mathbb E_F\left[V''(u)+\frac{2t}{u^2}\right],
\qquad
 I_t=\operatorname{Var}_F(\sigma_t),
\]

where

\[
 \sigma_t(u)=\frac{2t}{u}-V'(u).
\]

The boundary identities give

\[
 I_t=E_t-h_t'(a).                                      \tag{1}
\]

Define

\[
 \alpha_t=\frac{(A_t-a^2)h_t}{2m_t},
\qquad
 \beta_t=\frac{h_t'(a)}{E_t}.                          \tag{2}
\]

Then

\[
 0<\alpha_t<1,\qquad0\le\beta_t<1.
\]

## 2. Exact seam-improvement defect

The boundary-corrected Cramer floor differs from the unconditioned one by

\[
 \mathfrak H_t=\frac{(1-\alpha_t)^2}{1-\beta_t}.
\]

Define its signed numerator

\[
\boxed{
 \mathfrak D_t
 :=
 \beta_t-2\alpha_t+\alpha_t^2.
}                                                       \tag{3}
\]

Then

\[
 \boxed{
 \mathfrak H_t\ge1
 \quad\Longleftrightarrow\quad
 \mathfrak D_t\ge0.
}                                                       \tag{4}
\]

In unnormalized source variables, let

\[
 c_t=(A_t-a^2)h_t,
\qquad
 k_t=2m_t-c_t=-\operatorname{Cov}_F(R,\sigma_t)>0.
\]

Multiplying (3) by \(4m_t^2E_t\) gives

\[
\boxed{
 4m_t^2E_t\,\mathfrak D_t
 =
 4m_t^2h_t'(a)
 -4m_tc_tE_t
 +c_t^2E_t.
}                                                       \tag{5}
\]

Equivalently,

\[
\boxed{
 4m_t^2E_t\,\mathfrak D_t
 =
 k_t^2E_t-4m_t^2I_t.
}                                                       \tag{6}
\]

Thus seam improvement is itself a coupled positivity theorem between the
boundary-corrected Stein covariance and the far Fisher curvature.

## 3. Source-fixed boundary dynamics

The boundary hazard and score obey

\[
 \frac{h_{t+1}}{h_t}=\frac{a^2}{A_t},
\qquad
 \sigma_{t+1}(a)=\sigma_t(a)+\frac2a.                  \tag{7}
\]

Moreover,

\[
 h_t'(a)=h_t[\sigma_t(a)+h_t].                         \tag{8}
\]

These equations determine the boundary part of the phase trajectory without
approximation.  Only the far moments \(m_t,A_t,E_t\) remain to be transported
by size bias.

## 4. Formal far-mode balance

This subsection is asymptotic reconnaissance, not yet a uniform theorem.
Let \(u_t\) be the far saddle.  Primitive theta dominance gives

\[
 m_t\sim u_t,\qquad
 A_t-a^2\sim u_t^2,
\]

\[
 E_t\sim\frac{4t}{u_t},
\qquad
 \sigma_t(a)\sim\frac{2t}{a},
\qquad
 h_t'(a)\sim\frac{2t}{a}h_t.                           \tag{9}
\]

Therefore

\[
 \alpha_t\sim\frac{u_th_t}{2},
\qquad
 \beta_t\sim\frac{u_th_t}{2a}.                         \tag{10}
\]

It follows that

\[
\boxed{
 \frac{\beta_t}{2\alpha_t}
 \longrightarrow\frac1{2a}.
}                                                       \tag{11}
\]

## 5. Critical selection of the half-boundary

At leading order, the seam-improvement condition is

\[
 \beta_t\gtrsim2\alpha_t.
\]

Equation (11) predicts three regimes:

\[
\begin{array}{c|c}
 a<1/2 & \text{hazard repair dominates at leading order},\\
 a=1/2 & \text{leading-order critical balance},\\
 a>1/2 & \text{Stein loss dominates at leading order}.
\end{array}                                             \tag{12}
\]

Thus

\[
\boxed{
 a=\frac12
}
\]

is not merely the convenient endpoint of the previously proved curvature
chambers.  It is the unique cut at which the boundary hazard repair and the
lost Stein transport balance asymptotically.

This is a genuine coincidence between:

- the modular source boundary;
- the primitive/far proof boundary;
- the critical hazard phase boundary.

## 6. The first subleading term becomes decisive

At \(a=1/2\), (10) gives

\[
 \beta_t=2\alpha_t+o(\alpha_t)
\]

at leading order.  But the exact improvement boundary is

\[
 \beta_t=2\alpha_t-\alpha_t^2.
\]

Therefore the sign is decided by the first subleading difference

\[
\boxed{
 \mathfrak D_t
 =
 (\beta_t-2\alpha_t)+\alpha_t^2.
}                                                       \tag{13}
\]

The positive quadratic reserve \(\alpha_t^2\) can repair a small negative
linear mismatch.  This is another one-defect/one-repair structure.

The next calculation must retain one correction beyond (9):

1. the \(2t/u_t^2\) part of \(E_t\);
2. the finite \(V'(a)\) part of the boundary score;
3. the difference between \(m_t\) and \(u_t\);
4. the difference between \(A_t-a^2\) and \(u_t^2\);
5. the nonlinear hazard term \(h_t^2\).

Their combined sign determines whether the modular half-boundary lies on the
beneficial side of the parabola.

## 7. Subleading reconnaissance predicts a slight loss

At \(a=1/2\), retain the radial term in the far effective curvature:

\[
 E_t
 \sim
 \frac{4t}{u_t}+\frac{2t}{u_t^2}.
\]

The boundary score satisfies

\[
 \sigma_t(a)=4t-V'(1/2)=4t+O(1).
\]

Ignoring only terms smaller than \(u_t^{-1}\) relative to the leading
balance,

\[
\begin{aligned}
 \frac{\beta_t}{h_t}
 &=
 \frac{\sigma_t(a)+h_t}{E_t}\\
 &\sim
 \frac{4t}{4t/u_t+2t/u_t^2}\\
 &=
 \frac{u_t}{1+1/(2u_t)}
 =
 u_t-\frac12+O(u_t^{-1}).                              \tag{14}
\end{aligned}
\]

Meanwhile saddle concentration gives

\[
 m_t=u_t+o(1),
\qquad
 A_t=u_t^2+o(u_t),
\]

and therefore

\[
 \frac{2\alpha_t}{h_t}
 =
 \frac{A_t-1/4}{m_t}
 =
 u_t+o(1).                                             \tag{15}
\]

Thus the formal first mismatch is

\[
 \boxed{
 \beta_t-2\alpha_t
 =
 -\frac12h_t+o(h_t).
}                                                       \tag{16}
\]

The boundary hazard is exponentially small relative to the far saddle,
whereas

\[
 \alpha_t^2=O(u_t^2h_t^2)=o(h_t).
\]

Consequently

\[
 \boxed{
 \mathfrak D_t
 =
 -\frac12h_t+o(h_t)<0
}
                                                               \tag{17}
\]

is the asymptotic prediction.

This does not threaten the eventual cubic theorem.  It says only that
conditioning at the half-boundary makes the isolated far Cramer floor
slightly weaker than its unconditioned counterpart, by an exponentially
vanishing amount.  The full chamber response may still dominate the bounded
ceiling.

It does falsify a stronger explanation: the modular seam is not expected to
improve every positive component separately.  Its role is global sewing of
the chamber system, not monotone improvement of the far Fisher channel in
isolation.

## 8. The integer boundary split is exactly \(1,2,3\) versus \(t\ge4\)

At \(a=1/2\),

\[
 x=\pi e.
\]

Elementary rational bounds give

\[
 \frac{17}{2}<x<\frac{43}{5}.
\]

The primitive score is

\[
 V_1'(1/2)
 =
 2x-\frac52-\frac{4x}{2x-3}.                           \tag{18}
\]

This function is increasing for \(x>3/2\).  Evaluation at the two rational
endpoints gives

\[
 12<V_1'(1/2)<\frac{123}{10}.                          \tag{19}
\]

The completed-source mixture satisfies

\[
 V'=\sum_nw_nV_n',
\]

and the far label envelope from the degree-two proof gives

\[
 0<V'(1/2)-V_1'(1/2)
 <
 6x\sum_{n\ge2}n^6e^{-(n^2-1)x}
 <\frac1{100}.                                         \tag{20}
\]

Therefore

\[
\boxed{
 12<V'(1/2)<13.
}                                                       \tag{21}
\]

Since

\[
 t_\partial=\frac{V'(1/2)}4,
\]

we obtain

\[
\boxed{
 3<t_\partial<\frac{13}{4}.
}                                                       \tag{22}
\]

Consequently the integer tilts split canonically:

\[
\boxed{
\begin{array}{c|c}
 t=1,2,3 & \sigma_t(1/2)<0,\\
 t\ge4   & \sigma_t(1/2)>0.
\end{array}
}                                                       \tag{23}
\]

Thus only three integer tilts lie in the decreasing-at-the-seam regime.
This is an analytic source classification, not a numerical census.  The next
programme is correspondingly sharp:

1. prove one uniform positive-boundary-score theorem for all \(t\ge4\);
2. attack the three negative-score tilts through the exact seam Plucker
   identity, without moving the boundary.
