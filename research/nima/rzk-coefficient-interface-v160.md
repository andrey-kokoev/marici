# v160: global locally finite L2 coefficient map

The all-degree support bound now constructs one global map rather than merely a
compatible family of truncations. Apply the exact labelled p/q column formula
termwise to any finite polynomial source.

Because every term raises degree by between 2 and 7, source support in `[m,D]`
maps into `[m+2,D+7]`. The result is finite, and every cutoff matrix is the
strict restriction/projection of this single global operator.

Thus the global coefficient-level L2 chain map is now available; finite-cutoff
rank completion was not used to infer it. Two separate gates remain before
physical road-Cech closure: identify this coefficient operator with the
geometric soft nearby-cycle road map, and construct compatible integral
2/3-primary saturation data.

Evidence is `results/L2-global-locally-finite-chain-map.json` from
`checkers/check_L2_global_locally_finite_chain_map.py`.
`rzk/188-l2-global-locally-finite-chain-map.rzk.md` passes all eight declarations
without assumptions.
