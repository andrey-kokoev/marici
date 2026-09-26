# Seven-point NNMHV parity reproduction: completed computational example

## Result

The complete seven-point NNMHV tree superamplitude from the six-term sourced recursion equals the Grassmann-Fourier parity transform of the six-term NMHV amplitude as a rational identity on a regular, six-independent-modulus momentum-twistor chart. Parke-Taylor/MHV prefactors and Fourier complement signs are retained. The universal momentum delta, coupling normalization and shared overall amplitude phase are consistently stripped.

This completes the agreed example: reproduce the established seven-point amplitude with an independent parity comparison. It does not complete the parked nine-point geometric-contour derivation.

## Fresh reproducibility closure

Run:

`uv run --with sympy --with python-flint python research/voevodsky/checkers/check_seven_point_parity_suite.py`

A fresh run passed all six stages in236.731 seconds:

1. Six independent projective kinematic moduli, with nonzero invariant Jacobian.
2. Universal Ward-space basis, dimension3, with336 symbolic Ward checks.
3. Reconstructed all12 generic direct/parity terms from source utilities; verified termwise Ward membership over the six-variable rational field.
4. Proved all15 reduced quartic parity identities using exact integer polynomial arithmetic, with --fresh disabling cached identities.
5. Complete-tensor comparison at two rational inputs, covering35^4 coefficients per input and omitted-term negative controls.
6. Independent kinematics-only Ward embedding of all12 rational term vectors and their reduced parity identities.

`results/seven-point-parity-suite.json` records stage artifact digests, source hashes (including the primary recursion source), package versions, timing and scope. The generic constructor now has a clean successful construction status; it no longer attempts the obsolete slow monolithic quartic simplification. The quartic checker verifies constructor source freshness and binds the generated term artifact by hash. The suite rejects source changes during the run.

## Why fifteen identities suffice

For one flavor, Q and anti-Q constraints restrict the four-form to L1 wedge L2 wedge Lambda^2(ker R/span L), dimension3. Components1234,1235,1245 form coordinates on the regular spinor-frame open. Each superamplitude term is a scalar times the fourth tensor power of its single-flavor vector. Equality therefore reduces to the15 coefficients of a symmetric quartic in three coordinates. All were proved zero as generic rational functions, not inferred from numerical samples.

## Interpretation and limits

This is a reproducible exact computational algebra result using the published tree-recursion conventions in arXiv:0808.2475. It is not a proof-assistant formalization, an independent derivation of super-BCFW recursion, or a positive-cell coverage/contour proof. Generic equality is on a specified regular chart; standard covariance/projective interpretation relates equivalent generic descriptions. Rational continuation does not assign finite values at poles.

A separate positive-cell realization of the six histories, or the one-loop four-mass box, would be new follow-on objectives rather than unfinished parts of this parity-reproduction task.
