# Deeper search for the typed dual-reference readout interface

Target: `dual-reference-native-readout-binding` in Ramsey net revision28. This is a source search under that open node, not a new operation or a verdict change.

## 1. Strongest constructive lead: transported full-field bindings and readouts

Sources:

- `research/strominger/full-five-channel-candidate-v1.md`
- `research/strominger/joint-field-assembly-sewing-v1.md`
- `research/strominger/screw-field-sewing-result-v1.md`
- `research/strominger/checkers/check_joint_field_assembly_sewing.py`
- `research/strominger/checkers/check_screw_field_sewing.py`

These already construct more than a coefficient permutation. They retain a44-coordinate joint field (36 baryon coordinates plus8 electron coordinates), five-column coefficient embeddings, and their metric-adjoint readouts. For a packet h with actual coefficient permutation Pi_h and field frame U_h:

    B_h = U_h B0 Pi_h^-1
    R_h = B_h^sharp

Every tested native interface e:s->t satisfies

    U_e B_s = B_t Pi_e
    R_t U_e = Pi_e R_s
    R_h B_h = I5.

The readout square is checked on the entire44-dimensional field, not only a preferred input. The prior joint fixture has14 packet presentations and18 interfaces; the screw fixture has66 packets and95 interfaces. Bindings cannot be frozen by geometric chart alone: distinct retained coefficient histories can have the same field frame but different B_h.

At E, the prepared five-dimensional input splits into rank2 in E and rank3 in the retained baryon block. Thus there is an existing recovery interface preserving all five coefficients through E without pretending that its rank-two return or an active window contains the entire state.

### Why this matters for the new target

This is the concrete existing machinery to inspect before inventing a new five-to-six amplitude extension. A moving-basis candidate should transport **both** its embedding and its readout, then test the named-occurrence interface separately. Checking Q alone never did that.

There is a straightforward conditional calculation: given an already justified field map U between two presentations, rebasing coefficients by Q suggests

    B_dual = U B_old Q^-1,
    R_dual = Q R_old U^-1.

The recovery/readout equations follow algebraically. This is a search guide, NOT a newly source-admitted adapter: it still requires the actual U and an interpretation of the outgoing labels. The prior implementation derives bindings from chosen field frames; it does not import the T-seam outgoing reference or independently derive a coupling to new C0/old M2.

The documents explicitly distinguish contextual connection gluing from equality of raw geometric face fields. The36/8 field coordinates, five native reference slots and geometric vertex labels are different types. Neither full-field recovery nor its rank accounting silently identifies them.

## 2. A reversed-boundary validator already exists, at an experimental scope

Sources:

- `research/strominger/dual-isotope-rules-v1.md`
- `research/strominger/checkers/probe_dual_isotope_rules.mjs`

This is an actual two-direction certificate implementation, not merely a suggestion for one. It fixes coordinates, reverses edges and coefficient maps, changes M/C and P/E roles, reflects occurrence indices and exchanges complete entry/exit boundaries. Its negative-direction validator requires that reversal recover the exact independently audited forward certificate.

It also changes direction-dependent admission conditions explicitly:

- reverse E, not reverse P, must be regular;
- reverse P may be regular or split;
- reverse NN faces use the transported two-M condition;
- all old exits become entries, not one independently selected root.

The saved audit covers native N-15 and O-16 plus two experimental N-14 variants. It retains inverse edge maps and full boundary data and rejects corrupt maps, roles and collapsed boundaries.

**Correction to the search emphasis:** there is no need to invent a generic reversed-boundary validator. An isolated pullback validator already exists. However, it uses the prior inverse-map convention, not the T-seam moving-basis/readout binding, and it is not registered as a new outgoing rule in the native forward generator. The N-14 cases additionally inherit the experimental PE permission. Its full-boundary source type must not be collapsed to a single native packet.

This also explains why the16 split-E cases are not a universal reversal impossibility: the experimental negative-direction P type permits them. They still fail the unchanged forward P constructor.

## 3. Actual same-body reader comparison supplies a diagnostic precedent

Sources:

- `research/strominger/native-reader-comparison-v1.md`
- `research/strominger/checkers/check_native_reader_comparison.mjs`

The actual NE and NN alternatives on one primitive have a full-five comparison derived from their real source maps:

    Q_EN = [0,3,1,4,2].

It preserves all coefficients and has an inverse. But an active-E-invisible input becomes visible to the N reader; the complement must be retained. Three complete occurrences match, while the fourth changes C1 to C3 on the same vertex, and the outside reference changes vertex and index. The source's phase witness refuses this cross-species rereading, and its composition reader distinguishes the two assemblies.

This is a directly relevant test design: compare the entire retained carrier, the named active reader, outside context and admission witness separately. A full inverse is not an occurrence witness. This Q_EN is not the T-seam Q and must not be substituted for it by numerical analogy.

## 4. Reconstruction-aware reference changes are implemented on another carrier

Sources:

- `research/strominger/field-reference-transitions-v1.md`
- `research/strominger/direct-compact-transitions-v1.md`
- `research/strominger/checkers/field_reference_transitions.py`

The actual `change_reference` implementation validates a complete packet, reconstructs or retains its operator core, regenerates the target readouts AND leaf endpoint labels, recomputes target obligations, and preserves route history. Composition checks complete intermediate packet equality, including required fallback information. The direct compact implementation also retains completion columns or refuses an out-of-domain change.

This is a useful existing architecture for the desired typed bridge. It shows how changing a reference requires a target decoder and explicit missing-information retention, not just replacing a name or reusing old slot indices.

But its carrier is the twelve-arrow field/comparison representation, not the five-slot PNE reference. No binding from those reference choices to C0/M2 was found in the inspected implementation. Its reconstruction modulo common phase is not automatically the phase-bearing native coefficient transport.

## Evidence status

Read the above reports and the relevant implementation sections. The scientific suites were not rerun in this search. A fresh direct-pin check of saved receipts found:

- joint-field assembly sewing:10 recorded direct input hashes, all match;
- screw-field sewing:14 recorded direct input hashes, all match;
- dual-isotope rules:6 recorded direct input hashes, all match.

This is direct-source freshness, not transitive proof closure or a fresh scientific replay. The field-reference-transition receipt has no pins under the two hash field names used by that quick check; no freshness claim is made for it.

## Recommended concrete next investigation

The new target is the **intersection of two existing implementations**, not an invented generic duality:

1. Use the full-five/44-channel construction's B_h and R_h interfaces as the candidate retained readout carrier.
2. Type the T-seam's outgoing basis explicitly and compare its transported readout with the actual native incoming-basis reader; retain the new-C0/old-M2 and old-C0/new-M2 provenance.
3. Test that package against the existing negative-direction certificate type, preserving all entries, direction-specific shape/NN rules, and exact recovery of the forward witness.
4. Keep success in that experimental pullback model distinct from admission in the unchanged forward generator and from the parent's P/PN face-specific port target.

The missing evidence is their actual labelled-reference binding and policy compatibility. Existing readout squares and an existing reverse validator make this a specific construction target; they do not establish it by composition of citations.

Net revision28 and its open outcomes are unchanged. No owner source or receipt was rewritten.
