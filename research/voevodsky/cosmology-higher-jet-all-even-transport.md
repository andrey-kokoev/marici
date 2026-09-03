# All-even transport of higher-jet exactness

## Result

All order-three through order-six A12 memberships transport exactly to every even ambient degree at least 12.

The proof is structural. Squared-axis multiplication is independent of `(x,y,z)`, so it commutes with every derivative order. It maps source and target rows by the same descriptor shift and leaves rational word coefficients unchanged. Therefore exact words remain exact and raw zero rows remain zero.

The checker verifies:

- 35,024 A14 descriptor transports for the 17,512 nonzero words;
- 70,048 A16 descriptor transports;
- 17,512 mixed-path equalities;
- closure of every source and target descriptor in the appropriate ambient family.

The 73,064 raw-zero seed components transport to zero by the same injective row map. Parity-orbit induction covers every even degree. Orders above six vanish by interpolation degree.

## Claim boundary

This establishes raw derivative membership in the unchanged algebraic image. It does not provide a coherent primitive selector, higher-jet extension, admissibility rule, geometric comparison, or connecting morphism.

## Verification

- `research/voevodsky/check_cosmology_higher_jet_all_even_transport.py` — exit 0
- `research/voevodsky/results/cosmology_higher_jet_all_even_transport.json`
