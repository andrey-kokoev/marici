# Shared six-arrow seed: record-instruction experiment, withdrawn as the requested count

The 11,371 figure below is **not an answer to the operator's arrow-count question**.
It introduced a different primitive convention. The original-convention source
execution and independent closed-return certificate give **7,128** for the
specified shared-seed two-body three-stage network; see
`shared-seed-original-arrow-count.v1.md`. Retain this experiment only as a record
of the mismatched counting method, not as a candidate mass count.

## Exact question and remaining distinction

The seed used here is the existing shared two-body seed
AB, BC, CA, AD, DB, BA on A,B,C,D. It is not the newer one-point geometric
source or the neutron rotational-seed packet. The construction is the supplied
area-packet lift producing two twelve-triangle bodies and a shared core.

We now have a complete replayable run of an explicitly declared **record
instruction grammar** from that supplied seed to geometry, modes and operators.
It has **11,371 executed configuration transitions** and **11,372 visited
configurations**, including the initial configuration.

This is one canonical construction run. It is NOT a count of every possible
arrow between every reachable configuration, an unrestricted minimal program,
or an identification of these instructions with the mass arrows. The latter
primitive-identity comparison remains missing. Do not quote 11,371 as a mass.

## What is supplied, rather than generated from six bare arrows

The contract `contracts/shared-seed-construction-trace.v1.json` retains:

- the four named objects and six directed seed edges;
- the fixed tetrahedral contrast frame and scale;
- the exterior-square area action det(R)R;
- the cyclic coefficient character (1,omega,omega^2);
- the local-selection, frame-average and collective-feedback prescriptions;
- the positive cell schedule and lazy comparison rule.

These are mathematical construction inputs. The count does not prove that the
six arrows alone derive the metric, representation or coefficient rules.
The initial six seed arrows are not six executed steps and are not added to the
trace total. No object or unit-registration steps are silently inferred.

## Primitive level and retention

A configuration contains every previously appended typed result. One transition
executes one listed instruction and appends its result. An instruction may
compute a vector, matrix, cell or coefficient using exact arithmetic. Scalar
arithmetic inside it is not separately counted. Thus this is a fully specified
record-level cost, not a claim of source-authorized microscopic primitives.

All 72 executed generator products are retained, including those whose value
is an already discovered permutation. All evaluated transport/feedback entries
and all comparison matrix positions are retained, including zero results.
Local off-block zeros are represented by the declared sparse locality rule and
are not individually evaluated. Internal cell records remain after exposed
boundary faces cancel.

| Construction stage | Record transitions |
|---|---:|
| Frame, generators, identity, products, group and area actions | 105 |
| Point/centroid geometry, triangles, positive cells and their attachment | 80 |
| Mode vectors and the collective norm | 25 |
| Local, transport and feedback coefficient evaluation | 10,584 |
| Comparison graph and its matrix entries | 577 |
| **Total** | **11,371** |

These are append-only configurations linked by exact replay dependencies and a
hash chain. Numeric equality of two result values does not erase either
execution. Verification calculations, serialization, sorting and bookkeeping
are not additional construction instructions in this grammar.

## The independently recovered endpoint counts

The executor does not read a target arrow list. It derives the permutations,
coordinates, modes and matrices, and only then compares with the historical
endpoint audit. The result reproduces:

- dense coefficient-transfer arrows: 216+1728+5184 = **7128**;
- their body partition: 1836+1836+3456;
- retained directed geometric edges: **84**;
- sparse comparison entries: **144**, including 24 loops;
- positive geometric cells: **16**; union volume 4;
- one coupled identity line.

There are 3,456 evaluated zero dense coefficients and 432 evaluated zero
comparison coefficients. These are executed computations, not nonzero
coefficient-transfer arrows. In particular **11,371 is not 7,128 plus a newly
identified physical rest-energy contribution**.

Exact block multiplication checks GL=LG=N. Every cell attachment rechecks a
closed oriented surface. Replay recomputes each result from prior records;
it does not merely trust hashes or copied results. A separate canonical-run
comparison rejects a valid but incomplete prefix as a full construction.

## Why this is not yet the requested mass-arrow total

The original 1836 convention counts nonzero maps between typed staged ports.
The new trace counts record-producing instructions between accumulated
construction configurations. They are different endpoint types and different
notions of a primitive step. Also, one execution path is not the whole graph of
admissible configuration transitions.

For example, replacing the 5,184 scalar transport-entry instructions with one
bulk matrix instruction would preserve the completed matrix but reduce this
trace count by 5,183. That is outside the frozen grammar, but demonstrates why
its instruction count cannot become an invariant mass without the missing
source-level primitive identification. An arithmetic-level refinement would
instead increase the count.

The required next evidence is the actual source definition of a mass-counted
configuration and primitive arrow, including whether the reader counts one
execution, distinct endpoints, occurrences, or the whole admissible relation.
Then compile the same construction into that alphabet and prove the comparison.
The present trace supplies a retained dependency record for doing that; it does
not replace the definition with a convenient programming convention.

## Reproduction

    python research/voevodsky/checkers/check_shared_seed_construction_trace.py
    python research/voevodsky/checkers/test_shared_seed_construction_trace.py

Artifacts:

- `results/shared_seed_construction_trace.v1.json`: full instruction/dependency/result chain;
- `results/shared_seed_construction_count.v1.json`: counts, endpoint controls and scope;
- seven regression tests covering replay, truncation, bad dependencies, removed
  seed exchange, retained zeros/duplicates and tampering even after rehashing.

Nima's sources are imported read-only; their main routines are not invoked and
none of their artifacts is rewritten. Source hashes are retained. No existing
mass or reaggregation outcome is changed by this trace.
