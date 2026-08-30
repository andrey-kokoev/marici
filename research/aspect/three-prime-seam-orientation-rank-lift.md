# Three-prime seam-orientation rank lift

## Source operation

The three arithmetic grade rows are symmetric across the positive and
reciprocal sectors. Conjugate-reciprocal sewing supplies a different parity:
the oriented seam row changes sign under sector exchange.

On the six sector-prime columns, the minimal seam row is

`(1,1,1,-1,-1,-1)`.

The first three entries refer to primes `2,3,5` in the positive sector and the
last three to their reciprocal partners.

## Exact result

The primitive, square, and connected-tail rows span a three-dimensional even
subspace. The seam row is odd under sector exchange and therefore independent.
It raises boundary rank from three to four without adding internal states. The
packet remains `30x30`.

This is precisely why conjugate reciprocity matters. A same-sign row

`(1,1,1,1,1,1)`

is even. Because the three prime-grade rows already span the full
three-dimensional prime coordinate space, that same-sign row lies inside the
arithmetic row space and adds no rank. Holomorphic duplication cannot replace
the oriented seam.

Sector aggregation annihilates the odd row. Intensity, absolute value, or a
sum over reciprocal partners therefore recreates the shared theta/optical
blindness.

## Architecture

The packet now contains four independently generated directions:

- the arithmetic three: primitive, square, connected tail;
- the oriented seam direction.

The remaining rank deficit is two: endpoint totalization and archimedean
countercurrent. The seam result fixes orientation and rank, not its completed
norm or its coupling to those two global objects.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_three_prime_seam_orientation_rank_lift.py
```
