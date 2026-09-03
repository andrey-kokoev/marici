# Structural empty q family

## Derivation

A raw q row has the form

\[
e_{k,\ell,a}-q_i e_{k,\ell+e_i,a}.
\]

Parameter differentiation along `nx=(1,0,0)` kills the first term and gives

\[
-(\partial_x q_i)e_{k,\ell+e_i,a}.
\]

For the ordered family `(g1,g2,g3,g23,g31)`, the exact parameter derivatives are `(0,-1,0,-1,0)`. Thus q indices 0, 2, and 4 vanish identically, while indices 1 and 3 produce a one-column target. The identity is independent of evaluation point, pole, level, and exponent. Each index has 192 seed descriptors, yielding exactly the observed 576/384 partition.

The 576 empty certificates are therefore canonical structural zero words for the declared nx derivative, not evaluation accidents.

## Scope

This derives only the parameter derivative of raw q relation rows. It supplies no source differential, geometric support, DNC specialization, exceptional comparison, or horn consequence.

## Verification

- `research/voevodsky/check_cosmology_structural_empty_q_family.py` — exit 0 after correcting the initial confusion between polynomial-variable and parameter differentiation
- `research/voevodsky/results/cosmology_structural_empty_q_family.json`
