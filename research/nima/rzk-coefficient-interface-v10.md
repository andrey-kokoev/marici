# Coefficient interface v10: actual integer Hom square zero

Original objective: **coherent integer indexing, concrete coefficient modules,
and derived-Hom realization status**. This objective remains only partially
fulfilled. This increment closes the general assembled square-zero gap identified
in the [code review](rzk-integer-coefficients-review.md); it does not close the
physical coefficient or derived-realization gates.

## Checked increment

Source: `rzk/17-integer-hom-square.rzk.md` (24 definitions).

- `nima-integer-hom-post` and `nima-integer-hom-pre` are the actual transported
  operators underlying module 15, not arbitrary operator parameters.
- Transport preserves a specified zero section and binary operation, and
  commutes with a dependent differential. These statements use identity
  induction, not an assumption about transport.
- Their squares vanish from the component differential squares; pre-square
  uses the original Hom family's explicit zero-preservation witness.
- Mixed pre/post compositions agree by differential naturality, composition
  of transports and canonical integer identity-path uniqueness.
- `nima-integer-hom-differential-square` proves the square of the actual
  parity-selected differential is zero for every integer Hom degree n,
  source degree i and vector x. The outer parity is rewritten using the
  proved successor-flip law, including the negative/zero transition.
- `nima-z2-target-hom-square` instantiates all target arithmetic and operator
  laws on the existing Z-squared coefficient complex. Its source can be any
  pointed integer-indexed square-zero complex, and the Hom family must
  preserve zero. This is not restricted to the single map H from module 16.

The theorem's component assumptions are explicit: source/target square zero,
target differential preservation of addition/subtraction, the relevant target
zero/cancellation laws, and zero preservation of f. The previously conditional
pre/post operator laws themselves are now derived. No function-extensionality
axiom is used: the conclusion is pointwise. Closure of the full additive/scalar
linearity predicate under the differential remains a packaging obligation.

## Fresh verification and review evidence

- Final 82-file closure passed on 2026-09-06 at 22:30:29 UTC.
- Rzk elapsed time: **27,975 ms**; unchanged 120-second bound; no timeout.
- Source/executable hashes matched before and after verification.
- Result: `results/17-integer-hom-square.typecheck.json`.
- Manifest: `results/17-integer-hom-square.closure.json`.
- Execution: `structured_command_execution:e_39824_1788733829427132300_37`.
- The general theorem passed its first check before the concrete specialization
  was appended. The specialization also passed on its first check.

The closure builder now separately records literal #variable/#variables
parameter declarations. The sHoTT core has section parameters which Rzk prints
as #assume while checking; an empty literal #assume scan was NOT a complete
assumption audit. Existing proofs remain parameterized as indicated by their
signatures. No new #assume, variable declarations or physical inputs were added
to module 17. Upstream staged-source provenance is still not authenticated.

The manifest's added parameter metadata does not alter the checked Rzk sources,
file order or input hashes.

## Incoming coefficient result (subsequent update)

The [mixed normal/Chern integration review](mixed-normal-chern-integration-review.md)
records a successful replay of all 2,755 new ChatGPT checks and exact agreement
of all 215 Cech columns with the live target. A bounded free finite
endpoint-relative source now justifies derived Hom for the finite-to-Cech
coefficient pair and detects a primitive degree-two class. This is not yet an
Rzk instantiation or a normalization-to-physical comparison. The source-specific
qualification matters when reading the remaining gates below.

## Remaining objective gates

1. **Linear Hom and DG structure:** show the actual differential and composition
   preserve the full linear-map predicate; establish general graded Leibniz
   with index transports. The current square-zero result is stronger than a
   finite window but is not a packaged DG category.
2. **Intended concrete coefficients:** construct the polynomial/localized
   diagram and stalk modules and instantiate their maps/differentials, including
   the original-fibre-to-split coordinate change. Z squared is a genuine
   coefficient pilot, not the 215-generator physical target.
3. **Derived Hom:** identify a specific replacement P -> N of the intended
   normalization source, prove it is a quasi-isomorphism and justify the
   K-projective (or alternative suitable) property needed for Hom(P,-) to
   compute RHom(N,-). Being degreewise free without a suitable boundedness or
   other argument is not enough for an arbitrary unbounded complex.
4. **Framed realization:** relate the appropriate mapping-space realization of
   the derived Hom complexes, naturally with respect to the boundary restriction,
   to the module-11 homotopy fibre. A correspondence of raw cochain primitives
   alone does not establish this mapping-space comparison.

The physical Gysin identification and its Q-homotopy remain external inputs.
No vanishing/nonvanishing physical class or physical parity is selected here.
