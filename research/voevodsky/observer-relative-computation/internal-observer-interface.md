# Observer access is now explicit first-order package data

`agda/ObserverInternalInterface.agda` freshly typechecks under safe Cubical Agda --ignore-interfaces with exit0. Log: `results/agda-internal-interface.log`. IMPORTANT: the current check reports inherited UnsupportedIndexedMatch warnings, discussed below; it is not a warning-free computation certificate.

## Internal finite interface

A Package contains BOTH an actual history witness and a Code describing observer access. The code grammar has three constructors: result, rule, and both(c,d). Its constructor vocabulary is finite; composite codes can be arbitrarily large finite trees.

A single structurally recursive readout interprets these codes. No code constructor stores a callback, arbitrary evaluator or externally supplied observation function. Replies depend on the code: Unit for result, Bool for the rule witness, and a dependent pair for combined access. A tagged manifestation includes the code and its reply. A certificate retains its equality to the specified readout.

Checked properties:

- Every syntactically result-only composite is noninterfering with respect to the red/blue history distinction.
- No such result-only code faithfully recovers which history was supplied.
- A witness locating rule access inside a composite code gives a faithful history recovery function.
- The red/blue packages have equal result-only manifestations but distinguishable rule replies.

This internalizes the observer DESCRIPTION in the same package as the observed witness. It does not internalize the surrounding type-theoretic semantics, derive which observer exists, solve self-reference, or construct a physical observer. The Package fields are public mathematical data; this is not an access-control/security theorem against arbitrary functions outside the code interface.

## Newly recorded computation limitation

Agda2.8.0.1-001a4ed reports UnsupportedIndexedMatch for inherited definitions in ObserverPolicyReconstruction and ObserverNonuniqueHistory. The compiler specifically warns that these functions will not compute on transports. Several diagnostics are repeated in the end-of-run summary. The new interface itself typechecks; the warnings concern the history/uniqueness functions it imports.

Do not equate successful typechecking with unrestricted computational behavior under transport. The formal propositions remain accepted, and the concrete constructor examples check, but a warning-free computation claim for transported histories has not been established. No warning was suppressed or treated as a proof of a false statement.

The aggregate import list now includes this module, but its old24-entry receipt is historical and has not been relabelled as covering it.

## Next

Prioritize a transport-computation gate: reproduce the relevant warnings as errors, localize the affected indexed eliminators, and seek a transport-compatible implementation or an explicit scoped boundary. Preserve history witnesses and existing claims rather than bypassing the issue by silently replacing histories with an unrelated Bool. This matters directly to the sought alignment of mathematical transport and executable observation.
