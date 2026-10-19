# Reference changes with compositional retention obligations

## Question and result

A packet reconstructible for one excluded arrow need not be reconstructible from scalar data for another. Reference change is therefore not just renaming the mark or permuting the 121 arrow comparison entries.

This construction gives a verified transition between complete reconstruction-aware packets. It uses only the packet and its admitted context—not the original field, an amplitude anchor or a physical reference d.

The scalar-only interface is partial. On the validated domain, the interface with its required operator fallback admits every directed reference change. Identity, inverse and composition laws hold for the resulting packets, and reference changes commute with the retained numerical transport.

## Prior results used

- [Conditional scalar reconstruction](field-reconstruction-v1.md): the P/Q/C channels recover the entire field modulo common phase under explicit selected-span and reference-probe conditions.
- [Reconstruction-aware retained transport](reconstruction-aware-tower-v1.md): certificates and explicit fallback records accompany the 137 leaves through both retained-promotion policies.
- [Earlier complete operator preparation](field-comparison-preparation-v1.md): full outer-product data retain the field modulo common phase, with zero treated separately.

The new ingredient is a reference-independent intermediate and a checked law for when the destination packet must retain it.

## The complete unanchored operator core

In the declared corner coordinates define

```
Omega[e,f] = c_e c_f*,        e,f among all twelve directed arrows.
```

This is 144 matrix-valued blocks, independent of which arrow is excluded from the scalar branch. The common phase cancels.

For a valid source packet:

- if an operator sidecar is present, validate it and use its blocks;
- otherwise use the exact scalar decoder's representative y and positive rho, and construct `Omega = outer(y)/rho`.

The latter operation derives information already determined by the packet; it does not consult the original field or invent missing amplitudes. A source outside the scalar reconstruction domain without its required sidecar is rejected.

## Transition algorithm

For a new reference s:

1. Validate the complete source packet and its context.
2. Obtain its complete unanchored operator core Omega by the admitted route above.
3. Extract an exact representative y and positive rho from Omega.
4. Compute the P/Q/C comparisons with s excluded and divide their quadratic values by rho.
5. Regenerate all leaf parent endpoints and labels for s.
6. Recompute the reconstruction certificate and reference-equation margin bounds for s.
7. Retain Omega as the target sidecar whenever the existing policy requires it: weak, unresolved or outside the scalar reconstruction domain.
8. Rebuild the actual numerical family trees at the same rung, policy and source/target presentation, then validate the whole target packet.

No square root or common-phase choice is needed. The numerical route history is unchanged; reference-transition histories are separate typed records.

A missing-reference phase cannot be manufactured from a deficient scalar packet. The transition can preserve it only because it was either determined in the source chart or explicitly retained in the source sidecar.

## Why composition works

Let N_r(Omega) be the deterministic packet for reference r, fixed context, numerical rung, route history and retention policy. Its scalar values and certificate are determined by Omega. Its sidecar is either exactly Omega or absent under a certificate that allows Omega to be reconstructed.

Consequently extracting the operator core from N_r(Omega) always returns Omega. Therefore

```
T_(s->t)(T_(r->s)(N_r(Omega))) = N_t(Omega)
                               = T_(r->t)(N_r(Omega)).
```

The same argument gives identity and round-trip laws. These are equality statements about full resulting packets, not just their averages or their observable equivalence classes.

Composition validates every intermediate packet and requires complete endpoint equality, including sidecars and provenance. Direct and composite construction histories remain different records even when their final packets agree. The theorem is scoped to the fixed validated context and retention policy; it does not identify incompatible frames, policies or historical routes by assumption.

The complete operator core is a sufficient intermediate, not a proof of minimum storage. No minimum reference-transition record set is claimed.

## A reference-dependent failure found explicitly

Use the earlier blind-reference fixture, whose arrows (2,1) and (3,1) vanish while the other selected triples still span C3.

With excluded reference (0,2), the scalar decoder succeeds and the reference-equation margin passes the frozen threshold. No operator sidecar is retained.

Changing the excluded reference to (0,1) produces a deficient scalar packet. The two incoming probes needed to recover that excluded triple are now zero. The transition derives and retains all 144 operator blocks from the original good packet **before** dropping the corresponding scalar observation coverage.

Changing onward to (2,3) produces a good packet again; its scalar data determine the complete core and the policy no longer requires the sidecar. The exact retention pattern is:

```
(0,2): 0 fallback blocks
   -> (0,1): 144 fallback blocks
   -> (2,3): 0 fallback blocks.
```

The composite final packet equals the direct (0,2)->(2,3) result. A round trip through the deficient reference restores the original complete source packet exactly.

The checker also audits all twelve possible reference marks for this fixed field, rather than assuming that the chosen reference chart is privileged: nine pass the current scalar decoder and three trigger its fallback rule. A failed gate is not a general proof that scalar reconstruction is impossible by every method. For example, a zero excluded triple may be recoverable from its norm even when the linear probes do not span. The demonstrated nontrivial ambiguity is at (0,1); fallback elsewhere remains a sufficient, possibly conservative contract.

## Why equal scalar packets cannot be glued blindly

The earlier blind-reference pair differs only in the phase of arrow (0,1). At that deficient reference their entire 411-value scalar packets coincide, but their operator cores differ. At the good reference they are distinguishable.

An attempted composition that joins the first field's transition to the second field's transition on the basis of scalar equality is rejected: their complete intermediate packets differ in the retained operator sidecar. This is the concrete information obligation enforced by composition.

Removing a required sidecar, reusing the old certificate after changing the reference, inventing a successful target obligation, falsifying the reconstruction route, changing the context, or changing only the reference mark without rebuilding leaves is likewise rejected.

## Compatibility with retained transport

For both `inherited` and `common` policies, reference change commutes with:

- vertical source indexing;
- horizontal two-stage retained promotion;
- the complete numerical route to rung 4.

The reason is stronger than equality of terminal means: retained promotion keeps all leaves and their masses. It neither changes Omega nor its reconstruction obligations. Rebuilding the target reference and then promoting gives the same full trees and sidecars as promoting first and changing reference afterward.

The numerical diagram's positions are still not identified with native field grades. Nor does this establish compatibility with every possible information-changing map: channel deletion, probe deletion and terminal aggregation remain separate transition types requiring their own targets and retention laws.

## Boundaries

- No absolute phase is transported. Identity and round-trip laws on Omega do not establish a phase connection or a holonomy theorem.
- Reference mark changes do not select or change the numerical direct reference d.
- Exact transition laws do not imply uniform conditioning near the probe-rank boundary.
- Mathematical regeneration of comparisons is not a physical measurement implementation.
- The full operator fallback is sufficient but not proved minimal.
- No new binding to the original fixed 2x2 DG multiplication is claimed.

## Reproduction

```
python research/strominger/checkers/check_field_reference_transitions.py
```

Receipt: `research/strominger/results/field-reference-transitions/verification.json`. The checker replays the retained-transport and reconstruction prerequisites, checks the twelve-reference census, identity/round-trip/composition laws, six retained-transport naturality squares, a zero-stratum round trip and eight negative controls. No production or viewer code changes.
