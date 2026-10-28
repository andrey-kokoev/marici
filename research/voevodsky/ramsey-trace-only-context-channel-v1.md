# One coherent output repairs the prepared trace, not the state

## Fresh inputs and exact construction

This attempt rereads the complete pair census, the prepared-locality result and their pinned source artifacts. The local support and full-five preparation are unchanged.

Let M be the preceding exact2-by6 trace matrix on coordinates `[0,1,6,7,12,24]`. Its two coefficients on the remote legs are opposite between the two output rows. With

    w12 = M[0,4], w24 = M[0,5],
    c = w12 y12 + w24 y24,

the requested outputs are exactly

    trace0 = sum_(j<4) M[0,j] y_local[j] + c,
    trace1 = sum_(j<4) M[1,j] y_local[j] - c.

Both weights are nonzero and retained in exact multiradical form. The observation has four local outputs plus one additional complex scalar output. Direct matrix multiplication verifies its factorization on the entire five-dimensional prepared domain.

The remote input supports remain actual source slots12 and24: axis0 of triangles `(F_L0_L1_U1,U1,L0)` and `(F_L0_L2_U2,U2,L2)`. One recorded output is not one spatially local input. Coherent access and a phase reference between these legs are declared mathematical requirements, not supplied physical apparatus.

## Minimal output count and surviving kernel

The prior local kernel is span(e2,e3), and the desired trace has rank1 on it. Zero added outputs cannot work; the construction proves that one additional complex scalar suffices under the declared coherent linear access policy.

Nevertheless the complete prepared observation has rank4, not5, despite producing five scalar outputs. Let alpha=F[0,2], beta=F[0,3]. Both are nonzero. The nonzero coefficient vector

    k = (0,0,-beta,alpha,0)

is annihilated by the whole observation and by the requested trace. Its prepared field B_N k is nonzero. This gives an explicit one-dimensional unrecovered subspace. The channel is sufficient for the specified trace task only; it is not a faithful replacement for the retained parent field or packet.

## Controls

The exact factorization fails if either off-edge leg is deleted or the phase of slot24 is reversed while retaining the decoder.

The prepared inputs e2 and -e2 have identical zero local observations and identical per-leg powers on both remote slots, but opposite nonzero required complex-linear traces. Thus those powers alone do not replace the coherent amplitude channel. This is an information-theoretic control, not a claim that a particular hardware mixer has been built.

The channel remains valid only on the stated preparation domain; no full36-coordinate reconstruction or local-neutron-edge equivalence is asserted.

## Next composition gate

Before placing this smaller observation in a reusable incidence/transport package, test whether its lost direction remains invisible after the next admitted source action. Task sufficiency at one observation does not make its kernel a congruence for subsequent evolution.

A concrete available test is the source-derived neutron sector cycle and its existing five-coefficient action. Compare a fixed trace channel after that cycle with the present channel. Separately test the transported channel, which may retain covariance by carrying its context rather than identifying the two kernels. If the fixed kernel is not invariant, retaining either the lost coefficient or the transported context is necessary for reuse.

Native retained parent packages continue to carry the full records; they must not be replaced by this rank4 observation without that additional gate. Parent face-chart descent remains open.

## Verification

Contract: `contracts/ramsey-trace-only-context-channel-attempt.v1.json`.
Checker: `checkers/check_ramsey_trace_only_context_channel.py`.
Receipt: `results/ramsey-trace-only-context-channel-v1.json`.
Passing freeze: `scc-freezes/ramsey-trace-only-context-channel-v1.a019e9570242ccb3.json`.

The frozen SCC challenge passes the exact factorization, nonzero-kernel and hostile controls. No physical mixer, native higher-WG readout interpretation, net revision, graph verdict or Git checkpoint was produced.
