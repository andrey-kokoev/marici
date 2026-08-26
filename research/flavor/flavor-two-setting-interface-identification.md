# Two-setting interface identification theorem

Work package: WP577  
Owner: marici.Figueiredo

## Scope

WP576 leaves one missing common-frame map from the invariant portal response
coordinates ((r,q)) to a completed detector record. This packet asks for the
smallest local calibration design that can identify that map under a source-
frozen affine-response grammar.

Let (K) be a (3\times2) completed detector tangent. Probability
normalization requires

\[
\mathbf 1^T K=0.
\]

For a prepared source perturbation (x\in\mathbb R^2), the calibrated local
response is (Kx).

## One-setting obstruction

Freeze one perturbation (x=(1,c)^T). Its transverse covector is

\[
n=(-c,1)^T,
\qquad
n^Tx=0.
\]

For any nonzero completed-record tangent (w) satisfying
(mathbf1^Tw=0), define

\[
H=wn^T.
\]

Then (H\ne0), (mathbf1^TH=0), and (Hx=0). Consequently (K) and
(K+H) are distinct normalized detector transports that agree exactly on the
entire calibrated setting. One source tangent cannot identify the interface.

The smallest rational hostile uses

\[
x=(1,1)^T,
\qquad
w=(1,-1,0)^T,
\qquad
n=(-1,1)^T.
\]

With WP574's response (D), the transports (D) and (D+wn^T) agree on
(x) but disagree on the transverse perturbation (n).

## Two-setting sufficiency

Let (X=(x_1\ x_2)) collect two prepared perturbations and let
(Y=(Kx_1\ Kx_2)=KX) be their calibrated completed responses. If

\[
\det X\ne0,
\]

then

\[
K=YX^{-1}
\]

is unique. Thus two noncollinear settings are necessary and sufficient for
local identification of a two-column affine transport. This statement does
not grant the affine grammar; that grammar and its domain must be frozen from
the source and detector model before calibration.

## Portal typing

WP576 proves that the portal parameter surface has two independent invariant
tangents for (z>0). WP577 adds the detector-interface requirement: the
experiment must prepare or simulate two independently declared portal
perturbations, transport both through the same shower, detector, selection,
and completed-record pipeline, and calibrate the resulting response columns
in one frame.

Two Monte Carlo cards can identify a research-surrogate (K). They become a
physical flavor instrument only when the generator-to-detector chain is
publication-bound and its calibration, covariance, support, and nuisance
model are admitted. A scan along one correlated portal tangent leaves the
exact transverse completion above.

The construction descends under the full weak-basis groupoid when (x_1,x_2)
are perturbations of the invariant ((r,q)) coordinates. No reference port is
required for interface identification itself. If a selected-rate column is
used, the exposure port remains the relational experiment of WP571--WP574.

## Classification

This is an interface-identification theorem, neither a selector nor a
presentation rigidifier. It refines the contextual partition into:

- zero or one independent calibrated source setting: nonidentifiable (K);
- two noncollinear settings under a frozen affine grammar: unique local (K);
- unique surrogate (K) without publication binding: research instrument;
- publication-bound, uncertainty-stable (K): physical flavor probe.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp577_two_setting_interface_identification.py

The generated result is
`research/flavor/results/wp577_two_setting_interface_identification.json`.
