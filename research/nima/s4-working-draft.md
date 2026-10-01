# S4 source structure — working draft

## Status

**Draft revision 2** (dependency-audit correction). This document is a **draft** for discussion.
It records what the existing Agda sources define; it does not freeze an
authoritative typed interface. The registry field `source_basis.status`
remains `unresolved`; no derivation may rely on this draft as a frozen
signature.

## Source basis: three layers of S4 formalization

The repository contains three distinct but related S4 formalizations.

### Layer 1: `S4Aut.agda` — raw automorphism group

| Item | Definition | Source |
|---|---|---|
| `Point` | `Bool × Bool` (four distinct points) | `S4Aut.agda` line 18 |
| `s-iso : Iso Point Point` | Transposition of two points, order 2 | lines 48–52, 80–83 |
| `t-iso : Iso Point Point` | 4-cycle on four points, order 4 | lines 54–57, 85–88 |
| `st-fun` | Composition s∘t, order 3 | lines 93–99 |
| Coxeter relations | `s² = t⁴ = (st)³ = 1` (proved ∀x) | lines 80–99 |
| `g-fun, h-fun: Point → Point` | Stabiliser generators (S₃), Coxeter g²=h²=(gh)³=1 | lines 101–132 |

**Type**: `Iso Point Point` carries a forward map, an inverse map, and
pointwise proofs of invertibility (rightInv, leftInv). The set constructor
is the dependent Σ over Point→Point for the inverse data.

The `s² = t⁴ = (st)³ = 1` equations use pointwise equality (∀ x, f(x) ≡ x),
not term-level equality of the Iso records. The source comments identify the full automorphism group with S₄. The checked
terms exhibit generators, inverses and pointwise relations; this module does
not itself supply a 24-element enumeration or a proof of completeness of the
presentation. Do not treat those comments as checked cardinality evidence.

### Layer 2: `BoundaryGeneratedQuestions.agda` — Filler

| Item | Definition | Source |
|---|---|---|
| `Filler a b` | `Σ (El (retained a) ≃ El (retained b)) (λ e → equivFun e (value a) ≡ value b)` | `BoundaryGeneratedQuestions.agda` lines 19–21 |
| `identity a : Filler a a` | Id-equivalence with refl pointed witness | line 32 |
| `compose` | Composition of two fillers | lines 34–35 |
| `inverse` | Inverse of a filler | lines 36–37 |
| `swap-filler : Filler fourQ fourQ` | Coordinate swap on Bool×Bool, with pointed witness | lines 129–134 |
| `fillers-distinct` | identity ≠ swap-filler (fourQ has at least two distinct fillers) | line 135 |

**Key difference from layer 1**: `Filler a b` is a dependent sum that
pairs an **equivalence** between the retained types of two complete packages
with a pointed **compatibility witness** that the equivalence maps value a
to value b. The full automorphism group `Iso Point Point` from layer 1
carries no pointed witness; a `Filler` carries one.

`swap-filler` is the concrete filler whose underlying equivalence corresponds
to the coordinate swap `(x,y) ↦ (y,x)`. This is equivalent to the S₄ element
that swaps Bool coordinates.

### Layer 3: `RelationalCarrier.agda` — carrier interpretation

| Item | Definition | Source |
|---|---|---|
| `Carrier` | `Point` (Bool×Bool) | `RelationalCarrier.agda` line 41 |
| `Aut` | `R.Filler = B.Filler B.fourQ B.fourQ` | lines 53, 49, via RetainedComparisonSeries |
| `swap : Aut` | Aut element from swap-filler | line 58 |
| `twist : Aut` | Aut element from twist-filler | line 61 |
| `swap² = 1` | Proved as swap-twice-fst | lines 67–68 |
| `twist² = 1` | Proved as twist-twice | lines 70–71 |
| `signature-faithful` | Two-probe readings are injective on points | line 84 |
| `four-distinct` | All six point pairs are type-distinct | lines 86–96 |

**Key point**: `Aut` in the carrier is not `Iso Point Point` but
`Filler fourQ fourQ`. The chain is:
`RetainedComparisonSeries.Filler = BoundaryGeneratedQuestions.Filler`
applied to `B.fourQ` and `B.fourQ` (both `fourQ = E-package Bool … false`).

## Relationship between layers

```
RelationalCarrier.Aut = Filler fourQ fourQ
    ↓ forget pointed compatibility witness
El (retained fourQ) ≃ El (retained fourQ)
```

There is no automatic map from an arbitrary `Iso Point Point` to a pointed
self-filler: it must also preserve the selected value. In general types,
pointed witnesses may carry higher information. For this four-point set,
point equality is propositional, so proof multiplicity must not be asserted
as a source of distinct fillers.

## Structure maps

| Name | Arity | Codomain | Source |
|---|---|---|---|
| Filler.identity | `Complete → Filler a a` | identity filler | `BoundaryGeneratedQuestions.agda` line 32 |
| Filler.compose | `Filler a b → Filler b c → Filler a c` | composition | lines 34–35 |
| Filler.inverse | `Filler a b → Filler b a` | inverse | lines 36–37 |
| Filler.transport-question | `Filler a' a → Filler b b' → Filler a b → Filler a' b'` | transport | lines 42–44 |
| swap² | `∀ x, swap(swap(x)) = x` | involution | `RelationalCarrier.agda` lines 67–68 |
| twist² | `∀ x, twist(twist(x)) = x` | involution | lines 70–71 |

## Permitted constructions

1. Form identity, composition, inverse of fillers (layer 2 operations)
2. Transport fillers along other fillers
3. Retain pointed compatibility evidence; do not assert distinct proofs for the four-point set
4. Retain a filler as a Complete package (retain-filler)
5. Apply a filler as a Resolve transition (Application.perform)
6. Apply Coxeter generators to Point (layer 1 raw operations)
7. Distinguish points by two-probe signature

## Equations

- Coxeter relations: s² = t⁴ = (st)³ = 1 on Point (layer 1)
- Stabiliser: g² = h² = (gh)³ = 1 (layer 1)
- swap² = 1, twist² = 1 (layer 3)
- Filler compose associative with identity and inverse (layer 2)
- Filler transport composes with other transport (layer 2)
- signature-faithful: two-probe readings injective on four points (layer 3)

## Equivalence criterion (as defined in source)

Full type-theoretic equality of the filler Σ record is the criterion; pointed
fillers are not interchangeable with arbitrary S4 automorphisms. For the
four-point set, different compatibility proofs do not by themselves establish
distinct fillers. In particular, `identity fourQ`
and `swap-filler` are distinct even though their eta-truth values agree
(`truth-identifies-fillers`). Full type-theoretic equality of the Σ record
is the criterion.

## Boundary

This draft covers the mathematical S4 formalization only. It does not include:
- The generating grammar rules (Node, P-kind, Resolve, seed/apply)
- The retained-path or comparison-successor ledger operations
- The carrier probe adapter or physics interpretations
- A derivation from S4 to any grammar operation

## Dependency audit evidence

`checkers/check_interpretation_dependencies.py --write --self-test` records
local import edges, source hashes, explicit conditional DG interfaces and
hash-matched fresh-closure receipts in `results/interpretation-dependencies.json`.
It now covers thirteen roots and their local closure. The aggregate fresh check
also binds the compiler executable and all 1091 Cubical .agda sources, with
before/after inventory stability. This does not certify compiler built-in data
or semantic derivability from these source sorts. Compilation of
`RelationalCarrier` currently reports an unused/missing-export import warning
in `FibrationSigmaPiBridge`; a passing receipt does not mean warning-free.
The local audit is not sufficient to freeze this signature.

## Non-claim

The S4 object provides the carrier and automorphism structure for the
physics model. It does not generate the native grammar, supply arbitrary
type families, or determine admission certificates. Any future derivation
from S4 to a grammar operation must account for the additional data the
grammar requires beyond what S4 provides.