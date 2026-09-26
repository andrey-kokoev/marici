# Exact descent classification for internal coded observations

`agda/ObserverCodedAnchorDescent.agda` connects the finite internal code calculus to the higher-witness anchor example. A code observes the anchored Boolean by replaying it into the already proved History/Bool correspondence and applying the existing readout interpreter. No new observer callback constructor is added.

A descent witness specifies a function on forgotten reply/value pairs together with agreement on every original anchored record. This is the logical specification being tested, not a new primitive in the code language.

Checked results:

- Every result-only code descends, with an explicit constant function and its agreement proof.
- Every rule-sensitive code fails to descend: any proposed factor would recover the forbidden anchored Boolean normalization.
- Thus descent exists exactly for result-only codes; a total decision returns a factor or a refutation.
- Descent is preserved by every structural restriction in the internal calculus.
- Duplicate rule access still cannot descend, while paired result-only observations do exist.

The theorem classifies this language's observations of anchored content, not all possible observations of the unanchored space. In particular, failure of faithful rule access does not mean that observation itself disappears. It also does not identify a geometric observer area or prove a universal computation claim.

## Verification

Fresh safe Cubical Agda --ignore-interfaces -Werror: results/agda-coded-anchor-descent.log. The aggregate imports include the module. Fresh check_transport_gate.py passes local/whole ordinary/whole strict checks with inventoried source bytes unchanged: results/transport-gate.json.

## Next

The present tests compare retaining the whole comparison with forgetting it entirely. Investigate the intermediate case: retain only the comparison's finite action on the Boolean observer. Extend first-order comparison codes compositionally and test whether parity suffices for faithful observed-value normalization while failing to recover the full comparison path. Keep observer-relative sufficiency separate from reconstruction of all witness data.
