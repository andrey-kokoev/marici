# Multi-cell Bezout gate

## Theorem

For sourced face cells with attaching degrees `m1,...,mk` onto the primitive triangle cycle, the chain map is

`Z^k -> Z`,

with row `(m1,...,mk)`. Its cokernel is `Z/gZ`, where `g=gcd(m1,...,mk)`. The primitive obstruction is killed integrally exactly when the attaching degrees generate the unit ideal.

A Bezout filler word is generally nonunique. Two coefficient vectors producing one differ by the kernel of the attachment row; the filler class modulo that kernel is canonical.

## Correction

The single-cell packet stated too strongly that an admissible enlargement must contain an individual unit-degree face. An individual unit is sufficient, not necessary. Several nonunit sourced faces can kill the class jointly: degrees two and three admit the Bezout word `-1,1`. Degrees two and four leave `Z/2`.

This correction does not authorize fitted integers. Every face, degree, orientation, and carrier map must be independently source-derived.

## Next gate

Inventory all currently sourced candidate face cells and their integral attachment degrees. If their generated ideal is not the unit ideal—or if no carrier chain maps exist—the horn remains unfilled.

## Verification

- `research/voevodsky/check_cosmology_multi_cell_Bezout_gate.py`
- `research/voevodsky/results/cosmology_multi_cell_Bezout_gate.json`
