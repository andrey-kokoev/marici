# A connected observer diagram with actual higher cells

## Construction

`agda/ObserverCoherenceCube.agda` constructs a square and a three-dimensional
cube in the Cubical universe of types. Given an observer expansion e:O~=R,
set T=ua(e), so T(0)=O and T(1)=R. Then

    Square(i,j) = T(i) x T(j)
    Cube(i,j,k) = T(i) x (T(j) x T(k)).

These are actual interval-indexed type families. The square is a 2-cell; the
cube supplies six compatible faces, with the faces agreeing on shared edges
by construction. Agda checks all six face restrictions. Paths from the
square origin to its other vertices establish connectedness of this diagram.
The ua computation rule identifies each coordinate's transport with e.

For supplied u,v:O, `square-section` constructs a section over the entire
square, recovering (u,v) at the source corner and (e(u),e(v)) at the opposite
corner. `cube-section` does the same for three supplied observers. This
connects the type-level diagram to actual joint realizations.

## Source connection

The `FromSource` module imports the existing general dependent EP/PE chains
from `DependentSigmaPiCoherence.agda`, including all intermediate values and
link witnesses. A canonical full trace is

    Sigma(q:Q). Sigma(t:Trace(q)). t=canonicalTrace(q).

Its projection to q is proved equivalent to Q. Each trace here contains BOTH
previous routes; this is a redundant full-trace realization of the earlier
fixed-route observer presentation. The type explicitly restricts to canonical
traces. No theorem collapses arbitrarily varying trace or proof data to Q.

A free observer is a pair of canonical full traces. The resulting expansion

    e : Observer ~= Q x Q

instantiates the generic square and cube. For two observers, the four square
vertices are precisely the previous observer presentations:

    O x O              (Q x Q) x O
    O x (Q x Q)        (Q x Q) x (Q x Q).

The two expansion orders use explicit, separately typed intermediate maps.
Their composites agree pointwise. `ComparedRoutes` retains both schedule
constructors and their map equality. A discriminator proves the two schedule
constructors unequal: agreement of maps does not delete construction order.

## Return to Q

`nextQ` packages a realized square as an existing `WholePackageSigmaPi`
Complete: both source observers, both schedules, their homotopy, the output
and its boundary equation. Recovery of the source is checked.

The attachment family is separately retained:

    Attach(u,v) = routeA(source(u)) = routeB(source(v)).

Canonical diagonal observers have attachments by the previous route-comparison
proof. `AttachedObserver` stores an observer AND that witness. `nextAttachedQ`
packages two attached observers and their presentation square, and its recovery
theorem returns both observers with their attachment proofs. This implements
whole coherence data becoming the next source package.

The family of possible types can be formed without source inhabitants.
Realized sections require the actual source observers; attached realizations
additionally require their attachment witnesses. No numerical positive area,
or equation C(C(C(Q)))>0, is asserted by this construction.

## Connectedness and higher structure

The square/cube diagram is a finite fragment inside the higher groupoid of
types and equivalences supplied by Cubical type theory. It is not a completed
free infinity-groupoid presentation, a Kan-completion algorithm, or a theorem
that every parallel boundary admits a filler. The finite cube's shape being
contractible does not make its ambient types contractible.

A formal hostile makes that distinction concrete: ua(notEquiv) is a loop
Bool=Bool whose transport sends true to false. Agda proves that loop is not
refl. This also prevents interpreting path existence as universal path
uniqueness or forgetting the transport action.

Higher cube recipes can be obtained by adding independent product factors.
The new certificate explicitly checks dimensions two and three. The Python
incidence checker additionally checks boundaries through dimension four; that
finite calculation is not an arbitrary-dimensional formal theorem.

The three-observer cube expands to SIX Q factors. Cube dimension counts
independent expansion operations. The earlier 'quartic' terminology counts
four Q factors in the TWO-observer square. These counts measure different
parts of the same construction.

## Finite source regression

The existing dependent source has 18 values. Its original full-chain code
constructs 324 free observers and 18 attached ones. The new checker uses six
selected observers, including attached and unattached pairs, and tests:

- 216 observer triples;
- all six expansion orders, 1,296 retained routes total;
- all six square faces, 1,296 square comparisons total;
- reconstruction of the complete input traces at every intermediate state;
- preservation of attachment conditions after expansion;
- 8 vertices, 12 edges, 6 faces, 1 cube;
- boundary-squared-zero for every cell in dimensions one through four.

Deleting a cube face gives a nonzero boundary residual. Repeating an already
executed expansion is refused. An existing free observer with incompatible
source entries is correctly recognized as unattached.

## Verification

Run through shell:

```powershell
pwsh -NoProfile -File research/nima/checkers/check_observer_coherence_cube.ps1
```

Fresh Agda compilation passed under safe Cubical options, ignoring interfaces.
Both negative compiler controls failed with exit 42 and the intended errors:

- collapsing retained schedules: `leftFirst != rightFirst`;
- erasing specified transport: `false != true`.

Receipts:

- `results/agda-ObserverCoherenceCube.json`
- `results/observer-coherence-cube.json`
- `results/observer-coherence-cube-formal-audit.json`

The newly checked bridge is: full source traces -> observer expansion
square/cube -> realized compatible sections -> retained next-Q package.
Extending this fragment to a source-generated higher comparison calculus,
and connecting any positivity interpretation, remain separate obligations.
