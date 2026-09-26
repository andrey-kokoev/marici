# Presentation, restriction, and observation agreement are different claims

The operator redirected work from the pending massless unitarity cut to
structural synthesis. Fresh resume still selected that cut; it remains deferred,
not resolved by this interface.

## Checked interface

`agda/TypedPhysicalComparisons.agda` fixes an observation type V. An observation
object has a carrier, a marked point and a reader into V. It distinguishes:

| Claim | Required evidence | Permitted conclusion |
|---|---|---|
| Observed map | pointed map commuting with readers on all inputs | selected observations transport |
| Presentation | observed map plus equivalence evidence | invertible change of presentation |
| Restriction | observed map plus a specified left inverse | split inclusion, not surjectivity |
| Agreement | equality of readings at the marked points | selected outputs agree only |

Restrictions here are SPLIT injections. This is sufficient for the scalar-plane
example, not a claim that every embedding has a retraction. Its retraction is
not itself assumed to preserve every physical reading.

The formal interface proves identity and composition for observed maps,
inverse and composition for presentations, composition for restrictions, and
conversion from presentation to restriction. Every observed map induces marked
agreement. Postcomposing readers with any coarsening map preserves each of these
comparison types. A fine certificate can therefore be forgotten; no automatic
refinement operation is supplied.

These are proof-relevant types and operations. This turn does not claim a full
strict category, all higher coherence laws, or an authorization policy derived
from carrier structure. The readers must still be independently justified.

## Three instantiated distinctions

### 1. Actual chart comparisons are presentations

An adapter accepts the actual owner's retained-package `Observed` filler and
extracts its pointed, readout-preserving equivalence. It instantiates the three
checked action-jet charts from `ActionChartComparison.agda`.

The abstract observation object deliberately forgets source provenance. The
adapter separately retains the original complete-package certificate through
the existing owner-compatible retention operation and proves its recovery.
It must not replace the complete source/history package with the abstraction.

### 2. The scalar plane is a restriction, not a presentation

An exact integer tangent-coordinate model uses

    i(x)=(x,0,0), r(x,y,z)=x.

It preserves the declared scalar coordinate and has r(i(x))=x. The formal proof
exhibits an off-plane point with no preimage, so this inclusion has no right
inverse.

A stronger result excludes ANY presentation preserving that fixed observation:
the source fiber over scalar value zero is a singleton, while the target fiber
contains (0,0,0) and (0,1,0). Invertibility plus reader compatibility would force
those distinct states to coincide. This is an observation-fiber obstruction,
not an assertion about bare cardinality: the raw integer carriers can have
other equivalences that fail the specified reader condition.

The integer model is a structural tangent-coordinate test, NOT a formal proof
of real target geometry. The separate symbolic physical packet established
that the actual scalar plane is classically consistent while the full target
permits nonzero mixed scattering. The interface classifies that distinction;
it does not manufacture its physical evidence.

Notice that an inclusion may preserve even a rich reader ON ITS IMAGE and
still omit target states. Failure of full equivalence is not always a failure
of its commuting square. The missing surjectivity matters separately.

### 3. Marked agreement is weaker still

A compiler-checked Boolean example has equal readings at the selected point
but admits NO observation-preserving map at all. Thus marked agreement cannot
be promoted even to a map, let alone a presentation.

The physical refinement example supplies canonical profiles

    logarithmic: ((2,16),512), quartic-truncated: ((2,16),0).

They agree after forgetting the sixth entry; their full profiles are provably
unequal. The physical coefficients were calculated previously, not derived by
this type definition. Agreement can compose as equality of selected outputs;
that does not create a transformation of the underlying states.

## Structural consequence

The earlier strategy of representing every comparison as an equivalence plus
guards was too narrow. There are at least two independent questions:

1. Does the proposed map preserve the authorized observations?
2. Is it invertible, a restriction, or merely evidence of matching outputs?

Keeping these separate explains all three examples without either rejecting a
valid restriction or promoting a partial agreement to a physical identification.
The new stronger obstruction suggests the next structural theorem: characterize
observed presentations by equivalences of their fibers over the SAME observation
space. This should connect directly to the existing dependent/fibration
infrastructure, while retaining the independently supplied physical readers.

## Verification

    python research/voevodsky/check_native_radar_formal.py --typed-comparisons --fresh

Fresh safe/cubical closure passes. The upstream potential-only and false-sixth
rejection controls also fail as intended. The new no-map, no-right-inverse and
no-observed-presentation results are positive universal impossibility proofs in
the main module. Receipt: `typed-physical-comparisons-formal.json`.

No owner file was changed. No new amplitude, loop computation, continuum
completion or physical-policy selection is claimed.
