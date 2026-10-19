# Lithium discrimination: compatibility does not imply stability

## Fixed experiment

The [protocol](lithium-discrimination-protocol-v1.md) was written before the
sweep. Targets were Li-5 through Li-8 with 3P and 3e, the existing 343-cell
domain and unchanged geometry/phase acceptance rules. Only the enumerator's
target-count guard was widened from 3/4 to 2/3/4/5 neutrons. The same NN
reference assumption and native-proton-reader requirement apply throughout.
No retained-previous-isotope filter, stability labels, energy score or fitted
threshold entered the search. All enumerated reader assignments were tested.

## Results

| Target | Empirical ground-state status | Geometry candidates | Reader assignments tested | Accepted geometries / assignments |
|---|---|---:|---:|---:|
| Li-5 | Proton-unbound | 0 | 0 | 0 / 0 |
| Li-6 | Stable | 96 | 2,304 | 5 / 5 |
| Li-7 | Stable | 528 | 26,880 | 32 / 32 |
| Li-8 | Beta-minus radioactive | 3,744 | 119,808 | 10 / 10 |

All sweeps completed: 4,368 geometry candidates and 148,992 reader assignments
in total. Every accepted reference passed the full phase-history and entry/exit
coverage audit. The summary checker independently recompiled and audited all
47 accepted assignments from the saved records. Identical source hashes were
required across the four runs, and checked again against the current modules.

Li-5 fails before phase compilation: none of its 12 final connected nuclear
sets passes the typed-nucleus stage. This is a negative result in this bounded
neutral-assembly ansatz, not a proof of physical impossibility.

The larger Li-7 acceptance count is not inconsistent with the earlier retained
Li-6 result: that experiment required retaining the selected Li-6 geometry,
roles and readers. This experiment deliberately searches all candidates on
equal terms for all four targets.

## What this establishes—and what it does not

The rules do constrain assemblies: they reject Li-5 in this domain and admit
both stable lithium isotopes. However, they also admit ten Li-8 references.
Therefore **compatibility is not a sufficient criterion for empirical nuclear
stability**. Raw enumeration counts do not supply a justified stability ranking,
probability, binding energy or lifetime.

There is an important distinction: Li-5 is a proton-unbound resonance, whereas
Li-8 is a bound nucleus that undergoes beta decay (evaluated half-life 838.7 ms).
A geometrically and phase-compatible Li-8 assembly is not itself a contradiction.
What fails is interpreting acceptance as proof of stability against decay.
This small sample is consistent with the distinction between an assembly being
possible and being stable, but does not derive even a strong-binding criterion.

Do not add a Li-8 exclusion by hand to recover the desired labels. The remaining
physical question is whether an independently justified energetic or decay-channel
criterion can be obtained from the model. Until then, the admission label remains
**phase-coherent reference**, not physically stable nucleus. No unstable target
was added to the viewer and the phase/compiler acceptance rules were not relaxed.

## Empirical baseline and reproduction

Ground-state labels and the quoted half-life were checked against
[NUBASE2020](https://www-nds.iaea.org/amdc/ame2020/nubase_4.mas20.txt),
[publication DOI](https://doi.org/10.1088/1674-1137/abddae).
The four source rows are preserved in
`results/lithium-discrimination/empirical-baseline.json`; that file is used only
by the post-search summarizer, not by enumeration or phase compilation.

Run each complete sweep, then validate and summarize:

```sh
node research/strominger/checkers/check_lithium_discrimination.mjs 5
node research/strominger/checkers/check_lithium_discrimination.mjs 6
node research/strominger/checkers/check_lithium_discrimination.mjs 7
node research/strominger/checkers/check_lithium_discrimination.mjs 8
node research/strominger/checkers/summarize_lithium_discrimination.mjs
```

Evidence: `results/lithium-discrimination/li5.json` through `li8.json` contain
stage counts, rejection histograms, all accepted geometry/reader assignments,
first full certificates, and source/protocol/checker hashes.
`results/lithium-discrimination/verification.json` contains the validated
comparison. The counts are rooted, typed enumeration counts—not
symmetry-quotiented counts of distinct physical nuclei.
