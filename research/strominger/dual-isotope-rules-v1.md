# Direction-indexed reversed isotope rules

## Experiment

Extend the previous explicit reversal into an isolated two-direction certificate
model. The negative-direction rule is the pullback of the positive-direction
rule through the tested involution. This deliberately constructs a consistent
dual description; its success is not independent evidence that the forward
rules were physically derived or uniquely selected.

The involution keeps cell coordinates fixed, exchanges P/E reader labels,
exchanges M/C roles, reflects occurrence indices i -> K-i, includes the context
slot using the previously found species-specific order, inverts coefficient
permutations, reverses edges and exchanges the complete entry/exit boundaries.

## Direction-dependent conditions

| Property | Forward convention | Reversed convention |
|---|---|---|
| PN face | 2 M vertices | 2 M vertices (from old NE) |
| NE face | 1 M vertex | 1 M vertex (from old PN) |
| NN face | 1 M vertex | 2 M vertices |
| Regular-only body role | P | E |
| Role allowing regular or split geometry | E | P |
| Neutron geometry | Split | Split |
| Boundary | One root, multiple E exits | All former exits as entries, former root as exit |

Each transformed frame passes the existing local template audit with the
context-aware ordering. Every transformed edge's complete inverse coefficient
map and reversed endpoints are retained. Global role consistency and actual
face geometry come from the source certificate, with the explicit reversed
face-role rule checked as well.

The dual validator requires that reversing the entire submitted certificate
recovers the exact independently source-audited forward certificate. It does
not accept arbitrary new backward maps or derive inverse transitions from
counts alone. Corrupting a coefficient permutation, changing a frame role or
collapsing the entry boundary is rejected.

## Results

| Source | Bodies P/N/E after reversal | Records | Contacts | Reversed entry records / bodies | Result |
|---|---|---:|---:|---|---|
| N-15 | 7/8/7 | 44 | 25 | 8 / 7 | Pass |
| N-14 experimental, delete 16 | 7/7/7 | 43 | 23 | 8 / 7 | Pass |
| N-14 experimental, delete 17 | 7/7/7 | 42 | 21 | 8 / 7 | Pass |
| O-16 | 8/8/8 | 49 | 28 | 9 / 8 | Pass |

Each reversed graph has one exit: the original root. All records are reachable
from its full entry boundary and can reach that exit. All four reversed NN
faces in each sample satisfy the direction-indexed condition. Reversing twice
restores the entire source certificate exactly, not merely its particle count.
No single reversed entry reaches all records (best is 18 in nitrogen and 14 in
oxygen). Multiple entry records can lie on one body; they are not extra particles.

## Interpretation

These examples admit internally consistent forward and reversed descriptions
when direction transforms the geometry-role convention, NN face convention and
boundary together. They are NOT closed under literal relabelling while keeping
all the original directional admission conditions fixed.

The N-14 examples already assume the experimental terminal PE shortcut. Duality
transports that assumption and does not derive it or independently solve N-14
under the original native grammar. The reverse of the PE edge is included only
as the inverse of its recorded composite map. This test does not implement the
prior research's dual/Riesz mode-plane identification or a new spatial duality.

Production, viewer selectors and existing receipts remain unchanged. A future
physical or representation-theoretic argument would need to select/justify
these direction-indexed conventions beyond the fact that pullback is consistent.

## Reproduction

```sh
node research/strominger/checkers/probe_dual_isotope_rules.mjs
```

Evidence: `results/dual-isotope-rules/verification.json`, including full reversed
certificates, negative controls, boundary counts and source hashes.
