# Two-direction score singular gate

Work package: WP569  
Owner: marici.Figueiredo

## Scope and typing

WP568 established an exact robust radius test for one source-score direction.
Nima accepted that result as a prospective separator constructor and required
the detector metric and uncertainty provenance to remain independently frozen
inputs. This packet extends the result to the two-error experiment requested
by WP232. It does not assert that a current HHH release instantiates the
constructor.

Let \(D\) be the detector response matrix whose columns are the transported
tangents of two independently declared source perturbations. Let \(W\) be a
positive detector metric calibrated independently. Define

\[
A=W^{1/2}D.
\]

Calibration and nuisance completion perturb the response by \(E\). The
admitted uncertainty size is the operator norm

\[
\left\|W^{1/2}E\right\|_2\le\rho.
\]

This norm and its radius must be obtained from the detector calibration and
nuisance model; they are not tunable significance parameters.

## Robust rank theorem

Weyl's singular-value inequality gives

\[
\sigma_{\min}\!\left(W^{1/2}(D+E)\right)
\ge
\max\!\left(\sigma_{\min}(A)-\rho,0\right).
\]

Equivalently, the smallest eigenvalue of the completed Gram matrix obeys

\[
\lambda_{\min}\!\left((D+E)^TW(D+E)\right)
\ge
\max\!\left(\sigma_{\min}(A)-\rho,0\right)^2.
\]

Therefore rank two is certified throughout the admitted uncertainty set when

\[
\rho<\sigma_{\min}(W^{1/2}D).
\]

The smallest singular value, not the two column norms separately, is the
relevant gate. Two individually visible responses can become collinear under
an admitted completion.

## Exact probability-conserving hostile pair

Use three detector outcomes, two source directions, and \(W=I_3\):

\[
D=
\begin{pmatrix}
1&0\\
-1&1\\
0&-1
\end{pmatrix}.
\]

Both columns sum to zero, so they are probability tangents. The Gram matrix is

\[
D^TD=
\begin{pmatrix}2&-1\\-1&2\end{pmatrix},
\]

with eigenvalues \(1,3\). Hence \(\sigma_{\min}(D)=1\).

The weakest right singular direction is proportional to \((1,1)^T\), and its
left response is proportional to \((1,0,-1)^T\). An antiparallel rank-one
perturbation with operator norm \(1/2\) leaves the completed Gram smallest
eigenvalue exactly \(1/4\). At the critical radius \(1\), the corresponding
perturbation makes the two completed columns exact negatives. Each column
remains nonzero, but the response rank falls from two to one and the Gram
determinant vanishes.

Thus the critical completion is a smallest exact falsifier of columnwise
sensitivity as evidence for joint faithfulness.

## Experimental contract

A two-error flavor experiment has identification authority only if it
publishes, in one common frame:

1. two independently source-derived score directions;
2. the calibrated detector response matrix \(D\), including null outcomes;
3. the independently fixed metric \(W\);
4. the propagated operator-norm uncertainty radius or a stronger uncertainty
   set;
5. a strictly positive certified lower bound on the smallest completed Gram
   eigenvalue;
6. support, finite-resolution, and nuisance-completion assumptions.

This gate separates two local source directions when it passes. It does not
select a numerical source value and does not identify a unique UV constructor
beyond the declared source domain.

## Present status

The theorem supplies the exact robust rank-two criterion sought in WP232. It
is suitable prospectively or for an admitted surrogate whose calibration
inputs are frozen independently. Current ATLAS and CMS HHH releases do not
publish the portal-score response matrix and common-frame uncertainty operator
needed to evaluate it.

The construction uses invariant physical16 source paths and detector
probability tangents, so full weak-basis descent passes. No reference port is
added. The remaining physical-instrument gate is an executed two-error portal
experiment with publication-bound \(D\), \(W\), covariance, nuisance response,
and detector resolution.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp569_two_direction_score_singular_gate.py

The generated result is
`research/flavor/results/wp569_two_direction_score_singular_gate.json`.
