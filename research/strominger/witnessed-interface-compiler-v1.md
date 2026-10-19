# One metric-residual compiler for transport, mismatch and records

## Constructive result

One exact formula, without interface-kind dispatch, reproduces51 existing local comparison interfaces:

-21 native seam projectors;
-18 addressed/frame-dependent source-bank pulse projectors;
-12 full-field transport graph interfaces, whose reflections are the actual bidirectional transport exchanges.

The constructor accepts the source comparison map and metric, not a desired projector. It retains both alongside the derived operators. It does not discover which comparison task the source should perform. The axial and local mode rules remain the preceding construction's premises.

Protocol: `inputs/witnessed-interface-compiler-protocol-v1.json`.
Checker: `checkers/check_witnessed_interface_compiler.py`.
Full compiled inputs/operators: `results/witnessed-interface-compiler/contracts.json`.

## Common rule

For positive input metric M and independent residual rows B, define

    G = B M^-1 B^T,
    Gamma = G^-1,
    A = M^-1 B^T Gamma,
    Q = A B.

The returned comparison has residual Bx, normalized energy x^T M Q x, metric-orthogonal mismatch projector Q and reflection I-2Q. BA=I and Q²=Q are checked. The formulas complexify directly for the real24-coordinate mode/bank matrices. Complete complex two-plane transport is instead represented by exact four-real-coordinate matrices, retaining the factor3 in the imaginary-coordinate metric.

For a metric-isometric port map T, take B=[-T,I] on the direct sum of the two port spaces. The compiler's reflection is exactly

    (x,y) -> (T^-1 y, T x).

This recovers the full existing port transport, not just its graph kernel. All12 port maps retain the previously derived identity loop composition.

For a native seam, B is the actual selected-amplitude difference row. For a source-bank pulse, B is the metric dual of its actual difference direction. Applying the same formula reproduces every stored projector entry, including bank cross terms. Once Q is self-adjoint and idempotent, I+(exp(-i theta)-1)Q is the corresponding unitary phase family; the executable comparison here verifies Q and its endpoint reflection, not a physical-time parameter.

## Reversible residual record

The same data construct a record swap

    U = [[I-Q,A],[B,0]]

with joint metric diag(M,Gamma). Exact matrix checks give U²=I and U^T metric U=metric. For initially zero record:

    (x,0) -> ((I-Q)x,Bx).

The source mismatch energy equals (Bx)^T Gamma (Bx). The input is recovered by the same swap. This is transfer into a residual coordinate, not norm-duplicating copying.

Reuse the existing21 occurrence-memory slots from `neutron-comparison-memory.json`. Their Gamma and collective operator B M^-1 B^T Gamma are reproduced exactly. The21 rows have rank15 and six dependencies. All occurrence slots remain; no arbitrary equal spectral gap is fitted.

The local encoder is nevertheless NOT the previous collective polar encoder. Here each local record receives a raw residual. The previous encoding uses collective polar coordinates. Equal memory space, metric and a reproducible operator do not identify their actions or energy semantics. In particular, the local stored-residual energy above uses the identity operator in its Gamma metric; this is not automatically the previous collective memory Hamiltonian.

An explicit eight-write schedule starts with empty occurrence memory and a mixed native/source-bank state. Every write preserves the joint norm and is involutive. Reversing the ordered schedule recovers the exact initial state; deleting the emitted record prevents recovery. Two overlapping writes fail to commute, so order and intermediate states are retained in `results/witnessed-interface-compiler/history.json`.

## Two obstructions retained

### Existing bank capacity

The current24-complex-coordinate source envelope includes18 selected triangle modes and six independent bank-feature directions. Those six lie in the full16-complex-coordinate source bank and must remain protected under this task. Its orthogonal complement has dimension10.

Simultaneously encoding the full rank15 seam residual injectively into that complement requires at least15 complex coordinates. Ten do not suffice. This is a bound for simultaneous lossless storage wholly within unused bank directions, not a prohibition on sequential storage, changed protection requirements, or retaining information in native coordinates.

On arbitrary full-bank inputs, requiring all16 bank directions fixed pointwise is even stronger: a unitary fixing that subspace cannot transfer amplitude into it from its orthogonal complement. The existing21 occurrence-memory space is therefore reused explicitly rather than silently overwriting the source bank.

### Unchanged total energy

Let K be the existing native constraint energy divided by4 plus the21 seam projectors in the24-coordinate envelope. Extend it by the existing collective memory operator on the21 occurrence slots. This is the tested fixed core-plus-memory Hamiltonian, not an assertion that the extension was already a source execution law.

The new local storage gate does NOT conserve that operator. Writing interface0 from native basis input0 and empty occurrence memory changes its quadratic energy by

    -22380683579/35676273088.

The local residual energy and total metric norm remain exactly accounted for. The discrepancy is with the full fixed Hamiltonian, including other coupled comparisons and the distinct collective-memory energy. Thus an energy-compatible execution still needs a source-supported control/work accounting or another encoder; it cannot be inferred from reversibility.

## Disposition

A common operational comparison constructor exists. It produces transport exchange, mismatch energy and reversible record operations from one residual/metric contract, rather than dispatching to particle-specific recipes. Its individual projectors and transport maps reproduce the existing system.

The stronger claim that these new local record writes already compose into the unchanged autonomous global Hamiltonian is rejected by an exact counterexample. Information-preserving composition and Hamiltonian-compatible execution remain distinct obligations.

## Verification

Ten exact groups pass. The first frozen version tested arbitrary initial memory; a retained refinement strengthens the emitted-memory hostile to start with empty memory. Fresh focused execution, SCC check and frozen challenge pass under `a77e1d8da1d4406e`.

    python research/strominger/checkers/check_witnessed_interface_compiler.py
    python research/aspect/scc/scc.py check witnessed-interface-compiler
    python research/aspect/scc/scc.py challenge witnessed-interface-compiler research/strominger/checkers/check_witnessed_interface_compiler.py survives

Result receipt: `results/witnessed-interface-compiler/verification.json`. Sources are hash-bound and unchanged. No other-owner result, source law or viewer was modified. No Agda compilation, physical energy calibration, commit or push is claimed.
