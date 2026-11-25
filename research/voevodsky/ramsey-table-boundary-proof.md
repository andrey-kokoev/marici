# Exact boundary of the upper three-red cube cover

Paper proof. No proof assistant or catalogue assumption. This extends the [cube-difference note](ramsey-table-cube-differences.md); no Ramsey threshold is asserted.

Fix k ≥ 8. Write a row as (a,b,c) with 1 ≤ a, b ≥ a+2, c ≥ b+2, c ≤ k, in lexicographic order. Reversal sends (a,b,c) to (k+1−c,k+1−b,k+1−a). The mirror algorithm emits each front row into the upper half, consuming the current back only on a reversal match; a lone self-reversing row is a center instead.

## 1. Identify the upper half

The last five rows in descending lexicographic order and their unique mirrors are:

```
(k−4,k−2,k)     ↔ (1,3,5)
(k−5,k−2,k)     ↔ (1,3,6)
(k−5,k−3,k)     ↔ (1,4,6)
(k−5,k−3,k−1)   ↔ (2,4,6)
(k−6,k−2,k)     ↔ (1,3,7)
```

These follow by taking the largest possible first coordinate and, for each, the largest remaining coordinates. The first four mirrors occur in increasing front order, all strictly before the fifth back row (also at k=8). The fifth mirror has already been consumed, since (1,3,7) precedes (2,4,6). No later match or self-reversing center is possible: the back stays put until the front consumes it. Exactly the last four rows were removed. Equivalently, the upper half consists of all and only the legal triples with a ≤ k−6.

## 2. An earliest-start classifier

A cube with starts (i,j,h) consists of all eight triples in {i,i+1} × {j,j+1} × {h,h+1}. Legality requires i ≥ 1, j ≥ i+3, h ≥ j+3, h ≤ k−1. Every legal cube is witnessed in the upper half: i ≤ k−7, so even its largest first coordinate i+1 is ≤ k−6.

For an upper row form

```
i = max(1,a−1)
j = max(b−1,i+3)
h = max(c−1,j+3).
```

By successive lower bounds every start containing the row is coordinatewise at least this triple. Conversely these starts work whenever j ≤ b, h ≤ c and h ≤ k−1 (i ≤ a is automatic). If any test fails, increasing a start cannot repair that upper bound. This gives either a concrete cube or an impossibility witness.

* j > b exactly when a=1,b=3: for a≥2 the term i+3 is a+2 ≤ b, and for a=1 it is 4.
* h > c exactly when i+6 > c: the other competing terms are c−1 and b+2 ≤ c. For a≥2 this means c=a+4, forcing b=a+2. For a=1 it means c≤6, giving only b=3 or (b,c)=(4,6).
* h > k−1 exactly when b=k−2 (so c=k): expand h=max(c−1,b+2,i+6). Both c−1 and i+6 are ≤ k−1 because i ≤ k−7; hence only b+2 can fail.

## 3. Boundary and count

The failures form these disjoint lists:

| Row | Parameters | Count |
|---|---|---:|
| (1,3,c) | 5 ≤ c ≤ k | k−4 |
| (1,4,6) | — | 1 |
| (a,a+2,a+4) | 2 ≤ a ≤ k−6 | k−7 |
| (a,k−2,k) | 1 ≤ a ≤ k−6 | k−6 |

In particular the tight triples in the third family end at most at k−2, not k. Summing gives **3k−16**. This proves both inclusions at every width k ≥ 8; the earlier enumeration was a control, not a premise.
