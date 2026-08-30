# Symmetric support-cover measure jet

Work package: WP573  
Owner: marici.Figueiredo

## Correction inherited from WP572

For an amplitude affine in a source parameter, symmetric weights recover the
exact first derivative of the unnormalized event measure. At a zero of the
central amplitude, that first derivative also vanishes. The central
likelihood-ratio score is undefined, while nontrivial support can enter at
second order.

Therefore the source object is a local measure jet before it is a likelihood
score. This packet constructs one finite, source-authorized support cover and
factors both first- and second-order response into the experiment ports needed
by WP570--WP571.

## Frozen finite source family

Let the event carrier contain two selected cells \(A,B\) and one completed-
trial null cell \(N\). Freeze the affine amplitudes

\[
\mathcal A_A(\theta)=1+\theta,
\qquad
\mathcal A_B(\theta)=1,
\qquad
\mathcal A_N(\theta)=\theta.
\]

Their unnormalized weights are

\[
w_A=(1+\theta)^2,
\qquad
w_B=1,
\qquad
w_N=\theta^2.
\]

At \(\theta=0\), the measure, first derivative, and second derivative are

\[
\mu_0=(1,1,0),
\qquad
\dot\mu_0=(2,0,0),
\qquad
\ddot\mu_0=(2,0,2).
\]

Cell \(N\) is the exact quadratic support birth: its central weight and first
derivative vanish, but its second derivative is nonzero.

## Source-authorized dominating proposal

Before evaluating any event weights, freeze the symmetric source schedule

\[
\theta\in\{-h,0,h\},
\qquad h={1\over2}.
\]

Define the proposal measure

\[
\nu=\mu_{-h}+\mu_0+\mu_h.
\]

On \((A,B,N)\), its masses are

\[
\nu=\left({7\over2},3,{1\over2}\right),
\]

which are strictly positive on the union of the three source supports. Let
\(r_-,r_0,r_+\) be the three source-measure densities with respect to \(\nu\).
Then

\[
{r_+-r_-\over2h}
=\left({4\over7},0,0\right)
\]

is the density of \(\dot\mu_0\), and

\[
{r_+-2r_0+r_-\over h^2}
=\left({4\over7},0,4\right)
\]

is the density of \(\ddot\mu_0\). Multiplication by \(\nu\) recovers the
signed first derivative and the second-order support birth exactly, without
division by the central measure.

The proposal is authorized by its frozen symmetric source schedule, not by
observing which cell fails under central reweighting.

## Shape, rate, null, and exposure factorization

At the central point, the selected measure is \((1,1)\), with derivative
\((2,0)\). Its total selected rate and derivative are

\[
R=2,
\qquad
\dot R=2.
\]

The normalized selected shape and its derivative are

\[
p=(1/2,1/2),
\qquad
\dot p=(1/2,-1/2).
\]

Thus the selected signed response decomposes into a common-rate component and
a relative-shape component. The null cell has

\[
w_N=0,
\qquad
\dot w_N=0,
\qquad
\ddot w_N=2.
\]

It contributes no first-order score direction but is indispensable to the
second-order local family and to support completion.

To turn \(R\) into an observed count response, the experiment must join it to
the independently calibrated exposure port of WP571. Free profiling of that
port can erase the common-rate component; finite calibration precision can
retain it. This is a new relational rate experiment, not recovery of an
absolute quantity from shape alone.

## Two finite hostiles

### Quadratic support entry

The null amplitude \(\mathcal A_N(\theta)=\theta\) has no first-order central
score and no first-order signed response. Nevertheless every nonzero neighbor
has positive mass and \(\ddot w_N=2\). Any compiler that stores only the
first-order central likelihood score loses this local source behavior.

### Adaptive proposal

Suppose the central proposal is used first, the uncovered null cell is then
observed at neighboring hypotheses, and only afterward the proposal is enlarged
to the symmetric mixture. The enlarged measure dominates mathematically, but
its construction was selected from the failure. It has no source-response
authority for that test.

The exact temporal contract is:

- admitted: proposal schedule frozen before neighboring weights are evaluated;
- rejected: proposal chosen after the uncovered support is observed.

## Classification and remaining gate

WP573 supplies a support-safe local \(D_4\) measure-jet constructor on a finite
source family. It is source-derived and can feed a detector channel. It is a
separator input, not a selector or presentation rigidifier. The construction
uses a declared physical coupling path and event measures, so full weak-basis
descent passes. Exposure remains an explicit relational reference port.

The packet is a finite source theorem, not a physical HHH result. The remaining
gate is a portal-complete source path, a frozen dominating event proposal,
shower and detector transport, completed null/exposure records, covariance,
and robust resolution in one publication-bound instrument.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp573_symmetric_support_cover_measure_jet.py

The generated result is
`research/flavor/results/wp573_symmetric_support_cover_measure_jet.json`.
