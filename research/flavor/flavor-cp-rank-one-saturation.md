# CP rank-one saturation gate (WP389)

## Bounded question

Does CP symmetry derive the WP387 portal, or does the desired shell require an
additional coefficient saturation condition?

## General CP-invariant quadratic portal

Let $X=C$ and $Y=Dq$. Both are CP odd, so the most general real quadratic
CP-even portal is

\[
V_2=aX^2+\kappa XY+bY^2,
\qquad a>0,\quad b>0.
\]

Its Gram matrix and determinant are

\[
G=\begin{pmatrix}a&\kappa/2\\\kappa/2&b\end{pmatrix},
\qquad \det G=ab-\frac{\kappa^2}{4}.
\]

Square completion gives

\[
V_2=a\left(X+\frac{\kappa}{2a}Y\right)^2
+\left(b-\frac{\kappa^2}{4a}\right)Y^2.
\]

## Three coefficient classes

When $4ab>\kappa^2$, the portal is positive definite and its zero set is only
$X=Y=0$. When $4ab=\kappa^2$, it has rank one and acquires a nontrivial shell
with magnitude ratio

\[
\left|\frac{X}{Y}\right|=\sqrt{\frac ba}.
\]

When $4ab<\kappa^2$, the portal is unstable. The desired selector therefore
lives exactly on the boundary of the positive Gram cone. CP symmetry alone
does not enforce this codimension-one saturation or the ratio $b/a$.

## Sign correction

The two saturation signs factor as

\[
(\sqrt a X+\sqrt b Y)^2,
\qquad
(\sqrt a X-\sqrt b Y)^2.
\]

Before a carrier orientation is calibrated, $q\mapsto-q$ exchanges them.
Thus the sign criticized in the generic WP388 circuit is a presentation label
for the unlabelled CP carrier. After a branch-reference port is added, the
sign becomes a relational orientation observable in the stabilizer groupoid.

The magnitude condition $\kappa^2=4ab$ is not removable by relabelling. It is
the genuine source-selector gate.

## Disposition

WP389 corrects and sharpens the circuit obstruction. CP symmetry supplies the
parity typing and identifies the two terminal signs before branch calibration,
but it permits both generic positive-definite portals and rank-one portals.
It neither selects saturation nor predicts the shell ratio.

The smallest hostile pair is $a=b=1$ with $\kappa=0$ versus $\kappa=2$.
Both respect CP and nonnegativity; the first selects only the intersection,
while the second selects a line. The next gate is an independent source
principle forcing Gram rank one and fixing $b/a$.

Run `uv run --with sympy python
research/flavor/checkers/wp389_cp_rank_one_saturation.py` to regenerate the
result.
