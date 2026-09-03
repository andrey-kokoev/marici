# Source-derived actuator-normalization gate: WP1229

## Question

Can bounded control derive source-authorized actuator normalization?

## DPC resolution

- **Problem:** derive actuator normalization or cost/support fixing the
  admissible target scale.
- **Bold conjecture:** a bounded Chebyshev controller or formal rank-two
  actuator map fixes source-derived actuator normalization.
- **Named rivals:** assumed \(l_\infty\) budget; rank-one actuator; formal
  rank-two completion; zero-drift \(Q\)-direction family; zero-coefficient
  and transverse RG lifts.
- **Risky consequences:** the joint Chebyshev radius is \(B/5489\) only
  after \(B\) is assumed; rank-one actuation leaves the \(R\) direction
  unreachable; the rank-two completion is mathematical only; zero drift
  preserves \(R\) leaves; the same physical RG projection permits bracket
  ranks one and two.
- **Strongest falsification attempt:** every route either assumes the
  control norm, lacks transverse access, or fails to lift RG data to the
  coefficient plane.
- **Exact residual:** source-derived common-substrate RG-to-\((Q,R)\) lift,
  transverse actuator, positive command-cost Gram, and calibrated
  closed-loop error.
- **Disposition:** reject bounded/formal control as actuator authority;
  select common-substrate RG-lift rival.

Checker: `research/flavor/checkers/wp1229_source_derived_actuator_normalization_gate.py`

Result: `results/wp1229_source_derived_actuator_normalization_gate.json`
