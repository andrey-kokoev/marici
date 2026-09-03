# Physical16 soft-port-channel gate: WP1243

## Question

Can a Physical16 soft-port channel be realized by the existing event cell?

## DPC resolution

- **Problem:** realize soft and vector momentum ports in actual Physical16
  production/decay channels and derive source-to-detector gain.
- **Bold conjecture:** the common-source event cell carries the
  source-derived vector threshold ratio, but a physical soft-port channel
  requires a new channel-dependent reweighting map.
- **Named rivals:** vector-ratio event-cell constructor; pole-event
  relabeling; equal-weight partition; localized-branch identification;
  channel-dependent reweighting map.
- **Risky consequences:** ratio 4 reconstructs \(L=1/5\) and \(g=1\) on
  the atom cell; unit ratio leaves exact \(S\) and \(D\) gaps; a same-rate
  \(g=1/2\) laundering attempt is separated by the coherent row; 23 pole
  atoms cannot satisfy the \(3d/2\) event support and six event atoms
  cannot be an equal partition; no assignment of the six localized SU(6)
  branches satisfies the WP1052 event constraints.
- **Strongest falsification attempt:** ratio and atom relabeling hostiles
  fail, while channel weights, detector/monitor/cross labels, null
  outcomes, and actual Physical16 production/decay channels remain
  underived.
- **Exact residual:** derive a source-dynamical channel-dependent
  reweighting map from pole atoms to event atoms, with labels, nulls, and
  soft/vector port realization in one Physical16 frame.
- **Disposition:** accept the vector-ratio event branch conditionally;
  reject relabeling as a soft-port realization.

Checker: `research/flavor/checkers/wp1243_physical16_soft_port_channel_gate.py`

Result: `results/wp1243_physical16_soft_port_channel_gate.json`
