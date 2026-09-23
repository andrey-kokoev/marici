# A symbolic tail interface answers queries without materializing all facets

## Result

The owning admitted two-moment tail family now has a generator-based query engine with independent exact verification. It supports linear support queries, point membership and persistent observable-halfspace refinement followed by optimization or inconsistency detection.

The base model stores the parameter m, not a facet table. Run-specific evidence is retained separately in immutable refinement states. The implementation therefore avoids compulsory materialization of the source polygon without pretending that the model determines which evidence a run accepted.

At m=1024 the exact original-coordinate polygon needs 2048 facets. The tested refined queries generate at most one additional separating source facet, beyond four initial support bounds. This is a workload result, not a uniform constant bound for arbitrary queries.

## 1. Source and representation

Use the owning family

    Z_m = {sum_j t_j (1,128^-j) : 0<=t_j<=100+2j}, m>=2.

The owning verifier freshly checks its all-m admission into the Chebyshev relaxation and the exact signed-kernel normalization. The runtime works in normalized coordinates (U,V). These faces are not claimed to be prime-realizable uncertainty sets.

The base description is a fixed program and m. It contains no arrays of caps, slopes, vertices or facets. The program evaluates

    C(k) = sum_(j<k) (100+2j) = k(k+99),
    W(k) = sum_(j<k) (100+2j)128^-j

using an exact finite arithmetic-geometric sum formula.

This is a representation choice, not a claim of constant-bit arithmetic. Exact W(k), query results and certificates can require growing numerators and denominators.

## 2. Support queries

For a direction a=(a_0,a_1), each source coordinate contributes

    (a_0+a_1*128^-j)t_j.

The coefficient is monotone in j. Its positive indices form a prefix, suffix, all indices or none. Binary search finds that interval; differences of C and W give its exact endpoint witness and support value.

The certificate identifies the positive interval, the resulting observable point and its objective. The source witness sets those coordinates to their caps and the remaining coordinates to zero. No polygon edges need to be constructed.

The search takes logarithmically many comparisons, but this is not a logarithmic bit-complexity or output-size claim.

## 3. Membership with a generative source lift

At fixed total U, the maximum V fills the largest slopes first. The minimum fills the smallest slopes first. Sorting is already supplied by the source generator.

If the greedy maximum fills k coordinates completely and a partial next coordinate, its mass and value are computed from C(k) and W(k). The minimum is obtained by complementing the maximum allocation at total C(m)-U.

Thus membership is exactly

    0<=U<=C(m),
    V_min(U)<=V<=V_max(U).

An exchange argument proves the extremal allocations. Convexly interpolating them supplies every value in between. The witness is a small structural description of two greedy profiles and their mixing parameter, not a stored m-coordinate vector.

The mixing parameter can itself have a large exact encoding. The witness is also only a feasible source point; it is not a declaration that this was the actual source, and does not authorize new atom-level queries.

For an outside point, the same calculation gives a violated source support inequality. Source-coordinate reads outside the declared two-observable language are rejected.

## 4. Persistent refinement and lazy certificates

A refinement state stores m and the complete tuple of accepted observable frames. Appending a frame creates a new state; earlier snapshots remain unchanged.

To maximize an observable linear functional:

1. Check whether its unrestricted source support witness satisfies all retained frames. If so, it already proves the constrained optimum.
2. Otherwise start with four source support bounds and all retained frames.
3. Optimize over this outer polygon.
4. If the candidate has a source lift, emit a primal/dual certificate.
5. Otherwise add its separating source facet and repeat.

Every added inequality holds throughout the source. Every returned witness satisfies all retained frames. A feasible outer optimum therefore supplies both a true source lower witness and a matching upper certificate.

An empty outer polygon yields an exact Farkas contradiction. The dual uses at most two nonzero multipliers; the contradiction uses at most three. The independent verifier checks these identities rather than trusting an optimizer result.

Every generated separating facet excludes the current candidate and cannot duplicate an existing inequality. There are at most 2m such source facets, giving a finite termination bound. Arbitrary queries may nevertheless require many of them. Query work and accumulated evidence are not uniformly bounded.

## 5. Why the original run timed out

The first implementation tried to recover a known support optimum by repeatedly selecting an outer vertex. For a control retaining only V>=75, it chose a sequence of tied outer optima that generated all m upper facets.

This was not a missing source constraint or an incorrect certificate. It was avoidable work: the generator had already supplied an unrestricted maximizing source point satisfying the frame.

The implementation now checks that witness first and emits its exact support certificate when valid. The formerly timed-out controls finish without constructing the facet chain. This optimization does not weaken any query or omit evidence.

## 6. Exact controls

The producer checks:

- 118 support queries;
- 310 membership queries;
- 48 persistent refinement queries;
- 16 deliberate reset-history controls;
- m=2,3,4,8,16,64,256,1024.

At the owning finite replays, answers are compared with the already materialized exact polygons, including every exported facet omission witness and edge endpoint.

Persistent controls include:

    U<=50; U>=25; V>=75

and

    U<=50; V<=U/2; V>=30.

Both complete histories are inconsistent. Keeping only the final frame is feasible. This tests that the engine refines one accumulated relation rather than reopens the original source after each observation.

The independent verifier imports neither the engine nor an optimizer. It independently sums the source generators, verifies support signs and bounds, reconstructs source-lift identities, checks all primal/dual and Farkas packets, and ensures every declared prior frame occurs in the query certificate. Corrupted support values, source lifts, duals and dropped frames are rejected.

The largest exported exact rational has 7181 bits. That cost is recorded rather than hidden behind the small number of observable coordinates.

## 7. Structural meaning and limits

This is a positive representation-aware synthesis result:

    shared admitted generator
      + run-specific retained frames
      + query-specific witness or separator.

The full residual polygon need not be the persistent representation. Its unavoidable facet growth does not prevent exact queries through a different representation class.

But none of the storage obstructions disappears:

- the source generator does not encode which frames a run accepted;
- saturation does not make those visible-image restrictions free;
- hidden source-fiber restrictions cannot be recovered from a selected lift;
- changing observer closures is not interchangeable with exact conjunction;
- a short program does not promise short answers or cheap queries.

The engine assumes truthful frame semantics and faithful retention from a known initial state. It does not authenticate frames or detect an unreported earlier history supplied by an external caller. The immutable refinement API prevents accidental mutation of its own snapshots, not arbitrary tampering or omitted initialization.

No actual-prime, full-tail midpoint, or physical action-authorization claim is made.

## Reproduction

    uv run --with python-flint python research/grothendieck/checkers/verify_two_moment_tail_complexity.py
    python research/nima/checkers/check_symbolic_tail_interface.py
    python research/nima/checkers/verify_symbolic_tail_interface.py

Artifacts:

- `research/nima/results/symbolic-tail-interface-contract.json`
- `research/nima/results/symbolic-tail-interface-packet.json.gz`
- `research/nima/results/symbolic-tail-interface.json`
- `research/nima/results/symbolic-tail-interface-verification.json`
