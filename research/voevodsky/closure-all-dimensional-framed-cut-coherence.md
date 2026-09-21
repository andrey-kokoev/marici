# Arbitrary finite cut routes and all finite globular coherence levels

## Exact theorem now checked

For an arbitrary type K of cuts, suppose each cut k has an input type X(k), an output type Y(k), and supplied realization frames

- inputFrame(k): X(k) equivalent to A;
- outputFrame(k): Y(k) equivalent to B.

Fix a common operation f:A->B.

The new construction gives cut changes, comparison of any two finite routes with matching endpoints, closure of any finite cycle, and compatible higher comparison paths at every finite globular dimension.

This is a theorem for cuts with supplied common frames. It does not assert that every analytical realization, arbitrary filtration decomposition, or independently chosen cut transition supplies those frames and compatibilities.

Core: `agda/ClosureAllDimensionalCutCoherence.agda`.
Four-arity instance: `agda/ClosureArityCutCoherence.agda`.
Regression: `agda/ClosureAllDimensionalCutRegression.agda`.

## What is being compared

A compatible presentation at cut k is a pair:

1. F:X(k)->Y(k);
2. a square witness identifying outputFrame(k) composed with F with f composed with inputFrame(k).

`Compatible k` retains both the map and that witness. Postcomposition by the output frame is an equivalence of function types. Its fiber over the fixed common-operation presentation is therefore contractible.

Only this fiber is contractible. X(k), Y(k), and the full function space X(k)->Y(k) are not asserted to be sets or contractible. The circle regression explicitly retains the loop in an underlying realization.

## Actual cut-change maps

`change i j` transports the supplied function through the source and target frames. It also constructs the new square witness from the old square and the frame inverse laws.

`mapSpaceEquiv i j` is an equivalence between the full function spaces at i and j, before fixing f. `changeUnderlying` checks that the function part of `change` is precisely the forward action of this equivalence.

The construction is not just a choice of unrelated points in contractible types: it uses the actual function supplied at the earlier cut.

## All finite routes

`Route i j` is an inductive finite sequence of cuts. `run` applies the constructed cut changes along that route. There is no fixed bound on route length or on the number of possible cuts.

`routeComparison` compares any two runs with the same starting compatible presentation and the same final cut. `cycleLaw` specializes this to a return route and the identity route.

These are equalities of map-and-square pairs. They retain the compatibility information needed to compare the subsequent homotopies.

## All finite dimensions

`ContractibleTower` defines the entire hierarchy recursively:

- Boundary(0) is Unit and Cell(0) is the compatible-presentation type;
- a boundary at level n+1 consists of a boundary at level n and two parallel level-n cells;
- a level-(n+1) cell is a path between those parallel cells.

`allCellsContractible` is proved by induction on an arbitrary natural number n. `fillCell` supplies an inhabitant at every such boundary. This is not a finite list of checks at dimensions zero through three.

The dimension n counts iterated path depth in the compatible-presentation space. It is not input/output arity, cut position, or a physical realization dimension. The theorem concerns globular parallel-boundary fillers, not a separately formalized model of every higher categorical diagram shape or an infinite-limit completion.

## Connection to the existing four-arity/cofiber model

`ArityCuts` constructs common frames for the four Boolean indexing cuts from the already supplied sum-input and product-output equivalences. It installs the four concrete operations as compatible presentations.

Its `attach` operation admits an independently constructed indexed operation only with a proved equality to the displayed operation. The regression supplies the previous `ClosureBooleanArityCofiberBridge.operationComparison`, so the existing cofiber map is genuinely included rather than assumed compatible.

The regression compares clockwise and counterclockwise four-cut routes. It compares a direct cycle proof with a proof going through the other route, and then checks a third-dimensional comparison between independently assembled higher witnesses. It also instantiates the universally quantified all-finite-level theorem.

This does not yet identify every previously chosen canonical pentagon or ladder-composition witness with one of these fillers. Such an identification requires lifting those particular witnesses, including their square coherences, into the compatible-presentation fibers.

## Why invertibility alone is insufficient

A negative regression constructs Boolean negation as an equivalence Bool≃Bool and proves that its action is not homotopic to the identity. It also proves that this function cannot carry the required identity-operation square with fixed identity frames.

Thus independently selected invertible transitions can have nontrivial holonomy. The theorem constructs transitions from common frames; it does not declare arbitrary previously chosen transitions coherent simply because each one is invertible.

## Verification

Fresh dependency-closure check:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureAllDimensionalCutRegression.agda`

Exit 0. All three new modules use `--safe --cubical --guardedness`, with no holes or postulates. Existing source modules were not modified. The initial incremental check caught a name collision with Cubical's primitive `fill`; renaming the constructed operation to `fillCell` resolved it.

The mathematical engine is the standard HoTT contractibility of an equivalence fiber and its iterated identity types. The new deliverable is the explicit route construction, all-level proof, and checked connection to the existing cofiber/arity instance—not a claim of a new unconditional theorem about all realizations.

## Remaining realization gate

To apply the result to an arbitrary proposed realization cut system, provide the actual types and common frames, and prove that its independently defined operations/transitions carry the required compatibility witnesses. In particular, construction of every arbitrary-length filtration quotient and its intrinsic frames remains separate from this conditional coherence theorem.
