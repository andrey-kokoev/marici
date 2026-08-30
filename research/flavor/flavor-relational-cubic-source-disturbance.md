# A relational cubic orients the sign packet but disturbs the portal magnitude

Work package: WP619  
Owner: marici.Figueiredo

## Process and optionality snapshot

Protocol repair: the initial algebraic setup for this packet began before the
required activation and optionality snapshot was recorded. The following
snapshot was frozen after rereading the repository policy and before running
the exact checker. It is a mid-objective record, not a retrospectively claimed
preregistration.

- excitement: 9/10;
- confidence that the direct polynomial cross term disturbs the target:
  8/10;
- expected information gain: 8/10;
- immediate reason: this is the first source lift combining a genuine odd
  reference with the continuous portal coordinate;
- confounds: non-Gaussian mediators, higher mediator sectors, and a separately
  selected magnitude potential.

Frozen optionality space:

- one direct polynomial cross-interaction branch;
- one positive Gaussian mediator class;
- one formal pure-cross rival;
- two simultaneous-reflection sign orbits;
- one continuous magnitude coordinate \(r\);
- two joint experimental records: root-vector masses and referenced
  interference;
- ten exact checks declared;
- unresolved source data: mediator grammar, coupling signs, self-channel
  completion, and the magnitude potential.

## Bounded question

Can Nima's two-odd-port mechanism be lifted from an abstract sign quotient to
a physical source interaction while preserving the WP618 target portal ratio?

## Independently sourced odd ports

For the WP618 lens, include an explicit global sign sheet:

\[
X_s(r)=sX(r),
\qquad s\in\{-1,1\}.
\]

Its cubic is

\[
Q(s,r)=\operatorname{Tr}X_s(r)^3
=6s(r^2-1).
\]

The WP438 quadratic reference

\[
H=\operatorname{diag}(1,1,-2)
\]

has the independently nonzero cubic

\[
R=\operatorname{Tr}H^3=-6.
\]

The sign of \(H\) is relationally established by its construction from the
traceless part of the positive composite \(A^2+D^2\); it is not read from the
CKM target.

At the abstract sign level, simultaneous reflection identifies

\[
(+,+)\sim(-,-),
\qquad
(+,-)\sim(-,+).
\]

The character \(\operatorname{sgn}(QR)\) separates these two orbits exactly.
This proves relational orientation on the declared discrete quotient, not an
absolute sign.

## Continuous-source disturbance

The polynomial source interaction is

\[
V_{\mathrm{rel}}=-\lambda QR.
\]

Substitution gives

\[
V_{\mathrm{rel}}=36\lambda s(r^2-1),
\qquad
\frac{\partial V_{\mathrm{rel}}}{\partial r}=72\lambda sr.
\]

At the target \(r=3/5\),

\[
\left.\frac{\partial V_{\mathrm{rel}}}{\partial r}\right|_{3/5}
=\frac{216}{5}\lambda s.
\]

Thus every nonzero relational coupling moves the target magnitude unless a
second source force cancels it. The discrete sign selector is invasive when
lifted to the continuous charge lens.

Replacing \(Q\) and \(R\) by normalized sign characters would remove the
local magnitude force, but that operation is nonpolynomial and singular at a
zero of either cubic. It is not supplied by the declared local field theory.

## Gaussian completion gate

A real positive-mass mediator \(\sigma\) with coupling

\[
\sigma(g_QQ+g_RR)
\]

generates, after elimination,

\[
-\frac{1}{2M^2}(g_QQ+g_RR)^2.
\]

The resulting two-port kernel is a positive-semidefinite Gram matrix. Its
cross entry obeys

\[
K_{QR}^2\leq K_{QQ}K_{RR}.
\]

Consequently a nonzero cross channel requires self channels. A formal pure
cross matrix has eigenvalues \(+1\) and \(-1\) and cannot arise from
positive Gaussian elimination. Additional mediators preserve the same Gram
inequality. Canceling the self terms requires further independently derived
physics, not algebraic subtraction fitted after the target is known.

The cubic product has field dimension six. A Gaussian mediator with linear
couplings to each cubic is a renormalizable UV interface, but its complete
low-energy output includes the self terms and their magnitude backreaction.

## Joint physical criticism

The appropriate experiment must measure two records in the same prepared
source lineage:

1. the three root-vector masses, which test whether the portal magnitude still
   gives \(1:4:9\);
2. a coherent \(H\)-referenced interference record, which resolves the
   relative sign orbit.

If orientation appears together with a shifted mass ratio, the claimed
noninvasive relational selector is falsified. A valid architecture must derive
the mediator couplings, finite-width response, self-channel terms, and a
magnitude potential whose stationary point remains \(r=3/5\) after the full
interaction is included.

## Disposition

The two-cubic mechanism is a faithful relational sign selector on the finite
sign quotient. Its direct polynomial realization is not a selector of the
complete continuous lens: it changes the magnitude coordinate and carries
unavoidable Gaussian self channels.

The remaining source problem is therefore not merely to choose the sign of a
cross coupling. It is to derive a magnitude sector and orientation sector
whose composed stationary equations retain \(r=3/5\) without a fitted
counterforce.

## Post-objective process report

- excitement: 9/10;
- confidence in the bounded disturbance and Gaussian-Gram result: 10/10;
- realized information gain: 9/10;
- immediate reason: the calculation separates discrete relational
  orientation from continuous preparation and makes their backreaction exact;
- surviving confounds: non-Gaussian completions and a separately sourced
  magnitude sector.

Raw optionality delta:

- the relational sign character is promoted on the two-orbit finite quotient;
- the noninvasive continuous-selector interpretation is criticized;
- the formal pure-cross positive-Gaussian branch is eliminated;
- one joint two-record criticism is constructed;
- all ten declared exact checks pass;
- no contradiction remains inside the declared domain;
- mediator completion, finite-width calibration, and magnitude preparation
  remain open.

These process ratings are non-evidential.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp619_relational_cubic_source_disturbance.py

The generated result is
`research/flavor/results/wp619_relational_cubic_source_disturbance.json`.
