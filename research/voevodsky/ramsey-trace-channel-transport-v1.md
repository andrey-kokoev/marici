# A trace-sufficient channel is not a transport congruence

## Fresh source action

The trace-only observation O and its explicit one-dimensional prepared kernel were reread with live source pins. The existing field-sector permutation R cycles the three12-coordinate neutron sectors. The checker independently verifies

    R B_N = B_N C,
    C = permutation [0,3,1,2,4],
    R^3=I36, C^3=I5.

This is the source field-sector rotation already used by the full-five candidate. It is not silently identified with the native packet reader event, an autonomous clock, or an available physical actuator.

## Fixed observation fails the next-step test

Write A=O B_N and let k be the previous exact nonzero kernel vector. The fresh test finds

    A k=0,    A C k != 0,
    F C k != 0,

where F is the requested two-row prepared proton trace. Hence k and0 have identical present observations but different next fixed observations and next requested traces.

No deterministic update of the present observation alone can reproduce these future outputs for the full declared prepared family. This is stronger than saying that a particular guessed update fails. It does not refute the full retained field or a transported observation context: it identifies the information lost by this fixed compression.

The earlier one-output channel remains correct for its instantaneous trace task. It is not a reusable state quotient for this source action.

## Co-rotating family succeeds with support retained

Construct O_t=O R^-t for t in Z/3. Direct checks give

    O_t B_N C^t = O B_N,
    decoder O_t B_N = F C^-t.

All9 pairwise observation squares and27 comparison triangles pass exactly. Their source-coordinate supports are:

| Context | Four individual readings | One mixed output's input legs |
|---|---|---|
|0|0,1,6,7|12,24|
|1|12,13,18,19|0,24|
|2|24,25,30,31|0,12|

These are different observations, with different geometry. Carrying that frame/context makes the family covariant. It does not make the original fixed channel complete or local, and it does not supply an actual acquisition schedule.

## Minimal temporal information repair

The actual scalar at source coordinate0 after one sector rotation has prepared row `(B_N C)[0,:]`. Its value on k is nonzero. Since the present observation's kernel is exactly span(k), adjoining this one genuinely new scalar yields a rank5 prepared observation.

This is a checked rank/separation result, not a claim that the future scalar is inferable from current data. It requires an additional acquisition and the stated source action. It does not recover an arbitrary36-dimensional field.

## Consequence for retained incidence

If the trace channel is carried by an edge/vertex package, that package must distinguish at least:

- the full retained parent field/record;
- the current observation context and actual off-edge input supports;
- the trace-only compressed value;
- any newly acquired scalar or transported frame used for continuation.

Replacing the first item by the third erases a direction required by subsequent source transport. Native P retention from the earlier formal result offers the appropriate structural discipline, but does not itself interpret these linear observations in the kernel or prove their physical availability.

The next constructive step is to package the observation together with its full parent and frame, and verify restriction/transport squares without requiring a nonexistent update on the compressed value alone. The results should then be reconciled with the still-open face-chart descent node, retaining the distinction between native retained incidence and local field gluing.

## Verification

Contract: `contracts/ramsey-trace-channel-transport-attempt.v1.json`.
Checker: `checkers/check_ramsey_trace_channel_transport.py`.
Receipt: `results/ramsey-trace-channel-transport-v1.json`.
Passing freeze: `scc-freezes/ramsey-trace-channel-transport-v1.1120b5fc9e05faf9.json`.

The frozen SCC challenge passes the exact fixed-kernel obstruction, moving-family cells and additional-scalar separation. No physical instrument, native packet-event identification, parent descent closure, net revision, graph verdict or Git checkpoint was produced.
