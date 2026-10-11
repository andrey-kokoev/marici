# Iteration 2: typed Merkle expression and equality-proof input

## Delivered boundary

The new `merkle_identity_kernel.py` accepts external content-addressed proof stores for multivariable commutative polynomials over Q. Unlike the earlier fixed CRT and Cardano formulas, input terms and proof DAGs are supplied by the caller. The kernel supports arbitrary expressions in this declared grammar, within resource limits; it does not support arbitrary mathematical identities.

The grammar has type Q, declared variables, canonical rational constants, binary addition and multiplication, and unary negation. Powers are expressible by multiplication. Exact sparse polynomial normalization decides the `ring` rule universally for rational assignments, without numerical sampling. Rational coefficient arithmetic and polynomial normalization form part of the trusted implementation, not an external proof assistant.

## Proof rules and assumptions

| Rule | Checked obligation |
| --- | --- |
| `ring` | The two terms have equal exact polynomial normal forms |
| `refl` | Identical term references |
| `sym` | Reverse the exact endpoints of a checked premise |
| `trans` | Premise endpoints match exactly at the intermediate term |
| `congruence` | Same constructor applied to the paired endpoints of checked premises |
| `assumption` | Exact term pair is declared under that label in the current context |

Context, terms, proof nodes and final judgment are individually hashed. A judgment root binds its context and proof. Verification caches are local to one immutable-context kernel invocation; no cross-context cache reuse is performed.

Every derived judgment reports its actually used assumption labels. For example, x=y implies x*x=y*y by congruence, but this is explicitly conditional on x=y. The CLI option `--require-unconditional` refuses it as an unconditional theorem. Unused declared assumptions are not reported as proof dependencies. The kernel does not establish that a supplied assumption is true or that its context is consistent.

Unsupported constructors/rules, undeclared variables, incompatible types, unknown record fields, broken endpoint composition, noncanonical rational encodings, altered hashes and missing references fail verification. Division is unsupported: no implicit cancellation or nonzero side condition is invented. Analytic functions and quantified/dependent types are also unsupported. Basic object, nesting, polynomial-degree, term-count and CLI file-size limits exist; production hardening remains outstanding.

## Surface attachment bridge

The regression checker compiles each committed affine cube boundary into a Q-polynomial expression. Its witness proves the composed expression equals the input variable. The bridge checks the surface first, then all six independent kernel proofs, then exact correspondence of each proof's endpoints with its committed face boundary. It requires unconditional proofs.

A valid difference-of-squares theorem cannot replace a cube face proof: its endpoints are unrelated to that boundary and are rejected. Thus a valid theorem is not automatically a valid attachment witness.

This bridge is a prototype adapter in the regression checker, not a replacement of the surface edge-map grammar. General polynomial maps need not be invertible; arbitrary polynomial equalities cannot simply be installed as reversible edges. Extending typed map interfaces and inverse witnesses remains future work.

## Results

All 27 checks passed. Positive cases include difference of squares, three-variable distributivity, explicit symmetry/transitivity/reflexivity, conditional congruence, all six cube faces, JSON replay and fresh external CLI verification. Negative controls cover false equalities, assumption erasure, unrelated face witnesses, broken proof endpoints, unsupported operations and rules, undeclared variables, wrong types, noncanonical constants, extra fields, missing objects, hash tampering and excessive nesting. Conditional CLI verification succeeds only under the conditional policy.

The prior 19 torus checks and 14 surface checks are retained as regression suites; they remain distinct from this kernel's rule validation.

## Feed a new identity

From the repository root, a Python client can construct a store without manually computing hashes:

```python
import sys
sys.path.insert(0, 'research/voevodsky/checkers')
from merkle_identity_kernel import Builder, verify
b = Builder()
x, y = b.var('x'), b.var('y')
left = b.term('mul', x, b.term('add', x, y))
right = b.term('add', b.term('mul', x, x), b.term('mul', x, y))
p = b.proof('ring', left, right)
artifact = b.artifact(['x', 'y'], {}, p)
print(verify(artifact))
```

Serialize `artifact` as JSON and run:

```text
python research/voevodsky/checkers/merkle_identity_kernel.py FILE.json --require-unconditional
```

Reproduce the experiment:

```text
python research/voevodsky/checkers/check_merkle_identity_kernel.py
```

Artifacts:

- `research/voevodsky/results/merkle_identity_kernel.json`: test receipt and checker/kernel fingerprints.
- `research/voevodsky/results/merkle_polynomial_identity.json`: unconditional difference-of-squares proof store.
- `research/voevodsky/results/merkle_conditional_identity.json`: congruence proof with explicit hypothesis.
- `research/voevodsky/results/merkle_polynomial_surface_bridge.json`: original cube store and six attached expression proofs.

## Remaining work

This is progress on general input, not a universal proof language. Noncommutative operations, partial functions, quantified or dependent propositions, other coefficient domains, proof-producing search, gluing discovery, higher fillers and general witness transport remain open. A natural next bounded step is searching compatible face-boundary identifications while retaining these exact witness attachments.
