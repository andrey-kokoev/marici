# Temporal authority and descent — cycle 6

## Frozen basis

Nima’s directed task and Strominger’s
`authority-grant-composition-interpretation.md`, with its admitted and hostile
JSON fixtures.

## Increment

`TemporalAuthority.lean` defines a typed partial composition calculus. Grants
carry endpoints, authority kind, evidence domain, variance, and a half-open
validity interval. Composition exists only with endpoint/kind/domain/variance
matches, a nonempty interval intersection, and an explicit zero-defect
coherence witness. Defined composites are associative, satisfy left and right
identity laws on the same index interval, and preserve kind.

Cached evidence has an occurrence time but no authority field. Evidence
persists monotonically; authority expires or is revoked. Replay of the same
packet requires a live grant. The hostile fixture proves the requested theorem
that cached evidence cannot imply live authority.

Local flatness, effective unique descent, and holonomy are separate types and
predicates. Executable fixtures prove that flat overlap cells need not produce
global reconstruction or uniqueness, and distinguish zero from nonzero replay
holonomy.

`DescentEquivalence` strengthens the executable audit with proof-relevant
two-sided restriction/reconstruction laws. A flat `Unit` local fiber over an
empty global fiber is the hostile no-descent model. `RevocationEvent` requires
the revocation time to follow the evidenced authorized act, preserves that act
as history, and `Restoration` requires an unchanged packet plus a live
successor root; cached evidence alone cannot restore standing at revocation.

The minimal indexing object is `(time, authority kind, evidence domain)`.
`IndexedRecord` places a cached record and a live grant in one such fiber. The
theorem `descent_time_kind_pairwise_independent` supplies all three required
countermodels: each of effective descent, temporal validity, and kind
preservation can fail while the other two hold.

Reviewer panels, frozen packets, rival-admission jurisdiction, and appeal
dispositions appear only as concrete fixture values; they are not promoted to
the generic grant ontology.

## Disposition

**Generalized with temporal specialization.** Partial composition, kind
preservation, interval intersection, replay liveness, and descent distinctions
are common. Institutional governance remains fixture-level.

## Missing interfaces

1. Evidence-domain transports beyond exact equality.
2. Proof-relevant invertible coherence cells and their naturality laws.
3. A quotient/stabilizer object for stacky unique descent.
4. Content-address equality connected to the repository hash type.
5. A typed authority-root/charter provenance graph for concrete governance
   replay, without granting it mechanism-truth authority.
6. A law relating interval time to the graph event clock and preventing
   backdated revocation.

## Build

From `research/buzzard/marici_formal`, run `lake build`.

Result: `Build completed successfully (8716 jobs).` Lean/mathlib version:
`v4.33.1`.
