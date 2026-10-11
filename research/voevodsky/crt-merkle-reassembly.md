# Typed Merkle DAG for witness-preserving CRT reassembly

## Question and scope

Can the CRT reassembly experiment be content-addressed without dropping types, ordered dependencies, or witness attachments, while keeping identity distinct from mathematical equivalence?

The active obligation is attachment transport and fixed-domain route compatibility. The experiment uses the pure CRT grammar and all 225 environments from `crt-edge-reassembly.md`. It does not model effectful computations, arbitrary dependent proofs, geometric tetrahedral reconstruction, or authenticated publication.

## Representation

Objects use SHA-256 of a domain-separated canonical JSON record. The domain is `marici.typed-crt-merkle.v1` followed by a null byte; JSON uses sorted object keys, compact separators, UTF-8 and no NaN. Array order remains significant.

- Input records retain port name and type.
- Operation records retain constructor, parameter, result type and ordered input hashes.
- Witness records retain the fixed predicate, subject hash, input-port references and an exhaustive evaluation-table reference.
- A construction record retains its complete input/output interface and four witness references.
- An equivalence record names two construction hashes, the exact finite domain and the required verification method.

Witnesses reference term roots, while construction roots reference both terms and witnesses. This avoids a cyclic hash dependency. Shared identical pure terms have one stored object; local occurrence names and duplicated storage are not semantic data in this fixture. The original expansion layout remains in the source receipt rather than in the term-content hash.

## Results

| Representation | Unique operation nodes | Content root prefix |
| --- | ---: | --- |
| Expanded source after content addressing | 20 | `24787fe02b62` |
| Shared derivation | 20 | `24787fe02b62` |
| Algebraically normalized derivation | 16 | `ed061fee4790` |

Thus Merkle addressing deduplicates the original 54 operation occurrences automatically. Algebraic normalization is a separate step: it changes content identity. Four witness records remain attached to each construction. The valid combined store contains 44 objects, including shared inputs, operations, evaluation evidence, witnesses, construction roots and the equivalence certificate.

The separate certificate starts `a9b2e5205b48`. Its verifier checks both hashed closures, constructor typing, exact witness attachments, the complete 225-environment table, every CRT predicate, and equality of all four outputs across both constructions. Merely storing a certificate record or matching a hash is not treated as a proof. A JSON serialization round trip re-verifies from the saved object store.

## Falsification

All 17 checks passed:

- changing a coefficient while retaining its old hash is rejected by integrity checking;
- deleting a witness and honestly rehashing changes the root and fails interface validation;
- redirecting a witness to another well-typed output fails attachment validation;
- a fully rehashed wrong-coefficient graph passes neither the mathematical checks nor an alleged equivalence certificate;
- reversing ordered pair ports changes the content root and fails typing;
- renaming local operation IDs preserves content identity.

The result separates three obligations: content integrity, interface/attachment integrity, and mathematical correctness. It does not prove collision-freedom of SHA-256 or authenticate who supplied a root. Mathematical equivalence here is exhaustive extensional equivalence of the fixed CRT interface, not arbitrary equality of proof terms.

## Reproduction

Run in order:

1. `python research/voevodsky/checkers/check_crt_edge_reassembly.py`
2. `python research/voevodsky/checkers/check_crt_merkle_reassembly.py`

Both use only the Python standard library. The Merkle checker checks the producer hash recorded in the source receipt before using it.

Artifacts:

- `research/voevodsky/results/crt_merkle_reassembly.json`: checks, full root hashes and evidence fingerprints.
- `research/voevodsky/results/crt_merkle_store.json`: valid reachable objects and equivalence certificate. Deliberately invalid objects are excluded from this store.
- `research/voevodsky/checkers/check_crt_merkle_reassembly.py`: encoder and independently checking finite evaluator.

Next discriminating test: add a genuinely witness-dependent constructor, then test whether two equal output values with different attachment witnesses remain distinct. This fixture already binds witness references but does not establish arbitrary dependent-witness normalization.
