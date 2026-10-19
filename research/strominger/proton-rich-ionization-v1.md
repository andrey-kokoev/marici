# N-13 and O-14 with fewer electrons

## Result

Both targets have compatible **four-electron ion references** under the repaired
all-contact gate. Neither has a complete five-electron geometry in the same
bounded search. These are not neutral-atom references or stability predictions.

| Target | P / N / e | Charge | Complete geometry candidates | Phase result |
|---|---|---:|---:|---|
| N-13 | 7 / 6 / 5 | +2 | 0 | No candidate to compile |
| N-13 | 7 / 6 / 4 | +3 | 3,592 | First passing reference found |
| O-14 | 8 / 6 / 5 | +3 | 0 | No candidate to compile |
| O-14 | 8 / 6 / 4 | +4 | 504 | First passing reference found |

Every geometry search completed within the existing rooted 343-cell ansatz.
Nuclei were allowed to rearrange; these searches do not retain the selected
C-12. All six root markings were included and original MMCC, contact, split-E,
occupied-native-P-reference and port-budget assumptions were kept.

## Phase witnesses and search limits

The repaired compiler and independent auditor enforce native transport,
full five-slot maps, actual occurrence histories and origins, all physical
contact witnesses, and entry-to-E-exit coverage.

- **N-13+++**: candidate index 33, orientation **470**; **49** certificate
  states, **17/17** carriers covered. First success after **68,055** reader
  assignments out of **5,566,464** total assignments over all geometries.
- **O-14++++**: candidate index 9, orientation **2454**; **60** states,
  **18/18** carriers covered. First success after **39,319** assignments out
  of **2,064,384** total assignments.

Both phase sweeps stopped at their first witness. A prospective cap of 250,000
assignments per charge state was not reached. No uniqueness, full acceptance
count or exhaustive phase classification is claimed. Saved references were
recompiled in a fresh process and matched exactly, including independent
contact and history audits.

## A retained N-13 -> O-14 structural chain also works

The independently found O-14 witness is not the same geometry as the N-13
witness plus a proton. A separate search therefore retained the newly found
N-13 nucleus, all four electron cells, C/M roles and native readers.

That retained search finds **one geometry candidate**: add proton cell **55**.
All **4,096** reader assignments were tested. Exactly one, orientation **918**,
passes and preserves every old reader and transport edge. It has **55**
certificate states and covers **18/18** carriers with all contacts witnessed.

Thus a four-electron structural chain is available:

`N-13+++ + P -> O-14++++`

This arrow denotes compatible retained endpoint assemblies only. It does not
model motion, tunneling, gamma emission, energy/momentum balance or a physical
reaction rate. No claim that these are the dominant stellar charge states is
made. The earlier selected C-12 -> N-13 retained route is still blocked; this
chain begins from a rearranged N-13 reference, not that selected C-12.

## Why four differs from five in this ansatz

The four-electron witnesses each have four NN contacts. Six neutron cells
supply twelve MCC ports; four NN contacts consume eight, leaving a necessary
budget of **four** distinct E attachments. A fifth E cannot be added to these
fixed nuclei under the same port bookkeeping. This is an internal representation
constraint, not a physical rule limiting atomic electron populations.

The exhaustive five-electron geometry searches also allow nuclear rearrangement
but still fail: for N-13, 2,064 typed nuclei yield 3,824 five-E combinations,
all with E/E adjacency; for O-14, 288 typed nuclei yield 528 combinations,
likewise all rejected. The successful four-E search admits additional nuclei
with four NN contacts, which the five-E budget had necessarily pruned.

## Meaning

The repaired rules can represent **radioactive N-13 and O-14** at these charge
states. Together with the admitted radioactive Li-8 control, this reinforces
that compatibility is not a stability criterion. Neutralization, beta decay,
physical nuclear closure and E/E contact laws remain separate open problems.
No viewer or production rule was changed for these probes.

## Reproduction

```sh
node research/strominger/checkers/check_proton_rich_ionization.mjs
node research/strominger/checkers/check_proton_rich_ionization_witnesses.mjs
```

Evidence:
- `results/proton-rich-ionization/verification.json`: all four geometry sweeps,
  phase-search limits/rejections, source hashes and two complete witnesses.
- `results/proton-rich-ionization/replay-and-chain.json`: fresh witness replay,
  port-budget checks and complete retained-chain search with its certificate.
