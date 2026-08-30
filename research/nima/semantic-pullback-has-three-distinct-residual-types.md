# Semantic pullback has three distinct residual types

## Claim

Let a claimed compiler be represented by a partial functor from source states and
constructors to observable records and their compositions. Pulling the target
claim backward can fail at three different categorical levels:

1. **Object separation:** two admitted source states have the same record. The
   residual is an observation port.
2. **Image admission:** a claimed target record is outside the image of the
   source map. The residual is a target-domain predicate.
3. **Composition coherence:** the required generator images exist, but their
   defining relations do not hold. The residual is a coherence cell or an
   explicit anomaly budget.

These repairs are not interchangeable. Adding an observation cannot admit an
impossible target record. Narrowing the target schema cannot distinguish two
source states already identified by the record. Supplying all generator images
does not make their composites functorial.

## Frozen finite witnesses

### Missing port

The first three observations of the four-state Jordan transport have rank three
and kernel spanned by the fourth basis vector. The next observation separates
that direction and raises the rank to four.

### Missing target-domain predicate

For a positive full-support real distribution, the mean and second moment obey

\[
\nu-\mu^2>0.
\]

The record \((\mu,\nu)=(1,1)\) is therefore outside the image. No additional
observer makes that record source-realizable; the executable target must be
restricted to the strict moment domain.

### Missing coherence

Let

\[
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

Both generators are present and invertible, but \(XZ=-ZX\). A compiler for the
commuting presentation therefore retains the central defect \(-I\). Neither an
extra state observer nor target narrowing removes this relation-level defect.

## Categorical reading

The three gates are, respectively:

- faithfulness on the admitted source distinction;
- essential surjectivity onto the declared executable target;
- preservation of composition and defining relations.

This is a diagnostic trichotomy, not a theorem that every failure has only one
component. A real system may fail several gates simultaneously. The obligation
is to type each residual at the earliest failed gate and apply a repair of the
same type.

## Finite falsifier

Any repair compiler that maps all three witnesses to the same action, such as
`add_port`, is rejected. The checker requires the three residual types and their
minimal repairs to remain pairwise distinct.

