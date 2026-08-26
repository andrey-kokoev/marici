# Interior-mixing coefficient authority (WP261)

## Smallest nontrivial selector

On a nondegenerate two-generation spectral orbit, normalize the commutator
invariant as

\[
x=\sin^2(2\theta),\qquad 0\leq x\leq1.
\]

The smallest polynomial action that can stabilize an interior mixing point is

\[
V(x)=-a x+b x^2,
\qquad a>0,\quad b>0.
\]

For \(0<a<2b\), its unique minimum on the mixing interval is

\[
x_* = \frac{a}{2b},
\qquad V''(x_*)=2b>0.
\]

Because \(x\) is built from traces of the Gram commutator and spectral gaps,
the action descends under the full weak-basis group. It genuinely selects a
proper point of this admitted mixing slice once its coefficients are fixed.

## Hostile coefficient pair

Descent and action grammar do not select the coefficient ratio. Two positive
packets give

\[
(a,b)=(1,1)\Rightarrow x_*=\frac12,
\qquad
(a,b)=(1,2)\Rightarrow x_*=\frac14.
\]

Both minima are strict and interior. The checker also realizes \(x=1/2\)
directly with exact two-generation Gram matrices at \(\theta=\pi/8\).
Therefore invariant geometry supplies a family of conditional selectors, not
a numerical selector. Fitting \(a/b\) from the observed mixing angle would
move the desired answer into the source action.

## Classification and gate

This is a weak-basis-descending conditional source-action selector on a
two-generation slice. It is not a presentation rigidifier. Its first
nonfaithful arrow is from the invariant action grammar to the numerical
coefficient ratio.

A progressive realization must independently derive \(a/b\), a dynamical
flavon substrate, kinetic normalization, finite relaxation and stabilization,
the three-generation completion, and the physical readout. Until those fields
exist, the construction demonstrates selector architecture but does not
predict flavor.

Run `uv run --with sympy python
research/flavor/checkers/wp261_interior_mixing_coefficient_authority.py` for
the exact stationary points, curvatures, matrix witness, and hostile
coefficient pair.
