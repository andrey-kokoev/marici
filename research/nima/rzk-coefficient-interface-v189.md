# v189: explicit physical qg2 relative cut chain

On the normalized qg2 wall, the endpoint and conductor poles are at `xi=-1`
and `xi=-kappa`. For `kappa != 1`, the affine singular chain

`xi(t)=-1+t(1-kappa), 0<=t<=1`

joins them and meets either pole only at its corresponding endpoint. Its
relative boundary is `[-kappa]-[-1]`. Reparameterization by `t -> 1-t`
reverses the chain and negates its orientation, supplying the sign character
required in v188.

Thus the wall-relative chain inhabitant is now explicit rather than merely a
formal orientation line. The remaining geometric gate is its ambient tubular
or nearby-cycle transport from the normalized qg2 wall into the physical
ringed filtered target, followed by identification of its boundary with the
selected logarithmic road generator.

Evidence is `results/qg2-explicit-relative-cut-chain.json`.
`rzk/217-qg2-explicit-relative-cut-chain.rzk.md` passes all eight declarations
without assumptions.
