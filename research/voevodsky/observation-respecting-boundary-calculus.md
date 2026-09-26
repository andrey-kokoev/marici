# Observation-respecting boundary calculus

Fresh resume selected `observation-respecting-boundary-calculus:v1`.
The compatibility condition is now a checked reusable interface over the actual
owner boundary fillers and native comparison operations, not a replacement
carrier language.

## Definition and closure theorem

Given complete packages a,b, independently supplied observation maps
r:El(a)->V and s:El(b)->V, an observed filler consists of:

1. an actual `BoundaryGeneratedQuestions.Filler a b`, i.e. an equivalence e
   with its marked-point comparison;
2. a compatibility witness

       forall x, s(e(x))=r(x).

The common output space means the observations have already been aligned in
units, frame and channel interpretation. This alignment is supplied, not inferred
from equal output types or an arbitrary carrier equivalence.

`agda/ObservationRespectingBoundary.agda` proves closure under the owner's
identity, inverse and composition operations. For composition, the two
commuting squares compose. For inverse, use the original square at e^-1(y)
and the right inverse law. No injectivity of the observation is required.

These are operations on proof-relevant certified fillers. This turn does not
claim an additional strict groupoid or a complete higher-coherence formalization.
Compatibility is stated on the entire declared carrier. For a model requiring
only an admitted subdomain, that domain must be supplied explicitly rather than
silently treating every raw payload as physically admitted.

## Refinement theorem, with its proof-relevance qualification

For a fixed e, compatibility with a paired observation (r,u) is isomorphic to
compatibility with r AND compatibility with u. The module proves this isomorphism,
including both inverse laws. Projection therefore forgets a finer certificate
and cannot create a missing finer certificate.

For general output types, these witnesses may carry higher information: do not
call the forgetful map an injective map of ordinary sets without qualification.
When the output is a set, the module proves that compatibility is a proposition.
In that case it is an ordinary restriction on underlying fillers. In either
case, finer compatibility entails coarser compatibility.

## Native integration and evidence retention

The same certified interface is implemented over actual native packages and
native marked equivalences. Native identity, inverse and composition are checked;
`native-rule` produces the owner's actual `compare-kind` operation.

The source-to-native theorem accepts INDEPENDENT native observations and explicit
pointwise comparisons with the source observations. It transports the commuting
square along those comparisons. It does not define the native reading by
calling a legacy decoder.

Both source and native certificate packages retain the actual rule output AND
the compatibility witness, with recovery equalities. These are retention
constructions, not automatic source-admission proofs. The projection to a raw
rule alone forgets this extra certificate; the owner's unrestricted rule API
has not been globally changed or claimed to enforce our wrapper.

No owner artifact was edited or adoption inferred. Source policies, analytic
truth, and completion certificates remain separate obligations.

## Actual tidal instance and strict refinement

The preceding retained Newtonian/Rosen pair instantiates the common electric
reading with its actual source and native packages. The common observation is
identity on the electric tensor in the already fixed frame and units.

On the finer payload (E,g), the previously checked gradient-shift equivalence

    (E,g) -> (E,g+144)

has an electric-only compatibility certificate. This is expressly a weaker VIEW
of the fine payload, not authorization for its full attached physical profile.
The selected gradient numerators are -144 and 0 over denominator 13824.

The module proves that NO filler between these selected refined packages can
preserve the joint identity observation. Consequently no automatic upgrade from
an electric-only certificate to the full certificate exists. This rejection
uses the actual retained source pair, not the synthetic finite test domain.

The unrestricted shift remains bijective and isometric; it does not collapse
points within its carrier. It fails because it changes the named calibrated
observation. Thus metric control cannot replace compatibility with independent
physical readings.

## Remaining authorization boundary: observation substitution

There is another explicit, compiler-checked control: every unrestricted filler
preserves a constant Unit-valued observation. In particular, the otherwise
rejected shift becomes compatible if a caller is allowed to replace the intended
physical observation by that constant map.

This is not a contradiction in the calculus. Its theorem is relative to the
SUPPLIED maps. It shows precisely why a physical application must bind those
maps to its authorized source/profile data. Merely retaining a profile label
while accepting an arbitrary unrelated function does not establish that link.

The next leaf is therefore a profile-bound admission gate for this concrete
native application, with an attempted constant-observation substitution as a
rejection control. The existing code does not yet claim that gate.

## Verification

Run:

    python research/voevodsky/check_native_radar_formal.py --observed-boundary --fresh
    python research/voevodsky/check_observation_respecting_boundary.py

Fresh safe/cubical closure passes, including the actual retained tidal
construction. Source-record erasure and false gradient preservation reject for
the intended type mismatches. The exact audit passes 38 checks.

Its small permutation test is explicitly synthetic: a five-element domain has
120 unrestricted permutations, four preserving absolute value, and only the
identity preserving the joint (absolute value, signed value) observation. It
checks finite closure/refinement behavior; the universal results rest on Agda
proofs, not enumeration or claims about new physical sources.

Receipts: `observation-respecting-boundary-formal.json` and
`observation-respecting-boundary.json`.

The physical source derivations remain the digest-pinned written evidence from
the preceding leaf. No continuum field-equation verification, rational
normalization/refinement completion, or universal physical foundation is
claimed by this boundary-calculus result.
