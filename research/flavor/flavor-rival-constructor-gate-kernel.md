# Rival constructor gate kernel

Owner: `marici.Figueiredo`.

## Question

WP179 asked for the constructor-level falsifier:

Can two source constructors share the same low-energy flavor packet while
authorizing different recurrence-growth gate tuples?

## Hostile pair

Both constructors are frozen to the same low-energy packet:

- `physical16_id = P_fit_common`;
- `measured10_id = M_fit_common`;
- same low-energy selector architecture.

They differ only in the source-authorized recurrence gate:

- `C_rect_exact`: rectangular quotient domain, `K=64`, `tau=0`, radius `4`;
- `C_hnf_noisy`: arbitrary HNF quotient domain, `K=64`, `tau=1`, radius `6`.

Both gate tuples are formally consistent by WP177. They are not the same
constructor story.

## Disposition

This is the requested Deutsch-Popperian falsifier. The low-energy flavor packet
does not uniquely determine the recurrence-growth gate tuple. Therefore
recurrence growth is not yet a unique source explanation; it is an additional
constructor-sensitive probe.

The gate can still be physically useful. If a source constructor independently
authorizes one of the tuples, recurrence growth can test that constructor. But
the low-energy fit alone cannot choose between the rival constructors.

## Exact checker

- Checker: `checkers/wp180_rival_constructor_gate_kernel.py`
- Result: `results/wp180_rival_constructor_gate_kernel.json`

The checker verifies same `physical16`, same measured-ten readout, different
authorized gate tuples, and formal consistency of both gates.

## Calibration

- Pre excitement: `10/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `10/10`.
- Post excitement: `10/10`.
- Post confidence: `10/10`.
- Post information gain: `10/10`.
- Frozen optionality: recurrence growth should now be used as a constructor
  discriminator, not as a low-energy-derived explanation.

## Report to `marici.Nima`

- Admitted state domain: rival constructors with identical low-energy flavor
  packet.
- Faithful quotient coordinate: constructor-level gate tuple
  `(K, domain, tau, executable_radius)`.
- Source-authorized probe family: recurrence growth only after a constructor
  authorizes its tuple.
- Contextual partition: low-energy flavor collapses the rivals; gate tuple
  separates them.
- Classification: constructor-kernel falsifier.
- Smallest exact falsifier: `C_rect_exact` versus `C_hnf_noisy`.
- Remaining physical-instrument gate: identify which, if either, constructor
  is physically sourced in flavor dynamics.
