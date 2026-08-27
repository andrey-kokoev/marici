# UV Fixed-Point Portal and Relevant Clock Fiber

## Question

Can an interacting ultraviolet fixed point internalize WP800's portal and make
its sign, magnitude, RG basin, threshold survival, and physical readout jointly
unavoidable?

## Claim boundary

This packet establishes an exact structural result for a minimal fixed-point
normal form. It does not claim that a known gauge--Yukawa theory realizes the
required Standard Model flavor source. The normal form isolates what an
interacting fixed point can and cannot authorize before any model-specific
numerical fit.

## Dimensionless prediction

Put the Standard Model flavor operator and the portal vertex in one microscopic
gauge--Yukawa action. Near an isolated ultraviolet fixed point, let the portal
deviation obey

\[
\frac{d\,\delta p}{ds}=2\delta p,
\qquad
\delta p(s)=c_p e^{2s}.
\]

Reaching the fixed point as the ultraviolet coordinate (s\) tends to infinity
forces (c_p=0). In this precise sense an ultraviolet-repulsive portal
direction is predicted rather than tuned. This is the first candidate in the
programme that can internalize and fix a dimensionless portal coefficient.

The result is conditional: a concrete anomaly-complete chiral theory must
actually possess the fixed point, and the portal direction must remain outside
its ultraviolet critical surface after higher orders and threshold completion.

## Relevant-clock obstruction

A mass deformation has the opposite normal form,

\[
\frac{dm}{ds}=-m,
\qquad
m(s)=c_m e^{-s}.
\]

Every finite (c_m) reaches the same ultraviolet fixed point. Thus ultraviolet
completion does not select the trajectory coordinate (c_m). The exact pair
(c_m=1) and (c_m=4) has the same ultraviolet endpoint but thresholds in the
ratio (1:2). Fixed-point data can predict dimensionless ratios; an absolute
mass requires a source-derived clock or a relational calibration standard.
Dimensional transmutation does not evade this statement: it exchanges a
dimensionless boundary datum for an RG-invariant scale.

## Orientation obstruction

The minimal even fixed-point equation

\[
p^2=1
\]

selects the magnitude but retains (p=+1) and (p=-1). An intrinsic even
probe sees both as (p^2=1). A signed readout distinguishes a prepared branch,
but branch discrimination is not source selection. A physical relative sign
requires a rephasing-invariant cycle, and selecting it requires an
orientation-odd source term or boundary condition whose own orientation is not
inserted as a reference port.

## Probe partition

Use the faithful constructor coordinate ((p,m,\alpha)), where (alpha) is the
detector calibration. The intrinsic ultraviolet probe has Jacobian

\[
J_{\rm UV}=\begin{pmatrix}1&0&0\end{pmatrix}.
\]

It leaves a two-dimensional contextual kernel. Adding the threshold
(\sqrt m) and calibrated detector response (alpha p) gives a full-rank
Jacobian at ((1,1,1)), but those rows are authorized only by a massive
completion and a detector experiment. Formal availability of the coordinates
does not construct either instrument.

## Deutschian disposition

Asymptotic safety is a candidate explanatory principle for the dimensionless
portal only. It becomes a hard-to-vary explanation of the complete flavor
record only if one source simultaneously supplies:

1. an isolated chiral fixed point with no portal direction on its ultraviolet
   critical surface;
2. an orientation-odd invariant selecting one physical sign branch;
3. a unique massive vacuum or a source-generated relational clock selecting
   the threshold scale;
4. threshold matching that preserves the portal prediction;
5. an experimentally calibrated map to the faithful physical16 quotient.

Without items 2--5, the construction explains why a dimensionless coupling
could be predicted while merely relocating the unexplained data.

## Smallest exact falsifiers

- Relevant-clock falsifier: (c_m=1) and (c_m=4) share the ultraviolet
  endpoint and have distinct thresholds.
- Orientation falsifier: (p=+1) and (p=-1) satisfy the same even fixed-point
  equation.
- Instrument falsifier: (alpha=1) and (alpha=2) preserve the source but
  change the detector response.

## Disposition

Progressive for dimensionless magnitude, negative for the complete portal.
The next bounded candidate must test an anomaly-complete chiral gauge--Yukawa
fixed point together with its critical exponents. It is admissible only if the
flavor portal is irrelevant, while every parameter controlling its sign,
massive vacuum, and detector response is either internally selected or named
as an unresolved source coordinate.

Verification:

- checker: research/flavor/checkers/wp801_uv_fixed_point_relevant_clock_fiber.py
- generated result: research/flavor/results/wp801_uv_fixed_point_relevant_clock_fiber.json
- exact invocation: uv run --with sympy python research/flavor/checkers/wp801_uv_fixed_point_relevant_clock_fiber.py
- gauge--Yukawa asymptotic safety: [Litim and Sannino](https://arxiv.org/abs/1406.2337)
- effective predictivity and critical trajectories: [Held](https://arxiv.org/abs/2003.13642)
