# 4106 — Every Labelled Pole Grade Is Saturated and All Lift Complexity Is Extension Data

## Question

For Entry 4104's filtration by

\[
C_4\times B_5,
\]

do the associated-grade relation matrices contain integral torsion?

## Exact reduction

For every primitive integral relation, retain only coefficients whose target
block equals the declared relation-domain block.

Every associated-grade row then has width at most one. Hence its Smith data are
coordinatewise: the invariant attached to a constrained coordinate is the gcd
of its diagonal coefficients.

## Result

Across the \(15496\) labelled coordinates:

\[
\begin{aligned}
13218&\text{ coordinates are constrained by a unit relation},\\
2278&\text{ coordinates are unconstrained on the associated grade},\\
0&\text{ coordinates carry a Smith invariant greater than }1.
\end{aligned}
\]

Thus every associated-grade image is saturated, and every associated-grade
quotient is free abelian.

## Narrow conclusion

The characteristic-zero obstruction is not local torsion inside a labelled
pole block. All remaining lift complexity lies in the \(543\) off-diagonal
extension incidences between blocks.

This sharply localizes the next computation. A full global Smith normal form is
unnecessary unless successive extensions create torsion that is absent from
the associated grade.

## Next finite falsifier

Attach the blocks in any linear extension of \(C_4\times B_5\). At each step:

1. adjoin the source-derived off-diagonal relation columns;
2. compute the relative saturation index;
3. verify independence from the chosen linear extension;
4. reduce the cumulative filtered quotient modulo
   \(31991,32003,32009\);
5. compare its persistence grades with \(20,6,27\) and emergence rank \(1353\).

The first relative index greater than one is the exact birthplace of integral
torsion. If every index is one, the barcode admits a free integral filtered
lift and the earlier CRT failure is entirely a basis-presentation effect.

## Artifacts

- research/benincasa/checkers/check_interaction_net_integral_source_presentation.py
- research/benincasa/results/interaction-net-integral-source-presentation.json
