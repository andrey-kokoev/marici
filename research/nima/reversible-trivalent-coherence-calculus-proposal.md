# Reversible trivalent coherence calculus

## Status and provenance

**Exploratory structural proposal — revision 1.** Recorded from the operator's
cross-session research draft, titled “Reversible Trivalent Coherence Calculus”.
This document separates its proposed primitives, additional coherence data,
conjectures and executable tests. It is not a theorem, a frozen source signature,
or an admission of new rules to the checked generating grammar.

The question is how much finite diagrammatic structure can be generated from
one unoriented trivalent relation, without importing application-specific
semantics or treating every placement as a new primitive.

## 1. Proposed primitive specification

Use one object symbol X and two orientations of one trivalent vertex:

- merge: μ : X ⊗ X → X;
- split: μ̄ : X → X ⊗ X.

The proposed primitive reversal satisfies r(μ)=μ̄, r(μ̄)=μ and r²=1.
The three ports are distinguishable before any symmetry quotient. Input slots
and output slots therefore retain their positions in the initial syntax.

Wire permutations belong to the ambient wiring structure. For example μ and
μ∘σ are placements of the same primitive, not distinct vertex generators.
Identity wires, composition, tensor notation and permutations are structural
syntax; their equations must be specified separately from vertex generators.

Finite networks are built by gluing compatible output/input ports. Their
external boundary is (m,n): m inputs and n outputs. The intended first census
concerns connected networks. A PROP additionally admits disconnected tensor
products; connectedness must not be silently dropped when selecting a formal
home.

### Explicit non-assumptions

Do not assume:

- μ̄ is an inverse or adjoint of μ;
- merge is commutative or associative as an equality;
- diagrams with the same boundary are equal or have a comparison;
- all higher fillers exist, are unique, or follow from free syntax;
- a canonical seven-element, seven-cell or seven-grade object exists;
- any physical, metric, probabilistic, independent-copying or cost semantics.

Reversal of primitive orientations alone does not define reversal of a whole
network or rewrite. Extending r requires a convention for port order and its
compatibility with gluing, composition, permutations and higher-cell direction.
Those conventions must be explicit before claiming induced split-side cells.

## 2. Coherence data versus derived consequences

At boundary (3,1), the two ordered trees

    μ(μ ⊗ 1)     and     μ(1 ⊗ μ)

are distinct syntax. A comparison α between them is **additional generating
2-cell data**, not a consequence of the vertex alone. Whether α is directed,
invertible, or accompanied by a separate reverse rewrite is another choice.

Once local associativity rotations are admitted, the five planar binary tree
shapes with four inputs give the usual pentagon adjacency graph. A 3-cell
comparing its two routes is a further coherence datum unless derived in an
explicitly specified theory. A graph cycle is not itself a filler.

Mixed composites include

    K = μ̄ ∘ μ : (2,2),       L = μ ∘ μ̄ : (1,1).

Neither L=1 nor K²=K is assumed, even up to a higher comparison. Mixed rewrite
cells require explicit boundaries and provenance; a common boundary alone
must not be used as a rewrite-generation rule.

Critical-overlap completion is a research procedure relative to a chosen
rewrite system. It can suggest new coherence generators, but does not in
general force canonical, unique or finitely many fillers. “Minimal completion”
requires an explicit criterion and may depend on choices.

## 3. Conjectures and reduction targets

1. **Local coherence reduction:** can elementary mixed comparisons be generated
   from α, a specified reversal extension and ambient wire symmetry?
2. **Factorization:** how far does the pure-tree sector separate into tree shape
   and leaf permutation? An associahedral/symmetric-group description is a
   candidate, not an established product or semidirect-product decomposition
   for mixed networks.
3. **Trivalent generation:** which precisely specified class of finite coherent
   systems admits an interpretation from this calculus? “Every diagrammatic
   operation” is too broad without a target class and preservation criterion.
4. **Seven hypothesis:** does the first mixed coherence object have seven
   essential grades or cells? The expression 2(2+1)+1 is a counting hint only.
   Ports, generators, cells, dimensions and grades are different kinds of
   things; adding their counts does not establish a canonical object.
5. **Minimality:** propose another primitive only with an obstruction or
   invariant showing that the current specified calculus cannot generate the
   required structure. Different meanings or placements alone are insufficient.

Potential homes include properads, PROPs, polycategories and higher computads.
An operad describes the pure many-input/one-output sector but not arbitrary
mixed boundaries. Dagger structure is optional extra structure, not a synonym
for the primitive reversal assumed here.

## 4. Graph conventions to resolve before enumeration

Record these in the enumerator's configuration and output:

| Choice | Open decision |
|---|---|
| Directed cycles | Allowed, forbidden, or reported as separate sectors? |
| Self-gluing | May an output attach to an input of the same vertex? |
| Parallel wires | Allowed between the same two vertices? |
| Boundary order | Ordered external legs, labelled legs, or quotient by permutations? |
| Port order | Fixed local input/output slots or quotient by local symmetry? |
| Isomorphism | Which vertex relabellings and port/boundary permutations preserve a diagram? |
| Connectivity | Underlying undirected connectivity, and treatment of identity wires? |
| Closed diagrams | Is boundary (0,0) included? |
| Reversal | Exact port-order convention and action on rewrite direction? |
| Rewrites | Which directed/invertible cells exist, with which contextual placements? |

Do not aggregate counts from different choices. Fixed-boundary automorphisms
and automorphisms allowed to permute the boundary are different groups.

## 5. First executable computation

After fixing a configuration:

1. Enumerate connected port graphs with one through three trivalent vertices.
   Handle zero-vertex identity wires separately if included.
2. Enumerate merge/split orientation patterns and compatible port matchings.
3. Canonicalize under the declared isomorphism relation, preserving all data
   not explicitly quotiented out.
4. Record boundary (m,n), canonical graph, orientation pattern, local and
   boundary port orders, and automorphism group (including its action).
5. Check reversal twice returns the original canonical class under the chosen
   convention.
6. Group by boundary and build rewrite edges from explicitly admitted local
   cells and contextual embeddings. Do not connect all equal-boundary pairs.
7. Compute components and graph cycles. Identify critical overlaps separately
   from disjoint-support interchange. Compare paths only using the declared
   higher-cell presentation.
8. Test candidate seven-count claims only after specifying what is counted and
   what notion of “essential” is used. Report counts other than seven unchanged.

### Combinatorial sanity checks

For a nonempty connected trivalent port graph with V vertices, E internal
wires, B external legs and underlying cycle rank b₁, ordinary incidence counts
(including multiplicity and counting a self-loop twice) give

    3V = 2E + B,     b₁ = E − V + 1,
    B = V + 2 − 2b₁.

If M vertices are merges and S are splits, compatible internal gluings cancel
one input and one output each, so

    n − m = S − M.

These are graph-counting checks, not Agda theorems in the current repository.
In particular, two connected trivalent vertices have B=4−2b₁, not seven
external legs. This does not refute a seven-*cell* conjecture; it rules out
conflating that conjecture with external-port counting.

### Falsification and reporting

Report boundary obstructions, disconnected rewrite components, incompatible
proposed fillers, unbounded requirements for new relations, or failure of the
proposed reversal extension. A finite census can expose counterexamples within
its scope; it cannot prove finite generation or coherence in all arities.

## First bounded test

The [first census results](reversible-trivalent-census-results.md) record an
executed DAG experiment through three vertices, under explicitly chosen
conventions. It recovers the pure pentagon and finds seven mixed two-vertex
**diagram classes only after quotienting boundary permutations** (22 with
ordered boundaries). This is not yet a canonical seven-grade or coherence-cell
result. Mixed associativity/reversal components at two vertices are isolated.

## 6. Relationship to current checked work

The existing [generating grammar](generating-grammar/README.md) has its own
source-bound constructors, rules and retained Resolve derivations. Its current
[repair status](generating-grammar/repair-status.md) includes supplied-operand
pairing and conditional DG frame/history theorems. None is currently proved
to be generated by this proposed trivalent calculus.

In particular:

- the DG algebra interfaces remain additional semantic inputs;
- primitive orientation reversal must not be identified with the invertible
  active request g used in those theorems;
- retaining a computed result is not a native derivation of it;
- structural tensor/wiring does not automatically prepare independent operands;
- the S4 working draft and its unresolved source-signature audit are not
  superseded by this proposal.

A future bridge must define an interpretation of boundaries, vertex generators,
wiring and admitted higher cells, and prove the appropriate preservation laws.
A generation or universality claim needs more than an interpretation in one
model. Until then, maintain this as a separate exploratory branch.
