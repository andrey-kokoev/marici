# An explicit experimental reference-mediated P/E constructor

## Disposition

The proposed grade-zero terminal P/E rule is now a separately callable constructor with a context-bound witness and a whole-assembly replay interface. It is **not added to the native generator** and is not presented as derived from the existing occupancy laws.

This implements the missing operational premise identified in [the occupancy-semantics audit](reference-occupancy-semantics-v1.md): a selected endpoint transfer may use an unselected intermediate reader as a fully retained reference. The prior [support proof](neutron-support-nonderivability-v1.md) is unchanged. The new constructor is an explicit extension, not a proof of its physical availability.

## Opt-in and type boundary

The research-only module is `checkers/experimental_reference_pe.mjs`. Callers must supply the exact policy identifier:

```
experimental-reference-mediated-PE-v1
```

Each result records `admission: experimental-only` and `native: false`. Native operations are not modified, and the native `validateTransfer` still rejects this constructor. Production and viewer code do not import the module.

This turns the prior [terminal P/E probe](terminal-pe-probe-v1.md) into an independently revalidated API, rather than introducing a different isotope-specific rule.

## Constructor guards

The caller supplies a selected reader configuration and the IDs of actual source-owned PN and NE factors. The constructor requires:

1. Source-owned, consecutive PN and NE operations, each passing the unchanged native transfer validator.
2. Selected P and E endpoint readers and three distinct P/N/E body sites.
3. The intermediate N **body** is unoccupied. Selecting another reader on that body still violates vacancy.
4. Both factors have grade zero and all three origins agree.
5. The selected P reader has no outgoing selected native operation. This is reader terminality, not whole-body terminality.
6. The E reader has no native outgoing operation.
7. The endpoints share exactly the marked C1/M1 edge.
8. Full five-coordinate composition reproduces the selected E packet response.
9. The whole selected configuration passes the unchanged geometry, global C/M-role, species and contact-compatibility guards.

The result keeps the native factors and their ordered word, all three packet/chart frames, the reference-neutron identity, complete coefficient map, grade and marked edge. Required occupied support is {P,E}; reference support remains {P,N,E}. The saved frames retain external aliases as well, so the support-site lists are not misrepresented as an exhaustive coordinate dictionary.

## Context-dependent witnesses

The witness records the canonical selected packet set in which its vacancy and boundary conditions were checked. Validation reconstructs the witness from the current source rules and supplied selected context and compares every field.

A witness is therefore not an unconditional new arrow. Changing the selected configuration, reference marks, coefficients, admission tag or factor identity requires revalidation. In particular, adding an onward reader to the source P can invalidate its terminality without changing the occupied P body.

No source or target coefficients are fitted to the isotope. The constructor uses the same native factor permutations for every trial.

## Whole-assembly replay

The assembly audit separately checks:

- explicit target species counts;
- the original selected-configuration guards;
- root reachability using native operations plus the explicit experimental constructors;
- reachability of an electron exit from every selected record;
- a rooted construction sequence and all its geometric/role-compatible prefixes;
- a freshly constructed prefix-context witness for every experimental step;
- native witnesses for every occupied triangular contact.

The last check is important: an edge-based PE constructor cannot be counted as a substitute for an unwitnessed occupied face contact. Its support extension does not weaken the original contact ledger.

The sink-only invariant is also enforced: adding arrows into terminal E readers cannot make an unrooted nuclear reader reachable. Failures of nuclear construction are not hidden by adding electron exits.

`nativePass` and `experimentalPass` are recorded separately. Passing this audit does not relabel a native failure as a native success.

## Replayed finite results

The same constructor is tested on all 24 hydrogen markings and all 20 saved single-neutron deletions:

| Family | Result |
|---|---|
| H-1 markings | 24 experimental passes; native selected P/E paths still fail |
| H-2 controls | Native paths pass; no experimental constructor is added |
| N-14 from N-15 | Two experimental passes: deleted cells 16 and 17 |
| Ne-21 from Ne-22 | Two experimental passes: deleted cells 16 and 29 |

The four positive isotope configurations use six constructor instances in total. Their occupied geometry and particle counts are unchanged. All other saved deletion outcomes agree with the earlier probe.

The checker freshly regenerates the bounded native universes and compares their saved packets, charts and operations. It also freshly runs the separate Python witness checker and compares every isotope trial's outcome and shortcut count. The independent checker shares the rule specification, not this new JS constructor implementation.

No new layout, isotope search, binding energy, spin or physical stability result is claimed.

## Negative controls

Controls reject missing policy opt-in, an occupied reference N, occupancy through a different N reader on the same body, a nonterminal source P reader, corrupted coefficients/reference frames/context/admission tags, submission of the constructor to the native validator, and incorrect isotope counts.

The source-rule file hash is unchanged before and after replay, and the native operation list contains no experimental PE operation.

## What has and has not been achieved

We now have an executable, explicitly typed grammar extension with auditable local evidence and whole-configuration certificates. The existing four positive candidates can be reconstructed through it without weakening their original geometry, phase, contact or reachability checks.

We still lack an independently justified physical/source principle selecting this extension. Its finite success does not supply that derivation. Production admission and the viewer remain unchanged until that gate is addressed or an operator deliberately adopts the separate experimental grammar for further research.

## Reproduction

```
node research/strominger/checkers/check_experimental_reference_pe.mjs
```

Receipt: `research/strominger/results/experimental-reference-pe-constructor/verification.json`, including complete local constructor witnesses, construction prefixes, rejected-candidate reasons, separate native/experimental outcomes, independent-check evidence and source hashes.
