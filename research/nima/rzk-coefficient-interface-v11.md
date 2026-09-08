# v11: typed polynomial/Cech carriers and connector normal variation

**Superseded coefficient-checkpoint status:** see
[`rzk-coefficient-interface-v12.md`](rzk-coefficient-interface-v12.md). The
full 215-cell finite and Cech square-zero certificates and Lambda chain law now
pass fresh headless closure checks.

Original objective: coherent integer indexing, concrete coefficient modules,
and derived-Hom realization status. This checkpoint advances the actual
coefficient instantiation, but is not a completed R0-linear derived realization.

**Subsequent five-row update:** [objective impact](five-row-objective-impact.md)
records universal target-boundary-zero primitives for the two specified finite
sources and strict row vanishing on a specified homogeneous normalization
sector. Missing row values no longer block that finite-source coefficient
nullity result; stronger source admissibility and the formal gates below remain.
The packets and their derivation/impact links are now in the research graph.

## Freshly checked Rzk work

- `rzk/18-finite-coefficient-presentations.rzk.md`: 24 definitions and one
  parameterized datatype. Finite integral sums, evaluation equality, additive
  and integer-scalar laws, linear extension, congruence, composition and a
  generator-wise square-zero lifting theorem. A 70-file closure passed in
  29,960 ms. Result: `results/18-finite-coefficient-presentations.typecheck.json`.
- `rzk/19-loaded-polynomial-cech-modules.rzk.md`: 20 definitions and the actual
  215-constructor cell datatype. A 71-file closure passed in 41,363 ms with
  source/executable hashes stable. Result:
  `results/19-loaded-polynomial-cech-modules.typecheck.json`.
  Execution: `structured_command_execution:e_39824_1788736671850406200_72`.

Module 19 is not merely the homogeneous Hom slice. It contains the full finite
and Cech coefficient carriers, all 522 signed differential arrows, polynomial
scalar-action operations, cochain degree and degree-sorted carrier types, and
the actual diagonal finite-to-Cech coefficient map Lambda.

Each monomial has nine natural occurrence exponents. The nine normal exponents
are natural unless the cell's F-minus-H permits inversion, in which case they
are canonical integers. The types therefore prevent insertion of inverses on
illegal source/target summands. Each coefficient expression is a finite sum.
The generator and the complete cell-label table are recorded in
`checkers/build_loaded_polynomial_cech_rzk.py` and
`results/loaded-polynomial-cech-generation.json`.

### Representation boundary

These are **setoid presentations**, with equality defined by equality of every
integer-valued linear basis evaluation. They are not automatically quotient
identity types. Module 18 proves the displayed finite-sum laws; module 19
constructs the concrete bases and operations. The full R0-module axiom package,
well-definedness of the complete polynomial action, graded differential closure,
and a bridge to the identity-based Hom interfaces remain to be proved.

### Square-zero verification is not complete

`rzk/20-loaded-coefficient-square.rzk.md` is a bounded proof checkpoint for
cell 0 only, in both models. It is NOT a successful 215-cell square certificate.
The larger generated proof exceeded its bound. Named cell lemmas isolated the
cost to the first finite-cell proof. Splitting off syntactic column expansion
and bundling cancellation arguments still did not yield a passing 60-second
checkpoint. No timeout was promoted to success and no bound was raised.

The latest module-20 result is `timed_out`. Its own source hash matches, but
its recorded dependency closure predates the final addition of degree and
Lambda operations to module 19. The closure must be rebuilt before another
check. Module 18/19 successful hashes remain current.

Next proof work should inspect the normalization cost at the integer-evaluation
bridge, rather than run the same large proof again. Lambda's chain-map law and
the endpoint-relative quotient have not yet been kernel-checked here.

## New connector result: replayed, with scope retained

Incoming report:
`research/chatgpt/mixed-connector-normal-variation/mixed_connector_normal_variation.md`.

The read-only wrapper `checkers/check_mixed_connector_import.py` reproduced
**82,427 assertions** in 462 ms and matched all 215 Cech columns against the
live Voevodsky target. It also reproduced the prior nonzero derived detector.
Evidence: `results/mixed-connector-variation-replay.json`; execution
`structured_command_execution:e_39824_1788736420763267200_66`.
No other-owner files were written and the claimed repository commit was not
authenticated. This replay is not an Rzk verification of the new identities.

The key full-map identity is

    delta(J_b^E A_a - A_b J_a^S) = T^E kappa - kappa J_b^S J_a^S.

Thus a coefficient-flat collapsed source has an explicit primitive for T kappa.
Its Q component is zero; endpoint components also vanish under the stated
independence condition on the COMPLETE endpoint comparison, not merely on an
endpoint permutation or scalar trace. Whole-diagram arrows and higher
coherences still require their own connection compatibility.

The actual exceptional normal instead has

    u_E = u_03 + u_13 + u_03*u_13,

so its normal variation is nonzero. The flat-source theorem cannot simply be
applied to it. Both twenty-state local chart composites admit the checked legal
primitive, while the full connector action obeys

    [T kappa] = -[R kappa].

The remaining five incoming rows are explicitly exported by the replay. Their
actual source-to-target connector components are still absent. Neither the
local chart maps nor the collapsed-source coefficient result selects the full
physical Q-homotopy or constructs the raw-to-collapsed Gysin comparison.
