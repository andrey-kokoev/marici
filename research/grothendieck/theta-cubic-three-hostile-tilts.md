# Theta cubic three hostile tilts

Status: live low-tilt successor.

## 1. Exact boundary deficits

At the modular boundary \(a=1/2\), define

\[
 c_t=V'(a)-4t=-\sigma_t(a).
\]

The proved rational source bound

\[
 12<V'(1/2)<13
\]

gives

\[
\boxed{
 8<c_1<9,\qquad
 4<c_2<5,\qquad
0<c_3<1.
}                                                       \tag{1}
\]

Thus \(t=1,2\) are strongly decreasing at the seam, while \(t=3\) is the
unique near-critical negative-score tilt.

The same rational endpoint calculation is sharper for the last case.  At
\(x=17/2\), the primitive score equals

\[
 2x-\frac52-\frac{4x}{2x-3}
 =\frac{169}{14}
 =12+\frac1{14}.
\]

The upper primitive bound \(123/10\) and label tail \(<1/100\) give

\[
\boxed{
 \frac1{14}<c_3<\frac{31}{100}.
}                                                       \tag{1a}
\]

## 2. Exponential domination of the far tail

For \(t=1,2,3\), the far conditional score satisfies

\[
 \sigma_t'(u)
 =-V''(u)-\frac{2t}{u^2}<0.
\]

Hence, for \(u=a+x\ge a\),

\[
 \sigma_t(a+x)\le\sigma_t(a)=-c_t.
\]

Integrating,

\[
 \boxed{
 \frac{f_{F,t}(a+x)}{f_{F,t}(a)}
 \le e^{-c_tx}.
}                                                       \tag{2}
\]

The likelihood ratio of the residual coordinate

\[
 X=u-a
\]

against an exponential law of rate \(c_t\) is decreasing.  Therefore

\[
\boxed{
 X\preceq_{\rm st}\operatorname{Exp}(c_t),
 \qquad
 \mathbb E_FX^k\le\frac{k!}{c_t^k}.
}                                                       \tag{3}
\]

The far boundary hazard also satisfies

\[
\boxed{h_{F,t}\ge c_t,}                                 \tag{4}
\]

either from normalization of (2) or from increasing survival hazard.

## 3. Consequences for \(t=1,2\)

For the first two tilts, (1) and (3) give source-independent rational
residual bounds:

\[
\begin{array}{c|c|c}
t&\mathbb E_FX&\mathbb E_FX^2\\
\hline
1&<1/8&<1/32\\
2&<1/4&<1/8.
\end{array}                                             \tag{5}
\]

Since \(u=a+X\),

\[
 A_F-a^2=2a\mathbb E_FX+\mathbb E_FX^2.                \tag{6}
\]

Thus every far moment entering the boundary Stein loss is confined to a
short seam layer for \(t=1,2\).  These tilts should be attacked with direct
boundary-current bounds, not saddle geometry.

## 4. Why \(t=3\) is the unique hard low tilt

For \(t=3\), the exponential rate is quantitatively positive by (1a), but
its coarse exponential moment bounds allow

\[
 \mathbb E_FX<14,\qquad \mathbb E_FX^2<392,
\]

which are far outside the seam scale.  Equations (2)--(3) remain true but
discard too much theta curvature to provide a useful cubic reserve.

At the next integer tilt, \(t=4\), the boundary score is already positive:

\[
 \sigma_4(a)=16-V'(a)>3.
\]

Therefore

\[
\boxed{
t=3
\text{ is the sole integer tilt adjacent to the boundary-mode crossing.}
}                                                       \tag{7}
\]

This is the natural candidate for the one near-critical secular event in the
bounded cubic programme.

## 5. Revised low-tilt attack

The finite transition is not three equally unrelated cases:

1. \(t=1,2\): prove the cubic seam inequality using the explicit exponential
   domination (3), the hazard lower bound (4), and the exact boundary current;
2. \(t=3\): retain the full Plucker/secular identity without coarse tail
   replacement;
3. \(t\ge4\): use the positive-boundary-score mode and eventual saddle
   mechanism.

The sharp falsifier is now concentrated at \(t=3\).  If the rank-one seam
explanation fails there, no amount of strengthening the easy \(t=1,2\)
tail estimates can repair it.
