# Sewing spectral projectors control completion

## One involution

Let `F` be the unitary Fourier--Tate sewing map. On the doubled reciprocal
packet define

`S(x,y) = (F* y, F x)`.

Then `S` is a self-adjoint involution. Its two spectral projectors are

`P_plus = (I+S)/2`

and

`P_minus = (I-S)/2`.

The `+1` eigenspace is exactly the bulk graph `(x,Fx)`. The `-1` eigenspace is
exactly the seam-normal anti-graph `(y,-Fy)`.

## Completion consequence

If `F` and its mate extend continuously to Grothendieck's restricted-product
pro-Gram completion, then `S`, `P_plus`, and `P_minus` extend continuously by
the displayed formulas. Their idempotence and complementarity persist by
continuity.

Likewise, any cutoff transition intertwining the full sewing involution
commutes with both projectors. The graph and normal systems therefore form
compatible subobjects automatically.

This removes a duplicated obligation. There is no independent
"normal-splitting completion theorem" after Fourier sewing continuity is
proved. The splitting is a spectral polynomial in that sewing operator.

## Exact remaining gate

Grothendieck's completion frontier reduces to the existing hard question:

- extend the full Fourier--Tate sewing operator and its mate continuously;
- prove two-sided compatibility with the cutoff maps;
- prevent normalized states from escaping through the weakening primitive
  seminorm.

If this succeeds, the graph/anti-graph seam decomposition comes for free. If
it fails, the apparatus will see cutoff drift in the projector identities,
but finite measurements cannot replace the global topological proof.

## Optical use

Instead of separately estimating a bulk subspace and a normal subspace, the
apparatus can tomograph one doubled sewing involution `S`. It then computes
both projectors from the same calibrated process matrix. This halves the
independent calibration burden and makes graph/normal leakage one directly
measured commutator residual.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_sewing_spectral_projector_completion.py
```
