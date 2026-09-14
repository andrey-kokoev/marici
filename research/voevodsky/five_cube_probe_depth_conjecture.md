# Five-cube probe-depth conjecture

## Question

Does the canonical five-shell Boolean cube complete at grade 165165 and raise the required modulation depth from three settings to four?

## Claim boundary

This packet preregistered an exact sparse modular-rank test and now records its result. The predicted rank transition survives over two large prime fields, giving finite modular evidence. A characteristic-zero theorem and a general all-dimensional law require separate proofs.

## Predicted cube

Use shell ratios

\[
\frac32,\quad\frac53,\quad\frac75,\quad\frac{11}{7},\quad\frac{13}{11}
\]

on the base

\[
2310=2\cdot3\cdot5\cdot7\cdot11.
\]

The resulting Boolean five-cube has 32 vertices and 80 edges. Its top vertex is

\[
15015=3\cdot5\cdot7\cdot11\cdot13.
\]

The predicted final edge is

\[
12705\longrightarrow15015
\]

in shell \((11,13)\), admitted at

\[
165165=3\cdot5\cdot7\cdot11^2\cdot13.
\]

## Risky rank prediction

Compare the complete arithmetic graph at cutoffs 165164 and 165165. For each cutoff compute the rank of ordinary incidence stacked with the first one, two, three, and four generating-family settings

\[
\frac56,\quad\frac34,\quad\frac7{10},\quad\frac23
\]

over moduli \(1000000007\) and \(1000000009\).

The prediction is:

- at 165164, three settings have full edge rank;
- at 165165, three settings have deficiency one;
- at 165165, four settings restore full edge rank;
- both moduli agree;
- the final cube edge is present among the edges first admitted at 165165.

## Rivals

- an earlier unrelated graph relation already requires four settings;
- the grade introduces a rank change through another simultaneous edge;
- the five-cube completes while probe depth remains three;
- modular exceptional behavior produces inconsistent ranks;
- resource growth prevents an exact computation with the declared method.

If the main prediction survives, delete each edge admitted at grade 165165 and recompute the three-setting rank. Unique restoration after deleting \(12705\to15015\) localizes the transition to cube completion. Survival after deleting another edge assigns the mechanism to that rival or to a joint dependency.

## Method

Use a Rust sparse modular eliminator with exact rational settings represented by modular inverses. Add incidence row blocks incrementally so ranks after each setting share one elimination state. Record graph sizes, boundary rank, cycle dimension, cumulative deficiencies, elapsed time, cube vertices and edges, and the complete list of grade-165165 edges.

## Computed result

The Rust checker processed the complete graphs:

| cutoff | edges | vertices | cycle dimension | deficiencies after 1, 2, 3, 4 settings |
|---:|---:|---:|---:|---|
| 165164 | 49631 | 52049 | 9755 | 1438, 103, 0, 0 |
| 165165 | 49635 | 52050 | 9758 | 1440, 104, 1, 0 |

Both moduli give identical values. Four edges enter at grade 165165. Deleting the shell-2, shell-3, or shell-4 edge leaves the three-setting deficiency at one. Deleting only the cube-final shell-5 edge \(12705\to15015\) restores full three-setting rank.

## Disposition

The five-cube prediction survives exact modular computation and per-edge localization. The square--cube--four-cube pattern extends to cubical dimension five: completion raises the required modulated setting count from three to four. The remaining obligations are characteristic-zero proof and a general theorem relating adjacent-shell cubical dimension to character-evaluation depth.
