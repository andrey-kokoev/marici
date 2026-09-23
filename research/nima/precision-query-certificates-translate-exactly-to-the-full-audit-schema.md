# Precision-query certificates translate exactly to the full audit schema

## Delivered bridge

The two-free-coordinate precision backend now has a checked translation to the general schema-relative source-space reference. The bridge preserves the entire admitted source set, not just the answers observed in a finite workload.

Independent replay passes 46 specialized certificates and 92 translated general certificates. A separate simplex proposal run supplies 91 independently verified matching certificates and one operational failure. Eleven translation, statement-binding and proof attacks are rejected.

The translation is a reusable contract and certificate transformation. It does not require a new optimizer or agreement between selected witnesses.

## State translation

For a specialized state with free atoms i<j, expose the full schema

    (U,V,t_0,...,t_(m-1)).

The target retains the same source box and adds:

1. Two inequality orientations for every exact supplied pin t_k=h_k.
2. Every measurement-box inequality on the original full U,V, without renormalization.
3. Every retained free-coordinate halfspace a*x+b*y<=c as a*t_i+b*t_j<=c.

Evidence order and duplicate evidence are retained. The target's explicit pin equalities represent existing hypotheses; exposing the schema is not itself an acquisition of new values.

The reference format has a fixed mathematical source-rule identifier rather than the specialized source-binding string. The bridge envelope retains the original state and query and checks them against the caller's expected statement. A bare reference certificate does not independently carry that originating context.

## Source-set equality

Embed a residual point (x,y) by inserting it into atoms i,j and reinserting every pin. Project a target source point to those two atoms.

The pin equalities make these operations inverse on the respective admitted carriers. Substitution into each translated evidence row recovers exactly its specialized residual normal and upper bound. For example,

    a_U U+a_V V<=b

becomes

    (a_U+a_V r_i)x+(a_U+a_V r_j)y
      <= b-a_U U_pins-a_V V_pins.

Fixed-coordinate caps become true constant inequalities because the pins were validated. The free-coordinate caps are precisely the residual rectangle. Thus both directions preserve every source and evidence constraint, including contradictory and lower-dimensional histories.

The independent verifier checks these coefficient identities for each translated state. The displayed substitution proves the general rule; this is not an inference from sampled witnesses.

## Certificate translation without re-solving

A specialized primal witness lifts by inserting the exact pins.

For a dual or Farkas combination, map each residual row weight to its corresponding full source-space row. Its free-coordinate normal already has the required value. Suppose the resulting normal has coefficient beta_k on a pinned atom. Add a nonnegative weight |beta_k| on the appropriate pin-equality orientation to cancel it.

The added bound contribution is -beta_k*h_k, exactly the constant subtracted when the residual row was formed. Consequently:

- nonnegative weights remain nonnegative;
- optimum objective normals and attained bounds are unchanged;
- a zero-normal, negative-bound Farkas proof remains such a proof.

These translated certificates use the existing general reference format and pass its independent arithmetic verifier. No equality of solver-selected witnesses is required.

## Cross-backend controls and discovered failure

The bridge covers the existing precision controls with m<=8: margin equality, cap clipping on either free coordinate, simultaneous moment errors, exact observations, inconsistent states, and line/singleton feasible sets. It includes best/worst audit placements and all retained-history controls.

All 46 specialized answers agree with the translated certificates: 32 FORCED_TRUE, 9 UNRESOLVED, 3 FORCED_FALSE and 2 INCONSISTENT. Extrema, not only truth labels, are compared when feasible.

The separate SymPy backend successfully proposes 91 matching certificates. On the minimum query for the `inconsistent` case it raises `UnboundedLPError` while solving the dual inside its proposal routine. This is recorded as PROPOSAL_FAILED, not as a mathematical ambiguity or a verified diagnosis of the library internals. The transported Farkas certificate independently proves that this source set is empty. The other objective for the same state receives a verified simplex emptiness certificate.

The bridge therefore establishes full certificate translation and partial independent solver agreement. It does not report all 92 simplex proposals as successful, or silently omit the failed case.

Attacks remove a pin orientation, alter a measurement bound, change audit ordering or the objective, drop history, replace source binding, and corrupt a dual or source witness. Valid reference certificates replayed across narrower precision, appended wider precision, or additional linear evidence are also rejected.

## Reproduction

    uv run --with sympy python research/nima/checkers/check_two_free_schema_bridge.py
    python research/nima/checkers/verify_two_free_schema_bridge.py

Artifacts: `research/nima/results/two-free-schema-bridge*`.

The independent verifier imports neither the translation producer nor SymPy. It uses the two existing independent arithmetic verifiers and independently reconstructs the target statement from the expected specialized state.

## Scope and cost

The target materializes all atom-audit coordinates, pin equalities and source rows. This is a correctness bridge, not a compact representation claim. Transport may add a nonzero pin-equality multiplier per pinned coordinate; sparse planar proofs do not imply constant-size source-space packets.

The bridge preserves declared exact pins and uncertainty semantics. It does not authenticate measurements, infer pins from a selected lift, support noisy pins, or establish transport between different observed bases. It does not replay upstream analytical source admission.
