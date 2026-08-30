# Discrete-CP vacuum pictures rigidify phases but do not yet select physical16 (WP56)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

## Candidate

The declared flavor source sketches two UV pictures:

- a complex scalar with a (mathbb Z_4) potential and real/imaginary vacua;
- equal-magnitude (mathbb Z_8) flavon vevs whose phases are multiples of
  (pi/4).

The latter's displayed left-hand side evaluates exactly as

\[
i\frac{1-e^{i\pi/4}}{1+e^{i\pi/4}}=\tan(\pi/8).
\]

The extracted source prints (i\tan(\pi/8)) on the right. Exact cyclotomic
algebra gives the real value above, so WP56 preserves this as a nonzero source
residual rather than silently absorbing the factor of (i). The intended
simple-angle magnitude remains clear. This is independently motivated
discrete-phase algebra rather than a scalar fit performed after seeing data.

## Source-completeness gate

The source calls these "several simple pictures", introduces the first with
"for instance", and explicitly defers the theoretical possibilities to future
work. It does not declare:

- a complete flavon action or potential;
- coefficients and a vacuum-selection rule;
- a unique vacuum orbit;
- a map from that orbit to the full Yukawa quotient;
- a physical instrument for the proposed operation.

Consequently there is no executable source operation whose image or fixed
locus can be computed on `physical16`.

## Descent and classification

The exact (mathbb Z_8) identity fixes a relation among sparse Yukawa entries.
It is therefore a presentation rigidifier. The existing exact (3/5,4/5)
(U(3)_Q) transformation preserves every audited physical invariant while
destroying the sparse support and changing its loop phase. The proposed phase
datum does not descend by itself.

Classification: **rigidifier, not selector**. Its contextual classes are
fixed-phase classes of sparse presentations, not proper classes of the
physical quotient.

The smallest exact falsifier is the same weak-basis orbit counterexample. A
progressive successor must supply a complete UV action, select a vacuum orbit
before fitting, and give a weak-basis-invariant map from that orbit to a proper
`physical16` family. A discrete phase assigned directly to chart entries is
insufficient.

## Verification

`uv run --with sympy python research/flavor/checkers/wp56_spontaneous_cp_selector_gate.py`
writes `research/flavor/results/wp56_spontaneous_cp_selector_gate.json`.
