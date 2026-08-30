# Three-path exterior-purity gate

## Hostile question

Does the first three-alternative interface require a new \(\wedge^3\) Carrier
cell beyond its pairwise relational ports?

Let three normalized record states have Gram matrix

\[
G=
\begin{pmatrix}
1&a&b\\
\bar a&1&c\\
\bar b&\bar c&1
\end{pmatrix}.
\]

Its grade-three exterior weight is

\[
\boxed{
\det G
=1-|a|^2-|b|^2-|c|^2
+2\operatorname{Re}(ac\bar b).
}
\]

The final term is the real part of the gauge-invariant Bargmann product.

## Exact counterpair

Two strictly positive Gram packets with

\[
|a|=|b|=|c|=\frac13
\]

have identical pairwise distinguishabilities and identical total
\(\wedge^2\) weight, but different triple phases:

\[
(a,b,c)=\left(\frac13,\frac13,\frac13\right)
\]

versus

\[
(a,b,c)=\left(\frac13,\frac13,\frac i3\right).
\]

Their grade-three weights are respectively

\[
\frac{20}{27}
\qquad\text{and}\qquad
\frac23.
\]

Therefore pairwise magnitudes do not reconstruct the three-occurrence
interface.

## Correction

The triple port is nevertheless not independent when full oriented pairwise
coherences \((a,b,c)\) are retained.  The determinant formula derives it
exactly.  Hence the amplitude sector has the hierarchy

\[
\boxed{
\text{pairwise magnitudes}
<
\text{oriented pairwise coherences}
\Longrightarrow
\text{all rank-three exterior data}.
}
\]

The apparent higher cell is a coherence relation among pairwise ports, not a
new freely assignable coefficient.

## Three-slit implication

A quadratic Born screen readout contains populations and pairwise cross terms.
It has no independent cubic interference term.  The \(\wedge^3\) datum instead
appears as a consistency/positivity constraint on the complete pairwise
coherence packet.  This is compatible with vanishing third-order Sorkin
interference while retaining nontrivial three-state Bargmann geometry.

## Cross-sector falsifier

Benincasa's three-mode Gaussian test should now distinguish:

1. plain determinantal closure from its full oriented pair ports;
2. a symplectic/Pfaffian refinement forced by \(\Omega\);
3. a genuinely independent higher coefficient.

Only case 3 requires a new interface cell.  Case 2 supports shared
exterior-purity calculus with a sector-specific symplectic lens.

## Verification

```text
uv run --with sympy python research/nima/checkers/check_three_path_exterior_purity.py
```

