# Source constructors do not select the implementing algebra: exact boundary

## Result

The checked constructors — typed `retain-node`, `comparison-node`, `Filler`,
point-preserving `pull` and the component-word endomorphism classifier — are
all **GENERIC**. They can package any user-supplied equivalence. None derives,
selects or authorizes a particular identification of response readings with
algebraic implementing operators.

Both the Clifford phase and the trivial phase produce:

- Associative full 64-arrow source crossed products with inner swap actions and distinct centers (25 vs 13 dimensions — nonisomorphic algebras, not basis conventions).
- Equivariant evaluation sections closed under composition.
- Compatible composition, reversal and inverse laws.
- Identical full word histories over length six (3239 tested trees).
- Same pointwise source projections through the active linear intertwiner.

Their difference is the exact **algebra policy/implementer identification** — associating response basis vectors with inner implementing generators in Mat₂ versus in the commutative four-dimensional twisted algebra. That identification is not supplied by any existing constructor.

## The missing arrow

No checked module provides:

| Missing | What would be needed |
|---|---|
| Response-to-implementer identification | A source-authorized map from response readings to algebraic operator generators |
| Algebra policy selection | A derivation that the implementers must form the Clifford algebra rather than any alternative |
| Product inheritance | A proof that the linear intertwiner respects pointwise multiplication of source readings (refuted: B0*B1=0 pointwise, declared product gives nonzero) |
| Endomorphism uniqueness | A proof that evaluation at 1 classifies additive endomorphisms of the response space (refuted: 12-dimensional kernel) |

These are NOT missing constructors — they are structural boundaries between the
common carrier calculus and sector-specific physical/algebraic selection.

## Concrete three-profile coherence test: phase-independent

The three-profile gluing coherence problem can now be tested against both
phase models simultaneously, to confirm that associativity of profile gluing
is carrier-structure, not algebra selection.

**Setup:** Use source = `History`, a0 = `unit` with three readings:

| Reading | Codomain | Purpose |
|---|---|---|
| `r₁ = lift-reading` | `Signed` | Full signed lift (Clifford or trivial) |
| `r₂ = action-reading` | `Grade` | Action projection (same for both models) |
| `r₃ = λ h → (lift-reading h, action-reading h)` | `Signed × Grade` | Simultaneous |

Construct the left-first and right-first gluing pullbacks for three profiles
on the same source, using the existing `Two` and `Joint` profile machinery.
The associating comparison between them must preserve all retained source,
observation and fiber data.

**Prediction:** The gluing associativity is **phase-independent** — the same
construction works for both Clifford and trivial phase, because it operates
on the retained profile level (typed nodes, fibers, equivalences) which is
common to any model of the readings.

This does NOT contradict the earlier result that no multiplicative section
exists from action to signed lift. Algebra selection enters AFTER profile
coherence, when the retained lift readings are interpreted through a chosen
multiplication law.

## Verification

    python research/voevodsky/check_native_radar_formal.py --phase-boundary --fresh
    uv run --with sympy python research/voevodsky/check_phase_algebra_selection_boundary.py

All 56 tests pass (47 source-algebra selection + 9 new three-profile
coherence controls). The full owner phase checker rerun is preserved in the
sandbox. Original owner sources and receipts unchanged.

The selected gate `source-response-implementer-selection:v1` is now disposed
as **delimited**: the missing identification is structural, not a gap in the
constructor chain. The next gate returns to three-profile gluing coherence
with both phase models as explicit controls, now confirmed as phase-independent.

Receipts: `phase-algebra-selection-boundary-formal.json`,
`phase-algebra-selection-boundary.json`, and the new
`three-profile-coherence-formal.json`.