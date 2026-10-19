# Executable split: exact-domain transport and witnessed context creation

## Implemented contract

Following the proposed separation, the new reusable interface implements two distinct operations:

1. `T9_exact_domain`: reuse the existing inherited-key promotion twice, preserving the original context domain and member-weighted J4.
2. `ContextTransport`: compose records in an already admitted common-target context, or require an explicitly declared connector to create a cross-target context.

This is a declared conservative candidate interface, NOT confirmation of intended physical T9. It gives the missing operational choice a concrete implementation boundary rather than silently deciding it through a common target label.

Module: `checkers/record_context_transport.py`.

## Cross-fibre witness and literal typing

The checker chooses two actual existing records a and b whose targets differ. Without a connector the new interface rejects their composition, even though the existing flat frames supply a numerical coordinate transport.

Given an explicit declared connector k:t_a->t_b, the typed sequence is

    a:s_a->t_a,
    k:t_a->t_b,
    return_b:t_b->s_b,
    b:s_b->t_b.

The composite is b return_b k a:s_a->t_b. Its target is b's target, not a's old target. The returned packet retains both operand labels and the entire connector declaration: label, endpoints, matrix and provenance.

Undeclared connector labels, endpoint-mismatched/reversed use, duplicate declarations and empty provenance are rejected. Connector existence as a matrix is deliberately insufficient for admission.

These guards enforce a mathematical interface. They are not authentication or permission to mutate shared task graphs, and a caller-supplied provenance tuple is not proof of physical realization.

## Passive and active connectors are distinguished

Using the already existing flat port frames, a passive connector has value

    k=P_t_b P_t_a^-1.

The decoded composite is exactly C_b r C_a. Its numerical value agrees with the familiar matrix formula, but now the cross-target domain and endpoints are explicitly witnessed.

Two distinct connector declarations with equal matrices yield equal decoded effects while retaining distinct provenance. Thus equal coordinates do not erase declared histories.

An active invertible shear control

    k_active=P_t_b H P_t_a^-1

instead gives C_b r H C_a and changes the fixed decoded response. It is a different declared operation, not a passive gauge or calibration adjustment.

No active connector was selected to reproduce a target. The shear is only a rejection/discrimination control using the existing exact fixture.

## A local bridge is not common-target collapse

One directional bridge from t_a to t_b admits pairs in that particular source/destination target-fibre pair. It does not authorize every cross-fibre product, nor silently supply a reverse connector.

The checker measures that local added support and confirms it is strictly smaller than the17792 pairs added by global common-target collapse. Transport leaves, responses, weights and J4 are not modified by the test declarations.

## What this accomplishes

The conservative policy is now executable rather than merely recommended:

- all977 original admitted comparisons still work without extra witnesses;
- the full response/record endpoint contract remains unchanged;
- context creation is explicit and retains its connector provenance;
- passive transports cannot silently manufacture physical operations;
- active bridge responses are observable and not absorbed into transport calibration.

The remaining intended-T9 decision is consequently exposed at a specific interface: whether an actual source operation supplies connector declarations, and which declarations it supplies. A runtime declaration in this checker is not that source derivation.

The separately inspected `reference-cone-and-typed-successor.md` is consistent with this distinction: parallel higher comparison boundaries also require explicit alignment and an actual filler rule. This matrix connector API does NOT construct those higher fillers or identify their cell degrees with rung numbers.

## Verification

    uv run research/nima/checkers/check_explicit_context_transport.py

1972 exact checks pass. Dependencies freshly rerun the existing geometric record-port binding and original flat attachment/rung response chain. No fresh Agda closure or higher-cell theorem is claimed in this implementation step.

Artifacts:

- `checkers/record_context_transport.py`
- `checkers/check_explicit_context_transport.py`
- `results/explicit-context-transport.json`

Intended physical T9 and source-derived connector admission remain unconfirmed.
