# Protocol migration has preservation and choice defects

## Setup

Let a richer protocol refine a source-state equivalence. Its behavioral quotients have a canonical downgrade map

\[
p:Q_{v+1}\longrightarrow Q_v.
\]

Migrating an operation requires more than drawing an arrow in the opposite direction.

## Preservation defect

Suppose the old operation comes from a concrete source-state transformer (T:S\to S). It induces an operation on the richer quotient exactly when it preserves the refined equivalence:

\[
x\sim_{v+1}y
\;\Longrightarrow\;
T(x)\sim_{v+1}T(y).
\]

The finite falsifier is a pair identified by the new protocol whose images are separated by it. The checker records every such pair. A nonempty witness set means the old implementation has no well-defined migration, even if it was perfectly valid on the coarse quotient.

## Choice defect

Suppose instead that only an abstract old operation (f_v:Q_v\to Q_v) survives. A lift is an operation (f_{v+1}) satisfying

\[
p f_{v+1}=f_v p.
\]

Such lifts may exist in abundance. In the minimal checker fixture, the old quotient has one class and the new quotient has two. The old identity admits all four functions on the two refined classes as compatible lifts. The commuting square proves compatibility but does not select behavior.

A source transformer that passes the preservation gate can select one lift. Without that transformer or another authorized migration constructor, choosing among the four lifts invents semantics.

## Migration theorem

A protocol upgrade is valid only when both obligations are discharged:

1. Every migrated concrete operation preserves the new behavioral equivalence.
2. Every abstract operation with multiple compatible lifts has a source-authorized selection rule or remains explicitly unresolved.

These are independent. Preservation can fail even when the coarse operation was lawful. Choice can remain ambiguous even when compatible lifts exist.

## Quantitative defect

For finite systems, record two quantities:

- the preservation defect: the set of refined-equivalent pairs whose images land in different refined classes;
- the choice defect: the number and typing of compatible lifts left after all supplied migration laws.

Zero preservation defect establishes descent. A choice count of one establishes uniqueness only relative to the admitted constraints. Neither scalar output agreement nor existence of some commuting square discharges both gates.

## Consequence for repairable complexity

New contexts reduce observational ambiguity by splitting old classes. The same split can invalidate old implementations and multiply possible replacements. This is the precise sense in which a system can become more coherent observationally while accumulating repair work operationally.
