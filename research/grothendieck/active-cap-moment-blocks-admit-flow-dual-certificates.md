# Active-cap moment blocks admit flow-dual certificates

## Result and implementation status

Active caps do not prevent source-space certified support or exact block
composition for balanced-gain difference systems. They do invalidate the
independent-increment box and its quadratic projected-facet theorem.

An exact residual-network solver now computes moment support with checked
potential/flow certificates. Fifteen network answers agree with independently
checked source-LP references. Six moment-membership lifts, a hidden-cap
separating Farkas proof and a computed negative cycle also pass independent
verification. Seven corrupted statements/proofs are rejected.

This is not merely a generic LP backend renamed as a flow oracle: the support
solver uses rational shortest augmenting paths and imports no optimizer.
Moment-constrained membership remains a separate source-LP branch. No finite
projected-cut dictionary or polynomial augmentation-count claim is inferred.

## Source model

Fix a verified positive chart t_j=s_j z_j. Include an anchor z_*=0.
Represent every accepted gain inequality and every source cap as an edge

    z_v-z_u <= w_(u,v).

For the owning caps, the anchor edges have weights cap_j/s_j and zero.
They remain present even when active. Let M be the edge-node incidence
matrix: each row has +1 at its head and -1 at its tail. Then the normalized
source is Mz<=w, with the anchor fixed.

The anchor cap edges bound every source coordinate. A negative cycle gives
a contradiction by summing its inequalities. Conversely, without a negative
cycle, shortest-path potentials provide a feasible assignment; translating
the anchor to zero preserves every difference and satisfies the anchored
constraints. Thus this branch handles genuine inconsistency rather than
mistaking failed normalization or failed optimization for emptiness.

## Endpoint and moment objectives become node demands

A block observation is y=Tz, consisting of its selected raw endpoints and
its moment contributions

    U=sum_j s_j z_j,  V=sum_j r_j s_j z_j.

For an observable objective a, put q=T^T a on the non-anchor nodes and
q_*=-sum_(j!=*) q_j. Since the anchor is zero, its added coefficient changes
no objective. The total node demand is now zero.

The support problem and its flow dual are

    maximize q^T z subject to Mz<=w, z_*=0,
    minimize w^T f subject to M^T f=q, f>=0.

Here M includes the anchor column. The anchor balance equation follows from
the other balance equations and zero total demand. This is a transshipment
problem on the ORIGINAL source graph, not on projected facets.

For a nonempty bounded source, rational LP duality supplies a feasible
potential and nonnegative flow with equal objective values. The anchor edges
make routing possible in both directions. Valid certificates require only
primal edge checks, node balances and equality of the attained value with
w^T f. A verifier need not reproduce a shortest-path or flow algorithm.

An optimal basic flow exists with at most as many nonzero arcs as non-anchor
nodes: the incidence matrix has that rank, and the nonnegative flow polyhedron
is pointed. The proposer need not return that particular basic flow, and this
is a bound on its arithmetic support, not its entire statement or bit size.

A single checked flow proves an upper bound even when it is not optimal.
No claim that any chosen shortest-path potential optimizes the moment
objective follows: moment objectives impose distributed node demands.

## Exact joint membership requires more than shortest paths

At a requested interface value y, solve

    Mz<=w, Tz=y, z_*=0.

The moment equalities are generally not difference constraints. Consequently
ordinary shortest-path closure alone is not a complete membership algorithm
for the moment-aware interface.

A feasible potential is a source lift. An infeasibility certificate has

    f>=0,  M^T f+T^T eta=0,  w^T f+eta^T y<0,

after removing the anchored coordinate, or adding an explicit multiplier for
its equality. The moment multiplier eta is unrestricted. For every admitted
interface value y', the same identity proves

    -eta^T y' <= w^T f.

The requested y strictly violates this inequality. Thus a source-space
Farkas certificate gives a certified observable separator.

These separators need not lie in a predeclared finite dictionary. Strict
separation alone therefore does NOT establish finite termination of the
existing lazy projected optimizer. Exact source-space LP is a complete
reference route; a specialized network-plus-moment solver needs its own
termination contract.

## Composition remains exact

For adjacent blocks sharing raw atom h=t_s, retain both local moment pairs
and impose

    U=U_L+U_R-h,
    V=V_L+V_R-r_s h.

Include all shared source coordinates in both interfaces, every source cap,
and every evidence edge in at least one block. Charts must agree on overlaps.
Every global source restricts to compatible block points. Conversely, block
source lifts with matching shared values glue and satisfy the union of their
constraints, including active caps. The accounting identities establish the
global moments without double-counting.

This argument also accommodates block-local retained moment equalities or
inequalities, provided they are included in each block's source-space
certificate problem. It does not imply that their graph-only projection is
captured by shortest-path distances.

For a prescribed allocation of local objective coefficients, block flows give
valid block bounds. Their sum is a global bound when shared coefficients and
moment accounting match the global objective. Exact global optimality requires
compatible primal lifts attaining that bound; independently optimal block
witnesses need not agree. Shared-variable prices and moment multipliers are
the dual variables enforcing this compatibility, not newly observed data.

## Exact residual-network implementation

The network solver first uses Bellman--Ford relaxation from a virtual root to
find feasible potentials or extract an original-edge negative cycle. A cycle
is accepted as inconsistency only after its closed path and negative total
weight are checked.

For a consistent graph, attach a supersource to supply nodes and demand nodes
to a supersink. Original graph arcs have unbounded flow capacity. Repeatedly
augment along an exact shortest residual path, including reverse arcs for
positive flow. Supply and demand arcs have finite rational capacities.

There are no negative residual cycles initially; shortest-path augmentation
preserves that property. With a common denominator D for the demands, every
positive augmentation increases routed mass by at least 1/D. Hence the method
terminates on this bounded, anchor-connected rational source class. This is
a finite rational termination argument, not a polynomial bit-complexity bound:
D times total demand can be large in binary encoding.

At full routing, compute feasible potentials for the original residual graph.
Every original edge still has its forward residual arc. Every positive-flow
edge also has its reverse arc, forcing its potential inequality to equality.
Thus the potential is source-feasible and complementary to the flow, and
q^T z=w^T f. Independent verification checks these final identities rather
than reproducing the augmentation algorithm.

The verifier includes the anchor balance explicitly. Observable node demands
are completed at the anchor by minus their sum; equivalently, observations
use z_j-z_* before the anchor is fixed to zero.

## Resource distinction

For a chain, the original graph has O(m) cap and neighbor edges. A support
certificate can be expressed on these edges, irrespective of the number of
facets in the projected moment interface. With a feasible source there are no
negative cycles; nonnegative-cost circulations can be removed from an optimal
flow without worsening it. This does not make every optimal flow unique or
make its rational weights bounded-size.

Input rows, flow weights, potentials, moment coefficients, validation work
and retained histories must all be counted. For general graphs, charge the
actual edge count, not merely the number of endpoint audits. A bounded raw
separator is not by itself a bound on projected facets or on parametric
moment complexity.

This result separates two algorithmic gates:

1. Graph-form support with node-demand flow certificates, including active
   caps and a checked negative-cycle branch.
2. Complete moment-constrained membership and optimization, whose additional
   moment multipliers leave the pure difference-constraint class.

A successful support implementation would not alone close the second gate.

## Executable active-cap controls

Use s_j=1+(j mod 3), 0<=z_0<=1 and

    1/2<=z_(j+1)-z_j<=20,

together with EVERY owning cap. These increments cannot be treated as an
independent box: the relaxed corner z_j=1+20j already violates atom 2's cap.
For m=4,8,16 the capped U optima are 605/3, 1071/2 and 3461/3, whereas that
uncapped corner has U=227,1095,4731 respectively. The verified maximizing
flows use active source upper-cap rows, and their source witnesses attain
those caps.

Five objectives per size include U, V and mixed-sign endpoint/moment
combinations. Network flow costs agree with fifteen separately verified
source-LP primal/dual certificates; their chosen potentials need not agree.
The network runs use between 4 and 22 augmentations. Observed nonzero flow
counts are at most m. These are finite-workload measurements.

Six feasible moment queries are solved by imposing four observation
equalities on the source potentials. The source-LP output is checked directly.
A separate m=4 query has raw candidate (1,42,120,60): its endpoints obey their
caps and all gain-chain edges hold, but atom 2 exceeds 104. Its four
observations force that hidden value. An exact combination of its moment
equalities and the normalized atom-2 cap gives a separating inequality with
upper bound 104 and value 120 at the request. This is an algebraically
constructed Farkas control, not a general implemented infeasible-membership
solver. Finally, added edges z_1-z_0<=0 and z_0-z_1<=-1 supply a negative
cycle found by the network solver (node labels here denote the first two
atom potentials, not the anchor).

The producer uses SymPy only for source-LP comparison and feasible membership,
not inside the residual-network support solver. The independent verifier
imports neither solver nor producer. It checks expected source edges, raw
caps, charts, node balances, primal values, moment multipliers, and cycle
identities. It requires assertions enabled.

Files:

- `checkers/active_cap_network_support.py`
- `checkers/check_active_cap_moment_flows.py`
- `checkers/verify_active_cap_moment_flows.py`
- `results/active-cap-moment-flow-contract.json`
- `results/active-cap-moment-flows.json.gz`

    uv run --with sympy python research/grothendieck/checkers/check_active_cap_moment_flows.py
    python research/grothendieck/checkers/verify_active_cap_moment_flows.py

The expected source/evidence/query context is fixed by the research contract;
hashes bind versions, not observation authenticity. No fresh upstream source
admission or owning API change is claimed.

## Remaining gate

Support and its negative-cycle branch now have a specialized exact network
implementation. Full moment-constrained query completeness still needs a
separate implementation contract: the analytical source-LP formulation is
complete, but the current executable controls implement feasible membership
and one constructed separating proof, not an arbitrary moment-infeasibility
service or active-cap modular allocation optimizer.

In particular, do not feed arbitrary observable separators into the old lazy
algorithm and infer finite-cut termination. A controlled exact source-space
or network-plus-moment procedure must supply that missing progress argument.
The existing cap-redundant quadratic facet theorem remains unchanged.
