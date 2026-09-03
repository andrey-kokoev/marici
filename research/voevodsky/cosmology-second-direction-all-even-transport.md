# All-even transport of second-direction certificates

## Result

All 1,224 exact A12 second-tangent words were transported through the squared-axis maps.

- A14: 2,448 exact path replays, zero failures;
- A16: 4,896 exact path replays, zero failures;
- mixed A16 paths: 1,224 exact equalities.

The replay uses four-prime CRT reconstruction of integer rows followed by exact rational evaluation. Descriptor transport preserves source kinds and coefficients, and the established parity-orbit induction covers every even ambient degree at least 12.

The tangent lattice of `dp=(1,1,3)` is generated integrally by `(1,-1,0)` and `(3,0,-1)`. Both tangent derivative classes vanish, as does the `nx` class. Therefore every integral unit normal in the affine torsor `dp(n)=1` gives the same zero algebraic quotient class for every even ambient degree at least 12.

## Claim boundary

This is normal-choice independence in the labelled algebraic relation presentation. It does not construct a geometric normal bundle, DNC filtration, supported specialization, exceptional Bockstein, or physical class.

## Verification

- `research/voevodsky/check_cosmology_second_direction_all_even_transport.py` — exit 0
- `research/voevodsky/results/cosmology_second_direction_all_even_transport.json`
- source words: `cosmology_second_direction_exact_certificate_words.json` and `cosmology_second_direction_local_exact_words.json`
