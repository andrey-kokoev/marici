# Upstream reference snapshots

Source: https://github.com/zoharno/chamon_decoder

Authors: Zohar Schwartzman-Nowik and Benjamin J. Brown.
Paper: *Generalizing the matching decoder for the Chamon code*, Quantum 9, 1775 (2025), https://doi.org/10.22331/q-2025-06-18-1775 .

Unmodified source snapshots inspected and retrieved during the construction search:

| File | Git blob SHA-1 |
|---|---|
| `chamdec_stabs_syndromes.py` | `194d9ad3b5b2a0ecc1a64cc99b044392024bcb6d` |
| `chamdec_conversions.py` | `840909bdf1c9b1e4f761c01a551fc6e3e6a81177` |

The local checker verifies these content identifiers before evaluating the selected functions. It does not import the full decoder or install its dependencies. The unchanged stabilizer-builder function is evaluated with a small two-dimensional zero-array adapter implementing its indexed assignment operations; coordinate conversion functions are evaluated unchanged. No other upstream routines are executed.

The builder is used as an independent support-matrix reference for noncollapsed covers. Signed Pauli multiplication and the period-two repeated-site control are implemented separately in the owner-local checker. These files are reference inputs, not changes to production grammar, solver or viewer.
