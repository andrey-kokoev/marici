# Distinguished killed combinations

## Result

Exact bases are now available for each two-dimensional killed subspace at grades seven and eight.

At `A12→A14`, the same coefficient patterns occur in both grades: relative to the chosen surviving representative, killed directions use coefficients `1` with `1/9`, and `1` with `-1/12`.

At `A14→A16`, the recurring patterns are `1` with `-16/9` between the representative's `x²` and `y²` paths, and `1` with `16/81` between its `x²` path and the paired class's `y²` path.

For each grade and step, the distinguished source span has rank three, its `x²` image has rank one, and the listed two vectors are nonzero source combinations with zero transported image. Durable target IDs and path labels are recorded.

## Claim boundary

The target set is closed under exchanging exponent axes, but the second-tangent derivative is not swap-invariant. No symmetry identification between the `x²` kernels and injective `y²` maps is asserted. Results are finite algebraic pole-filtered coordinates only.

## Disposition

Derive the transport law of the one-dimensional surviving image and test whether its coefficients recur at the next ambient step.

## Verification

- `research/voevodsky/check_cosmology_distinguished_kernel_combinations.py` — exit 0
- `research/voevodsky/results/cosmology_distinguished_kernel_combinations.json`
