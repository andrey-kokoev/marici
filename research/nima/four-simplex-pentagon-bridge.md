# Independent marked pentagon: construction checked, comparison open

## Independent four-cell relation

`agda/MarkedFourSimplexCoherence.agda` now defines an old-style marked four-cell
using only path concatenation, the ten triangle equations, the five old
`MarkedTetrahedronCoherence` witnesses, and the Cubical library's associator
pentagon. It does not import the simplex decoder or either presentation bridge.

For four consecutive edges `p,q,r,s`, `Pentagon.WithFaces` names the five
bracketings:

1. `((p ∙ q) ∙ r) ∙ s`
2. `(p ∙ (q ∙ r)) ∙ s`
3. `p ∙ ((q ∙ r) ∙ s)`
4. `p ∙ (q ∙ (r ∙ s))`
5. `(p ∙ q) ∙ (r ∙ s)`

Each has a reduction path `r1` through `r5` to the marked diagonal `z`.
The five tetrahedra determine the pentagon's edges:

- `edge12` uses tetrahedron 0123;
- `edge23` uses 0134;
- `edge34` uses 1234;
- `edge15` uses 0234;
- `edge54` uses 0124.

The edges retain their witnesses, with explicit congruence-composition,
associator-naturality and interchange paths. `base-pentagon` reverses the
library's `pentagonIdentity` and normalizes its double composition.
`pentagon-tail` attaches the common terminal reduction path.

`FourCell h t` is the equality of the long three-edge route (1→2→3→4)
and short two-edge route (1→5→4), with that explicit boundary correction.
All five tetrahedron witnesses appear in the relation.

## Checked completion theorem

`edge34-equivalence` is an equivalence of the full 1234 witness space with
its whiskered pentagon-edge space. Prepending the fixed other long-route edges
therefore yields `long-route : T1234 ≃ Route`.

Consequently:

- `unique1234` proves contractibility of the missing-1234 completion pair;
- `complete` supplies the missing tetrahedron **and** its pentagon witness;
- `solve1234` identifies the four-cell relation with equality of the supplied
  fifth tetrahedron and the independently computed one.

This completion theorem is independent of the induced equation-family
completion. Contractibility of their respective completion spaces is not used
to claim their fifth tetrahedra coincide.

## Exact remaining comparison

`agda/FourSimplexPentagonBridge.agda` translates the ten Cubical triangles
by the established J-based face comparison and identifies all five old
tetrahedron types with those of the marked pentagon. Its `pentagon-horn`
retains the four supplied old tetrahedron witnesses unchanged.

It names two fifth-tetrahedron values:

- `induced-center h`: transport in the induced equation family from
  `FourSimplexEquationBridge`;
- `pentagon-center h`: the independent marked-pentagon completion.

The target `Goal` is a filler equivalence for **every fixed fifth tetrahedron**:

```agda
(h : B.EquationHorn) (t : B.O1234)
  → B.OldFourCell h t ≃ PentagonFourCell h t
```

The module proves both implications between this target and:

```agda
CenterCoherence = (h : B.EquationHorn)
  → induced-center h ≡ pentagon-center h
```

`from-center-coherence` constructs the target via the two filler-to-path
equivalences. `to-center-coherence` extracts the necessary center equality by
applying any proposed target equivalence to the canonical transport filler.
This establishes necessity and sufficiency, not an equivalence of the spaces
of all possible comparison choices.

`RouteCoherence` expresses the same obligation as the independent pentagon
route equation evaluated at the induced center; both conversions are checked.
`cubical-to-pentagon` then conditionally composes the established Cubical-to-
induced bridge with the proposed pentagon comparison.

## Canonical-completion reduction

`induced-center-on-image` now proves that the induced center on a translated
Cubical horn equals `translated-center`, the independently translated fifth
tetrahedron of its canonical Cubical completion. It is the fifth-face projection
of the already proved induced completion square. This compares two values in
the same induced presentation, not the independent pentagon center.

`GeneratedRouteCoherence` asks only for the independent pentagon equation on
these translated canonical Cubical completions. Its fifth tetrahedron contains
no old-to-Cubical decoder or endpoint-reindexing operation.
`from-generated-coherence` and `to-generated-coherence` prove that this is
necessary and sufficient for `CenterCoherence`; the former uses the checked
horn roundtrip to cover every old horn.

`extend-generated-coherence` extends such a proof to every actual Cubical
filled pair by dependent transport along its completion-space contraction.
Both the fifth tetrahedron and its four-cell witness are retained during this
transport. `goal-from-generated-coherence` constructs the full target
conditionally from the same canonical-completion proof.

**Neither `GeneratedRouteCoherence`, `CenterCoherence`, `RouteCoherence`, nor
`Goal` is supplied with an inhabitant.** The next proof must verify the explicit
marked-pentagon route for the translated canonical Cubical completion. Separate
uniqueness theorems for the two presentations do not supply that equation.

## Computation law and geometric sweep cube

The selected tetrahedron equivalence now has a proved computation law, rather
than being treated as an arbitrary equivalence of its boundary-indexed types.
`TetrahedronPresentationBridge.FixedBoundaryTarget.equivalence-route-computation`
exposes its route expression by naturality of the inverse-equivalence section,
transport in the path family, and cancellation of the route-derived correction.

`agda/PathSweepCoherence.agda` supplies `mapped-pathover-pasting`: mapping a
canonical transport filler and then its residual endpoint path agrees with
mapping the original dependent path. Its proof is an explicit square with
entry `f (i ∨ j) (transp (λ k → F (j ∨ (i ∧ k))) (j ∨ ~ i) (t j))`.
Applying it gives the stronger
`FixedBoundaryTarget.equivalence-sweep-computation`: the **existing** tetrahedron
map agrees with the direct route sweep, with its proved initial and terminal
corrections. No comparison map was replaced to obtain this theorem.

`horn-sweep-computation` and `center-sweep-computation` apply that law to all
five translated tetrahedra. `sweep-pentagon-normalization` is an equivalence
between the canonical-completion pentagon obligation and the independent
pentagon applied to those explicit sweep expressions. `generated-from-sweep`
converts a proof of the latter into `GeneratedRouteCoherence`.

`flag-sweep` also constructs an actual cube of paths from vertex 0 to vertex 4
from any Cubical four-cell, by composing its three moving initial segments.
Its five tetrahedral boundary formulas and collapsed-234 formula are checked
pointwise by reflexivity. `flag-initial` identifies the initial corner with
three left units on `e04`; `flag-terminal` identifies the final corner with
`p ∙ (q ∙ (r ∙ s))`.

The remaining step is **not** existence of this cube: it is the higher boundary
normalization identifying its five face sweeps (and collapsed sixth face) with
the marked pentagon's corrected long and short routes. No term of that
normalized pentagon relation, or of the general `Goal`, is claimed yet.

## Verification

All four modules below passed fresh `--safe --cubical --guardedness` checks via
`check_cubical_agda.ps1 -Module <Module> -Fresh`. The bridge closure check also
rechecked the existing tetrahedron and induced four-cell bridge dependencies.
The receipts report stable inputs, ignored interfaces and independently matched
source hashes:

- `PathSweepCoherence`: finished 2026-10-05T12:52:18Z,
  SHA-256 `11b6cac8a98eb62ca791ae11de859d05268c9446434338b6cc4f97138f0f63f8`.
- `TetrahedronPresentationBridge`: finished 2026-10-05T12:56:30Z,
  SHA-256 `140984c2dcd6fa9f70855b2bf8b8bd485dfa81ba25e95848ef3b034bea14817c`.
- `MarkedFourSimplexCoherence`: finished 2026-10-05T12:56:52Z,
  SHA-256 `6a973e6e3b2ea7504120a9b2dd89391b669a40cb760bc080347dcf2114658e6e`.
- `FourSimplexPentagonBridge`: finished 2026-10-05T13:02:25Z,
  SHA-256 `94b0f4abb8dc6315f881f7347bfea45ac6f316fd7b1697da69baa69008f84d18`.

Only the pre-existing `TypedGeneratorLayers` import warning remains.
`check_four_simplex_pentagon_bridge.py` passes, including rejection controls for
incremental and wrong-module receipts. Its classification is
`independent_pentagon_checked_comparison_coherence_open`.
The nonconstant `TypedFixture` checks independent pentagon completion, the
induced-versus-translated-Cubical center normalization, the chosen tetrahedron's
sweep computation, and the explicit four-cell's sweep cube and terminal corner.
It does not assert equality of the independent pentagon and induced centers.
The tetrahedron receipt audit also passes against this updated inventory.

The older per-module receipts recorded in the preceding notes are historical;
adding these source files changes the owner inventory used by their auditors.
The new fresh bridge receipt verifies the current dependency closure.
No SCC execution, graph admission, commit or ledger publication is claimed.
