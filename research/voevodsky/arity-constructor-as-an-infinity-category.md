# The ordered arity constructor as an infinity-category

## Question

Construct one arity-indexed higher constructor and prove that it is an infinity-category rather than displaying only its first four dimensions.

## Construction

Let \(\mathbf A\) be the category whose objects are natural numbers and with one arrow

\[
m\longrightarrow n
\]

exactly when \(m\leq n\). Composition is supplied by transitivity, and the identity at \(n\) is supplied by reflexivity.

Define the constructor \(X\) as the nerve of \(\mathbf A\):

\[
X_n
=
\{(a_0,\ldots,a_n)\mid a_0\leq\cdots\leq a_n\}.
\]

It is defined for every natural number \(n\), not only through dimension three.

The face map deletes one entry:

\[
d_i(a_0,\ldots,a_n)
=
(a_0,\ldots,\widehat{a_i},\ldots,a_n).
\]

The degeneracy map repeats one entry:

\[
s_i(a_0,\ldots,a_n)
=
(a_0,\ldots,a_i,a_i,\ldots,a_n).
\]

Deletion and repetition satisfy the simplicial identities because deleting or repeating tuple positions in either prescribed order produces the same tuple.

## Infinity-category theorem

The nerve of every ordinary category is a quasicategory. Equivalently, every inner horn has a unique filler.

For this particular nerve, an inner horn records all faces of one nondecreasing tuple except one. The remaining faces determine the omitted entries and their order relations. Their union reconstructs one nondecreasing tuple, which is the unique filler.

Therefore \(X=N(\mathbf A)\) is an infinity-category.

## What was constructed

The levels have a single definition:

\[
X_0,X_1,X_2,\ldots
\]

with face maps, degeneracies, and fillers at every dimension. No rank reset or terminal dimension is used.

The first levels are:

- \(X_0\): arity positions;
- \(X_1\): ordered arity transitions;
- \(X_2\): composable pairs with their composite;
- \(X_3\): compatible triples of compositions;
- \(X_n\): chains of \(n\) composable arity transitions.

## Claim boundary

This construction gives a strict baseline. Its inner-horn fillers are unique because \(\mathbf A\) is an ordinary category. It does not retain independent planes between a direct conductor and a composite route. Adding such plane multiplicity requires replacing \(\mathbf A\) by a category enriched in spaces and taking its coherent nerve.

Thus the ordered arity constructor has now been made into an infinity-category, while the nontrivial plane-bearing coherence pyramid remains a separate extension problem.

## Verification

```text
python research/voevodsky/checkers/check_ordered_arity_nerve.py
```

The checker exhaustively verifies simplicial identities and unique inner-horn reconstruction through dimension five over the four-object cutoff. The unbounded theorem follows from the nerve construction, not from that finite computation.
