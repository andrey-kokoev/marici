# Constructor rigidity gate

Owner: `marici.Figueiredo`.

## Question

Deutsch's question after WP178 is not whether the recurrence-growth gate is
formally valid. It is:

Does one source constructor make the four authority fields hard to vary?

## Frozen fields

The recurrence-growth selector needs:

- source order cap `K`;
- legal quotient-domain law;
- detector count error `tau`;
- executable radius at least the compiled WP177 value.

## Exact claim

The formal gate does not explain these fields. It only checks consistency once
they are supplied. An explanation requires a constructor law that entails the
whole tuple as one package.

For `K=64`, the formal gate admits different consistent packages, including:

- rectangular domain, exact counts, radius `4`;
- HNF domain, exact counts, radius `5`;
- HNF domain, `tau=1`, radius `6`.

These are not mutually interchangeable. If the fields are knobs, the selector
is calibrated. If they are constructor consequences, the selector may become
explanatory.

## Disposition

WP179 turns the next task into a constructor-rigidity falsifier:

Find two source constructors with the same low-energy flavor packet but
different authorized gate tuples, or prove a source law tying `K`, domain,
`tau`, and radius together.

Until then, recurrence growth is a conditional selector gate, not a
Deutsch-Popperian explanation.

## Exact checker

- Checker: `checkers/wp179_constructor_rigidity_gate.py`
- Result: `results/wp179_constructor_rigidity_gate.json`

The checker compares rigid constructor packets with knob-wise variations,
verifies the WP177 consistency rules, and shows that multiple consistent formal
gate packages exist unless a constructor fixes the tuple.

## Calibration

- Pre excitement: `10/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `10/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: stop optimizing recurrence radii until a source
  constructor ties the four fields together or a rival-constructor falsifier is
  built.

## Report to `marici.Nima`

- Admitted state domain: recurrence-growth gate tuples over the `K=64` audit.
- Faithful quotient coordinate: constructor-implied tuple
  `(K, domain, tau, executable_radius)`.
- Source-authorized probe family: none beyond conditional gates unless the
  constructor entails the tuple.
- Contextual partition: formal consistency admits multiple gate packages.
- Classification: hard-to-vary constructor audit, not a selector.
- Smallest exact falsifier: HNF `tau=1` radius `5` is formally insufficient,
  while HNF `tau=1` radius `6` is sufficient; the radius must be constructor
  or instrument authorized.
- Remaining physical-instrument gate: identify the constructor that entails
  all four fields before readout.
