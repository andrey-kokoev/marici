# v196: local raw physical Cech defect equals the road boundary

The missing raw function is now defined on the selected qG12 wall sector from
the source Leray frames, independently of the road construction:

`rawCech_qG12 = dlog(n12/n31)`.

Here `n12=-1/(2 X1 X2)` and `n31=-1/(2 X3 X1)`, so the labelled G31-to-G12
transition is `X3/X2`. In the homogeneous qG12 chart it is `-v/(v-2)`.
Under `v=2(xi+1)/(1-kappa)`, its logarithmic differential is exactly

`dlog((xi+1)/(xi+kappa))`.

The independently constructed ramified relative road boundary has the same
rational one-form. Therefore the raw local physical Cech defect equals the road
boundary and the selected local Cech direction is killed by road correction.
This statement is deliberately local to the one labelled qG12 sector and does
not assert the unsupported global three-cut Cech cover.

Evidence is `results/qg12-raw-physical-cech-formula.json`.
`rzk/224-qg12-raw-physical-cech-road-equality.rzk.md` passes all eight
declarations without assumptions.
