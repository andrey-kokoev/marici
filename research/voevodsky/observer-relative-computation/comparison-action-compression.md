# Partial comparison retention: sufficient for one observer, not for the path

`agda/ObserverComparisonCompression.agda` introduces a first-order comparison language with stay, turn, and composition. Expressions are finite trees over a finite constructor vocabulary; the set of expressions is not finite. No evaluator callback is stored, and no completeness claim for arbitrary paths or inverse-loop expressions is made.

## Checked positive result

Each word has a retained parity bit. For EVERY Boolean input, transport along the interpreted path equals the Boolean action of that parity. Applying the parity action to the displayed value agrees with the full anchored normalization that uses the actual inverse comparison path. In particular it faithfully recovers every supplied Boolean value after manifestation.

Thus retaining the entire comparison path is unnecessary for this observer's readout. Retaining nothing was insufficient in the previous leaf; retaining its one-bit action is sufficient here.

## Checked loss of semantic witness information

A new three-state cover cycles zero→one→two→zero along the same underlying loop. Two turns and stay have identical Boolean parity, but the three-state observer reads two and zero. This proves their actual interpreted paths are unequal—not merely their constructor labels.

Therefore no decoder from parity can faithfully recover every interpreted comparison path in the language. Observer-relative readout sufficiency is strictly weaker than full comparison-witness recovery. The proof does not identify comparison paths inside a fixed fibre merely because one observer gives the same readout.

## Verification

Fresh safe Cubical Agda --ignore-interfaces -Werror passes: results/agda-comparison-compression.log. The aggregate includes the module. Fresh check_transport_gate.py passes local/whole ordinary/whole strict checks with inventoried source bytes unchanged: results/transport-gate.json.

## Continuing frontier

Investigate joint observer refinement: combine the binary and ternary actions, characterize the information retained jointly, and distinguish refinement from complete path recovery. Test incomparability of the two individual observation partitions and residual witness loss after combining them. This continues the observer-relative programme beyond this dispatch; iteration exhaustion is not a foundational conclusion or terminal programme state.
