# Full multichannel bridge: Gaussian transverse contraction fails heat

Target: `rh:channel-carrier-source-map`, still open.
Checker: `research/voevodsky/checkers/check_transverse_gaussian_bridge.py`.
Receipt: `research/voevodsky/results/transverse-gaussian-bridge-v1.json`.
Run: `uv run research/voevodsky/checkers/check_transverse_gaussian_bridge.py`.

## A concrete source-map candidate

Let D>=2, fix the supplied marked coordinate x, and write the transverse coordinates as y in R^(D-1). Work in the ADDITIVE tempered distribution space, not the raw log-radial rigging. Set g(y)=exp(-pi||y||²) and define

    (Q_g T)(phi) = T(phi tensor g).

The Schwartz map phi -> phi tensor g is continuous, so this is a well-defined continuous distributional contraction. It is not pointwise restriction of an arbitrary distribution. Parameters, mark, original source and off-axis archive remain explicitly retained.

This candidate has a genuinely useful property: F g=g in the declared self-dual normalization. By the tensor Fourier identity and duality,

    Q_g F_D = F_1 Q_g.

Both transverse delta_0 and transverse constant 1 pair to one against g. Hence this map compares the alternating ambient Fourier charts of a marked-axis comb with the selected one-dimensional Fourier orbit. This is a constructed mathematical Fourier bridge, not inferred from dimensions or an L2 restriction to a measure-zero subspace.

## Exact continuation hostile

Use the finite two-atom tempered packet, with longitudinal delta_0 suppressed in notation,

    h = exp(pi) delta_(y=e1) - delta_(y=0).

Then Q_g h=0. After full unit isotropic heat, multiplication by exp(-pi(x²+||y||²)),

    Q_g H_1,D h = (exp(-pi)-1) delta_(x=0) != 0.

Thus the kernel of Q_g is not invariant under a licensed full source heat operation. There cannot be ANY linear descended heat operator L on the one-dimensional quotient satisfying Q_g H_1,D=L Q_g on this domain: its right side would vanish on h. Adding a scalar normalization of the target heat cannot fix kernel escape.

This is a retained-data failure in a proposed coarse reader, not an instability or numerical approximation. Both h and zero have the same present selected readout and different next readouts under the same source operation. Keeping h in an archive does not make the quotient alone predict its continuation.

## General fixed-contraction obstruction

For any fixed g in S(R^(D-1)), suppose Q_g H_t,D=H_t,1 Q_g for some fixed t>0 on ALL tempered distributions. Testing delta_(0,y) gives

    exp(-pi t||y||²) g(y) = g(y).

For every y!=0 the exponential factor differs from one, so g(y)=0. Continuity then forces g(0)=0. Therefore g=0. No nonzero fixed Schwartz transverse contraction intertwines those unchanged full/longitudinal heat actions. This written argument is stronger than the one Gaussian fixture, but does not exclude restricted source domains, a varying context, or retention of the full transverse state.

The checker verifies the explicit kernel packet exactly and the transverse Gaussian normalization factors at D=2,3,20,54. It does not promote these finite tests into a formal proof of the Schwartz-space theorem.

## Why the old pointed-axis result survives

On an axis-supported packet T tensor delta_0, full isotropic heat restricts to the longitudinal heat and no transverse information is lost. That is the earlier explicitly narrowed task. After ambient Fourier the transverse factor is constant, not delta_0; full transverse heat turns it into a Gaussian. Against g, its extra factor at time t is (1+t)^(-(D-1)/2), whereas the delta chart retains factor one. A reader treating both charts as a scalar one has therefore forgotten a state needed by the next heat step.

The pointwise axis selection and its licensed domain are not refuted. What fails is extending a Fourier-compatible contraction to full ambient heat without retaining its new transverse state. The supplied mark and domain restriction cannot be omitted.

## Honest repair and remaining gate

Retain a changing transverse test/context: under heat, the pulled-back test is H_t g; under Fourier, it is Fg. Then a context-indexed observer can keep the exact pairing history. Alternatively keep the full transverse distribution in the source. Neither option is a fixed one-dimensional quotient of every full multichannel operation.

A subsequent common-source proposal must say which repair it uses and preserve the original off-axis/geometric archive and operation words. The twelve-arrow native cycle still needs its actual restricted embedding; adding continuous analytic operations is not proof that they are native or physical. This failed candidate does not close the broad source-map node or alter the separately rejected Weil-form comparison.

Next nonredundant task: test a context-indexed observer with explicit backward test transport and composition order, rather than trying another fixed scalar contraction or repeating the old axis-only Fourier square.
