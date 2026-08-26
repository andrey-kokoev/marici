# Four-point score-channel constructor

Work package: WP567  
Owner: marici.Figueiredo

## Deutsch question

WP566 proved that no currently admitted end-to-end path measures the formal
four-point flavor derivative. The constructive successor is not another fitted
quartic limit. It is the following preregistered question:

What detector-level difference is forced by a frozen source score and an
independently calibrated detector channel?

This packet gives the exact answer for a finite event model.

## Source and detector typing

Let \(X\) be a finite source-event space and \(Y\) a finite detector-record
space. Near a frozen source point, write

\[
p_\theta(x)=p_0(x)\bigl(1+\theta s(x)\bigr)+O(\theta^2),
\qquad
\sum_x p_0(x)s(x)=0.
\]

Here \(s\) is the source-derived four-point score. It must be computed from a
source action or source event generator before detector data are used.

Let \(K(y\mid x)\) be a column-stochastic detector channel, frozen through an
independent calibration. The detector distribution and its derivative are

\[
q_0(y)=\sum_x K(y\mid x)p_0(x),
\qquad
\dot q(y)=\sum_x K(y\mid x)p_0(x)s(x).
\]

Whenever \(q_0(y)>0\), the detector score is forced to be

\[
t(y)={\dot q(y)\over q_0(y)}
=\mathbb E_{0}[s(X)\mid Y=y].
\]

This conditional expectation is the missing parallelization constructor. It
does not fit a detector derivative from the desired source answer. It composes
two independently typed objects: a source score and a calibrated channel.

## Exact faithfulness criterion

The detector Fisher information in this direction is

\[
I_Y=\sum_y {\dot q(y)^2\over q_0(y)}.
\]

Therefore

\[
I_Y>0
\quad\Longleftrightarrow\quad
K\,\operatorname{diag}(p_0)s\ne0.
\]

The law of total variance also gives

\[
I_X-I_Y
=\mathbb E_0\!\left[\operatorname{Var}(s(X)\mid Y)\right]\ge0.
\]

Thus detector transport can preserve or erase the source direction but cannot
create Fisher information about it. The first nonfaithful arrow is precisely
the kernel of the calibrated conditional-expectation map.

## Hostile calibration pair

Take two equally likely source cells with score

\[
p_0=\left({1\over2},{1\over2}\right)^T,
\qquad
s=(1,-1)^T.
\]

Compare three exact detector channels:

\[
K_{\mathrm{keep}}=
\begin{pmatrix}1&0\\0&1\end{pmatrix},
\qquad
K_{\mathrm{noisy}}=
\begin{pmatrix}3/4&1/4\\1/4&3/4\end{pmatrix},
\qquad
K_{\mathrm{erase}}=
\begin{pmatrix}1/2&1/2\\1/2&1/2\end{pmatrix}.
\]

All three give the same baseline detector distribution
\(q_0=(1/2,1/2)^T\). Their directional Fisher informations are respectively

\[
I_Y=1,\qquad {1\over4},\qquad 0.
\]

Consequently baseline agreement cannot calibrate the source response. A
truth-conditioned or otherwise source-labelled calibration of \(K\) is
required. This is the smallest exact falsifier of any attempt to infer the
detector derivative from the nominal histogram alone.

## Experiment contract

A future four-point flavor measurement can now be preregistered without
choosing its detector completion after seeing the answer:

1. freeze a physical16 source path and compute its normalized event score
   \(s(x)\);
2. freeze source-event cells with support adequate for that score;
3. calibrate \(K(y\mid x)\) independently, including null and failed-selection
   outcomes;
4. compute \(\dot q=K\operatorname{diag}(p_0)s\) before examining the signal
   fit;
5. publish the detector metric or nuisance likelihood used to test \(\dot q\);
6. accept sensitivity only if the uncertainty-supported Gram value remains
   positive under calibration completion and nuisance profiling.

The source-generated score plus independently calibrated channel is a probe,
not a selector. If it is nonzero it separates nearby physical points along the
declared source direction. It does not choose the numerical source value.

## Present status

This theorem supplies the missing mathematical interface constructor and a
concrete experimental contract. It does not retrospectively turn ATLAS or CMS
into a flavor measurement: neither current release supplies a portal-score-
conditioned detector channel with the required provenance and uncertainty
support.

All variables are physical event probabilities and invariant coupling paths,
so the construction descends under the full weak-basis groupoid. No reference
port is added. The remaining physical gate is an independently calibrated,
publication-bound \(K\) on the portal source support, including its uncertainty
model and detector instrument.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp567_four_point_score_channel_constructor.py

The generated result is
`research/flavor/results/wp567_four_point_score_channel_constructor.json`.
