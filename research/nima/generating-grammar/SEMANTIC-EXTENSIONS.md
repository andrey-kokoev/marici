# Computational grammar extensions

Generated from `semantic-extensions.json`. These are source-defined computational operations, not extra native rule tags.

## Retained-path grammar

A finite nonempty registry of distinct primitive IDs with source/target fields, exact rational arithmetic, sortable path records, and one identity-owning ledger. Optional descriptors must pass the source validation equations.

```text
Stage ::= Root(registry) | Successor(Stage), provided every parent word has an endpoint-compatible primitive extension
Weighted ::= SuppliedStage(Stage,coefficients) | SuppliedPaths(words,coefficients) | Compose(Weighted,Weighted)
Indexed ::= Index(Stage,source) | Index(Stage,target)
Mode ::= Inherit(Stage,registered_descriptor_name)
Observation ::= one of the declared readout/guard operations below, applied to records owned by the same ledger
```

Each successful constructor registers immutable data and returns a same-ledger object of its declared class. Compose may return an empty weighted family; externally supplied path families must be nonempty. Recursive assembly histories preserve the actual operands and cut, not merely a factorization of the final coefficients.

| Operation | Source definitions | Kind | Signature | Rule / restriction |
|---|---|---|---|---|
| path.linear_constants | identity, zero | support | n -> rational n-by-n matrix | Construct Kronecker identity or zero matrix. Requires: Nonnegative dimension |
| path.apply | apply | readout | matrix,vector -> vector | Exact rowwise matrix-vector multiplication. Requires: Nonempty matrix and matching coefficient dimension |
| path.coefficients | coefficients | guard | values,size -> rational vector | Validate dimension and integer/Fraction entries, then coerce exactly. Requires: Integers or exact fractions, not floats |
| path.length | PathStage.word_length | readout | Stage -> Nat | Read the common retained word length. Requires: Registered nonempty homogeneous stage |
| path.initialize | RetainedSuccessorLedger.__init__ | constructor | registry,optional descriptors -> Ledger | Create root primitive words, identity lifts/decoders and incidence continuation; validate optional spectral data. Requires: Nonempty unique primitive registry; supplied descriptors if used |
| path.root | RetainedSuccessorLedger.root | readout | Ledger -> Stage | Return the registered root by identity. Requires: Initialized ledger |
| path.register_stage | RetainedSuccessorLedger._register_stage | support | typed stage fields -> Stage | Allocate a ledger-local fresh label and retain all stage fields. Requires: Internal constructor invariants; not a public admission bypass |
| path.resolve | RetainedSuccessorLedger.resolve, RetainedSuccessorLedger.resolve_payload, RetainedSuccessorLedger.resolve_mode | guard | candidate object -> registered object or mode stage | Require the exact object identity in the owning ledger, not just equal fields. Requires: Same-ledger object ownership |
| path.successor | RetainedSuccessorLedger.successor | constructor | Stage -> Stage | Append all endpoint-compatible root primitives, retain parent slots, build L and sibling-average A, verify A L=I and summary continuation. Requires: Every parent has at least one extension |
| path.deconstruct | RetainedSuccessorLedger.deconstruct | readout | Stage -> registry or parent plus extension pairs | Recover stored parent words and appended primitives. Requires: Owned stage |
| path.index | RetainedSuccessorLedger.family | constructor | Stage,direction -> IndexedPathFamily | Group all words by source or target and retain their stage identity. Requires: Explicit direction source or target |
| path.unindex | RetainedSuccessorLedger.deconstruct_family | readout | IndexedPathFamily -> ordered stage words | Recover every word and restore stage order, not group-flattening order. Requires: Owned family and complete recovery |
| path.transition | RetainedSuccessorLedger.transition | derived | ancestor,descendant -> (L,A) | Compose successive lifts and decoders along the actual ancestor chain; identity chain gives identities. Requires: Both stages on the requested same-ledger chain |
| path.encode | RetainedSuccessorLedger.encode | derived | ancestor,descendant,coefficients -> descendant coefficients | Apply the composed lift L. Requires: Valid transition and ancestor dimension |
| path.decode | RetainedSuccessorLedger.decode | derived | ancestor,descendant,coefficients -> ancestor coefficients | Apply A and reject unless L(A x)=x. Requires: Input in the lift image |
| path.register_payload | RetainedSuccessorLedger._register_payload | support | payload fields -> WeightedPathFamily | Retain values, word length, operation, parent IDs and cut slots under a fresh ledger identity. Requires: Internal constructor invariants |
| path.supply | RetainedSuccessorLedger.retain_path_payload, RetainedSuccessorLedger.retain_payload | constructor | owned stage or explicit words,coefficients -> WeightedPathFamily | Validate and register supplied coefficients; zero values do not delete word slots. Requires: Homogeneous distinct sewn words over registered primitives or an owned stage; exact coefficient dimension |
| path.compose | RetainedSuccessorLedger.compose_payloads | constructor | WeightedPathFamily,WeightedPathFamily -> WeightedPathFamily | Sew endpoint-compatible words and multiply their coefficients at the retained cut; keep both parent records. Requires: Same-ledger operands; rational multiplication |
| path.parents | RetainedSuccessorLedger.deconstruct_payload, RetainedSuccessorLedger.assembly_history | readout | WeightedPathFamily -> parents/cut or recursive assembly tree | Read registered provenance; do not infer parents by factoring output values. Requires: Owned payload |
| path.factor_test | RetainedSuccessorLedger.composition_blocks | readout | left,right,candidate -> CompositionBlock family | For each sewing vertex test rank at most one using exact cross products on the complete cut domain. Requires: Candidate has exactly the product word domain and total length |
| path.primitive_product | RetainedSuccessorLedger.compose_primitive_payloads | derived | first-successor,left coefficients,right coefficients -> product coefficients | Supply two root payloads and compose them; verify the resulting word carrier matches the stage. Requires: Direct successor of root |
| path.split | RetainedSuccessorLedger.split_payload | derived | nonroot Stage,child coefficients -> (parent means,remainder) | x maps to (A x, x-L A x). Requires: Owned nonroot stage; arbitrary exact child coefficients |
| path.reassemble | RetainedSuccessorLedger.reassemble_payload | derived | nonroot Stage,parent coefficients,remainder -> child coefficients | (c,r) maps to L c+r; reject if A r is nonzero. Requires: Typed parent dimension and r in ker A |
| path.summary | RetainedSuccessorLedger.summarize | readout | Stage,coefficients -> primitive final-occurrence summary | Sum coefficients by the last primitive ID. Requires: Owned stage and exact dimension |
| path.spectrum_validation | RetainedSuccessorLedger._validate_spectrum | guard | registered descriptors -> validation or rejection | Check idempotence, two-sided eigenrelations, completeness and mutual annihilation, including distinct-field sectors. Requires: Supplied exact quadratic descriptors for this continuation operator |
| path.inherit | RetainedSuccessorLedger.inherit | constructor | Stage,descriptor name -> InheritedMode | Register a stage-indexed handle retaining origin and primitive occurrence order. Requires: Validated registered descriptor |
| path.projector | RetainedSuccessorLedger.inherited_projector | derived | InheritedMode -> pair of rational matrices | Return L E A for each quadratic-field component. Requires: Owned mode; sum is the image projector, not ambient identity |
| path.mode_readout | RetainedSuccessorLedger.read_mode | readout | InheritedMode,coefficients -> pair of rational vectors | Decode to root, project there and lift back. Requires: Input in origin-lift image; arbitrary child payloads are rejected |

### Equations

- With parent slot pi(j) and sibling count m_i: L[j,i]=1_{pi(j)=i}; A[i,j]=1_{pi(j)=i}/m_i. Nonempty sibling families give A L = I.
- Split(x)=(A x, x-L A x). Its remainder is in ker A. Reassemble(c,r)=L c+r for A r=0. These maps are inverse on the full child space and parent space times ker A.
- decode is the inverse of encode ONLY on im L. It is not the averaging map on arbitrary child coefficients.
- For a sewn product at a retained cut, coefficient(p concatenated q)=left(p)*right(q); parent slots recover the supplied operand records.
- Associative path concatenation gives equal coefficient maps across bracketings; the stored assembly trees remain different.

## Component arithmetic

Word ::= zero | suc Word (the imported inductive Nat type, not imported Nat arithmetic)

```text
empty=zero; unit=suc empty
append zero b=b; append (suc a) b=suc(append a b)
endo a zero=empty; endo a (suc b)=append a (endo a b)
multiply=endo
numeral zero=0_S; numeral(suc a)=1_S+numeral(a)
```

| Operation | Source definitions | Kind | Rule |
|---|---|---|---|
| word.carrier | Word | carrier | Alias the imported inductive Nat type. |
| word.constants | empty, unit | constructor | zero and suc zero. |
| word.append | append | recursive_operation | Recurse on the first word, copying its constructors onto the second. |
| word.endo | endo, multiply | recursive_operation | Recurse on the second word, appending one copy of the first per successor; multiply is this endomorphism evaluation. |
| word.add_laws | append-unit, append-assoc, append-copy, append-comm, interchange | theorem | Inductive append unit, associativity, successor compatibility, commutativity and interchange proofs. |
| word.endo_laws | endo-generator, endo-add, endo-unique | theorem | Endomorphism generator value, additivity and uniqueness from that value. |
| word.multiply_laws | zero-left, unit-left, pointwise-add, composition, multiply-comm | theorem | Annihilation, unit, distribution, endomorphism composition and commutativity. |
| word.semiring | componentSemiring | derived_structure | Assemble the constructed operations and proofs into the Cubical Semiring record. |
| word.readout | Readout.numeral | readout | Interpret words in a supplied target semiring by zero/unit/addition recursion. |
| word.readout_laws | Readout.numeral-unit, Readout.numeral-add, Readout.numeral-multiply, Readout.unique | theorem | Prove numeral preserves unit, addition and constructed multiplication, and is the unique zero/unit/addition preserving map. |

## Native relationship

- **paths**: Source-backed partial computational algebra over exact rational path coefficients. A formal operational interpretation into native Resolve has not been constructed. Storing a Python result as an atom is not such an interpretation.
- **words**: Word is the supplied inductive natural-number type; append and endo are defined recursively without importing arithmetic. NativeComponentArithmetic supplies the constructed semiring to the existing native expression interpretation.
- **s4**: Neither rational coefficients, inductive words, grouping policies nor arbitrary spectral descriptors are claimed to be generated by S4. Their inputs remain explicit.

ComponentPort requires M equiv Word. The source does not derive that geometric normal form or identify arbitrary native packages with Word.

## Coverage boundary

- Census completeness covers every function/method defined in retained_path_successor.py, including private guards/support, and every named definition in ComponentArithmetic.agda. Imported dependencies remain explicit source structure.
- Exact rational tests exercise path equations on declared finite fixtures. The general split proof follows from A L=I; no global physical dynamics is inferred.
- The word proof and its native expression bridge have their own fresh Agda receipts, not inferred from a Python reimplementation.
- Signed and rational arithmetic extensions and all sector operations are outside this two-source census; this does not assert they are absent from Marici.
