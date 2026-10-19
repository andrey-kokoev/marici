# Boundary data and E/E contact: what can actually be derived

**Update:** the [all-contact repair](assembly-contact-coverage-repair-v1.md)
now enforces the missing gate and reselects affected references. The gap and
proton IDs described below are historical; the refreshed diagnostic receipt
checks current references and reports all their contacts witnessed.

## Outcome

Native outgoing boundary **readouts** can be constructed without occupying
additional electron cells. A physical nuclear boundary condition or binding law
still cannot be inferred from them. Literal shared-occurrence E/E sewing can
be classified, but does not supply a complete E/E transport law.

A separate implementation gap was also found: carrier coverage does not imply
that every declared physical contact has a transport witness. This qualifies
some earlier reference passes and needs repair before stronger admission claims.

## Native nuclear-boundary traces

Starting with the unchanged nuclear-local compiler prefix, recover each native
PN packet whose NE target lies outside the occupied nucleus. Replay the source
window constructor and its NE event. This gives an ordered boundary face,
actual occurrence origin and the existing five-slot map `[0,4,2,3,1]`.

The new diagnostic checks rooted path histories and phase advances, native NE
same-occurrence compatibility at the reached origin, full five-slot inverse
recovery, and the terminal window's three spectral components. It records the
geometric M2 provenance but does not assign M2 a new spectral coefficient.

| Retained reference's nucleus | Nuclear cells | Native outgoing ports |
|---|---:|---:|
| C-12 | 12 | 8 |
| N-14+ (first recorded witness) | 14 | 6 |
| N-15 | 15 | 8 |

Every nuclear chart in these three cases has a route to an outgoing trace.
These ports are **not occupied electrons**; their number is not a charge or
neutrality prediction. Their hypothetical cell placements are not jointly
admitted, and no nonoverlap, E/E compatibility or new electron assembly is
claimed. Nor is there a new complete history-bearing nuclear certificate.
This constructs boundary interface data, not a physical boundary condition.

## Literal same-occurrence E/E sewing

For an MMCC E carrier `M1 C1 C2 [M2]`, a shared face has either MCC or MMC
roles. Enumerate the four local role-preserving E frames on each side: sixteen
pairs per face pattern.

In each pattern, exactly four pairs allow all shared occurrence indices to
agree under a single relative origin. That offset must be zero: the shared
same-channel pair has consecutive indices 1 and 2, which admits no nonzero
common translation or reversal preserving the pair.

This already shows that phase labels alone do not forbid every E/E contact.
But the matching cases expose two different obstructions:

1. **Both shared faces are the active incoming E window** (two MCC cases).
   Native NE construction requires a neutron immediately across that face.
   In this manifold, each E would therefore require the other occupied E cell
   to serve as N. That conflicts with distinct particle occupancy under the
   existing NE construction. This is a specific contact configuration, not a
   proof that every touching E pair is impossible.
2. **The shared face includes M2 context on both sides** (the other two MCC
   cases and all four MMC cases). M2 has geometric provenance but no sixth
   native spectral coefficient in the retained source. Equal phase labels do
   not supply the missing full-face field data or its transport rule.

These are local E-template comparisons, not an exhaustive classification of
jointly constructed multi-particle packets. All EE transitions still fail the
unchanged transition-witness gate; E reader phase advance is not supplied.
Other occurrence identifications would require their own source witness.

Even a fully specified active face cannot determine a five-slot extension:
identity and a sign flip on the outside C0 coefficient preserve all active E
readouts and the full norm, yet disagree outside the face. These are two
mathematical completions of face data, **not two source-authorized native EE
operators**. Selecting either as an interaction would add an assumption.

## Newly exposed contact-coverage gap

The existing compiler validates the physical contact ledger and builds native
packet edges, then checks that every carrier is represented and can reach an
E exit. It does not additionally require every declared NE contact to appear
among those packet edges.

A report-only all-contact audit gives:

- He-3, He-4, Li-6, Li-7, Be-9 and C-12: all declared contacts witnessed.
- Selected B-10, B-11, C-13 and N-15: the declared **N13–E14** contact lacks a
  native NE edge (13 and 14 here are cell IDs, not isotope labels).
- N-14+ obtained by adding proton **18**: the same missing contact.
- N-14+ obtained by adding proton **24**: all declared contacts witnessed.

Thus the first recorded N-14+ witness and selected N-15 are legacy-checker
passes, not established all-contact-compatible assemblies. The alternative
N-14+ witness survives this stronger audit, so the existence of a six-electron
N-14 reference is not lost at this step. No stability claim follows.

No production fix or viewer reselection has been made here. A subsequent repair
must make contact coverage explicit in compiler/auditor, re-enumerate affected
references under that declared gate and rerun regressions. It must not silently
invent NE edges or certify the current displays as all-contact checked.

## Verification

```sh
node research/strominger/checkers/check_boundary_contact_derivation.mjs
```

Receipt: `results/boundary-contact-derivation/verification.json`. It records
source hashes, open-port data, both exhaustive local E-face classifications,
all-contact audits for ten selected references and both N-14+ alternatives,
and the transport-underdetermination control.

No production/viewer files or physical admission laws were changed.
