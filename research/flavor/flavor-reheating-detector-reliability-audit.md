# Reheating transfer and detector-reliability audit (WP137)

Owner: `marici.Figueiredo`.

## Bounded question

Can a source-derived reheating channel transfer WP136's cosmological law
faithfully into the flavor relevant operator, and does WP133's multi-point
probe identify the UV constructor uniformly over that ensemble?

Pre-objective process report: excitement `9/10`, confidence `8/10` in faithful
amplitude transfer and `9/10` that finite reach prevents uniform
identification, expected information gain `9/10`. Confounds are sudden
quadratic mixing, Gaussian equilibrium, and no collider implementation. These
reports are non-evidential.

Frozen optionality snapshot: two singlets; one rational rotation; one
covariance pushforward; one accessibility domain; one rigorous reliability
bound; four hostile constructors; twelve exact checks.

## Source-derived amplitude transfer

Let `delta` be the cosmological spectator and `chi` the weak-basis-singlet
coefficient field of WP135's relevant flavor operator. A quadratic term
`epsilon delta chi` is gauge, Lorentz, and weak-basis invariant. Freeze the
integrated reheating evolution as

\[
\binom{\delta_f}{\chi_f}=
\begin{pmatrix}3/5&-4/5\\4/5&3/5\end{pmatrix}
\binom{\delta_i}{0}.
\]

The rotation is exactly orthogonal,

\[
\chi_f=\frac45\delta_i,
\qquad \operatorname{Var}(\chi_f)=\frac{16}{25}\sigma^2.
\]

Hence `w=chi_f/[(4/5)sigma]` retains WP136's standard Gaussian law. The map
is injective and sign-preserving on the admitted initial line. Sign is erased
only later by the scale readout proportional to `sqrt(|chi|)`. The transfer is
conditional on a source-derived mass matrix and reheating duration; another
mixing phase can change or null it.

## Detector reliability over source support

Declare the calibrated domain `|w|<2`. Its exact Gaussian probability is
`erf(sqrt(2))`. Independently of evaluating that transcendental number, the
unit variance gives

\[
P(|w|\ge2)\le\frac14,
\qquad P(\text{accessible})\ge\frac34.
\]

On accessible draws, WP133's formal multi-point family has rank four on four
constructors. On inaccessible draws, every mediator decouples: rank is one
and the kernel dimension is three. A Gaussian has nonzero support beyond every
finite reach, so the experiment is not uniformly faithful on the full source
domain. An expected rank would hide this contextual kernel.

Conditioning on accessibility creates a postselected relational experiment.
It can support conditional identification only if selection and normalization
are physical; it cannot become unconditional source authority.

The accessible partition has four singleton classes. The inaccessible
partition has one four-member class. Thus the first nonfaithful arrow is

\[
\text{cosmological amplitude ensemble}\to
\boxed{\text{finite detector domain}}\to\text{constructor record}.
\]

## Disposition

WP137 supplies faithful amplitude transport and a rigorous reliability bound,
but not uniform source identification or an executable instrument.
Classification: **source-derived ensemble transport with conditional,
non-uniform constructor identification**.

The smallest exact falsifier is any admitted `|w|>=2` draw, whose detector
kernel has dimension three. The remaining gate is either a bounded-support
source law wholly inside detector reach or an effectively complete instrument,
plus an implemented multi-point channel.

Post-objective process report: excitement `9/10`, confidence `10/10`, realized
information gain `10/10`. Raw delta: one reheating map becomes injective; the
Gaussian law transfers exactly; reliability is bounded below by `3/4`; four
singleton classes coexist with one inaccessible four-member class; twelve of
twelve checks pass; uniform faithfulness remains absent. These reports are
non-evidential.
