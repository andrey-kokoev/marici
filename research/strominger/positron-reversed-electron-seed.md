# Positron: reversed electron seed

The collection now contains proton, neutron, electron, neutrino #1 and positron.

| Model | Seed cycle |
|---|---|
| Electron | A -> B -> C -> D -> E -> A |
| Positron | A -> E -> D -> C -> B -> A |

The positron generator is the exact affine inverse T^-1=T^4 of the existing electron generator. The metric, initial seed and attachment-pole role are unchanged.

Twelve exact checks pass:

- every primitive seed arrow is reversed;
- both compositions T T^-1 and T^-1 T are identity;
- both generators have order five;
- complete geometry, attachment and centroid selection are identical;
- derived five-corner characters change by k -> -k mod 5.

Thus the two records have the same four-simplex shape but opposite cyclic actions. The trivial character is fixed; the nontrivial characters pair as 1 <-> 4 and 2 <-> 3.

This operationalizes seed reversal, not yet reversal of the full native coefficient protocol. The next algebraic test is whether the existing external charge action is odd under this reversal.

## Files

- Source: `research/strominger/inputs/relative-positron-candidate.json`
- Checker: `research/strominger/checkers/check_positron_reversed_seed.py`
- Result: `research/strominger/results/positron_reversed_seed.json`
- Five-model collection: `research/strominger/results/arrow_particle_collection.json`

```sh
python research/strominger/checkers/check_positron_reversed_seed.py
```
