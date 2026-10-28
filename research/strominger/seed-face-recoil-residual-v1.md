# The direct/indirect seed residual survives the shared mechanical reading

## Frozen comparison

Use the existing six-port tensor-feature adapter, its unchanged metric and pulse law, and the old preparation: one unit at record AB, zero carrier. Compare actual parallel directed routes AB and AD;DB. Their endpoints agree. No native equality/filled face between these free routes is presumed.

The seed adapter already establishes that their carrier/record actions differ. This follow-up computes the difference in the existing shared generalized recoil representation. It is not a new discovery of the source mismatch or a repeat of the unrelated 137-slot rectangle test.

## Exact result

Let e select record AB, F be the existing six features, D=F^T H F. On the real zero-configuration endpoints the shared mechanical readout is

    P0=F^T H y, pi=r.

The direct route gives (P0,pi)=(D e,0). The indirect route leaves the preparation unchanged and gives (0,e). Therefore

    direct - indirect = (D e,-e).

The AB partner momentum is respectively 0 and 1. Nevertheless both have the same total generalized momentum P0+D*pi=D e and endpoint kinetic energy 1/2. Conservation of those quantities does not imply equality of mechanical states or routes.

The readout is injective on y in span(F): y=F D^-1 P0, with r=pi. A faithful change to these body coordinates cannot erase the source mismatch. The checker verifies the endpoint intertwining equation for all six ports, rather than just interpreting one scalar. It preserves the old negative control: this same AB preparation leaves both return routes BA and BC;CA idle even though their operators differ.

## What is rejected

The hypothesis that these parallel routes can be flattened to equal full mechanical effects under this unchanged adapter is false. This is a concrete obstruction to one proposed face interpretation, not a counterexample to the existence of an actual native triangle, a nontrivial witness action, or a broader physical-domain representation.

The conserved total is a coarser observation than the full state. Nor does endpoint agreement furnish a native face certificate. A comparison may retain a nonzero response or act nontrivially on the attached state; it must then be represented as such, not silently as equality of final effects.

## Prior material relevant to the remaining comparison

- `research/nima/seed-port-response-descent-gate.md` proves that full-effect factorization through source/final ports, with injective primitive actions, forces parallel positive paths to have equal effects. It explicitly distinguishes this from factorization of a coarse observation.
- `research/nima/tetrahedral-comparison-feedback.md` already applies native feedback to an actual filled package. Its changed routes are new presentation histories, not AB and AD;DB; its geometric payload is atomic. This must not be mistaken for either missing generic feedback or an existing field-sensitive mechanical binding.
- `research/nima/seed-exchange-hypothesis-existing-instrument-realization.md` already supplies conditional instrument realizability and explains why primitive-addressed six-port actions differ from the composite-addressed 137-slot contract.

Thus the unresolved original-face binding is a comparison between actual retained native witnesses and attached response actions. It is not a request to make these free routes equal, to invent feedback or to find another compatible pulse model. Source selection of a physical attachment remains a separate assumption.

## Verification

`uv run --with sympy python research/strominger/checkers/check_seed_face_recoil_residual.py` passes with exact SymPy matrices. The checker reads the actual registry and pure exchange expressions from the existing owner implementations using AST selection, without executing their IO or rewriting their receipts. The mechanical endpoint equations are independently evaluated from the documented shared embedding.

Receipt: `results/seed-face-recoil-residual/verification.json`. This is fresh endpoint-level checking, not a full rerun of the shared cotangent/intermediate-pulse checker, native Agda proofs or apparatus experiment.
