# The arithmetic mesh carrier must be oriented, not unsigned incidence

The literal positive-region model assigns

\[
\Phi(D)_\alpha
=
\sqrt{c_\alpha}\mathbf1_{\alpha\in D},
\qquad c_\alpha>0,
\]

so every cross-pairing satisfies

\[
\langle\Phi(D),\Phi(E)\rangle
=
C(D\cap E)
\geq0.
\]

The computed source kernel at \(\sigma=0.005\), \(h=0.25\) has multiple negative off-diagonal values. Its primitive-increment kernel

\[
2K(mh)-K((m-1)h)-K((m+1)h)
\]

also has both signs.

Therefore the arithmetic observer cannot be represented by unsigned overlaps of positive causal regions, even if its complete Gram matrices are positive.

This does not obstruct a positive Hilbert carrier. Positive Gram matrices routinely have negative cross-inner-products. The mesh realization must retain orientation or phase:

\[
\Phi(D)_\alpha
=
s_D(\alpha)\sqrt{c_\alpha},
\qquad |s_D(\alpha)|=1,
\]

which gives

\[
\langle\Phi(D),\Phi(E)\rangle
=
\sum_\alpha
\overline{s_D(\alpha)}s_E(\alpha)c_\alpha.
\]

The diagonal remains positive while cross-pairings may be negative or complex.

This matches prior retained-carrier data such as the source orientation

\[
S_{12}=\operatorname{diag}(-1,+1).
\]

## Revised missing map

The arithmetic-to-mesh comparison must construct both positive cell weights and coherent orientation amplitudes:

\[
L(p_D^*p_E)
=
\sum_\alpha
\overline{s_D(\alpha)}s_E(\alpha)c_\alpha,
\qquad c_\alpha>0.
\]

An unsigned charge-overlap map is falsified. The first missing object is an oriented positive-mesh factorization whose phases are source-derived and satisfy forward/reverse incidence.

## Verification

```text
python research/voevodsky/checkers/check_unsigned_mesh_incidence_against_source_kernel.py
```

Artifacts:

- `research/voevodsky/checkers/check_unsigned_mesh_incidence_against_source_kernel.py`
- `research/voevodsky/results/unsigned_mesh_incidence_source_kernel_no_go.json`
