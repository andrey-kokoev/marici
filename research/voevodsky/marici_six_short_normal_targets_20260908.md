# Full six-short-normal family of strict conductor targets

Date: 2026-09-08

## Result

Use the source ordering

\[
(X_0,X_2,X_4;X_1,X_3,X_5)
=(02,04,24;13,15,35).
\]

For every short normal

\[
k\in\{02,04,24,13,15,35\},
\]

transport the certified conormal extension to a two-state object with basis `u_k,v_k`:

\[
X_k u_k=\beta v_k,
\qquad X_kv_k=0,
\qquad \pi_k(u_k)=1,
\qquad \pi_k(v_k)=0.
\]

All other short coordinates act by zero in this retained coefficient model. Define

\[
D_k=\operatorname{holim}
\left(
\omega[2]\xrightarrow q C\Pi^\vee[3]
\xleftarrow{\pi_k}E_{\beta,k}\Pi^\vee[3]
\right).
\]

The same strict 50-state conductor map `q` works for every `k`. Since `d_E=0`, `pi_k` is a chain map, and the already checked equation `q d_omega=0` proves all six pullback differentials square to zero.

## Dihedral organization

Rotation has cycles

\[
02\to04\to24\to02,
\qquad
13\to15\to35\to13.
\]

Reflection pairs are

\[
02\leftrightarrow13,
\qquad04\leftrightarrow35,
\qquad24\leftrightarrow15.
\]

The checker verifies `r^3=s^2=1` and `srs=r^{-1}` on all six labels.

## Joint marked detector

Before forgetting normal labels, the six kernel generators

\[
(v_{02},v_{04},v_{24},v_{13},v_{15},v_{35})
\]

have their six coordinate detectors. Their matrix is `I_6`, hence has rank six. Thus the full marked short-normal family is jointly separating on the direct sum of its declared kernel lines; no one normal is privileged at target level.

This rank statement is deliberately scoped. It concerns the marked conormal kernel object, not the entire admissible RH source or completed analytic carrier.

## Remaining source transport

The complete framed spatial maps have so far been independently compiled only for the reflected pair `35/04`. Target relabelling proves existence and covariance of the other four strict pullback objects, but it does not by itself transport the complete framed source maps. That next step must rotate:

- the physical source labels;
- the subsets `T`;
- determinant and polarity lines;
- support ideals and Cech maps;
- operation and antipode data.

Only after that transport can the six-normal family be claimed jointly detecting on the spatial or RH source.

## Verification

```sh
python research/voevodsky/check_marici_six_short_normal_targets_20260908.py \
  --root . \
  --output research/voevodsky/marici_six_short_normal_targets_certificate_20260908.json
```

The checker performs 39 exact structural and dihedral assertions.
