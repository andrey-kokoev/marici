# Reflection-even completion makes the Fourier graph Lagrangian

Author: marici.Grothendieck

Date: 2026-08-26

Status: exact finite Green-form theorem

## The raw Fourier graph fails

For the standard boundary Green form

\[
\Omega((x,y),(x',y'))
=\langle y,x'\rangle-\langle x,y'\rangle,
\]

the graph of an operator \(A\) is isotropic exactly when \(A=A^*\).

The Fourier transform is unitary, but on the full source space

\[
F^2=R,
\]

where \(R\) is reflection. Therefore \(F^*=F^{-1}=RF\), and the full graph
of \(F\) is generally not isotropic.

This closes a tempting shortcut: normalized metaplectic uniqueness does not
by itself produce a self-adjoint boundary relation.

## Even completion repairs the Green form

The completed Riemann theta source is reflection-even. On the even sector,

\[
R=1,
\qquad
F^2=1,
\qquad
F^*=F.
\]

Hence the graph of the restricted Fourier transform is isotropic. Its
dimension is half that of the doubled boundary phase space, so it is
Lagrangian.

The odd sector behaves differently: there \(R=-1\), so

\[
F^2=-1.
\]

It retains a genuine quarter-turn and its raw graph is not a self-adjoint
boundary condition for this Green form.

## Explanation

Evenness is not merely a convenient symmetry of the scalar theta kernel. It
changes the operator type of Fourier transport:

- on the full carrier, Fourier is a metaplectic quarter-turn;
- on the completed even carrier, it is a self-adjoint reflection;
- only then does its graph become a Lagrangian boundary condition.

This is a source-derived bridge from modular completion to boundary
self-adjointness. It also clarifies the earlier ninety-degree intuition: the
quarter-turn survives in the discarded odd sector, while the physical even
completion folds it into an involution.

## Remaining infinite-dimensional gates

The finite theorem transfers only if:

1. the adelic Fourier transform preserves the completed even rigged space;
2. its restricted graph is closed in the chosen boundary topology;
3. the graph is maximal for the actual doubled Dirac Green form, including
   primitive, square, seam, and archimedean channels; and
4. its relative determinant is the completed theta transform up to a source
   unit.

The third gate is now narrower than arbitrary phase selection. One must audit
whether the actual Green form is the standard doubled form or contains typed
boundary corrections that change isotropy.

## Falsifier

The route fails at the first finite source cutoff where the completed even
Fourier relation leaves a nonzero typed Green residual. Scalar cancellation
after discarding the odd or seam channel is insufficient.

## Scope

The full-graph obstruction and even-sector Lagrangian theorem are exact in
the finite Fourier model. The completed adelic Green-form statement and
determinant bridge remain open.

## Verification

The checker verifies that the full Fourier graph has nonzero isotropy defect,
while the reflection-even restriction is a self-adjoint involution with a
maximal isotropic graph. It also isolates the odd quarter-turn sector.
