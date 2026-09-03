# Partial composition for the coherence-pyramid computad

## Question

Which compositions can be admitted from the typed signature without reintroducing the unrestricted pushouts, unidentified kernels, or completion failures already falsified?

## Claim boundary

This packet defines identity, sequential-composition, and reindexing constructors with executable admission predicates. Associativity, unitor naturality, interchange, Beck–Chevalley, and completion-composition coherence remain unproved.

## Identity constructors

Each variance class has its own typed identity:

- vertical identity preserves ports;
- under identity is the identity Green isometry;
- over identity has zero kernel and identity exactness;
- comparison identity preserves the quotient form domain.

Identity certificates erase only after type checking. A bare identity function does not certify the surrounding structure.

## Sequential composition

Vertical restrictions and under embeddings compose when the middle objects agree and their certificates compose.

Over quotients require more: the kernel of a composite surjection is generally larger than either input kernel. Composition therefore requires a new composite-kernel identification and exactness witness.

Closed-form comparisons require composable domain maps, radical descent, form isometry, and a strictly positive composite reduced minimum modulus. Positivity of each finite fixture does not substitute for this composite bound.

## Reindexing

Three partial constructors remain distinct:

1. under amalgamation requires the full joint cross pairing and joint positivity;
2. over pullback requires the fiber product, transported kernel, and pullback exactness;
3. completion transport requires common-core, closed-limit, radical, and coercivity transport.

Sequential composition is not silently identified with reindexing.

## Strongest falsification suite

The checker admits one fixture for each sequential and reindexing constructor, verifies left and right identity normalization on typed arrow tokens, and refuses six hostile mutations:

- middle-object mismatch;
- omitted composite kernel;
- pairwise-only amalgamation;
- pullback without exactness;
- collapsed comparison modulus;
- nontransportable completion certificate.

## Disposition

The composition leaf is resolved at the constructor level. The computad now has typed partial composition, but no category or double-category laws have been proved. The next leaf must construct associators, unitors, interchange, and Beck–Chevalley cells and test whether the admitted constructors close under those laws.

## Verification

- `research/voevodsky/coherence-pyramid-partial-composition.json`
- `research/voevodsky/checkers/check_coherence_pyramid_partial_composition.py`
- `research/voevodsky/results/coherence_pyramid_partial_composition.json`
