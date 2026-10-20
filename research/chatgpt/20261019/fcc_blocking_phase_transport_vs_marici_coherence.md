# FCC blocking-phase transport versus Marici eight-channel coherence

Date: 2026-10-19.

## Exact finite FCC calculation

Define L = {(x,y,z) in Z^3 : x+y+z even}, V=L/4Z^3 (32 elements), C=2L/4Z^3 (4 elements). Eight blocking-origin phases P=V/C. Gamma=V ⋊ C3 (order 96) acts transitively on P by translations and coordinate cyclic permutations. The stabilizer of C is C⋊C3 ≅ A4 (order 12), acting on the four coarse anchors as twelve even permutations. Exhaustive enumeration: `check_fcc_blocking_phase_transport.py`, output `fcc_blocking_phase_transport_results.json`.

Nerve of the action groupoid P//Gamma has homotopy type BA4. Accordingly pi1=A4, pi2=0, H1(Z)=C3, H2(Z)=C2 (Schur multiplier).

## Marici comparators

Ledger entry 069: the rank-two polarity carrier is homotopy equivalent to K_{2,12}, hence a wedge of 11 circles; pi1=F11, H1=Z^11. The separate quadrangulation compatibility cell complex is an RP2 cellulation, as detailed in ledger entry 019: pi1=C2, pi2=Z with sign action; H1=C2 and H2(Z)=0.

These are not homotopy equivalent to BA4. In particular no surjective homomorphism A4 -> C2 exists since A4_ab=C3, so a map BA4 -> RP2 cannot detect the nontrivial RP2 loop via pi1.

## Interpretation and limit

All eight Gaussian FCC blocking presentations are isomorphic via spatial translation (including boundary kernels and normalization), giving an equivariant coefficient family over P//Gamma. The univalent representation of *presentations* is hence governed by BA4. This does not define or compute a physically justified quotient: a physical readout, admissible comparison maps, and coherence cells beyond the symmetry groupoid must first be specified. The Marici quartic data are not canonically induced by FCC blocking phases.

Do not infer equality of physical quotients, or an obstruction to every possible enriched correspondence, from the mismatch of the bare carriers.

## Source links
- https://marici.narada.systems/ledger/20260813-69-full-core-suspension-and-the-two-axis-quadrangulation-carrier/
- https://marici.narada.systems/ledger/20260812-19-period-level-qtds-descent-and-the-eight-point-coherence-complex/
