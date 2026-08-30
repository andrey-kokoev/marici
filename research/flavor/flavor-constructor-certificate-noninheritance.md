# Constructor certificates do not transfer across task mutation (WP84)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

## Question

WP82 makes the faithful probe algebra look one Boolean gate from a selector:
it passes descent, task totality, authority, instrument, repeatability, and
ensemble gates, failing only proper image. Can one simply add proper reduction
and inherit the other certificates?

## Task-indexed evidence

No. A certificate has the typed form

\[
e=(T,\mathcal D,\mathcal R,g,\text{evidence}),
\]

where `T` is the exact input-output task, `D` its domain, `R` its resources,
and `g` the certified gate. The readout task

\[
T_I:x\mapsto(x,I(x))
\]

and any proper-image substrate task

\[
T_S:x\mapsto S(x),\qquad \operatorname{im}S\subsetneq X_{16},
\]

have different task identities. Evidence that the mass/CKM apparatus
implements `T_I` says nothing about an apparatus implementing `T_S`.
Likewise source authority for measuring invariants is not authority for a new
dissipative or boundary operation, and ensemble adequacy of the observed
readout is not a numerical prediction of `im(S)`.

Therefore Boolean gate distance is not physical resource distance. Flipping
`P` on a faithful probe invalidates at least the task-indexed `A`, `I`, `R`,
and `E` certificates and requires them to be proved anew. The closest
proper-image mathematical maps already display exactly this missing bundle.

## Consequence

There is no one-resource shortcut from faithful flavor readout to selection.
The minimum reopening unit is a coherent new task package: exact proper map or
attribute, independent source authority/normalization, its own physical
implementation and repeatability account, and its own ensemble prediction.
Certificates may compose only when their task, domain, quotient, and resource
interfaces agree exactly.

## Falsifiers

- a typed instrument certificate whose task hash equals both a substrate-
  preserving readout and a proper-image state map;
- authority for invariant measurement explicitly authorizing state reduction;
- a selector ensemble prediction derivable without specifying its image;
- a valid composition whose resource interfaces do not match.

Verification:
`python research/flavor/checkers/wp84_constructor_certificate_noninheritance.py`.
