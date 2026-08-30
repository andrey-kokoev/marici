# Predecessor invariance alone certifies a blinding reset

A reset can remove predecessor dependence by mapping every target to the same output. Such a channel passes the current invariance gate perfectly and destroys the experiment.

The exact hostile compares two four-target transfer matrices. The identity reset has rank four and infinity-norm reconstruction condition one. The blinding reset has four identical rows and rank one. Both can have zero predecessor spread, but only the first retains target information.

Reset qualification must therefore impose a joint gate: predecessor dependence disappears while an independently calibrated spanning target family remains reconstructible through the reset with full rank and a frozen condition-number bound. Neither property substitutes for the other.

Executable witness: `checkers/check_blinding_reset_falsifier.py`.
