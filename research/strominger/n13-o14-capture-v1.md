# N-13 and O-14: retained-capture and bounded count tests

**Follow-up:** [four-electron ionization tests](proton-rich-ionization-v1.md)
now find all-contact-compatible N-13+++ and O-14++++ references, including a
retained N-13 + proton endpoint chain. Five-electron searches still fail.
The six-or-more-electron negatives and selected C-12 obstruction below remain
scoped to their tested charge states and retained core.

## Retained C-12 route

The selected C-12 reference passes its existing phase audit (18 carriers), but
**cannot accept an additional adjacent proton while retaining its nucleus**.
There are no unoccupied regular proton cells sharing a face with that nucleus.
Stripping its electrons does not change this: the bare retained-core control
also has zero adjacent proton extensions. This is not an electron-packing
failure at the first retained step.

Consequently there is no retained N-13 precursor on which to run the proposed
second proton addition. The conditional O-14 and neutralization stages were
**not reached**, not counted as independently executed negative phase tests.

## Additional searches without retaining C-12

To test both isotopes despite the blocked precursor, five complete geometry
searches were run over the existing rooted 343-cell domain, allowing nuclear
rearrangement and all six root MMCC markings. Contact rules, split nonadjacent
electrons and the occupied native-P-reader requirement were unchanged.

| Target | P / N / e | Typed nuclei surviving necessary pruning | Complete assemblies |
|---|---|---:|---:|
| N-13+ | 7 / 6 / 6 | 2,064 | 0 |
| Neutral N-13 | 7 / 6 / 7 | 0 | 0 |
| O-14++ | 8 / 6 / 6 | 288 | 0 |
| O-14+ | 8 / 6 / 7 | 0 | 0 |
| Neutral O-14 | 8 / 6 / 8 | 0 | 0 |

For N-13 with six electrons, 1,712 typed nuclei offer only five individually
eligible electron cells. The other 352 offer six, but selecting all six creates
an E/E face contact in every case.

For O-14 with six electrons, 240 typed nuclei offer five electron cells; the
other 48 offer six but likewise fail the E/E exclusion.

The seven/eight-electron searches prune earlier. Six neutrons supply twelve
MCC ports; each NN contact consumes two and each distinct electron needs at
least one. Reserving seven or eight electrons therefore permits at most two
NN contacts. No target nuclear geometry survives that bound in this domain.
This does not mean there are no nuclear geometries when the electron quota is
removed: the six-electron searches already demonstrate otherwise.

No candidate reaches phase compilation in these five searches, and no new
isotope is added to the viewer.

## Meaning and limits

Unlike the successful C-13 + P six-electron N-14+ reference, the proposed
C-12 + P route is blocked at retained-core attachment. Even rearrangement does
not produce a complete N-13 or O-14 reference at the electron counts tested.

These are model limitations, **not predictions of radioactive decay**. N-13
and O-14 physically exist and are radioactive. Our tests neither simulate
proton capture nor derive decay, binding, lifetimes or beta transitions.
More strongly ionized states (five or fewer electrons), larger domains and
other electron representations were not tested here. Negative results remain
conditional on the bounded ansatz.

## Verification

The independent count-parameterized enumerator is checked against the complete
production candidate lists for Li-5/6/7/8 and the established N-14 baseline
(2,384 nuclei and 5,632 electron-contact rejections). All five count sweeps
completed, without timeouts. Receipts include source fingerprints checked
before and after execution.

```sh
node research/strominger/checkers/check_n13_o14_capture.mjs
node research/strominger/checkers/check_proton_rich_counts.mjs
```

Evidence:
- `results/n13-o14-capture/verification.json`: retained-core route and bare control.
- `results/n13-o14-capture/unrestricted-counts.json`: all five broader count searches.

Production admission rules and viewer files are unchanged.
