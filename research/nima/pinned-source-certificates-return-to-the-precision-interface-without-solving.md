# Pinned source certificates return to the precision interface without solving

## Delivered reverse direction

The full-schema bridge now has an algebraic reverse translator. Independent replay verifies 94 pairs, or 188 objective-proof translations, without optimizer calls. Six statement/proof/ledger mutations are rejected.

This closes the missing certificate direction on a deliberately restricted domain. It does not infer a general inverse translator merely from source-set equality.

## Exact operational domain

The expected origin is a valid two-free precision state. The source certificate must use EXACTLY its existing full-schema translation:

- the same source box and ordered full atom schema;
- the same ordered pin equalities and translated evidence;
- the explicit source-cap row convention;
- maximization of either minus or plus the first free atom;
- a checked feasible optimum with explicit nonnegative dual weights, or an EMPTY certificate with explicit nonnegative Farkas weights.

The translator verifies the input against that independently supplied expected statement before translating. Extra rows, reordered encodings, membership-query proofs, arbitrary objectives and other semantically equivalent presentations are outside this contract unless first certified and converted into the expected format.

Two opposite objective proofs produce one specialized threshold packet. A general objective packet does not itself bind the threshold or the origin's source-binding string: those are supplied by the caller's expected precision statement and checked in the output envelope.

## Row substitution and constant slack

Substitute every exact pin in each source row.

- Free-atom caps become the four residual cap rows.
- Retained evidence becomes its existing planar row.
- Pin equalities become 0<=0.
- A pinned lower cap becomes 0<=h_k.
- A pinned upper cap becomes 0<=b_k-h_k.

Let C be the weighted sum of the last two kinds of constant bounds. Since the pins obey their caps and weights are nonnegative, C>=0. Dropping these rows preserves the residual normal and changes the combined bound from B to B-C.

For an optimum, the projected source point is feasible for every residual row. Its objective equals the original bound B. The residual combination would otherwise give an upper bound B-C strictly below that attained value. Hence C=0. Removing constant rows therefore preserves exact optimality, not merely a weaker bound.

For a Farkas proof, the original normal is zero and B<0. After substitution and removal, the residual normal is zero and B-C<=B<0. The contradiction remains valid, even when C is strictly positive.

This accounts for arbitrary admitted nonnegative weights in the declared proof format, not only the sparse rays emitted by one solver. There is no need to renormalize an empty proof to upper bound -1; the specialized verifier accepts any strictly negative bound.

## Witnesses and four-valued answers

A feasible source witness projects to its two free coordinates. All pin values and retained constraints remain available through the expected state. The translated minimum and maximum determine FORCED_TRUE, FORCED_FALSE or UNRESOLVED with the existing weak-threshold equality rules.

Two checked empty objective packets yield INCONSISTENT. The reverse API intentionally requires a pair; accepting a single empty certificate would be a separate convenience interface, not a mathematical necessity.

Opposite translations need not recover original packet syntax or a solver's chosen witness. They preserve the covered statements, certified extrema and audit answers.

## Verification controls

The replay uses all 46 states from the earlier full-schema bridge in two variants:

- both algebraically transported source proofs;
- independently verified simplex proofs, using the disclosed transported fallback for the one failed simplex proposal.

Two additional variants exercise proof forms beyond normal solver output:

- nonzero cycles on opposite pin-equality rows;
- Farkas combinations with deliberately positive pinned-cap constant slack.

The independent verifier imports neither the reverse translator nor an optimizer. It checks both certificate endpoints, independently reconstructs row correspondence and the constant-slack ledger, and verifies the projected primal and transferred weights.

## Resource accounts

No solver is invoked by either algebraic direction. This does not make translation or verification free.

For K input nonzero terms and m source coordinates, the reverse row-weight map scans K terms and retains at most K nonzero terms; pin lookup and source-point projection require the source context. Constant accounting performs rational additions and multiplications, whose bit costs depend on the actual encodings. The implementation's statement construction and certificate validation also materialize source-space rows and perform the existing dense arithmetic checks; their cost is separate from this sparse mapping bound.

The forward map can add one pin-equality cancellation term per pinned atom. The reverse map removes those terms and constant cap rows. These directional bounds do not establish equal packet sizes or equal verification work.

Observed reverse-workload maxima:

| Encoding/account | Maximum |
| --- | ---: |
| Input pair, compact JSON including both statements | 3,125 bytes |
| Output audit packet, compact JSON including statement | 1,189 bytes |
| Input nonzero terms per objective | 8 |
| Output nonzero terms per objective | 3 |

The byte comparison includes packaging differences: two objective packets become one audit packet. It is not an information-theoretic compression theorem or permission to discard an input archive. Rational bit complexity and persistent evidence remain charged independently.

## Reproduction

    python research/nima/checkers/check_reverse_two_free_certificates.py
    python research/nima/checkers/verify_reverse_two_free_certificates.py

Implementation: `research/nima/checkers/reverse_two_free_certificates.py`.

Artifacts: `research/nima/results/reverse-two-free*`.

The result supplies bidirectional algebraic certificate transfer for the translated pinned subfamily and its covered objectives. It does not establish audit retirement, continuation equivalence after forgetting, arbitrary witness interchange, observation authentication, or a fresh upstream source-admission proof.
