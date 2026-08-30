# Coupled-port rival source

Owner: `marici.Figueiredo`.

## Question

WP186 gave a source law for rectangular quotients:

`independent port resets -> b=0 -> rectangular domain`.

This packet tests the rival:

Can a coupled-port source share the same low-energy flavor packet while
requiring the arbitrary HNF recurrence gate?

## Hostile pair

Both sources share:

- `physical16_id = P_fit_common`;
- `measured10_id = M_fit_common`;
- order cap `K=64`.

They differ in port law:

- `S_independent_ports`: independent axis resets, rectangular domain,
  exact radius `4`, `tau=1` radius `5`;
- `S_coupled_ports`: coupled port relations, arbitrary HNF domain,
  exact radius `5`, `tau=1` radius `6`.

## Exact claim

The low-energy flavor packet cannot choose the port law. The port law changes
the legal quotient domain, which changes the recurrence-growth gate.

The smallest falsifier to porting the rectangular law is the WP175 skew HNF
hostile `(10,4,6)`, index `60`: it is illegal under independent resets and
legal under coupled relations.

## Disposition

Quotient-domain law is now source-discriminating. It cannot be treated as a
notation choice. A recurrence selector must declare whether flavor source
dynamics has independent port resets or coupled port relations.

## Exact checker

- Checker: `checkers/wp187_coupled_port_rival_source.py`
- Result: `results/wp187_coupled_port_rival_source.json`

The checker verifies same low-energy packet, same `K`, different port laws,
different quotient domains, and different required recurrence radii.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: future constructor laws must explicitly declare port
  independence versus coupled-port relations.

## Report to `marici.Nima`

- Admitted state domain: rival port-law sources with the same low-energy
  flavor packet.
- Faithful quotient coordinate: port-law-implied quotient domain and radius.
- Source-authorized probe family: recurrence growth only after port law is
  declared.
- Contextual partition: low-energy flavor collapses the rivals; port law and
  recurrence gate separate them.
- Classification: rival source falsifier for quotient-domain law.
- Smallest exact falsifier: HNF `(10,4,6)` is legal for coupled sources and
  illegal for independent-port sources.
- Remaining physical-instrument gate: derive the actual port law from flavor
  source dynamics.
