# Retained Resolution Calculus (RRC) and Dependent Substitution Calculus (DSC)

## Naming decision

The operator requested names for the two formulations, then requested that these names be documented and communicated to Nima. This note records that terminology; it does not rename source modules, change either calculus, or certify an equivalence between them.

## Retained Resolution Calculus — RRC

Name for the whole-package resolution formulation developed in Nima's research.

A complete package contains an expression and an actual value of its interpreted type. Expressions can retain prior packages, dependent families, maps, comparisons and actual witnesses. For an admitted seed family S, the witness-bearing closure has the form

    C(S) = Σ Q. Resolve(S,Q).

Resolve retains seeds, typed rule applications and their complete premise derivations. One closure operator accommodates multiple generator schemas, including dependent E/Pi and witnessed comparisons. Entire histories can be reified as subsequent complete inputs, with the required universe-level increase.

Nested histories admit flattening with unit and associativity laws. Flattening is not generally an equivalence on raw retained histories; reachability idempotence belongs to a separately truncated view. Comparison completeness remains relative to the specified source theory and guards.

Short description: **witnessed construction with retained provenance**.

Primary sources:

- `research/nima/coherence-resolution-closure.md`
- `research/nima/whole-package-generators.md`
- `research/nima/whole-package-universal-property.md`
- `research/nima/agda/WholePackageResolution.agda`

## Dependent Substitution Calculus — DSC

Name for the simplified dependent formulation developed in the Voevodsky resolution-net research.

Its semantic core is dependent context extension, substitution, application and witnessed transport. Supplying x:X determines the type Y(x) of the next input; a dependent continuation k applied to (x,y) returns a value of Z(x,y). Substitution composes these interfaces. A supplied comparison p:x=y acts on dependent data through transport in a family F.

“Substitution” is deliberately preferred to “single rewrite”: the semantic model inherits dependent functions and transport from Cubical type theory. A separate small object-language machine has explicit directed reduction and checked preservation, but is not a complete independent dependent type theory or a universal one-rule evaluator.

Short description: **dependent composition through typed interfaces**.

Primary sources:

- `research/voevodsky/resolution-net-v1/agda/ResolutionNetDependentSubstitution.agda`
- `research/voevodsky/resolution-net-v1/dependent-interface-foundation.md`
- `research/voevodsky/resolution-net-v1/dependent-machine.md`

## Relationship and limits

RRC describes admitted constructions together with their witnesses and histories. DSC describes how dependent inputs compose and how supplied comparisons act. The shorter presentation can move structure into types and whole input boundaries; it does not eliminate that structure or automatically retain histories.

Nima's native application-boundary construction is a concrete bridge:

    Application = Σ b:B. Σ out:Closure. eval(b) = out.

The one boundary input retains its full family, child histories and introduced indices. Treating it as one input does not manufacture missing premises. See `research/nima/native-branch-boundary-coordinates.md`.

These are complementary formulations with checked partial bridges. Neither their full equivalence nor reduction of all RRC generators to a single DSC rewrite primitive has been established. The names do not assert physical causality, universal computation-as-observation, or identity of raw histories with equal effects.

## Sufficiency research branches

The operator requested explicit branches for the remaining adequacy obligations. Their integration home is the observer-relative computation tree `issue-tree:b860b514b76f8592b7c7773d`, under `rrc-dsc-sufficiency:v1`. The graph admitted the addition as proposal `ep_bcd6a832-07b0-441e-930b-d6572aa026ce`, without a request to dispose of or replace the existing selected checkpoint.

Open children (node IDs use the integration tree prefix):

- `rrc-dsc-source-signature:v1`: admitted sources/generators and primitive-versus-derived structure.
- `rrc-dsc-witness-construction:v1`: constructing witnesses, not merely checking supplied evidence.
- `rrc-dsc-representation-bridge:v1`: faithful translations and scoped roundtrips; highest initial branch score.
- `rrc-dsc-comparison-coverage:v1`: transfer generated comparison witnesses, without identifying raw histories.
- `rrc-dsc-operational-realization:v1`: object syntax, reduction and semantic simulation.
- `rrc-dsc-observer-internalization:v1`: encode the checked observer interfaces and preserve their recovery/obstruction results.
- `rrc-dsc-resources-effects:v1`: explicit copying, ownership, commitment and cost boundaries.

Source/comparison work is cross-referenced to Nima's tree `issue-tree:ec9d8dc9a050db37f5f82cd0`; operational work to Resolution Net v1, `issue-tree:eaac890b531559a26d4086ec`. No change to either tree or assignment of another agent's ownership is implied. These branches test sufficiency; they do not assert that the two calculi are already sufficient.

## Coordination

This terminology is documented in the Voevodsky research area and communicated to `marici.Nima` for cross-reference through `marici-epistemic-graph`. The notice was admitted under proposal `ep_be41740e-3ddd-486e-9a7b-76fb99ec624a` (idempotency key `rrc-dsc-terminology-notice-to-nima-v1`). Admission records communication provenance, not confirmed reading or agreement. It does not assert that Nima has already adopted the terminology or authorize edits to Nima-owned artifacts.
