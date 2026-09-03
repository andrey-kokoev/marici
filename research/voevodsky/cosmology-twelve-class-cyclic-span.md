# Distinguished cyclic-span kernel intersection

## Result

The joint span of the twelve filtered classes does intersect transport kernels.

- Grade six is injective for both axes through A16.
- At grades seven and eight, `y²` remains injective on the distinguished span.
- At grades seven and eight, `x²` has a two-dimensional restricted kernel at both `A12→A14` and `A14→A16`.

The total restricted kernel dimension across the twelve checks is eight.

Each class ray survives separately, but exact linear combinations are killed. At grades seven and eight the four A12 classes span dimension three; their `x²` images span dimension one. The same rank pattern recurs at A14.

## Consequence

The full twelve-class cyclic module is not torsion-free under `x²`. Any persistence theorem must isolate the grade-six sector, the `y²` direction, or a quotient of the grade-seven/eight span by the two-dimensional killed subspace.

## Claim boundary

The calculation is finite through A16 and uses algebraic pole-filtered quotient coordinates. It supplies no DNC or geometric interpretation.

## Verification

- `research/voevodsky/check_cosmology_twelve_class_cyclic_span.py` — exit 0
- `research/voevodsky/results/cosmology_twelve_class_cyclic_span.json`
