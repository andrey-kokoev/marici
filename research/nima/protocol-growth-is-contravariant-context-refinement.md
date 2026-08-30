# Protocol growth is contravariant context refinement

## Result

Suppose protocol version (v) observes a source through an authorized context family (C_v), and version (v+1) adds contexts without deleting old ones. Behavioral equivalence can only become finer:

\[
x\sim_{v+1}y \;\Longrightarrow\; x\sim_v y.
\]

Therefore there is a canonical surjection from the richer behavioral quotient to the poorer one:

\[
S/{\sim_{v+1}}\longrightarrow S/{\sim_v}.
\]

The arrow points from protocol (v+1) to protocol (v). It forgets the newly observable distinctions.

There is generally no canonical arrow in the upgrade direction. An old equivalence class may split into several new classes, and choosing one representative branch requires additional constructor data. Protocol upgrade is therefore a refinement span or extension problem, not merely a functor that relabels old values.

## Exact finite model

The checker uses 32 source states labelled by five bits. Version (v) exposes the first (v) independent context bits. The number of behavioral classes is

\[
1,2,4,8,16,32.
\]

At each strict upgrade every old class splits in two. The downgrade map is unique. A forward section has one binary choice for every old class, so the number of possible sections grows as

\[
2^{|S/{\sim_v}|}.
\]

None is selected by the quotient data itself.

## Incoherence accounting

For a fixed finite carrier, let ambiguity be the number of state pairs still identified by the current protocol. Let distinction be the number already separated. Context enrichment monotonically decreases ambiguity and increases distinction, while their sum remains the fixed number of state pairs.

This resolves the apparent paradox that relationships can grow while incoherence falls. The new relationships are separating witnesses. They reduce average ambiguity even though the explicit relational structure becomes larger. Exponential growth occurs when independent binary contexts keep exposing independent source coordinates; redundant contexts add syntax without changing the behavioral partition.

## Interpretation

A protocol version is not an irreducible numerical distance from source data. It is a stage in a filtration of authorized observational power. Its meaningful distance from the source is the unresolved behavioral kernel, not the version number.

Moving from (v) to (v+1) requires:

- the newly authorized context;
- evidence that old observations remain valid;
- a refinement relation between old and new behavioral classes;
- migration data for operations that previously acted on an unsplit class.

This is why upgrades can accumulate their own incoherence. The new context removes observational ambiguity but creates migration obligations wherever old operations were defined only on coarser classes.
