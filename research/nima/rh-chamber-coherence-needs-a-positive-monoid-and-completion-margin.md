# RH chamber coherence needs a positive monoid and a completion margin

## Question

What lies beneath a proposed source-observer chamber law, and what prevents
finite chamber preservation from collapsing onto an incidence wall during
completion?

## Three distinct structures

Orientation, chamber transport, and completion stability are not equivalent.

### Orientation

An invertible transport may preserve ambient orientation while carrying a
source line into the observer's incidence divisor. The quarter-turn is the
minimal hostile: its determinant is positive, but a selected coordinate
coefficient vanishes.

### Positive-monoid reduction

A chamber law requires reducing the transport group to a source-derived
submonoid that preserves the ordered open cell. In a two-dimensional model,
strictly positive matrices with positive determinant preserve the positive
flag chamber, and their products remain in that chamber.

This is additional source structure. It cannot be inferred from unitarity,
invertibility, determinant sign, reciprocal symmetry, or scalar functional
equations.

### Completion margin

Finite transports may lie in an open chamber while converging to its wall. For
example, every power of

\[
D_q=\operatorname{diag}(q,1),
\qquad 0<q<1,
\]

has positive determinant and a nonzero selected first coefficient, but

\[
\det(D_q^n)=q^n\longrightarrow0,
\qquad
\langle e_1,D_q^ne_1\rangle=q^n\longrightarrow0.
\]

Thus finite chamber membership does not imply that restricted-product or
cutoff completion stays in the open chamber. A source-derived uniform margin,
proper completion topology, or closed extension retaining the relevant
incidence data is a separate requirement.

## Exact finite model

For rational (0<q<1), define

\[
M(q)=\frac12
\begin{pmatrix}
1+q&1-q\\
1-q&1+q
\end{pmatrix}.
\]

Every entry and the determinant are positive. Moreover,

\[
M(q_1)M(q_2)=M(q_1q_2).
\]

This gives a genuine chamber-preserving composition law. The checker contrasts
it with the quarter-turn and with the diagonal completion-collapse family.

## Refined RH DPC

The chamber route now has four gates:

1. **Flag incidence:** construct the ordered source and observer flags from
   labelled theta/Tate data.
2. **Monoid reduction:** prove each local and cutoff transport lies in a
   source-derived chamber-preserving monoid.
3. **Composition:** prove the reduction is stable under Euler, seam, and
   archimedean composition with the declared ordering.
4. **Completion margin:** prove the relevant generalized minors cannot tend to
   zero along an admissible completed packet.

The fourth gate is not automatically a uniform lower bound over all spectral
parameters. It is the exact continuity or properness statement needed for the
chosen source completion and the particular incidence minor.

## Presentation and carrier safeguards

- A divisor seen only in one elimination chart is not a chamber wall. Support
  must survive adapted-chart comparison.
- A rank-losing projection cannot become a full-state coherencer by later
  composition. If the mixed probe requires a larger carrier, that carrier must
  be constructed explicitly.
- Coordinate changes such as renormalization-scale choices are not independent
  physical contexts. A contextual chamber test needs executable source or
  observer differences.

## Claim boundary

This packet proves only the finite separation among orientation, positive
composition, and completion stability. It does not identify the theta/Tate
positive monoid or establish a completion margin. Defining the monoid by the
desired scalar nonvanishing would be circular.

## Disposition

The next-rung chamber proposal survives, but splits into a source-derived
positive-monoid theorem and an independent completion-margin theorem. Either
failure closes this route.

