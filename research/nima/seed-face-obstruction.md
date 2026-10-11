# The free seed realization refutes the two proposed face equalities

## Exact question

Can the face inputs of `SeedTetrahedronBridge.WithFaces` be constructed from that module's declared free geometric realization?

The required types were:

    ForwardFace : AD followed by DB = AB
    TriangleABC : AB followed by BC = reverse CA.

`agda/SeedFaceObstruction.agda` proves that BOTH types are empty in that specific realization. This strengthens the prior “not supplied” boundary to an explicit obstruction. It does not refute other interpretations or all WG-generated comparisons.

## Diagnostic construction

Define a Boolean-fiber family over the actual realization. Every vertex has fiber Bool. Traversal AB transports by Boolean negation (via univalence); the other five primitive paths transport identically. Since the realization has no face relations, this is a valid family, checked by the compiler.

Starting from false:

| Path | Transported probe |
|---|---|
| AD DB | false |
| AB | true |
| AB BC | true |
| reverse CA | false |

An equality of either proposed pair of paths would identify these transported values. The compiler-checked proofs derive a contradiction using true != false. Transport through composed paths is justified by the library's `substComposite`, not numerical evaluation or an informal parity assumption.

The Boolean probe is a mathematical discriminator, not a chosen physical payload, response law or new source coefficient. Its existence proves that the free realization cannot force the requested equalities.

## Consequence for paired completion

The bottom-face/filler completion theorem remains valid for its stated inputs. It cannot create the missing inputs or override this obstruction. The previous conditional `WithFaces` module is therefore not instantiable in the chosen free realization; its source-preserving filled tetrahedron has not been constructed. The separate all-composite spine control still fills, but replaces the independent seed edges and remains outside the claimed bridge.

Progress now requires an explicit new interpretation or relation. For example, a quotient could adjoin the desired faces, but would no longer retain this probe as a compatible observable; it must not be described as recovering a relation already present. A coarser effect comparison can instead coexist with separately retained source histories, provided its meaning and response law are supplied. Retaining the discrepancy without imposing equality is also valid.

No impossibility of gravitational physics, no universal WG obstruction, and no choice of the correct additional law is established here. The concrete finding is that further normalization or horn completion alone cannot derive these faces from the free seed realization.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module SeedFaceObstruction -Fresh

Passed first run with safe Cubical/guardedness flags, ignored interfaces and stable inputs. Receipt: `results/agda-SeedFaceObstruction.json`. Finished 2026-10-05T20:29:30.7713728Z; source SHA-256 `87a939a1d6f9e743a922375f7005a8b4d304e8d51040d71c9a9bc8919f3a45b8`.

No postulates or unresolved holes were added. No ledger entry, commit or publication is claimed.
