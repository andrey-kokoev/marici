# v190: explicit strict-transform tubular prism

The wall-relative chain now has an explicit collar inside the qg2 strict
transform. In coordinates `(x,a,xi)`, define

`H(r,t)=(r, p-r(kappa/2-1), -1+t(1-kappa))`.

The strict-transform wall equation

`qg2=a-p+x(kappa/2-1)`

pulls back identically to zero. The face `r=0` is the endpoint-to-conductor
relative chain; `r=epsilon` is its lifted physical-wall chain. The face `t=0`
lies exactly on `qg1: xi+1=0`, and `t=1` specializes to the conductor point
`xi=-kappa`. The prism transports the cut orientation through the collar.

This constructs the first nearby-cycle/tubular transport rather than merely
postulating it. The remaining checks are the higher-order ambient conductor
face and promotion of this algebraic collar to the literal ringed filtered Q
comparison.

Evidence is `results/qg2-tubular-prism.json`.
`rzk/218-qg2-strict-transform-tubular-prism.rzk.md` passes all eight declarations
without assumptions.
