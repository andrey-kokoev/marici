# UV-fixed-point scale-authority audit (WP135)

Owner: `marici.Figueiredo`.

## Bounded question

Does specifying a UV fixed point or asymptotically safe critical surface close
WP134's boundary-authority gate and uniquely select the flavor crossover
scale?

Pre-objective process report: excitement `8/10`, confidence `9/10` that a
relevant-direction amplitude survives, expected information gain `8/10`.
The immediate reason is that fixed points determine critical exponents but
normally leave relevant coordinates as boundary data. Confounds are nonlinear
flows, dangerously irrelevant operators, and hypothetical fixed points with
no relevant directions. These reports are non-evidential.

Frozen optionality snapshot: one fixed point; one relevant eigenoperator; two
RG presentations of one trajectory; one hostile critical-surface point; one
zero-deformation limit; ten exact checks.

## Linearized critical-surface map

Let `delta` be the coefficient of a relevant eigenoperator near a UV fixed
point and let

\[
\frac{d\delta}{d\log\mu}=-\theta\delta,
\qquad \theta>0.
\]

The RG-invariant crossover scale is

\[
\Lambda=\mu|\delta(\mu)|^{1/\theta},
\qquad
\log\Lambda=\log\mu+rac1\theta\log|\delta(\mu)|.
\]

The fixed point determines the eigenoperator and exponent `theta`. The
trajectory amplitude `delta` selects where the flow leaves the fixed-point
regime.

For `theta=2`, take `(log mu,log|delta|)=(0,-4)`. Then
`log Lambda=-2`. Re-express the same trajectory at `log mu=3`; exact running
gives `log|delta|=-10`, and the scale remains `-2`. Thus the crossover scale
descends under RG presentation changes.

## Hostile critical-surface fiber

At the same reference scale, choose the equally admissible relevant amplitude
`log|delta|=-2`. It gives `log Lambda=-1`, an exact residual of one. Both
trajectories approach the same UV fixed point and share its critical exponent,
but generate different physical thresholds.

Setting `delta=0` exactly does not select a finite crossover scale at all: the
trajectory remains at the fixed point. Hence neither the fixed-point location
nor its linearized spectrum supplies the missing amplitude.

With several relevant directions the ambiguity is larger: their amplitudes
select both scales and dimensionless ratios. Irrelevant couplings may be fixed
by UV safety, but that does not silently convert relevant coordinates into
predictions.

## Disposition

WP135 classifies a UV fixed point as a **critical-data rigidifier and
conditional trajectory selector**, not an absolute-scale selector by itself.
It can reduce the admissible coupling family and make irrelevant couplings
predictive, but every surviving relevant amplitude remains a source boundary
datum unless a separate operation selects it.

A zero-dimensional critical surface could remove coupling freedom, but an
overall RG-time translation still requires relational matching to a physical
clock such as the Planck or electroweak scale. Such a gravitational or
cosmological matching arrow would define a new source relation and must be
tested independently.

The smallest exact falsifier is the pair `log|delta|=-4,-2`, approaching the
same fixed point but shifting `log Lambda` by one. The remaining gate is a
source-generated relevant-amplitude distribution or boundary condition with
an independently typed physical clock. No threshold instrument is established.

Post-objective process report: excitement `8/10`, confidence `10/10` in the
bounded negative result, realized information gain `9/10`. Raw delta: one UV
fixed point and exponent are frozen; two presentation charts merge exactly;
two critical-surface trajectories remain physically distinct; one finite
crossover disappears at zero deformation; ten of ten checks pass; no
relevant-amplitude selector or instrument is added. These reports are
non-evidential.
