# Sharp uniform two-monomial boundary cover

## Theorem

At ambient degree A, every cutoff-boundary exponent has total degree between A-6 and A-4. If neither exponent coordinate is at least 2, their sum is at most 2. Therefore both coordinates cannot be below 2 once A-6 is at least 3.

Hence the images of multiplication by the two axis-square monomials cover every boundary exponent for every integer A at least 9, and in particular every even A at least 10.

The threshold is sharp: at A=8, exponent `(1,1)` has boundary degree 2 and lies in neither image.

## Disposition

P5d3b2 and P5d3b are completed. The arbitrary-degree transition interface now consists of:

1. uniform source-constructor naturality under either square-monomial multiplication; and
2. a sharp two-image cover of every boundary from A=9 onward.

P5d3c becomes active. Since all exact K-target contractions at A12 are available, the next task is to formulate and verify the induction/colimit construction: unchanged descriptors retain old contractions, while square-monomial transport generates new exponent sectors; overlap choices agree in the quotient by exact source syzygies.

The cover theorem alone does not prove base contraction existence or produce a canonical source word.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_uniform_two_monomial_boundary_cover.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_uniform_two_monomial_boundary_cover.json`
