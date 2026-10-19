# N-14: controlled assumption tests

The [protocol](n14-assumptions-protocol-v1.md) was fixed before the probes.
All geometry sweeps completed; no resource limit was reached. Production
admission rules, isotope selections and viewer files were not changed.

## Results

| Change from baseline | Domain cells | Typed nuclei | Complete geometry candidates |
|---|---:|---:|---:|
| None | 343 | 2,384 | 0 |
| Permit E/E face contact, geometry diagnostic only | 343 | 2,384 | 5,632 |
| Permit regular OR split electron cells; E/E still forbidden | 343 | 2,384 | 0 |
| Add one full neighboring-item shell; split electrons | 875 | 2,912 | 0 |
| Larger shell AND regular/split electrons; E/E still forbidden | 875 | 2,912 | 0 |

The enlarged domain is a geometric superset, not a rescaling. Whole neighboring
tetrahedral/octahedral items are generated through their actual faces using
`acrossFace` and the same subdivision. All original cells keep their indices
and coordinates. Every face of every original cell now has a neighbor in the
expanded domain; the original boundary is fully surrounded.

## What each experiment says

### 1. Electron nonadjacency is the immediate packing obstruction

Removing just the E/E face exclusion recovers all 5,632 seven-electron choices
previously rejected. This supplies **packings only**. The unchanged phase
compiler explicitly rejects a root-compatible example with
`Unsupported physical face contact`. No E/E transport law, coefficient sewing
rule or exit-certificate exception was supplied. None was promoted to an
admitted isotope or added to the viewer.

This does not establish that E/E contact should be permitted physically. It
identifies which current test removes the otherwise eligible geometries.

### 2. The split-only electron restriction is not the sole cause here

Allowing regular electron tetrahedra changes neither the eligible-electron
pool histogram nor the result for these N-14 nuclei. In 343 cells, 1,920 typed
nuclei have seven individually eligible electron positions and 464 have eight.
Every selection of seven still has an E/E face contact.

This is not a general claim that regular electron targets never occur: the
common native constructor does allow them in other seed/reader embeddings.
The change simply supplies no extra eligible positions for the nuclear
arrangements surviving this experiment's other restrictions.

### 3. One additional shell does not fix the failure

The 875-cell domain produces 528 additional typed nuclei. Its electron-pool
histogram is 2,240 nuclei with seven positions and 672 with eight. All
`2,240 + 672 * choose(8,7) = 7,616` electron selections violate the E/E ban.
Allowing regular electrons simultaneously changes neither histogram nor outcome.

Thus the result is not cured by this first boundary enlargement. It does not
exclude still larger or unbounded domains, other reference conventions, or a
non-tetrahedral representation of electrons.

## Interpretation

Within the tested representation and other fixed rules, the **E/E full-face
exclusion is the immediate obstruction**. The experiments do not justify simply
deleting that rule to admit a known stable isotope. The next foundational audit
is what an E/E geometric contact means, whether terminal E readers entail such
a prohibition, and what occurrence/coefficient boundary compatibility would be
required if contact were permitted. No answer to those questions was invented
by this packing test.

In particular, N-14 remains physically stable but unrepresented by the current
admission framework. These results are not a stability or binding calculation.

## Verification and reproduction

The independent diagnostic enumerator reproduces the production baseline's
full prefix counts, typed-nucleus count, eligible-pool histogram and all 5,632
rejections. Early role pruning uses the same restriction-of-coloring argument.
The expanded-domain phase adapter changes only lattice/domain bindings and
asserts byte-identical compile/audit function bodies. Since the enlarged cases
have no geometry candidates, **no enlarged-domain phase witness was claimed**.

Run:

```sh
node research/strominger/checkers/check_n14_assumptions.mjs baseline
node research/strominger/checkers/check_n14_assumptions.mjs ee
node research/strominger/checkers/check_n14_assumptions.mjs regular
node research/strominger/checkers/check_n14_assumptions.mjs larger
node research/strominger/checkers/check_n14_assumptions.mjs larger-regular
node research/strominger/checkers/summarize_n14_assumptions.mjs
```

Each receipt records source/protocol fingerprints, domain and pruning counts,
completion status and any witness. Fingerprints are checked before/after each
run and against one another by the summarizer. Evidence is under
`results/n14-assumptions/`; `verification.json` gives the checked comparison,
`ee.json` contains the unsupported-contact packing witness, and the enlarged
receipts preserve the expanded cell coordinates and component provenance.
