# Lexicographic Morse matching for canonical attachments

## Question

Is there a uniform cell-level contraction rule for canonical relative attachments, replacing dimension-specific linear-algebra pivots?

## Claim boundary

A deterministic lexicographic matching is tested on exact relative face posets through dimension ten. If it pairs every cell and the reversed Hasse graph is acyclic, it gives a discrete Morse contraction with no critical cells in that range. An all-dimensional proof remains separate.

## Matching rule

Order relative cells first by degree, then by direction tuple, then by base natural. Process degrees upward. For each unmatched \(k\)-cell \(f\), choose the lexicographically least unmatched \((k+1)\)-cell \(c\) whose relative boundary contains \(f\) with coefficient \(\pm1\), and match \(f\leftrightarrow c\).

The number of required pairs between degrees \(k\) and \(k+1\) is

\[
\operatorname{rank}\bar d_{k+1}
=[x^k]A_{n-1}(x).
\]

If the algorithm exhausts every cell, these pair counts are forced by the attachment recurrence.

## Morse orientation

Orient every unmatched face relation downward from a cell to its face. Reverse each matched relation. A directed cycle would be a closed gradient path and would obstruct a cell-level contraction. If the directed Hasse graph is acyclic and no cells remain unmatched, Forman cancellation contracts the entire relative attachment.

This rule uses only cell labels and incidence. It does not inspect matrix ranks or select arbitrary rational combinations.

## Strongest falsification attempt

Construct canonical relative face posets in dimensions three through ten. Run the same matching rule without dimension-specific exceptions. Require complete pairing, pair counts equal to the boundary-rank vector, and acyclicity of the reversed Hasse graph. Retain the first unmatched cell or directed cycle if the rule fails.

## Computed result

The same rule completely pairs every relative cell in dimensions three through ten. Pair counts in each adjacent degree equal the predicted boundary-rank vector, and every reversed Hasse graph is acyclic. No dimension-specific exception, unmatched cell, or closed gradient path occurs.

## Disposition

The lexicographic matching supplies a uniform cell-level filler rule through dimension ten. Unlike the prior split-basis contraction, it uses only arithmetic cell labels and face incidence. The remaining obligation is an all-dimensional proof of matching completeness and gradient acyclicity.
