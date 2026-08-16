---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Integral A2 Eigensplitting and the Second Mod-Two Gluing

## Result

Entry 283 determines that the physical \(\ell_1\)-loop exchanges the two
square-root roots of the reduced cubic while fixing the analytic root.
Keeping the root ordering

\[
t_-,
\qquad
t_0,
\qquad
t_+,
\]

this is the outer transposition

\[
t_-\longleftrightarrow t_+,
\qquad
t_0\longmapsto t_0.
\]

On the integral \(A_2\) Milnor lattice, it is reflection in the highest
root. If \(\alpha,\beta\) are the simple vanishing roots joining
successive ordered roots, then

\[
\theta=\alpha+\beta
\]

is the outer-root vanishing cycle and

\[
T(\alpha)=-\beta,
\qquad
T(\beta)=-\alpha.
\]

Thus

\[
[T]_{(\alpha,\beta)}
=
\begin{pmatrix}
0&-1\\
-1&0
\end{pmatrix}.
\]

The eigenlines are

\[
L_+=\mathbb Z(\alpha-\beta),
\qquad
L_-=\mathbb Z(\alpha+\beta),
\]

but they do not split the integral \(A_2\) lattice:

\[
\boxed{
A_2/(L_+\oplus L_-)
\simeq
\mathbb Z/2.
}
\]

Over \(\mathbb Q\), the finite \((+1)\) target remaining from entry 283
is therefore a canonical rank-one algebraic Tate line. Integrally it is
glued to the reflection line by a forced mod-two class.

This is the same arithmetic pattern found independently in the
occurrence-resolved conductor quotient:

\[
\text{rational eigensplitting}
+
\text{integral half-sum defect}.
\]

It is coefficient-lattice structure over the existing signed-energy
normal, not evidence for a new carrier cell.

## Physical braid

The reduced frozen family has the form

\[
XY
=
\alpha_0 t^3+\beta_0\lambda t
+
O_{\rm wt}(4),
\qquad
\alpha_0\beta_0\neq0.
\]

Its roots satisfy

\[
t_0=O(\lambda),
\qquad
t_\pm
=
\pm\kappa\sqrt{\lambda}
+
O(\lambda)
\]

for a nonzero kinematic unit \(\kappa\). A loop around
\(\lambda=0\) exchanges \(t_+\) and \(t_-\), leaving \(t_0\)
fixed.

Because the exchanged roots are the outer pair in the chosen ordering,
the corresponding vanishing cycle is not a chosen simple root. It is the
highest root

\[
\theta=\alpha+\beta.
\]

Picard--Lefschetz reflection in \(\theta\), using

\[
(\alpha,\alpha)
=
(\beta,\beta)
=
2,
\qquad
(\alpha,\beta)=-1,
\]

gives

\[
s_\theta(\alpha)
=
\alpha-(\alpha,\theta)\theta
=
-\beta,
\]

\[
s_\theta(\beta)
=
\beta-(\beta,\theta)\theta
=
-\alpha.
\]

This fixes \(\eta=\alpha-\beta\) and negates
\(\theta=\alpha+\beta\).

## Orthogonal eigenlattices

The two eigenvectors satisfy

\[
(\eta,\theta)=0,
\]

and

\[
(\eta,\eta)=6,
\qquad
(\theta,\theta)=2.
\]

The change-of-basis matrix from \((\eta,\theta)\) to
\((\alpha,\beta)\) has determinant \(2\). Hence

\[
[L_{A_2}:L_+\oplus L_-]=2.
\]

Equivalently,

\[
\alpha
=
\frac{\eta+\theta}{2},
\qquad
\beta
=
\frac{-\eta+\theta}{2}.
\]

The rational projectors

\[
\pi_\pm=\frac{1\pm T}{2}
\]

are canonical, but they are not integral endomorphisms of the primitive
root lattice.

## Quadratic base change

Make the minimal cover

\[
\lambda=\mu^2.
\]

Then the three roots become analytic:

\[
t_0=O(\mu^2),
\qquad
t_\pm=\pm\kappa\mu+O(\mu^2).
\]

The order-two semisimple monodromy is killed. After simultaneous ADE
resolution, the finite vanishing lattice is represented by the algebraic
exceptional \(A_2\) chain. It is therefore Tate; the deck involution
retains the distinction between the invariant line \(L_+\) and the
anti-invariant Kummer line \(L_-\).

This is a standard simultaneous-resolution consequence, not a claim that
the entire marked relative extension splits after base change.

## Consequence for the surviving top extension

Entry 283 excludes any rational extension of the top conductor class into
\(L_-\). The only finite surface target is

\[
L_+\otimes\mathbb Q
=
\mathbb Q(\alpha-\beta).
\]

Therefore the unresolved finite part of the top column is at most one
scalar:

\[
N_{\rm rel}(g_{111})
\stackrel?=
c\,(\alpha-\beta),
\]

possibly together with the already separate elliptic unipotent target.

The present calculation does not determine \(c\). It does determine its
type:

- rationally, it is an extension between Tate objects;
- integrally, its normalization is constrained by the index-two
  eigensublattice;
- no transcendental or new carrier target remains in the finite
  \(A_2\) sector.

## Comparison with the conductor half-sum

Entry 280 found

\[
0
\to
\mathcal K_{\Delta_{W_1}}
\oplus
\mathcal K_{\Delta_{W_2}}
\to
H^1(W)
\to
\mathbb Z_{\rm top}
\to0
\]

with extension class \((1,1)\in(\mathbb Z/2)^2\), and a rational
invariant top lift requiring halves.

The \(A_2\) lattice now supplies an independent index-two phenomenon:

\[
0
\to
L_+\oplus L_-
\to
A_2
\to
\mathbb Z/2
\to0.
\]

The two mod-two classes must not yet be identified. The next calculation
must determine whether the marked specialization map relates them
canonically.

## Classification

| Datum | Classification |
|---|---|
| quadratic cover \(\lambda=\mu^2\) | resolved normal/Kummer coordinate |
| \(L_-\) | anti-invariant algebraic Kummer coefficient line |
| \(L_+\) | invariant algebraic Tate coefficient line |
| index-two defect | integral coefficient-lattice gluing |
| new carrier cell | none |

## Deutsch--Popperian conjecture M2.27

The specialization map of the frozen marked pair identifies the primitive
mod-two defect of the disappearing top conductor cycle with the
index-two defect of the \(A_2\) eigensplitting. After this identification,
the finite \((+1)\) extension is canonical and entirely algebraic; no
additional support or carrier datum is required.

The finite falsifier is integral. Compute the semistable specialization
map on primitive lattices. If the two parity classes disagree, they remain
independent coefficient extensions. If the map requires an additional
geometric component absent from the frozen pair, the shared-carrier
hypothesis fails.

## Next hostile test

After the base change \(\lambda=\mu^2\):

1. simultaneously resolve the \(A_2\) surface family;
2. take the strict transforms of the two frozen marked walls;
3. compute their incidence with the exceptional \(A_2\) chain;
4. evaluate the specialization of the primitive top graph cycle;
5. compare its parity class with
   \(A_2/(L_+\oplus L_-)\);
6. keep the elliptic unipotent block separate.

Only this primitive incidence calculation can decide whether the two
mod-two gluings are the same class.
