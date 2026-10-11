# The full Bool Tick is classified by its ordered schedule tags

## Original question

Does retained Tick structure constrain continuous dynamics beyond its discrete
readout? Before constructing more analytic models, determine whether the
omitted fields actually carry independent information.

## Checked result

`agda/TickRetainedStructure.agda` proves, for `O = R = Bool`,
`e = notEquiv`, and a fixed source `s : Bool × Bool`:

    Tick(s) ≃ Schedule × Schedule

This is an equivalence of the FULL existing record, not a replacement
record that discards the return section. `tick-equiv-tags` supplies the
forward map, reconstruction, and both inverse laws.

The current `ComparedRoutes` type does not require the schedules to be
distinct. Thus the classification includes all four ordered pairs, not
only fresh and swapped.

Additional checked consequences:

- `canonical-return-section`: the complete dependent return-section
  function equals the canonical backward section at the attached source.
- `readout-injective`: equal existing discrete readouts imply equal full
  Bool Ticks at the same source.
- `observation-factors`: every ordinary type-theoretic map from a full Tick
  into any type agrees with its value on the reconstruction from the tags.

## Why the interior cannot independently vary here

A section of the fixed cubical square family is determined up to path
by its value at `(1,1)`. `SectionExt.section-ext` proves this by transporting
along the ray from that corner to each point. The argument does not claim
that arbitrary higher cells with a fixed boundary have unique fillers:
this particular section field has no independently fixed edge boundary.

The end law and source attachment fix its corner. For the Bool
specialization, endpoint identity types and route-function identity types
are propositions, so the remaining law witnesses cannot distinguish two
records with equal tags. The record path explicitly includes those laws.

## Correction to the previous assessment

Omitting fields syntactically does NOT imply losing distinguishable
mathematical information. The prior worry that the full return-section
interior might invalidate the readout's classification is now resolved
for this Bool specialization. The readout is injective up to path equality.
This does not establish equivalence between arbitrary raw readouts and
Ticks: arbitrary readouts need not satisfy the Tick laws.

## What this says about dynamics—and what it does not

There is no additional independent Bool Tick information hidden in the
omitted fields for an equality-respecting observation to exploit.
An analytic interpretation may still supply additional structure and
compatibility obligations. The classification alone neither selects such
an interpretation nor proves non-uniqueness modulo time reparameterization.
A finite source can be assigned a unique evolution by an external rule;
counting source states is not a no-go theorem for that possibility.

That successor task is now settled for the declared stochastic class in
`tick-admissible-interpretations.md`: two path images are inequivalent under
any parameter substitution. Separately, `tick-unitary-image-nonuniqueness.md`
now excludes image uniqueness in its declared commuting unitary annotation
class, without claiming to classify all unitary interpretations.
The structural classification here remains closed; neither additional
polynomial continuity work nor a new physical-selection question reopens it.
Current source-to-generator disposition: `source-to-generator-audit.md`.

## Verification

Fresh headless Agda with `--safe --cubical --guardedness
--ignore-interfaces` exits 0. Includes: Nima Agda, both Nima adapter
folders, Cubical 0.9. Only the existing `TypedGeneratorLayers` export
warning remains. No Voevodsky analytic modules are needed for this result.
