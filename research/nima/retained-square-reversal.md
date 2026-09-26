# Reversal of the actual retained source square

Obligation: route/coherence compatibility, before scalar readout.

`ObserverCoherenceCube.Geometry` already contains a type-valued square
`square i j = axis i × axis j`, with `axis = ua e`, and a source-dependent
section over the whole square. It also retains `leftFirst` and `rightFirst` as
distinct schedules although their evaluated maps agree. `nextQ` retains the
source, schedules, comparison, target and target law.

`agda/RetainedSquareReversal.agda` constructs the backward cell and section by
reflecting BOTH cubical interval coordinates:

```text
backward-cell i j = square (~ i) (~ j)
backward-section s i j = square-section s (~ i) (~ j)
```

The section starts at the actual developed pair and ends at the original source
pair. Reflecting twice recovers the original cell and its section pointwise.
`RetainedReturn` keeps the entire original `RealizedSquare` alongside this return
section and its endpoint laws. `next-returned-Q` packages the record through the
existing `WholePackageSigmaPi.Universe` constructor. Recovery proves that the
original forward package, source, and both distinct schedule tags survive.

This constructs the canonical reverse of the existing square, a concrete part
of rule 2. It makes no claim about arbitrary independently chosen backward
witnesses or the full higher comparison conditions in rules 3–5. The formal
double-reflection identity is recorded as a consistency law, not relabeled as
the entirety of rule 3. No complex coefficient field, probe or physical readout
is introduced.

Fresh safe/cubical headless compilation passes:

```text
pwsh -NoProfile -File research/nima/checkers/check_retained_square_reversal.ps1 -Fresh
```

Receipt: `results/agda-RetainedSquareReversal.json`. The existing source modules
were read and imported; this work adds new owner-local files only.
