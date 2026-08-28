# Three-prime connected-tail rank lift

## Why the packet must grow

The first connected determinant grade is `k=3`. A depth-two valuation chain
cannot retain it. Moreover, three candidate grade rows evaluated on only two
primes have rank at most two. The `18x18` two-prime packet was therefore too
small in two independent senses.

The smallest test uses primes `2,3,5`, valuation depth three, both reciprocal
sectors, and six boundary coordinates:

`2 sectors * 3 primes * 4 states + 6 boundary states = 30 states`.

## Source rows

For Nima's concrete endpoint source `G(q)=exp(-q)`, grade `k` at prime `p`
has weight

`(1/k)(p^(-3k/2)-p^(-k/2))`.

The checker forms the exact `3x3` matrix with grades `1,2,3` as rows and
primes `2,3,5` as columns. Its determinant is nonzero. Thus the first
absolutely summable connected grade is independent of both the distributional
primitive grade and the Hilbert prime-square grade.

Boundary observation rank rises from two to three. Reciprocal-sector
duplication preserves rank three rather than manufacturing extra type rank.

## Minimality and hostiles

- two primes cannot witness a rank-three grade packet;
- depth two cannot retain grade three;
- copying the square row and renaming it connected tail leaves rank two;
- summing all three grades into one scalar returns rank one.

The required growth from 18 to 30 states is therefore source-forced, not
computational padding.

## Implication

The arithmetic three-stratum interior is now present at finite cutoff:
primitive, square, and connected tail. The remaining rank deficit is three,
carried by seam, endpoint totalization, and archimedean countercurrent.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_three_prime_connected_tail_rank_lift.py
```
