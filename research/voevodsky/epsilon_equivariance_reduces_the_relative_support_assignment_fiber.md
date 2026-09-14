# Epsilon equivariance reduces the relative-support assignment fiber

## Question

Do the audited conductor symmetries and the relative source's site-exchange symmetry constrain the eight signed assignments between the two obstruction vectors and the two active point strata?

## Claim boundary

This computes an equivariant assignment fiber. It does not prove that conductor epsilon swap is the geometric site exchange or supply the missing support map.

## Conductor orbit

In enhanced coordinates ordered by

\[
(\chi_\delta,\chi_\epsilon,\chi_{\epsilon\delta}),
\]

the epsilon flip is

\[
D_\epsilon=\operatorname{diag}(1,-1,-1).
\]

For

\[
q_1=(1,1,1)^T=\Phi_{++},
\qquad
q_2=(1,-1,-1)^T=\Phi_{-+},
\]

one has

\[
D_\epsilon q_1=q_2,
\qquad
D_\epsilon q_2=q_1.
\]

Thus the two added support vectors form one epsilon orbit. The delta flip instead sends them to the complementary ambient columns:

\[
D_\delta q_1=\Phi_{+-},
\qquad
D_\delta q_2=\Phi_{--}.
\]

The selected two-support completion therefore preserves one root-swap orbit but not the full four-point orbit.

## Relative orbit

The relative arrangement

\[
S_1=x_1+X_1+Y,
\quad
S_2=x_2+X_2+Y,
\quad
S_3=x_1+x_2+X_1+X_2
\]

has a site-exchange involution

\[
(x_1,X_1,S_1)\leftrightarrow(x_2,X_2,S_2),
\qquad S_3\mapsto S_3.
\]

It exchanges

\[
p_{23}\leftrightarrow p_{13}.
\]

Hence the two active relative point classes also form one two-element orbit.

## Equivariant assignment fiber

Before symmetry, assigning \((q_1,q_2)\) to \((\delta_{23},\delta_{13})\) permits two bijections and two independent signs, for eight signed bijections.

If the conductor epsilon flip is required to intertwine the relative site exchange without an additional sign character, the two assigned signs must agree. The equivariant fiber therefore contains

\[
2!\cdot2=4
\]

assignments: either bijection and one common orientation sign.

The source equations give both nonzero boundary coefficients with the same displayed minus sign. This is compatible with a common sign but cannot select it until the orientation conventions of the two complexes are compared.

## Obstruction to stronger identification

The delta flip moves the chosen conductor pair into the omitted pair \((\Phi_{+-},\Phi_{--})\), whereas the relative Stokes step retains only the two intersections incident to \(S_3\). This suggests that choosing the active relative boundary breaks one of the two root-swap symmetries. It also means full \((\mathbb Z/2)^2\)-equivariance cannot be asserted on the two-generator completion alone.

## Disposition

Equivariance reduces the formal assignment fiber from eight to four under the explicit hypothesis that epsilon swap models site exchange with trivial orientation character. The hypothesis and common sign remain unverified. A geometric support map must test them and explain the complementary delta orbit.
