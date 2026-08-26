# Poisson exposure rank restoration

Work package: WP571  
Owner: marici.Figueiredo

## Why WP570 is not the only completion

WP570 proved that a normalized binary record has only one probability-tangent
direction, and that a typed null outcome can restore rank two. Collider
likelihoods can carry another physical coordinate: the absolute selected-event
rate relative to a calibrated exposure or luminosity.

This packet separates the two cases exactly. A selected-only shape likelihood
has rank one for two binary perturbations. A Poisson count likelihood with a
calibrated exposure can recover the independent rate direction. If exposure is
left unconstrained, profiling removes that direction again.

## Exact two-bin Poisson experiment

Let two selected detector bins have independent Poisson means

\[
\mu_1=1+\theta_1,
\qquad
\mu_2=1+\theta_2
\]

at the nominal point. The response Jacobian is \(D=I_2\), so the Poisson
Fisher matrix is

\[
G_{\mathrm{Poisson}}
=D^T\operatorname{diag}(1/\mu)D
=I_2.
\]

The normalized selected-bin probabilities are \(p=(1/2,1/2)^T\). Their
Jacobian is

\[
J_{\mathrm{shape}}=
\begin{pmatrix}
1/4&-1/4\\
-1/4&1/4
\end{pmatrix},
\]

which has rank one. With expected total count \(N=2\), the shape Fisher
contribution is

\[
G_{\mathrm{shape}}
=
\begin{pmatrix}
1/2&-1/2\\
-1/2&1/2
\end{pmatrix}.
\]

The total-rate derivative is \(t=(1,1)\), giving

\[
G_{\mathrm{rate}}
={1\over2}t^Tt
=
\begin{pmatrix}
1/2&1/2\\
1/2&1/2
\end{pmatrix}.
\]

Exactly,

\[
G_{\mathrm{Poisson}}=G_{\mathrm{shape}}+G_{\mathrm{rate}}=I_2.
\]

Thus the second direction is not created by algebra. It is carried by the
physical rate record relative to exposure.

## Exposure calibration and profiling

Introduce a fractional common exposure perturbation \(\eta\). Its response in
the two Poisson means is \((1,1)^T\), the same direction as the total rate.
Let an independent exposure calibration contribute precision \(\pi\ge0\).
The nuisance-profiled source Gram is the Schur complement

\[
G_{\mathrm{profiled}}
=I_2-{1\over 2+\pi}
\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]

Its eigenvalues are

\[
1,
\qquad
{\pi\over2+\pi}.
\]

Consequently:

- if \(\pi=0\), exposure is unconstrained, the common-rate direction is
  removed exactly, and rank falls to one;
- if \(\pi>0\), the formal profiled rank is two;
- practical identification still requires the smallest eigenvalue to exceed
  the WP568--WP569 uncertainty and resolution threshold.

## Relational status of the exposure port

The calibrated exposure is a reference port. It defines a relative rate
experiment between counted detector records and an independently measured
luminosity or trial number. It does not reveal an absolute cross section of the
original shape-only experiment. Adding it changes the physical groupoid and
must be declared explicitly.

There are therefore two legitimate support completions:

1. retain a source-sensitive null or failed-selection record in the completed
   outcome alphabet;
2. retain the absolute selected count and join it to an independently
   calibrated exposure port.

Both are physical only when their interfaces and uncertainties are admitted.
Neither can be replaced by normalizing a simulation to the desired answer.

## Consequences for the flavor constructor

For a two-direction portal-score measurement, selected event bins may carry
rank two through rate plus shape even without an explicit null category. But
that authority disappears if luminosity, acceptance normalization, or total
trial exposure is freely profiled. The experiment must publish the rate
response, exposure calibration, their correlations, and the profiled smallest
Gram eigenvalue.

This is still a separator, not a selector or rigidifier. It descends under the
full weak-basis groupoid because the source entrance uses invariant physical16
paths and the exit uses physical event counts. The exposure port defines a new
relational experiment over the stabilizer groupoid, as required by the flavor
typing rules.

Current HHH analyses possess real luminosity calibration, but their public
releases do not supply the portal-score-conditioned rate-and-shape response
matrix. WP571 therefore identifies a physically available kind of reference
port without claiming that the existing HHH likelihood realizes the formal
four-point flavor derivative.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp571_poisson_exposure_rank_restoration.py

The generated result is
`research/flavor/results/wp571_poisson_exposure_rank_restoration.json`.
