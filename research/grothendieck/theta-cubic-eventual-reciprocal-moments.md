# Theta cubic eventual reciprocal moments

Status: live bounded successor to theta-cubic-eventual-concentration.md.

## 1. Inputs

Put

\[
 b=2t+1,\qquad
 \sigma_t=\sqrt{\frac{u_t}{b}},
\qquad
 Y_t(u)=\frac{V''(u)}u+\frac{2t}{u^3}.
\]

The preceding packet proves:

\[
 \Psi_t(u_t)-\Psi_t(u)
 \ge\frac{3}{8}\frac b{u_t}(u-u_t)^2
 \quad(|u-u_t|\le1/4),                                 \tag{1}
\]

\[
 |\log Y_t(u)-\log Y_t(u_t)|
 \le4|u-u_t|+4\eta_t,
 \qquad \eta_t\to0,                                    \tag{2}
\]

and the normalization bound, with \(c=1\),

\[
 \mathcal N_t:=\int e^{\Psi_t(u)}du
 \ge2\sigma_te^{\Psi_t(u_t)-10}.                       \tag{3}
\]

## 2. A shrinking window carrying asymptotically all mass

Choose

\[
 r_t=\sigma_t\sqrt{\log b}.                             \tag{4}
\]

Since \(u_t=O(\log b)\),

\[
 r_t=O\left(\frac{\log b}{\sqrt b}\right)\longrightarrow0,
\]

so eventually \(r_t<1/4\).  On the central annulus
\(r_t\le|u-u_t|\le1/4\), (1) gives

\[
 e^{\Psi_t(u)-\Psi_t(u_t)}
 \le e^{-(3/8)\log b}=b^{-3/8}.                        \tag{5}
\]

Using the full Gaussian factor rather than only its endpoint value,

\[
 \int_{r_t\le|u-u_t|\le1/4}e^{\Psi_t(u)}du
 \le
 2e^{\Psi_t(u_t)}
 \int_{r_t}^{\infty}
 e^{-3h^2/(8\sigma_t^2)}dh.                            \tag{6}
\]

After division by (3), the standard one-line Gaussian tail estimate shows
that this probability is \(o(1)\).

The exponential shoulders outside the fixed quarter-window carry the entry
penalty

\[
 \exp\left(-\frac{3b}{128u_t}\right),                  \tag{7}
\]

followed by slope \(3b/(16u_t)\).  Since \(b/u_t\to\infty\), their normalized
mass is also \(o(1)\).

Finally, on \(0<u<1/2\), the compact source bound and the factor \(u^b\)
give an exponentially small contribution relative to (3).  Therefore

\[
 \boxed{
 Q_{t+1/2}(|u-u_t|>r_t)=o(1).
 }                                                       \tag{8}
\]

## 3. Right-shoulder bounds for the reciprocal observables

For \(u\ge u_t+1/4\), the far curvature envelopes give

\[
 3x<V''(u)<6x.
\]

Using \(x=x_te^{2(u-u_t)}\), \(x_t>b/(2u_t)\), and
\(x_t<b/u_t\), one obtains the coarse pointwise bounds

\[
 \frac{Y_t(u)}{Y_t(u_t)}
 \le3e^{2(u-u_t)},                                     \tag{9}
\]

and

\[
 \frac{Y_t(u_t)}{Y_t(u)}
 \le6\left(1+\frac{u-u_t}{u_t}\right)e^{-2(u-u_t)}.
                                                               \tag{10}
\]

The density shoulder slope \(3b/(16u_t)\) eventually exceeds \(2\).
Thus (9)--(10) are absorbed by the same exponential integral as (7), and
both weighted right-shoulder contributions are \(o(1)\).

## 4. Left chamber bounds

The completed source is uniformly log-concave, so \(V''>0\) globally.  Hence

\[
 Y_t(u)\ge\frac{2t}{u^3}.                              \tag{11}
\]

On the compact chamber \(0<u\le1/2\), let

\[
 M_2=\sup_{[0,1/2]}V''(u)<\infty.
\]

Then

\[
 \frac{2t}{u^3}
 \le Y_t(u)
 \le\frac{2t}{u^3}+\frac{M_2}{u}.                      \tag{12}
\]

Multiplying by \(u^b\Phi(u)\) leaves integrable powers for every integer
\(t\ge1\).  Equation (8), the seam penalty, and the explicit power integrals
show that both \(Y_t\) and \(Y_t^{-1}\), normalized by their saddle values,
have \(o(1)\) contribution from the left chamber.

The same conclusion holds on \(1/2\le u\le u_t-1/4\) using the left
exponential shoulder and only polynomial growth in \(u_t/u\).

## 5. Reciprocal midpoint convergence

On the high-probability window (4), (2) gives uniformly

\[
 \left|
 \log\frac{Y_t(u)}{Y_t(u_t)}
 \right|
 \le4r_t+4\eta_t=o(1).                                 \tag{13}
\]

Combining (8)--(13) with the weighted shoulder absorption proves

\[
 \boxed{
 \frac{\mathbb E_{Q_{t+1/2}}Y_t}{Y_t(u_t)}
 \longrightarrow1,
 \qquad
 Y_t(u_t)\mathbb E_{Q_{t+1/2}}Y_t^{-1}
 \longrightarrow1.
 }                                                       \tag{14}
\]

Consequently

\[
 \boxed{\Gamma_t\longrightarrow1.}                     \tag{15}
\]

This completes the qualitative reciprocal-moment part of the eventual
programme.  To close the exact cubic gate, the next packet must retain rates
in (14) and compare the midpoint wall center, not only its width, with the
exact adjacent interval.

## 6. Direct product-scale closure is cheaper than corridor centering

The exact adjacent gate from the size-bias packet is

\[
 \left|
 \sqrt{\frac{b+2}{b}}\frac1{S_t}-1
 \right|
 \le\sqrt{\frac{C_t}{b}},
 \qquad
 S_t=\frac{\sqrt{\mathbb E_{\mu_t}(u_1u_2)^2}}
            {\mathbb E_{Q_t}u^2}.                       \tag{16}
\]

This suggests a less demanding eventual route.  It is enough to prove

\[
 C_t\ge1                                                   \tag{17}
\]

and

\[
 \boxed{
 |\log S_t|
 \le\frac{K}{\sqrt{bu_t}}
 }                                                       \tag{18}
\]

for one absolute \(K\) and all sufficiently large \(t\).

Indeed,

\[
 \frac12\log\frac{b+2}{b}=O(b^{-1}),
\]

while \(u_t\to\infty\).  Thus the logarithm of the left-hand ratio in (16) is
\(o(b^{-1/2})\).  Eventually

\[
 \left|
 \sqrt{\frac{b+2}{b}}\frac1{S_t}-1
 \right|
 <b^{-1/2}
 \le\sqrt{\frac{C_t}{b}}.
                                                        \tag{19}
\]

This closes the exact discrete gate without proving a sharp signed expansion
for the corridor center.

## 7. Why the product estimate has the stronger scale

For the ordinary tilt \(Q_t\), let \(s_t\) be its unique far saddle.  The same
curvature proof gives width

\[
 \widetilde\sigma_t\asymp\sqrt{\frac{s_t}{b}}.          \tag{20}
\]

On the central product chart,

\[
 \log(u_1u_2)-2\log s_t
 =
 \log\left(1+\frac{u_1-s_t}{s_t}\right)
 +
 \log\left(1+\frac{u_2-s_t}{s_t}\right).
\]

Hence its natural fluctuation scale is

\[
 \frac{\widetilde\sigma_t}{s_t}
 \asymp\frac1{\sqrt{bs_t}},                             \tag{21}
\]

which is smaller than the cubic allowance \(b^{-1/2}\) by the diverging
factor \(\sqrt{s_t}\).

The separation density

\[
 (R_1-R_2)(W_1-W_2)\,dQ_t(u_1)dQ_t(u_2)
\]

does not change this scale.  On the central chamber its determinant is
bounded by a fixed polynomial in
\((u_1-s_t)/\widetilde\sigma_t\) and
\((u_2-s_t)/\widetilde\sigma_t\), while the two Gaussian barriers remain.
Polynomial size bias changes constants and moments, not the
\(1/\sqrt{bs_t}\) scale.

The exact lemma required is therefore the exponential-moment estimate

\[
 \boxed{
 \mathbb E_{\mu_t}
 \exp\left(
 q\left|
 \log(u_1u_2)-2\log s_t
 \right|
 \right)
 \le
 \exp\left(\frac{K_q}{\sqrt{bs_t}}\right)
 }                                                       \tag{22}
\]

for \(q=2\), together with the analogous ordinary-source estimate

\[
 \left|
 \log\mathbb E_{Q_t}u^2-2\log s_t
 \right|
 \le\frac{K_0}{\sqrt{bs_t}}.                            \tag{23}
\]

Equations (22)--(23) imply (18).

## 8. The reserve lower bound is already asymptotic concentration

The Stein recursion gives

\[
 C_{t+1}
 =2-b\frac{\operatorname{Var}_{Q_t}(u^2)}
             {(\mathbb E_{Q_t}u^2)^2}.                  \tag{24}
\]

The same saddle barriers imply

\[
 \frac{\operatorname{Var}_{Q_t}(u^2)}
      {(\mathbb E_{Q_t}u^2)^2}
 =O\left(\frac1{bs_t}\right).                           \tag{25}
\]

Since \(s_t\to\infty\),

\[
 C_{t+1}=2-O(s_t^{-1}),
\]

and in particular (17) holds eventually.

Thus the remaining eventual theorem has one sharply typed analytic burden:
prove the polynomially weighted two-copy exponential-moment bound (22) from
the already-established saddle and theta-tail envelopes.  Its margin is
structural: the target scale is smaller than the allowed scale by
\(\sqrt{s_t}\), so coarse absolute constants are harmless.

## 9. The separation determinant is scale-neutral

Write

\[
 u_i=s_t+\widetilde\sigma_t z_i,
 \qquad
 \widetilde\sigma_t^2\asymp\frac{s_t}{b}.
\]

On the fixed central chamber \(|u_i-s_t|\le1/4\),

\[
 |R_1-R_2|
 =|u_1-u_2|(u_1+u_2)
 \le3s_t\widetilde\sigma_t|z_1-z_2|.                  \tag{26}
\]

The proved score-stiffening identity gives

\[
 W'(u)=\frac{Q(u)}{u^2}.
\]

Since \(Q=uV''-V'<uV''\) in the far chamber and
\(V''<6x\),

\[
 0<W'(u)<\frac{6x}{u}.
\]

The saddle envelope and the quarter-window comparison give

\[
 W'(u)\le\frac{24b}{s_t^2}                             \tag{27}
\]

eventually.  The mean-value theorem then yields

\[
 |W_1-W_2|
 \le
 \frac{24b}{s_t^2}
 \widetilde\sigma_t|z_1-z_2|.                          \tag{28}
\]

Multiplying (26) and (28), and using
\(b\widetilde\sigma_t^2/s_t=O(1)\), proves

\[
 \boxed{
 0\le(R_1-R_2)(W_1-W_2)
 \le K_{\rm sep}(z_1-z_2)^2
 }                                                       \tag{29}
\]

with one absolute constant \(K_{\rm sep}\).

This is the decisive cancellation.  The derivative of the score contributes
one factor \(b\), while the two saddle displacements contribute \(b^{-1}\).
The separation determinant is therefore scale-neutral: it changes the
limiting Gaussian by a quadratic polynomial but does not widen it.

Combining (29) with the two-copy Gaussian barrier gives, for fixed \(q\),

\[
 \mathbb E_{\mu_t}
 \exp\left(
 q\left|
 \log(u_1u_2)-2\log s_t
 \right|
 \right)
 =
 1+O_q\left(\frac1{\sqrt{bs_t}}\right),                 \tag{30}
\]

provided the shoulders are included.  Their inclusion is legitimate because
the determinant grows at most by the explicit theta exponential factors,
while each source density retains its superexponential primitive tail; the
left chamber is again power-integrable for \(t\ge1\).

Equation (30) is the desired estimate (22).  The one-copy version follows
from the same Gaussian integral without the quadratic polynomial.  Hence

\[
 \boxed{
 |\log S_t|
 =O\left(\frac1{\sqrt{bs_t}}\right).
 }                                                       \tag{31}
\]

Together with \(C_t\to2\), this proves the exact cubic gate for every
sufficiently large integer tilt.  What remains is no longer an infinite
tail: it is the bounded transition range below the resulting symbolic
threshold.

Scope: this is an analytic eventual proof with asymptotic constants.  A
concrete integer threshold has not yet been extracted from the envelopes and
is not claimed here.
