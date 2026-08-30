# Endpoint-evaluation rank lift

## Independent source operation

Every arithmetic endpoint displacement has the form

`Delta_(p,k)G = G(k log p)-G(0)`.

The endpoint operation itself is evaluation

`epsilon_0(G)=G(0)`.

It cannot be reconstructed from differences. On a finite set of translated
sample points, every displacement row annihilates the constant sample vector,
while endpoint evaluation returns one. The same finite values can be realized
by a compactly supported smooth interpolant, so the witness does not require a
globally constant adelic test function.

## Rank result

The `30x30` packet already reserved an endpoint boundary coordinate but had no
source incidence for it. Activating `epsilon_0` raises source-generated
boundary rank from four to five. No new internal valuation state is required.

A fake endpoint row formed by copying or combining prime-local rows adds no
rank. The new direction is global precisely because it evaluates the common
origin before prime translation.

## Remaining distinction

Endpoint evaluation is not endpoint totalization. We now possess the endpoint
port, but not the joint renormalized law that combines primitive, square,
connected tail, seam, endpoint, and the archimedean countercurrent.

Only one independent boundary type remains absent: the archimedean
countercurrent. After it is constructed, rank six will still be a necessary
condition, not proof that the six ports satisfy the required totalization and
losslessness identities.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_endpoint_evaluation_rank_lift.py
```
