# Algebraic formula synthesis: Wolfram benchmark

## Question

Can a search return a formula together with adequacy and minimality witnesses?
The operator requested automated extraction of Wolfram's formula as the test.
The intended type is implemented in `agda/AlgebraSynthesisSpecification.agda`:

\[
\sum_f \bigl(\mathsf{Adequate}(f)\times
\prod_g(\mathsf{cost}(g)<\mathsf{cost}(f)\to\mathsf{Adequate}(g)\to\bot)\bigr).
\]

Adequacy means both validity in every Boolean NAND algebra and reconstruction
of a Boolean structure, recovering the original operation, from a nonempty
set satisfying the identity. It is not truth on a fixed finite carrier.

## Claim boundary

The prototype recovers

\[
((a\mid b)\mid c)\mid\bigl(a\mid((a\mid c)\mid a)\bigr)=c.
\]

The generator enumerates syntax without the target formula, proof database,
or a formula seed. A separate backend recognizes a generated candidate for
which the existing quantified Agda adequacy proof applies. **This is bounded
rediscovery with proof reuse, not autonomous synthesis of that proof.** The
held-out reference occurs in `check_algebra_synthesis.py`, never in
`algebra_formula_search.py`.

Agda checks the emitted formula, canonical naming, cost six, and its adequacy
at every universe level. The proof backend consumes the existing
[Boolean/NAND equivalence](wolfram-nand-equivalence.md); it does not rerun the
historical automated theorem discovery.

In this original benchmark, the minimum is supported by an independently
replayed finite certificate, without a complete Agda Sigma inhabitant.
The [successor completion](algebra-synthesis-completion.md) now kernel-checks
exhaustive minimum coverage and constructs `Goal.Result`, still reusing the
existing adequacy proof. Fresh adequacy discovery remains open. The original
benchmark receipts below retain their original, narrower scope. Python and
JSON are tested, not extracted from the formal specification.

## Search contract

- One binary operation symbol, no constants or additional axioms; one identity
  with arbitrary terms on both sides.
- Variables are alpha-normalized by first occurrence across the entire identity.
  No fixed variable limit is imposed. No commutativity, side exchange, or
  Boolean truth-table quotient is applied to source syntax.
- Cost is the total number of operation occurrences. At cost n, the two sides
  have n+2 variable occurrences, so symbol length including equality is 2n+3.
- The run covers costs zero through six: **1,901,165 identities**. Cost-six
  ordinal **1,488,521**, zero-based, is the displayed formula.
- Formula/algebra syntax, the Boolean semantic goal, the cost measure, and the
  bound are declared inputs; they are not inferred from the general Marici
  constructor. This is a new search layer, not a verified extension of the
  existing Layer4 runtime.

For fixed n, there are C(n+1) binary-tree shapes for the equation pair and
B(n+2) restricted-growth variable patterns, where C and B are Catalan and
Bell numbers. The audit reconstructs identities by independent arithmetic
unranking rather than the generator's recursive construction. It checks
scalar semantics rather than the generator's bit-plane evaluator.

## Rejection certificate

All **125,105** cheaper identities are covered:

| Cost | Identities | False in Boolean NAND | Non-Boolean countermodel |
|---|---:|---:|---:|
| 0 | 2 | 1 | 1 |
| 1 | 10 | 10 | 0 |
| 2 | 75 | 72 | 3 |
| 3 | 728 | 718 | 10 |
| 4 | 8,526 | 8,258 | 268 |
| 5 | 115,764 | 114,760 | 1,004 |

Thus the audited minimum is **six operation occurrences**, or **15 symbols**,
in the declared single-identity grammar. It is not uniqueness or minimality
under another signature, multiple-axiom presentation, or cost measure.

The first filter rejects Boolean-invalid identities. A second supplies
explicit non-Boolean operation tables satisfying the candidate. The failure
witness names a necessary Boolean NAND law: commutativity, diagonal
involution, absorption, or independence of the constructed top. These laws
are proved for arbitrary Boolean structures in the Agda specification.
Finite-model survival never supplies adequacy.

The size-two/three search left 32 cheaper obligations. With the initial
three-law rejection filter, exhausting the 65,536 four-element lifts of a fixed
two-element NAND quotient did not resolve them.
A bounded SymPy SAT search found this different four-element operation:

| Operation | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|
| 0 | 1 | 2 | 2 | 1 |
| 1 | 3 | 0 | 0 | 3 |
| 2 | 1 | 2 | 2 | 1 |
| 3 | 3 | 0 | 0 | 3 |

It satisfies all 32 identities but is not commutative: 0 operated with 1 is 2,
whereas 1 operated with 0 is 3. The runtime checks all valuations. Generated
Agda case proofs independently verify all 32 refutations, their canonical
syntax, and their costs, using a lifted four-element set at arbitrary universe
level. **The carrier is a four-element set, not the four-element Boolean
algebra with its usual operation.** An exhaustive check of all 16 maps to Bool
finds no NAND homomorphism, explaining the quotient-lift family's limitation.

The SAT solver is untrusted: only decoded tables passing replay are accepted.
Its search family fixes operation(0,0)=1 and requests a necessary-law violation.
An unsatisfiable family or an exhausted budget leaves the obligation open.
The admitted backend is SymPy 1.14.0; a Z3 invocation was policy-refused.

At cost six, the generator reuses the lower-cost countermodel bank rather than
conducting a complete model search. Its 668 surviving candidates are **not**
668 proved axiomatizations. The positive backend currently handles the known
Wolfram adequacy certificate; it does not prove arbitrary surviving candidates.

## Verification and reproduction

Run from the repository root:

```text
python research/nima/checkers/algebra_formula_search.py --max-cost 6 --output research/nima/results/algebra-formula-search.json
uv run --with sympy python research/nima/checkers/algebra_finite_sat.py research/nima/results/algebra-formula-search.json research/nima/results/algebra-finite-sat.json --size 4 --seconds 15 --limit 32
python research/nima/checkers/check_algebra_synthesis.py --emit
pwsh -NoProfile -File research/nima/checkers/check_graded_boundary_coherence.ps1 -Module DiscoveredWolframFormula -ReceiptStem algebra-synthesis -NegativeModules SynthesisBadFormula,SynthesisBadNormalization,SynthesisBadCountermodel
python research/nima/checkers/check_algebra_synthesis.py
python research/aspect/scc/scc.py check nima-algebra-synthesis
```

Invoke these as separate admitted commands in the harness. An optional nested
PowerShell driver was discarded when uv failed under its reduced child
environment; it is not part of the verified pipeline. The compiler command
uses the repository's installed Agda/Cubical toolchain.
The final audit replays every cheaper identity, verifies source-bound formal
receipts, and runs 18 tests. Tests include independent unranking, scalar versus
bit-plane evaluation, source-distinction retention, malformed/forged models,
missing/duplicate rejections, omitted supplementary obligations, and refusal
to turn budget exhaustion into a refutation. Three compiler controls reject a
mutated formula, noncanonical naming, and falsely asserted countermodel
commutativity.

Artifacts:
- `agda/AlgebraSynthesisSpecification.agda`: generic Sigma interface, concrete
  grammar/adequacy predicate, necessary laws, and an inhabited minimal toy case.
- `agda/DiscoveredWolframFormula.agda`: actual emitted candidate and checked
  reused adequacy witness.
- `agda/GeneratedLowerRefutations.agda`: 32 checked supplementary refutations.
- `results/algebra-formula-search.json`: candidate coordinates and base witnesses.
- `results/algebra-finite-sat.json`: supplementary concrete countermodels.
- `results/algebra-synthesis-formal-audit.json`: fresh compiler closure/controls.
- `results/algebra-synthesis-audit.json`: independent coverage/replay, hashes,
  test count, and separate runtime/kernel completion flags.

## Disposition

The benchmark formula is recovered and its adequacy checked; its declared
minimum has an exhaustive replayed certificate. The governing request for a
fully constructed Agda Sigma witness remains partial, rather than being
weakened to finite truth-table validity.

Named rivals were seeded-answer generation, an incomplete enumeration missing
a shorter identity, and finite-model survival mistaken for adequacy. Target-free
generation, independent unranking, explicit countermodels and omission/tampering
controls address those rivals at the tested-runtime boundary. Positive proof
reuse remains disclosed rather than counted as new proof discovery.

The remaining constructors are a checked enumeration/coverage and reflection
bridge, a general adequacy proof-search backend, and a runtime refinement to
the formal source calculus. No compression, performance, Bend2 implementation,
or physical interpretation follows from this benchmark. Work is uncommitted.
