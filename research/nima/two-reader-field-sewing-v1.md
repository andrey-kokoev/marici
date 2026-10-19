# Two-reader field attachment: routes agree, geometric sewing remains open

## Result

Strominger's declared candidate is consistent on the saved two-reader materialization experiment **at the whole-reader transport level**. Both direct terminal-PE transports equal their selected PN→NE replacements; all retained readers keep the same candidate field map across the batch.

This does not establish a field on the tessellation. Geometric restriction maps to shared face patches and a common seam comparison have not been supplied.

## Exact test fixture

The certified initial selection contains8 reader records. Its atomic materialization adds neutron readers6 and51 on body2, producing10 records. Adding either reader alone loses rootedness; the tested change remains a two-reader atomic operation.

| Configuration | Selected interfaces | Outside representative tree | Occupied face contacts |
|---|---:|---:|---:|
|Initial|9|2|2|
|Final|13|4|6|

The test checks every selected interface, not only the construction tree, and checks the native witness equations at every occupied contact. It preserves all five coefficient permutations and absolute origins.

## Candidate and verification method

The declared attachment uses the saved global metric-unitary PN map/inverse, geometric P-reader rotation, co-moving identity N/NN transport, and fixed contrast-to-E map. PE field transport is **defined here by composition** of PN and NE, so its direct/factored equality is not independent evidence for a physical PE law. The additional checks concern compatibility with the other selected reader routes and contacts.

The initial dense exact computation exceeded180 seconds. The successful checker instead uses the saved unitary PN identity and the candidate's common-frame normal form. It freshly computes the small contrast projection

`V = K* M_N PN UP^q BP`

from the saved full PN matrix. Here BP is the root five-column binding, UP the P-reader rotation, q its parity and K the orthonormal neutron contrast frame. All arithmetic is exact rational/multiradical; no floating-point rank threshold is used. Both tested routes have q=1.

The source hash chain is checked. Saved PN metric unitarity and the chosen co-moving transport conventions are reused assumptions/results; the dense inverse product and all source-owner suites were not rerun. Source-owner files and receipts are unchanged.

## The channel accounting survives this transport

For both routes P2→E8 and P20→E53:

- electron block rank: **2**;
- retained baryon block rank: **3**;
- joint input rank: **5**;
- electron Gram matrix is a rank-two projector;
- electron and residual Gram matrices sum exactly to the5-dimensional identity.

The residual is retained as the factorized reference field

`(I - K K* M_N) PN UP^q BP`.

Before the batch, it is reference-fiber data—not occupied neutron matter. After materialization, the corresponding native neutron reader carries the pre-exchange baryon field. Occupancy and field accounting have not been equated.

The residual rank is checked using the exact2-by-2 reduction `I2 - V V*`: for a five-isometric input its rank is `3 + rank(I2 - V V*)`. Here that reduction vanishes, giving3. Electron rank is checked by exact minors.

## Two outputs do not automatically mean independent channels

Both PE routes start with the **same five-component root input** and reach the same common field frame. Their8-by-5 electron maps are exactly equal. Stacking the two maps therefore still has rank2, not4; their residual maps agree in the common reference frame as well.

This is a correlation statement under the declared common input. It does not forbid independent site preparations. It says those independent inputs, tensor factors or extra boundary data must actually be supplied; different bodies, origins or histories alone did not create them in this test. No sum of these duplicated field evaluations is called a conserved physical energy.

## What remains missing

A native face witness identifies a valid transfer route, but the global PN map mixes beyond one face. Checking that map across an occupied contact is not the same as matching geometric field values on that contact.

The next required data are:

1. restrictions from P/N/E carrier fields to each shared geometric face or edge;
2. typed seam comparison maps between those restrictions, with the metrics retained;
3. consistency of several reader descriptions on a shared body;
4. a declaration of shared versus independently prepared body inputs.

Until these are supplied, the result is **candidate route compatibility with geometric sewing unresolved**. No occupancy rule, generator, production admission or viewer behavior changed.

## Cross-owner review: a stronger geometric requirement is already obstructed

At the review boundary, Strominger's event16192 supplied a newer [rotation/realization result](../strominger/rotation-realization-square-v1.md). For every metric-unitary PN map exchanging the named L/G projectors, requiring the independently defined geometric C3 actions as well gives a rank-two relative-sector discrepancy. In his notation, `E^sharp E = 3(G_P-N_P)` while `N_N E = 0`: return-only observation hides the discrepancy.

That result was read and its receipt is pinned here, not freshly rerun by this experiment. It does not contradict our fixed-route agreement: our candidate uses the declared co-moving transport convention, and we did not impose the additional named geometric-C3 square. It does rule out promoting this result to that stronger equivariant sewing claim. Merely choosing another PN complement within the same projector-role-exchanging class cannot remove his universal obstruction. A future seam specification must say which geometric actions it retains and must not erase the relative sector just to make the square pass.

## Controls and reproduction

Three fixed-equation controls detect a changed coefficient permutation, a phase flip on only one competing route, and loss of the three-channel residual. They are not an independent review of the entire candidate.

```sh
python research/nima/checkers/check_two_reader_field_sewing.py
python research/aspect/scc/scc.py check two-reader-field-sewing
```

[Prospective protocol](two-reader-field-sewing-protocol-v1.md) · [Exact receipt](results/two-reader-field-sewing/verification.json) · [Source-replayed fixture](results/two-reader-field-sewing/fixture.json)
