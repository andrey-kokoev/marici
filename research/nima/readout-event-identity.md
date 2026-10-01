# Aliases versus new traversal events in the rung4 readout

## Tested distinction

Each retained event receives an explicit identity and four-component label
vector. A presentation is a sequence of references to events. Referencing one
event twice is distinct from retaining a newly performed event with the same
label vector. The test supplies these identities; it does not infer novelty
from an identical or different numerical payload.

Start with two events a,b in two seed directions. Compare:

- alias: [a,b,a];
- fresh event: [a,b,a_new], where a_new has the same vector as a;
- fresh replay: [a,b,a_new,b_new].

Use the same G4 contrast projection and seed-edge units as the previous readout.

| Readout | Spatial change under alias | Under one fresh event | Under full fresh replay |
|---|---:|---:|---:|
| Sum of presented references | squared change3/8 |3/8|1/2|
| Sum of unique events |0|3/8|1/2|
| Average of unique events |0|1/36|0|

The unique-event counts are respectively2 initially,2 after aliasing,3 after one
fresh event,4 after full replay. Average plus count recovers the additive vector
exactly in every test. Full event histories are retained separately; these
aggregate vectors do not reconstruct arbitrary event order or provenance.

## Outcome

Raw reference summation fails invariance under re-presentation. Identity-aware
sums and averages both pass. Full replay changes the accumulated sum and event
count while preserving the average spatial location. Hence the test distinguishes
new events from duplicate references, but does not force event count to appear
in physical distance rather than a separate retained quantity.

The earlier growing-graph metric added ancestral endpoint-occurrence vectors.
It did not specify which repeated ancestral occurrences represented new performed
traversals versus additional references to existing history. Its expansion
result therefore remains conditional on that identity interpretation. Event
novelty must be tied to the actual interaction records before their multiplicity
can serve as a physical length or clock readout.

## Verification

```
python research/nima/checkers/check_readout_event_identity.py
```

All exact rational assertions passed. Artifacts:

- `checkers/check_readout_event_identity.py`
- `results/readout-event-identity.json`
