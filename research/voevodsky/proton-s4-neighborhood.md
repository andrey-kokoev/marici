# The S4 neighborhood of the retained proton-like package

## Focus and declared comparison

The focus is ledger 4314's 1836-arrow Merkle package, root `f7bd09c2a515ac4ac9f2bcb33105767c6ed8a4fcf93bdc1c22719228585c7e02`. Its exact coefficients, typed endpoints, owner attachments and pruning witness are freshly verified. No charge, mass or weak-interaction observable is supplied by this experiment.

The source natively uses the proper tetrahedral rotation group A4. We test two explicit extensions to S4. Neither extension is silently attributed to the source or selected as physical law.

The compared state is the complete labelled coefficient-arrow inventory, sorted canonically. Its Merkle content view does not include an extra marked vertex, action history or choice of group element. Transport witnesses retain those group elements separately. This distinction matters: different automorphisms can have the same state as their target.

## Action on geometry, ports and weights

For a vertex permutation p, the exact spatial matrix is

\[
R_p=\frac14\sum_{k=1}^{4}v_{p(k)}v_k^{T}.
\]

These are signed permutation matrices. Their determinant is +1 for even permutations and -1 for odd ones.

An even permutation maps an outer triangle label ab to p(a)p(b). An odd permutation maps it to p(b)p(a): reversing the endpoint order repairs the outward orientation after reflection. Without this repair, naive odd relabelling attaches triangles to the wrong retained parent-face sector.

Each spatial coordinate port moves under the corresponding signed coordinate permutation. A coefficient gets the product of its source and target coordinate signs. We then distinguish:

1. **Linear extension:** apply the signed permutation without complex conjugation.
2. **Parity-semilinear extension:** additionally conjugate coefficients for odd p.

Conjugation sends a+b sqrt(-3) to a-b sqrt(-3). The rule is explicit in every action witness. On a local triangle, exchanging the two outer vertices exchanges the two nonreal cyclic phases, which explains why conjugation enters the orientation-repaired comparison.

## Computed neighborhood

| Convention / observable | Orbit size | Stabilizer size | Adjacent-transposition effect |
| --- | ---: | ---: | --- |
| Linear action on the unmarked coefficient state | 2 | 12 | All three generators reach the same complex-conjugate presentation |
| Parity-semilinear action on that state | 1 | 24 | All three generators are automorphisms returning to the focus view |
| A marked geometric corner alone | 4 | 6 | Permutations move the marker among four corners; not four particle states |

The three tested adjacent transpositions are (AB), (BC), and (CD). They remain three distinct action witnesses even when their target content hashes coincide. In the linear convention, the two coefficient-view roots are:

```text
focus:      bd0054a4c74f3cd559196be2895bf027eb2569d116e074ea256bbb40e3e7a126
conjugate:  5045076c9a79e0b2b04d6709ace63ac5541138e15c74feecaf27db15663ff858
```

All even permutations stabilize the focus. All odd linear images equal its exact complex conjugate. Adding odd conjugation makes every S4 image equal the original coefficient state. Thus there are not 24 distinct coefficient states merely because S4 has 24 elements.

These are distinct or coincident labelled presentations under declared actions, not an identification of neutron, electron, neutrino or antiparticle sectors. In particular, complex conjugation alone is not a verified charge-conjugation operation here.

## Verification and preservation

All 17 checks passed:

- the source operator and fixed-weight pruning certificate reverify;
- all 24 matrices have the expected determinant;
- parent-face ownership is preserved after orientation repair, and naive odd relabelling fails that test;
- all 576 group products act correctly, with coordinate signs, on all 108 typed ports; conjugation parity composes correctly;
- all three generators square to identity in both conventions;
- the two orbit/stabilizer computations agree exactly with 24 divided by stabilizer size;
- the positive closed-cycle weight multiset is preserved;
- the conjugate presentation independently passes the full operator/pruning verifier;
- distinct generator witnesses are retained;
- removing the required conjugation flag and honestly rehashing the witness is rejected;
- serialized neighborhood verification repeats the result.

The source's 1836-arrow support and fixed-weight pruning property survive the transformations. This does not show that a proton has physically transformed into anything else. A particle-transition graph would additionally need charge and energy observables, interaction maps and conservation witnesses.

## Artifacts and replay

```text
python research/voevodsky/checkers/check_proton_s4_neighborhood.py
python research/voevodsky/checkers/check_proton_s4_neighborhood.py --verify research/voevodsky/results/proton_s4_neighborhood_store.json
```

- `research/voevodsky/results/proton_s4_neighborhood.json`: orbit results, generator targets, tests and fingerprints.
- `research/voevodsky/results/proton_s4_neighborhood_store.json`: retained focus package, two coefficient-state objects and 48 exact action witnesses (24 for each convention).
- `research/voevodsky/checkers/check_proton_s4_neighborhood.py`: exact constructor and verifier.

The next discriminating model choice is which observable, marking or interaction distinguishes proposed physical sectors. The current unmarked semilinear orbit provides automorphisms, not a neutron neighbour.
