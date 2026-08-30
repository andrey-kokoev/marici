# Aspect's Seven-Axis Tester Validates the Separation but Needs a Domain Axis

## Question

How does the corrected Hodge-control model compile through Aspect's updated
seven-axis event tester?

## Two scoped events

The unrestricted global Hodge circle compiles as

```text
path=admissible
coefficient=native
action=authorized
```

The locally varying Hodge selector without an active duality connection
compiles as

```text
path=unknown
coefficient=native
action=missing
```

This confirms Aspect's central correction: coefficient character, path, and
action are independent. The native real Hodge generator does not by itself
authorize local action.

## Superseded frozen fixture

Aspect's original selective-gate fixture records

```text
path=disconnected
coefficient=requires_extension
action=missing
```

The coefficient value is superseded by Entry 3782: multiplication by \(i\) is
the coordinate form of a real Hodge operation. The path value remains correct
only when its carrier is explicitly the reflection-fixed projective locus. On
the unrestricted radiative carrier, the Hodge circle gives an admissible path.

Thus the two path classifications are not contradictory. They refer to
different declared objects.

## Hostile alias in the updated tester

The seven axes assign the same tuple to two different failures:

1. no selector operation has been supplied;
2. the local Hodge formula exists, but its selector current leaves the
   derivative-defined domain.

Both appear as `action=missing`, with native coefficient and unknown path.
The first is absence; the second is a domain obstruction with an exact
nonzero residual.

The smallest additional axis is therefore

```text
domain=preserved | obstructed | unknown
```

This is not a fitted exception for Hodge theory. Any partially defined action
can exist algebraically while failing to preserve the object on which it is
claimed to act.

## Disposition

Aspect's separation theorem survives. Its frozen selective-gate coefficient
fixture needs correction, and its event type is incomplete for partial
constructors. An eighth domain axis separates the smallest hostile pair.

## Verification

```powershell
python research/strominger/checkers/aspect_seven_axis_hodge_model_audit.py
```
