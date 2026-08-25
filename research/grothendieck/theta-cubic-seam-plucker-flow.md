# Theta cubic seam Plucker flow

Status: live successor to theta-cubic-modular-seam-rank-one.md.

## 1. Chamber odds

At the fixed boundary \(a=1/2\), put

\[
 Z_{B,t}=\int_0^a u^{2t}\Phi(u)\,du,
 \qquad
 Z_{F,t}=\int_a^\infty u^{2t}\Phi(u)\,du,
\]

and define the far-to-bounded odds

\[
 \lambda_t=\frac{Z_{F,t}}{Z_{B,t}}.                    \tag{1}
\]

Because passage from \(t\) to \(t+1\) is \(R=u^2\) size bias and every far
point has larger \(R\) than every bounded point,

\[
 \boxed{\lambda_{t+1}>\lambda_t.}                      \tag{2}
\]

This is strict TP2 of the two chamber rows against adjacent Mellin columns.

## 2. The hostile term is an adjacent Plucker minor

The inverse-moment drag in the seam reserve contains

\[
\begin{aligned}
 &p_tq_t(r_{B,t}-r_{F,t})\\
 &\quad=
 \frac{
 Z_{F,t}Z_{B,t-1}-Z_{B,t}Z_{F,t-1}
 }{Z_t^2}.                                             \tag{3}
\end{aligned}
\]

The numerator is the adjacent chamber minor

\[
 \boxed{
 \Delta_t^{BF}
 =
 \det
 \begin{pmatrix}
 Z_{B,t-1}&Z_{B,t}\\
 Z_{F,t-1}&Z_{F,t}
 \end{pmatrix}
 >0.
}                                                       \tag{4}
\]

Equivalently,

\[
 \Delta_t^{BF}
 =
 Z_{B,t}Z_{B,t-1}(\lambda_t-\lambda_{t-1}).             \tag{5}
\]

Thus the hostile bulk is not arbitrary.  It is the positive oriented area
traversed by the chamber moment vector in one adjacent tilt step.

## 3. The repair fraction is normalized odds velocity

Let

\[
 j_{B,t}=\frac{a^{2t+1}\Phi(a)}{Z_{B,t}}
\]

be the bounded boundary hazard.  The dimensionless repair consumer from the
preceding packet is

\[
 \chi_t
 =
 \frac{
 p_tq_t(2t-1)(r_{B,t}-r_{F,t})
 }{4\mathfrak s_t}.
\]

Using \(a^2=1/4\), (3)--(5), and
\(\mathfrak s_t=a^{2t+1}\Phi(a)/Z_t\), all partition factors cancel:

\[
\boxed{
 \chi_t
 =
 \frac{
 (2t-1)(\lambda_t-\lambda_{t-1})
 }{
 j_{B,t-1}(1+\lambda_t)
 }.
}                                                       \tag{6}
\]

Therefore

\[
 \boxed{
 0<\chi_t<1
 \quad\Longleftrightarrow\quad
 (2t-1)(\lambda_t-\lambda_{t-1})
 <j_{B,t-1}(1+\lambda_t).
}                                                       \tag{7}
\]

The boundary hazard is the capacity of the modular seam; the adjacent odds
increment is the amount consumed transporting mass toward the far chamber.

## 4. The forward barycentre gap is the next odds step

Let

\[
 A_{B,t}=\frac{Z_{B,t+1}}{Z_{B,t}},
 \qquad
 A_{F,t}=\frac{Z_{F,t+1}}{Z_{F,t}}.
\]

Since

\[
 \frac{\lambda_{t+1}}{\lambda_t}
 =\frac{A_{F,t}}{A_{B,t}},
\]

we have

\[
\boxed{
 \Delta A_t=A_{F,t}-A_{B,t}
 =
 A_{B,t}
 \frac{\lambda_{t+1}-\lambda_t}{\lambda_t}.
}                                                       \tag{8}
\]

Thus the two factors in the rank-one seam channel are consecutive odds
increments:

- \(1-\chi_t\) is the capacity left after the backward step
  \(\lambda_t-\lambda_{t-1}\);
- \(\Delta A_t\) is the forward step
  \(\lambda_{t+1}-\lambda_t\).

## 5. Exact odds-flow form of the seam channel

Because

\[
 \mathfrak s_t=\frac{j_{B,t}}{1+\lambda_t},
\]

the rank-one completion is

\[
\boxed{
 \mathcal R_t
 =
 \frac{
 4j_{B,t}A_{B,t}
 }{
 \lambda_t(1+\lambda_t)
 }
 (\lambda_{t+1}-\lambda_t)(1-\chi_t).
}                                                       \tag{9}
\]

The boundary hazard itself evolves by

\[
\boxed{
 \frac{j_{B,t}}{j_{B,t-1}}
 =\frac1{4A_{B,t-1}}.
}                                                       \tag{10}
\]

Equations (6), (9), and (10) express the entire modular seam through one
positive odds trajectory \(\lambda_t\) and one boundary hazard trajectory
\(j_{B,t}\).

## 6. New theorem target

The bounded cubic transition is now a discrete curvature problem for the
odds flow.  The hard-to-vary target is:

\[
\boxed{
\text{the normalized odds velocity }\chi_t
\text{ and the forward odds step evolve coherently enough that }
\mathcal R_t
\text{ contracts the internal inverse-length defect.}
}                                                       \tag{11}
\]

The most informative next quantity is the cross ratio

\[
 \mathfrak q_t
 =
 \frac{
 (\lambda_{t+1}-\lambda_t)
 (\lambda_{t-1}+1)
 }{
 (\lambda_t-\lambda_{t-1})
 (\lambda_t+1)
 }.                                                     \tag{12}
\]

It compares consecutive odds velocities after normalizing by the available
chamber mass.  A source-derived monotonicity or one-sided bound for
\(\mathfrak q_t\), combined with the exact hazard evolution (10), would turn
the rank-one criterion into a scalar discrete transport theorem.

The falsifier is one reversal of this normalized odds curvature at an
integer tilt below the eventual saddle threshold.

## 7. The odds curvature is another positive correspondence

The Plucker minor (4) has the exact two-copy integral

\[
\boxed{
 \Delta_t^{BF}
 =
 \int_B\int_F
 u^{2t-2}v^{2t-2}(v^2-u^2)
 \Phi(u)\Phi(v)\,du\,dv.
}                                                       \tag{13}
\]

Normalize this positive integrand to a probability law
\(\xi_t^{BF}\) on \(B\times F\).  Then

\[
\boxed{
 \frac{\Delta_{t+1}^{BF}}{\Delta_t^{BF}}
 =
 \mathbb E_{\xi_t^{BF}}(uv)^2.
}                                                       \tag{14}
\]

Thus adjacent Plucker transport is precisely size bias by the squared
bounded--far product coordinate.

Since

\[
 \lambda_t-\lambda_{t-1}
 =
 \frac{\Delta_t^{BF}}{Z_{B,t}Z_{B,t-1}},
\]

we obtain

\[
\boxed{
 \frac{\lambda_{t+1}-\lambda_t}
      {\lambda_t-\lambda_{t-1}}
 =
 \frac{
 \mathbb E_{\xi_t^{BF}}(uv)^2
 }{
 A_{B,t}A_{B,t-1}
 }.
}                                                       \tag{15}
\]

The normalized odds curvature (12) is therefore

\[
\boxed{
 \mathfrak q_t
 =
 \frac{
 \mathbb E_{\xi_t^{BF}}(uv)^2
 }{
 A_{B,t}A_{B,t-1}
 }
 \frac{1+\lambda_{t-1}}{1+\lambda_t}.
}                                                       \tag{16}
\]

This is a faithful correspondence object:

\[
\text{bounded source point}
\times
\text{far source point}
\xrightarrow{(uv)^2\text{ size bias}}
\text{next seam minor}.
\]

The remaining bounded theorem is now a product-scale inequality on a
one-crossing support \(u\le a\le v\).  Unlike the global separation law, this
pair has a fixed geometric separator.  Any useful bound must exploit that
separator rather than treating \(u\) and \(v\) as two unrestricted source
copies.

## 8. Universal log-convexity of the raw seam minors

Push the positive measure

\[
 (v^2-u^2)\Phi(u)\Phi(v)\,du\,dv
 \quad\text{on }B\times F
\]

forward through

\[
 y=(uv)^2.
\]

Then (13) says

\[
 \Delta_t^{BF}=\int_0^\infty y^{t-1}\,d\vartheta(y)
\]

for one fixed positive measure \(\vartheta\).  Cauchy--Schwarz gives

\[
\boxed{
 (\Delta_{t+1}^{BF})^2
 <
 \Delta_t^{BF}\Delta_{t+2}^{BF}.
}                                                       \tag{17}
\]

Equivalently,

\[
\boxed{
 \frac{\Delta_{t+2}^{BF}}{\Delta_{t+1}^{BF}}
 >
 \frac{\Delta_{t+1}^{BF}}{\Delta_t^{BF}}.
}                                                       \tag{18}
\]

Thus the raw seam product scale grows monotonically under adjacent tilt.
This theorem is universal and exact.

It does not yet orient the normalized odds increments because (15) divides
by \(A_{B,t}A_{B,t-1}\), whose own factors increase by moment log-convexity.
The surviving coupled theorem is precisely

\[
 \boxed{
 \text{compare the growth rate of the cross-product moment ratio with the
 growth rate of two consecutive bounded-chamber moment ratios.}
}                                                       \tag{19}
\]

The geometric separator \(u\le a\le v\) is the additional datum that may
force this comparison.  Raw Stieltjes positivity alone cannot: it orients
both numerator and denominator but does not compare their speeds.

## 9. Exact conditional-variance frontier

For either chamber \(X=B,F\), adjacent size bias gives

\[
\begin{aligned}
 A_{X,t}-A_{X,t-1}
 &=
 \frac{\mathbb E_{X,t-1}(R^2)}
      {\mathbb E_{X,t-1}R}
 -\mathbb E_{X,t-1}R\\
 &=
 \frac{\operatorname{Var}_{X,t-1}(R)}
      {A_{X,t-1}}.
\end{aligned}                                           \tag{20}
\]

Consequently

\[
\boxed{
 \Delta A_t-\Delta A_{t-1}
 =
 \frac{\operatorname{Var}_{F,t-1}(R)}{A_{F,t-1}}
 -
 \frac{\operatorname{Var}_{B,t-1}(R)}{A_{B,t-1}}.
}                                                       \tag{21}
\]

Thus convexity of the chamber odds flow would follow from the
source-specific response inequality

\[
\boxed{
 \frac{\operatorname{Var}_{F,t}(R)}{A_{F,t}}
 \ge
 \frac{\operatorname{Var}_{B,t}(R)}{A_{B,t}}.
}                                                       \tag{22}
\]

The exact normalized condition is slightly weaker.  From (15), consecutive
odds increments increase precisely when

\[
\boxed{
 \frac{\Delta A_t}{\Delta A_{t-1}}
 \ge
 \frac{A_{B,t}}{A_{F,t-1}}.
}                                                       \tag{23}
\]

The right side is strictly below one because of the separator.  Therefore
the far response may be somewhat smaller than the bounded response without
destroying odds convexity.

## 10. Hostile separator counterexample

Condition (23) is not a consequence of separated support alone.  Scale the
boundary to \(R=1\).  Let the bounded chamber have two atoms at \(R=r\) and
\(R=1\), with equal masses and \(0<r<1\), and let the far chamber initially
be a point mass at \(R=1\).  Then

\[
 \lambda_t=\frac{2}{1+r^t}.
\]

Its first two increments satisfy

\[
 \lambda_1-\lambda_0=\frac{1-r}{1+r},
\]

and

\[
 \frac{\lambda_2-\lambda_1}{\lambda_1-\lambda_0}
 =\frac{2r}{1+r^2}<1.                                  \tag{24}
\]

Thus the odds increase but their velocity decreases.  Moving the far atom
slightly above one preserves the strict inequality by continuity; smooth
approximations of the atoms preserve it as well.

Therefore

\[
\boxed{
 \text{one geometric separator}
 +\text{positive seam minors}
 \not\Rightarrow
 \text{convex normalized odds flow}.
}                                                       \tag{25}
\]

The theta theorem must use the shapes of the two conditional source laws,
not merely their ordered supports.

## 11. Sharpened theta target

The completed theta source supplies two properties absent from the hostile
example:

1. the bounded conditional law has a smooth log-concave density rather than
   a boundary atom;
2. the far conditional law has a superexponential tail whose mode continues
   moving outward under tilt.

The next theorem should compare their size-bias responses directly.  The
minimal useful statement is (23), not the stronger variance ordering (22).
Written with (21), it permits an explicit deficit in the far variance
response, bounded by the separator factor
\(1-A_{B,t}/A_{F,t-1}\).

This is a one-dimensional truncated-source inequality.  It can be attacked
with the exact boundary currents and the uniform log-concavity theorem,
without returning to the full two-copy determinant.
