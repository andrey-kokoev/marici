# Seed tetrahedron bridge: the bottom surface arrives with its filler

## Source-relative skeleton

`agda/SeedTetrahedronBridge.agda` maps the six seed occurrences into an explicitly declared free geometric realization: vertex constructors and one path constructor per occurrence, with no face relations added. This is a new path interpretation, not a claim that the literal four vertex constructors were already equal or that the free directed histories were invertible.

Use tetrahedral order (A,D,B,C). The six edge slots are:

| Slot | Realized path | Provenance |
|---|---|---|
| AD | AD | Primitive |
| DB | DB | Primitive |
| AB | AB | Primitive, retained independently |
| BC | BC | Primitive |
| DC | DB followed by BC | Derived diagonal |
| AC | reversal of CA | Reversal in the declared path interpretation, not a primitive AC row |

BA remains an independent path constructor; it is not identified with reversed AB. The corresponding `ReverseAB` type is recorded but not inhabited. Original directed histories remain in the preceding source modules; geometric realization does not replace them.

The DBC triangular face is reflexivity because its diagonal was defined as DB followed by BC. Two further sufficient face inputs are precisely:

    ForwardFace : AD followed by DB = AB
    TriangleABC : AB followed by BC = reverse CA.

These types are formed, not derived from endpoint incidence. The bridge is conditional on supplied inhabitants. No assertion of their impossibility in every interpretation is made.

## Paired completion, including independently supplied bottom data

The operator's recollection is correct: the existing constructor returns a dependent pair of missing face and filler over that face. It does not first supply an arbitrary face and later an unrelated filler.

For given ForwardFace and TriangleABC, the bridge uses existing `unique013` to construct the previously unsupplied ADC side face together with its coherence, retaining ABC. That supplies the horn accepted by `RetainedTetrahedralPackage.Cells.build`.

The actual generated ABC bottom and filler are then recovered as one value:

    bottom-and-filler : Missing023 forward face-DBC face-ADC.

Contractibility of this exact completion fiber proves

    bottom-and-filler = (supplied ABC, supplied-bottom-filler).

The module separately derives the face equality and the dependent path comparing fillers along that face equality. This is stronger and more correctly typed than an unqualified equality between fillers over different faces.

**Scope of that agreement:** the ADC face was generated compatibly from the supplied ABC. It was not an independently fixed face changed retrospectively. This theorem does not say that arbitrary independently supplied faces automatically agree or fill a tetrahedron. If all faces are independently fixed, their coherence remains an obligation.

## Control against silently replacing seed edges

The module also constructs an unconditional tetrahedron using only the three-edge spine AD,DB,BC, with every diagonal defined as a composite. Associativity suffices there. That easy completion replaces the independently supplied AB and reversed CA by composites, so it is explicitly NOT counted as the requested source-preserving bridge.

## Disposition

We now have a checked conditional bridge with a source-relative skeleton, identified face obligations, and a bottom-surface/filler pair whose agreement with retained supplied data is proved. The operator's correction is incorporated in the actual returned packet. No filler was postulated and no scalar coupling introduced.

What remains is to obtain the ForwardFace and TriangleABC witnesses from a justified interpretation or retain their discrepancies. The free six-arrow seed has not thereby become a physically filled tetrahedron, and no back-reaction dynamics or gravitational constant has been derived.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module SeedTetrahedronBridge -Fresh

Fresh safe Cubical/guardedness check passed, with ignored interfaces and stable inputs. Receipt: `results/agda-SeedTetrahedronBridge.json`. Finished 2026-10-05T20:25:54.5886463Z. Source SHA-256: `7c80f095dc5dd500ba46ef77f600bbd5115396edd290191290ce7c18bb78c9f0`.

The preliminary draft also checked, but was revised to retain and compare the paired bottom explicitly; the receipt above verifies the revised source. No postulates or unresolved holes were introduced. No ledger entry, commit or publication is claimed.
