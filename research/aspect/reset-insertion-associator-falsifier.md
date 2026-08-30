# A reset can preserve the associator null while replacing the ternary experiment

A reset-native three-body phase of `pi` flips the entire ternary curve. Left and right bracketings still agree, so the associator remains exactly zero. Destructive and zero-coherence controls also remain zero. Every internal null gate passes while the reset has changed the scientific channel.

For the frozen coherence `3/5`, the direct curve without reset is `[3/5,0,-3/5,0]`; with the hostile reset it is `[-3/5,0,3/5,0]`. The reset cannot be authorized by the associator null it helps define.

Qualification must include a reset-insertion transport gate: measure the direct ternary curve with and without the reset under matched hardware, phase, and calibration conditions. Both bracketings are then compared with the independently preserved direct curve. A reset that changes direct ternary transport is rejected even when its left-minus-right residual vanishes.

Executable witness: `checkers/check_reset_insertion_associator_falsifier.py`.
