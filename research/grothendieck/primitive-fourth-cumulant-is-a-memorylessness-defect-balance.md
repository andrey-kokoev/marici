# The primitive fourth cumulant is a memorylessness-defect balance

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: exact score elimination and sharpened theorem target

## Setup

Fix a wall position $a$ and residual coordinate $R=v-a>0$.  For
$q>0$, let $Q_q$ have density proportional to

\[
R^qF(a+R)\,dR.
\]

Put

\[
H=\log R,
\qquad
\sigma=\frac{F'}F,
\qquad
m=\mathbb E_{Q_q}(R^{-1}).
\]

Let $Q_q^-$ be the inverse-residual bias of $Q_q$:

\[
dQ_q^-=\frac{R^{-1}}m\,dQ_q.
\]

This is not a new measure family.  It is exactly the adjacent exponent law
$Q_{q-1}$.

Write

\[
d=\mathbb E_{Q_q}H-\mathbb E_{Q_q^-}H,
\]

and denote the log-residual variance and third central moment by
$v,\mu_3$, with $v^-,\mu_3^-$ for the inverse bias.

## Exact score elimination

For smooth test functions $g$, integration by parts gives

\[
\mathbb E_{Q_q}(\sigma g)
=-\mathbb E_{Q_q}
\left(g'+\frac qR g\right).
\]

There is no wall term because $q>0$.  Applying this identity to the first
three centered powers of $H$ eliminates the carrier score from the mixed
fourth cumulant.  Direct simplification yields

\[
\frac{\operatorname{cum}_{Q_q}(\sigma,H,H,H)}m
=q(\mu_3-\mu_3^-)
+3(qd-1)(v^--v)
+d^2(qd-3).
\]

This identity is exact for every admissible carrier, wall, and $q>0$.

## Memoryless reference

For an exponential residual law,

\[
d=\frac1q,
\qquad
v^--v=\frac1{q^2},
\qquad
\mu_3-\mu_3^-=\frac2{q^3}.
\]

The three terms then cancel exactly.  Thus the desired strict negative sign
is not generic positivity.  It measures departure from residual
memorylessness.

For the primitive theta carrier in the required window, diagnostics show

\[
qd<1,
\qquad
v^->v,
\qquad
\mu_3>\mu_3^-.
\]

The skew-drift term is positive, while the other two terms are negative.
The exact remaining inequality is

\[
q(\mu_3-\mu_3^-)
<3(1-qd)(v^--v)+d^2(3-qd).
\]

This is the source-native repair law: loss of memorylessness creates two
negative variance-and-mean repair channels, and they must dominate the
positive adjacent skew drift.

## What is universal and what is not

Log-concavity of the residual density implies the normalized-moment
comparison $qd\le1$, with equality for the exponential reference.  That
orients the coefficient of $v^--v$, but does not by itself prove either
variance transport or domination of skew drift.  The hostile analytic
sources from the cubic programme show that no generic log-concavity shortcut
can supply the final inequality.

The theorem target is now a comparison between two adjacent residual-power
views of one carrier.  It has no theta-label sum, no arbitrary Gram feature,
and no scalar determinant imported from the desired answer.

## Aging-spectrum opportunity and its sharp limitation

A stronger candidate is complete monotonicity of the log-residual variance

\[
K''(q)=\operatorname{Var}_{Q_q}(H).
\]

If

\[
K''(q)=\int_0^\infty e^{-qt}\,d\rho(t),
\qquad
\rho\ge0,
\]

then the three adjacent statistics are moments of one positive aging
spectrum.  With

\[
d\nu_q(t)=e^{-qt}(e^t-1)\,d\rho(t),
\]

one has

\[
d=\int\frac1t\,d\nu_q,
\qquad
v^--v=\int d\nu_q,
\qquad
\mu_3-\mu_3^-=\int t\,d\nu_q.
\]

For the exponential reference, $d\nu_q=t e^{-qt}\,dt$.  The theorem then
becomes a comparison of the negative-first, zeroth, and first moments of the
actual aging spectrum against this reference geometry.

Crucially, a positive spectrum alone does not prove the repair law.  At
$q=4$, take

\[
\nu=\frac1{320}\delta_{5/2}.
\]

Then the dimensionless moments

\[
A=qd,
\qquad
B=q^2(v^--v),
\qquad
C=q^3(\mu_3-\mu_3^-)
\]

are

\[
A=\frac1{200},
\qquad
B=\frac1{20},
\qquad
C=\frac12.
\]

But the desired inequality would require

\[
C<3(1-A)B+A^2(3-A)<0.15,
\]

which fails.  Therefore complete monotonicity would provide a faithful
positive spectral coordinate, but not the RH-bearing orientation.  The
missing theta property must constrain where the aging-spectrum mass lies or
how its tail compares with the exponential spectrum.

The normalization reveals the exact reduced target.  Set

\[
A=qd,
\qquad
B=q^2(v^--v),
\qquad
C=q^3(\mu_3-\mu_3^-).
\]

Then the source law is precisely the open three-moment cone

\[
C<3(1-A)B+A^2(3-A).
\]

The exponential spectrum lies on its boundary at $(A,B,C)=(1,1,2)$.
The hostile atom lies far outside it: its right-hand side is exactly
$0.149324875$, while $C=1/2$. Consequently, proving complete monotonicity
and reconstructing the entire positive measure would still be excessive.
The minimal surviving theorem is that the theta aging spectrum maps into
this three-moment cone. Any proposed source explanation must say why that
cone, rather than merely the positive-measure cone, is invariant under the
moving-wall transport.

## Memoryless centering collapses the cone

There is a stronger algebraic reduction.  Center the three normalized
coordinates at the exponential boundary:

\[
x=A-1,
\qquad
y=B-1,
\qquad
z=C-2.
\]

Direct expansion gives the exact identity

\[
3(1-A)B+A^2(3-A)-C
=-\bigl(z+3xy+x^3\bigr).
\]

The expression on the right is the third complete Bell polynomial in the
formal cumulant triple $(x,y,z)$.  Equivalently, it is the formal third raw
moment associated with those centered defect cumulants.  Thus the live
inequality is not an arbitrary curved boundary in three-moment space.  It is
exactly

\[
z+3xy+x^3<0.
\]

This identifies a sharper constructor target: derive one signed defect
packet from adjacent residual-power transport whose first three cumulants
are $(x,y,z)$.  The entire pointwise order-four theorem would then say that
this packet has negative third raw moment.  The existence and source typing
of that packet are not yet proved; treating the Bell-polynomial identity as
an actual probability representation would be premature.

The one-atom hostile spectrum now has an especially clear role.  Positivity
of the aging spectrum does not orient the skewness of the centered defect
packet.  Theta must supply a separate ordering or coupling that does.

## Exact reciprocal Mellin defect

The formal packet has a canonical scalar generating function.  Let

\[
K(q)=\log M_q
\]

and define, near $t=0$,

\[
\Psi_q(t)
=-K(q-qt)+K(q-1-qt)+K(q)-K(q-1)+\log(1-t).
\]

Then

\[
\Psi_q(0)=0,
\qquad
\Psi_q'(0)=x,
\qquad
\Psi_q''(0)=y,
\qquad
\Psi_q'''(0)=z.
\]

Exponentiating gives the normalized reciprocal adjacent Mellin ratio

\[
\mathcal R_q(t)
=(1-t)
\frac{M_q}{M_{q-1}}
\frac{M_{q-1-qt}}{M_{q-qt}}.
\]

Consequently,

\[
\mathcal R_q'''(0)=z+3xy+x^3.
\]

The pointwise cubic gate is therefore exactly

\[
\mathcal R_q'''(0)<0.
\]

For every exponential residual carrier, the adjacent Mellin ratio is
$M_q/M_{q-1}=q/\lambda$, so $\mathcal R_q(t)\equiv1$.  The function
$\mathcal R_q$ is thus a pure memorylessness-defect readout, with no
exponential background left to cancel numerically.

This is an exact scalar construction, but its positivity type is still open.
In particular, it has not been shown that $\mathcal R_q$ is a moment-
generating function of a positive measure.  The next sharp question is
whether the primitive theta residual forces a source-derived signed order on
this reciprocal Mellin ratio strong enough to give
$\mathcal R_q'''(0)<0$ throughout the required wall and exponent window.

## Collapse to one adjacent-ratio shape theorem

The reciprocal Mellin defect has no irreducible two-variable content. Define
the normalized adjacent moment ratio and its reciprocal by

\[
r(q)=\frac{M_q}{qM_{q-1}},
\qquad
h(q)=\frac1{r(q)}
=q\frac{M_{q-1}}{M_q}
=q\,\mathbb E_{Q_q}(R^{-1}).
\]

Using

\[
\frac{M_{q-qt}}{M_{q-1-qt}}
=q(1-t)r\bigl(q(1-t)\bigr),
\]

the exact defect generator becomes

\[
\mathcal R_q(t)
=\frac{r(q)}{r(q(1-t))}
=\frac{h(q(1-t))}{h(q)}.
\]

It follows immediately that

\[
\mathcal R_q'''(0)
=-\frac{q^3h'''(q)}{h(q)}.
\]

Since $h(q)>0$, the entire pointwise order-four theorem is equivalent to the
one-variable shape condition

\[
h'''(q)>0,
\qquad
h(q)=q\,\mathbb E_{Q_q}(R^{-1}).
\]

Thus the previous cumulant balance, three-moment cone, Bell polynomial, and
reciprocal Mellin curvature are four coordinate presentations of one fact:
the normalized inverse-residual response is strictly third-order convex in
the continuous residual-power exponent. The exponential carrier has
$h(q)\equiv\lambda$, so it is again the neutral boundary case.

This is the smallest current theorem target. Complete monotonicity of an
auxiliary aging spectrum is stronger than needed. What remains is to derive
$h'''(q)>0$ directly from the primitive theta residual potential, uniformly
in the wall parameter and for the required exponent interval.

## Restoring-force interpretation

The adjacent ratio is itself a source expectation. Integration by parts,
with the wall term killed by $q>0$, gives

\[
qM_{q-1}
=-\int_0^\infty R^qF'(a+R)\,dR.
\]

If $F=e^{-V}$, then

\[
h(q)
=-\mathbb E_{Q_q}\!\left(\frac{F'}F\right)
=\mathbb E_{Q_q}\bigl(V'(a+R)\bigr).
\]

For the primitive moving-wall carrier

\[
F(v)=e^{5v/2}(2e^{2v}-3)e^{-e^{2v}},
\]

put $c=e^{2a}$ and $x=ce^{2R}$. Its restoring force is

\[
V'(a+R)
=2x-\frac92-\frac6{2x-3},
\]

and therefore

\[
h(q)
=2c\,\mathbb E_{Q_q}(e^{2R})
-\frac92
-6\,\mathbb E_{Q_q}\!\left(\frac1{2ce^{2R}-3}\right).
\]

Hence the missing theorem has a direct mechanical meaning: the expected
restoring force of the primitive wall has positive third response under
continuous logarithmic-distance tilting. Differentiating an expectation
under this tilt recovers

\[
h'''(q)
=\operatorname{cum}_{Q_q}\bigl(V',H,H,H\bigr)
=-\operatorname{cum}_{Q_q}(\sigma,H,H,H).
\]

This last equality closes the equivalence loop without adding a new proof.
Its value is explanatory and tactical: it exposes the exact source force
whose third tilt response must be controlled, instead of asking for a
generic fourth-cumulant inequality.

Define the exponential and wall-pole responses

\[
T_{\exp}(q)=\partial_q^3\mathbb E_{Q_q}(e^{2R}),
\qquad
T_{\rm pole}(q)
=\partial_q^3\mathbb E_{Q_q}\!\left(\frac1{2ce^{2R}-3}\right).
\]

Then

\[
h'''(q)
=2cT_{\exp}(q)-6T_{\rm pole}(q),
\]

so the theorem is exactly

\[
cT_{\exp}(q)>3T_{\rm pole}(q).
\]

The two terms have different provenance. The exponential term is the
ordinary confining force; the pole term records the moving wall's primitive
zero at $c=3/2$. Neither third tilt response has a generic sign. This is now
the smallest source-native hostile test: determine whether the primitive
carrier enforces the weighted response dominance above, and whether either
channel admits a separately oriented comparison. The discarded
quartic-exponential two-mode calculation belonged to a different carrier
and supplies no evidence for this theorem.

## Correct-channel reconnaissance

A dependency-free midpoint sweep was run directly in the exact source
coordinate

\[
x=e^{2v}=c+y,
\qquad
R=\frac12\log\left(1+\frac yc\right).
\]

It covered a $25\times25$ logarithmic-linear grid:

\[
1.500001\le c\le200,
\qquad
4\le q\le10.
\]

All $625$ sampled pairs showed the stronger separated orientation

\[
T_{\exp}(q)>0,
\qquad
T_{\rm pole}(q)<0.
\]

Thus both source channels contribute positively:

\[
h'''(q)
=2cT_{\exp}(q)+6|T_{\rm pole}(q)|>0.
\]

The smallest sampled values occurred at $c=200$, $q=10$:

\[
T_{\exp}\approx3.68434\times10^{-7},
\qquad
T_{\rm pole}\approx-3.45837\times10^{-9},
\]

with

\[
cT_{\exp}-3T_{\rm pole}
\approx7.36972\times10^{-5}.
\]

This is reconnaissance, not an interval certificate. Its conceptual value is
that it removes the apparent cancellation problem. The primitive zero at
the wall does not create an adverse correction: its pole response has the
opposite sign and repairs the exponential response.

The sharpened theorem target is therefore channelwise:

\[
\partial_q^3\mathbb E_{Q_q}(e^{2R})>0,
\qquad
\partial_q^3\mathbb E_{Q_q}\!\left(\frac1{2ce^{2R}-3}\right)<0.
\]

The observables are respectively increasing and decreasing in $R$, so the
signs agree with their order. Ordinary monotone-likelihood-ratio transport
proves only the first derivative, however. The missing explanation is an
order-three response-preservation theorem for these two source observables,
not generic monotonicity.

## The hidden variance ellipse

The third response has an exact two-copy symmetrization. For any observable
$g(H)$, put

\[
Z=H-\mathbb E H,
\qquad
v=\mathbb E(Z^2),
\qquad
P_3(H)=Z^3-3vZ.
\]

Then

\[
\partial_q^3\mathbb E_{Q_q}(g)
=\operatorname{cum}_{Q_q}(g,H,H,H)
=\operatorname{Cov}_{Q_q}(g,P_3).
\]

For two independent copies, covariance symmetrization gives

\[
\partial_q^3\mathbb E(g)
=\frac12\mathbb E
\left[
(g_1-g_2)(H_1-H_2)
\left(Z_1^2+Z_1Z_2+Z_2^2-3v\right)
\right].
\]

Introduce pair midpoint and half-separation coordinates

\[
m=\frac{Z_1+Z_2}{2},
\qquad
d=\frac{Z_1-Z_2}{2}.
\]

The final factor becomes

\[
Z_1^2+Z_1Z_2+Z_2^2-3v
=3m^2+d^2-3v.
\]

Thus the sign transition is the canonical variance ellipse

\[
3m^2+d^2=3v.
\]

For an increasing observable, define its nonnegative secant weight

\[
s_g(H_1,H_2)=\frac{g_1-g_2}{H_1-H_2}.
\]

Then

\[
\partial_q^3\mathbb E(g)
=2\mathbb E
\left[
s_gd^2\left(3m^2+d^2-3v\right)
\right].
\]

For a decreasing observable, the same formula holds with the opposite sign
after defining $s_g=-(g_1-g_2)/(H_1-H_2)\ge0$.

Consequently, both primitive channel signs are instances of one geometric
statement: under the channel's source-derived secant weight, contribution
outside the variance ellipse dominates contribution inside it. Ordinary
monotone-likelihood-ratio ordering controls the secant sign but not this
ellipse balance. A two-point exponential family already shows that third
response need not inherit the first-response sign.

The next transport target is now concrete. Construct a source-derived
pairing from the interior of $3m^2+d^2<3v$ to its exterior that increases
the weighted radial quantity for both authorized secant weights. Failure of
such a common pairing would explain why the two channels need separate
arguments even though their numerical orientations agree.

The two primitive observables illuminate complementary exterior lobes. As
functions of $H$,

\[
g_{\exp}(H)=e^{2e^H},
\qquad
-g_{\rm pole}'(H)
=\frac{4ce^He^{2e^H}}{(2ce^{2e^H}-3)^2}.
\]

The exponential secant weight grows toward the upper residual tail. The
pole secant weight concentrates toward the lower wall, especially as
$c\downarrow3/2$. Thus the two terms in the restoring force are naturally
typed as complementary observation ports: the upper confining port and the
lower primitive-wall port.

Each port weights an exterior lobe of the same variance ellipse. This gives
a source-specific Explanation candidate for the separated signs: the
primitive restoring force retains both tails that a central scalar moment
would merge. The rigorous burden is to prove exterior dominance for each
secant weight; complementarity alone does not establish the inequality.

The smallest generic falsifier is a two-point family. If $H\in\{0,1\}$ and
$g(H)=H$, exponential tilting gives a logistic mean $p(q)$. At $p=1/2$,

\[
\frac{d^3p}{dq^3}=-\frac18<0
\]

despite $g$ being increasing. This proves that the primitive ellipse theorem
must use the carrier's tail geometry, not monotonicity alone.

## Canonical ellipse-inversion attack

The sign geometry supplies a canonical candidate transport. Set

\[
u=\sqrt3\,m,
\qquad
w=d,
\qquad
\rho^2=u^2+w^2,
\qquad
R_0^2=3v.
\]

The negative region is the disk $\rho<R_0$. Kelvin inversion through its
boundary,

\[
\mathcal I(u,w)
=\frac{R_0^2}{\rho^2}(u,w),
\]

maps it bijectively to the exterior. It has Jacobian magnitude

\[
|\det D\mathcal I|
=\frac{R_0^4}{\rho^4},
\]

and reverses the sign polynomial by

\[
\rho(\mathcal I)^2-R_0^2
=-\frac{R_0^2}{\rho^2}(\rho^2-R_0^2).
\]

Write the centered-log pair density as

\[
p_q(H_1)p_q(H_2),
\qquad
H_{1,2}=\mathbb EH+\frac{u}{\sqrt3}\pm w.
\]

For either channel, let $s_g\ge0$ be its oriented secant weight. Pulling the
exterior contribution back through $\mathcal I$ shows that a sufficient
pointwise transport certificate is

\[
\frac{
p_q(H_1')p_q(H_2')s_g(H_1',H_2')
}{
p_q(H_1)p_q(H_2)s_g(H_1,H_2)
}
\ge
\left(\frac{\rho}{R_0}\right)^{10},
\]

where $(H_1',H_2')$ is the inverted pair. The exponent ten comes from the
two powers of separation, one sign-polynomial factor, and the
two-dimensional inversion Jacobian.

If this holds throughout the interior disk, inversion pairs every negative
contribution with a dominating positive one; all unpaired exterior
contribution is already positive. The inequality is only sufficient, not
known true. Its value is that it is explicit, source-derived, and locally
falsifiable. The first interior point and channel violating the ratio is the
smallest hostile witness against this canonical pairing, without falsifying
the channel sign itself.

The hostile test rejects this pointwise inversion strongly. Near the disk
center, inversion sends ordinary pairs into double-exponentially thin source
tails. Sampled log margins become overwhelmingly negative for both
channels. The failure is geometric rather than a precision issue.

The milder radial reflection

\[
\rho'=2R_0-\rho
\]

was then tested. It sends the interior to the adjacent annulus instead of
the remote tail. It too fails broadly: on representative source points,
hundreds of sampled angle-radius cells have negative transported margins for
each channel.

Therefore the variance ellipse is a valid exact sign decomposition, but no
pointwise radial transport currently explains its orientation. Any surviving
pairing must retain angular information, aggregate canonical angular blocks,
or use different transports for the upper exponential and lower pole ports.
This is the first real obstacle after the adjacent-ratio collapse.

## Angular aggregation and port-conditioned radius

The angular information can be retained without choosing a pointwise
transport. For either oriented channel, define the positive pair measure

\[
d\Pi_g
=\frac{
s_g(H_1,H_2)d^2p_q(H_1)p_q(H_2)\,dH_1dH_2
}{
\mathbb E(s_gd^2)
}.
\]

Then the exact secant formula becomes

\[
|\partial_q^3\mathbb E(g)|
=2\mathbb E(s_gd^2)
\left(
\mathbb E_{\Pi_g}(\rho^2)-3v
\right),
\]

with the sign of the original monotone channel restored separately.
Consequently, both desired channel orientations are equivalent to the same
relationship-energy statement:

\[
\mathbb E_{\Pi_g}(\rho^2)>3v.
\]

Each authorized port must select pairs whose mean squared ellipse-radius
lies outside the source variance circle. This is the invariant shell
formulation that the failed radial maps were trying to prove pointwise.

There is a useful unported baseline. Let $\Pi_0$ be the pair law weighted
only by $d^2$. If $\mu_4=\mathbb E(Z^4)$, independence and symmetry give

\[
\mathbb E(d^2)=\frac v2,
\qquad
\mathbb E(d^2\rho^2)=\frac{\mu_4}{2},
\]

and hence

\[
\mathbb E_{\Pi_0}(\rho^2)=\frac{\mu_4}{v}.
\]

This yields a two-gate sufficient theorem:

\[
\mu_4>3v^2
\]

and

\[
\operatorname{Cov}_{\Pi_0}(s_g,\rho^2)\ge0
\]

for each primitive port. The first condition is positive excess kurtosis of
the log-residual source. The second says that the port secant does not move
separation-biased pair mass inward. Together they imply

\[
\mathbb E_{\Pi_g}(\rho^2)
\ge\mathbb E_{\Pi_0}(\rho^2)
>3v.
\]

This split is stronger than necessary but materially more local than the
original fourth cumulant: one source-tail theorem plus one port-radius
association theorem. Either covariance becoming negative is an immediate
falsifier of this explanation while leaving the exact channel sign open.

That falsifier fires. A direct two-copy quadrature at representative source
points finds that the exponential-port covariance is negative throughout
the tested set. The pole covariance is positive near $c=3/2$ but becomes
negative at larger $c$. Thus neither port generally pushes the
separation-biased pair law outward.

The exact decomposition nevertheless reveals why the channel signs survive:

\[
\mathbb E_{\Pi_g}(\rho^2)-3v
=
\left(\frac{\mu_4}{v}-3v\right)
+
\frac{
\operatorname{Cov}_{\Pi_0}(s_g,\rho^2)
}{
\mathbb E_{\Pi_0}(s_g)
}.
\]

The first term is the source's positive excess-kurtosis reserve. The second
is the port's radial displacement, which may be negative. The correct
theorem is therefore the budget inequality

\[
\frac{\mu_4}{v}-3v
>
-
\frac{
\operatorname{Cov}_{\Pi_0}(s_g,\rho^2)
}{
\mathbb E_{\Pi_0}(s_g)
}.
\]

On the representative grid, the port-conditioned mean radius remains above
$3v$ even when the covariance is negative. At $c=200$, the margins are
small: for $q=4$, the exponential-port mean exceeds $3v$ by about
$8.99\times10^{-5}$; for $q=10$, by about $7.69\times10^{-5}$. This is
consistent with the already derived far-wall near-memoryless asymptotics.

The Explanation has therefore changed again. The ports do not create
super-Gaussian separation. The unported source already carries it, and the
ports consume only part of that reserve. The next theorem must couple the
source kurtosis and port localization costs; proving them independently
with favorable signs is impossible.

## Bernstein-response conjecture

The adjacent-ratio reduction suggests that the coupled budget may be one
shadow of a stronger source law. The candidate is that

\[
h(q)=q\frac{M_{q-1}}{M_q}
\]

is a Bernstein function of $q$ for every physical wall:

\[
(-1)^{n-1}h^{(n)}(q)\ge0,
\qquad
n\ge1.
\]

The first four required signs were tested on the same $25\times25$ grid.
All $625$ pairs satisfy

\[
h'>0,
\qquad
h''<0,
\qquad
h'''>0,
\qquad
h^{(4)}<0.
\]

The smallest sampled signed reserves were

\[
\min h'\approx0.8300003,
\qquad
\min(-h'')\approx8.3730\times10^{-3},
\]

\[
\min h'''\approx1.4739\times10^{-4},
\qquad
\min(-h^{(4)})\approx4.3572\times10^{-6}.
\]

The final three minima occur at $c=200$, $q=10$. Higher double-precision
jets become cancellation-dominated in that far-wall regime and are not
evidence.

If the conjecture holds, the cubic gate is immediate and the source admits
a Lévy--Khintchine representation

\[
h(q)=\alpha+\beta q
+\int_0^\infty(1-e^{-qt})\,d\eta(t),
\qquad
\eta\ge0.
\]

This is now the strongest hard-to-vary Explanation candidate: primitive
moving-wall transport generates a positive response spectrum, and every
alternating derivative is one resolution of the same spectrum. It is also
sharply Popperian. A single $(c,q,n)$ with
$(-1)^{n-1}h^{(n)}(q)<0$ kills the hierarchy while leaving the already
certified cubic finite difference open.

The next constructive target is not another derivative census. It is to
derive or finitely obstruct the positive measure $\eta$ from the exact
carrier factor

\[
e^{5v/2}(2e^{2v}-3)e^{-e^{2v}}.
\]

## Subordinator interpretation

The Bernstein conjecture has an exact probabilistic meaning. If $I$ is the
exponential functional of a subordinator with Laplace exponent $\phi$, its
Mellin moments obey the recurrence

\[
\frac{\mathbb E(I^q)}{\mathbb E(I^{q-1})}
=\frac q{\phi(q)}.
\]

For the normalized primitive residual law, the left side is
$M_q/M_{q-1}$. Therefore its candidate subordinator exponent is not fitted:

\[
\phi(q)
=q\frac{M_{q-1}}{M_q}
=h(q).
\]

Consequently, subject to the standard Mellin-recurrence and moment-
determinacy hypotheses, the following statements are equivalent:

1. $h$ is a Bernstein function.
2. The primitive residual law is the exponential functional of a
   subordinator with Laplace exponent $h$.
3. The full alternating response tower is generated by one positive Lévy
   measure.

This turns the conjecture into a constructor problem. Derive a monotone Lévy
scale flow whose accumulated exponential survival time has density
proportional to $F(a+R)$, or prove that no such subordinator can produce the
primitive wall factor. The cubic sign would then follow from constructibility
rather than an isolated inequality.

The relevant primary framework is Patie and Savov,
[Bernstein-gamma functions and exponential functionals of Lévy
processes](https://arxiv.org/abs/1604.05960). Their general theory supplies
the recurrence architecture, not the missing identification of this theta
carrier. That identification remains our source-specific theorem.

At the hardest tested point $c=200$, $q=4$, logarithmic-coordinate Decimal
quadrature stabilizes all signed derivatives through order twenty:

\[
(-1)^{n-1}h^{(n)}(4)>0,
\qquad
1\le n\le20.
\]

The twentieth value is about $1.9651\times10^{-20}$. Step halving agrees
through order ten to many digits. This is strong discovery evidence but not
an interval certificate or an all-orders theorem.

The endpoint behavior gives the first exact parameter of the candidate
subordinator. If $F(a)>0$, then

\[
M_{q-1}
=\frac{F(a)}q+O(1)
\]

as $q\downarrow0$, and hence

\[
h(0+)=\frac{F(a)}{M_0}.
\]

For $c>3/2$, this is the killing rate of the candidate subordinator. At the
primitive boundary $c=3/2$, the carrier vanishes linearly at the wall, so
$M_{q-1}$ remains finite and

\[
h(0+)=0.
\]

Thus the primitive wall factor $2e^{2v}-3$ has a direct constructor meaning:
it switches off subordinator killing exactly at the boundary source. The
wall-pole response is not an arbitrary analytic correction; it records how
this killing channel changes as the wall moves away from the primitive
zero.

This also supplies a new consistency test for any proposed Lévy measure.
Its killing coefficient must equal $F(a)/M_0$ for $c>3/2$ and vanish
continuously as $c\downarrow3/2$. A representation with a fitted or
wall-independent killing term is not source-admissible.

## Truncated Lévy-moment gate

Alternating derivatives alone are weaker than the proposed positive Lévy
measure. At a fixed $q$, put

\[
a_n=(-1)^{n-1}h^{(n)}(q).
\]

If $h$ is Bernstein, then for $n\ge2$ these are consecutive moments of the
positive measure $t^2e^{-qt}\,d\eta(t)$:

\[
a_n=\int_0^\infty t^n e^{-qt}\,d\eta(t).
\]

Therefore the ordinary and shifted Hankel forms built from

\[
m_j=a_{j+2}
\]

must both be positive.

At the hostile far-wall point $c=200$, $q=4$, the stable order-twenty jet
passes this stronger test. The ordinary matrices

\[
(m_{i+j})_{0\le i,j<9}
\]

and shifted matrices

\[
(m_{i+j+1})_{0\le i,j<9}
\]

have strictly positive Decimal LDL pivots. The ninth pivots are
approximately

\[
2.1435\times10^{-23}
\]

and

\[
1.9791\times10^{-25},
\]

respectively.

Thus a positive truncated Stieltjes measure is compatible with the observed
response jet to this order. This is not an all-orders existence theorem and
does not identify the source Lévy measure, but it closes the cheapest
moment-cone falsifier of the subordinator conjecture at the numerically most
delicate sampled point.

## Truncated-Gamma score normal form

The carrier admits a sharper exact normal form. Put

\[
x=ce^{2R},
\qquad
L=\log(x/c).
\]

Then, up to the normalization which cancels in adjacent moment ratios,

\[
M_q
=2^{-q-1}\int_c^\infty
L^q x^{1/4}(2x-3)e^{-x}\,dx.
\]

The apparently special primitive factor is an exact weighted derivative:

\[
x^{1/4}(2x-3)e^{-x}\,dx
=-2x^{-1/4}\,d\!\left(x^{3/2}e^{-x}\right).
\]

For $q>0$, integration by parts therefore gives

\[
M_q
=2^{-q}\int_c^\infty x^{1/4}e^{-x}
\left(qL^{q-1}-\frac14L^q\right)\,dx.
\]

Thus the primitive residual law is a logarithmic pushforward of a truncated
Gamma $5/4$ carrier acted on by one first-order score operator. The wall
$c=3/2$ is exactly where the score $2x-3$ first becomes nonnegative on
the entire retained tail. This is more rigid than an arbitrary positive
density and gives a concrete possible origin for the Bernstein response:
the adjacent-ratio generator may be the Mellin shadow of this positive
truncated-Gamma score transport.

It also defines the next honest gate. One must prove that the first-order
score operator preserves the Bernstein property of the adjacent logarithmic
moment ratio for every $c\ge3/2$, or exhibit the first $(c,q,n)$ where it
does not. Positivity of the score alone is insufficient; the theorem must
use its derivative provenance and the moving lower wall.

## Source Lévy tail as a Volterra deconvolution

The subordinator claim has a sharper necessary-and-sufficient density test.
Let $k_c(r)=F(a+r)/M_0$ be the normalized primitive residual density on
$r>0$, and put

\[
\kappa_c=k_c(0)=\frac{F(a)}{M_0}.
\]

For a driftless subordinator killed at rate $\kappa_c$, the density of its
exponential functional satisfies

\[
k_c(r)
=\int_r^\infty
\overline\Pi_c\!\left(\log(y/r)\right)k_c(y)\,dy
+\kappa_c\int_r^\infty k_c(y)\,dy.
\]

Conversely, a nonnegative Lévy-tail solution $\overline\Pi_c$ to this
equation constructs the required subordinator. With $y=re^t$, the source
equation is the explicit multiplicative Volterra deconvolution

\[
k_c(r)-\kappa_c\int_r^\infty k_c(y)\,dy
=\int_0^\infty
\overline\Pi_c(t)k_c(re^t)re^t\,dt.
\]

This confirms the endpoint calculation: the wall value $F(a)/M_0$ is
exactly the killing coefficient demanded by the density equation. At
$c=3/2$ both vanish, giving an unkilled flow without fitting a parameter.

The live theorem is now constructive and local to the source. Deconvolve
the displayed equation and prove that its unique kernel is a nonnegative,
nonincreasing Lévy tail with the required integrability, for every
$c\ge3/2$. A negative value, increase, or integrability failure is an exact
falsifier. This gate is stronger and more explanatory than any finite
derivative or Hankel census.

The density equation and its converse are supplied by Pardo, Rivero, and
van Schaik, [On the density of exponential functionals of Lévy
processes](https://arxiv.org/abs/1107.3760). Their theorem supplies the
constructor criterion; positivity of the deconvolved theta kernel remains
the source-specific problem.

Mellin transformation diagonalizes the deconvolution. If

\[
K_c(s)=\int_0^\infty r^{s-1}k_c(r)\,dr,
\]

then the density equation gives

\[
\frac{K_c(s)}{K_c(s+1)}
=\frac{\kappa_c}{s}
+\int_0^\infty e^{-st}\overline\Pi_c(t)\,dt.
\]

Since $K_c(s+1)/K_c(s)=M_s/M_{s-1}=s/h(s)$, the candidate tail is forced by

\[
\int_0^\infty e^{-st}\overline\Pi_c(t)\,dt
=\frac{h(s)-\kappa_c}{s}.
\]

There is therefore no freedom to select a favorable subordinator after the
fact. The exact next gate is whether the inverse Laplace transform of
$(h-\kappa_c)/s$ is a nonnegative nonincreasing function with Lévy-tail
integrability. The alternating derivative tower probes this object only
indirectly.

## Drift and total jump moment are forced

The remaining Lévy data already have exact source formulas. A Bernstein
exponent has drift

\[
d_c=\lim_{s\to\infty}\frac{h(s)}s
=\lim_{s\to\infty}\frac{M_{s-1}}{M_s}.
\]

The primitive residual has unbounded support. Its adjacent moment ratio
$M_s/M_{s-1}$ therefore tends to infinity, so

\[
d_c=0.
\]

Thus the Volterra equation correctly required a driftless subordinator; this
was not an assumption chosen for convenience.

The opposite endpoint fixes the total first jump moment. For $c>3/2$, write

\[
M_{s-1}=\frac{k_c(0)}s+C_c+O(s),
\qquad
M_s=1+s\ell_c+O(s^2),
\]

where

\[
C_c
=\int_0^1\frac{k_c(r)-k_c(0)}r\,dr
+\int_1^\infty\frac{k_c(r)}r\,dr,
\qquad
\ell_c=\int_0^\infty k_c(r)\log r\,dr.
\]

It follows that

\[
h'(0+)=C_c-k_c(0)\ell_c
=\int_0^\infty\overline\Pi_c(t)\,dt
=\int_0^\infty t\,\Pi_c(dt).
\]

At $c=3/2$, $k_c(0)=0$ and the formula reduces to

\[
h'(0+)=M_{-1}.
\]

Any proposed Lévy tail must therefore match three independently forced
features: killing $k_c(0)$, zero drift, and total mass integral $h'(0+)$. A
failure at any one of them rejects the construction before higher response
signs are considered.

## Lambert-W saddle theorem and small-jump target

The exact double-exponential carrier controls the opposite end of the Lévy
tail. The logarithm of the $M_s$ integrand has second derivative

\[
-\frac{s}{r^2}
-\frac{24ce^{2r}}{(2ce^{2r}-3)^2}
-4ce^{2r}<0.
\]

It therefore has one saddle and the tilted residual law concentrates there.
The saddle equation gives

\[
2ce^{2r_s}\sim\frac{s}{r_s}.
\]

Equivalently,

\[
2r_s\sim W(s/c),
\]

where $W$ is the Lambert function. Its Gaussian width is of order
$\sqrt{r_s/s}$, hence negligible relative to $r_s$. Standard moving-saddle
Laplace bounds then give

\[
h(s)\sim\frac{2s}{W(s/c)},
\qquad
\mathcal L\overline\Pi_c(s)
\sim\frac{2}{W(s/c)}.
\]

For a nonnegative candidate tail, the measure-level Tauberian consequence is
the integrated asymptotic

\[
U_c(t):=\int_0^t\overline\Pi_c(u)\,du
\sim\frac{2}{W(1/(ct))}
\]

as $t\downarrow0$. This already forces infinite jump activity while remaining
compatible with a finite first jump moment.

The stronger pointwise prediction is

\[
\overline\Pi_c(t)
\sim
\frac{2}{t\log^2(1/(ct))}
\]

at leading logarithmic order. It is the derivative scale suggested by the
integrated law, but it does not follow from leading slow variation alone.
A second-order Tauberian or monotone-density theorem is still required.

Thus the Lambert-$W$ moment and transform asymptotics are promoted to the
analytic saddle target, while only the pointwise tail equivalent remains
conjectural. Finite activity, a power-law integrated singularity, or failure
of the Lambert-$W$ transform asymptotic would reject the proposed Lévy
interpretation even if low-order derivatives remain positive.

## Adjacent-ratio Darboux transform

The integration-by-parts normal form gives an exact algebraic reduction of
the score operation. Define the unscored truncated-Gamma logarithmic moments

\[
A_q=\int_c^\infty \log(x/c)^q x^{1/4}e^{-x}\,dx
\]

and their adjacent-ratio generator

\[
b(q)=q\frac{A_{q-1}}{A_q}.
\]

The scored moments satisfy

\[
M_q=2^{-q}A_q\left(b(q)-\frac14\right).
\]

Therefore, for $q>1$, the primitive generator is exactly

\[
h(q)
=2b(q)
\frac{b(q-1)-1/4}{b(q)-1/4}.
\]

This is a contiguous Darboux-type transform: the primitive score does not
introduce an independent response tower. It compares two consecutive values
of the base truncated-Gamma generator around the source-fixed level $1/4$.
Positivity of $M_q$ also forces

\[
b(q)>\frac14.
\]

The central theorem has consequently split into two smaller questions:

1. Determine the Bernstein or higher-response class of the unscored
   generator $b$.
2. Prove that the displayed shifted fractional transform preserves the
   required third-response sign on $q\ge4$.

Ordinary total positivity of the Mellin kernel proves log-convexity of
$A_q$ and monotonicity of $A_q/A_{q-1}$, but it does not by itself prove
either preservation statement. The exact transform identifies what extra
source inequality is needed instead of attributing the result vaguely to
total positivity.

The shift $1/4$ is itself source-derived. A second integration by parts
gives

\[
qA_{q-1}
=\int_c^\infty
\log(x/c)^q x^{1/4}(x-5/4)e^{-x}\,dx.
\]

Hence, under the unscored $q$-tilted Gamma law,

\[
b(q)=\mathbb E_q(x-5/4),
\qquad
b(q)-\frac14=\mathbb E_q(x-3/2).
\]

If

\[
u(q)=\mathbb E_q(x-3/2)>0,
\]

then the primitive generator becomes

\[
h(q)=2\left(u(q)+\frac14\right)\frac{u(q-1)}{u(q)}.
\]

Thus the Darboux transform transports expected primitive-wall distance
between adjacent logarithmic tilts. The constant $1/4$ is the difference
between the Gamma restoring-force offset $5/4$ and the primitive wall
$3/2$; it is not a fitted normalization.

## Moving-wall differential-difference system

The Darboux transform is also the compatibility law of two source flows.
Retain the wall parameter in $A_q(c)$. Differentiation of the moving lower
limit gives, for $q>0$,

\[
c\,\partial_c A_q(c)=-qA_{q-1}(c).
\]

Consequently,

\[
b(q,c)=-c\,\partial_c\log A_q(c).
\]

After absorbing the Gamma quarter-weight into

\[
\Psi_q(c)=c^{1/4}A_q(c),
\]

the primitive wall-distance response becomes exactly

\[
u(q,c)=b(q,c)-\frac14
=-c\,\partial_c\log\Psi_q(c).
\]

Moreover the scored moment is the wall flux

\[
M_q(c)
=-2^{-q}c^{3/4}\partial_c\Psi_q(c),
\]

and hence

\[
h(q,c)
=2q\frac{\partial_c\Psi_{q-1}(c)}
{\partial_c\Psi_q(c)}.
\]

This is an exact differential-difference system: continuous wall motion
lowers the exponent by one, while the primitive adjacent-ratio generator is
the ratio of two consecutive wall fluxes. The quarter-shift disappears
after the canonical gauge $A_q\mapsto c^{1/4}A_q$.

The cubic gate is therefore not merely a property of a moment ratio. It is
an order-three response statement for adjacent solutions of one moving-wall
lowering equation. The next conceptual attack is to determine whether this
system carries a sign-regular or Toda-type comparison law for its wall
fluxes. Calling it integrable before deriving that law would be premature;
the displayed lowering equation is the exact source structure presently
established.

## First universal wall-flux sign law

Let

\[
B_q(c)=\int_c^\infty
\log(x/c)^q x^{1/4}(x-3/2)e^{-x}\,dx.
\]

For $c\ge3/2$, this is a positive moment function and

\[
\frac{h(q,c)}q=2\frac{B_{q-1}(c)}{B_q(c)}.
\]

The Mellin kernel makes $B_q$ strictly log-convex in $q$. Hence

\[
q\longmapsto\frac{B_q}{B_{q-1}}
\]

is strictly increasing, and therefore

\[
\frac{d}{dq}\left(\frac{h(q,c)}q\right)<0.
\]

Equivalently,

\[
qh'(q,c)-h(q,c)<0.
\]

This proves source-derived sublinearity of the primitive response and is
consistent with its zero-drift limit. It is the strongest sign obtained
from ordinary two-by-two total positivity alone.

That mechanism cannot yield the cubic theorem by itself. For a positive
two-atom wall-flux measure,

\[
B_q=pa^q+(1-p)b^q,
\qquad
0<a<b,
\]

one has

\[
\frac{B_{q-1}}{B_q}
=\frac1b\left(1+(e^d-1)\frac{z}{1+z}\right),
\qquad
d=\log(b/a),
\quad
z=\frac{p}{1-p}e^{-dq}.
\]

The logistic factor $z/(1+z)$ has a second derivative whose sign changes
when it crosses $1/2$. Thus even a strictly totally positive moment kernel
does not force complete monotonicity of the adjacent reciprocal ratio.

The remaining source law must therefore use more than positivity of the
wall-flux measure. It must exploit the continuous truncated-Gamma density,
its moving-wall lowering equation, or a stronger interlacing property that
the two-atom model lacks.

## Berwald-Borell orientation of the first response

The continuous wall flux has exactly the missing property. In the coordinate

\[
y=\log(x/c),
\]

its moment density is, up to normalization,

\[
w_c(y)
=(ce^y)^{5/4}(ce^y-3/2)e^{-ce^y},
\qquad y>0.
\]

Writing $x=ce^y$, direct differentiation gives

\[
\frac{d^2}{dy^2}\log w_c(y)
=-x-\frac{(3/2)x}{(x-3/2)^2}<0.
\]

Thus the wall-flux law is strictly log-concave, a property absent from the
two-atom falsifier.

The Berwald-Borell moment theorem now applies: the normalized moment
function

\[
C_c(q)=\frac{B_q(c)}{\Gamma(q+1)}
\]

is log-concave for $q\ge0$. Since

\[
h(q,c)=2\frac{C_c(q-1)}{C_c(q)},
\]

putting $f_c(q)=\log C_c(q)$ yields

\[
\frac{h'(q,c)}{h(q,c)}
=f_c'(q-1)-f_c'(q)>0.
\]

Hence

\[
h'(q,c)>0.
\]

This proves the first Bernstein sign structurally for every $c\ge3/2$ and
$q>1$. The proof uses precisely the continuous Gamma-wall log-concavity
that the hostile discrete model lacks.

It also isolates the higher obstruction. Define

\[
\delta_j(q)=f_c^{(j)}(q-1)-f_c^{(j)}(q).
\]

Then

\[
\frac{h'''(q,c)}{h(q,c)}
=\delta_3+3\delta_1\delta_2+\delta_1^3.
\]

Berwald-Borell supplies $delta_1>0$ but does not determine the coupled sign
of the other two terms. The primitive cubic theorem is therefore a precise
higher Berwald-Borell curvature inequality for this particular wall-flux
density.

The normalized-moment theorem is recalled and proved in Bobkov and Madiman,
[Concentration of the information in data with log-concave
distributions](https://arxiv.org/abs/1012.5457). Klartag and Lehec's
[Poisson processes and a log-concave Bernstein
theorem](https://www.math.tau.ac.il/~klartagb/papers/log_concave_bernstein.pdf)
supplies a relevant stronger framework: Berwald-Borell determinant defects
are themselves Laplace transforms of positive measures. Whether the
specific cubic defect above is one of those transforms is now the sharp
comparison question.

## Flow-mismatch obstruction

The stronger log-concave Bernstein theorem cannot be imported directly.
Its positive transform evolves a log-concave measure in the additive
Laplace parameter conjugate to $y$. Our response parameter $q$ instead
multiplies the wall-flux density by $y^q$, which is an additive exponential
tilt only after the change of variables

\[
T=\log y.
\]

That change does not preserve the needed source property. If

\[
g_c(T)=e^T w_c(e^T),
\]

then, writing $y=e^T$, $x=ce^y$, one has

\[
\frac{d^2}{dT^2}\log g_c(T)
=y\left(\frac54+\frac{x}{x-3/2}-x\right)
-y^2\left(x+\frac{(3/2)x}{(x-3/2)^2}\right).
\]

For $c=2$ and $y\downarrow0$, the leading coefficient is

\[
y\left(\frac54+\frac{2}{2-3/2}-2\right)
=\frac{13}{4}y>0.
\]

Hence the $T$-density is locally log-convex, not log-concave. The two flows
are genuinely different. Klartag--Lehec use additive tilt in $y$, whereas
the primitive gate uses additive tilt in $\log y$.

This is the first real theorem-level obstruction after the Berwald-Borell
advance. Ordinary normalized-moment log-concavity proves $h'>0$, but the
available stronger Laplace-flow theorem does not type-check against
$h'''$. The missing result is a higher continuous Berwald-Borell theorem
for the specific Gamma-wall family, or an explicit representation of

\[
\delta_3+3\delta_1\delta_2+\delta_1^3
\]

as a positive source transform. Any derivation that silently identifies
the $y$-Laplace flow with the $q$-Mellin flow is invalid.

Klartag and Lehec explicitly note that characterizing when their
Berwald-Borell transform measures remain log-concave would yield constraints
beyond the ordinary Berwald-Borell inequality. The primitive cubic defect is
now a concrete source-specific instance of precisely that higher-constraint
frontier.

## One-fold curvature classification of the Gamma wall

The wall-flux potential has only one higher-curvature defect. Write

\[
w_c(y)=e^{-V_c(y)},
\qquad
x=ce^y,
\qquad
a=\frac32.
\]

Then

\[
V_c''(y)
=x+\frac{ax}{(x-a)^2}>0
\]

and

\[
V_c'''(y)
=x\left(1-\frac{2a(x+a)}{(x-a)^3}\right).
\]

Putting $x=az$ and $d=z-1>0$, the unique sign transition is determined by

\[
3d^3-4d-8=0.
\]

The cubic has exactly one positive root $d_*$ beyond its only positive
turning point. Hence

\[
x_*=\frac32(1+d_*)
\]

is the unique curvature-fold coordinate, numerically about $4.06$.

Therefore the source family splits canonically:

1. If $c\ge x_*$, then $V_c'''ge0$ on the entire retained wall flux.
2. If $3/2\le c<x_*$, there is one initial negative-curvature band followed
   by one positive-curvature band.

This classification is independent of moment order and introduces no fitted
partition. It identifies the exact extra structure absent from arbitrary
log-concave measures: the Gamma-wall potential has increasing curvature
after at most one canonical fold.

The next theorem should first test whether log-concavity together with
$V'''ge0$ forces the higher Berwald-Borell cubic defect. If it does, the
entire far-wall region $c\ge x_*$ closes at once, and only a single bounded
near-wall defect requires a source-derived repair. If it does not, the
smallest increasing-curvature counterexample will prevent another false
generalization.

## Increasing curvature does not force the cubic defect

Consider the smooth perturbation of the memoryless carrier

\[
w_\varepsilon(y)=\exp(-\lambda y-\varepsilon y^3),
\qquad y>0,
\qquad \lambda>0,
\qquad \varepsilon>0.
\]

Its potential is strictly convex and has increasing curvature:

\[
V_\varepsilon''(y)=6\varepsilon y>0,
\qquad
V_\varepsilon'''(y)=6\varepsilon>0.
\]

Let

\[
B_q(\varepsilon)=\int_0^\infty
y^q e^{-\lambda y-\varepsilon y^3}\,dy,
\qquad
r_\varepsilon(q)=q\frac{B_{q-1}(\varepsilon)}{B_q(\varepsilon)}.
\]

At fixed $q>-1$,

\[
B_q(\varepsilon)
=\frac{\Gamma(q+1)}{\lambda^{q+1}}
\left[
1-\frac{\varepsilon}{\lambda^3}(q+1)_3
+\frac{\varepsilon^2}{2\lambda^6}(q+1)_6
+O(\varepsilon^3)
\right].
\]

Consequently,

\[
r_\varepsilon(q)
=\lambda
+\frac{3\varepsilon}{\lambda^2}(q+1)(q+2)
-\frac{18\varepsilon^2}{\lambda^5}
(q+1)(q+2)(q+3)^2
+O(\varepsilon^3),
\]

and therefore

\[
r_\varepsilon'''(q)
=-\frac{108\varepsilon^2}{\lambda^5}(4q+9)
+O(\varepsilon^3).
\]

For every fixed $q>-1$, this is negative for all sufficiently small positive
$\varepsilon$. Thus log-concavity together with $V'''>0$ does not imply the
primitive cubic gate. The memoryless exponential is an order-three
stationary point: the first variation is quadratic in $q$ and disappears
under three derivatives, while failure first appears at second order.

The Gamma-wall fold remains useful source geometry, but it cannot close the
far-wall theorem through a universal increasing-curvature principle. The
next viable theorem must use the exact Gamma-wall differential equation or a
source-specific two-copy transport identity.

## Falsifier

At any $a$ and $4\le q\le10$, failure of

\[
q(\mu_3-\mu_3^-)
<3(1-qd)(v^--v)+d^2(3-qd)
\]

falsifies the pointwise order-four explanation.  The weaker cubic B-spline
average may still survive, so pointwise failure must not be misreported as
failure of the already certified theta gate.
