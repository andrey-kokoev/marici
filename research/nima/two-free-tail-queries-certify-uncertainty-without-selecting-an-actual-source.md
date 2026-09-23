# Two-free tail queries certify uncertainty without selecting an actual source

## Result

A separate source-space backend now answers finite-precision atom-threshold queries with independently checkable certificates. It retains every measurement box and linear refinement rather than inverting a nominal point and declaring that lift actual.

The workload passes 79 certificates through m=1024. Independent replay rejects ten corrupted certificates and three stale-snapshot replays. Seven malformed inputs are rejected by the constructor/query boundary.

## Frozen representation

Fix two free atom indices i<j. All other atom values are supplied exactly, within the owning bounds 0<=t_k<=100+2k. Let x=t_i and y=t_j. The state contains:

- the source binding and m;
- the two free indices and every exact pin;
- the full ordered evidence history.

The observation normalization is unchanged:

    U = U_pins + x+y,
    V = V_pins + 128^-i x + 128^-j y.

Accepted evidence is either a closed linear halfspace in (x,y), or a coordinatewise error box on the full (U,V). A measurement box produces four source-space inequalities after subtracting the exact pin contributions. The four source-cap rows are always present.

Pins are supplied hypotheses or observations, not inferred from an earlier chosen witness. Missing, duplicate and out-of-cap pins are invalid declarations. Measurements incompatible with valid pins instead produce an INCONSISTENT possibility set and a Farkas certificate.

## Refinement and completeness

`TwoFreeTail.measure(center,error)` and `refine(normal,upper)` return new immutable states. Their evidence is appended, never substituted. In particular, appending a wider error box does not remove an earlier tighter measurement.

For every finite accepted history the residual source is a bounded rational planar polyhedron. The existing exact planar machinery enumerates feasible intersections of pairs of boundary lines. Every nonempty bounded polyhedron has an optimizing vertex, including line and singleton cases. An empty system receives a nonnegative Farkas combination.

Thus this backend is complete under its declared finite closed linear refinements. No joint-image separator or unproved finite-cut dictionary is required: the source-space constraints are explicit. This does not establish a backend for arbitrary variable audit schemas.

With N rows, pair enumeration and feasibility checks use O(N^3) rational operations; the existing Farkas search also enumerates up to triples. This is not a polynomial bit-complexity claim. Exact pins require retained information growing with m, and rational encodings can grow substantially.

## Four mathematical answers

The query is x<=h, where x is the first declared free atom. The backend certifies both extrema whenever the feasible set is nonempty:

| Status | Obligation |
| --- | --- |
| FORCED_TRUE | maximum x <= h |
| FORCED_FALSE | minimum x > h |
| UNRESOLVED | minimum x <= h < maximum x |
| INCONSISTENT | the feasible set is empty |

Each extremum has an admitted residual source point and a matching nonnegative dual bound. Reattaching the exact pins gives a full source witness. In the unresolved branch the two extrema supply witnesses with opposite audit truth values.

The minimum is certified by maximizing -x. A Farkas certificate has zero combined normal and strictly negative combined upper bound. No witness accompanies the empty branch.

Threshold equality is intentional: equality at the maximum forces truth; equality only at the minimum does not force falsehood. Unsupported inputs raise errors; computational failure is not converted to UNRESOLVED.

## Independent binding and verification

`verify_two_free_tail_queries.verify(expected_state, expected_query, packet)` takes the expected statement separately. It imports neither the backend nor the LP solver. It reconstructs all cap and evidence inequalities from the expected state, checks the envelope, and checks primal feasibility and dual/Farkas identities using rational arithmetic.

The complete free-index choice, exact pins, measurement centers and errors, retained halfspaces, source binding and audit threshold are part of the statement. Digests bind these data but do not authenticate their origin. A caller must not obtain its expected history from the answer packet itself.

The test contract freezes expected requests and analytical answers before executing the queries. Replaying a valid old certificate against a refined history fails even when the reported truth value happens to agree.

## Decisive controls

For m=3,4,8,16,64,1024, the tests compare free pairs {0,m-1} and {m-2,m-1} under identical absolute moment error bounds. At a source center x=20,y=30 and threshold 21, the worst pair crosses from forced truth to ambiguity as weighted-moment error exceeds its slope gap. The best pair still forces truth at the tested larger error. Nothing rescales V.

Additional controls cover simultaneous U/V errors, exact observations, forced falsehood and both threshold equalities.

Cap clipping is genuinely joint. With x=20,y=0 at an exact total, unconstrained inversion gives x in [19,21], but y>=0 cuts the maximum to 20. Clipping x alone would give the wrong audit answer. A corresponding upper-y-cap control cuts the minimum instead.

The history controls include a narrow box followed by a wider box, a retained linear audit bound, a zero-normal contradictory row, and inconsistent full moments. Line, singleton and m=2/no-pin cases are also checked.

## API example

With the checker directory on the import path:

```python
from fractions import Fraction as Q
from two_free_tail_queries import TwoFreeTail
from verify_two_free_tail_queries import verify

state = TwoFreeTail(3, (1, 2), ((0, 1),), "caller-owned-source-context")
gap = Q(1, 128) - Q(1, 16384)
state = state.measure((51, 1 + Q(20, 128) + Q(30, 16384)), (0, gap))
expected_state = state.descriptor()
expected_query = {"kind": "free-atom-threshold", "atom": 1,
                  "relation": "<=", "threshold": "21"}
packet = state.audit(21)
assert verify(expected_state, expected_query, packet) == "FORCED_TRUE"
```

## Reproduction and scope

    python research/nima/checkers/check_two_free_tail_queries.py
    python research/nima/checkers/verify_two_free_tail_queries.py

Artifacts: `research/nima/results/two-free-tail-query*`.

The existing two-observable interface is unchanged. This extension does not cover noisy pins, authenticate measurement acquisition, infer an actual source, authorize transport, or change upstream analytical-admission status. Source-report hashes bind versions; this run is not a fresh upstream source-admission proof. The independent research verifier refuses execution with Python assertions disabled.
