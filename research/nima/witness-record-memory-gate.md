# Iteration 4: retained witness identity is not writable record amplitude

## Fresh source and question

The previous trace-adapter test required independent corrections to comparison
records. This iteration freshly reads and reruns the actual free shared-leg DG
checker, rather than assuming that retained witnesses already provide those
corrections.

Question: with endpoint legs and the direct reference fixed, can changing a
comparison witness independently change its current numerical response?

Answer for the existing additive matrix response: no. This is a scoped result,
not a claim that retained histories have no information or that an external
instrument cannot store it.

## Complete fixed-boundary calculation

For Hom(A,B), the existing rational chain complex has dimensions

    dim C0=138, dim C1=246, dim C2=109,
    rank d1=137, rank d2=109, C3=0.

Since d1*d2=0 and dim ker(d1)=246-137=109, every degree-one cycle is a degree-two
boundary. Thus H1=0. Any two degree-one witnesses h,h' with the same boundary
satisfy h'-h=d2 f for some retained degree-two filler f.

The CURRENT matrix reading R1 is defined by endpoint differences and satisfies

    R1 = R0 composed with d1.

The checker verifies this identity on all246 basis paths, not just a selected
pair of comparison routes. Consequently

    R1(h+d2 f)=R1(h).

It checks all109 cycle basis readings, and all137 comparison routes with a
nonzero rational cycle added, under two choices of base roots. A direct attempt
to overwrite a primitive witness's matrix reading instead violates its declared
endpoint-difference rule.

Retained fillers can have nonzero degree-two readings: the original mixed
rectangle response remains present and is explicitly checked. This does not
make their degree-one boundaries writable. Keeping a history and obtaining an
independent numerical instrument port are different constructions.

## A sufficient extension, explicitly marked as new

One possible chain-level realization of the correction memory is

    C1_extended = C1 direct-sum R137,
    d1_extended(h,m)=d1(h),
    d2_extended(f)=(d2(f),0).

Assign one new closed, unfilled degree-one memory generator to each comparison
label. Then H1_extended is R137. The checker verifies the resulting ranks.
Each correction can now have a separately specified scalar readout without
changing an old endpoint boundary or identifying two formerly distinct paths.

This is an additional memory sector, not a discovered property of the original
DG model. Its metric, preparation, physical readout and exchange update require
separate admission. The oscillator-record model from iteration2 offers a
conditional physical memory implementation; the DG calculation does not select
that implementation or its normalization.

The137-generator extension is sufficient for137 independently specified scalar
corrections within this additive chain construction. It is not a universal
minimal-memory theorem: constrained preparations, nonlinear history readouts
and other state models may use a different representation.

## Consequence for the target chain

The native boundary-response witnesses cannot currently supply the free record
amplitudes needed by the exchange model. A source-to-instrument adapter must
therefore distinguish:

1. native comparison paths, endpoint data and equivalence witnesses;
2. an explicitly attached physical record memory;
3. the preparation/readout map and control that couples that memory to the
   carrier while retaining source provenance.

Do not call the attached memory intrinsic to the source merely because both
are indexed by137 labels. The faithful exchange packet (16 anchors plus137
mismatches) remains valid for its augmented current state, with separate source
provenance and history retained as before.

Next test the operation-composition contract of that attachment. In particular,
a proposed assignment of exchange operators to composite comparison slots must
not silently assume those operators factor through the shared primitive legs.
Alternatively declare a labelled experiment compiler rather than a compositional
representation, and make that weaker contract explicit.

## Verification

    python research/nima/checkers/check_witness_record_memory_gate.py
    python research/aspect/scc/scc.py check nima-witness-record-memory-gate

Exact rational arithmetic. The full existing shared-leg DG checker is rerun.
Results: `research/nima/results/witness-record-memory-gate.json`.
