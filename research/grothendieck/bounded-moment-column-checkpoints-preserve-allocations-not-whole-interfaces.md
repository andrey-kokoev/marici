# Bounded moment-column checkpoints preserve allocations, not whole interfaces

## Delivered result

The active-cap moment master now supports bounded retained source columns and
verifier-owned reuse across public-frame refinements.

For B blocks with the fixed four-coordinate observer (two endpoints, U,V),
EVERY current convex allocation can be represented using at most **5B source
columns**, at most five per block. Exact compaction preserves the current local
allocations, hence all shared values and applicable linear frames. It does not
preserve the whole feasible interface in those columns.

A live checkpoint retains these columns and their weights, the complete
expected state, and at most one checked pricing result per block. Four tested
refinements agree with independent full replay and cold-start optimization.
Warm runs use 26 master solves versus 30 cold; one warm run is worse. Of 52
successor pricing proofs, 48 receive fresh local arithmetic and four reuse
checked results. One hit comes from the predecessor checkpoint and three from
earlier checks within the same candidate.

The complementary obstruction is explicit: six uniquely exposed source points
in the owning four-atom active-cap block show that no fixed five-source-column
dictionary represents its complete endpoint/moment image. The retained graph
and fresh pricing remain necessary.

## 1. What is fixed, and what can change

This continues the source and observer contract of
`active-cap-moment-blocks-compose-by-finite-network-pricing.md`: all original
caps remain, charts are s_j=1+(j mod 3), and normalized chain increments lie
in [1/2,20], with z_0<=1. Block intervals and global slopes r_j=128^-j remain
fixed during a session.

The query engine accepts global and block-local linear endpoint/moment frames.
The checkpoint's current transition API appends one GLOBAL public frame;
block-local frames, objective, source, chart, observer and decomposition are
fixed by bootstrap. It does not authorize source edits, chart joins, domain
widening or new hidden audits. Changed source premises require a new bootstrap.

The expected state and appended frame come from the owning caller. Candidate
proofs are checked against that reconstructed successor, not against their own
claimed history. Inputs outside the declared state/frame schema are refused.

## 2. Exact five-column compaction

For a block let y_i be the four-coordinate observation of admitted source
column z_i, and let lambda_i>=0, sum lambda_i=1, be its current master weights.
The retained allocation is

    y = sum_i lambda_i*y_i.

If more than five weights are positive, the vectors (1,y_i) are linearly
dependent. Find a rational nonzero mu with

    sum_i mu_i=0,  sum_i mu_i*y_i=0.

It has both positive and negative entries. Set

    theta=min_(mu_i>0) lambda_i/mu_i,
    lambda'_i=lambda_i-theta*mu_i.

The new weights remain nonnegative, preserve their sum and every observed
coordinate, and eliminate at least one positive weight. Repetition terminates
with at most five original source columns. No new source point, approximate
rounding or observer rescaling is needed.

The verifier does not replay this elimination algorithm. It independently
reconstructs raw endpoints and globally weighted moments from the selected
source columns, then checks positivity, per-block mass one, the five-column
bound and exact equality with the original certified allocation.

Basic master solutions often already have sparse positive support. Pruning
zero-weight generated columns is a substantial part of the workload's
compaction. A separate eight-positive-column control exercises actual affine
dependence elimination; the theorem does not depend on the solver returning
a basic point.

## 3. What compaction preserves

For a feasible query result, replacing each block mixture by its compacted
mixture preserves both shared endpoints and both local moments. Convexity
preserves each block's source caps and gain edges. Therefore the compacted
mixtures glue to an admitted source satisfying the same global and local
linear frames and attaining the same objective.

Hidden atom values can change. This is an interface-allocation certificate,
not identity of the entire previous source vector, a claim about the actual
source, or a bound on displacement in the original atom metric.

For an infeasible query, the last query-Phase-I master still has convex block
mixtures. Compaction preserves their local observations and violation amounts,
but they need not glue or satisfy the requested frames. No global source lift
is claimed in that case. The already verified negative source-bound combination
remains the certificate of the infeasible slice.

In either case the selected columns belong to the unchanged bare block graphs.
They remain valid seeds after another public frame is appended, even if their
old allocation violates that new frame. The new query-Phase-I master supplies
fresh allocation search and its own feasibility or inconsistency certificate.

## 4. Bounded warm state versus query completeness

The query engine now accepts explicit initial source columns. It checks their
source edges and grid admission; the independent verifier requires EXACTLY
the expected seed prefix, supplied by the live checkpoint. Any subsequent
positively priced addition must still be a new admitted source-grid column.

Compaction discards old generated columns but not the block graphs. Each new
query still has the previous finite-grid completeness argument. Its seed may
be smaller than the previously accumulated dictionary; omitted columns can be
regenerated by network pricing.

Thus retained columns are bounded BETWEEN queries. Columns and master matrices
can still grow during a query, and repeated refinements can regenerate the
same discarded columns. This is not a bound on cumulative generation work,
query-time memory, master pivots or transcript size.

The implementation restarts the exact restricted-master solve from the warm
column set. It does not preserve a simplex basis or claim never to restart
allocation search.

## 5. Verifier-owned local reuse

Bootstrap verifies the entire initial proof. The session issues an opaque
process-local handle and retains immutable encodings. A successor must present
the current handle and the exact expected predecessor. There is no serialized
checkpoint import API. Foreign handles, stale handles and serialized cache
claims cannot confer authority.

A reusable local pricing result binds:

- the verification-rule source-file epoch;
- global atom identities and their order;
- every chart scale and normalized graph edge, including caps;
- the EXACT normalized source-node objective;
- the complete pricing-certificate encoding;
- the previously checked potential and support value.

Both dependency bytes and proof bytes must match, not merely a candidate's
statement that a cache was checked. Changed objectives or changed proof bytes
trigger fresh checking. A changed rule epoch refuses reuse through the session.

The local premise is the BARE block graph. Retained moment frames reside in
the master, not in that graph. Consequently history need not enter the local
arithmetic key when graph and actual priced objective are unchanged. The
complete new history, objective pullback and all master rows are nevertheless
checked freshly before a local result can be used in the composed proof.

Fresh successor checks still include:

- source-column admission and exact expected seed identity;
- every restricted-master primal and dual certificate;
- actual current node objectives and pricing thresholds;
- pricing progress and terminal source-bound combinations;
- shared-value and moment accounting, local frames and source gluing;
- the new allocation-compaction certificate.

The producer still computes its network pricing answers. These cache hits save
VERIFICATION arithmetic, not network optimization calls. The default standalone
verifier continues to perform full local replay. The checkpoint callback is a
trusted in-process hook, never a packet-selected verifier.

Only the last checked pricing result per block is retained. During an advance,
the old cache and a staged successor cache can coexist. Publication occurs only
after global verification AND compaction checks succeed; rejection discards
staged results and leaves the old head intact. Session operations are locked.
The service is not a security boundary against code modifying its own memory
or replacing trusted functions.

## 6. Why five columns cannot replace the full interface

Consider the four-atom block. Write

    z_0=b,  z_1=b+d1,  z_2=b+d1+d2,  z_3=b+d1+d2+d3.

Take b in {0,1}, d3=1/2, and

    (d1,d2) in {(1/2,1/2),(20,1/2),(1/2,20)}.

These six distinct box corners all obey the owning caps and chain edges.
In particular z_2<=21.5<104/3, so the active-cap source contains them even
though other corners of the increment box are excluded.

For each corner, assign coefficient +1 to an increment selected at its upper
bound and -1 to an increment selected at its lower bound. The resulting linear
functional has that corner as its UNIQUE maximizer on the increment box.
Since the corner is admitted, it remains the unique maximizer on the capped
source subset.

For four atoms, the observation consisting of two endpoints and U,V is an
invertible linear map: after the endpoints are fixed, the two middle atoms
are determined by their sum and their two distinct weighted slopes. Each of
these exposing source functionals is therefore an observable objective. The
checker verifies all six network support certificates and objective pullbacks.

To attain a uniquely exposed source point as a convex mixture of admitted
columns, every positive-weight column must be that point. Hence any fixed
five-column set misses at least one of these six support answers.

This is a lower bound for a COMPLETE SOURCE-COLUMN representation, not for
affine section formulas. In this four-atom example the inverse observer itself
is affine; describing and recognizing its full domain is a separate task.

## 7. Workload and independent controls

The two-block m=8 plan appends an endpoint bound, a coupled U+V bound, a right
endpoint bound and finally an incompatible left endpoint bound. Cached
verification agrees with full replay, and warm optimization agrees with cold
optimization in status and, when feasible, exact value.

| Successor | Warm master solves | Cold master solves | Retained columns |
|---|---:|---:|---:|
| Left endpoint bound | 5 | 8 | 4 |
| Coupled moment bound | 11 | 12 | 4 |
| Right endpoint bound | 9 | 7 | 5 |
| Contradictory history | 1 | 3 | 4 |

There are 23 rejection controls covering foreign/serialized handles, stale
heads, changed predecessors, mismatched expected operations, altered local
flow proofs and invalid compaction weights. Failed candidates leave the FULL
previous checkpoint unchanged, including its local cache. Mutations of caller
state and returned snapshots do not change the retained state.

Across accepted successors:

- 26 fresh global master checks, versus 30 in the cold workloads;
- 52 presented pricing proofs;
- 48 fresh local arithmetic checks and four cache hits;
- one predecessor-cache hit and three within-candidate hits;
- at most five retained columns in this workload, below the 5B=10 bound;
- maximum encoded checkpoint payload of 2,667 bytes.

These are kernel/solve counts and serialized payload bytes, not wall-clock,
arithmetic-operation or Python heap bounds. Separate full replays, cold solves
and rejected attempts are comparison/adversarial work outside those accepted-
successor counters. Proof parsing, dependency encoding/comparison, chart/source
reconstruction, column checks, master checks and compaction checks remain
charged. Checkpoint payloads include the retained local proof encodings.

The checker archives whole cold/warm transcripts separately. Those archives
are not included in the bounded checkpoint payload, nor are shared code and
source-rule implementations. Rational mixture weights, current prices and the
full retained frame history can grow in bit size even when column count is
bounded. Original graph access remains available and charged.

## 8. Relation to the parallel lanes

This adopts the authority discipline of
`../nima/verified-checkpoints-reuse-local-arithmetic-without-trusting-cache-claims.md`;
it is a separate moment-master prototype, not an integration or replacement
of that service.

The scalar metric reduction and coarse-core/cap construction establish a
whole-domain approximate-section scale in their own family:

- `../voevodsky/the-full-atom-metric-reduces-to-a-scalar-envelope-band.md`
- `../nima/a-coarse-core-and-local-caps-give-the-cubic-scalar-band-upper-bound.md`

Our pointwise convex-allocation argument does not establish a continuous
section, a common domain partition, epsilon-closeness to previous fine
witnesses, or whole-domain coverage. The six-exposure control shows precisely
why a compact current allocation cannot be promoted to complete column access.

Likewise, the full two-cell section in
`../voevodsky/a-real-retired-domain-now-has-full-two-cell-section-coverage.md`
has genuine rank-one coverage implications. No analogous coverage statement
is inferred from this checkpoint's retained columns or its ability to answer
future queries through fresh source access.

## Reproduction and continuation

    python research/grothendieck/checkers/check_active_cap_moment_master.py
    python research/grothendieck/checkers/verify_active_cap_moment_master.py
    python research/grothendieck/checkers/check_moment_column_checkpoints.py

Implementation: `checkers/moment_column_checkpoints.py`.
Artifact: `results/moment-column-checkpoints.json`.
The full verifier now exposes importable verification functions; importing it
does not load archived tests or retain those test packets in session globals.

The new structural distinction is sharp: bounded current-allocation storage
and bounded local verification-cache entry counts coexist with unavoidable
future source regeneration. The next resource question is whether a declared
class of refinement histories controls that regeneration and certificate-bit
growth. No such amortized or polynomial bound is supplied here.
