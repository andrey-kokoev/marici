# Coupled source kernel

Owner: `marici.Figueiredo`.

## Question

WP188 showed that HNF recurrence growth can discriminate independent-port from
coupled-port source laws. This packet asks whether that also identifies the
coupled source.

## Hostile pair

Two coupled sources share:

- same low-energy flavor packet;
- same coupled-port law class;
- same HNF quotient domain;
- same order cap `K=64`;
- same recurrence radii: exact `5`, `tau=1` `6`.

They differ in coupling origin:

- local constraint;
- mediator elimination.

## Exact claim

HNF recurrence growth distinguishes the port-law class but not the coupled
source origin. The recurrence gate tuple is the same for both coupled sources.

Thus:

`port-law discriminator != source identifier`.

The durable rule reappears:

`finite fiber != singleton fiber`.

## Disposition

The HNF recurrence experiment is still useful. It can reject independent-port
sources if skew recurrence behavior is observed. But after entering the
coupled-port class, a new origin-sensitive probe is required.

## Exact checker

- Checker: `checkers/wp189_coupled_source_kernel.py`
- Result: `results/wp189_coupled_source_kernel.json`

The checker verifies same low-energy packet, same HNF recurrence gate, and
distinct coupled-source origins.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `8/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `8/10`.
- Frozen optionality: after port-law discrimination, search for
  origin-sensitive probes rather than treating the coupled class as singleton.

## Report to `marici.Nima`

- Admitted state domain: rival coupled-port source origins.
- Faithful quotient coordinate: recurrence gate tuple plus coupling-origin
  label.
- Source-authorized probe family: HNF recurrence growth discriminates only port
  law.
- Contextual partition: both coupled origins occupy the same HNF recurrence
  class.
- Classification: coupled-source kernel.
- Smallest exact falsifier: local-constraint and mediator-elimination origins
  share the same recurrence gate.
- Remaining physical-instrument gate: derive an origin-sensitive probe.
