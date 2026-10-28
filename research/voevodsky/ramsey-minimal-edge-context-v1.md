# Minimal added-coordinate repair, with a weaker trace-only requirement

## Fresh scope

This audit keeps the preceding prepared domain, source full-five neutron binding and local uv slots `[0,1,6,7]` unchanged. It rereads the live locality receipt and its pinned inputs. All32 other intrinsic source coordinates and all496 pairs are considered before selecting a repair.

Minimality is relative to this fixed four-coordinate local observation and scalar linear supplements. It is not a global optimum over all instruments or a physical detector claim.

## Complete pair classification

The local observation has rank3 and kernel span(e2,e3). Every source coordinate in sector1 sees the missing active coefficient e2 but not e3; every source coordinate in sector2 sees e3 but not e2. All their active coefficients are nonzero. Remaining sector0 coordinates see neither missing direction.

Exactly144 pairs complete the local observation to rank5:

    i in {12,...,23}, j in {24,...,35}.

The other352 pairs fail the rank test on the local kernel. For every successful pair, an explicit decoder was constructed and checked by `D A_extended=I5`, not merely by dimension counting. Known coefficients0,1,4 are first reconstructed from the local weighted Gram; their contributions are subtracted from the additional observations before solving for coefficients2 and3.

Since each scalar adds at most one rank, at least two additional scalars are necessary for full prepared reconstruction. The144 exact decoders establish sufficiency. Six scalar coordinates total are needed when the original four must all be retained; this is not a claim that five suitably chosen measurements cannot reconstruct the same five-dimensional state.

## Selected source-supported repair

The lexicographically first pair is `[12,24]`, giving six coordinates `[0,1,6,7,12,24]`.

-12 is axis0 of triangle3: `(F_L0_L1_U1, U1, L0)`.
-24 is axis0 of triangle6: `(F_L0_L2_U2, U2, L2)`.

These are actual native intrinsic axes on two off-edge patches. Along with the original local edge L1–U0, the observations span three distinct geometric edges. The exact decoder and the two-row proton trace readout are saved in the receipt.

This improves the earlier12-coordinate reconstruction to six retained coordinates without pretending the additional support is local.

## Trace-only information is strictly weaker

A separate calculation restricts the requested two-row proton trace F to the local kernel span(e2,e3). That2-by2 matrix has **rank1**, not2. Thus recovering the two traces does not require reconstructing both missing coefficients independently.

Nevertheless neither column is zero, and every single existing off-edge source coordinate sees at most one of the two missing directions. The checker tests all32 candidates: none alone repairs the two requested traces. So two additional **raw source coordinates** remain necessary under that access policy.

If arbitrary coherent scalar mixing of off-edge coordinates is authorized, one added scalar could instead measure the particular rank-one combination needed by F. Such a channel would still draw on two distinct source locations, and its authorization/normalization is a separate construction. The distinction is between number of recorded outputs and spatial support, not a contradiction in the rank bounds.

## Next executable obligation

Construct that one-output trace-only channel explicitly from slots12 and24, retaining its two physical source legs and the local correction terms. Check the exact factorization for the requested traces, show its remaining prepared kernel, and do not promote it to full state reconstruction. If used in the Ramsey incidence packages, retain the off-edge dependency as part of the context witness rather than erase it at an edge restriction.

The native retained incidence proof is unaffected. The source-defined edge-local obstruction is also unaffected: a spatially extended reconstruction is not a local gluing theorem.

## Verification

Contract: `contracts/ramsey-minimal-edge-context-attempt.v1.json`.
Checker: `checkers/check_ramsey_minimal_edge_context.py`.
Receipt: `results/ramsey-minimal-edge-context-v1.json`.
Passing freeze: `scc-freezes/ramsey-minimal-edge-context-v1.b211e9fb3f2bb943.json`.

The frozen SCC challenge passes exact arithmetic checks, including144 explicit decoder identities. No physical instrument, full-field recovery, parent descent closure, graph verdict, net revision or Git checkpoint was produced.
