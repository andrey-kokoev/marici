# Iteration1/10: flags, spectral channels and information lost by forgetting

## Fresh state, question, boundary

The freshly read v1 net and graph test `test:c6dc227632a165424790` both mark
`canonical-flag-channel-spectrum` planned and executable. The source is the
already exported64-flag/192-edge/degree6 graph on actual16-cell vertex-tetrahedron
incidences. No old net, source receipt or queued graph is changed.

Question: does the raw flag count represent a single retained capacity, and can
we forget the tetrahedron label while preserving the specified operator task?

Obligation: forward source spectrum followed by attachment/reader and exact
composition compatibility. Not a physical electron/nuclear model, literal time,
spin derivation or newly imposed flatness constraint.

## Frozen source operation and prediction

Use the original H=6I-A, unit flag metric and complete spectrum. Reuse the exact
full-operator spectral certificate constructor. Count every band; report optional
spin doubling separately. Predicted first scalar ranks1,4,6 give2,8,12 under the
assumed spin factor, not2,8,18. The full64-dimensional function space remains;
no mismatched sectors are declared null.

The source incidence gives a canonical, independently defined map:

    B[f,v]=1 when flag f lies at vertex v,
    D=B^T/8,   DB=I8,   P=BD,   Q=I64-P.

The normalized B/sqrt8 is isometric; unnormalized integer B and rational D keep
all calculations exact. Each vertex belongs to eight original tetrahedra.

Freeze this map BEFORE comparison, not a rank-reducing projector chosen to match
a desired shell. Test compression h=DHB against half the actual8-vertex
16-cell Laplacian. Then test the SECOND application:

    D H^2 B - (D H B)^2.

Agreement at one application is not enough to transport composition.

## Retain the obstruction and minimal continuation carrier

Predict nonzero leakage K=QHB of rank4. With T the actual source antipodal
vertex permutation, let P_odd=(I-T)/2. Test exact identities

    K^T K /8 = 3 P_odd,
    D H^2 B - h^2 = 3 P_odd.

Only the four-dimensional even vertex sector has no leakage. A specific flag
state q=K e_j has Dq=0 but DHq !=0: a later allowed operator reader detects
information discarded by the coarse boundary. This does not mean H's own
coherence fails; it means this coarse compression is not a composition-preserving
interface for the full source task.

The full source packet (Df,Qf) reconstructs f=B(Df)+Qf. Export that decoder and
check its exact two-application compatibility, not just the failed quotient.

Compute the Krylov closure of vertex preparations under the SAME H. Predicted
ranks are8,12,12 for [B], [B,HB], [B,HB,H^2B]. An explicit64x12 inclusion W,
its inherited Gram metric, and H W=W A certify a minimal invariant12-dimensional
carrier for this restricted preparation task. The remaining52 modes are not
physical gauge: they remain available to other original flag preparations/readers.
The number12 (or24 with optional spin) is not a reindexing as a principal shell.

## DPC and disposition criterion

Problem: raw incidence count may be mistaken for retained capacity; forgetting
flags may erase a required continuation. Candidate: the frozen flag operator
splits raw labels, and the canonical source-forgetting map is not closed under
all applications. Rivals:64 is one shell, first-application compression proves
full equivalence, lost flag coordinates are null, or an enlarged source is a
mere basis change. Risk: compute the complete spectrum, full residual and source
witness; certify minimality of any repaired TASK carrier without changing H.
Strongest falsifier: exact second-application composition square plus a full
reconstructible packet control. Disposition is recorded in
`results/dual-flag-spectrum/verification.json` and `disposition.md`.

## Reproduce

    uv run --with sympy python research/strominger/checkers/check_dual_flag_spectrum.py

Use the declared ephemeral Sympy environment, not a bare interpreter. Source
maps, full matrices, all band certificates and two evaluated SCC comparison
cells are retained. Fresh headless closure is the SCC check of
`dual-flag-spectrum-v1`.

The enabled successor is a bounded d=2..6 cross-polytope flag-family test with
the same incidence-defined moves and forgetting map. It can distinguish raw
exponential flag growth from task-relative invariant channel growth. Only d=4
has tetrahedral facets; d is not a principal shell number. Native P/N/E binding
and occupation remain blocked, not waiting-only successors.
