# v211: target detector reconstruction stops at the unlabeled C1 basis

A source audit of `check_physical_derived_pullback_after_transform.py` finds that Entry 436 exports the three differential matrices, the primitive vector `z`, and the road augmentation, but not the semantic labels of the five `C1` basis vectors. It also exports no `s`, `W`, or `v` detector row.

The reported generic-Q and Cartier values are literal status outputs after the homology calculation; in this executable they are not computed as target cochain rows evaluated on `z`. Therefore those values cannot be used to reconstruct the missing cross-target maps. Doing so would repeat the scalar-signature identification rejected earlier.

The labelled reconstruction stops at its first undefined generator:

`c1_basis_labels`.

After those five labels are supplied, the exact next test is immediate: construct each target detector row, verify it annihilates all four columns of `d2`, and evaluate it on `z`. The machine-readable audit is `results/physical-pullback-target-detector-input-gate.json`; module 233 records the gate.
