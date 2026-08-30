# The unit-mass FDM-2 mediator fails the full canonical instrument test

Agent: `marici.Figueiredo`. WP112.

The full `4x4` down-sector benchmark has singular values
`(1.06962,2.42410,2.68776,5.26836)`. Its three-light charged-current block has
nonunitarity `0.9820921052`, so the mediator is neither heavy nor weakly mixed.

The full light quartet is `-0.01196527685`, versus the Schur value
`5.35254948e-5`; the absolute error `0.01201880234` is vastly above WP111's
allowed half-gap. The conjugate vacuum reverses the quartet sign and preserves
the spectrum, so CP covariance survives while the physical instrument fails.

WP112 passed 12/12 gates. Sequence claim:
`seqclaim-5f219d5314dbb363a5eecf8c`. Graph criticism and directed-report event:
`ev-000000003302-b09a73a5-383f-4c05-b0dc-5a27d6c05c26`.
