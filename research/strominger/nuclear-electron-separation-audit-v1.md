# Nuclear structure versus electron-exit coverage: source audit

## Decision

Separate **necessary nuclear-local compatibility** from **complete assembly
admission**, but do not manufacture a nuclear binding or stability criterion.
The source examined here does not provide a justified replacement nuclear
boundary/closure law. Existing production rules and viewer admissions remain
unchanged.

## Provenance of the three requirements

| Requirement | Grounding found | What does not follow |
|---|---|---|
| Electron occupies a tetrahedral carrier | `electron-M2-carrier-trial-v1.md` explicitly records the operator-specified trial `E = M1 C1 C2 [M2]`. `carrier.mjs#trial` retains it; `window-construction-model.mjs` binds the ordered face and new context vertex to a lattice primitive. | This is a retained geometric trial, not a derivation of physical electron localization. It is not an accidental implementation detail that can simply be deleted. Split-only occupancy is a further isotope-search restriction. |
| E/E full-face contacts forbidden | The isotope enumerator explicitly excludes adjacent electrons. `compilePhaseAssembly` rejects equal-species non-neutron face contacts. | A terminal reader has no forward continuation; that does **not** imply that two terminal carriers cannot touch geometrically. No E/E transport or compatibility law was supplied by the inspected window protocol. Lack of such a law also does not establish that contact is harmless. |
| Every entered nuclear state must reach E | The retained P→N→E traversal exits at E into the next realization. The whole-assembly compiler then requires an E route from every chart and builds a finite entry/exit certificate. | A completion rule for that traversal is not independently a physical existence, binding or stability criterion for a bare nucleus. |

Relevant historical scope qualifications are explicit: `cmc-mcm-carrier-binding-v2.md`
calls P/N binding a corrected proposed assignment, not native physical equivalence;
`electron-M2-carrier-trial-v1.md` calls the E geometry a trial and distinguishes
M2 geometric provenance from the five retained spectral coefficients;
`window-transfer-prior-research-recovery.md` preserves the declared frame adapter
without promoting it to physical dynamics.

Thus my earlier suggestion that the coupling is too tight needs qualification:
**the coupling is real in the implementation, but some of its geometry was an
explicit trial input. The unsupported step is treating the resulting combined
certificate as a universal physical nucleus test.**

## Executable separation, without changing admission

`check_nuclear_electron_separation.mjs` creates an isolated diagnostic from the
exact existing compiler prefix. It stops immediately before exit-path selection.
It retains:

- explicit MMCC roles, root boundary and complete physical interface ledger;
- native PN packets, inverse PN transport and local reader-phase comparisons;
- the existing NN witness tests and zero-advance phase audits;
- a reader for every occupied nuclear cell and directed reachability from root.

Its only successful status is `nuclear-local-compatible`, with **`admitted:false`**
and **`boundaryStatus:'not-assessed'`**. It refuses occupied electrons. It neither
renames neutrons as exits nor inserts closure edges or new transport laws.
The ordinary compiler is not modified.

This is a necessary local-prefix test, not a complete ordered entry/exit
certificate. It inherits the model's native-P-reader and reference-transport
assumptions. Native packets still compute E-lookahead context, including the
lookahead used by existing NN tests; no claim of removing all electron-protocol
dependence is made. What is separated is occupied electrons and exit coverage,
not the historical provenance of the reference rules.

## Checks and countercontrols

- Strip occupied electrons from ten existing reference isotopes (He-3 through
  N-15 in the available reference list), preserving their nuclear roles and
  PN/NN reader assignments. All ten pass the necessary prefix diagnostic.
- Recompile and audit the recorded N-14+ six-electron witness, then strip its
  electrons. Its nucleus also passes the prefix diagnostic.
- All eleven bare controls fail the unchanged complete compiler with
  `phase-directed-dead-end`. This isolates the additional E-exit obligation.
- Corrupted interface ledgers and MMCC roles remain rejected. Occupied-electron
  inputs are refused by the diagnostic.
- An **isolated proton** fails this occupied-PN-chart diagnostic with
  `missing-carrier-reader`. This important countercontrol prevents presenting
  it as a universal nuclear admissibility test.
- An abstract branching graph can have two terminal exits on geometrically
  touching cells. `auditStateCoverage` accepts its terminal coverage, while
  rejecting any outgoing edge added to an exit. This is only a countermodel
  to the logical inference “terminal implies nonadjacent”; its arrows are
  explicitly **not** claimed to be native physical transport or an admitted E/E
  assembly.
- With no exit boundary specified, the generic coverage auditor reports
  `pending-boundary`, not proven physical failure. Its exit obligation is
  supplied by its caller.

The original retained-window checker was rerun and passed all its seed-marking,
mode, attachment, history and terminal checks. No window law was relaxed.

## Search consequence

The present enumeration also couples electron quotas to nuclear pruning:
`NN <= floor((2*N - E)/2)`. This is a necessary port budget for the declared
combined packing, **not an electron-independent nuclear restriction**.
Changing the requested electron count can therefore change which nuclear
prefixes are even enumerated. Earlier N-13/O-14 negatives must retain those
charge-state qualifications.

For future nuclear-only enumeration, the electron-quota pruning cannot be used
as a nuclear existence test. Even removing that pruning supplies only candidate
geometry, not the missing nuclear boundary, interaction or binding law.

## Remaining gate

Before replacing the assembly criterion, specify a source-supported nuclear
boundary/continuation object and what physical claim it can support. Separately,
E/E contact needs an occurrence/coefficient compatibility rule or a justified
exclusion—not merely terminality. No such new rule was derived in this audit.
Electron attachment should then be assessed as a distinct extension problem.

No new isotope search or viewer admission was performed. No isotope-specific
exception, fictitious E exit, binding energy or decay prediction was added.

## Reproduce

```sh
node research/strominger/checkers/check_nuclear_electron_separation.mjs
node research/strominger/checkers/check_window_construction.mjs
```

Evidence: `results/nuclear-electron-separation/verification.json`, with source
fingerprints, the exact compiler-prefix fingerprint, eleven controls and the
standalone-proton and terminality countercontrols.
