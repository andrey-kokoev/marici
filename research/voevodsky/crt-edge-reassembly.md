# CRT edge decomposition and witness-preserving reassembly

## Question

The operator proposed expanding nested tetrahedral packages, decomposing them into individual edges, and reassembling a minimal construction. This experiment tests the algebraic part on CRT modulo 3 and 5: can a typed constructor graph be decomposed and rebuilt with fewer nodes without losing any endpoint or witness condition?

The active SCC obligation is route/coherencer compatibility. The input stratum is exactly a in Z/3, b in Z/5, x in Z/15: 225 environments. Ports, arithmetic codomains, and the four witness predicates remain fixed. This is not a geometric tetrahedral decomposition.

## Frozen constructor language and source

Input ports a, b, x are free. Each canonical lift Z/3 -> Z/15 or Z/5 -> Z/15, scalar multiplication modulo 15, modular addition, reduction modulo 3 or 5, and ordered pairing costs one constructor node. No lookup table or primitive CRT operator is allowed. A constructor with multiple inputs is represented by an ordered typed hyperedge, not by unlabelled geometric adjacency.

The deliberately expanded forward expression is

\[
F(a,b)=(5a+5a)+(3b+3b)\pmod{15}.
\]

Each occurrence includes its typed lift. The four output roots are F(a,b), G(x), G(F(a,b)), and F(G(x)), where G(x)=(x mod 3,x mod 5). The whole starting graph repeats expressions independently at each root.

Four retained witness constraints require the two assembled residues to equal a and b, the pair round trip to equal (a,b), and the residue round trip to equal x. They are independently checked predicates, not discarded arithmetic nodes. Their count is reported separately from constructor cost.

## Construction and rivals

1. Serialize every operation with its output type, ordered input references, coefficient, and output port. Retain the root and witness tables.
2. Decode this edge representation, checking types and dependencies. The reconstructed term forest must equal the source forest structurally.
3. Hash-cons equal typed subterms into a shared DAG.
4. Collect modular coefficients in arithmetic expressions, treating typed lifts and other non-arithmetic operations as atoms; share the normalized terms again.

The governing conjecture is that this typed decomposition preserves the entire specified behavior while allowing constructor reuse. Its rivals are bare-edge reconstruction that loses attachments, type-blind sharing, and value-only simplification that passes one example but violates another route.

## Exact result

| Stage | Entire four-root derivation | Forward map alone | Witness constraints |
| --- | ---: | ---: | ---: |
| Expanded, unshared | 54 | 11 | 4 |
| Reassembled with sharing | 20 | 7 | 4 |
| Coefficient-normalized and shared | 16 | 5 | 4 |

The forward normal form is

\[
F(a,b)=10a+6b\pmod{15}.
\]

All four output roots agree across all three representations in every one of the 225 environments. Every retained witness holds. The exact source graph, shared graph, normalized graph and their attachment tables are in the result JSON.

## Bounded minimality

The five-node forward realization uses two typed lifts, two scalar multiplications, and one addition. Exhaustive testing of all 225 coefficient pairs modulo 15 yields the unique admissible pair (10,6).

In the forward affine subgrammar of typed lifts, scalar multiplication, and addition, both lifts are necessary. With at most four nodes, at most two arithmetic operations remain. A result depending on both inputs can then have coefficients only of the forms (k,1), (1,k), or (k,k); these also include the two-addition cases (2,1), (1,2), and (2,2). None is (10,6) modulo 15. Hence five nodes is minimal in this subgrammar.

No global minimum is established for the 16-node four-root derivation, for an expanded grammar with reductions or branching inside F, or for a presentation admitting CRT as one primitive. The artificial duplication of the starting expression makes this an explicit normalization test, not an implementation benchmark.

## Falsification and disposition

- Deleting a witness constraint is rejected during decoding.
- Feeding the Z/5 input into a Z/3 lift is rejected as a typed-port mismatch.
- Changing coefficient 6 to 5 remains well typed but fails the retained witnesses: on (a,b,x)=(2,3,8), assembly gives 5, the pair round trip gives (2,0), and the residue round trip gives 5.

All nine checks passed. Thus edge-level reassembly succeeds when operation arity, types, root identities, and higher correctness constraints remain attached. This result does not show that naked edges determine fillers, instantiate all the tetrahedral construction rules in type theory, or establish a 2-Segal identification.

## Reproduction

Run `python research/voevodsky/checkers/check_crt_edge_reassembly.py` from the repository root; only the Python standard library is required.

- Checker: `research/voevodsky/checkers/check_crt_edge_reassembly.py`.
- Receipt and full derivation graphs: `research/voevodsky/results/crt_edge_reassembly.json`.
- Algebraic source: ledger 4310, `src/ledger/20261007-4310 Cardano and Chinese Remainders as Witnessed Assembly.md`.
- Next discriminating extension: introduce a nontrivial attachment-dependent constructor and test whether normalization retains its witness dependency rather than merely its evaluated output. This experiment settles only the fixed CRT grammar above.
