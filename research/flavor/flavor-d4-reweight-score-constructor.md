# D4 reweight score constructor

Work package: WP572  
Owner: marici.Figueiredo

## Question

WP567 requires a source-derived event response before detector calibration is
used. WP565 identified a public multi-Higgs UFO model, but the frozen
repository itself contains no event sample, reweight card, derivative routine,
or score basis. This packet asks whether the quartic event score is nonetheless
executable through an admitted generator operation.

The answer is positive at leading order on common phase-space support.
MadGraph's official reweight module assigns a generated event the
matrix-element weight of a new parameter hypothesis. The operation is
source-side and does not use detector data.

Sources:

- public model: https://gitlab.com/apapaefs/multihiggs_loop_sm at revision
  `788431390ded97d4b44c25a0013b184053b4aaad`;
- model paper: https://arxiv.org/abs/2312.13562;
- official reweight documentation:
  https://cp3.irmp.ucl.ac.be/projects/madgraph/wiki/Reweight.

## Frozen model facts

The restricted five-parameter UFO exposes
\((D_3,D_4,CT_1,CT_2,CT_3)\). Its `D4` external parameter is BSMINPUTS entry
997. The coupling file defines the modified four-Higgs vertex linearly in
\(D_4\), and the vertex file uses that coupling only at the four-Higgs vertex.

For connected leading-order \(gg\to hhh\) graphs, a four-Higgs vertex can
occur at most once. Therefore, with all other generator parameters frozen, the
event amplitude is affine:

\[
\mathcal M_x(c)=a_x+c b_x,
\qquad c=D_4.
\]

Its event weight is a quadratic polynomial,

\[
w_x(c)=|a_x+c b_x|^2.
\]

## Exact three-weight derivative

For any nonzero step \(h\), quadraticity gives the identity

\[
{w_x(c+h)-w_x(c-h)\over2h}=w_x'(c).
\]

Thus this is not a finite-difference approximation. Central and two symmetric
MadGraph reweights determine the exact local derivative of the unnormalized
event measure. Where \(w_x(c)>0\), it can be represented by the normalized
source score

\[
s_x(c)={w_x'(c)\over w_x(c)}
-{\sigma'(c)\over\sigma(c)},
\]

where the second term centers the score over the generated event ensemble.
The signed-measure derivative exists before this division and remains the
authoritative source response when the score coordinate is unavailable.
The total-rate derivative and normalized shape score together provide the
WP571 rate-and-shape decomposition.

A minimal prospective reweight card around \(c=1\), with \(h=1/2\), is:

    launch --rwgt_name=d4_minus
      set BSMINPUTS 997 0.5
    launch --rwgt_name=d4_plus
      set BSMINPUTS 997 1.5

The central event weight is supplied by the generation hypothesis. The card is
an executable specification for a compatible MadGraph installation; it is not
claimed to have been run in the current environment.

## Support theorem and hostile event

Matrix-element reweighting is faithful only where the baseline sample covers
the new hypothesis. If \(w_x(c)=0\), the ratio

\[
R_x(c\pm h)={w_x(c\pm h)\over w_x(c)}
\]

is undefined even when the neighboring hypothesis has nonzero weight.

The smallest exact hostile amplitude is

\[
\mathcal M(c)=1-c
\]

at \(c=1\). The central weight vanishes, while both symmetric neighboring
weights equal \(h^2\). The exact first derivative of the weight also vanishes,
while its second derivative equals two. Thus the central likelihood-ratio
score is undefined, the first-order signed response is zero, and the nontrivial
support birth occurs at second order. A first-order score cannot represent this
second-order entry.

Therefore a support-safe local measure-jet constructor requires either:

- a baseline hypothesis with support covering every admitted variation;
- a source-generated mixture of baseline samples whose union covers the
  variation family; or
- direct generation at the required hypotheses followed by a declared common
  phase-space integration.

Support coverage must be verified independently of the desired answer. A
source-authorized symmetric mixture of the central and neighboring hypotheses
can dominate their union without dividing by the central weight.

## Portal typing

The exact constructor supplies the partial \(D_4\) event score. It does not by
itself supply the full trace-adjoint/Higgs portal score. A physical portal path
also transports correlated changes in \(D_3\), \(CT_1\), widths, branching
fractions, and potentially heavy-state amplitudes. The complete score is a
source-derived chain-rule combination of all those generator-coordinate
scores.

Hence WP572 is progressive but bounded:

- the quartic source-side signed derivative is executable in principle at LO;
- a likelihood score exists only on an admitted domination domain;
- it is a separator input, not a selector or rigidifier;
- common-support coverage is an exact source-generation gate;
- the portal tangent and detector channel remain uninstantiated.

All generator coordinates represent physical couplings after the declared
portal map, so weak-basis descent passes at the entrance. No reference port is
added by reweighting. Exposure calibration remains the relational port of
WP571.

## Present instrument gate

The public model repository has no frozen HHH reweight card, HHH event sample,
score output, support audit, shower/detector transport, or likelihood join.
Generic MadGraph capability makes the signed-response task executable, but does
not make the current ATLAS or CMS HHH result a flavor measurement.

The next physical object must bind:

1. a portal-complete generator path;
2. a frozen support-covering event mixture;
3. exact signed event-weight derivatives and, where dominated, scores;
4. shower and detector transport;
5. completed outcome or exposure calibration;
6. nuisance covariance and robust smallest-singular-value resolution.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp572_d4_reweight_score_constructor.py

The generated result is
`research/flavor/results/wp572_d4_reweight_score_constructor.json`.
