# Completion-B Yukawa Fiber Has One Cycle Phase and a Reducible Discriminant

## Exact determinant divisor

Keep the WP887 Clifford realization and the exact nonzero spinor-Higgs witness
(phi=(1,2,3,5)^T), but leave all six allowed Yukawa coefficients symbolic.
The full component determinant factors as

\[
\det\mathcal M_B=
85632148167696\,
y_1^4y_2^4y_3^2y_6^2
(y_1y_5-y_2y_4)^2.
\]

The rank-deficient divisor on this slice is therefore the union

\[
y_1y_2y_3y_6(y_1y_5-y_2y_4)=0.
\]

The last component is not visible from vertex coverage. It is a coherent
four-edge cancellation around the cycle

\[
S-V-X-n_1-S.
\]

## Field-rephasing quotient

With canonical kinetic terms, admitted field-coordinate changes are unitary
rephasings, not arbitrary complex rescalings. For fixed scalar-vacuum gauge,
the connected six-vertex, six-edge Yukawa graph has cycle rank one. Five
independent fermion rephasings remove five edge phases; the remaining phase is
carried by the cycle ratio

\[
\rho=\frac{y_1y_5}{y_2y_4}.
\]

Its phase is invariant under all six fermion rephasings. The magnitudes
(|y_i|) remain physical coordinates. The generic rephasing stabilizer is the
one-dimensional alternating phase on the bipartite graph.

Thus the nonzero-coupling quotient retains at least seven real coordinates:
six magnitudes and one cycle phase. Treating general nonunitary field
rescalings as gauge would falsely erase the physical magnitudes.

## Discriminant and hostile deformation

On the nonzero torus, the coherent discriminant is (ho=1). Its squared
factor in the determinant records an even determinant zero; it does not by
itself determine the monodromy of individual singular values.

More strongly, full-rank points have different scale-free spectra. Define

\[
K=\frac{\operatorname{tr}[(\mathcal M_B^\dagger\mathcal M_B)^2]}
{\operatorname{tr}[\mathcal M_B^\dagger\mathcal M_B]^2}.
\]

At the WP887 witness (y=(2,3,5,7,11,13)),

\[
K=\frac{63449}{368082}.
\]

Changing only (y_3:5\to6) preserves full rank but gives

\[
K=\frac{1603}{9680}.
\]

Therefore no universal normalized mass spectrum or source-forced mass ratio
follows from generic massability.

## Aspect classification

- Quotient: six magnitudes plus one cycle phase on the fixed-vacuum,
  nonzero-coupling slice.
- Generic stabilizer: one alternating fermion phase.
- Discriminant: four coordinate components plus the coherent cycle component.
- Monodromy: not yet authorized from the determinant alone; it requires
  tracking eigenprojectors or singular vectors around each component.
- Reference channels: premature until that monodromy calculation is done.

## Verdict

Completion B has a nontrivial source fiber even after field rephasing. Its
full-rank locus contains continuously inequivalent normalized spectra. The
mass constructor is operational but selector-free. The next bounded problem
is exact singular-projector continuation around the coherent component
(ho=1), not another fitted mass ratio.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp888_spin5_completion_b_yukawa_fiber_quotient.py
~~~
