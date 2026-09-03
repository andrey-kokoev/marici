# All-even Hessian transport

## Result

All 7,344 exact A12 Hessian words transport through the squared-axis embeddings.

- A14: 14,688 exact path replays, zero failures;
- A16: 29,376 exact path replays, zero failures;
- mixed A16 paths: 7,344 exact equalities.

Hessian interpolation commutes with the descriptor embeddings. The six tested components form a basis of the symmetric bilinear directions on the rational `(x,y,z)` space. Combined with parity-orbit induction, every raw Hessian row lies in the unchanged algebraic source image for every even ambient degree at least 12.

## Claim boundary

This is an exact algebraic second-derivative membership theorem. It does not define a second-order jet complex, connecting extension, admissibility rule, geometric comparison, or Bockstein.

## Verification

- `research/voevodsky/check_cosmology_second_jet_all_even_transport.py` — exit 0
- `research/voevodsky/results/cosmology_second_jet_all_even_transport.json`
