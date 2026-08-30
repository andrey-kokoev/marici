# Theta cubic tilt-three interface

Status: live exact-interface packet.

## 1. Boundary-score crossing

Put

\[
 c=V'(1/2)-12.
\]

The rational source bounds give

\[
\boxed{
 \frac1{14}<c<\frac{31}{100}.
}                                                       \tag{1}
\]

At the two adjacent tilts,

\[
 \sigma_3(1/2)=-c,
\qquad
 \sigma_4(1/2)=4-c.                                    \tag{2}
\]

Therefore

\[
\boxed{
 \frac{369}{100}<\sigma_4(1/2)<\frac{55}{14}.
}                                                       \tag{3}
\]

The interface crosses from a weakly decreasing far density to a uniformly
increasing one in a single source-fixed step.

## 2. Minimal hazard coordinates

Let \(h_3\) be the far boundary hazard at tilt three.  Increasing hazard and
\(\sigma_3(a)=-c\) imply

\[
 h_3\ge c.
\]

Define the hazard-excess coordinate

\[
 \rho=\frac{h_3}{c}\ge1.                               \tag{4}
\]

Then

\[
\boxed{
 h_3'(a)=c^2\rho(\rho-1).
}                                                       \tag{5}
\]

Thus \(\rho=1\) is the exact exponential-tail limit; \(\rho-1\) measures
the theta curvature beyond a pure exponential seam tail.

## 3. Exact transport to tilt four

Let

\[
 A_F=A_{F,3}=\mathbb E_{F,3}(u^2)>\frac14.
\]

The hazard recursion gives

\[
\boxed{
 h_4=\frac{h_3}{4A_F}
 =\frac{c\rho}{4A_F}<h_3.
}                                                       \tag{6}
\]

Together with (2),

\[
\boxed{
 h_4'(a)
 =
 \frac{c\rho}{4A_F}
 \left(
 4-c+\frac{c\rho}{4A_F}
 \right).
}                                                       \tag{7}
\]

Equations (5)--(7) are the complete boundary-hazard dynamics across the
critical interface.  No source integral remains except the three scalars
\((c,\rho,A_F)\).

The invariant comparison is the logarithmic hazard slope:

\[
 \frac{h_3'}{h_3}=c(\rho-1),
 \qquad
 \frac{h_4'}{h_4}=4-c+\frac{c\rho}{4A_F}.
                                                               \tag{8}
\]

Consequently

\[
\boxed{
 \frac{h_4'}{h_4}>\frac{369}{100},
}
                                                               \tag{9}
\]

whereas \(h_3'/h_3\) can approach zero.  For \(\rho>1\), the unnormalised
amplification is exactly

\[
\boxed{
 \frac{h_4'}{h_3'}
 =
 \frac{4-c+c\rho/(4A_F)}{4A_Fc(\rho-1)}.
}
                                                               \tag{10}
\]

It diverges in the exponential-tail limit \(\rho\downarrow1\).  The score
crossing therefore creates curvature rather than merely transporting the
small curvature already present at tilt three.

## 4. Interpretation

At tilt three, the hazard slope is generated only by the nonlinear excess
\(h_3-c\):

\[
 h_3'=h_3(h_3-c).
\]

At tilt four, the fixed score increment \(4\) supplies a positive linear
term:

\[
 h_4'=h_4(h_4+4-c).
\]

Thus the adjacent transport replaces a potentially near-zero nonlinear
repair by a uniformly positive linear repair.  This is the precise boundary
event that the global chamber decomposition had hidden.

## 5. Exact cubic interface gate

The two reserves are

\[
 C_3=7-5\frac{Z_4Z_2}{Z_3^2},
\qquad
 C_4=9-7\frac{Z_5Z_3}{Z_4^2}.                         \tag{11}
\]

The sole near-critical cubic gate is

\[
\boxed{
 \left|
 \sqrt{\frac9{C_4}}
 -
 \sqrt{\frac7{C_3}}
 \right|\le1.
}                                                       \tag{12}
\]

Equivalently, its scalar secular remainder is

\[
\boxed{
 \Sigma_3
 =
 C_3C_4-
 \left(3\sqrt{C_3}-\sqrt{7C_4}\right)^2
 \ge0.
}                                                       \tag{13}
\]

## 6. Far covariance closes under truncated score integration

For a general tilt \(t\), put

\[
 A_{F,t}=\mathbb E_{F,t}(R),
 \qquad
 r_{F,t}=\mathbb E_{F,t}(R^{-1}),
 \qquad
 h_t=\frac{a^{2t}\Phi(a)}{Z_{F,t}}.
\]

Integration by parts on \([a,\infty)\) gives the two exact identities

\[
 \mathbb E_{F,t}(RW)=2t+1+ah_t,
 \qquad
 \mathbb E_{F,t}(W)=\frac{h_t}{a}+(2t-1)r_{F,t}.
                                                               \tag{14}
\]

Hence the far internal covariance is not an uncontrolled integral:

\[
\boxed{
 C_{F,t}
 =2t+1+ah_t
 -A_{F,t}\left(\frac{h_t}{a}+(2t-1)r_{F,t}\right).
}
                                                               \tag{15}
\]

At the source-fixed seam \(a=1/2\), this becomes

\[
 C_{F,t}
 =2t+1+\frac{h_t}{2}
 -A_{F,t}\bigl(2h_t+(2t-1)r_{F,t}\bigr).              \tag{16}
\]

Size bias eliminates the tilt-four reciprocal moment exactly:

\[
 r_{F,4}=\frac1{A_{F,3}}=\frac1{A_F}.                  \tag{17}
\]

Therefore

\[
\boxed{
\begin{aligned}
 C_{F,3}
 &=7+\frac{c\rho}{2}
   -A_F\bigl(2c\rho+5r_{F,3}\bigr),\\
 C_{F,4}
 &=9+\frac{c\rho}{8A_F}
   -A_{F,4}\left(\frac{c\rho}{2A_F}+\frac7{A_F}\right).
\end{aligned}
}                                                       \tag{18}
\]

The important negative result is now exact: boundary hazard amplification
does not by itself close the cubic gate.  After all score and size-bias
identities are used, the far transport still depends on the two genuine
shape coordinates \(r_{F,3}\) and \(A_{F,4}\).  These are the reciprocal
and forward responses of the same tilt-three law.  Any successful next
inequality must couple them; bounding them independently discards the
adjacent-tilt structure.

## 7. The two shape coordinates are one Mellin-curvature profile

Let expectation now be under the far tilt-three law and define

\[
 K(\theta)=\log\mathbb E_{F,3}(R^\theta).
\]

Then

\[
 K''(\theta)
 =\operatorname{Var}_{F,3;\theta}(\log R)\ge0,          \tag{19}
\]

where the semicolon denotes the additional \(R^\theta\)-tilt.  The three
remaining moments are samples of this single convex function:

\[
 r_{F,3}=e^{K(-1)},
 \qquad
 A_F=e^{K(1)},
 \qquad
 A_{F,4}=e^{K(2)-K(1)}.                                \tag{20}
\]

In particular,

\[
\boxed{
 \log(A_Fr_{F,3})
 =\int_{-1}^{1}(1-|s|)K''(s)\,ds,
}                                                       \tag{21}
\]

and

\[
\boxed{
 \log\frac{A_{F,4}}{A_F}
 =\int_0^2(1-|s-1|)K''(s)\,ds.
}                                                       \tag{22}
\]

Thus the unresolved interface is not two unrelated moment bounds.  It is a
comparison of two adjacent triangular averages of the same log-scale
variance profile.  Ordinary log-convexity yields only

\[
 A_Fr_{F,3}\ge1,
 \qquad
 A_{F,4}\ge A_F,                                      \tag{23}
\]

which has the wrong strength to orient the secular remainder.  The next
source-specific theorem should control the transport of \(K''\) from
\([-1,1]\) to \([0,2]\).  A monotonicity or one-crossing law for this
Mellin-curvature profile would couple exactly the two terms left in (18).

Indeed, translate the second triangular window back to \([-1,1]\) and put

\[
\boxed{
 \Omega_{34}
 =\int_{-1}^{1}(1-|s|)
   \bigl(K''(s)-K''(s+1)\bigr)\,ds.
}                                                       \tag{24}
\]

Equations (21)--(22) give the exact transport identity

\[
\boxed{
 A_{F,4}=A_F^2r_{F,3}e^{-\Omega_{34}}.
}                                                       \tag{25}
\]

Thus (18) becomes

\[
\boxed{
\begin{aligned}
 C_{F,3}
 &=7+\frac{c\rho}{2}
   -A_F\bigl(2c\rho+5r_{F,3}\bigr),\\
 C_{F,4}
 &=9+\frac{c\rho}{8A_F}
   -A_Fr_{F,3}e^{-\Omega_{34}}
      \left(\frac{c\rho}{2}+7\right).
\end{aligned}
}                                                       \tag{26}
\]

This is the first paired form of the far interface: the same reciprocal
shape coordinate occurs in both tilts, and all failure of naive transport
is carried by the single oriented curvature flux \(\Omega_{34}\).

A sufficient but deliberately stronger source theorem would be

\[
 K''(s+1)\le K''(s)
 \quad(-1\le s\le1),                                  \tag{27}
\]

which implies \(\Omega_{34}\ge0\) and

\[
 A_{F,4}\le A_F^2r_{F,3}.                             \tag{28}
\]

Pointwise monotonicity is stronger than the corresponding weighted sign
target \(\Omega_{34}\ge0\); a single crossing of the two variance profiles
could still establish that sign.  The next section tests this candidate
against the source's local seam geometry.

## 8. The exponential seam model reverses the naive sign

The preceding sufficient sign is not compatible with the natural local
model of the exceptional tilt.  Since

\[
 K'''(\theta)
 =\mathbb E_{F,3;\theta}
   \left[(\log R-\mathbb E_{F,3;\theta}\log R)^3\right], \tag{29}
\]

the sign of the variance transport is the skewness of log-scale.  Moreover,

\[
\boxed{
 \Omega_{34}
 =-\int_{-1}^{1}(1-|s|)
   \int_s^{s+1}K'''(v)\,dv\,ds.
}                                                       \tag{30}
\]

In the exactly seam-pinned model

\[
 Y=\log R=y_0+X,
 \qquad X\sim\operatorname{Exp}(\lambda),\quad\lambda>2,
\]

one has

\[
 K''(\theta)=\frac1{(\lambda-\theta)^2},
 \qquad K'''(\theta)=\frac2{(\lambda-\theta)^3}>0.     \tag{31}
\]

Hence \(\Omega_{34}<0\), not \(\Omega_{34}\ge0\).  The earlier
monotonicity proposal is therefore a deliberately hostile falsifier, not a
plausible theta theorem.  This agrees with the geometry: a distribution
pinned against a left endpoint normally has positive log-scale skewness,
and forward size bias increases its variance.

The viable source theorem is quantitative:

\[
\boxed{
 -\Omega_{34}\le \mathcal B(c,\rho,A_F,r_{F,3}),
}                                                       \tag{32}
\]

where the admissible budget \(\mathcal B\) is obtained by substituting
(26) and the chamber seam terms into the exact secular inequality (13).
In other words, the interface need not reverse the natural skewness.  It
must show that the skewness-generated amplification

\[
 e^{-\Omega_{34}}>1
\]

does not consume the score-jump and rank-one seam reserves.  This is a much
harder-to-vary statement than an incorrect global sign law.

## 9. Seam decomposition at the interface

Write

\[
 C_j=I_j+\mathcal R_j,
\qquad j=3,4,
\]

where \(I_j\) is the sum of the two internal chamber covariances and
\(\mathcal R_j\) the rank-one seam term.  Its exact ratio is

\[
\boxed{
 \frac{\mathcal R_4}{\mathcal R_3}
 =
 \frac1{4A_3^{\mathrm{glob}}}
 \frac{\Delta A_4}{\Delta A_3}
 \frac{1-\chi_4}{1-\chi_3}.
}                                                       \tag{33}
\]

Here \(A_3^{\mathrm{glob}}=\mathbb E_{Q_3}(R)\); it is distinct from the
far conditional mean \(A_F=A_{F,3}\) used above.

The interface theorem is now finite-dimensional:

1. express \(\chi_3,\chi_4\) through the adjacent chamber odds;
2. express the far internal parts through (18), coupling rather than
   separating \(r_{F,3}\) and \(A_{F,4}\);
3. insert \(\mathcal R_3,\mathcal R_4\) into (13);
4. show that the score jump \(4\) supplies the missing secular reserve.

The falsifier is exact: \(\Sigma_3<0\).  No other negative-boundary-score
tilt is adjacent to the positive-mode regime.

## 10. Exact carrier-loss form of the cubic gate

The Stein recursion and strict nondegeneracy give

\[
 0<C_3<2,
 \qquad
 0<C_4<2.                                               \tag{34}
\]

Set

\[
 a_3=\sqrt{\frac7{C_3}}>1.
\]

Then the cubic gate (12) is exactly the interval condition

\[
\boxed{
 D_-(C_3)\le C_4\le D_+(C_3),
}
                                                               \tag{35}
\]

where

\[
 D_-(C)=\frac{9C}{(\sqrt7+\sqrt C)^2},
 \qquad
 D_+(C)=\frac{9C}{(\sqrt7-\sqrt C)^2}.                 \tag{36}
\]

This separates the two possible failure directions instead of hiding them
inside the squared secular expression.

Let \(p_4,q_4\) be the bounded/far chamber masses.  Using (26), define

\[
\begin{aligned}
 \Gamma_4
 &:=p_4C_{B,4}+\mathcal R_4
   +q_4\left(9+\frac{c\rho}{8A_F}\right),\\
 \Pi_4
 &:=q_4A_Fr_{F,3}\left(7+\frac{c\rho}{2}\right)>0.
\end{aligned}                                          \tag{37}
\]

The full tilt-four reserve now has the exact one-channel form

\[
\boxed{
 C_4=\Gamma_4-\Pi_4e^{-\Omega_{34}}.
}                                                       \tag{38}
\]

Thus increasingly negative Mellin-curvature flux moves \(C_4\) strictly
downward.  It can never cause failure through the upper boundary \(D_+\).
Its only possible failure is exhaustion of the lower carrier:

\[
 \Gamma_4-\Pi_4e^{-\Omega_{34}}<D_-(C_3).              \tag{39}
\]

Equivalently, provided \(\Gamma_4>D_-(C_3)\), the precise admissible flux
budget is

\[
\boxed{
 -\Omega_{34}
 \le
 \log\left(
  \frac{\Gamma_4-D_-(C_3)}{\Pi_4}
 \right).
}                                                       \tag{40}
\]

This is the carrier-loss formulation sought from the magnetic analogy.
There are two logically prior carrier gates:

\[
 \Gamma_4>D_-(C_3),
 \qquad
 \Gamma_4-D_-(C_3)\ge\Pi_4.                            \tag{41}
\]

The first says that bounded internal curvature, the score-jump baseline, and
the rank-one seam even reach the cubic admissible region before the skew
channel is inserted.  The second is the zero-flux reserve.  Negative flux
can destroy the cubic gate only after consuming their ratio in (40).

Accordingly the next theorem is no longer a sign claim.  It is the coupled
source inequality

\[
\boxed{
 \Pi_4e^{-\Omega_{34}}
 \le \Gamma_4-D_-(C_3).
}                                                       \tag{42}
\]

Its falsifier is simultaneous: the transported skew channel exceeds the
sum of every independent carrier remaining above the exact lower cubic
boundary.  No nullspace or finite tilt census is needed to state that event.

## 11. Skew and seam share one size-bias transport

The far chamber mass is itself transported by size bias:

\[
\boxed{
 q_4
 =q_3\frac{A_F}{A_3^{\mathrm{glob}}}.
}                                                       \tag{43}
\]

Using (25), the dangerous term in (38) therefore simplifies to

\[
\boxed{
 \Pi_4e^{-\Omega_{34}}
 =\frac{q_3}{A_3^{\mathrm{glob}}}
   A_{F,4}\left(7+\frac{c\rho}{2}\right).
}                                                       \tag{44}
\]

Meanwhile the seam transport (33) reads

\[
\boxed{
 \mathcal R_4
 =\frac{\mathcal R_3}{4A_3^{\mathrm{glob}}}
   \frac{\Delta A_4}{\Delta A_3}
   \frac{1-\chi_4}{1-\chi_3}.
}                                                       \tag{45}
\]

The common denominator is source-forced.  The adverse far response and the
positive rank-one repair are two channels of the same global size-bias step,
not independently normalized estimates.  Their exact competition is

\[
\boxed{
 \frac{\mathcal R_4}{\Pi_4e^{-\Omega_{34}}}
 =
 \frac{\mathcal R_3}{4q_3A_{F,4}
        (7+c\rho/2)}
 \frac{\Delta A_4}{\Delta A_3}
 \frac{1-\chi_4}{1-\chi_3}.
}                                                       \tag{46}
\]

The global normalization has cancelled.  This is the first genuine
two-carrier comparison at the interface.  What remains is local to the
tilt-three far law, the adjacent chamber response, and the seam-consumption
ratio.  A proof that estimates the two channels separately would reintroduce
the normalization that the exact transport has already removed.

There is one final cancellation.  Recall

\[
 \mathcal R_3=4\mathfrak s_3\Delta A_3(1-\chi_3),
 \qquad
 \mathfrak s_3=a q_3h_3
 =\frac12q_3c\rho.                                    \tag{47}
\]

Substitution into (46) cancels \(q_3\), \(\Delta A_3\), and
\(1-\chi_3\), giving

\[
\boxed{
 \frac{\mathcal R_4}{\Pi_4e^{-\Omega_{34}}}
 =
 \frac{c\rho\,\Delta A_4(1-\chi_4)}
      {A_{F,4}(14+c\rho)}.
}                                                       \tag{48}
\]

This identity changes the interpretation.  The seam is not an arbitrary
positive counterterm whose absolute size must be estimated.  Its repair
fraction is exactly the product of:

1. the small boundary-score defect \(c\rho/(14+c\rho)\);
2. the normalized chamber separation \(\Delta A_4/A_{F,4}\);
3. the surviving seam fraction \(1-\chi_4\).

All three are source-typed and dimensionless.  In particular, the seam alone
cannot be presumed to dominate the adverse far channel: its coefficient
contains the near-critical factor \(c\).  The large carrier must come from
the score-jump baseline and bounded internal covariance, while the seam
supplies a precisely normalized correction.  This rules out a misleading
``rank-one repair does everything'' explanation of the cubic interface.

Indeed,

\[
 0<\frac{\Delta A_4}{A_{F,4}}<1,
 \qquad
 0<1-\chi_4<1,
 \qquad
 0<\frac{c\rho}{14+c\rho}<1.
\]

Therefore (48) proves the strict universal ordering

\[
\boxed{
 0<\mathcal R_4<\Pi_4e^{-\Omega_{34}}.
}                                                       \tag{49}
\]

So the rank-one seam repair never cancels the complete transported far-shape
cost, regardless of the detailed theta tail.  The cubic gate, if true, is
necessarily a genuinely coupled positivity theorem: the bounded chamber and
the score-jump carrier must contribute essentially.  This is an exact
elimination of one proposed explanation, not an asymptotic or numerical
observation.

More sharply, (48) implies

\[
 \frac{\mathcal R_4}{\Pi_4e^{-\Omega_{34}}}
 <\frac{c\rho}{14+c\rho}.
\]

Hence the net transported far cost obeys

\[
\boxed{
 \Pi_4e^{-\Omega_{34}}-\mathcal R_4
 >
 \frac{14}{14+c\rho}\,
 \Pi_4e^{-\Omega_{34}}.
}                                                       \tag{50}
\]

At least this fixed fraction must be absorbed by the bounded internal and
score-jump carriers.  The remaining attack is consequently narrower: prove
that those two carriers exceed the explicit residual in (50) plus the lower
cubic boundary \(D_-(C_3)\).  The seam has now been eliminated as an
independent unknown from that burden.

## 12. Scope correction: the seam is a cut-cancellation term

The preceding comparison is algebraically correct, but the interpretation of
\(\mathcal R_t\) as an independent physical repair carrier is too strong.
The exact truncated score identities expose its actual role.

For an arbitrary cut \(a>0\), let

\[
 j_t=\frac{a^{2t}\Phi(a)}{Z_t}.
\]

The bounded and far conditional score identities are

\[
\begin{aligned}
 \mathbb E_{B,t}(RW)&=2t+1-ah_{B,t},\\
 \mathbb E_{B,t}(W)&=(2t-1)r_{B,t}-\frac{h_{B,t}}a,\\
 \mathbb E_{F,t}(RW)&=2t+1+ah_{F,t},\\
 \mathbb E_{F,t}(W)&=(2t-1)r_{F,t}+\frac{h_{F,t}}a.
\end{aligned}                                          \tag{51}
\]

Because

\[
 p_th_{B,t}=q_th_{F,t}=j_t,
\]

the boundary contribution in the weighted internal covariances is exactly

\[
 -\frac{j_t}{a}\Delta A_t.                            \tag{52}
\]

On the other hand, the conditional score gap is

\[
 \Delta M_t
 =\frac{j_t}{ap_tq_t}
 -(2t-1)(r_{B,t}-r_{F,t}),                            \tag{53}
\]

so the first part of the rank-one term is

\[
 p_tq_t\Delta A_t\frac{j_t}{ap_tq_t}
 =\frac{j_t}{a}\Delta A_t.                            \tag{54}
\]

Equations (52) and (54) cancel identically.  The remaining inverse-moment
terms recombine by the elementary identity

\[
\begin{aligned}
 &p_tA_{B,t}r_{B,t}+q_tA_{F,t}r_{F,t}\\
 &\quad+p_tq_t\Delta A_t(r_{B,t}-r_{F,t})
 =A_t^{\mathrm{glob}}r_t^{\mathrm{glob}}.
\end{aligned}                                          \tag{55}
\]

Therefore the complete chamber decomposition collapses exactly to

\[
\boxed{
 C_t
 =2t+1-(2t-1)A_t^{\mathrm{glob}}r_t^{\mathrm{glob}}.
}                                                       \tag{56}
\]

This is the undecomposed global score identity.  No cut coordinate remains.

Consequently, statements (48)--(50) compare legitimate terms inside one
chosen chamber presentation, but they do **not** identify separately existing
physical repair channels.  The rank-one seam is the covariance correction
required by the law of total covariance, and its boundary-current part
precisely removes the artificial current created by truncating the source.

The durable explanation is therefore:

\[
\boxed{
 \text{cut source}
 +\text{conditional score currents}
 +\text{rank-one recombination}
 =\text{one undecomposed global covariance}.
}                                                       \tag{57}
\]

This supersedes the proposed next step of proving positivity by independently
estimating bounded, score-jump, and seam carriers.  Such estimates can remain
useful analytically, but their individual sizes are chart data.  The invariant
cubic frontier must be stated directly in the global adjacent moment ratios
or in a source-derived transport that does not depend on the arbitrary cut.

## 13. Cut-free global curvature flux

Write

\[
 a_t=\log Z_t,
 \qquad
 \eta_t=a_{t+1}-2a_t+a_{t-1}
 =\log\frac{Z_{t+1}Z_{t-1}}{Z_t^2}.                   \tag{58}
\]

Then (56) becomes

\[
\boxed{
 C_t=2t+1-(2t-1)e^{\eta_t}.
}                                                       \tag{59}
\]

For the exceptional interface, put

\[
 x=e^{\eta_3}=\frac{Z_4Z_2}{Z_3^2},
 \qquad
 \Omega_3^{\mathrm{glob}}=\eta_3-\eta_4.
\]

Strict moment log-convexity and \(C_3>0\) give

\[
 1<x<\frac75.                                         \tag{60}
\]

The two reserves are now

\[
\boxed{
 C_3=7-5x,
 \qquad
 C_4=9-7xe^{-\Omega_3^{\mathrm{glob}}}.
}                                                       \tag{61}
\]

This is the invariant version of (38).  All chamber masses, hazards, seam
currents, and conditional moments have disappeared.

To expose its source meaning, define the global tilt-three cumulant

\[
 K_3(\theta)=\log\mathbb E_{Q_3}(R^\theta).
\]

Exactly as before,

\[
\boxed{
 \Omega_3^{\mathrm{glob}}
 =\int_{-1}^{1}(1-|s|)
  \bigl(K_3''(s)-K_3''(s+1)\bigr)\,ds.
}                                                       \tag{62}
\]

Thus the chamber analysis did reveal the right mathematical object, but in
a nonfaithful coordinate system.  The faithful object is the translated
Mellin-variance flux of the entire theta source.

Substituting (61) into the lower boundary of (35) gives the exact negative
flux budget

\[
\boxed{
 -\Omega_3^{\mathrm{glob}}
 \le
 \log\left(
  \frac{9-D_-(7-5x)}{7x}
 \right).
}                                                       \tag{63}
\]

The right side depends on the single preceding curvature coordinate \(x\).
This is the cut-free theorem target.  Its falsifier is a theta source whose
unit Mellin shift increases the triangular log-variance average beyond the
explicit budget in (63).

The remaining upper boundary is

\[
 xe^{-\Omega_3^{\mathrm{glob}}}
 \ge\frac{9-D_+(7-5x)}7,                               \tag{64}
\]

whenever the right side is positive.  Negative curvature flux increases the
left side, so it cannot violate (64).  The near-critical hostile direction is
therefore uniquely the lower-reserve exhaustion encoded by (63).
