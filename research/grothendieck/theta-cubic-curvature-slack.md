# Theta cubic curvature slack

Status: live bounded successor to theta-cubic-adjacent-size-bias.md.

## 1. The common curvature field

Under

\[
 dQ_t(u)\propto u^{2t}e^{-V(u)}\,du,\qquad R=u^2,
\]

define

\[
 \mathcal K_t(u)=u^2\left(V''(u)+\frac{2t}{u^2}\right)
 =2t+RW+uQ(u),
\]

where \(W=V'/u\) and \(Q=uV''-V'>0\).  The Cramer--Rao and
Brascamp--Lieb variance walls are

\[
 \mathsf L_t=
 \frac{4(\mathbb E\sqrt R)^2}
      {\mathbb E(\mathcal K_t/R)},
 \qquad
 \mathsf U_t=
 4\mathbb E(R^2/\mathcal K_t).
                                                        \tag{1}
\]

Their relative slack is

\[
 \Gamma_t=\frac{\mathsf U_t}{\mathsf L_t}
 =\frac{\mathbb E(R^2/\mathcal K_t)
        \mathbb E(\mathcal K_t/R)}
       {(\mathbb E\sqrt R)^2}\ge1.                       \tag{2}
\]

## 2. Canonical multiplicative-dispersion law

Introduce the \(\sqrt R\)-size-biased source

\[
 d\pi_t(u)=\frac{\sqrt R}{\mathbb E_{Q_t}\sqrt R}\,dQ_t(u)
\]

and the scale-normalized curvature

\[
 Y_t(u)=\frac{\mathcal K_t(u)}{R^{3/2}}.                 \tag{3}
\]

Then the slack becomes exactly

\[
 \boxed{
 \Gamma_t=
 \mathbb E_{\pi_t}Y_t\,
 \mathbb E_{\pi_t}Y_t^{-1}.
 }                                                       \tag{4}
\]

Thus the loss introduced by using two separate functional inequalities is
the multiplicative dispersion of one source field.  It vanishes precisely
when \(Y_t\) is constant.

Equivalently,

\[
 \boxed{
 \Gamma_t-1
 =\frac12\mathbb E_{\pi_t\otimes\pi_t}
 \frac{(Y_1-Y_2)^2}{Y_1Y_2}.
 }                                                       \tag{5}
\]

This is a positive two-copy separation energy in logarithmic curvature.

## 3. The global-range shortcut is unavailable

If \(0<m\le Y_t\le M\), the Kantorovich inequality would give

\[
 \Gamma_t\le\frac{(M+m)^2}{4Mm}
 =\cosh^2\left(\frac12\log\frac Mm\right).               \tag{6}
\]

But this route is structurally unavailable.  For integer cubic tilts
\(t\ge1\),

\[
 Y_t(u)\sim \frac{2t}{u^3}\qquad(u\downarrow0),
\]

while the completed theta potential forces growth again in the far chamber.
Hence the global oscillation of \(\log Y_t\) is unbounded even though both
expectations in (4) are finite.

The correct theorem must therefore be weighted.  Two viable forms are:

\[
 \mathbb E_{\pi_t}e^{Z_t}\,
 \mathbb E_{\pi_t}e^{-Z_t}\le 1+\eta_t,
 \qquad
 Z_t=\log Y_t-\mathbb E_{\pi_t}\log Y_t,                \tag{7}
\]

or a chamber decomposition in which endpoint contributions are absorbed by
the exact theta tails before applying a bounded-oscillation inequality on the
central chamber.

## 4. Sharp research target

The corridor strategy can succeed only if its allowed slack, computed from
the exact cubic interval, dominates \(\Gamma_t-1\).  This is necessary, not
by itself sufficient: the corridor must also be centered correctly.
Therefore the next calculation must:

1. derive source-exact endpoint envelopes for \(Y_t\) under the weighted law
   \(\pi_t\);
2. split primitive, transition, and far chambers using the already-proved
   theta curvature bounds;
3. estimate the two reciprocal exponential moments together, preserving
   their cancellation;
4. compare the resulting \(\Gamma_t\) directly with the corridor budget.

Bounding \(\mathbb E Y_t\) and \(\mathbb E Y_t^{-1}\) independently with
unrelated worst cases would destroy precisely the multiplicative coherence
measured by (5).  The paired product in (4) is the physical object.

## 5. Width and center are the complete corridor invariants

Let

\[
 \mathsf G_t=\sqrt{\mathsf L_t\mathsf U_t}
 =4\mathbb E\sqrt R\,
 \sqrt{
 \frac{\mathbb E(R^2/\mathcal K_t)}
      {\mathbb E(\mathcal K_t/R)}
 }.
                                                        \tag{8}
\]

Then

\[
 \mathsf L_t=\frac{\mathsf G_t}{\sqrt{\Gamma_t}},
 \qquad
 \mathsf U_t=\mathsf G_t\sqrt{\Gamma_t}.                \tag{9}
\]

For completeness, put

\[
 c_t^-=
 \frac{2t+3}{(\sqrt{(2t+1)/C_t}+1)^2},
 \qquad
 c_t^+=
 \frac{2t+3}{(\sqrt{(2t+1)/C_t}-1)^2},
\]

and define the exact variance interval obtained from the cubic gate by

\[
 v_t^-=\max\left\{0,\frac{A_t^2}{2t+1}(2-c_t^+)\right\},
 \qquad
 v_t^+=\frac{A_t^2}{2t+1}(2-c_t^-).                    \tag{10}
\]

The two functional inequalities close it exactly when

\[
 \boxed{
 v_t^-\sqrt{\Gamma_t}
 \le \mathsf G_t
 \le \frac{v_t^+}{\sqrt{\Gamma_t}}.
 }                                                       \tag{11}
\]

When \(v_t^->0\), in particular,

\[
 \Gamma_t\le\frac{v_t^+}{v_t^-}                         \tag{12}
\]

is only the width condition.  Equation (11) is the additional location
condition.  This correction prevents small curvature dispersion from being
mistaken for a proof when both walls are coherently displaced outside the
physical cubic interval.

If \(v_t^-=0\), the lower-variance side of the cubic interval is automatic
and no width ratio should be formed; only the Brascamp upper wall remains
decisive.

## 6. The slack lives at the canonical half tilt

The size-biased law introduced above is not an auxiliary measure:

\[
\begin{aligned}
 d\pi_t(u)
 &\propto \sqrt R\,u^{2t}\Phi(u)\,du\\
 &=u^{2t+1}\Phi(u)\,du.
\end{aligned}
\]

Therefore

\[
 \boxed{\pi_t=Q_{t+1/2}.}                               \tag{13}
\]

The entire functional-inequality slack is consequently measured at the
canonical midpoint between the two adjacent integer tilts whose Jensen
reserves are being compared:

\[
 \boxed{
 \Gamma_t
 =\mathbb E_{Q_{t+1/2}}Y_t\,
  \mathbb E_{Q_{t+1/2}}Y_t^{-1}.
 }                                                       \tag{14}
\]

This half-step is source-forced by the Stein pairing: Cramer--Rao contributes
one factor of \(u\), while Brascamp--Lieb contributes its reciprocal curvature
partner.  It is not a fitted interpolation.

The revised explanation target is now symmetric:

\[
 \boxed{
 \text{the half-tilt controls both the width and the center of transport
 between the two neighboring integer reserves.}
 }                                                       \tag{15}
\]

This suggests a better attack than three unrelated chamber estimates:
rewrite the two walls directly under \(Q_{t+1/2}\), then seek a midpoint
reflection or reciprocal pairing for \(Y_t\) and \(Y_t^{-1}\).  Such a
pairing would control their product and their relative scale simultaneously,
which is exactly the pair \((\Gamma_t,\mathsf G_t)\).

## 7. Both walls on the same midpoint law

Put

\[
 m_t=\mathbb E_{Q_t}u
 =\frac{\mathcal Z_{t+1/2}}{\mathcal Z_t},
\qquad
 a_t=\mathbb E_{Q_{t+1/2}}Y_t,
\qquad
 b_t=\mathbb E_{Q_{t+1/2}}Y_t^{-1}.                   \tag{16}
\]

The change of measure gives

\[
 \mathbb E_{Q_t}(\mathcal K_t/R)=m_ta_t,
 \qquad
 \mathbb E_{Q_t}(R^2/\mathcal K_t)=m_tb_t.             \tag{17}
\]

Therefore the two walls themselves are

\[
 \boxed{
 \mathsf L_t=\frac{4m_t}{a_t},
 \qquad
 \mathsf U_t=4m_tb_t.
 }                                                       \tag{18}
\]

Accordingly,

\[
 \boxed{
 \Gamma_t=a_tb_t,
 \qquad
 \mathsf G_t=4m_t\sqrt{\frac{b_t}{a_t}}.
 }                                                       \tag{19}
\]

This is the complete midpoint parametrization.  Width is the product of the
two reciprocal curvature moments; location is their ratio times the exact
half-moment \(m_t\).

The cubic corridor conditions become simply

\[
 \boxed{
 \frac{4m_t}{a_t}\ge v_t^-,
 \qquad
 4m_tb_t\le v_t^+.
 }                                                       \tag{20}
\]

There are now no unmatched probability measures in the proposed proof.
Everything difficult lives in the joint behavior of \(Y_t\) and \(Y_t^{-1}\)
under the single canonical midpoint law \(Q_{t+1/2}\).  This is the correct
place to apply modular chamber pairing.

## 8. Symbolic far-tilt reconnaissance

This subsection records an asymptotic target, not a proved estimate.

For the primitive theta carrier, put

\[
 x=\pi e^{2u}.
\]

The exact source formula has

\[
 V'(u)=2x+O(1),\qquad V''(u)=4x+O(1)                   \tag{21}
\]

in the far chamber; all higher arithmetic labels are exponentially smaller.
The midpoint law has effective potential

\[
 V(u)-(2t+1)\log u.
\]

Its saddle \(u_t\) therefore obeys

\[
 u_tV'(u_t)=2t+1,
\qquad
 x_t\sim\frac{t}{u_t},
\qquad
 u_t\sim\frac12\log t.                                 \tag{22}
\]

At the saddle,

\[
 \mathcal V_{t+1/2}''(u_t)
 =V''(u_t)+\frac{2t+1}{u_t^2}
 \sim\frac{4t}{u_t},                                   \tag{23}
\]

so the midpoint width is predicted to be

\[
 \operatorname{Var}_{Q_{t+1/2}}(u)
 \sim\frac{u_t}{4t}.                                   \tag{24}
\]

Meanwhile

\[
 Y_t(u_t)
 =\frac{V''(u_t)}{u_t}+\frac{2t}{u_t^3}
 \sim\frac{4t}{u_t^2},
\]

and

\[
 \left.(\log Y_t)'\right|_{u_t}=2+O(u_t^{-1}).          \tag{25}
\]

The resulting formal prediction is

\[
 \operatorname{Var}_{Q_{t+1/2}}(\log Y_t)
 =O\left(\frac{u_t}{t}\right)
 =O\left(\frac{\log t}{t}\right),                       \tag{26}
\]

and hence

\[
 \boxed{
 \Gamma_t=1+O\left(\frac{\log t}{t}\right).
 }                                                       \tag{27}
\]

The same saddle gives

\[
 C_t=2+O((\log t)^{-1}),
\qquad
 L_t=\sqrt{\frac{2t+1}{C_t}}
 =\sqrt t\left(1+O((\log t)^{-1})\right),               \tag{28}
\]

so

\[
 L_{t+1}-L_t=O(t^{-1/2}).                               \tag{29}
\]

Thus the exact unit gate should have increasing reserve in the far tilt.
The asymptotic architecture predicts:

\[
 \boxed{
 \text{one rigorous eventual saddle theorem}
 +\text{one bounded modular transition theorem},
 }
                                                               \tag{30}
\]

not an infinite census of Jensen orders.

## 9. What must be made rigorous

The eventual theorem requires only source-derived estimates already natural
for the theta carrier:

1. a unique saddle and a quadratic lower bound for the midpoint effective
   potential on its central window;
2. exponential tail bounds outside that window;
3. uniform primitive-label dominance at \(u_t\);
4. reciprocal exponential-moment control for \(\log Y_t\);
5. comparison of the resulting width and center bounds with (11).

No zero data or finite-order scouting enters this route.  Its falsifier is
analytic: failure of the predicted curvature-concentration rate, or a
corridor center that remains displaced despite \(\Gamma_t\to1\).

## 10. Rigorous first lemma: the far saddle is unique

Let

\[
 \Psi_t(u)=(2t+1)\log u-V(u)
\]

be the log density of the midpoint law, up to normalization, and put

\[
 g_t(u)=\Psi_t'(u)=\frac{2t+1}{u}-V'(u).                \tag{31}
\]

On the far chamber \(u\ge1/2\), the completed-source theorem already gives

\[
 Q(u)=uV''(u)-V'(u)>0.
\]

Every primitive label also has \(V_n'(u)>0\) there, and
\(V'=\sum_nw_nV_n'\), so \(V'(u)>0\).  Consequently

\[
 V''(u)=\frac{Q(u)+V'(u)}u>0
 \qquad(u\ge1/2).                                      \tag{32}
\]

It follows that

\[
 g_t'(u)=-\frac{2t+1}{u^2}-V''(u)<0.                   \tag{33}
\]

Since \(g_t(u)\to-\infty\) as \(u\to\infty\), whenever

\[
 2(2t+1)>V'(1/2),                                      \tag{34}
\]

there is exactly one \(u_t>1/2\) with \(g_t(u_t)=0\).
Thus the explicit symbolic threshold

\[
 t\ge t_{\mathrm{saddle}}
 :=
 \max\left\{
 1,\,
 1+\left\lfloor\frac{V'(1/2)-2}{4}\right\rfloor
 \right\}                                               \tag{35}
\]

places a unique mode in the far chamber.  No assertion about the exact
numerical value of this threshold is needed for the reduction.

This proves the qualitative part of the eventual architecture.  What remains
is quantitative concentration about this unique mode and absorption of the
bounded chamber \(0<u\le1/2\).

## 11. Exact primitive envelope at the saddle

For \(x=\pi e^{2u}\), the primitive potential satisfies

\[
 V_1'
 =2x-\frac52-\frac{4x}{2x-3},
\qquad
 V_1''
 =4x+\frac{24x}{(2x-3)^2}.                             \tag{36}
\]

The label ratios obey, for \(u\ge1/2\),

\[
 \frac{\phi_n}{\phi_1}
 \le2n^4e^{-(n^2-1)x}.                                 \tag{37}
\]

Since \(V'=\sum_nw_nV_n'\), the same labelwise comparison used in the
degree-two proof gives an explicit convergent envelope

\[
 |V'(u)-V_1'(u)|
 \le
 6x\sum_{n\ge2}n^6e^{-(n^2-1)x}
 =:\mathcal E_1(x).                                    \tag{38}
\]

At the saddle,

\[
 \frac{2t+1}{u_t}=V'(u_t),
\]

and therefore

\[
 \left|
 2x_t-\frac{2t+1}{u_t}
 -\frac52-\frac{4x_t}{2x_t-3}
 \right|
 \le\mathcal E_1(x_t).                                 \tag{39}
\]

Equation (39) is the rigorous replacement for the formal relation
\(x_t\sim t/u_t\).  The error is a positive explicit theta-label series
whose first exponent is \(-3x_t\).

The next lemma should derive the analogous envelope for \(V''\), use (39) to
obtain a quadratic lower bound for
\(\Psi_t(u_t)-\Psi_t(u)\), and integrate that bound directly against the two
reciprocal observables \(Y_t^{\pm1}\).
