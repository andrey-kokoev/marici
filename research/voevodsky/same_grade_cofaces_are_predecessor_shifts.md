# Same-grade cofaces are predecessor shifts

## Question

What exact arithmetic relation generates the same-grade positive-dimensional pairs used by the successful bounded Morse constructor?

## Claim boundary

The theorem concerns distinct-shell cells under the Carrier max-shell grade. It characterizes individual same-grade cofaces. It does not by itself prove that simultaneous choices form a complete acyclic matching.

## Theorem

Let \(c=[D;I]\), let \(m=\max I\), and let \(j\notin I\). A coface in new direction \(j\) having \(c\) as its upper \(j\)-face must be

\[
C_j(c)=
\left[\frac{Dp_j}{p_{j+1}};I\cup\{j\}\right].
\]

It exists integrally exactly when \(p_{j+1}\mid D\). Its grade equals the grade of \(c\) exactly when \(j<m\).

Indeed, for \(j<m\), the maximal shell remains \(m\), and cancellation in the grade formula gives

\[
g(C_j(c))=g(c).
\]

If \(j>m\), the maximal-shell factor changes, and strict prime growth prevents equality. Lower cofaces cannot have the same grade. Therefore all same-grade cofaces are precisely predecessor shifts: replace one available factor \(p_{j+1}\) in the base by \(p_j\), then add direction \(j\), with \(j<\max I\).

## Consequence

Same-grade filling is not accidental. A cell can be lifted without changing grade whenever its base contains an unused successor prime below its maximal active shell. The global matching problem is therefore a conflict-resolution problem among finitely many predecessor shifts.

## Strongest falsification attempt

Across multiplicative degrees two through five and all cells through grade 20000, enumerate every actual coface. Require equivalence between same-grade upper cofaces and the predecessor-shift criterion, and require every same-grade lower coface claim to be absent. Record cells with multiple eligible predecessor shifts as critical branchings for the confluence proof.

## Computed result

The criterion is exact for every cell in multiplicative degrees two through five through grade 20000: there are no missed or spurious same-grade upper cofaces and no same-grade lower cofaces. The numbers of predecessor-shift incidences are 73, 422, 502, and 341.

Branching begins in degree three. There are 35 cells with two eligible shifts; degrees four and five contain 56 and 37 branching cells, with maximum branching three. The first branch is \([75;\{3\}]\) at grade 525, which admits both directions 1 and 2.

## Disposition

The individual-coface theorem is proved algebraically and survives exhaustive transport checks. Global synchronization is now reduced to confluence of competing predecessor shifts. Degree two has no branching, explaining its immediate forest structure; higher degrees require cubes and higher cells to resolve branch choices coherently.
