# Terminal P/E shortcut: comparative experiment

## Result

An explicitly hypothetical reference-mediated P->E shortcut repairs selected
H-1, N-14 and Ne-21 configurations without changing their retained occupied
body geometry or counts. This result uses a new edge rule in an isolated
checker, not the unchanged native generator. Production and viewer admission
remain unchanged.

| Target family | Trials | Electron terminal | Electron + proton reader terminal | Electron + whole proton body terminal |
|---|---:|---:|---:|---:|
| H-1, all seed markings | 24 | 24 pass | 24 pass | 24 pass |
| N-14 from N-15 single-N deletions | 8 | 2 pass | 2 pass | 0 pass |
| Ne-21 from Ne-22 single-N deletions | 12 | 2 pass | 2 pass | 0 pass |

All 24 H-2 controls retain their original native paths and receive no shortcut.

## Exact candidate rule

For a selected proton packet P and selected electron packet E:

1. Require an actual source-generated PN operation P->N and NE operation N->E.
2. Validate both operations using unchanged `validateTransfer`.
3. Require the intermediate N **body** to be unoccupied (not merely that a
   particular N packet is absent).
4. Require P and E to share exactly the C1/M1 edge and have equal origins.
5. Compose the full five-coordinate maps; require the result to reproduce the
   selected E packet permutation exactly.
6. Require E to have no native outgoing operation.
7. Depending on the tested variant, impose a proton terminality condition.

The candidate edge is directed P->E. E remains a sink. Original global C/M,
species and occupied-face contact guards are not weakened. Edge contact does
not excuse any actual occupied face from having a native witness.

### Three definitions compared

- **Electron terminal:** no outgoing native operation from E. Every generated
  electron already satisfies this, so terminality alone is not a selective
  criterion among electrons.
- **Proton reader terminal:** no outgoing native operation from this selected
  P packet into another selected packet, including same-body reader advances.
  This is relative to the selected configuration. It does NOT mean the source
  grammar supplies no possible outgoing PN or advance operation.
- **Whole proton body terminal:** no selected reader on that P body has an
  outgoing native operation into a different occupied nuclear body. Same-body
  reader advances are permitted in this definition.

The latter two definitions are different, not an implication hierarchy. A
single proton body can have one terminal reader and other readers participating
in the nuclear network. The positive isotope examples rely on that distinction.

## Positive deletions

Cell IDs refer to each source witness's own regenerated universe.

| Source | Deleted neutron cell | Resulting counts | Eligible PE shortcuts |
|---|---:|---|---:|
| N-15 | 16 | 7P/7N/7e | 1 |
| N-15 | 17 | 7P/7N/7e | 2 |
| Ne-22 | 16 | 10P/11N/10e | 2 |
| Ne-22 | 29 | 10P/11N/10e | 1 |

For each positive variant, every selected record is reachable from the original
root, every record reaches an electron exit, and every occupied face contact
has a selected operation witness. The checker reconstructs a rooted sequence
of native operations and experimental shortcuts, and checks original geometry/
role guards on every prefix. Full operation lists and selected packet IDs are
saved with the receipt.

These positive N-14 deletions are NOT the earlier promising deletions at cells
8 and 12. Those earlier candidates already had exits but lacked nuclear entry
routes; the sink-only shortcut does not repair them. The new successful
candidates delete exit-supporting neutrons instead and use the edge shortcut
to restore electron access.

## Structural reason and boundaries

Adding only edges into terminal electrons cannot make any previously unrooted
nuclear record reachable: no path continues from E into a nucleus. The checker
asserts this invariant for every trial. The successful cases already have all
retained nuclear readers rooted; they lack terminal electron connections.

No special last-added electron, isotope-specific coefficient map or changed
root is needed in the tested cases. One shortcut suffices for at least one
N-14 and one Ne-21 candidate. This supports a shared candidate repair, but the
new admission premise is explicit: a validated two-face reference map may be
used with its intermediate N unoccupied. Source validation of the two factors
does not itself derive that premise or establish an edge-local field law.

This probe does not search alternative readers, geometry or arbitrary larger
assemblies. It does not implement electron-to-proton propagation, physical
binding, nuclear spin coupling or global coupled-field sewing. No production
selector was changed and no native certificate was relabelled as passing.

## Reproduction

```sh
node research/strominger/checkers/probe_terminal_pe.mjs
```

Evidence: `results/terminal-pe-probe/verification.json`, including all hydrogen
markings, 20 neutron-deletion trials, composed maps, construction sequences,
terminality conditions and source hashes.
