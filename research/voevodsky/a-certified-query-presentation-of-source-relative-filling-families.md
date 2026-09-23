# A certified query presentation of source-relative filling families

## Purpose

Unify the working symbolic tail interface with the storage and witness-comparison obstructions. This is a representation theorem and implementation contract, not another counterexample. It separates denotation, certified access, cost and witness identity.

## 1. Denotation: what a state represents

Fix m>=2, the source box

    P_m=product_(0<=j<m) [0,100+2j],
    L_m(x)=(sum x_j, sum 128^-j x_j),
    Z_m=L_m(P_m).

A runtime state is m together with a complete finite tuple E of accepted rational observable halfspaces (a_i,b_i). Define

    Q_E={y in Z_m : a_i dot y<=b_i for every retained i},
    C_E=P_m intersect L_m^-1(Q_E),
    W_E(y)={x in C_E : L_m(x)=y}.

The state denotes this entire family, not a selected source point or a facet list. The shared generator program, its interpretation and the source admission are part of the contract. This is the analytical relaxation, not a prime-realizable source claim.

The carrier is saturated relative to L_m by construction. Every witness in a visible fiber is either admitted or excluded together. Hidden source-coordinate restrictions are outside this representation class unless explicitly added to the state language.

Appending a frame intersects Q_E with its halfspace. It does not change the ambient generator or reopen any earlier restriction. Different ordered tuples may denote the same carrier; syntactic history and semantic equality are distinct.

## 2. Certified access theorem

For this source family and finite rational E, the state supports exact rational membership and linear optimization without requiring a persistent facet representation of Q_E.

### Membership

A point belongs to Q_E iff it satisfies every frame and belongs to Z_m. A failed frame itself certifies exclusion. Otherwise the generator membership method returns either an admitted source lift or a source support inequality separating the point. `Generator.member` implements base membership. The subsequent state-bound extension now exposes `RetainedInterface.member`, adding retained-frame checks and state/query binding; see `research/nima/state-relative-query-certificates-require-an-independent-expected-history.md`.

Greedy maximum and minimum profiles at fixed U give the exact allowed V interval. Their convex interpolation is a compactly described feasible witness. It selects one witness per nonempty observable fiber, not all witnesses and not the actual unknown source.

### Optimization or inconsistency

For a rational objective a, a feasible returned point y with an admitted lift gives a lower bound a dot y. Nonnegative multipliers on verified source supports and retained frames give a matching upper bound. Equality proves exact optimality over Q_E.

A nonnegative combination of these same valid inequalities with zero normal and negative upper bound proves Q_E empty. This is the Farkas branch; no witness is returned.

The lazy engine begins with a bounded source-support rectangle and all frames. An outer optimum either has a source lift or generates a violated source facet. Each new facet excludes the current point and differs from existing rows. The base polygon has 2m facets, so at most 2m such additions occur. The bounded rational outer polytope is either empty or has an optimizing vertex, including lower-dimensional nonempty cases. Exact planar enumeration and the primal/dual checks therefore supply termination and correctness in this family.

The feasible-unrestricted-support fast path is a proof-preserving optimization: its source witness already satisfies E, and its global support bound is also a bound on Q_E.

This is not a general theorem that any compact source generator has an efficient separation or optimization oracle. The ordered slopes, exact support sums, greedy membership argument and finite facet bound are substantive hypotheses of this instance.

## 3. Implementation and verification binding

Implementation: `research/nima/checkers/check_symbolic_tail_interface.py`.

- `Generator`: shared m-indexed source rules, support and base membership.
- `RetainedInterface.refine`: immutable append of accepted observable frames.
- `RetainedInterface.maximize` / `lazy_maximize`: exact refined optimization or inconsistency.

Independent replay: `research/nima/checkers/verify_symbolic_tail_interface.py`.

- `support`: independently sums generators and checks support signs and values.
- `lift`: checks greedy-profile source-lift identities and caps.
- `check_lp`: checks every expected frame occurs, validates source rows and nonnegative dual/Farkas identities, and checks the primal witness when present.

A fresh replay for this synthesis passed 118 support queries, 310 membership queries, 48 persistent queries and 16 reset-history controls, rejecting four deliberate corruptions, through m=1024. This is replay of the existing packet, not a fresh producer run or a fresh upstream analytical-admission proof.

For arbitrary callers, `check_lp` must receive the expected history from an independently trusted state. Checking a packet against a history supplied by the same untrusted packet does not prove that prior evidence was retained. The shipped replay supplies its known expected traces independently. Source hashes bind artifact versions; they do not authenticate external frame truth or unknown histories.

## 4. Cost ledger: storage, work, proof and accuracy

| Account | What must be counted | Established bound or limitation |
| --- | --- | --- |
| Persistent source presentation | Fixed generator program, m, source/semantic binding | No persistent array of source facets, vertices, caps or slopes in the runtime generator; encoding m still costs bits |
| Persistent run-specific evidence | Every retained rational frame and its coefficients | Grows with E; the current implementation retains the full tuple, including redundant frames |
| Query and verification work | Rational arithmetic, support comparisons, outer vertex enumeration, validation | At most 2m new source facets per lazy query; this is not a bound on total arithmetic operations or bit complexity; independent verification enumerates source generators |
| Returned proof | Source-lift description, source supports, retained frames, dual/Farkas data and cut trace | At most two nonzero optimum multipliers or three contradiction multipliers, but the full packet may contain all frames and up to 4+|E|+2m rows; rational encodings may grow |

Accuracy is a separate account: declare input error sets, output tolerances and source/observation norms. The unpinned greedy section is within an additive one of optimal global Lipschitz conditioning, with growth Theta(m^2) in the frozen norms. Exact audit pins can instead leave a two-coordinate inverse with constant 2*128^(m-1)/127. These are reconstruction-sensitivity bounds, not operation counts. Exponentially small absolute error can require only linearly growing fractional precision bits.

Immutable snapshots retain history; they are not a free-storage mechanism. Cumulative storage across saved snapshots, verification caches and exported packets must also be charged when those are retained.

The program represents a family with a small description. Exact numerical parameters, outputs and proofs do not inherit a constant-bit bound. Sparse dual support is not the same thing as a constant-size certificate packet.

## 5. Which lower bounds survive?

- Original-coordinate facet lower bounds constrain explicit irredundant halfspace presentations. They do not rule out a generator plus certified query algorithm.
- Distinct run-specific visible images require distinguishable state information whenever some admitted query distinguishes them. The shared source program does not identify E or Q_E. No claim is made that every syntactically distinct history is semantically necessary.
- Hidden restrictions within an observable fiber cannot be reconstructed from a saturation-based state or from a chosen feasibility lift.
- Large exact numbers remain large even when their structural description uses a few fields.
- Successful finite workloads do not establish constant worst-case query work. A query may temporarily discover many source facets even though they were not stored persistently.

Every lower bound should name the represented object, admissible representation class, query language, exactness standard and cost account. A bound on facets is not automatically a bound on programs, state bits, arithmetic work or proof length.

## 6. Witness identity is an additional contract

None of the access theorem requires a canonical actual source, bijections between fibers, or coherent comparison maps.

For ordinary Euclidean fiber homotopy and only the two declared observables, the greedy section is continuous and its straight-line contraction is natural under visible restrictions. This is a separate positive theorem: `the-symbolic-tail-section-contracts-fibers-naturally-under-visible-refinement.md`.

Adding raw-coordinate audits changes the obligations. Query-preserving transport must preserve the audit map on each witness. Nonempty contractible fibers may have disjoint audit ranges, precluding any such map. Even equality of ranges is generally insufficient without compatible structure within the audit fibers. Grothendieck's complete coordinate (S,F,h) product slice supplies a special case with unique coherent audit-preserving transport.

Thus extending query access, selecting feasible witnesses, and constructing witness interchange are separate engineering and mathematical tasks. A certified query presentation need not promise all three.

## 7. Schema, evidence and uncertainty: the extended contract

A proposed extended state has semantic components (source binding, m, observation schema A, retained evidence E). The schema declares L_A(x)=(U,V,(x_j)_(j in A)); it does not supply the values of those audits. Supplied values, bounds and measurement error sets belong to E. A query declares its quantifier and precision semantics. A comparison request additionally declares the allowed witness identity. These fields must not be inferred from whichever witness an earlier query happened to return.

Its denotation remains

    C_(A,E)={x in P_m : E(L_A(x))}.

The state represents possibilities. A certificate is evidence about those possibilities, not a replacement for them.

### Three distinct update operations

1. Evidence refinement under fixed A intersects the admitted set. The same fiber contraction restricts naturally.
2. Schema extension A subset B exposes finer coordinates. Old evidence is pulled back along the projection L_B->L_A; adding a schema alone supplies no new values and changes no source possibilities. New audit evidence then restricts them. The owning selectors obey R_A R_B=R_A, but generally not R_B R_A=R_B. Reading new values from R_A(x) is not observation of x.
3. Changing measurement precision changes the error set being asserted. Narrowing it requires justified new evidence; widening it is a deliberate weakening, not ordinary conjunction or silent history replacement.

Nima's conditional section implements exact supplied pins by subtracting their moment contributions and using the residual box. It preserves the enlarged observation and rejects empty common audit fibers. It is not a general optimizer for all enlarged-schema predicates or noisy pins.

### Answer semantics for uncertain inputs

Interpret certified measurement error as constraints on possible sources, not as a request to invert a nominal point and call the result actual. For a declared predicate phi:

| Answer | Mathematical obligation | Example certificate |
| --- | --- | --- |
| INCONSISTENT | C is empty | Exact separating/Farkas proof |
| FORCED_TRUE | C is nonempty and every x in C satisfies phi | Feasible witness plus universal bound |
| FORCED_FALSE | C is nonempty and every x in C violates phi | Feasible witness plus strict separating bound |
| UNRESOLVED | Both truth values occur in C | Two admitted witnesses with opposite truth values |

For a closed linear threshold over a compact rational polytope, certified minimum and maximum suffice, with careful strictness at equality. An unresolved answer is successful certified query answering, not computational failure. Timeout or unsupported predicates are separate operational statuses and must not be reported as mathematical ambiguity.

The last-two-free-coordinate control derives the exact interior radius (epsilon_V+r_q epsilon_U)/(r_p-r_q) for a moment error box. This illustrates the contract; it does not implement all uncertainty languages.

### Capability status

| Capability | Current evidence |
| --- | --- |
| Two-observable support, base membership, retained-halfspace optimization | Owning engine and independent packet verifier |
| Conditional section and contraction with explicit exact atom pins | Owning audit-aware constructor and separate verifier |
| State-relative membership with trusted expected-history binding | Now exposed by the owning state-bound interface and independently replayed; expected context remains caller-supplied |
| General audit-conditioned optimization with arbitrary retained histories | Not established by the conditional section |
| Set-valued finite-precision threshold answers | Exact two-free-coordinate prototype and affine proof; no independent packet verifier yet |
| Audit-preserving interchange between arbitrary bases | Not promised; empty/incompatible audit fibers can prohibit it |

The global section is necessarily non-affine for m>=3. This obstructs strict affine interpolation preservation, not certified query access or ordinary convex homotopies.

## 8. Synthesis and next implementation gate

The working factorization is

    shared admitted source presentation
      + declared observation schema and query/accuracy semantics
      + faithfully retained carrier constraints
      + query-specific independently checkable certificate.

It presents a source-relative filling family without compulsory persistent boundary materialization. It does not eliminate evidence information, computation costs or identity obligations.

The previously identified state-relative membership gate is now implemented by the owning state-bound interface. The following requirements describe that gate rather than pending work. Bind each certificate to the source version, schema, immutable state and exact query (including any error set). The verifier must obtain the expected state independently of the answer packet; hashes alone do not authenticate evidence. Reuse the existing lift/support arithmetic and add frame checks. Acceptance tests should reject a certificate from another state, dropped prior frames, a schema mismatch and a newly asserted audit copied from an old representative without observational justification. The last issue requires provenance/admission controls, not arithmetic alone.

This synthesis did not implement that extension; the owning Nima work supplies it. The raw optimization method still does not acquire binding automatically: callers use the new certificate envelope API.

The next research result is `finite-separation-makes-certified-query-presentations-closed-under-refinement.md`: finite certified separation plus exact bounded LP gives closure under retained rational halfspaces. For enlarged linear audit schemas, rational-polytope closure exists mathematically, but a verified higher-dimensional separation/optimization backend remains a distinct implementation obligation.

## Reproduction

    python research/nima/checkers/verify_symbolic_tail_interface.py

Existing replay artifact: `research/nima/results/symbolic-tail-interface-verification.json`.

Related source notes:

- `research/nima/a-symbolic-tail-interface-answers-queries-without-materializing-all-facets.md`
- `research/nima/symbolic-query-correctness-does-not-supply-witness-interchange.md`
- `research/grothendieck/query-preserving-filling-transport-needs-a-common-audit-fiber.md`
