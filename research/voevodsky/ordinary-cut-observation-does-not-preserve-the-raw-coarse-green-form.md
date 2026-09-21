# Ordinary cut observation does not preserve the raw coarse Green form

## Exact hostile

The maps in `ordinary-coarse-cut-maps-descend-to-the-common-observation.md` retain cut labels in orthogonal target blocks. That target pairing is not automatically the pullback of the raw single-seam derivative pairing.

Use four distinct event indices 0,1,2,3, all marks forgotten, and set

    u = r0(0,1) path(2,3),
    v = r0(0,2) path(1,3).

Under the actual path derivative with terminal histories, the suffix contributions cancel, leaving the respective first-diamond cycles. Their only shared edge coordinate is root -> {0}, with coefficient +1 in each. All histories are vacuum and the seam letter is Omega. The prescribed orthogonal edge form with unit vacuum/Omega therefore gives

    q(Du,Dv) = 1.

Their first two-event cuts, {0,1} and {0,2}, are distinct. The cut-defined target makes these summands orthogonal, so its pairing of their images is zero. No theta approximation, spectral normalization, or memory weight enters this discrepancy.

Tensor both vectors with the same final forgotten relation on two further events. Its derivative norm is four, so the corresponding six-event coarse cross entry is four, whereas the orthogonally labelled three-block target still gives zero (times the common root pairing).

## Interpretation

This refutes isometry between the raw derivative coarse form and this orthogonal refined target. It does NOT refute equality of the two cut-defined observations in their common target, and it does not establish a discrepancy for every possible independently prescribed coarse form.

The raw derivative kills the four tested two-relation products; quotient descent is not the obstruction exhibited here. The obstruction is loss of cross-cut pairings when replacing a shared coarse edge carrier by orthogonal cut labels.

## Next gate

Identify which coarse form is actually intended. If it is the raw derivative form, compute the full cross-cut Gram transport rather than declaring distinct cut labels orthogonal. Such a transport is an additional target pairing to justify from the existing coarse assembly, not a fitted positive relation metric. Then compare left and right induced forms on the common ordinary sector. If a different coarse assembly is prescribed, document its cut orthogonality before claiming isometry.

Verification: `uv run --with sympy python research/voevodsky/checkers/check_coarse_derivative_green_descent_obstruction.py`. The fixture checks the actual source derivatives, four product vanishings, and the exact cross entry 1 versus 0. It does not compute the full ordinary Green matrix.
