# Stable tri-complex block template

## Issue-tree position

The single-family template failed. The next depth-first leaf tests whether all nonminimum expansions share a block support organized by source kind, relation constructor, pole level, and marked wall.

## Result

A stable support-level template exists. Every nonminimum representative contains the same 14 special blocks:

- special IBP at \(K\)-pole levels 0 and 1;
- special \(K\)-multiplication at pole levels 0 and 1;
- special marked-\(q\) multiplication at pole levels 0 and 1 for each of `g1`, `g2`, `g3`, `g23`, and `g31`.

One p-tangent block is also common to all four samples:

- p-tangent IBP at pole level 0.

Total occupied block counts vary:

| sample | occupied blocks |
|---|---:|
| lower quartile | 16 |
| median | 18 |
| upper quartile | 15 |
| maximum | 26 |

The maximum sample additionally activates special marked-\(q\) blocks at pole level 2 and a broader set of tangent corrections.

## Meaning

Template extraction does not fail completely. The reusable core is a 14-block special tri-complex coupling IBP, \(K\), and every marked wall at pole levels 0 and 1. The p-tangent correction is sample-dependent beyond a common `T:IBP:k0` block.

This is a support template, not a coefficient formula. It does not constrain monomial shifts or produce a uniform homotopy.

The next depth-first leaf is to factor the sample-dependent tangent correction against target pole level and marked-wall data. If no rule survives, this template branch should be marked support-only and the tree rescored toward second-prime source coefficients or the independent \(K\)-absorption mechanism.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_tricomplex_block_template.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_tricomplex_block_template.json`
