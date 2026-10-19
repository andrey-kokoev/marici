# Context-indexed observer: exact backward transport without quotient descent

Target: `rh:channel-carrier-source-map`, remains open.
Predecessor: `transverse-gaussian-bridge-v1.md`; its fixed-contraction rejection is retained.
Checker: `research/voevodsky/checkers/check_context_indexed_observer.py`.
Receipt: `research/voevodsky/results/context-indexed-observer-v1.json`.
Run: `uv run research/voevodsky/checkers/check_context_indexed_observer.py`.

## Contract and convention

Keep the full additive tempered source T, its supplied marked coordinate, original geometric/off-axis record, and the ordered generator word. A query is a Schwartz test psi, initially of the form phi(x) g(y) if a selected-axis observer is desired. More general transported tests are allowed. Do not replace this state by its one scalar readout.

Use the COMPLEX BILINEAR distribution/test pairing T(psi), without conjugating psi. For regular distributions it is the integral of f psi. This convention differs from the Hermitian L2 pairing: Fourier's transpose here is F, whereas its Hermitian adjoint is F^-1. The distinction matters for phases and is not an assertion that F is Hermitian self-adjoint.

For every continuous declared generator A define the test transpose A^t by

    (A T)(psi) = T(A^t psi).

Under Ff(xi)=integral exp(-2pi i x xi)f(x)dx, translations T_b f(x)=f(x-b), modulation M_c f(x)=exp(2pi i c x)f(x), and positive Gaussian multiplication H_t,d:

    F^t=F,  T_b^t=T_-b,  M_c^t=M_c,  H_t,d^t=H_t,d.

All preserve Schwartz space; their distributional extensions are continuous. No negative heat or ordinary log-tempered domain is introduced.

## Ordered continuation theorem

Let A1 act first and An last, so the forward state is An ... A1 T. The same observation is obtained from the retained source by

    (An ... A1 T)(psi) = T(A1^t ... An^t psi).

Operationally apply An^t to the final test FIRST, then work backwards. This follows by induction from the transpose definition, not from the finite examples. It supplies a generator-level composition law for an OBSERVER on a retained source. It is not a quotient operation on a fixed readout, and it does not derive these analytic generators from the twelve-arrow native clock.

For a coordinate permutation sigma, use (P_sigma T)(psi)=T(psi composed with sigma). Transport the mark and coordinate-indexed parameters with the state; transporting a state while freezing a marked test generally changes its observation. This addresses the relabelling square at the analytic observer level, not a new operation on the original geometric archive.

## Replay of the discarded transverse distinction

The preceding hostile was h=exp(pi) delta_e1-delta_0, observed with g(y)=exp(-pi||y||²). Initially h(g)=0. To observe AFTER full unit heat, query the retained h against H_1 g instead:

    h(H_1 g)=exp(-pi)-1.

This matches direct heat evolution exactly. Zero and h remain indistinguishable by the old fixed query but distinguishable by this new query. No information has been recovered from zero; it was available because the full source was retained. An archive inaccessible to the observer would not suffice.

For full isotropic heat, both longitudinal and transverse tests change. Updating only g while leaving a nontrivial longitudinal test unchanged would omit part of the operation. For Fourier/heat words the transpose order also changes Gaussian widths and normalization. Neither a frozen transverse flag nor a scalar renormalization substitutes for the transported test.

## Exact replay and boundaries

The checker evaluates all 84 words of lengths one through three in F,T,M,H on complex Gaussian densities/tests using exact rational parameters and symbolic Gaussian integration. It compares independent forward-state and backward-test computations, rejects wrong transpose order and translation sign, replays the old kernel hostile, and tests a two-coordinate transported-mark square with a frozen-mark counterexample.

The general distributional result rests on the written continuity/transpose argument; Gaussian samples do not prove it. This is not reconstruction of arbitrary distributions from finitely many probes, a finite-state implementation, a claim of computability for all tempered inputs, or a laboratory construction.

## Net disposition and next source obligation

Constructed at the declared analytic scope: a context-indexed observation protocol preserving ordered continuation when the full source remains accessible. The fixed-quotient no-go is untouched. `channel-carrier-source-map` is still open: no single reviewed native constructor has yet tied the canonical full channel/geometric operations to the original twelve-arrow/retained-history operations.

The next nonredundant task is an explicit source-access contract: name the shared seed and mark, specify which observer queries the retained-history representation can actually execute, and supply the maps/update laws for its geometric/off-axis archive. Classify each generator as native, newly admitted, or unsupported. Bind this protocol to those maps before requesting a scoped source-map verdict. No further fixed-contraction search or Gaussian replay is needed for that decision.
