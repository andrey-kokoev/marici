# Active-cap moment blocks compose by finite network pricing

## Result

There is now a complete mathematical construction, with an executable exact
prototype, for moment-constrained membership and allocation across active-cap
chain blocks. It uses network-priced source columns, not projected facets.

It supplies:

- a source lift or a source-relative separating certificate for a requested
  endpoint/U/V tuple;
- optimization with global AND block-local retained linear frames;
- joint search over shared endpoint values and local moment allocations;
- exact witness gluing and composed flow-based objective certificates;
- finite progress from a fixed source grid, with all growth charged.

This is a Dantzig--Wolfe-style decomposition specialized to the declared
source and certificate contract. It is not a polynomial column-generation
bound, a new general LP theorem, or a claim of superiority to source-space LP.

## 1. Source and scope

The executable subclass keeps the original caps 0<=t_j<=100+2j, the global
chart s_j=1+(j mod 3), and z_j=t_j/s_j. Its evidence is

    0<=z_0<=1,
    1/2<=z_(j+1)-z_j<=20.

Every cap remains in each block graph, including active caps. Block [l,r]
contains all its atom caps and internal neighbor edges; it includes z_0<=1
only when l=0. Blocks cover a chain, have disjoint interiors and share their
adjacent endpoints. A shared raw value uses the SAME global chart and slope
r_j=128^-j in both blocks.

Every declared block is nonempty: z_j=(j-l)/2 is an admitted local source.
Global feasibility is not assumed after adding retained frames or moment pins.

The structural argument below applies more generally to nonempty bounded
rational difference-constraint blocks with a fixed rational linear observer.
Their positive charts, graph coverage and cap admission must first be
certified. An inconsistent block would terminate through its negative-cycle
certificate before seeding the master. The executable Block constructor here
implements the specified chains, not arbitrary gain-graph admission.

## 2. A finite source dictionary without projected facets

Choose D so that every normalized graph edge weight multiplied by D is
integral. In this executable family D=6 works for all blocks.

The anchored incidence matrix is totally unimodular. Consequently every
vertex of

    Mz<=w, z_*=0

has Dz integral. The cap-bounded source is therefore the convex hull of its
admitted D-grid points. It is unnecessary to enumerate them.

There is also a direct guarantee on the particular NETWORK oracle's output.
Its final potential is obtained from shortest paths in a residual graph whose
weights are original edge weights or their negatives. Subtracting the anchor
potential leaves every coordinate on the same D-grid. Rational moment prices
change flow demands, but do NOT change this potential grid.

For a block with cap C_j/s_j on normalized coordinate j, the admitted grid
contains at most

    G_b = product_(j in block) (floor(D*C_j/s_j)+1)

points. This is a finite schema-dependent dictionary bound, typically enormous.
It is not the old quadratic projected-facet bound. The runtime stores only
columns it actually generates.

## 3. What the master retains

A column is an admitted block potential z, its source provenance and its local
observation (left endpoint, right endpoint, U_b,V_b). Each block has nonnegative
column weights summing to one. Their convex mixture is an admitted local
source and realizes the corresponding local moment allocation.

Neighboring block mixtures must agree on their shared RAW endpoint. Global
moments are computed by

    U = sum_b U_b - sum_shared h,
    V = sum_b V_b - sum_shared r_h*h.

The implementation charges each overlap's moments once, retaining global
slopes rather than restarting the slope sequence inside each block. It pulls
global endpoint/moment frames through these identities and also accepts
block-local endpoint/moment frames.

The master searches these allocations. It does not receive a preselected
shared endpoint, local moment budget or compatible source section.

If all couplings hold, the mixed local source vectors glue at their shared
values. Every original cap and chain edge belongs to a block; all retained
local frames hold at that block's mixture. Global accounting then gives the
requested observations and global frames exactly.

## 4. Query Phase I: complete feasibility, not a failed-solver inference

Seed each block with one admitted network column. Keep its convexity equality
hard. Write every other coupling, retained frame and requested observation pin
as inequalities, using both signs for equalities. For each of these rows add
one nonnegative violation variable, and maximize MINUS their sum.

This restricted master is always nonempty: choose the seed columns and make
the violation variables large enough. Its objective is bounded above by zero.
This remains true as columns are added.

At a restricted optimum, let mu>=0 be its checked row multipliers, and let
alpha_b be the net multiplier of block b's convexity equality. Pricing asks
block b to maximize the negative weighted coupling/frame functional on its
ORIGINAL graph. This is the existing node-demand network support problem.

If its value exceeds alpha_b, its returned source column strictly violates a
restricted-master dual inequality. It cannot already be a stored column.
Add that column and repeat.

If no block has positive pricing:

- value zero gives a feasible allocation and zero violations;
- a negative value proves the requested slice infeasible.

The latter conclusion follows from valid block flow bounds and row
multipliers, not merely from the master solver's status. Summing the local
flow inequalities and the weighted retained rows cancels every source-node
coefficient and leaves a strictly negative constant.

For a membership request y, collect the net multipliers eta of its observation
equalities. Removing their constant terms gives a displayed separator

    -eta^T y' <= B,
    B+eta^T y < 0.

It is valid for every observable y' admitted under the SAME retained global
and local frames. An infeasible pinned slice does not mean the underlying
unrefined source graph is empty.

## 5. Query Phase II: optimization and certificate composition

After Phase I reaches zero, remove its violation variables. The restricted
master remains feasible, and its column weights lie in products of simplices,
so every linear objective has a finite optimum.

Now pricing maximizes, in each block,

    local objective - weighted coupling/frame functionals.

A positive price again adds a new source column. If no price is positive,
the block flow bounds plus the master row multipliers give a global upper
bound. The mixed, glued source attains it, proving exact optimality.

Shared-endpoint row pairs supply unrestricted net shared-value prices. Moment
pins and local/global frames supply the other multipliers. Independent block
maximizers need not agree: they certify local PRICE bounds. The master mixture,
not an arbitrary collection of those price maximizers, supplies the compatible
primal source.

## 6. Finite progress and the restricted-master implementation

The network oracle always returns an admitted grid point. Every positively
priced point is new. Columns persist across the two query phases, so there
are at most

    sum_b G_b - B

column additions after one seed per block. This proves finite outer progress
without any projected-facet dictionary. Strict separation by arbitrary cuts
would not, by itself, have established this result.

The master also needs a terminating exact method. The initial stronger
membership experiment stalled in the previous SymPy proposal path. The final
implementation does not use that path: it has a rational, two-phase simplex
with Bland's entering and leaving rules. Those rules prevent cycling over
the finite basis set. Zero artificial basic variables are pivoted out, or their
redundant rows removed, before the simplex objective phase.

Every returned master point and dual vector is checked against its original
rows. Slack columns retain the original-row transformation and yield the dual
weights. No floating-point admission is involved.

An exhaustive rational basis fallback independently supplies the same bounded,
nonempty-master contract. Enumerate independent active bases, solve primal
and dual systems, and accept only primal-feasible points with nonnegative
basis duals. A bounded nonempty nonnegative-variable LP has an optimal vertex;
its objective lies in the cone of its active normals. An independent conic
support can be extended to a full active basis with zero extra weights, so a
certifying basis exists. This fallback is finite but can be impractical.

The API permits bypassing the simplex proposer with fast_master=False. The
reported workload uses the checked Bland simplex. Two separate controls force
proposal failure and a false infeasibility report; both are replaced by checked
basis certificates, never accepted as evidence that a query is empty.

The simplex's internal feasibility phase is distinct from the QUERY Phase I
above. Query Phase I is deliberately feasible even when the requested source
slice is empty.

## 7. Independent executable evidence

The frozen workload contains seven requests:

| Request | Stored columns | Master solves | Result |
|---|---:|---:|---|
| Hidden active-cap membership | 7 | 7 | excluded |
| Feasible active-cap membership | 7 | 8 | source lift |
| Two-block U support | 6 | 6 | U=1071/2 |
| Two-block coupled global frames | 12 | 12 | optimum |
| Three-block equivalent global frames | 15 | 14 | same optimum |
| Two-block local moment frame | 12 | 12 | U=2537/6 |
| Contradictory retained history | 4 | 3 | infeasible |

The coupled requests retain an endpoint bound and a U+V bound. Two and three
block decompositions agree exactly. The local-frame request constrains the
LEFT block's U to at most 70 while maximizing global U; this is not just a
public-only refinement.

The stronger hidden-cap control requests the observations of raw candidate

    (1,32,108,45).

It satisfies the chain differences and endpoint caps, but violates atom 2's
cap 104. Importantly, the admitted source (1,36,104,45) has the SAME endpoints
and U. Only the requested V distinguishes the impossible tuple: together the
four observations force atom 2 to be 108. The generated Phase I certificate
has value -127/4096 and supplies an explicit observable separating row. This
is automatic moment-infeasibility handling, not the earlier hand-constructed
cap separator.

The positive membership control requests the observations of (1,36,104,45)
and reconstructs a source from generated columns. No compatible source witness
is supplied to the master.

Across the workload the verifier checks all 62 restricted-master proofs and
123 network pricing certificates, as well as every added grid column, terminal
source bound/Farkas combination, shared value, local frame and glued source.
Eight mutations are rejected, including a dropped expected frame, altered
flow, non-grid column, mismatched shared lift, corrupted objective, forged
Phase I value and invalid progress record. Two fallback controls are checked
separately.

The verifier imports no optimizer, source constructor, pricing routine or
simplex implementation. It builds source-node coefficients directly, rather
than sharing the producer's endpoint/moment bookkeeping map. It requires
assertions enabled.

Files:

- `checkers/active_cap_moment_master.py`
- `checkers/exact_master_simplex.py`
- `checkers/finite_master_lp.py`
- `checkers/check_active_cap_moment_master.py`
- `checkers/verify_active_cap_moment_master.py`
- `results/active-cap-moment-master-contract.json`
- `results/active-cap-moment-master.json.gz`

Reproduce with the Python standard library only:

    python research/grothendieck/checkers/check_active_cap_moment_master.py
    python research/grothendieck/checkers/verify_active_cap_moment_master.py

## 8. Resource and continuation limits

The method keeps original block graphs and generated source columns. If K
columns are stored, the objective-phase master has K nonnegative variables;
query Phase I also has one violation variable per non-convexity inequality.
Retaining B block identities does NOT make this master fixed-dimensional.

A column contains a source vector. Flow certificates charge graph edges and
rational weights. Retained frames, exact moment coefficients, mixture weights,
master matrices, pricing transcripts and witness archives all count. The
independent verifier checks full traces; no total-storage saving is inferred
from a compact terminal certificate or a compressed archive.

The source-grid bound can be exponential in the number of atoms and very large
in coefficient encoding size. Bland simplex and exhaustive basis enumeration
are finite, not polynomial iteration guarantees. The residual-network solver
also has a rational finite-augmentation argument, not a polynomial bound for
this implementation. Workload counts above must not be promoted to such bounds.

The source graph and fixed observer carry the original information. Generated
columns are a growing access representation, not a lossless replacement for
the graph under arbitrary future source refinements. Further hidden audits
require extending the retained observer/master rows with valid source access;
the returned source lift is only a witness of possibility, not the actual
source. Charts do not silently change the declared observation accuracy norm.

The research contract fixes synthetic source/evidence/query cases. Hashes bind
versions, not observation authenticity or fresh upstream source admission.

## Synthesis and next boundary

Active caps no longer separate support access from complete moment-aware
composition: the network oracle, an exact master and a finite source-grid
pricing theorem now supply the missing link on this chain subclass.

The next structural question is RESOURCE CONTROL rather than basic closure:
can graph structure or a bounded number of moment couplings give useful
bounds on generated columns, master size and certificate bits, without the
huge all-grid bound? Arbitrary balanced-gain graph admission and non-chain
separator topologies also require their own verified source/overlap contracts.

Related:

- `active-cap-moment-blocks-admit-flow-dual-certificates.md`
- `moment-aware-chain-blocks-compose-with-quadratic-flat-interfaces.md`
