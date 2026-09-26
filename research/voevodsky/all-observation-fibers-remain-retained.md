# All observation fibers remain retained

Fresh resume selected `observation-fiber-presentation-characterization:v1`.
The operator clarified the central requirement: observations and scalar
restrictions must NOT replace the full retained source by selected fibers.

## 1. Reassembly, without deleting fibers

For any source type A and supplied reader r:A->V, define

    Fiber_r(v) = sum(a:A) [r(a)=v],
    Total_r = sum(v:V) Fiber_r(v).

`agda/RetainedObservationFibers.agda` proves A is equivalent to Total_r, with
both recovery laws. It uses no truncation, quotient, representative selection,
or assumption that V or the fibers are sets. Equality witnesses are included.
Recovery of the original source a is definitionally a; recovery of arbitrary
fiber data is a typed path, not a byte-serialization assertion.

A may be the COMPLETE admitted source/history type. `HistoryRetention` applies
the construction directly to the owner's proof-relevant resolution closure for
any supplied seed policy and reader. It does not manufacture source admission or
missing continuum evidence. The coefficient-jet examples are instances, not a
replacement for that general source type.

Every fiber remains an indexed type, INCLUDING empty fibers. A checked Boolean
control has an empty fiber and proves that no selection of an inhabitant in
every fiber exists. Retaining a fiber is not asserting that it has a state.

## 2. Coarsening is regrouping, not quotienting

Given q:V->W, the retained coarse fiber is

    Grouped(w) = sum(t:Total_r) [q(t.index)=w].

It stores the original v, the complete source a, the witness r(a)=v, and the
coarse witness q(v)=w. Accessors recover the original index and fiber data.
The total of these groups is again equivalent to A, with both recovery laws.
A further theorem proves that regrouping cannot identify distinct source values.
This holds even when q itself is many-to-one or constant.

The projections and witnesses matter. A bare equivalence of total types is not
permission to ignore their observation maps. Coarser comparison compatibility
also does not imply compatibility with every old observation: the retained data
allows a later refinement to TEST that additional condition.

## 3. Exact fiberwise criterion

For a FIXED map f:A->B and supplied commuting witness

    s(f(a))=r(a),

there is an induced map on EVERY observation fiber:

    (a,p:r(a)=v) |-> (f(a), commuting(a) followed by p).

The new proof reuses Cubical's existing fiberwise-equivalence theorem to show

    f is an equivalence
        iff each induced fiber map is an equivalence.

The forward direction transports the equivalence through the source/total
reassembly maps, preserving the supplied commuting witness. The reverse
assembles all fiber maps and recovers the underlying map. This is a criterion
for the fixed coherent map, not an arbitrary pairing of a few observed values.

Conversely, supplied equivalences of ALL fibers reconstruct an observed carrier
equivalence. To reconstruct a MARKED presentation, its action on the distinguished
point must additionally be supplied; the code makes that requirement explicit.
No complete equivalence between all higher record presentations or all coherence
laws is claimed beyond these checked constructions and implications.

## 4. The physical examples now have the right status

- The actual retained action-chart presentations instantiate the criterion:
  every fiber of the specified reader is transported, not just the vacuum
  reading. The existing source packages and histories remain retained separately.
- The integer tangent-coordinate scalar inclusion fails already on the fiber
  over zero. Its target fiber contains off-plane states; the proof excludes an
  equivalence on that fiber.
- `FullTargetRetention` still retains ALL target points and fibers. The failed
  inclusion does not delete the massless directions or replace the target.
- The real mixed-scattering calculation remains separate physical evidence;
  no integer tangent model is relabelled as a formal continuum field theory.

Thus the scalar example is now used only to expose an invalid promotion. It is
not a proposed reduced carrier for the synthesis.

## Verification and next integration boundary

    python research/voevodsky/check_native_radar_formal.py --retained-fibers --fresh

Fresh safe/cubical closure passes, as do the intended upstream potential-only
and false-sixth rejection controls. New universal proofs include source and
fiber-data recovery, no source erasure under regrouping, the fiber criterion,
the zero-fiber obstruction and impossibility of choosing every fiber.
Receipt: `retained-observation-fibers-formal.json`.

Next: encode this ALL-fiber family in the actual native graph/table interface,
including empty fibers, WITHOUT requiring a chosen complete package in every
fiber. Prefer unpointed family graphs where appropriate; only the supplied
source point needs to mark the total. Keep representation recovery distinct
from admission by a constructor rule. No owner modification or automatic new
seed authorization is inferred.
