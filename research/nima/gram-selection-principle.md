# Gram interference: conditional norm, not a Born-rule derivation

**Supersedes the historical probability/quantum-completion claims — 7 October
2026.** See `gram-interference-and-bell-readout-comparison.md` for the complete
source and instrument comparison. Original bytes, including the rank-one and
continuum assertions, are preserved in
`quarantine/20261007-quantum-readout-evidence/gram-selection-principle.md`.

## Retained mathematical statement

For the declared complex record vectors, use the consistent convention
G_ij=v_i-dagger v_j. Then

\[
I(\theta)=q^\dagger Gq=\|Vq\|^2,\qquad q_i=e^{i\theta_i}.
\]

This is a quadratic coherent norm, equivalent to the corresponding amplitude
sum. It is not automatically a probability. The old checker recorded a factor-of-two
mismatch for every pair without asserting its expected values. The repaired
checker enforces the raw norm and separately calculates the balanced-port
probability with its preparation and effect factors.

## Interpretation boundary

A rank-one Gram admits a scalar amplitude factorization. That fact neither
selects a prepared quantum state nor derives the Born rule. Higher-rank density
matrices also obey that rule. The full five-filler construction now has an
explicit comparison with the existing conditional quantum instrument, retaining
both the encoded record vectors and the original filler actions.

The metric/encoding, coherent preparation, state-effect pairing, analyzers and
laboratory record assignment must not be silently identified. No continuum
aperture limit, path integral, physical probability law or measurement
interpretation is derived here. Further compatible Gram factorizations would
not resolve those independent interfaces.

## Verification

```text
uv run --with sympy python research/nima/checkers/check_gram_selection_principle.py
uv run --with sympy python research/nima/checkers/check_gram_bell_readout_comparison.py
```

New exact receipt: `results/gram-selection-principle-repaired.json`. The second
command additionally requires the source-bound legacy transport described in
the comparison packet. Neither command overwrites the historical receipt.
