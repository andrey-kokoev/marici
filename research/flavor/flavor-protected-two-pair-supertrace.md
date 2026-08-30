# Protected two-pair supertrace: WP669

## Frozen protected slice

For one WP668-protected channel, take equal pair masses and reciprocal real
off-diagonal triplet Yukawas. The six-by-six field-dependent Dirac mass is

\[
\mathcal M=
\begin{pmatrix}
M I&yJ_n\\
yJ_n&M I
\end{pmatrix}.
\]

Conjugating by the species parity while sending \(n\mapsto-n\) leaves
\(\mathcal M\) invariant. The exact Dirac supertrace is

\[
-4\operatorname{Tr}\mathcal M^4
=-24M^4-96M^2y^2|n|^2-16y^4|n|^4.
\]

The protected loop remains flip even and preserves the scalar operator
support. Its norm-quartic erosion is twice the one-pair conditional result of
WP664.

## Corrected protected bound

Let \(P_n,P_m\) sum \(y^4\), including multiplicities, over protected
two-pair frame channels. At the repaired benchmark,

\[
\frac{dD}{dt}=1136-64(P_n+P_m).
\]

The exact nonerosion condition on this slice is

\[
P_n+P_m\leq\frac{71}{4}.
\]

The literal WP651 frame-word census has two protected \(n\)-channels and two
protected \(m\)-channels. At unit Yukawas, \(P_n=P_m=2\) and the derivative
is 880.

## Disposition

Exact flip protection repairs kinetic support but strengthens fermionic
erosion. The full cone still leaks at every positive protected strength. This
bound is restricted to equal masses and reciprocal real vertices; unequal
masses, independent vertices, matching, thresholds, and running remain open.

The result constrains an admissible source region and selects no flavor point.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp669_protected_two_pair_supertrace.py

Generated result: results/wp669_protected_two_pair_supertrace.json.
