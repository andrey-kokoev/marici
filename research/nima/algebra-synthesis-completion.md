# Synthesis completion: minimum closed, fresh adequacy open

## Result

`agda/SynthesisCertifiedMinimum.agda` now constructs the **original
`Goal.Result`**, at every universe level. Its adequacy component deliberately
reuses the existing proof; its minimum component is new and kernel checked.
The grammar and quantified Boolean-algebra predicate have not been weakened.
The minimum is six operations, hence 15 symbols in the declared grammar;
uniqueness is not asserted.

**The stronger request remains incomplete:** fresh proof search has not
constructed an independent `Adequate` witness. This is not reported as full
success or as autonomous formula-to-proof synthesis. The old benchmark and
its receipts remain separate.

## Exhaustive kernel coverage

- `SynthesisMinimumSupport.agda` defines size-indexed syntax, an erasure
  retraction to the original equation syntax, the ordinary two-element
  Boolean structure, and explicit non-Boolean finite models.
- `GeneratedMinimumShape0.agda` through `GeneratedMinimumShape195.agda`
  contain universally quantified refutation templates. Unresolved variable
  labels are parameters, not representative assignments.
- `GeneratedMinimumCoverage.agda` covers every admissible formula cheaper
  than six. Its 196 complete equation shapes are covered by Agda pattern
  matching; 429 partial tree prefixes reject larger syntax using the cost
  inequality. Noncanonical natural-number labels contradict the original
  `normal` predicate.
- Canonical prefix splitting compresses the 125,105 cheaper identities into
  8,576 refutation templates and 2,786 noncanonical branches. These counts
  are descriptive: the proof does **not** trust Python's enumeration count.
- Removing an actual normalized branch produces `[CoverageIssue]`.
  Mutating a Boolean refutation produces `[UnequalTerms]`.

The initial monolithic certificate exceeded its compilation budget. It was
partitioned by shape; finite carriers use Bool, Maybe Bool, and Bool × Bool.
An initial ambiguous lift level and an indexed-pattern unification failure
were corrected without changing the goal. Fresh safe compilation now passes.
Agda reports indexed-match transport-computation warnings for the size-indexed
syntax; no executable extraction or runtime-refinement theorem is claimed.

## Fresh search boundary

`checkers/fresh_equational_search.py` implements bounded proof-producing
completion, unification, critical pairs, simplification, backward
simplification, and weight/age selection. It loads the supplied axiom, not
published derivations or the existing adequacy theorem.

The final run used the previously enumerated cost-six candidate as an
**explicit benchmark input**, not autonomous candidate selection. Under a
60-second, 600-record, weight-70 budget it produced 90 checked records:
the input axiom and 89 newly derived equations. None of the four standard
Boolean NAND basis goals was derived. Budget exhaustion means unresolved,
not inadequate.

`check_fresh_equations.py` independently checks the inference DAG and input/
goal bindings. `FreshEquationalConsequences.agda` checks the emitted paths
using only Cubical Prelude and the supplied axiom as a parameter. A mutated
conclusion is rejected. These are conditional consequences, **not** a fresh
adequacy certificate. Boolean validity, reconstruction, and autonomous
selection still need a completed positive backend.

## Evidence and reproduction

Fresh checks and all three new negative controls passed:

- `results/synthesis-kernel-formal-audit.json`
- `results/fresh-equations-kernel-formal-audit.json`
- `results/synthesis-completion-audit.json` — 15 new tests
- The existing benchmark's 18 tests also pass unchanged.

Commands, run as separately admitted invocations:

```text
python research/nima/checkers/build_minimality_cover.py
python research/nima/checkers/emit_minimum_kernel.py
python research/nima/checkers/fresh_equational_search.py research/nima/results/algebra-formula-search.json research/nima/results/fresh-equational-search-final.json --ordinal 1488521 --seconds 60 --facts 600 --weight 70
python research/nima/checkers/emit_fresh_equations.py research/nima/results/fresh-equational-search-final.json research/nima/agda/FreshEquationalConsequences.agda
pwsh -NoProfile -File research/nima/checkers/check_synthesis_kernel.ps1 -Module FreshEquationalConsequences
pwsh -NoProfile -File research/nima/checkers/check_synthesis_kernel.ps1
python research/nima/checkers/check_synthesis_completion.py
```

The checker uses stable before/after inventories, fresh interfaces, a headless
compiler, owned-child timeout cleanup, and an ignored run manifest. Do not
rewrite Agda sources during either compiler check. Search timing can change
the number of derived records; rerun both formal checks after re-emission.

The local SCC packet declares forward realization and compatibility, not
scientific truth by admission. The first missing typed object is an
**independently derived `Adequate` witness**. A verified connection to the
previous Layer4 runtime remains a separate obligation.
