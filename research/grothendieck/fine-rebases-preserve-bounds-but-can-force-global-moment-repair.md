# Fine rebases preserve bounds but can force global moment repair

## Delivered result

A fixed-chart fine-rebase prototype now distinguishes inherited upper bounds,
retained support attainment, surviving source columns, and fresh global
allocation repair. It consumes an independently owner-authorized successor;
it does not select actual history from a source witness or cached proof.

The mathematical result has three parts:

1. Adding source edges preserves old flow upper bounds by zero extension.
   Source columns and witnesses must separately satisfy the new edges.
2. If every retained column in an optimal checkpoint survives, its compacted
   allocation certifies the old optimum by restriction plus attainment,
   without a new master solve.
3. Repair is not spatially local in general. One edge in the last block can
   force every block's allocation to change and require regeneration in an
   unchanged remote block.

There is nevertheless a useful AMORTIZED event bound for fixed-grid,
append-only source refinement and a fixed query: every repair-triggering
consistent update consumes at least one unit of a nonnegative integer
shortest-path potential. This bounds repair events, not per-repair work.

## 1. Declared source and authority boundary

The source is the existing active-cap chain family: t_j=s_j z_j,
s_j=1+(j mod 3), original caps 0<=t_j<=100+2j, z_0<=1 and

    1/2<=z_(j+1)-z_j<=20.

A fine operation appends one normalized difference row

    z_v-z_u<=w

to one declared block. The anchor denotes zero. Both endpoints must belong to
that block or be the anchor. Charts, node identities, block ownership, observer,
objective, public frames and block-local moment frames remain fixed. Original
rows are not overwritten or removed.

The implementation requires 6w integral, preserving the existing D=6 source
grid. The mathematical flow transfer holds for arbitrary rational w, but a
changing grid denominator is outside this implementation. Cross-block new
edges, chart changes and source widening require another adapter.

Bootstrap verifies a full initial query proof. Fine advancement requires an
external trusted-owner callback approving the exact retirement/session event,
expected predecessor, operation and reconstructed successor. The test owner
admits opaque process-local references to these statements. A candidate cannot
supply its own approval metadata or use another event's valid reference.

This is an explicit owner-admission assumption. It is NOT authentication of
physical observations, archive import, actual-history recovery, or integration
with the Nima/Voevodsky restoration vault. A restored relation authorized by
such an owning service could be an input to a future adapter; no existing
archive reference is accepted here merely by resemblance.

## 2. The dependency-exact transfer rules

Write a block's old constraints Mz<=w and its successor constraints as the old
rows followed by new rows. The chart and normalized variable order are fixed.

### Flow upper bounds

If f>=0 satisfies M^T f=q, append zeros on the new rows. Then

    M_new^T (f,0)=q,
    w_new^T (f,0)=w^T f.

Thus the old upper bound for the SAME priced functional remains valid on the
smaller block domain. The rebase verifier checks the exact row prefix,
objective, zero extension, node balances and bound value.

This does not make the bound optimal after refinement. The carried priced
witness may violate a new row. If that happens, the producer looks for an
admitted surviving column attaining the same bound. A surviving witness plus
the bound certifies attained support; otherwise the packet retains an UPPER
BOUND ONLY. Absence of a retained witness is not a proof of strict slack.

Nor does an old flow answer a different node-demand objective merely because
the graph is unchanged. Fresh allocation repair can change prices in every
block.

### Source columns

An old column is admissible in the successor exactly when it passes the added
rows in its owning block. Columns of unchanged blocks remain admitted. The
packet classifies every retained column as KEEP or DROP; the verifier
reconstructs that classification from the expected source graphs.

Passing source admission does not certify that an unchanged block's old
allocation remains compatible with new shared values. That is a global issue.

## 3. Fast paths with genuine semantic certificates

The retained checkpoint has at most five source columns per block and weights
preserving its current four-coordinate allocation.

If all those columns remain admitted and the predecessor query was optimal,
their mixtures remain admitted in each successor block. Shared endpoints and
local moments are unchanged. The verifier reconstructs the mixed source,
checks gluing and all retained frames, and checks the old attained objective.

The successor domain is a subset of the predecessor domain, so the old
certified optimal value remains an upper bound. The reconstructed source
attains it. This gives RETAINED_OPTIMUM with zero new master solves.

The old full source vector need not be reused: the compacted mixture may have
different hidden atoms. What matters is its actual successor admission and
attainment, not identity with a previous selected witness.

If the predecessor fixed query was already infeasible, append-only refinement
preserves that infeasibility. INHERITED_INCONSISTENCY needs no new optimization.
When the fixed query contains a public point pin, this is a statement about
that pinned slice, not automatically about the whole unpinned source domain.
No feasible allocation is claimed for an empty checkpoint.

These fast paths depend on the verified predecessor head. A serialized head
or candidate digest alone is not authority to assert the old optimum or
infeasibility. Standalone semantic replay starts from a fully verified initial
proof and checks every transition in sequence.

## 4. Repair when retained columns fail

If an optimal checkpoint loses columns, preserve all admitted survivors.
Every block lacking a seed gets a fresh zero-objective network query on its
successor graph.

- A checked negative cycle proves that local source graph empty and hence the
  whole fixed query infeasible.
- A feasible network potential supplies a replacement grid column.

Exhaustion of cached columns alone NEVER proves emptiness.

The exact network-priced master then searches shared endpoint values and local
moments with the complete successor graphs. Its ordinary source lifts,
pricing flows, Phase-I contradiction or optimality certificate are checked
against those graphs. A new exact compaction certificate bounds the retained
pool again.

The local flow transfers remain useful certified statements, but the current
implementation does not install them as a pricing cache inside the repair
optimizer. Fresh repair uses its normal network oracle. Nor does the rebase
checker skip all old arithmetic: it rechecks source admission and transferred
flows. Classification locality is not an unmeasured kernel-reuse claim.

## 5. Atomic publication

Under the wrapper lock, advancement:

1. checks the current opaque handle and independently expected predecessor;
2. reconstructs the append-only successor;
3. obtains the externally supplied owner authorization for that exact event
   and statement;
4. checks column classification, flow transfer and the selected fast-path or
   repair certificate;
5. publishes a fresh immutable head only after all checks succeed.

Failure leaves the complete old head usable and unchanged. Old handles fail
after successful publication. The initial handle accessor does not provide a
way to fetch later generations. There is no serialized-head import API.

The resulting capability is the verified fixed-query result under the new
fine relation. This wrapper does not grant archival re-exposure, arbitrary
objective changes, source-chart edits or actual-history reconstruction. It is
a trusted-process service, not a hostile-memory security boundary. Concurrency
is serialized by a lock; concurrent scheduling is not tested here.

## 6. A locality obstruction inside the owning chain family

Take an otherwise unrefined chain of length m, with objective U and no extra
moment frames. Append just

    z_(m-1)<=(m-1)/2

to the final block. Original lower bounds give

    z_0>=0,  z_(j+1)-z_j>=1/2,

so this one additional row forces EVERY atom to

    z_j=j/2.

Before that refinement, z_j=1+j/2 is an admitted source. Difference-constraint
sources are closed under coordinatewise maximum: for two feasible potentials,
the maximum also satisfies every difference row, anchor and cap. Since U has
strictly positive coefficients in normalized coordinates, any old U maximizer
must dominate that admitted baseline coordinatewise. Otherwise taking its
maximum with the baseline would improve U.

Thus the new optimum changes every source coordinate and every block's
allocation, although only the last block's graph changed. A repair strategy
that keeps all unchanged block allocations fixed cannot be complete.

The executable m=16 control uses four blocks. The refinement is owned by block
3. All old retained columns in block 0 have z_0=1, while the new global source
requires z_0=0. No convex combination of those old block-0 columns can supply
the new allocation. The fresh master actually generates columns in ALL FOUR
blocks, including the remote unchanged block 0.

This is semantic nonlocality and an obstruction for the explicit retained
column pool. It is not a universal computational lower bound against an
implicit formula describing many changed atoms at once.

## 7. A fixed-grid amortized repair-event bound

There is a stronger resource statement than the original all-grid dictionary
bound, provided the query and source chart stay fixed.

For a consistent block, let d(u,v) be its complete shortest-path distance.
It equals the maximum admitted z_v-z_u: shortest-path potentials from u attain
that difference, and translation fixes the anchor without changing rows.

Let C_u be the original normalized atom cap, with C_anchor=0. Then

    -C_u <= d(u,v) <= C_v.

Choose a fixed D such that all original and appended edge weights and the caps
have integral D-scalings. Here D=6. Define

    Phi_b = D * sum_(u!=v) (d(u,v)+C_u).

This is a nonnegative integer. Edge addition cannot increase any distance.
If a retained admitted column violates the new row z_v-z_u<=w, then

    w < d_old(u,v).

If the successor block is consistent,

    d_new(u,v) <= w < d_old(u,v),

so Phi_b decreases by at least one. A consistent self-loop cannot invalidate
a column; a negative self-loop belongs to the empty-source branch.

Every global REPAIRED transition in this protocol requires at least one
invalidated retained column; the rebase verifier enforces that condition. If none is invalidated, the old allocation
certifies the fast path. Therefore the number of repair events before local
inconsistency is at most sum_b Phi_b(initial). A first locally inconsistent
update can add one final event; thereafter the fixed query is empty and all
further refinements use inherited infeasibility.

For N_b nodes INCLUDING the anchor,

    Phi_b <= 2D*(N_b-1)*sum_u C_u.

Thus a valid overall event bound is

    1 + sum_b 2D*(N_b-1)*sum_u C_u.

For this fixed cap formula and D=6, it is polynomial in explicit block atom
counts and the global atom index range. With arbitrary binary-encoded caps or
a growing grid denominator, the same expression is a numerical-range bound,
not a polynomial bit-complexity claim.

This bound concerns repair EVENTS only. One event can regenerate columns
throughout the chain, and one master run can still have a very large finite
column/basis bound. Infinitely many redundant authorized refinements can also
accumulate history, graph rows, parsing work and authority records without
triggering a repair. No total-runtime or total-storage bound follows.

The runtime does not compute all-pairs closures. The checker computes Phi
separately as a proof/control metric. In the main plan it is

    23168 -> 23168 -> 23162 -> 21874 -> 18567 -> 18522 -> 18521.

Each of its four repair events strictly decreases Phi. The final decrease
requires no repair because the query was already infeasible.

## 8. Executable evidence

The m=8 two-block plan keeps objective U and performs six authorized updates:

| Added normalized row | Outcome | New master solves |
|---|---|---:|
| z_0<=1 | retained optimum 1071/2 | 0 |
| z_0<=1/2 | repaired optimum 534 | 4 |
| z_3<=10 | repaired optimum 795/2 | 6 |
| z_7<=7/2 | repaired optimum 27 | 5 |
| z_7<=3 | globally infeasible query | 2 |
| z_0<=1/3 | inherited infeasibility | 0 |

At z_3<=10, the unchanged RIGHT block must generate new columns. At z_7<=7/2,
the unchanged LEFT block must do so. The z_7<=3 update leaves each local graph
nonempty but makes their shared endpoint requirements incompatible; a global
master contradiction, not a fabricated local cycle, establishes infeasibility.

A separate z_0<=-1 update produces a checked local negative cycle. The four-block
remote-refinement control uses nine master solves and regenerates in every
block. All repaired main-plan answers agree with fresh cold-start proofs.

A further genuinely moment-coupled control keeps an active U+V frame and adds
z_5<=15 inside the five-atom right block. Atom 5 is not one of that block's
exposed endpoints. The U+V frame remains tight before and after refinement,
the optimum changes, and the unchanged left block generates new columns.
Repair uses ten master solves and agrees with an independently checked cold
answer.

A separate lower-bound control adds z_3>=71/2. It excludes the carried left
pricing witness, but a surviving column still attains the old flow bound.
Some cached columns are lost, and three master solves repair the allocation
while preserving the old global optimum 1071/2. The prototype's fast path is
conservative: losing cached columns does not imply losing an optimum, and it
can run a repair even when an old global witness still attains that optimum.

The hidden-atom row z_5<=15 is not determined even by the right block's four
observations.
For example, perturb its raw vector (13,28,45,16,34) by

    +/- (0,1,-129,128,0)/1000.

Both old sources obey the block graph and have identical endpoints, U and V,
but one satisfies t_5<=45 and the other violates it. Attaching the same admitted
left prefix gives two globally admitted sources with identical public moments
and both local allocations. The checker verifies this fiber distinction.
Thus preserving a coarse allocation or selected section is not, by itself,
a certificate of the new hidden fine predicate.

Fifty-five refusal controls cover self-asserted approval, foreign-event grants,
changed predecessors and operations, altered flow extensions, false column
classification, stale handles and grants, authority-free execution, and a
corrupted negative-cycle proof. They also reject discarded witnesses offered
as current support attainment and an unnecessary REPAIRED declaration when
no column was invalidated. Failed candidates preserve head equality.

The independent semantic replay imports no rebase producer or optimizer. It
shares the established source/master and compaction verification kernels,
checks the fixed expected workload rather than trusting candidate state labels,
and replays the full chain from its verified bootstrap. It does not pretend
to authenticate external owner grants: that behavior is exercised separately
by the live wrapper tests.

## 9. Retention and remaining limits

Nonempty repaired checkpoints again retain at most five admitted columns per
block. Flow records, dense zero extensions, fine-edge history, rational weights
and source graph access remain charged. Empty checkpoints may retain fewer
columns and have no feasible mixture weights.

Main-plan head encodings peak at 982 bytes; the remote successor head is 1,522
bytes; the coupled-frame successor is 1,361 bytes. These are JSON payload sizes,
not heap or total retained information. The test owner retains sixteen approval
records containing 7,094 bytes of
predecessor/operation/successor statements; opaque event/token objects and
Python overhead are additional. Full proof/cold-replay archives and shared
source code are separate. No history-selector bit or physical provenance is
claimed to be reconstructed by this experiment.

The two amortization boundaries remain important:

- bounded column retention does not bound per-repair global work;
- bounded repair-event count does not bound redundant-history or authority
  storage, or the bit size of certificates.

The next implementation frontier is broader successor schemas: changing grid
denominators, new separator-crossing edges, chart changes, or arbitrary
restored fine relations. They need explicit dependency and authority contracts,
not silent acceptance through this fixed-chart append-only interface. A separate
structural target is a useful per-repair column bound, especially for updates
preserving the path-plus-anchor graph: event amortization leaves that cost open.

## Reproduction

    python research/grothendieck/checkers/check_moment_fine_rebase.py
    python research/grothendieck/checkers/verify_moment_fine_rebase.py

Files:

- `checkers/moment_fine_rebase.py`
- `checkers/verify_moment_fine_rebase.py`
- `checkers/check_moment_fine_rebase.py`
- `results/moment-fine-rebase.json`

Related:

- `bounded-moment-column-checkpoints-preserve-allocations-not-whole-interfaces.md`
- `active-cap-moment-blocks-compose-by-finite-network-pricing.md`
- `../voevodsky/archive-authority-now-publishes-an-actual-fine-refined-successor.md`
- `../nima/capability-escalation-returns-verified-ambiguity-without-selecting-history.md`
