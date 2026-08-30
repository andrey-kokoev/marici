# Accidental-coincidence audit for the X-state determinant

## Question

When does side-window subtraction remove accidental coincidences from the
four correlation records, and when can background structure manufacture a
false determinant sign?

## Exact subtraction contract

Write the prompt counts as signal plus an additive background distribution
over the four coincidence channels. Side-window subtraction is exact when the
side window transports that complete channel-resolved distribution to the
prompt window with the correct exposure factor.

Matching only the total accidental rate is insufficient. The background can
carry a setting-dependent same-versus-different correlation even when its
total rate is correct.

## Decisive hostile

Start from the existing true-boundary X-state record. Add background at one
percent of the signal rate, with correlation `+1` in `XX` and `-1` in `YY`,
`XY`, and `YX`. Subtract a side window with the correct total rate but a
uniform four-channel distribution.

The residual shifts the four correlations by the signed background amount and
produces false NPT determinant `3/4000`. Thus a total-rate sideband monitor
cannot certify the physical determinant.

## Calibration consequence

Record every side-window coincidence channel under every analyzer setting,
and transport the full background distribution with an independently checked
exposure ratio. Any channelwise mismatch becomes part of the corresponding
correlation error radius.

In the frozen exposure hostile, underestimating a fully polarized background
by `1/1000` leaves correlation residual `1/1000`. This is a typed readout error,
not source coherence.

## Claim boundary

The model assumes additive background and linear detector response. Dead time,
pileup, saturation, afterpulsing, and finite side-window counts violate or
enlarge this contract and remain separate detector ports.

## Verification

Run:

```text
python research/aspect/checkers/check_accidental_coincidence_x_state_determinant.py
```

The dependency-free exact checker verifies matched subtraction, the
equal-total hostile, its false determinant, and an exposure-mismatch residual.
