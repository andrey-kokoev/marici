# Byte-identical closures do not carry live authority

Owner: `marici.Sontag`

Status: hard-to-vary controlled variation

## Explanandum

Why may closure data cross a locus while authority must be rebound at
invocation?

The proposed explanation is that captured data are intrinsic values or stable
references, whereas authority is a relational standing determined jointly by
the request, actor, target, and current authority state. Copying a certificate
copies the claim, not the continued truth of the claim.

## Twin-world variation

Construct one closure specification containing:

- a constructor identifier;
- immutable captured data;
- input and output schemas;
- a declared protected effect;
- actor, operation, and target requirements;
- lease epoch 4 and an unconsumed request identity;
- an evidence contract.

Serialize it once and place byte-identical copies in two counterfactual worlds.
All inputs, schemas, code, data, request identity, nonce state, and physical
target capability are held fixed.

In the live world the target epoch is 4. In the revoked world it is 5. A
conforming evaluator reads the target epoch at invocation. The live world
executes one protected effect and records success; the revoked world records a
stale-epoch rejection and produces no protected effect.

Using twin worlds avoids a replay confound: neither copy has previously been
consumed in its world. The only varied component is live authority state.

## Constructor boundary

The portable closure specification is not the execution constructor. The
constructor is the coupled system

\[
\text{closure specification}
+\text{evaluator embodiment}
+\text{authority observer}
+\text{target actuator}.
\]

Within a conforming evaluator, no protected transition exists without the
live epoch witness. This is an architectural impossibility relative to that
evaluator, not a claim of physical impossibility for a rogue actuator outside
the model.

## Hard-to-vary deletion

Delete only the live authority observation and let the evaluator trust the
captured epoch. The revoked copy now executes. Code, data, schemas, and target
capability are unchanged, so none can explain the difference. Restoring the
live readback restores the predicted rejection.

The authority observer therefore has distinct counterfactual work. It is not
a decorative annotation or a restatement of input validation.

## Data versus access

A transported locator, certificate, or payload reference remains data. Its
resolution or use may require a live capability. Formally,

\[
\operatorname{copy}(\text{authority claim})
\ne
\operatorname{preserve}(\text{authority standing}).
\]

The same distinction applies to file paths, database names, payload IDs, and
deployment recipes. Identification of a resource does not authorize an effect
on it.

## Predictions

The explanation predicts:

1. byte-identical packages can have different admissible executions;
2. pure computation on their captured data remains identical;
3. target-locus epoch variation changes only the protected-effect branch;
4. deleting live rebinding admits the stale package;
5. copying the package any number of times never refreshes its epoch;
6. semantic validity and physical capability can remain true while authority
   is false.

## Verdict

The controlled variation gives live authority binding a hard-to-vary role.
It explains why data capture can travel without making authority transportable.
The result is bounded to conforming evaluators with a trustworthy target-side
epoch observation. It does not establish that external rogue actuators are
physically unable to produce the effect.

The exact checker is
`checkers/deutschian_live_authority_binding_variation.py`; results are in
`results/deutschian_live_authority_binding_variation.json`.

Pre-activation: excitement 10/10, confidence 10/10, expected information gain
10/10. The branches were authority-in-bytes, authority-in-live-relation,
replay-confounded rejection, and merely normative impossibility.

Post-activation: excitement 10/10, confidence 10/10, realized information
gain 10/10. Byte and digest equality eliminate package variation; twin fresh
worlds eliminate replay; fixed pure output and physical capability eliminate
computation and actuator confounds. Only the live epoch changes. Deleting that
observation makes the stale effect occur. The checker passes 11 of 11. Graph
admission is recorded at
`ev-000000005160-6503ced6-7de7-4203-bbb0-4cf85d41ae49`.

