# Binary-cardinality groupoid audit (WP320)

## Candidate explanation

The proximity found in WP318 invites the claim

\[
64=2^6,
\]

perhaps from six binary source choices. WP320 tests whether this number
survives the source equivalence relation.

## Three distinct counts

Six labelled binary slots have 64 literal words. If slot permutations are
gauge, the complete invariant is Hamming weight and only seven physical orbits
remain. If global bit complement is also an admitted equivalence, only four
orbits remain.

These are different experiments:

- 64 requires six individually addressable labelled ports;
- 7 is the quotient count under unlabelled slot permutations;
- 4 is the further relational quotient under complement exchange.

Algebraic cardinality therefore cannot establish a physical charge of 64
until the labels and the map from state count to charge have source authority.
Adding label ports changes the groupoid; it does not reveal labels that were
absolute in the unlabelled experiment.

## Exact hostile pair

The words `000001` and `100000` are distinct literal matrices of bits but lie
in the same permutation orbit. They are the smallest concrete witness that a
literal count cannot silently become a quotient count.

Run `uv run python
research/flavor/checkers/wp320_binary_cardinality_groupoid.py` to regenerate
the exact audit.
