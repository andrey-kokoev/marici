# The witness's own marked endpoints cannot generate a mismatch

## Question

Can the prepared source probe and target reference in the witness-driven controller be supplied simply by the inhabited vertices of the existing typed tetrahedral package?

They can supply a typed comparison, but it always agrees. This distinguishes a witness's certified target from an independently prepared reference against which it may be measured.

## General checked theorem

The existing `RetainedTetrahedralPackage.TypedValue` is a dependent pair (T,t) of a type and an inhabitant. Given a path p from (S,s) to (T,t), its second component already supplies

    transport(fst along p, s) = t.

`agda/MarkedWitnessControlAudit.agda` proves this using `fromPathP` on the retained dependent inhabitant path. It then applies the theorem to the actual first edge of every filled typed-value tetrahedron.

Thus using the source inhabitant as probe and that edge's own target inhabitant as reference cannot create a discrepancy. This is a general endpoint-compatibility statement, not a sampled calculation or a choice to normalize the response to zero.

## Existing concrete fixture

The actual `TypedFixture.result` has false at the first marked vertex, true at the second, and the witnessed Boolean flip between them. The compiler checks:

    flip(false)=true,
    disagrees(flip(false),true)=false.

The preceding witness-driven test instead supplied false as the target comparison reference. That question genuinely disagrees with the flip output, but its false reference is NOT the pointed target certified by the flip witness. The module proves that treating it as such would imply true=false.

The earlier ordinary/twisted packages were type-valued vertices, not a preparation of false at every inhabited vertex. Adding those probe values was an explicit additional preparation. This distinction cannot be removed by reusing the same vertex names.

## Consequence

The witness-driven controller remains a valid conditional experiment with an independent prepared reference. It has not eliminated the reference-preparation input merely by calling its question source-derived.

For a nonzero comparison, one must retain a reference or record whose value is not already constrained to be the certified output of that very witness. The source must provide the independent record and the operation relating it to the comparison. Alternatively an operation can inspect higher witness data, but it must not be represented as a mismatch between endpoints that the witness itself proves compatible.

This result does not forbid independent measurements, interactions, or active edits of retained witnesses. It identifies which attempted preparation shortcut fails. No new update law, forced coupling or gravitational coefficient has been supplied.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module MarkedWitnessControlAudit -Fresh

Passed first run with safe Cubical/guardedness flags, ignored interfaces and stable inputs. Receipt: `results/agda-MarkedWitnessControlAudit.json`. Finished 2026-10-05T23:33:55.4915049Z; source SHA-256 `5c56219413bd0508524841a1e6ace5930d146597def525bfe5248e94a6abb0d7`.

No postulates or unresolved holes were introduced. No ledger entry, commit or publication is claimed.
