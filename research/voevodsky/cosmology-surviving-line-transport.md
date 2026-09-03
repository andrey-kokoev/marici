# Surviving-line transport

## Result

For each of grades seven and eight, the normalized `x²` image functional recurs exactly from `A12→A14` to the `x²`-generated paths under `A14→A16`.

The functionals are not grade-independent. In normalized target-ID order:

- grade seven has seed vector `(1, -1/108, -1/9, 1/12)` and `y²`-path vector `(9/16, -1/192, -1/16, 3/64)`;
- grade eight has seed vector `(1, -1/9, 12, -4/3)` and `y²`-path vector `(9/16, -1/16, 27/4, -3/4)`.

Thus both grades collapse to a line under `x²`, and each grade's functional persists for the second tested step, but no common grade-independent functional exists in these coordinates.

## Claim boundary

The calculation covers two finite transport steps. It neither proves an all-even recurrence nor defines a sourced module presentation.

## Verification

- `research/voevodsky/check_cosmology_surviving_line_transport.py` — exit 0 after removing the falsified grade-independence assertion
- `research/voevodsky/results/cosmology_surviving_line_transport.json`
