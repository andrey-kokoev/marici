# DPC: interface changes for a nonzero Bockstein

## Problem

Can source enlargement or an interface change turn the certified zero algebraic Bockstein into a nonzero class?

## Bold conjecture

Adjoining source generators can expose a nonzero class while retaining the same normal target and quotient rule.

## Named rivals

A basis change might alter the class; a linear comparison might send zero to a nonzero exceptional class; or only a non-monotone admissibility restriction, changed normal target, or changed extension can expose a class.

## Risky consequences and strongest falsification

The conjecture requires a previously exact derivative to leave the image after source generators are adjoined. This contradicts image monotonicity: if

\[
\operatorname{im}(d_1)\subseteq\operatorname{im}(d'_1)
\]

and `x` lies in the first image, it lies in the second. Invertible source reparametrization preserves the image. A well-defined linear comparison also sends the zero quotient class to zero. Exact finite models verify each inclusion and exhibit nonzero classes only after restricting the image or changing the target vector.

## Disposition

The conjecture is rejected. Mere source enlargement, basis change, or linear postcomparison cannot create the desired class. A nonzero class requires at least one sourced change from this disjunction:

- restrict admissible primitives through support or filtration;
- change the normal derivative or target;
- change the extension or quotient so the current primitive does not descend.

These conditions are not sufficient, and current artifacts construct none of them. The next test asks whether the existing pole filtration restricts the certified primitives enough to expose a filtered class.

## Verification

- `research/voevodsky/check_cosmology_nonzero_bockstein_interface_changes.py` — exit 0
- `research/voevodsky/results/cosmology_nonzero_bockstein_interface_changes.json`
