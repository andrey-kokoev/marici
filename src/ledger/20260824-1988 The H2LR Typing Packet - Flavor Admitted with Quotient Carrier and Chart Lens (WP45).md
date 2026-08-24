---
author: marici.Figueiredo
---

# 1988 - The H2LR Typing Packet: Flavor Admitted with Quotient Carrier and Chart Lens (WP45)

The brief's sixth work package: assemble the source-derived package
(F, K_flavor, O_flavor, <-,->_flavor) and test whether it descends through
every equivalence class the flavor problem declares. It does (6/6 gates),
and flavor is admitted as a fourth Marici sector - with a specific typing
that WP11 forced and WP44 completed.

## The admitted package

  carrier  F     = {(Yu, Yd)} / U(3)^3 - the physical flavor quotient
  lens     K     = sparse nine-link chart atlas: 9 edge magnitudes per pair
                   + loop U(1) holonomy
  readout  O     = observables17: 6 quark masses, 6 |V_ij|, 3 unitarity
                   angles, 2 light-mass ratios
  pairing  <-,-> = the WP44 gap-cancelled law:
                   C_anchor = (block gap) Dd (CKM monomial)
                              / (scale^2 |Hd_02|^2 |Hd_12|)

## Gate results (checkers/wp45_h2lr_typing.py, 6/6)

  G1 full U(3)^3 quotient: obs17 invariant under random basis change,
     1.1e-10 per-coordinate relative.
  G2 chart groupoid (rephasings + permutations): 6.7e-12.
  G3 fiber compatibility: charts land inside experimental fibers,
     max pull 1.60 sigma.
  G4 CP conjugation: exact (masses/|V| identical, angles reflected).
  G5 pairing factorization: WP44 law re-verified, n = 394, 2.7e-11.
  G6 lens vs readout: phi std 19.86 deg vs gamma std 0.13 deg, ratio 152.5.

## What the typing settles

- The nine-link graph is NOT the carrier (WP11); it is the lens. The
  carrier is the physical U(3)^3 quotient, and the sparse textures are its
  chart atlas.
- phi and the Yukawa triangle are internal lens coordinates; only their
  CKM image is readout. G6 makes the split quantitative: the lens
  coordinate is two orders of magnitude more volatile than the readout it
  feeds.
- The anchor constants are point values through exact chart algebra (WP44),
  evaluated at the physical flavor point; the pairing is exact on the
  Hd_01 = 0 family and certified not to extend universally.
- Consequently the pi/8 clustering is lens-level phenomenology. After
  WP11 + WP45 it cannot be promoted to a physical law except through a
  pushforward into the weak-basis invariant ring - which remains the one
  open route (Nima's harmonic-support question) and is explicitly not
  claimed here.

## Methods note (load-bearing for future gates)

Invariance was gated on per-coordinate relative error with masses from a
direct SVD of Y. The naive route (eigh on H = Y Y^dagger, absolute
comparison) fails G1/G2 at ~3e-6 purely from the eps ||H||/lambda_min
conditioning floor on the light masses - an algorithm artifact, not
physics. Recorded in flavor-h2lr-typing-packet.md so no future checker
rediscovers it as a fake symmetry violation.

## Status vs the brief's admission criterion

The criterion asked for a source-derived package whose essential components
descend through the appropriate equivalences. Established: carrier descent
(G1), chart-groupoid descent (G2), physical fibers (G3), CP (G4), exact
pairing (G5), and the lens/readout separation (G6). Flavor is admitted.
The remaining cross-sector step - comparing structural operations to the
string/scattering/cosmology sectors before any H2S parent-object claim -
is a separate work package and per the brief comes only after this packet,
which is now in place.

Evidence: research/flavor/checkers/wp45_h2lr_typing.py,
research/flavor/results/wp45_h2lr_typing.json,
research/flavor/flavor-h2lr-typing-packet.md.
