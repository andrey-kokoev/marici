# The retained history metric now constructs the adjoint incidence but not its Xi characteristic

## Earlier obstruction

The triangular theta-tail system retained a forward source incidence

\[
B:U\to H
\]

but no typed reverse arrow.  Reciprocal doubling preserved arrow direction and
therefore did not construct an adjoint completion.

## Metric adjoint now available

The retained half-density history graph fixes a Hilbert metric on \(H\), and
the seam coefficient topology fixes the metric on \(U\).  The exact incidence
columns satisfy the Hilbert--Schmidt bound

\[
\|B\|_2^2
=
\sum_p\frac{\|b_p\|^2}{\log p}<\infty.
\]

Consequently the metric adjoint is a bounded Hilbert--Schmidt map

\[
B^\dagger:H\to U,
\]

with coordinates

\[
(B^\dagger f)_p
=
\frac{\langle b_p,f\rangle}{\log p}.
\]

This is the source-typed reverse incidence requested by the earlier
adjointness audit.  It is not inferred from reciprocal reflection or from a
raw transpose.

## Completed paired operator

On the common graph domain one may therefore form

\[
\mathcal D^{\rm pair}(s)
=
\begin{pmatrix}
D_H(s)&-B(s)\\
B(s)^\dagger&D_U(s)
\end{pmatrix},
\]

where the off-diagonal block is skew-adjoint in the declared direct-sum
metric.  Primitive, square, and connected source coordinates remain separate
inside \(U\).

Thus the purely operator-theoretic gate “construct a reverse incidence” is
closed on the retained history/seam topology.

## What reciprocal sewing still does

Fourier--Poisson sewing must transport the pair by

\[
B_-(s)=W_HB_+(1-s)W_U^{-1},
\]

\[
B_-^\dagger(s)
=W_UB_+^\dagger(1-s)W_H^{-1}.
\]

This is now a covariance test for an existing adjoint, not a definition of the
adjoint.

## Spectral-characteristic obstruction

Adding \(B^\dagger\) changes the triangular controlled system into a
closed-loop system.  Its Schur characteristic contains

\[
D_U+B^\dagger D_H^{-1}B
\]

with the sign fixed by the block convention.  No existing theta identity
shows that the determinant section of this paired operator is \(E(s)\xi(s)\)
with \(E\) a unit.

For the rank-one forcing column, the new lower equation is precisely the
adjoint-history residual condition.  The natural Xi history does not satisfy
it automatically off the seam.

## Correct status change

Closed:

- existence and boundedness of the reverse incidence;
- exact source-metric adjoint formula;
- vector-level cancellation of the forcing cross term;
- reciprocal covariance target.

Open:

- Xi-divisor compatibility of the paired characteristic;
- divisor-to-state chain map;
- complement invertibility and multiplicity preservation;
- completed cutoff convergence of the full paired pencil.

## Disposition

The previous “missing adjoint incidence” wording is obsolete on the retained
history/seam carrier.  The remaining obstruction is not construction of
\(B^\dagger\); it is proving that the resulting paired closed-loop pencil has
the Xi divisor rather than an unrelated Schur divisor.  No RH conclusion is
authorized.
