# P-normal marked-wall support decomposition

## Result

The 10,080 nonzero marked-\(q\) derivative rows per normal direction are explained exactly by which labelled walls move.

At `(3,6,-3)`:

- along `nx=(1,0,0)`, only `g2` and `g23` vary;
- along `ny=(0,1,0)`, only `g1` and `g31` vary;
- along the p-tangent `nx-ny`, all four of `g1,g2,g23,g31` vary;
- `g3` is fixed along all three directions because it depends only on `z` here.

For ambient degree 14, each active mark contributes

\[
3\cdot16\cdot105=5040
\]

rows, from three \(K\)-pole levels, sixteen choices of the other mark levels, and 105 monomials of degree at most 13. Hence each unit normal has exactly

\[
2\cdot5040=10080
\]

nonzero marked-\(q\) derivative rows, exactly matching the two-prime complexity census.

## Meaning

The 15,120 zero marked-\(q\) rows per normal are structurally inactive walls, not failed computations. The remaining 10,080 rows arise from exactly two moving marks and still require genuine reduction into `S+T`.

This gives an algebraic explanation for the marked-wall support count. It does not yet explain why the active rows reduce to zero, nor why the IBP and \(K\)-multiplication families are absorbed.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_marked_q_support.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_marked_q_support.json`
