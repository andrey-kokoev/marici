# Theta cubic chi-square contraction

Status: live direct-route packet.

## 1. Adjacent tilt as a likelihood-ratio experiment

The adjacent theta laws satisfy

\[
 \frac{dQ_t}{dQ_{t-1}}(u)
 =\frac{R(u)}{A_{t-1}},
 \qquad
 R=u^2,
 \qquad
 A_{t-1}=\mathbb E_{Q_{t-1}}R.                        \tag{1}
\]

Thus the canonical tilt step is a size-bias likelihood ratio, not merely a
relation between moment tables.

Its Pearson divergence is

\[
\begin{aligned}
 \mathsf d_t
 &:=\chi^2(Q_t\Vert Q_{t-1})\\
 &=\mathbb E_{Q_{t-1}}
   \left[\left(\frac{R}{A_{t-1}}-1\right)^2\right]\\
 &=\frac{\operatorname{Var}_{Q_{t-1}}(R)}{A_{t-1}^2}.
\end{aligned}                                          \tag{2}
\]

Size bias gives

\[
\boxed{
 1+\mathsf d_t
 =\frac{A_t}{A_{t-1}}
 =\frac{Z_{t+1}Z_{t-1}}{Z_t^2}
 =e^{\eta_t}.
}                                                       \tag{3}
\]

Hence raw moment log-curvature is exactly the logarithm of an adjacent
Pearson divergence:

\[
 \eta_t=\log(1+\mathsf d_t).                           \tag{4}
\]

## 2. The Gaussian carrier is the extremal likelihood experiment

For the Gaussian/gamma carrier with shape \(t-1/2\),

\[
\boxed{
 \mathsf d_t^{\mathrm G}=\frac2{2t-1}.
}                                                       \tag{5}
\]

Therefore the Gaussian-relative curvature slack is

\[
\boxed{
 \varepsilon_t
 =\log\frac{1+\mathsf d_t^{\mathrm G}}
              {1+\mathsf d_t}.
}                                                       \tag{6}
\]

The degree-two theta theorem is precisely

\[
 \mathsf d_t<\mathsf d_t^{\mathrm G}.                 \tag{7}
\]

Thus source stiffening contracts the adjacent size-bias likelihood
experiment relative to the Gaussian carrier.

This statement is invariant: both laws, their Radon--Nikodym derivative, and
the reference gamma experiment are fixed by the moment source.  No chamber,
deformation path, or fitted norm enters.

## 3. Additive divergence deficit

Define

\[
\boxed{
 \Delta_t
 :=\mathsf d_t^{\mathrm G}-\mathsf d_t>0.
}                                                       \tag{8}
\]

The Stein identity gives

\[
\boxed{
 C_t=(2t-1)\Delta_t.
}                                                       \tag{9}
\]

Moreover,

\[
 1-e^{-\varepsilon_t}
 =\frac{\Delta_t}{1+\mathsf d_t^{\mathrm G}}
 =\frac{(2t-1)\Delta_t}{2t+1}.                        \tag{10}
\]

The inverse reserve therefore becomes

\[
\boxed{
 L_t
 =\sqrt{\frac{1+\mathsf d_t^{\mathrm G}}{\Delta_t}}
 =\sqrt{\frac{2t+1}{(2t-1)\Delta_t}}.
}                                                       \tag{11}
\]

## 4. Cubic hyperbolicity as a contraction-speed law

The exact cubic gate is now

\[
\boxed{
 \left|
 \sqrt{\frac{1+\mathsf d_{t+1}^{\mathrm G}}{\Delta_{t+1}}}
 -
 \sqrt{\frac{1+\mathsf d_t^{\mathrm G}}{\Delta_t}}
 \right|\le1.
}                                                       \tag{12}
\]

At \(t=3\),

\[
\boxed{
 \left|
 \sqrt{\frac{9}{7\Delta_4}}
 -
 \sqrt{\frac{7}{5\Delta_3}}
 \right|\le1.
}                                                       \tag{13}
\]

This is the direct Deutschian explanation target:

> Theta stiffening contracts every adjacent size-bias experiment below its
> Gaussian Pearson divergence; cubic coherence says the inverse square-root
> contraction length cannot change by more than one adjacent tilt.

Degree two controls the sign of the information loss.  Degree three controls
its speed.

## 5. Positive two-copy representation of information loss

The divergence deficit is not an abstract subtraction.  Since

\[
 C_t=\operatorname{Cov}_{Q_t}(R,W),
 \qquad W=\frac{V'(u)}u,
\]

one has

\[
\boxed{
 \Delta_t
 =\frac1{2(2t-1)}
 \mathbb E_{Q_t\otimes Q_t}
 \left[(R_1-R_2)(W_1-W_2)\right].
}                                                       \tag{14}
\]

The proved monotonicity of \(W\) makes the integrand positive.  Thus the
amount by which theta contracts the gamma likelihood experiment is exactly a
source separation energy.

The cubic problem is consequently not to invent a stronger divergence.  It
is to compare two consecutive positive separation energies after the known
carrier factors are removed.

## 6. Why ordinary data processing does not close the theorem

Pearson divergence contracts under a common Markov kernel.  But the pair

\[
 Q_{t-1}\to Q_t,
 \qquad
 Q_t\to Q_{t+1}
\]

consists of two different size-bias experiments.  No common stochastic map
between them has been derived.  Applying the data-processing inequality by
analogy would therefore be untyped.

The missing object would be a source-derived commutative square

\[
\begin{array}{ccc}
 Q_{t-1}&\longrightarrow&Q_t\\
 \downarrow K_t&&\downarrow K_t\\
 Q_t&\longrightarrow&Q_{t+1}
\end{array}                                             \tag{15}
\]

whose vertical kernel transports the likelihood ratio coherently and whose
strong data-processing coefficient reproduces the exact unit budget in
(12).  Ordinary size bias supplies the horizontal arrows but not such a
vertical Markov kernel.

## 7. Sharp next theorem and falsifier

The invariant theorem target is a comparison of the two separation deficits:

\[
\boxed{
 \Delta_{t+1}
 \in
 \left[
  \frac{1+\mathsf d_{t+1}^{\mathrm G}}
       {\left(sqrt{(1+\mathsf d_t^{\mathrm G})/\Delta_t}+1\right)^2},
  \frac{1+\mathsf d_{t+1}^{\mathrm G}}
       {\left(sqrt{(1+\mathsf d_t^{\mathrm G})/\Delta_t}-1\right)^2}
 \right].
}                                                       \tag{16}
\]

This is exactly cubic hyperbolicity, not a surrogate.

The constructive route is to derive a coupling or correspondence between the
two positive separation laws representing \(\Delta_t\) and
\(\Delta_{t+1}\).  Its normalization must arise from size bias and must retain
the likelihood ratios.  The sharp falsifier is failure of either endpoint in
(16); failure of a proposed Markov square alone falsifies only that
explanation.

## 8. The gamma carrier has an exact add-one square

For the Gaussian source, the radial laws are gamma distributions.  If

\[
 X_a\sim\operatorname{Gamma}(a,\lambda),
 \qquad
 E\sim\operatorname{Gamma}(1,\lambda)
\]

are independent, then

\[
\boxed{
 X_a+E\sim\operatorname{Gamma}(a+1,\lambda).
}                                                       \tag{17}
\]

Thus one fixed additive Markov kernel

\[
 K(x,\cdot)=\operatorname{Law}(x+E)                    \tag{18}
\]

transports every adjacent gamma tilt.  The universal carrier really does
possess the commutative add-one square suggested in (15).

This explains the unit step in the inverse-reserve geometry: adjacent gamma
shape is generated by one identical independent increment at every level.

## 9. Why an exact theta add-one kernel is too strong

Suppose a fixed additive increment \(Y\), independent of the current radial
state, transported every theta tilt:

\[
 R_t+Y\overset d=R_{t+1}.                              \tag{19}
\]

Taking expectations would give

\[
 A_{t+1}-A_t=\mathbb EY
\]

independently of \(t\), hence

\[
 \Theta_t=A_{t+1}-2A_t+A_{t-1}=0.                     \tag{20}
\]

The heat-curvature audit showed that nonzero \(\Theta_t\) is exactly the
departure from the gamma-neutral transport profile.  Therefore an exact
source-independent additive square would erase the non-Gaussian transport
data rather than explain its controlled deficit.

The correct theta object must be a defect-bearing correspondence:

\[
\boxed{
 \text{gamma add-one carrier}
 +\text{source-derived coherent defect}
 \longrightarrow
 \text{theta adjacent size bias}.
}                                                       \tag{21}
\]

Its defect cannot be arbitrary.  Its Pearson energy is \(\Delta_t\), and its
change under one adjacent step must satisfy (16).  This is structurally
parallel to the prime-two result, but with an important difference: the
repair is not a freely added rank-one term.  It is the controlled failure of
the theta radial family to be an exact gamma convolution semigroup.

## 10. Revised correspondence target

Seek a positive coupling \(\Pi_t\) on

\[
 (R_{t-1},R_t,R_{t+1},E)
\]

with the correct three theta marginals and gamma increment marginal, such
that

\[
 R_t=R_{t-1}+E+\mathcal E_t,
 \qquad
 R_{t+1}=R_t+E'+\mathcal E_{t+1},                      \tag{22}
\]

in a typed transport sense.  The variables \(\mathcal E_t\) are residual
coupling coordinates, not assumed independent or pointwise additive errors.

The desired theorem is that their adjacent Pearson energies obey the exact
inverse-deficit unit bound.  The cheapest falsifier is more basic: if no
positive coupling can realize the theta marginals while retaining the gamma
increment as a common labelled component, then the add-one explanation fails
and the separation-energy route must remain purely two-copy.

This target must not be satisfied by an arbitrary quantile coupling.  The
common increment and residuals must be derived from theta labels or modular
scale transport; otherwise the construction has no explanatory authority.

## 11. Radial Stein kernel realizes the defect

Under \(Q_{t-1}\), the radial variable has density

\[
 p_t(r)
 =\frac1{\mathcal Z_t}r^{k_t-1}e^{-\varphi(r)},
 \qquad
 k_t=t-\frac12,
 \qquad
 \varphi(r)=V(\sqrt r).                                \tag{23}
\]

Let \(A=A_{t-1}=\mathbb E_{p_t}R\).  Its canonical Stein kernel is

\[
\boxed{
 \tau_t(r)
 =\frac1{p_t(r)}\int_r^\infty(x-A)p_t(x)\,dx.
}                                                       \tag{24}
\]

It satisfies

\[
 \operatorname{Cov}_{p_t}(R,f(R))
 =\mathbb E_{p_t}[\tau_t(R)f'(R)]                     \tag{25}
\]

for the admitted test functions, and in particular

\[
 \mathbb E_{p_t}\tau_t(R)=\operatorname{Var}_{p_t}(R).
                                                               \tag{26}
\]

For the gamma carrier with shape \(k_t\) and the same mean \(A\),

\[
 \tau_t^{\mathrm G}(r)=\frac{A}{k_t}r,
 \qquad
 \mathbb E\tau_t^{\mathrm G}=\frac{A^2}{k_t}.         \tag{27}
\]

Define the normalized Stein-defect field

\[
\boxed{
 \mathscr D_t(r)
 =\frac{r}{k_tA}-\frac{\tau_t(r)}{A^2}.
}                                                       \tag{28}
\]

Its mean is exactly the Pearson contraction deficit:

\[
\boxed{
 \mathbb E_{Q_{t-1}}\mathscr D_t(R)
 =\frac1{k_t}-\frac{\operatorname{Var}(R)}{A^2}
 =\Delta_t.
}                                                       \tag{29}
\]

Thus the previously abstract coherent defect has a canonical source
representative.  It is the failure of the theta Stein kernel to equal the
linear gamma kernel.

Pointwise positivity of \(\mathscr D_t\) is not asserted; the degree-two
theorem proves positivity of its mean.  Promoting mean contraction to a
pointwise kernel order would be a stronger claim requiring separate proof.

## 12. Cubic theorem as adjacent Stein-defect coherence

Equations (12) and (29) give

\[
\boxed{
 \left|
 \sqrt{
  \frac{1+1/k_{t+1}}
       {\mathbb E_{Q_t}\mathscr D_{t+1}}}
 -
 \sqrt{
  \frac{1+1/k_t}
       {\mathbb E_{Q_{t-1}}\mathscr D_t}}
 \right|\le1.
}                                                       \tag{30}
\]

The missing correspondence is therefore not an arbitrary coupling of four
radial variables.  It is a transport law relating the Stein-defect field
under one size bias to the next Stein-defect field:

\[
 (Q_{t-1},\mathscr D_t)
 \longrightarrow
 (Q_t,\mathscr D_{t+1}).                               \tag{31}
\]

The source determines both fields through (24).  A proof may now attack their
means while retaining pointwise correlation information, rather than
inventing residual increments.

The sharp next calculation is the exact size-bias evolution of \(\tau_t\).
If it has the form

\[
 \tau_{t+1}
 =\mathcal T_t(\tau_t)+\text{positive labelled correction},  \tag{32}
\]

with \(\mathcal T_t\) fixed by the gamma carrier, then the required
correspondence exists.  If the evolution introduces an indefinite new field
not determined by \(\tau_t\), the Stein route merely shifts the hierarchy and
must be rejected like heat differentiation.

## 13. Exact size-bias evolution raises the tail order

Let \(p=p_t\), \(A=A_{t-1}\), and

\[
 A'=A_t=\frac{\mathbb E_pR^2}{A}.
\]

The size-biased density is

\[
 p^{\mathrm s}(r)=\frac rA p(r).
\]

Applying the definition (24) to this law gives the exact evolution

\[
\boxed{
 \tau_{t+1}(r)
 =\frac1{r p(r)}
  \int_r^\infty x(x-A')p(x)\,dx.
}                                                       \tag{33}
\]

The numerator is a second tail-moment primitive.  It is not determined
locally by \(\tau_t(r)\), whose numerator contains only

\[
 \int_r^\infty(x-A)p(x)\,dx.                           \tag{34}
\]

An integration-by-parts expansion makes the new datum explicit.  With

\[
 S(r)=\int_r^\infty p(x)\,dx,
\]

one obtains

\[
\boxed{
\begin{aligned}
 r p(r)\tau_{t+1}(r)
 ={}&[r+A-A']\tau_t(r)p(r)\\
 &+\int_r^\infty\tau_t(x)p(x)\,dx
 +A(A-A')S(r).
\end{aligned}
}                                                       \tag{35}
\]

Although the complete left side is positive, the three terms on the right
do not have a fixed separate sign because \(A'<A\) is false under nontrivial
size bias.  Thus no universal decomposition

\[
 \tau_{t+1}=\mathcal T_t(\tau_t)+\text{positive repair}
\]

follows from size bias alone.

This is the Stein hierarchy-shift obstruction:

\[
\boxed{
 \text{first tail kernel under size bias}
 \longrightarrow
 \text{second tail kernel}.
}                                                       \tag{36}
\]

The route remains viable only if the completed theta source supplies a
differential or label recursion reducing the second tail primitive in (33)
back to the first kernel plus controlled boundary data.  Generic probability
theory does not provide that closure.

## 14. Surviving direct target

The information-geometric retyping remains invariant and useful even though
the proposed Stein closure fails generically:

\[
 \Delta_t
 =\chi^2_{\mathrm{gamma},t}
  -\chi^2(Q_t\Vert Q_{t-1}).                           \tag{37}
\]

But the most economical proof target returns to the two-copy separation
energy (14), whose adjacent size-bias evolution is already exact and does not
pretend that a first-order Stein kernel closes.  Theta labels must orient that
two-copy transport directly.
