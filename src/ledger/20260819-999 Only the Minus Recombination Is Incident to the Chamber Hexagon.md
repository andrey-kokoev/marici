# 999 — Only the Minus Recombination Is Incident to the Chamber Hexagon

## Labelled incidence audit

Entry 998 shows that a normal Gysin shift does not by itself supply the support map from Entry 997's recombination costalk to Entry 979's chamber-edge cochain.  Before deriving coefficients, test whether the two recombination supports are even incident to the frozen chamber hexagon.

Entry 979 fixes the oriented occurrence cycle

\[
(0,1,4,5,3,2).
\]

The four source-wall blocks from Entries 974–975 are

\[
\begin{array}{c|c}
\text{wall}&\text{labelled occurrences}\\
\hline
(ZA_2)^2=1&\{0\}\\
(ZA_2B_{24})^2=1&\{1,2\}\\
(A_3/Z)^2=1&\{3\}\\
(A_3B_{34}/Z)^2=1&\{4,5\}.
\end{array}
\]

## Plus recombination

The \((++)\) collapse occurs at the intersection of occurrence blocks

\[
\{0\}\cap\{3\}.
\]

Occurrences 0 and 3 are not adjacent in the frozen cycle.  Hence this algebraic wall intersection is not a vertex of the chamber hexagon:

\[
\boxed{N^{\rm chamber}_{++}=0.}
\]

No chamber Cousin differential can send the \((++)\) modification into Entry 979's six-edge complex without enlarging the chamber carrier or supplying a different correspondence.

## Minus recombination

The \((--)\) collapse occurs between the repeated blocks

\[
\{1,2\}\quad\text{and}\quad\{4,5\}.
\]

Exactly one cross-block pair is adjacent in the oriented cycle:

\[
(1,4).
\]

Thus

\[
\boxed{N^{\rm chamber}_{--}=1.}
\]

This is the unique labelled realization of the repeated-wall recombination support in the frozen hexagon.  The other nearby adjacency \((3,2)\) uses the unshifted wall \((A_3/Z)^2=1\), not the repeated \((A_3B_{34}/Z)^2=1\) block, and therefore is not a \((--)\) recombination vertex.  The vertex \((1,4)\) is a legitimate domain for a local vertex-to-edge Cousin boundary.

## Result

\[
\boxed{
\text{the proposed comparison with Entry 979 splits by character: absent for }(++),
\text{ incidence-typed but coefficient-unfixed for }(--).
}
\]

This is a carrier-incidence statement only.  It neither identifies the \((--)\) modification with the exceptional edge class nor assigns a physical meaning to it.  The rational units and residue orientations at the two vertices remain to be derived from the source regularized intersection pairing.

## Next finite test

At the labelled vertex \((1,4)\), compute the two outgoing Pochhammer boundary maps in Entry 979's transported base frame.  Test whether the resulting two edge coefficients reproduce the corresponding restriction of the \((--)\)-character projection of the exceptional cochain.  The \((++)\) line must remain outside this hexagon comparison unless an independently derived carrier correspondence is found.

## Verification artifacts

- `research/benincasa/marici-gm/src/bin/string_six_point_recombination_hexagon_incidence.rs`
- `research/benincasa/string-six-point-recombination-hexagon-incidence.json`

The checker reconstructs adjacency directly from the frozen labelled occurrence cycle and verifies the counts zero and one.

Epistemic graph event: `ev-000000000617-46c1c0c2-15b4-4fbb-a1ba-6bf95877980d`.
