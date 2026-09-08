# Source-admissible comparisons: Cubical interface

## Question

How do extension interfaces retain the distinction between an unrestricted filler, an admissible filler for fixed maps, replacement of those maps, and transport of normalization?

## Claim boundary

`agda/SourceAdmissibleComparisons.agda` imports the previously checked extension-fibre module. It defines a caller-supplied admissibility predicate on pointwise paths and a forgetful projection. `MapReplacement` names two maps without claiming they agree. `transportExtension` requires a pointwise comparison; `transportNormalization` requires a commuting readout square. Neither constructor silently supplies these witnesses.

Checked regressions: a nonempty restricted marking type can have an empty fibre at a boundary that extends in the unrestricted type; replacing an endpoint can destroy filler existence; an unrestricted path need not satisfy a supplied constraint; a change of markings need not preserve normalization. These are constructive refutations, not expected compiler failures.

The admissibility predicate must still be instantiated with source-derived coefficient, localization, grading, and transport conditions. These abstract examples do not formalize the polynomial obstruction, Gysin comparison, octagon chain maps, or full higher descent. No physical authority follows from declaring a predicate. Pairwise path data do not certify arbitrary higher coherence. No analytic evaluator interface was changed.

## Disposition

Passed Agda 2.8.0.1 with Cubical 0.9, `--safe --cubical --guardedness`, no holes or postulates. Targeted check exited 0 with no warnings:

```
pwsh -NoProfile -Command "& 'C:/Users/andrey/tools/agda-2.8.0.1/agda.exe' --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/SourceAdmissibleComparisons.agda"
```

Operator-authorized shell fallback applies to Agda execution because structured-command excludes Agda. The first run exposed a binder collision with Prelude's `lift` constructor and an unsupported indexed-pattern computational warning. Renamed the binder and represented the restricted locus by a path to `first`, eliminating indexed matching; rerun passed. All file mutations used filesystem MCP. No aggregate rebuild, installations, Git commands, commit, or push. New owned files are this packet and its Agda module; the earlier extension module remains unchanged.

The first missing physical object remains a source-defined normal-line/Gysin comparison with its readout square. Acceptance for that separate branch requires an actual source construction, not another abstract witness requirement. This interface does not claim to fill that gap.
