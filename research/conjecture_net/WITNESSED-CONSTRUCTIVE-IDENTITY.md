# Proposed witnessed constructive identity

## What we are proposing

A reversible identification is not adequately realized by a pair of arrows or equal final outputs. It requires a source-generated, reusable package witnessing the identification, its comparisons through other presentations, and the dependent continuations it licenses.

This is the reversible branch of a broader constructive-capability foundation. An arbitrary function A->B is not required to be invertible. Noninvertible construction needs its own criterion, such as retaining the larger process/history space and specifying what its readout forgets.

Proposed net: `contracts/witnessed-constructive-identity.proposed.v1.json`.

**Frozen first instance:** [finite reversible witnessed realization](FINITE-REVERSIBLE-WITNESSED-REALIZATION.md). Source: NOT/CNOT/Toffoli with clean work. Target: every finite bit-string bijection. Third presentation: retained input/output graph. Common center: the exact marked pair. Continuations: all specified finite permutation words and logical predicates. This selects a bounded theorem, not the universal parent's source.

## One picture, three kinds of things

    A -------- ab --------> B
    ^ <------- ba --------- |
    |                       |
    ca / ac             bc / cb
    |                       |
    +---------- C ----------+

The picture denotes six directed edges: ab,ba,ac,ca,bc,cb. It is not itself a coherence certificate.

- A,B,C: typed presentations with actual marked inhabitants.
- Directed edges: source-licensed operations between those presentations.
- Cells: witnesses comparing operations and witnesses comparing those witnesses.

Composition notation below is conventional right-to-left: cb o ac means A->C->B. Identity on A is id_A, not the type A itself.

## The package, layer by layer

| Layer | Required data | What it establishes |
|---|---|---|
| 0. Marked presentations | a:A, b:B, c:C, with source/context | Actual inhabitants, not just named types |
| 1. Reversible bridge | ab:A->B, ba:B->A; eta:ba o ab~id_A, epsilon:ab o ba~id_B; pointed compatibility ab(a)=b | Recovery of the full admitted inputs, not one sampled endpoint |
| 2. Independent comparison | ac,ca,bc,cb; alpha:cb o ac~ab, beta:ca o bc~ba, with marked/source compatibility | The C routes realize the same proposed bridge |
| 3. Filled returns | T_A:ba o cb o ac~id_A, T_B:ab o ca o bc~id_B | The two oriented comparison complexes actually close |
| 4. Coherence of certificates | Compatibility of T_A with eta after alpha, T_B with epsilon after beta; inverse triangle coherence; further typed pasting cells required by composition | The independently constructed certificates describe one coherent identification |
| 5. Reusable realization | Dependent continuation transport, package composition and retained-certificate recovery | The result remains a constructive capability in its next context |

Each row adds a different kind of datum. An edge count does not supply a face, and two faces do not automatically supply their comparison cell.

## What the common center means

The operator's coincident barycenters ask that the two oriented complexes share a rooted realization, not merely analogous shapes.

Specify a common realization D, actual realization maps for both complexes, a marked center m:D, and witnesses identifying their realized centers with m. Retain the boundary and source comparisons alongside that mark.

Two alternatives must remain explicit:

1. A geometric barycenter: declare the affine/metric realization, weights, and center construction; then prove center equality.
2. A constructive center: m is the common marked source/constructor witness, with explicit maps connecting the two complexes to it. This is not an arithmetic average.

In either case, coincident centers alone do not imply equality of complexes. The center is an anchor within the certificate, not its compression. The proposal uses the constructive-center reading as its default; a geometric specialization adds its own realization data.

The triangle returns live at A and B. Their fillers cannot literally be equated before transporting to a common comparison type. Every higher cell must name its parallel boundary.

## The first higher equations

For all x:A, inverse coherence compares

    ap ab (eta_x) = epsilon_(ab(x)).

Pointwise path application is meant by ap. The two paths have the same endpoints ab(ba(ab(x))) and ab(x).

At the A return, alpha and eta supply a canonical candidate filler: first whisker alpha by ba, then use eta. If T_A is independently constructed, require a higher comparison between T_A and that candidate. Similarly compare T_B with beta whiskered by ab followed by epsilon.

This prevents defining the independent comparison solely by renaming the desired answer. When further bridges are composed, require their cells to paste compatibly; the resulting association/transport equations must be given at the chosen interface's higher level.

## The conjecture versus the definition

Definition candidate: the package above specifies what counts as a witnessed reversible realization at a fixed source/interface scope.

Conjecture: every reversible identity admitted by the proposed common process account has such a source-generated realization, and composing/transporting those realizations preserves the licensed dependent continuations. An identity admitted by mere endpoint agreement is insufficient when those continuations distinguish its underlying processes.

The generation requirement is substantive. The source operations, marked comparison and continuation library must be fixed independently of the answer. Merely storing externally supplied equivalences/fillers in a record does not establish generation.

To make the universal conjecture executable, freeze the source class, admitted reversible identities, context/resource policy and continuation family. A counterexample must be typed against that scope. There is no circular rule saying that an identity is admitted exactly when it already has the desired package.

## How the known research fits

- Kitaev's n, P(n), C(n), J(n): acts, composed acts, situated compositions, relationship vocabulary. These organize candidates for the package; their cardinalities do not supply its cells.
- `research/voevodsky/closure-four-presentations-hott-proof.md`: a model-level comparison of independently constructed maps AND their square witnesses.
- `research/nima/retained-tetrahedral-package.md`: actual boundaries/fillers with typed downward recovery.
- `research/nima/tetrahedral-hierarchy-at-vertex.md`: a bare returned vertex loses the package; a retained marked view preserves it.
- `research/nima/dependent-transport-machine.md`: concrete execution and continuation semantics distinguish equal endpoints.
- `research/sontag/deutschean-control-explanation-of-marici-object.md`: the object as a source-relative contextual law of constructive possibility.
- Routing-only projector obstruction: a particular attempted realization cannot preserve the required coherent action.

## Constructed first path-sensitive test

[Witness-sensitive route realization](../voevodsky/witness-sensitive-route-realization-v1.md) binds the existing stay/turn/follow machine to filled return triangles. A dependent transport continuation consumes the retained first edge. Stay and turn have identical vertices and return diagonal but yield false and true. A safe Cubical theorem excludes every observer of only that diagonal which claims to recover this continuation. This realizes a nontrivial path-sensitive scope, not universal higher coverage.

## Next mathematical test

Instantiate A,B,C and the six maps from an existing independently constructed comparison, not from three renamed copies. Write the exact types of its two return fillers and the higher comparisons, then test a dependent continuation that actually consumes retained witness information.

The first deliverable is that complete instance and a certificate-erasure hostile. It is not another inventory of possible metadata or a physical experiment.

## Hodge comparison research branch

[HODGE.md](HODGE.md) develops the operator's higher-coherence intuition as a separate [rational Hodge research net](contracts/hodge-conjecture-net.v1.json). This net's `research_branches` entry and the [typed attachment overlay](contracts/hodge-foundational-attachments.v1.json) provide reciprocal references, not proof transfer. The algebraic cycle-class map is generally noninjective: Hodge asks for algebraic preimages, not reversible recovery of every cycle witness. A proposed packet obstruction must descend to rational cohomology and vanish on **all** algebraic cycles, not just divisor-generated ones. Those necessity and descent bridges remain open; finite controls do not supply them.

## Subsequent configuration-space proposal

[Ledger 4322 — Configuration Coherence and the Candidate Constant 1836](../../src/ledger/20261014-4322%20Configuration%20Coherence%20and%20the%20Candidate%20Constant%201836.md) develops the broader proof-as-capability proposal through signed codimension-one dependencies, input/output recovery and coherent continued use. It proposes a sector count of n times 2^(n−1) and a three-product encounter count giving 1836 at n=3. Its recovery equations can preserve a supported configuration without giving global equivalences, so that proposal is broader than the reversible branch specified here. Source generation, witness-consuming continuations and actual certificate accounting remain the shared test obligations; the later entry does not assign outcomes to this net.
