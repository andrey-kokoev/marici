# Sequential charge-predicate lower bound

Owner: `marici.Kitaev`

Status: exact exhaustive coding theorem; physical predicate compilers remain
open.

## Bounded question

Can an eight-state one-shot sector bus be replaced by a reusable qubit whose
three binary rounds mostly use the existing holonomy interface?

Three binary predicates are necessary because `2^2<8`, and sufficient at the
level of abstract labels.  But every one of the three predicates must be
charge-sensitive.

A holonomy-class-only bit is constant on each of the flux blocks of sizes

\[
3,\quad2,\quad3.
\]

It therefore partitions the labels by a union of whole blocks.  The possible
side sizes are

\[
0,2,3,5,6,8,
\]

never four.  Yet after fixing one coordinate of an injective three-bit code,
each binary side has only four available words.  Both sides must therefore
contain at most four labels, forcing a `4+4` partition.  Contradiction.

Consequently every coordinate of every bijection from the eight sectors to
`F2^3` splits at least one flux class.  Exhaustive enumeration confirms this
for all `8!=40320` labelings.

## Resource interpretation

Sequential reuse lowers the workspace dimension from eight to two and uses
three rounds, but it demands three separately charge-sensitive Boolean
predicate compilers.  Zero rounds can be implemented by a gauge-invariant
holonomy-only phase table.  This is a space/interface trade rather than a
free compression.

The theorem does not say that three charge-sensitive predicates cannot be
compiled.  It says that their charge content cannot be displaced into the
existing flux bus by relabeling the sectors.

## Verification and falsifiers

Run:

```text
python research/kitaev/checkers/check_s3_sequential_sector_predicate_minimum.py
```

The checker enumerates every three-bit labeling and verifies the class-union
counting obstruction.  Saved output:
`research/kitaev/results/s3-sequential-sector-predicate-minimum.json`.

Falsifiers are a class-union of size four, an injective two-bit labeling, or
any three-bit bijection with a coordinate constant on every flux class.

