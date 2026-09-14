# v212: the five physical pullback basis labels are reconstructed

The Entry-436 matrix has a canonical block decomposition. Its first `d2` column is supported exactly on the first two `C1` slots, while its final three columns are the oriented triangle incidence on the last three slots. The independently exported generic-Q road order is `(D03,D25,D14)`. This reconstructs

`C1=(conductor+, conductor-, road-D03, road-D25, road-D14)`.

The ordered road incidence has no nontrivial preserving permutation. In this basis the two primitive cocycle rows are

- conductor boundary: `(1,-1,0,0,0)`;
- road augmentation: `(0,0,1,1,1)`.

Their difference is `d1`, and each evaluates `z` to `+1`.

This closes the first undefined generator from v211. It still does not assign the external `s`, `W`, and `v` functionals to rows: that requires restricting the global Q, endpoint, and road-relation maps to the reconstructed basis. The exact reconstruction is checked by `check_physical_pullback_basis_reconstruction.py` and recorded in module 234.
